

Student Instructions for Learning Programming Structure
The following detailed step-by-step exercises will guide you through the fundamental principles of structured programming. Follow each instruction carefully, and try to solve the tasks without looking up code examples immediately. 
Use this link to help you solve the each code structure task: https://www.w3schools.com/python/default.asp

1. Sequence (Step-by-Step Execution)
Task: Create a User Information Program
Instructions:
Open your Python environment and create a new file for this task.
Create a new Python file and name it appropriately, such as user_info.py.
In your program, prompt the user to enter their name, age, and favorite color using input statements.
Store each input in a separate variable.
Create a new variable that modifies one of the collected values. For example, calculate what the user’s age will be next year.
Print a message that includes the user’s name, age, favorite color, and the modified variable you created.
Run your program multiple times, entering different values, and verify that it behaves correctly.
✅ Goal: Understand linear execution of code where statements run in order, one after another.

2. Selection (Decision Making)
Task: Determine if a User is Eligible to Vote
Instructions:
Open your Python environment and create a new file for this task.
Write a program that asks the user to enter their age.
Store the user’s age in a variable.
Use an if-else statement to check if the user's age is 18 or older.
If the user is 18 or older, print a message indicating they can vote.
Otherwise, print a message indicating they cannot vote.
Test the program by entering different ages (below 18, exactly 18, and above 18).
Modify the program to include an additional condition that prints a special message if the user is exactly 18 years old.
✅ Goal: Learn how to use conditional statements to control program flow based on user input.

3. Iteration (Loops)
Task: Print a Sequence of Numbers Using a Loop
Instructions:
Open your Python environment and create a new file for this task.
Write a program that prints the numbers from 1 to 10.
Instead of writing each print statement manually, use a loop to automate the process.
Modify your program so that it prints only even numbers in the range.
Further modify the program to allow the user to input the starting and ending numbers for the sequence.
Ensure the program can handle cases where the starting number is greater than the ending number.
Test the program with different values to see if it prints the expected sequences.
✅ Goal: Understand loop structures and how to control repetitive execution in a program.

4. Functions (Reusable Code Blocks)
Task: Create a Function that Performs a Simple Calculation
Instructions:
Open your Python environment and create a new file for this task.
Write a function that takes a single number as input and returns a modified version of that number.
Ensure the function does not print anything directly but returns a value.
In the main program, call the function multiple times with different numbers and store the results in variables.
Print the results to see how the function processes different inputs.
Modify the function so that it can accept two numbers instead of one and returns a calculated result using both numbers.
Call the modified function and verify that it produces the expected outputs.
✅ Goal: Learn how to create and use functions to make code reusable and modular.
Detailed Instructions:
Define a Function with a Single Parameter:
Use the def keyword to define a function that accepts one numerical parameter.
Within the function, perform a calculation or modification using this parameter.
Ensure the function returns the result of this computation without printing anything directly.
Call the Function with Various Inputs:
In the main program, invoke the function multiple times, each with different numerical arguments.
Store the returned results in separate variables for further use.
Display the Results:
Print the stored results to observe how the function processes different inputs.
Modify the Function to Accept Two Parameters:
Update the function definition to accept an additional numerical parameter.
Implement a calculation that utilizes both parameters to produce a result.
Return the computed result without direct printing within the function.
Test the Modified Function:
In the main program, call the updated function with various pairs of numerical inputs.
Store and print the results to verify the function's behavior with two parameters.
Key Considerations:
Function Definition:
Ensure that the function is defined before it is called in the main program.
Use descriptive names for both the function and its parameters to enhance code readability.
Return Statement:
The function should use the return statement to send the computed result back to the caller.
Avoid using print statements within the function to maintain separation between computation and output.
Function Calls:
When calling the function, provide appropriate arguments corresponding to the parameters defined.
Store the returned values in variables if further processing or display is needed.
Testing:
Test the function with a variety of input values to ensure it handles different cases correctly.
Consider edge cases, such as zero or negative numbers, to verify robustness.
Search Prompts for Further Learning:
To deepen your understanding and find practical examples, you can explore the following topics:
"Python function definition"
"Python return statement"
"Python function parameters and arguments"
"Python function call"
"Python function testing"

