HIROGLIFX

** due to updates a lot of this manual is deprecated. I am updating the
** docs as quickly as possible, but if you are unsure about what currently works
** please consult the Progress.txt file or Progress Stats.py

Table of Contents:

1:What is HIROGLIFX?
2:Creating a HIROGLIFX project
3:Ints & Strings
4: Decorators and Variable Declaration
5: Keywords
6: UI (User Input)
7: Loops
8: User Generated Functions
9: BluePrints

1.What is HIROGLIFX?

HIRO or HIROGLIFX is a high level interpreted (toy) language implemented in Python. It's purpose is to help
people who want to learn to write code by using a very basic syntax.
It's basic rules are as followed. 

2. Creating a HIROGLIFX project

To start a HIROGLIFX project simply work within the scroll.glif file within the root directory.
All code for your project goes into this file.Run the main.py file to see what your
code outputs.

** Note scrolls (scroll.glif files) are automatically generated within a while loop for your convenience
** If you need to break out of the loop simply use the brk keyword within an @inside@ boolean
statement.(check the scroll file in the Hello World folder in this directory for an example)
***. If this file did not contain the brk keyword it would run in an infinite loop
***(which would be annoying).

3. Ints(Nums) & Strings

Ints or Nums are described as integers that do not contain a decimal point.
They can perform various operations including addition, subtraction, etc.
All Strings are ASCII characters not including numbers contained within a
pair of "".

4. Decorators & Variable Declaration

Decorators are simply ASCII characters reserved for specific operations or uses in HIRO.
The ! decorator is used to express a conditional statement. These include if and else statements.
In addition use the # decorator to begin declaration of an integer or 'num', and $ for strings. Enclose the 
variable name followed by the 'VAR' keyword within the proper decorator.
Be sure that the closing decorator and equal sign have no space between them.  

Variable Declaration Examples:

# x var #= 3
$ name var $= "Noah"

As you can see variable names are capitalized within the structure (Decorator Variable_Name VARDecorator=). Also strings need
quotations to be stored in memory. You can get a variable's data by typing (Decorator VARNAME VAR). 

5. Keywords

There are many keywords that are used for specific circumstances within HIROGLIFX. All keywords are capitalized
within HIRO for readability purposes. They are as followed:

write():

To print to the terminal use the keyword WRITE(). You can write all data types, and the values of variables that have already been
declared.

!if!{}:

!if()!{} is the construction for an if statement within HIRO. The proper structure is as follows:

!if (CONDITION)!{EXECUTE THIS()}

As you can see the if statement checks the condition within the logical decorator (!!) and executes the code within the
{} if this condition evaluates to True.

** IF-NOT is deprecated
!IF-NOT()!{} checks if a condition is not true and executes the condtion within the {} if this is the case.
It is the main form of negation within HIROGLIFX.

!IF-NOT(2 < 1)!{EXECUTE THIS()}

@inside@:
This keyword checks whether a string variable is inside of another string variable.

$ FIRSTSTRING VAR $=New
$ SCNDSTRING VAR $=N

!IF( $ SCNDSTRING var $ @inside@ $ FIRSTSTRING var $)!{WRITE{'FOUND N')}

brk:

The brk keyword is used to break out of loops. It needs to be given an if condition and it executes when this condition
is satisfied.

6. User Input

User Input is gathered by using the UI(' ') command. A user's input can be saved to a
variable using the following syntax:

$^ n var ^$= UI(What is your name?")

After saving this variable you can treat it like any other variable to perform
operations as you desire.

7. Loops

HiroGlifx currently offers one type of loop, a "loop_through" loop that is similar to a for loop.
Being that HiroGlifx is automatically generated within a while loop, a while loop
is never necesary to run HiroGlifx. Here is an example of a loop_through loop.

loop_through(val=3:data_store=x){
write(3), write(u)

The val variable represents the amount of iterations that you want to occur on a piece
of data, data store stores the data of each iteration during the time of each
iteration.