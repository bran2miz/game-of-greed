# Game of Greed

**Author**: Brandon Mizutani, Clarissa Pamonicutt

**Version**: 1.1.0 (PR URL: [PR URL](https://github.com/bran2miz/game-of-greed/pull/15))
<!-- (increment the patch/fix version number if you make more commits past your first submission) -->

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for this class. (i.e. What's your problem domain?) -->

We are building a dice game based on the game, "Farkle", in order to expand our understanding and get practice with the Python standard library.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->

### Lab 06

**Define a GameLogic class in game_of_greed/game_logic.py file.**

**Handle calculating score for dice roll**:

- Add calculate_score static method to GameLogic class.
- The input to calculate_score is a tuple of integers that represent a dice roll.
- The output from calculate_score is an integer representing the roll’s score according to rules of game.

**Handle rolling dice**:

- Add roll_dice static method to GameLogic class.
- The input to roll_dice is an integer between 1 and 6.
- The output of roll_dice is a tuple with random values between 1 and 6.
- The length of tuple must match the argument given to roll_dice method.

**Handle banking points**:

- Define a Banker class
  - Add a shelf instance method
    - Input to shelf is the amount of points (integer) to add to shelf.
    - shelf should temporarily store un banked points.

- Add a bank instance method

  - bank should add any points on the shelf to total and reset shelf to 0.
  - bank output should be the amount of points added to total from shelf.  

- Add a clear_shelf instance method
  - clear_shelf should remove all un banked points.

---

### Lab 07

- Application should implement all features from previous version
- Application should simulate rolling between 1 and 6 dice
- Application should allow user to set aside dice each roll
- Application should allow “banking” current score or rolling again.
- Application should keep track of total score
- Application should keep track of current round
- Application should have automated tests to ensure proper operation

- Starter code contains acceptance tests in the form of “simulation” files.
  - E.g. `tests/version_1/quitter.sim.txt`
- These simulation files are used in concert with `tests/flo.py` to examine actual vs. expected output.

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Python, Poetry,

## Change Log

<!-- Use this area to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Application now has a fully-functional express server, with a GET route for the location resource. -->

12-22-21: Began game logic, 12 tests passing

12-23-21: Finished game logic and banker points, all tests passing

12-30-21: 69 Tests passing

12-03-21: 71 Tests passing, lab complete

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->

Eddie Ponce

Osborn Del Angel

Alex Payne

Isaiah Burkes

### Resource Links

[Source](https://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary)

[Source](https://docs.python.org/3/library/collections.html)

[Source](https://en.wikipedia.org/wiki/Dice_10000)

[Source](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/)
