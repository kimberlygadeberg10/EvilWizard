# Defeat the Evil Wizard

## Overview
*Defeat the Evil Wizard* is a Python-based turn-based game where you create a hero character and battle a powerful Evil Wizard. The game demonstrates Object-Oriented Programming (OOP) concepts such as inheritance, methods, and interactions between objects.

In the game, players can choose from four character classes, each with unique abilities, and engage in strategic combat using attacks, special abilities, healing, and defensive moves.

---

## Features

- **Four Playable Classes:**
  - **Warrior** – High health and strong basic attacks.
  - **Mage** – High attack power with magical abilities.
  - **Archer** – Uses ranged attacks and can evade enemy attacks.
  - **Paladin** – Balanced hero with healing and defensive abilities.

- **Unique Special Abilities:**
  - Archer: *Quick Shot* (double attack), *Evade* (avoid next attack)
  - Paladin: *Holy Strike* (bonus damage), *Divine Shield* (block next attack)

- **Turn-Based Battle System:**
  - Players choose actions each turn: Attack, Special Ability, Heal, or View Stats.
  - The Evil Wizard regenerates health and attacks after the player’s turn.

- **Healing Mechanic:**
  - Players can restore health without exceeding their maximum.

- **Dynamic Gameplay:**
  - Randomized attack damage adds unpredictability to battles.
  - Defensive mechanics such as Evade and Divine Shield can alter outcomes.

- **Victory and Defeat Messages:**
  - Clear messages display who won at the end of the game.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your computer
- A terminal or command prompt
- Optional: VS Code for running the project

### How to Run
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the game using:
   ```bash
   python main.py