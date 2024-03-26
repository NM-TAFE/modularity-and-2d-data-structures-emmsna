# Overview
Provides a report addressing the following questions:

```text
Justification for your refactoring decisions.
The challenges you would have faced maintaining and testing the original monolithic code.
How you would modify your refactored code to handle a custom-sized tic-tac-toe game (larger than 3x3), and how 
this implementation would be easier to handle than in the original code.
```

## Justification

I refactored the code into classes because ... ... it provides the following benefits:

1. The code, classes and functions can be reused, programs with reused code are generally smaller, more consistent
and require less effort to write as you can write it in "chunks".
2. It allows for easier maintainability, as you don't have to check duplicated code for the same errors and each 
module can be updated or worked on individually.
3. Testing is easier when the code is modular, as you are not testing duplicated code, and each module can be 
individually tested in smaller, easy to understand chunks.

Without the refactoring, the code would have faced the following challenges:
1. It would not be flexible for different board sizes.
2. It would be more difficult to read and understand and therefore harder to maintain.

## Handling Custom-Sized Tic-Tac-Toe

My implementation can handle custom sizes because:
1. It uses a variable for size
2. The functions that check for a winner or if the board is full, are scalable according to the size
3. The function that draws the board is scalable according to the size variable

On the other hand, the original code could not handle custom sizes because:
1. The board drawing is hard coded to a 3 x 3 size
2. The Win Conditions are hard codes to a 3 x 3 size
3. The function that validates the user input is hard coded to the 3 x 3 size

## Conclusion

The activity allowed me to practice refactoring and to understand the benefits of object-oriented programming. 
I learned that it is worth modularising code, due to its benefits of scalability and maintainability and I will 
apply this knowledge in future projects.