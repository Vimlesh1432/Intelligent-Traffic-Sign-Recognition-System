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
                "padding": "0!important",
                "background-color": "#0f172a"
            },

            "icon": {
                "color": "#b3daeb",
                "font-size": "18px"
            },

            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#1b574d",
            },

            "nav-link-selected": {
                "background-color": "#562848",
                "color": "white",
            },
        },
    )

    return selected