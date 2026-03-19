import random

#major arcana 
cards = ["The Fool (0)", "The Magician (I)", "The High Priestess (II)", "The Empress (III)", "The Emperor (IV),
         "The Hierophant (V)", "The Lovers (VI)", "The Chariot (VII)", "Strength (VIII)", "The Hermit (IX)",
         "The Wheel of Fortune (X)", "Justice (XI)", "The Hanged Man (XII)", "Death (XIII)", "Temperance (XIV)",
         "The Devil (XV)", "The Tower (XVI)", "The Star (XVII)", "The Moon (XVIII)", "The Sun (XIX)", 
         "Judgment (XX)", "The World (XXI)"] 

#draw some cards
reading = random.sample(cards, 3)
