# Text Adventure Game

## A text based choice game built using Python where the player enters their name and then makes decisions that affects how the story unfolds.

The game simulates a school journey where the player decides which high school to attend, which subjects to take, and whether to accept academic opportunities. Each decision leads to a different path and ending. 

## What The Program Does:

1. Asks for the users name.
2. Welcomes them to the game.
3. Asks which highschool they would like to select:
   - Crawford Sandton
   - Hyde Park High School
4. Based on that choice, the story branches.

## Branch 1: Crawford Sandton

After one year, the school fees are too high.
The user must now choose between:
   - St. Davids
   - Hyde Park High School
   - 
Each choice gives a different ending.

## Branch 2: Hyde Park High School

In grade 10, the user chooses between 2 subjects:
   - History
   - Physics

If they choose History, they then decide whether to accept an AP English offer based on their strong essay-writing ability:
    
   - yes
   - no

At the end, the program thanks the user for playing and gives them the option to play again.

## Key Concepts Demonstrated

* While loops (game replay functionality)
* If/elif/else statements (decision-making)
* Functions (handling invalid choices)
* String methods:
   - .strip()
   - .lower()
   - .title()
* User Input Handling

## Technology Used

Python 3

## How To Run The Game

1. Make sure you have Python installed (Python 3+ recommended).
2. Clone this repository or download the file.
3. Open your terminal or command prompt
4. Navigate to the project folder
5. Run the script:
   python game.py
   
## Notes

- All inputs are case-insensitive. 
- Players can type either the number(e.g. 1) or the full name(e.g. "crawford sandton").
- Invalid choices will end the game.

## Future Improvements

* Add more story branches and endings.
* Add random events.

# Author

Created by Unathi Malangabi
