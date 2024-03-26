# Overview
Provide brief answers to the knowledge-question worksheet.

## Answers

**1. Briefly explain what is modular programming**

Modular programing is the practise of writing code that is organised into Files, Classes and Functions that
allow for resuability and scalability. It is particularly useful for larger programs.


**2. How can you import only a specific function or class from a module in Python? What is the syntax for this?**

By using the import statment! The syntac is:

from [file name] import [Class Name/s]

**3. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or 
pass-by-reference? Justify your answer.** 

Python uses pass-by-object-reference, which is where functions receives its own copy of the reference to an 
object. It doesn't recieve the original reference to the object (like in pass-by-reference), nor its own copy of 
the object (like in pass-by-value). I think it is equally as similar to each of the other two mechanisms for 
different reasons - it won't affect the original object if the object is immutable (like in pass-by-value) but 
it will affect the orginal object if the object is mutable (like in pass-by-reference).

**4. Given the following Python code, what will be the output and why?**

    ```python
    def modify_list(list_):
        list_.append("new")
        list_ = ["completely", "new"]

    items = ["original"]
    modify_list(items)
    print(items)
    ```

It will print a list containing ['original', 'new''].
It does this because the "list_.append" is referencing the global "items" list through the function's parameter (and 
therefore altering it as if it was written as "items.append"), but  "list_" by itself is creating a new local list 
variable - which is not the same as the parameter (even though they look the same!) and this new variable is 
only available inside this function as the scope of the variable is only inside the function.


**5. In Python, even though variables created within a function are local, there are still situations where you can 
modify data outside the scope with a local variable. Explain this anomaly and relate it to both mutability and 
pass by reference.**

There are some situations where you can alter a local variable outside the scope, but only if that variable is a 
mutable type due to Python's parameter pass-by-object-reference mechanism. This is similar to pass-by-reference as
it also alters a local variable outside of the function.

**6. List two benefits of modular coding approaches. How do these benefits assist in the development of medium-sized
applications?**

1 - Reusable code - Benefits medium-sized programs as they can build their own libraries of functions and they can 
update every use of each function as easily as updating the one time, at the source! Reusable code cuts down 
on the overall size of a project as the same code isn't being duplicated, multiple times.

2 - Code is easier to read - It's a huge benefit in the developement of medium-sized applications as modular
programming breaks down the code into small chunks that usually have only the one function. This allows reading
and needing to understand one small piece at a time. Functions can also be given more meaningful names (as the code
doean't need to be trimmed down) when they are modularised, making the piecing them all together coding easier 
to read.