class GlobalConstants:
    ################### APP SETTINGS
    TEXT_DISPLAYS = ("console", "discord")


    ################### GAME SETTINGS
    SPACE = "space"
    WATER = "water"
    FORBIDDEN = "forbidden"
    WOUND = "wound"
    SPARK = "spark"

    CHAR_TRAITS = {
        "honesty_humility": [
            "sincerity",
            "fairness",
            "greed_avoidance",
            "modesty"
        ],
        "emotionality": [
            "fearfulness",
            "anxiety",
            "dependence",
            "sentimentality"
        ],
        "extraversion": [
            "social_self-esteem",
            "social_boldness",
            "sociability",
            "liveliness"
        ],
        "agreeableness": [
            "forgivingness",
            "gentleness",
            "flexibility", 
            "patience"
        ],
        "conscientiousness": [
            "organization",
            "diligence",
            "perfectionism",
            "prudence"
        ],
        "openness_to_experience": [
            "aesthetic_appreciation",
            "inquisitiveness",
            "creativity",
            "unconventionality"
        ],
        "other": [
            "altruism_vs_antagonism",
            "negative_self_evaluation"
        ]
    }

    ######### ATTRIBUTES
    OBJ_BASE_ATTRIBUTES = ["reference", "name", "element"]

    CHAR_BASE_ATTRIBUTES = OBJ_BASE_ATTRIBUTES + ["pack"]

    DOMAIN_BASE_ATTRIBUTES = OBJ_BASE_ATTRIBUTES + ["level", ]
