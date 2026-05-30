class GlobalConstants:
    ################### APP SETTINGS
    TEXT_DISPLAYS = ("console", "discord")
    MANUAL_MODE = "manual"
    AUTOMATIC_MODE = "automatic"

    ################### GAME SETTINGS
    SPACE = "space"
    WATER = "water"
    FORBIDDEN = "forbidden"
    WOUND = "wound"
    SPARK = "spark"

    ELEMENTS = [SPACE, WATER, FORBIDDEN, WOUND, SPARK]

    ############ Char traits, then regrouped as aspects
    HONESTY_HUMILITY = [
        "sincerity",
        "fairness",
        "greed_avoidance",
        "modesty"
    ]
    EMOTIONALITY = [
        "fearfulness",
        "anxiety",
        "dependence",
        "sentimentality"
    ]
    EXTRAVERSION = [
        "social_self-esteem",
        "social_boldness",
        "sociability",
        "liveliness"
    ]
    AGREEABLENESS = [
        "forgivingness",
        "gentleness",
        "flexibility",
        "patience"
    ]
    CONSCIENTIOUSNESS = [
        "organization",
        "diligence",
        "perfectionism",
        "prudence"
    ]
    OPENNESS_TO_EXPERIENCE = [
        "aesthetic_appreciation",
        "inquisitiveness",
        "creativity",
        "unconventionality"
    ]
    TRAITS_OTHERS = [ # before you complain about the vague name, did you want to type "interstitials"
        "altruism_vs_antagonism",
        "negative_self_evaluation"
    ]
    CHAR_TRAITS = {
        "honesty_humility": HONESTY_HUMILITY,
        "emotionality": EMOTIONALITY,
        "extraversion": EXTRAVERSION,
        "agreeableness": AGREEABLENESS,
        "conscientiousness": CONSCIENTIOUSNESS,
        "openness_to_experience": OPENNESS_TO_EXPERIENCE,
        "others": TRAITS_OTHERS
    }

    ######### ATTRIBUTES
    OBJ_BASE_ATTRIBUTES = ["reference", "name", "element"]

    CHAR_BASE_ATTRIBUTES = (
        OBJ_BASE_ATTRIBUTES +
        HONESTY_HUMILITY +
        EMOTIONALITY +
        EXTRAVERSION +
        AGREEABLENESS +
        CONSCIENTIOUSNESS +
        OPENNESS_TO_EXPERIENCE +
        TRAITS_OTHERS +
        ["pack"]
    )

    DOMAIN_BASE_ATTRIBUTES = OBJ_BASE_ATTRIBUTES + ["level", ]
