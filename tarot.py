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
        "image" : "card_images/3_TheEmpress.png", 
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Emperor (IV)":{
        "number" : "4",
        "image" : "card_images/4_TheEmperor.png", 
        "default": "Order and control",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hierophant (V)":{
        "number" : "5",
        "image" : "card_images/5_TheHierophant.png", 
        "default": "Tradition and conformity",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Lovers (VI)":{
        "number" : "6",
        "image" : "card_images/6_TheLovers.png", 
        "default": "Conscious connections and bonds",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Chariot (VII)":{
        "number" : "7",
        "image" : "card_images/7_TheChariot.png", 
        "default": "Invasion and victory",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Strength (VIII)":{
        "number" : "8",
        "image" : "card_images/8_Strenght.png", 
        "default": "Resilience, compassion, and confidence",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hermit (IX)":{
        "number" : "9",
        "image" : "card_images/9_TheHermit.png", 
        "default": "Introspection and contemplation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Wheel of Fortune (X)":{
        "number" : "10",
        "image" : "card_images/10_TheWheelOfFortune.png", 
        "default": "Change and unpredictability",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Justice (XI)":{
        "number" : "11",
        "image" : "card_images/11_Justice.png", 
        "default": "Fairness and consequences",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Hanged Man (XII)":{
        "number" : "12",
        "image" : "card_images/12_TheHangedMan.png", 
        "default": "Different perspectives",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Death (XIII)":{
        "number" : "13",
        "image" : "card_images/13_Death.png", 
        "default": "Self-awareness and transformation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "Temperance (XIV)":{
        "number" : "14",
        "image" : "card_images/14_Temperance.png", 
        "default": "Balance and moderation",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Devil (XV)":{
        "number" : "15",
        "image" : "card_images/15_TheDevil.png", 
        "default": "Confusion and misfortune",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Tower (XVI)":{
        "number" : "16",
        "image" : "card_images/16_TheTower.png", 
        "default": "Unexpected interruptions and chaos",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Star (XVII)":{
        "number" : "17",
        "image" : "card_images/17_TheStar.png", 
        "default": "Optimism, discernment, and hope",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Moon (XVIII)":{
        "number" : "18",
        "image" : "card_images/18_TheMoon.png", 
        "default": "Troubled waters, lies, betrayal, and fear of the unknown",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The Sun (XIX)":{
        "number" : "19",
        "image" : "card_images/19_TheSun.png", 
        "default": "Abundance, happiness, and fun",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },
    "Judgement (XX)":{
        "number" : "20",
        "image" : "card_images/20_Judgement.png", 
        "default": "Rebirth and self-reflection",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    },

    "The World (XXI)":{
        "number" : "21",
        "image" : "card_images/21_TheWorld.png", 
        "default": "Achievement and a pause before the next cycle",
        "past": "BLANK",
        "present":"BLANK",
        "future": "BLANK"
    }
}

'''
STEP 1 - DRAW 3 RANDOM CARDS FROM THE MAJOR ARCANA
'''
#draw some cards (store as a list)
reading = random.sample(list(card_D.keys()), 3)
print(reading)

'''
STEP 2 - LINK INTERPRETATIONS 
'''

past = card_D[reading[0]]
present = card_D[reading[1]]
future = card_D[reading [2]]

print("\nPast")
print(reading[0])
print(past["default"])

print("\nPresent")
print(reading[1])
print(present["default"])

print("\nFuture")
print(reading [2])
print(future["default"])

