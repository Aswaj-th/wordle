# Wordle

Welcome to the Word Guessing Game! This Python project implements a simple word guessing game where players try to guess a word letter by letter within a limited number of attempts.

## Features

- Interactive gameplay: Players can input their guesses and receive feedback on whether their guess is correct or not.
- Word generation: Random words are fetched from an external API or selected from a backup array if the API fails.
- Game state tracking: The game keeps track of the current state of the word, the number of lives left, and the number of correctly guessed letters.
- Winning and losing conditions: The game ends when the player successfully guesses the word or runs out of lives.

## Setup

1. Clone the repository to your local machine:

```
git clone https://github.com/Aswaj-th/wordle.git
```

2. Run the game

```
python main.py
```

## Dependencies

- Python 3.x
- `requests` library: Used to make HTTP requests to fetch random words from an external API.
- `re` module: Used for regular expression matching to validate input.
- `random` module: Used for selecting random words from the backup array.

## Usage

- When prompted, enter a single lowercase English letter as your guess.
- The game will provide feedback on whether your guess is correct or not.
- Keep guessing until you either successfully guess the word or run out of lives.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request
