# Quiz App Using Python and Tkinter

This is a Python application that creates a quiz using the Tkinter library for the graphical user interface. It allows users to answer a series of questions and provides feedback on their answers.

## Prerequisites

Before running this application, make sure you have the following:

- **Python** installed on your computer.
- The **tkinter** library, which is included in Python's standard library.
- The **ttkbootstrap** library for improved styling (you can install it using `pip install ttkbootstrap`).

## Usage

1. **Import the necessary modules**:

   ```python
   import tkinter as tk
   from tkinter import messagebox, ttk
   from ttkbootstrap import Style
   from quiz_data import quiz_data
   ```

2. **Define functions** for displaying questions, checking answers, and moving to the next question.

3. **Create the main window** and configure its appearance:

   ```python
   root = tk.Tk()
   root.title("Quiz App")
   root.geometry("600x500")
   style = Style(theme="flatly")
   ```

4. **Create labels** for the question, feedback, and score.

5. **Create choice buttons** for answering questions.

6. **Initialize the score** and set up the "Next" button for navigation.

7. **Show the first question**.

8. **Start the main event loop**:

   ```python
   root.mainloop()
   ```

## How It Works

- Questions and choices are defined in an external **quiz_data.py** file, which you can customize to create your quiz.

- Users click on choice buttons to answer questions.

- The application provides immediate feedback on whether the answer is correct or incorrect and updates the user's score.

- Once all questions are answered, a message box displays the final score, and the quiz ends.

Feel free to **modify the quiz_data.py** file to create your quiz content. Enjoy using and customizing this quiz app!

## Author

Shubh Patel
```

You can copy and paste this text into Sublime Text while maintaining the bold formatting for headings and code blocks.
