TRAFFIC_SIGNS = {
    0: {
        "name": "Speed Limit (20 km/h)",
        "description": "Maximum speed allowed is 20 km/h.",
        "category": "Speed Limit",
        "risk": "Low"
    },

    1: {
        "name": "Speed Limit (30 km/h)",
        "description": "Maximum speed allowed is 30 km/h.",
        "category": "Speed Limit",
        "risk": "Low"
    },

    2: {
        "name": "Speed Limit (50 km/h)",
        "description": "Maximum speed allowed is 50 km/h.",
        "category": "Speed Limit",
        "risk": "Medium"
    },

    3: {
        "name": "Speed Limit (60 km/h)",
        "description": "Maximum speed allowed is 60 km/h.",
        "category": "Speed Limit",
        "risk": "Medium"
    },

    4: {
        "name": "Speed Limit (70 km/h)",
        "description": "Maximum speed allowed is 70 km/h.",
        "category": "Speed Limit",
        "risk": "Medium"
    },
    5: {
        "name": "Speed Limit (80 km/h)",
        "description": "Maximum speed allowed is 80 km/h.",
        "category": "Speed Limit",
        "risk": "Medium",
        "driver_action": "Stay within the 80 km/h speed limit."
    },

    6: {
        "name": "End of Speed Limit (80 km/h)",
        "description": "The previous 80 km/h speed restriction has ended.",
        "category": "Speed Limit",
        "risk": "Low",
        "driver_action": "Follow the next applicable speed limit."
    },

    7: {
        "name": "Speed Limit (100 km/h)",
        "description": "Maximum speed allowed is 100 km/h.",
        "category": "Speed Limit",
        "risk": "Medium",
        "driver_action": "Drive below 100 km/h."
    },

    8: {
        "name": "Speed Limit (120 km/h)",
        "description": "Maximum speed allowed is 120 km/h.",
        "category": "Speed Limit",
        "risk": "Medium",
        "driver_action": "Maintain a speed below 120 km/h."
    },

    9: {
        "name": "No Passing",
        "description": "Overtaking other vehicles is prohibited.",
        "category": "Regulatory",
        "risk": "High",
        "driver_action": "Do not overtake until the restriction ends."
    },

    10: {
        "name": "No Passing for Vehicles over 3.5 Tons",
        "description": "Heavy vehicles are not allowed to overtake.",
        "category": "Regulatory",
        "risk": "High",
        "driver_action": "Heavy vehicles must stay in their lane."
    },

    11: {
        "name": "Right-of-Way at Intersection",
        "description": "You have priority at the upcoming intersection.",
        "category": "Priority",
        "risk": "Medium",
        "driver_action": "Proceed carefully while maintaining priority."
    },

    12: {
        "name": "Priority Road",
        "description": "You are on a priority road with right of way.",
        "category": "Priority",
        "risk": "Medium",
        "driver_action": "Continue carefully and watch for crossing traffic."
    },

    13: {
        "name": "Yield",
        "description": "Give way to other vehicles before proceeding.",
        "category": "Regulatory",
        "risk": "High",
        "driver_action": "Slow down and allow other traffic to pass first."
    },

    14: {
        "name": "Stop",
        "description": "You must come to a complete stop before proceeding.",
        "category": "Regulatory",
        "risk": "High",
        "driver_action": "Stop completely and continue only when safe."
    },
        15: {
        "name": "No Vehicles",
        "description": "All vehicles are prohibited from entering this road.",
        "category": "Prohibition",
        "risk": "High",
        "driver_action": "Do not enter with any vehicle."
    },

    16: {
        "name": "Vehicles over 3.5 Tons Prohibited",
        "description": "Heavy vehicles exceeding 3.5 tons are not allowed.",
        "category": "Prohibition",
        "risk": "High",
        "driver_action": "Heavy vehicles must use an alternate route."
    },

    17: {
        "name": "No Entry",
        "description": "Entry is prohibited from this direction.",
        "category": "Prohibition",
        "risk": "High",
        "driver_action": "Do not enter this road."
    },

    18: {
        "name": "General Caution",
        "description": "Be alert and drive carefully due to possible hazards.",
        "category": "Warning",
        "risk": "Medium",
        "driver_action": "Reduce speed and stay attentive."
    },

    19: {
        "name": "Dangerous Curve Left",
        "description": "A sharp left curve is ahead.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Slow down and steer carefully to the left."
    },

    20: {
        "name": "Dangerous Curve Right",
        "description": "A sharp right curve is ahead.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Slow down and steer carefully to the right."
    },

    21: {
        "name": "Double Curve",
        "description": "Two consecutive curves are ahead.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Reduce speed and prepare for multiple turns."
    },

    22: {
        "name": "Bumpy Road",
        "description": "Uneven road surface ahead.",
        "category": "Warning",
        "risk": "Medium",
        "driver_action": "Drive slowly and maintain vehicle control."
    },

    23: {
        "name": "Slippery Road",
        "description": "Road may be slippery due to weather or surface conditions.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Reduce speed and avoid sudden braking."
    },

    24: {
        "name": "Road Narrows on the Right",
        "description": "The road becomes narrower from the right side.",
        "category": "Warning",
        "risk": "Medium",
        "driver_action": "Stay centered and reduce speed."
    },

    25: {
        "name": "Road Work",
        "description": "Construction or maintenance work is ahead.",
        "category": "Warning",
        "risk": "Medium",
        "driver_action": "Slow down and follow temporary signs."
    },

    26: {
        "name": "Traffic Signals",
        "description": "Traffic lights are ahead.",
        "category": "Warning",
        "risk": "Medium",
        "driver_action": "Prepare to stop or proceed according to the signal."
    },

    27: {
        "name": "Pedestrians",
        "description": "Pedestrian crossing area ahead.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Reduce speed and give way to pedestrians."
    },

    28: {
        "name": "Children Crossing",
        "description": "Children may cross the road unexpectedly.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Drive very carefully and be ready to stop."
    },

    29: {
        "name": "Bicycles Crossing",
        "description": "Cyclists may cross the road ahead.",
        "category": "Warning",
        "risk": "Medium",
        "driver_action": "Watch for bicycles and slow down if necessary."
    },
        30: {
        "name": "Beware of Ice / Snow",
        "description": "Road may be icy or covered with snow.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Reduce speed and avoid sudden braking."
    },

    31: {
        "name": "Wild Animals Crossing",
        "description": "Wild animals may cross the road.",
        "category": "Warning",
        "risk": "High",
        "driver_action": "Drive cautiously and be prepared to stop."
    },

    32: {
        "name": "End of All Speed and Passing Limits",
        "description": "Previous speed and overtaking restrictions have ended.",
        "category": "Regulatory",
        "risk": "Low",
        "driver_action": "Follow the normal traffic rules and posted limits."
    },

    33: {
        "name": "Turn Right Ahead",
        "description": "A mandatory right turn is ahead.",
        "category": "Mandatory",
        "risk": "Medium",
        "driver_action": "Prepare to turn right."
    },

    34: {
        "name": "Turn Left Ahead",
        "description": "A mandatory left turn is ahead.",
        "category": "Mandatory",
        "risk": "Medium",
        "driver_action": "Prepare to turn left."
    },

    35: {
        "name": "Ahead Only",
        "description": "You must continue straight ahead.",
        "category": "Mandatory",
        "risk": "Low",
        "driver_action": "Do not turn left or right."
    },

    36: {
        "name": "Go Straight or Right",
        "description": "You may continue straight or turn right.",
        "category": "Mandatory",
        "risk": "Low",
        "driver_action": "Choose either straight or right."
    },

    37: {
        "name": "Go Straight or Left",
        "description": "You may continue straight or turn left.",
        "category": "Mandatory",
        "risk": "Low",
        "driver_action": "Choose either straight or left."
    },

    38: {
        "name": "Keep Right",
        "description": "Pass to the right side of the obstacle or divider.",
        "category": "Mandatory",
        "risk": "Low",
        "driver_action": "Stay on the right side."
    },

    39: {
        "name": "Keep Left",
        "description": "Pass to the left side of the obstacle or divider.",
        "category": "Mandatory",
        "risk": "Low",
        "driver_action": "Stay on the left side."
    },

    40: {
        "name": "Roundabout Mandatory",
        "description": "A roundabout is ahead.",
        "category": "Mandatory",
        "risk": "Medium",
        "driver_action": "Enter the roundabout carefully and follow traffic flow."
    },

    41: {
        "name": "End of No Passing",
        "description": "The no-passing restriction has ended.",
        "category": "Regulatory",
        "risk": "Low",
        "driver_action": "Overtaking is now allowed if safe."
    },

    42: {
        "name": "End of No Passing by Vehicles over 3.5 Tons",
        "description": "Heavy vehicles may overtake again where safe.",
        "category": "Regulatory",
        "risk": "Low",
        "driver_action": "Heavy vehicles may overtake only when it is safe."
    }

}