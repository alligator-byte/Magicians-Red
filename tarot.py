import random

#major arcana - dictionary with sub dictionary idea
card_D = {
    "The Fool (0)":{
        "number" : "0", 
        "image" : "card_images/0_TheFool.png", 
        "default": "Innocence and spontaneity",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Magician (I)":{
        "number" : "1",
        "image" : "card_images/1_TheMagician.png", 
        "default": "New beginnings",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The High Priestess (II)":{
        "number" : "2",
        "image" : "card_images/2_TheHighPriestess.png", 
        "default": "Intuition and arcane knowledge",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Empress (III)":{
        "number" : "3",
        "default": "Growth of new life",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Emperor (IV)":{
        "number" : "4",
        "default": "Order and control",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hierophant (V)":{
        "number" : "5",
        "default": "Tradition and conformity",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Lovers (VI)":{
        "number" : "6",
        "default": "Conscious connections and bonds",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Chariot (VII)":{
        "number" : "7",
        "default": "Invasion and victory",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Strength (VIII)":{
        "number" : "8",
        "default": "Resilience, compassion, and confidence",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hermit (IX)":{
        "number" : "9",
        "default": "Introspection and contemplation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Wheel of Fortune (X)":{
        "number" : "10",
        "default": "Change and unpredictability",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Justice (XI)":{
        "number" : "11",
        "default": "Fairness and consequences",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hanged Man (XII)":{
        "number" : "12",
        "default": "Different perspectives",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Death (XIII)":{
        "number" : "13",
        "default": "Self-awareness and transformation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Temperance (XIV)":{
        "number" : "14",
        "default": "Balance and moderation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Devil (XV)":{
        "number" : "15",
        "default": "Confusion and misfortune",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Tower (XVI)":{
        "number" : "16",
        "default": "Unexpected interruptions and chaos",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Star (XVII)":{
        "number" : "17",
        "default": "Optimism, discernment, and hope",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Moon (XVIII)":{
        "number" : "18",
        "default": "Troubled waters, lies, betrayal, and fear of the unknown",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Sun (XIX)":{
        "number" : "19",
        "default": "Abundance, happiness, and fun",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },
    "Judgment (XX)":{
        "number" : "20",
        "default": "Rebirth and self-reflection",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The World (XXI)":{
        "number" : "21",
        "default": "Achievement and a pause before the next cycle",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    }
}



#draw some cards
reading = random.sample(list(card_D.keys()), 3)
print(reading)