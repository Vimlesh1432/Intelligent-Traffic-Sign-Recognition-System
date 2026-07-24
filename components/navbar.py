from streamlit_option_menu import option_menu

def navbar():
    selected = option_menu(
        menu_title=None,
        options=[
                "Dashboard",
                "Detect", 
                "History", 
                "Profile", 
                "Settings", 
            ],

        icons=[
                "house-fill", 
                "camera-fill", 
                "clock-history", 
                "person-fill", 
                "gear-fill", 
                "box-arrow-right"
            ],

        menu_icon=None,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0px !important",
                "background-color": "transparent !important", # 👈 Bilkul transparent
                "margin": "0px !important",
                "border": "none !important",
                "box-shadow": "none !important",
            },

            "icon": {
                "color": "#60a5fa", 
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "5px",
                "background-color": "rgba(255, 255, 255, 0.07)", # 👈 Individual buttons ka glass look
                "border": "1px solid rgba(255, 255, 255, 0.1)",
                "border-radius": "12px",
                "color": "white",
                "padding": "10px",
                "transition": "all 0.3s ease",
                "--hover-color": "rgba(255, 255, 255, 0.15)",
            },
            
            "nav-link-selected": {
                "background-color": "rgba(59, 130, 246, 0.2)",
                "border": "1px solid #3b82f6",
                "color": "white",
            },
        },
    )
    return selected