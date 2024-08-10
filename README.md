# Two-Player Trivia Battle Game

## Project Overview

This project is a competitive two-player trivia game built using HTML, CSS, and JavaScript. Players input their names, choose a category, and answer trivia questions fetched from The Trivia API. The game keeps track of the scores based on the correctness of the answers and declares a winner at the end.

## Features

- **Player Setup**: Two players enter their names to start the game.
- **Category Selection**: Players choose a category from a list, and the game fetches 6 trivia questions (2 easy, 2 medium, 2 hard) from the selected category.
- **Turn-Based Gameplay**: Players take turns answering questions. Scores are awarded based on the difficulty level of the question.
- **Score Calculation**:
  - Easy question: 10 points
  - Medium question: 15 points
  - Hard question: 20 points
- **Post-Question Options**: After all questions in a category are answered, players can either select another category or end the game.
- **Game End and Results**: The game ends when players choose to end it or all categories are exhausted. The player with the higher score is declared the winner.

## Technologies Used

- **HTML**: For structuring the web pages.
- **CSS**: For styling the game interface.
- **JavaScript**: For handling game logic, API interactions, and user interaction.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/two-player-trivia-game.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd two-player-trivia-game
   ```
3. **Open the project in a web browser**:
   - You can open the `index.html` file directly in your browser or use a local server like Live Server in VSCode for live reloading.

## How to Play

1. **Enter Player Names**: Both players should enter their names and click "Start Game."
2. **Select a Category**: Choose a category from the dropdown list.
3. **Answer Questions**: Players take turns answering questions. Player 1 answers the first easy question, Player 2 answers the second easy question, and so on.
4. **Score Calculation**: Points are awarded based on the difficulty of the question answered correctly.
5. **Post-Question Options**: After all questions in a category are answered, players can either select a new category or end the game.
6. **End Game and Results**: The game ends when players choose to end it or all categories are exhausted. The player with the higher score wins.

## API Used

- **The Trivia API**: This project uses The Trivia API to fetch trivia questions. More details about the API can be found [here](https://the-trivia-api.com/).

## Known Issues

- Ensure that the selected category is not reused.
- The game currently fetches questions in separate requests for each difficulty, which could cause delays.

## Contributing

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. Suggestions for new features and bug reports are also welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to The Trivia API for providing a reliable source of trivia questions.
- Thanks to the HVA Mini Hackathon for providing the opportunity to build this project.
