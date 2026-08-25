"""
Resize-stable glass navbar (TrafficAI theme).

- Flex nowrap + media queries: window chhota/bada karne par layout shift nahi hota,
  menu hamesha ek hi row mein dikhta hai (bade pe jaisa, chhote pe waisa).
- Chhoti screen par labels chhup kar icon-only pills ban jate hain.
- Bahut narrow ho to row scroll ho jati hai (tooti hui layout kabhi nahi).
- State: hidden radio (key="nav") + JS bridge — wahi pattern jo app.py use karta hai.

Usage:
    selected = navbar()
"""

import streamlit as st
import streamlit.components.v1 as components

PAGES = ["Dashboard", "Detect", "History", "Profile", "Settings"]
NAV_ICONS = {
    "Dashboard": "fa-house",
    "Detect": "fa-camera",
    "History": "fa-clock",
    "Profile": "fa-user",
    "Settings": "fa-gear",
}

NAVBAR_HTML = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<style>
    /* Underline / bottom-border fix */
    .stable-nav a,
    .stable-nav a *,
    .stable-nav a:hover,
    .stable-nav a.active,
    .stable-nav a.active * {
        text-decoration: none !important;
        border-bottom: none !important;
    }

    /* Main row: kabhi wrap nahi hoga */
    .stable-nav {
        display: flex;
        flex-wrap: nowrap;
        align-items: center;
        gap: 3px;
        padding: 4px;
        margin: 0;
        width: 100%;
        background: rgba(201, 24, 74, 0.08);
        border: 0.5px solid rgba(201, 24, 74, 0.2);
        border-radius: 14px;
        overflow-x: auto;   /* bahut narrow -> scroll, layout toota nahi */
        scrollbar-width: thin;
        white-space: nowrap;
    }

    .stable-nav a {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        flex: 0 0 auto;     /* pill kabhi shrink nahi hogi */
        padding: 9px 16px;
        font-size: 15px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.78);
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .stable-nav a:hover {
        background: rgba(255, 255, 255, 0.15);
        color: #fff;
    }

    .stable-nav a.active {
        background: rgba(201, 24, 74, 0.2);
        border-color: #C9184A;
        color: #fff;
    }

    .stable-nav a i {
        font-size: 18px;
        color: #938D8F;
    }

    .stable-nav a.active i {
        color: #fff;
    }

    /* Chhoti window: labels chhupao, sirf icons — row waise hi rahegi */
    @media (max-width: 720px) {
        .stable-nav a { padding: 9px 12px; }
        .stable-nav a .nav-label { display: none; }
    }
</style>

<nav class="stable-nav">
    {links}
</nav>

<script>
(function () {
    var parent = window.parent;
    if (!parent || !parent.document) return;

    /* Sab radios dhundho - light DOM + shadow DOM dono mein (naye Streamlit versions) */
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

    /* Sirf PEHLA radio (nav wala) hide karo - page ke doosre radios visible rahenge */
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

    /* Nav click -> matching hidden radio click */
    function clickNavRadio(pageName) {
        var radios = findRadios(parent.document);
        if (!radios.length) return;
        var labels = radios[0].querySelectorAll('label');
        for (var j = 0; j < labels.length; j++) {
            if ((labels[j].textContent || '').trim() === pageName) {
                var input = labels[j].querySelector('input');
                if (input) input.click(); else labels[j].click();
                break;
            }
        }
    }

    var nav = document.querySelector('.stable-nav');
    if (nav) {
        nav.addEventListener('click', function (e) {
            var btn = e.target.closest ? e.target.closest('.stable-nav a') : null;
            if (!btn) return;
            e.preventDefault();
            var pageName = btn.getAttribute('data-page');
            if (pageName) clickNavRadio(pageName);
        });
    }

    /* 1) Turant hide */
    hideNavRadio();

    /* 2) MutationObserver - radio baad mein render ho to bhi hide ho jayega
       (Community Cloud slow load fix) */
    if (parent.__tsrObs) parent.__tsrObs.disconnect();
    try {
        parent.__tsrObs = new MutationObserver(function () { hideNavRadio(); });
        parent.__tsrObs.observe(parent.document.body || parent.document.documentElement, { childList: true, subtree: true });
    } catch (e) {}

    /* 3) Fallback polling */
    if (!parent.__tsrNavTimer) {
        parent.__tsrNavTimer = setInterval(hideNavRadio, 400);
    }
})();
</script>
"""


def navbar():
    # Current page = hidden radio ka session value
    current = st.session_state.get("nav", st.session_state.get("current_page", "Dashboard"))
    if current not in PAGES:
        current = "Dashboard"

    links = "".join(
        f'<a class="nav-btn{" active" if p == current else ""}" data-page="{p}">'
        f'<i class="fa-solid {NAV_ICONS[p]}"></i><span class="nav-label">{p}</span></a>'
        for p in PAGES
    )

    # Hidden radio = single source of truth (JS ise click karta hai)
    page = st.radio(
        "",
        PAGES,
        horizontal=True,
        index=PAGES.index(current),
        key="nav",
        label_visibility="collapsed",
    )

    # Nav render: HTML + CSS + click bridge ek saath
    components.html(NAVBAR_HTML.replace("{links}", links), height=70)

    return page