5. Modularization (Using Multiple Files)
Task: Create a Helper Module for Reusable Functions
Instructions:
Open your Python environment and create a new folder for this task.
Inside the folder, create two separate Python files:
One file will contain a function definition that performs a basic mathematical operation.
The second file will import and use the function from the first file.
Ensure the function in the first file does not run on its own but only works when imported.
In the second file, call the function with multiple different values and print the results.
Run the second file and verify that the output is correct.
Modify the program so that the function returns multiple values instead of just one.
Test the modified version and ensure it still works correctly.
✅ Goal: Learn how to structure a program into multiple files and import reusable functions.
Detailed Instructions:
Create the Function Definition File (math_helper.py):
Define the Function:
Implement a function that accepts a list of numbers and calculates basic statistics such as total, average, minimum, and maximum.
Ensure the function returns these statistics as multiple values.
Prevent Unintended Execution:
Include a conditional statement to ensure that the function executes only when explicitly called, preventing it from running during import.
Create the Main Program File (Modularization.py):
Import the Function:
Use the appropriate import statement to bring the function from math_helper.py into this file.
Prepare Test Data:
Define various lists of numbers to test the function's versatility.
Call the Function:
Iterate over the test data, passing each list to the imported function.
Capture the returned statistics and print them in a readable format.
Run and Verify the Program:
Execute the Main Program:
Run Modularization.py to ensure it correctly imports the function and processes the test data.
Validate the Output:
Check that the printed statistics match the expected results for each test case.
Modify the Function to Return Multiple Values:
Update the Function:
Adjust the function in math_helper.py to return additional statistics or data points as needed.
Test the Modified Function:
Update Modularization.py to handle the additional returned values.
Run the program again to ensure it processes the updated function correctly.
Key Considerations:
File Structure:
Ensure both math_helper.py and Modularization.py are in the same directory or properly reference each other to facilitate importing.
Function Importing:
Use the correct syntax to import the function, ensuring the module name matches the filename without the .py extension.
Returning Multiple Values:
When a function returns multiple values, they are typically returned as a tuple.
In the main program, unpack these values into separate variables for clarity.
Search Prompts for Further Learning:
To deepen your understanding and find practical examples, you can explore the following topics:
"Python import function from another file"
"Python function returning multiple values"
"Python if name == 'main' explained"

Create a math_helper.py file: copy this code and place it there. This file will be used as an import for Modularization.py
math_helper.py
def calculate_stats(numbers):
    """Calculate basic statistics for a list of numbers.
    Returns: total, average, minimum, maximum"""
    if not numbers:
        raise ValueError("List cannot be empty")
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum



6. Object-Oriented Programming (OOP)
Task: Create a Class and Work with Objects
Instructions:
Open your Python environment and create a new file for this task.
Define a class that represents a real-world object (e.g., a car, a person, or a book).
The class should have at least two attributes (e.g., brand and model for a car).
Inside the class, define a method that prints or returns information about the object.
Create an instance (object) of the class in the main program.
Call the method you created and verify that it behaves as expected.
Modify the class by adding an additional attribute and method.
Create multiple objects of the class and use them in the program.
✅ Goal: Learn the basics of Object-Oriented Programming (OOP), including classes, objects, attributes, and methods.
Building upon our previous discussion on Object-Oriented Programming (OOP), let's focus on creating a Book class with the attributes: title, author, pages, and is_open. This exercise will help you understand how to define classes, initialize objects, and manage their state in Python.
Detailed Instructions:
Define the Book Class:
Use the class keyword to define a new class named Book.
Ensure the class name follows the PascalCase naming convention.
Initialize Attributes:
Implement the __init__ method to initialize the object's attributes.
The __init__ method should accept parameters for title, author, and pages.
Set the is_open attribute to a default value indicating whether the book is open or closed.
Define Methods:
__str__ Method:
Implement the __str__ method to return a string representation of the book, including its title and author.
open_book Method:
Define a method named open_book that changes the is_open attribute to indicate the book is open.
close_book Method:
Define a method named close_book that changes the is_open attribute to indicate the book is closed.
Create Instances:
In the main part of your program, create instances of the Book class with different titles, authors, and page counts.
Interact with the Objects:
Call the open_book and close_book methods on the instances to change their state.
Print the string representation of each book to verify the __str__ method works as intended.
Enhance the Class:
Add a method to display the current status of the book, indicating whether it is open or closed.
Create additional instances to demonstrate the class's functionality.
Additional Tips:
Method Naming: Use descriptive names for your methods to clearly indicate their purpose.
Attribute Access: Use the self keyword to access instance attributes and methods within the class.
Testing: After defining your class and methods, thoroughly test them by creating multiple instances and calling various methods to ensure they behave as expected.
Search Prompts for Further Learning:
To deepen your understanding and find practical examples, you can explore the following topics:
"Python class definition"
"Python init method"
"Python str method"
"Python instance methods"
"Python object-oriented programming examples"


