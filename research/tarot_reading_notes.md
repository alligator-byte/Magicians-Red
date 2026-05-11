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
  - **56 Minor Arcana**
    - represent everyday situations and smaller influences
    - divided into 4 suits:
      - Cups
      - Pentacles
      - Swords
      - Wands

---

## General Tarot Reading Process

### 1. Set intention / ask question
- Reader or user chooses a focus.
- Questions are often open-ended.
- Examples:
  - "What should I know about my current situation?"
  - "What energy surrounds this decision?"

---

### 2. Shuffle the deck
- Cards are shuffled to randomize order.
- Some traditions involve:
  - focusing on a question while shuffling
  - cutting the deck before drawing

---

### 3. Draw cards
- A specific number of cards is drawn depending on spread.
- Example:
  - 1 card = daily guidance
  - 3 cards = simple reading
  - larger spreads = more detailed analysis

---

### 4. Assign spread positions
- Each card is placed into a predefined position.

Common 3-card spreads:
- Past / Present / Future
- Situation / Challenge / Advice
- Mind / Body / Spirit

Example:
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
  - new beginnings
  - leap of faith
- The Fool in Past:
  - earlier risk-taking or innocence

---

### 6. Interpret card relationships
- Read cards as a sequence or narrative.

Questions asked:
- How does card 1 influence card 2?
- Does the progression suggest movement, conflict, or resolution?

Example:
- High Priestess → Fool → Hierophant
  - intuition leads to a new beginning, which develops into structure/tradition

---

### 7. Build narrative
- Combine individual meanings into a coherent story.

Example format:
- Past influenced present
- Present leads toward future

Narrative style:
- "You come from X, are currently facing Y, and may be moving toward Z."

---

## Reversed Cards (optional)
- Some readings include reversed cards (upside down).
- Often interpreted as:
  - blocked energy
  - internalized meaning
  - opposite or weakened influence

Example:
- Upright Sun = optimism
- Reversed Sun = delayed clarity or reduced confidence

(Not required in all systems.)

---

## Important Interpretation Principles
- Tarot is not usually treated as fixed prediction.
- Meanings are flexible and contextual.
- Same card can mean different things depending on:
  - spread position
  - neighbouring cards
  - question context

Example:
- Death may mean:
  - endings
  - transformation
  - transition
  - release

Not necessarily literal death.

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

## Common App Features
- Daily draw
- 3-card spread
- Custom questions
- Saved readings
- Reversed card toggle
- Different spread types
