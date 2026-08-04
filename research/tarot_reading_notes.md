# Tarot Reading Notes

## Core Idea
- Tarot readings are an interpretive practice using symbolic cards to explore themes, situations, or possible directions.
- A reading is usually built from:
  - the cards drawn
  - the positions of those cards in a spread
  - the relationships between cards

---

## Tarot Deck Structure
- Standard tarot deck has **78 cards**
  - **22 Major Arcana**
    - represent major life themes, archetypes, or significant turning points
    - examples:
      - The Fool
      - Death
      - The Tower
      - The Sun
  - 56 Minor Arcana will not be considered for this tool at the moment

---

## General Tarot Reading Process

### 1. Set intention / ask question
- Reader or user chooses a focus and asked questions
- Application should just prompt reader to draw 

---

### 2. Shuffle the deck
- Cards are shuffled to randomize order.
- This is currently achieved by python random library (will remain this way unless a better implementation is found)

---

### 3. Draw cards
- A specific number of cards is drawn depending on spread.
  - 3 cards = standard reading
  - Possibly implement single (1 card) drawings later as a feature on the app

---

### 4. Assign spread positions
- Each card is placed into a predefined position.

Common 3-card spreads:
- Past / Present / Future
- 
Thus:
- Card 1 = Past
- Card 2 = Present
- Card 3 = Future

---

### 5. Interpret each card individually
- Look at:
  - card meaning
  - symbolism
  - position meaning

Example:
- The Fool in Present:
  - new beginnings & a leap of faith
- The Fool in Past:
  - earlier risk-taking or innocence

---

### 6. Interpret card relationships
- Read cards as a sequence or narrative.
Example:
- High Priestess → Fool → Hierophant
  - intuition leads to a new beginning, which develops into structure/tradition
This functionality is not planned at the moment; meanings shall be left open ended so that they can fit together and allow the user to extrapolate further.

---

### 7. Build narrative
- Combine individual meanings into a coherent story.
- Print out the Card images, with the meanings allowing a brief story to be crafted.
---

## Additional Info - Reversed Cards (optional)
- Some readings include reversed cards (upside down).
- Often interpreted as having an opposite meaning to that card
- This feature won't be implemented yet

---

## For Tarot App Implementation
- Store each card with:
  - base meaning
  - optional position-specific meanings

Example structure:
- card
- keywords
- past meaning
- present meaning
- future meaning

Flow:
- random draw
- assign positions
- retrieve interpretations
- combine into narrative output

Example output:
- "You come from a period of introspection, are entering a new phase, and may move toward greater structure."

---

## Possible App Features
- Daily draw
- 3-card spread
- Custom questions
- Saved readings
- Reversed card toggle
- Different spread types
