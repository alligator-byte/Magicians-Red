import random

#major arcana 
cards = ["The Fool (0)", 
         "The Magician (I)", 
         "The High Priestess (II)", 
         "The Empress (III)", 
         "The Emperor (IV)",
         "The Hierophant (V)", 
         "The Lovers (VI)", 
         "The Chariot (VII)", 
         "Strength (VIII)", 
         "The Hermit (IX)",
         "The Wheel of Fortune (X)", 
         "Justice (XI)", 
         "The Hanged Man (XII)", 
         "Death (XIII)", 
         "Temperance (XIV)",
         "The Devil (XV)", 
         "The Tower (XVI)", 
         "The Star (XVII)", 
        "The Moon (XVIII)", 
        "The Sun (XIX)", 
         "Judgment (XX)", 
         "The World (XXI)"] 

#draw some cards
reading = random.sample(cards, 3)
print(reading)

#dictionary with sub dictionary idea
interpretation = {
    "The Fool (0)":{
        "default": "Innocence and spontaneity",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Magician (I)":{
        "default": "New beginnings",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The High Priestess (II)":{
        "default": "Intuition and arcane knowledge",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Empress (III)":{
        "default": "Growth of new life",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Emperor (IV)":{
        "default": "Order and control",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hierophant (V)":{
        "default": "Tradition and conformity",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Lovers (VI)":{
        "default": "Conscious connections and bonds",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Chariot (VII)":{
        "default": "Invasion and victory",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Strength (VIII)":{
        "default": "Resilience, compassion, and confidence",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hermit (IX)":{
        "default": "Introspection and contemplation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Wheel of Fortune (X)":{
        "default": "Change and unpredictability",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Justice (XI)":{
        "default": "Fairness and consequences",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hanged Man (XII)":{
        "default": "Different perspectives",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Death (XIII)":{
        "default": "Self-awareness and transformation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Temperance (XIV)":{
        "default": "Balance and moderation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Devil (XV)":{
        "default": "Confusion and misfortune",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Tower (XVI)":{
        "default": "Unexpected interruptions and chaos",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Star (XVII)":{
        "default": "Optimism, discernment, and hope",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Moon (XVIII)":{
        "default": "Troubled waters, lies, betrayal, and fear of the unknown",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Sun (XIX)":{
        "default": "Abundance, happiness, and fun",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },
    "Judgment (XX)":{
        "default": "Rebirth and self-reflection",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The World (XXI)":{
        "default": "Achievement and a pause before the next cycle",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    }
}


#lists for each - then use the indexes to find
past = ["Info here...",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""]
present =  []
future = []
