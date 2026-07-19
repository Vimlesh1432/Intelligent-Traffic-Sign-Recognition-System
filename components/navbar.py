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
            "Logout"
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
                "padding": "0!important",
                "background-color": "#0f172a"
            },

            "icon": {
                "color": "#38bdf8",
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#1e40af",
            },

            "nav-link-selected": {
                "background-color": "#2563eb",
                "color": "white",
            },
        },
    )

    return selected