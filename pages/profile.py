import streamlit as st

from database import (
    get_total_predictions,
    get_today_predictions,
    get_average_confidence,
    get_best_prediction,
    get_top_signs,
)

def profile():
    # --- Fetch Logic (no user_id now) ---
    total = get_total_predictions()
    today = get_today_predictions()
    accuracy = get_average_confidence()
    best = get_best_prediction()
    top = get_top_signs()

    # Adaptive Header (Mobile pe stack, Desktop pe side-by-side)
    h_left, h_right = st.columns([1, 3])

    with h_left:
        st.markdown("""
            <div style="text-align: center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
                     style="width: 140px; border-radius: 50%; border: 3px solid rgba(255,255,255,0.2); background: rgba(255,255,255,0.05);">
            </div>
        """, unsafe_allow_html=True)

    with h_right:
        st.markdown("""
            <div style="text-align: left; padding: 10px;">
                <h1 style="margin:0; font-weight:800; color:white;">Traffic Sign Analyst</h1>
                <p style="margin:0; opacity:0.6; font-size:16px;">Local AI Detection Profile</p>
                <div style="margin-top:15px;">
                    <span style="background:rgba(59, 130, 246, 0.2); padding:5px 12px; border-radius:8px; font-size:12px; color:#60a5fa; border:1px solid rgba(59, 130, 246, 0.3); margin-right:5px;">🤖 AI User</span>
                    <span style="background:rgba(34, 197, 94, 0.2); padding:5px 12px; border-radius:8px; font-size:12px; color:#4ade80; border:1px solid rgba(34, 197, 94, 0.3); margin-right:5px;">🚦 Expert</span>
                    <span style="background:rgba(255,255,255,0.1); padding:5px 12px; border-radius:8px; font-size:12px; color:white; margin-right:5px;">📅 Joined 2026</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # ================= 2. Stats Grid (Adaptive 4 Columns) =================
    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown(f'<div class="card" style="text-align:center; padding:15px;"><p style="margin:0; font-size:12px; opacity:0.6;">TOTAL</p><h2 style="margin:0;">{total}</h2></div>', unsafe_allow_html=True)
    with s2:
        st.markdown(f'<div class="card" style="text-align:center; padding:15px;"><p style="margin:0; font-size:12px; opacity:0.6;">TODAY</p><h2 style="margin:0;">{today}</h2></div>', unsafe_allow_html=True)
    with s3:
        st.markdown(f'<div class="card" style="text-align:center; padding:15px;"><p style="margin:0; font-size:12px; opacity:0.6;">ACCURACY</p><h2 style="margin:0;">{accuracy}%</h2></div>', unsafe_allow_html=True)
    with s4:
        best_val = f"{best['confidence']*100:.1f}%" if best else "0%"
        st.markdown(f'<div class="card" style="text-align:center; padding:15px;"><p style="margin:0; font-size:12px; opacity:0.6;">BEST</p><h2 style="margin:0;">{best_val}</h2></div>', unsafe_allow_html=True)

    # ================= 3. Activity & Achievements =================
    left, right = st.columns([2, 1])

    with left:
        # Best Prediction Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🚦 Best Achievement")
        if best:
            st.success(f"""
                **Traffic Sign:** {best['sign_name']}  
                **Confidence:** {best['confidence']*100:.2f}%  
                **Time:** {best['prediction_time']}
            """)
        else:
            st.info("No records found yet.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Achievements Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🏅 Badges & Rank")
        a1, a2, a3 = st.columns(3)
        with a1:
            if total >= 10:
                st.success("🥉 Beginner")
            else:
                st.markdown('<div style="opacity:0.4; text-align:center;">🥉 Beginner</div>', unsafe_allow_html=True)
        with a2:
            if total >= 50:
                st.success("🥈 Explorer")
            else:
                st.markdown('<div style="opacity:0.4; text-align:center;">🥈 Explorer</div>', unsafe_allow_html=True)
        with a3:
            if total >= 100:
                st.success("🥇 Expert")
            else:
                st.markdown('<div style="opacity:0.4; text-align:center;">🥇 Expert</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Popular Signs List
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📈 Most Detected Signs")
        if top:
            for row in top:
                st.write(f"**{row['sign_name']}** ({row['count']} detections)")
                st.progress(min(row["count"] / 20, 1.0))
        else:
            st.info("Detection history is empty.")
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        # AI Health Card
        st.markdown('<div class="card" style="text-align:center;">', unsafe_allow_html=True)
        st.subheader("⚡ AI Status")
        if accuracy >= 90:
            st.success("🟢 Excellent")
        elif accuracy >= 75:
            st.warning("🟡 Good")
        else:
            st.error("🔴 Improving")
        st.markdown('</div>', unsafe_allow_html=True)

        # Quick Actions Card
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🚀 Actions")
        if st.button("New Detection", use_container_width=True):
            st.session_state.current_page = "Detect"
            st.session_state.nav = "Detect"
            st.rerun()
        if st.button("View History", use_container_width=True):
            st.session_state.current_page = "History"
            st.session_state.nav = "History"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<p style="text-align:center; opacity:0.3; font-size:12px;">Traffic Sign Recognition System · Local Mode</p>', unsafe_allow_html=True)