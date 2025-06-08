# **Hangman Game**

This is a comprehensive Hangman game project that offers two gameplay experiences:  
a classic text-based Command-Line Interface (CLI) version for quick and straightforward play,  
and a graphical user interface (GUI) built with Python’s Tkinter library for a more interactive and visually engaging experience.  

Both versions implement core Hangman game mechanics, including tracking guessed letters,  
displaying hangman visuals, and handling win/loss conditions.

**Each mode is implemented in a separate file and should be run individually.**


## **Features**

- Classic Hangman game logic with win/loss detection  
- Two versions: CLI (`hangman_cli.py`) and GUI (`hangman_gui.py`)  
- CLI uses keyboard input and terminal display  
- GUI built with Tkinter for interactive play  
- Both versions show hangman visuals and tracks guesses

## **Gameplay**

The Hangman game challenges the player to guess a hidden word one letter at a time before the hangman figure is fully drawn.

- You can guess one letter per turn.
- Correct guesses reveal the letter’s position(s) in the word.
- Incorrect guesses add a part to the hangman drawing.
- You have limited chances to guess wrong before the game ends.
- The game ends with a win if you guess the full word, or a loss if the hangman is completed.
  
## **How to Install and Run**

1. Install Python 3.x on your system if you don’t have it already.  
   Download from [python.org](https://www.python.org/downloads/).
   
3. Clone the repository
   - Open your terminal and run the following command:
   ```bash
   git clone <repository_url>
   ```
   *Replace <repository_url> with your own fork's URL if applicable.*
     
4. Navigate to the project directory
   - Run the command in the terminal:
     ```bash
     cd hangman-game
     ```
▶️ Running the CLI Version

5. To start the command-line interface version of the game, run:
   ```bash
   python hangman_cli.py
   ```
6. Follow the instructions displayed in the terminal to play.

▶️ Running the GUI Version

7. To start the graphical user interface version, run:
   ```bash
   python hangman_gui.py
   ```
*Note*: The CLI and GUI versions are separate programs and need to be run individually.

## **Tools and Techonologies Used**

- Python 3.13.4 — The programming language used to develop both the CLI and GUI versions.
- Tkinter — Python’s built-in library for creating the graphical user interface (GUI) in the project.
- random — Python standard module used to select words randomly from the word list.
- VS Code — Code editor for writing and running the Python scripts.
- GitHub — Used for version control and hosting the project repository.

## **Credits**

This Hangman game project was inspired and developed using the following resources:

- **Project Idea and Implementation**:  
  [Python Tutorial by freeCodeCamp](https://www.freecodecamp.org/news/python-projects-for-beginners/) — Provided the core concept and detailed explanation for building the Hangman game.

- **Word List Source**:  
  [Random Lists - Words JSON](https://www.randomlists.com/data/words.json) — Used as the source for random words to guess in the game.

- **GUI Development Guide**:  
  [GeeksforGeeks - Python GUI Tkinter Tutorial](https://www.geeksforgeeks.org/python-gui-tkinter/) — Helped in designing and implementing the graphical user interface using Tkinter.


### Thank You!



      



