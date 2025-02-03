# Documentation...

## Before
When developing this CLI calculator program there was a it went a bit well just doing def functions for basic arithmetic problems like addition, subtraction, multiplication and division with asking the user first number and second number and if they want to try again. There was a bit of problem when diving zero by zero, I have learnt that you can use a zerodivisionerror
method to bypass the issue. Afterwards I created the logic behind for when the user wants to begin using the calculator and if they want to stop.

## After
When asking for feedback on the code there wasn't much of an issue that was needed to be fixed. But there was some major issues if I would want to continue this app like 

### Key Improvements:
DRY (Don't Repeat Yourself) Principle: Common tasks (input, display, retry) are handled by helper functions.

Safer Execution: No recursion → uses loops for repeated operations.

### Robust Input Handling:

Invalid numbers are caught and retried.

Division by zero is explicitly handled.

### Clearer Structure:

Operations are stored in a dictionary for easy expansion.

Separation of concerns between input, calculation, and output.

### User Experience:

Reduced sleep time to 1 second.

Clear error messages.

Consistent prompts.

## Overview

Within my code there was lots of repeat/copy and pasting for each function which caught the attention of the person who gave me feedback. So I followed a youtube guide on "how to make a CLI calculator" I took inspiration on rewriting my code which kept it clean and had less recursions. 
There was another issue that visually there the input system. I had set up the input system which that allows numbers in but I didn't have a value handler which tells the user to only enter in numbers ONLY. I had also changed my code to have more while loops instead of regular loops for safer execution 
