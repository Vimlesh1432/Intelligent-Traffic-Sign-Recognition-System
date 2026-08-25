import streamlit as st
import streamlit.components.v1 as components

from config import (
    APP_NAME,
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from database import create_database

from components.theme import apply_theme

from views.dashboard import dashboard
from views.detect import detect
from views.history import history
from views.profile import profile
from views.settings import settings
from utils.helpers import load_css

# ----------------------------
# JS Bridge - nav click ko hidden radio click me convert karta hai.
# Koi URL change nahi hota, isliye naya window/login page nahi khulta.
# ----------------------------
NAV_BRIDGE_JS = """
<script>
(function () {
  var parent = window.parent;
  if (!parent || !parent.document) return;

  // Sab radios dhundho - light DOM + shadow DOM dono mein (naye Streamlit versions)
  function findRadios(root) {
    var found = [];
    var list = root.querySelectorAll('[data-testid="stRadio"]');
    for (var i = 0; i < list.length; i++) found.push(list[i]);
    var hosts = root.querySelectorAll('*');
    for (var j = 0; j < hosts.length; j++) {
      var sr = hosts[j].shadowRoot;
      if (sr) found = found.concat(findRadios(sr));
    }
    return found;
  }

  // Sirf PEHLA radio (nav wala) hide karo - Detect page ka radio visible rahega
  function hideNavRadio() {
    var radios = findRadios(parent.document);
    if (!radios.length) return;
    var r = radios[0];
    r.style.position = 'absolute';
    r.style.opacity = '0';
    r.style.pointerEvents = 'none';
    r.style.height = '0';
    r.style.overflow = 'hidden';
  }

  function clickNavRadio(pageName) {
    var radios = findRadios(parent.document);
    if (!radios.length) return;
    var labels = radios[0].querySelectorAll('label');
    for (var i = 0; i < labels.length; i++) {
      if ((labels[i].textContent || '').trim() === pageName) {
        var input = labels[i].querySelector('input');
        if (input) { input.click(); } else { labels[i].click(); }
        break;
      }
    }
  }

  function handleClick(e) {
    var el = e.target;
    var btn = el && el.closest ? el.closest('.nav-btn') : null;
    if (!btn) return;
    e.preventDefault();
    var pageName = btn.getAttribute('data-page');
    if (pageName) clickNavRadio(pageName);
  }

  // 1) Turant hide
  hideNavRadio();

  // 2) MutationObserver - radio baad mein render ho to bhi hide ho jayega.
  //    Community Cloud par load slow hai, isliye script radio se pehle chal
  //    jaati thi aur radio dikhne lagta tha - yahi bug tha.
  if (parent.__tsrObs) parent.__tsrObs.disconnect();
  try {
    parent.__tsrObs = new MutationObserver(function () { hideNavRadio(); });
    parent.__tsrObs.observe(parent.document.body || parent.document.documentElement, { childList: true, subtree: true });
  } catch (e) {}

  // 3) Fallback polling (agar MutationObserver unsupported ho)
  if (!parent.__tsrNavTimer) {
    parent.__tsrNavTimer = setInterval(hideNavRadio, 400);
  }

  // Click bridge sirf ek baar bind karo (har rerun par naya iframe banta hai)
  if (!parent.__tsrNavBound) {
    parent.__tsrNavBound = true;
    parent.document.addEventListener('click', handleClick, true);
  }
})();
</script>
"""

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
)

load_css("assets/css/style.css")
apply_theme()

# ----------------------------
# Create Database
# ----------------------------

create_database()

# ----------------------------
# Navigation State
# ----------------------------

PAGES = ["Dashboard", "Detect", "History", "Profile", "Settings"]
NAV_ICONS = {
    "Dashboard": "fa-house",
    "Detect": "fa-camera",
    "History": "fa-clock",
    "Profile": "fa-user",
    "Settings": "fa-gear",
}

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# True current page = hidden radio ka session value (key="nav"),
# warna pehla load par current_page — isse active pill kabhi lag nahi karegi
current = st.session_state.get("nav", st.session_state.get("current_page", "Dashboard"))
if current not in PAGES:
    current = "Dashboard"
st.session_state.current_page = current

# ----------------------------
# Glassmorphism header: logo left + nav right
# ----------------------------

st.markdown(
    f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <style>
        /* ---- Underline fix: header ke har element se underline / bottom border hatao ---- */
        .app-header a,
        .app-header .nav-btn,
        .app-header .nav-btn *,
        .app-header .brand,
        .app-header .brand * {{
            text-decoration: none !important;
            border-bottom: none !important;
        }}
        .app-header a:hover,
        .app-header .nav-btn:hover,
        .app-header .nav-btn.active,
        .app-header .nav-btn.active * {{
            text-decoration: none !important;
            border-bottom: none !important;
        }}
    </style>
    <div class="app-header">
        <div class="brand">
            <span class="brand-logo">🚦</span>
            <span class="brand-name">Traffic<span>AI</span></span>
        </div>
        <nav class="header-nav">
            {''.join(
                f'<a class="nav-btn{" active" if p == current else ""}" '
                f'href="#" data-page="{p}" style="text-decoration: none !important;">'
                f'<i class="fa-solid {NAV_ICONS[p]}"></i><span class="nav-label">{p}</span></a>'
                for p in PAGES
            )}
        </nav>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- Hidden radio (page state) - JS ise click karta hai ----
page = st.radio(
    "",
    PAGES,
    horizontal=True,
    index=PAGES.index(current),
    key="nav",
    label_visibility="collapsed",
)
st.session_state.current_page = page

# ---- JS bridge (invisible) ----
components.html(NAV_BRIDGE_JS, height=0)

# ----------------------------
# Page routing
# ----------------------------

if page == "Dashboard":
    dashboard()
elif page == "Detect":
    detect()
elif page == "History":
    history()
elif page == "Profile":
    profile()
elif page == "Settings":
    settings()