# Game of Greed

**Author**: Brandon Mizutani, Clarissa Pamonicutt

**Version**: 1.3.0 (PR URL: [PR URL](https://github.com/bran2miz/game-of-greed/pull/15))

[Lab08 PR URL](https://github.com/bran2miz/game-of-greed/pull/20)

[Lab09 PR URL](https://github.com/bran2miz/game-of-greed/pull/19)
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

---

### Lab 08

- Application should implement features from versions 1 and 2
- Should handle setting aside scoring dice and continuing turn with remaining dice.
- Should handle when cheating occurs.
  - Or just typos.
  - E.g. roll = [1,3,5,2] and user selects 1, 1, 1, 1, 1, 1
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle zilch
  - No points for round, and round is over

---

### Lab 09

- Create an AI Bot to play Game of Greed
  - The only method available for use from Game class is play.
  - All static methods of GameLogic class are available.
  - All other interactions with game can take place ONLY via the I/O features of the game.
    - In other words, via injectable print and input functionality.
    - It is FORBIDDEN to inject a custom roller function into Game class.
- Copy bots.py to your project.
  - Place it at root of project, at same level as pyproject.toml
- Your Bot class should be added to bots.py file with name of your choosing replacing YourBot.
  - NOTE the code for BaseBot class is supplied for reference, but your custom code will be in the overridden _roll_bank_or_quit and _enter_dice methods.
- User should be able to see your bot play by executing bots.py from terminal.
- Application should implement features from previous classes

The goal is to beat Nervous Nellie - A reference bot that banks on the first roll every time.

---

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

01-08-22: 78 Tests passed

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->

Eddie Ponce

Osborn Del Angel

Alex Payne

Isaiah Burkes

Referenced Roger Huba Lab 09 code for Lab 08

### Resource Links

[Source](https://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary)

[Source](https://docs.python.org/3/library/collections.html)

[Source](https://en.wikipedia.org/wiki/Dice_10000)

[Source](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/)

[Roger Huba game.py](https://github.com/codefellows/seattle-code-python-401n4/blob/main/class-9/game-of-greed/game_of_greed/game.py)

[Roger Huba Game Logic](https://github.com/codefellows/seattle-code-python-401n4/blob/main/class-9/game-of-greed/game_of_greed/game_logic.py)
