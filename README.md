# Project Name

**Author**: Brandon, Clarissa

**Version**: 1.0.0
<!-- (increment the patch/fix version number if you make more commits past your first submission) -->

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for this class. (i.e. What's your problem domain?) -->

We are building a dice game based on the game, "Farkle", in order to expand our understanding and get practice with the Python standard library.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->

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
    - shelf should temporarily store unbanked points.

- Add a bank instance method

  - bank should add any points on the shelf to total and reset shelf to 0.
  - bank output should be the amount of points added to total from shelf.  

- Add a clear_shelf instance method
  - clear_shelf should remove all unbanked points.

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Python, Poetry,

## Change Log

<!-- Use this area to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Application now has a fully-functional express server, with a GET route for the location resource. -->

## Estimates
<!-- See below -->
Estimate of time needed to complete:

Start time:
Finish time:

Actual time needed to complete:

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->

### Resource Links

[](https://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary)

[](https://docs.python.org/3/library/collections.html)

[](https://en.wikipedia.org/wiki/Dice_10000)