7. Data Structures & Algorithms
Task: Work with Lists and Sorting
Instructions:
Open your Python environment and create a new file for this task.
Define a list that contains at least five numerical values.
Print the list in its original order.
Write a program that sorts the list in ascending order and prints the sorted list.
Modify the program to allow the user to input values into the list instead of using predefined numbers.
Ensure the program correctly sorts different sets of numbers.
Modify the sorting logic so that the list is sorted in descending order instead of ascending.
Print the final sorted list and verify that it’s correct.
✅ Goal: Learn how to use lists and sorting algorithms in a structured program.
Detailed Instructions:
Define a List with Predefined Numerical Values:
Begin by creating a list containing at least five numerical values. This will serve as your initial dataset.
Print the Original List:
Display the list in its original order to provide a reference point before any sorting operations.
Sort the List in Ascending Order:
Utilize Python's built-in sorting capabilities to arrange the list from the smallest to the largest value.
After sorting, print the list to verify the order.
Modify the Program for User Input:
Instead of using a predefined list, prompt the user to input numerical values.
Collect these inputs and store them in a list.
Ensure that the program can handle multiple entries and that the user can indicate when they have finished entering data.
Sort and Display the User-Provided List:
Once the user has finished entering numbers, sort the list in ascending order and display it.
Sort the List in Descending Order:
Modify the sorting logic to arrange the list from the largest to the smallest value.
Print the list to confirm the new order.
Key Considerations:
User Input Handling:
Prompt the user clearly to enter numerical values.
Implement a mechanism to allow the user to finish inputting data, such as pressing Enter without typing a number.
Validate the input to ensure that only numerical values are accepted, and handle any invalid inputs gracefully.
Sorting Mechanisms:
Understand the difference between in-place sorting (which modifies the original list) and creating a sorted copy of the list.
Be aware of how to reverse the sorting order to achieve descending arrangement.
Search Prompts for Further Learning:
To deepen your understanding and find practical examples, you can explore the following topics on W3Schools:
"Python Lists"
"Python User Input"
"Python List sort() Method"
"Python sorted() Function"
"Python String isnumeric() Method"

8. Debugging & Error Handling
Task: Handle Invalid User Input
Instructions:
Open your Python environment and create a new file for this task.
Write a program that asks the user for a numerical input.
Store the input in a variable and attempt to convert it into an integer.
If the user enters an invalid value (e.g., text instead of a number), handle the error gracefully and print a message prompting them to try again.
Ensure that the program does not crash when an invalid input is entered.
Modify the program so that it keeps asking for input until the user provides a valid number.
Once a valid number is entered, print a confirmation message and end the program.
✅ Goal: Learn how to handle exceptions and prevent programs from crashing due to invalid user input.

Detailed Instructions:
Prompt the User for Input:
Use Python's input function to display a message requesting the user to enter a number.
Store the user's response in a variable for further processing.
Attempt to Convert Input to an Integer:
Try to convert the user's input from a string to an integer, as input returns data in string format by default.
Be aware that if the user enters non-numeric text, this conversion will raise a ValueError.
Implement Exception Handling:
Utilize a try-except block to catch exceptions that occur during the conversion process.
If a ValueError is raised, display an error message informing the user of the invalid input and prompt them to try again.
Loop Until Valid Input is Received:
Encapsulate the input and conversion logic within a loop that continues to prompt the user until a valid integer is entered.
Once a valid integer is obtained, exit the loop.
Confirm Successful Input:
After receiving a valid integer, display a confirmation message to the user, indicating the successful input.
Key Considerations:
User Experience:
Provide clear and concise prompts to guide the user in entering the correct data.
Ensure that error messages are informative but not overwhelming, encouraging the user to correct their input.
Exception Handling:
Focus on catching specific exceptions, such as ValueError, to handle known error conditions effectively.
Avoid using broad exception handling (e.g., a bare except clause) as it can obscure other potential issues in the code.
Loop Control:
Implement a loop that continues to prompt the user until valid input is received, ensuring the program can handle multiple invalid attempts gracefully.
Search Prompts for Further Learning:
To deepen your understanding and find practical examples, you can explore the following topics on W3Schools:
"Python input() function"
"Python try-except blocks"
"Python exception handling"
"Python ValueError exception"


