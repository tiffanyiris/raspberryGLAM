# **GLAM_General Using Python and Tkinter**

This is a Python application that creates a quiz using the Tkinter library for the graphical user interface. It allows users to answer a series of questions and provides feedback on their answers.

## **Prerequisites**

Before running this application, make sure you have the following:

- **Python** installed on your computer.
- The **tkinter** library, which is included in Python's standard library.
- The **ttkbootstrap** library for improved styling (you can install it using `pip install ttkbootstrap`).

## **Usage**

1. **Import the necessary modules**:

   ```python
   import tkinter as tk
   from tkinter import messagebox, ttk
   from ttkbootstrap import Style
   from quiz_data import quiz_data
   ```

2. **Define functions for displaying questions, checking answers, and moving to the next question**:

   ```python
   # Function to display the current question and choices
   def show_question():
       # Get the current question from the quiz_data list
       question = quiz_data[current_question]
       qs_label.config(text=question["question"])

       # Display the choices on the buttons
       choices = question["choices"]
       for i in range(4):
           choice_btns[i].config(text=choices[i], state="normal") # Reset button state

       # Clear the feedback label and disable the next button
       feedback_label.config(text="")
       next_btn.config(state="disabled")

   # Function to check the selected answer and provide feedback
   def check_answer(choice):
       # Get the current question from the quiz_data list
       question = quiz_data[current_question]
       selected_choice = choice_btns[choice].cget("text")

       # Check if the selected choice matches the correct answer
       if selected_choice == question["answer"]:
           # Update the score and display it
           global score
           score += 1
           score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
           feedback_label.config(text="Correct!", foreground="green")
       else:
           feedback_label.config(text="Incorrect!", foreground="red")

       # Disable all choice buttons and enable the next button
       for button in choice_btns:
           button.config(state="disabled")
       next_btn.config(state="normal")

   # Function to move to the next question
   def next_question():
       global current_question
       current_question +=1

       if current_question < len(quiz_data):
           # If there are more questions, show the next question
           show_question()
       else:
           # If all questions have been answered, display the final score and end the quiz
           messagebox.showinfo("Quiz Completed",
                               "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
           root.destroy()
   ```

3. **Create the main window and configure its appearance**:

   ```python
   root = tk.Tk()
   root.title("Quiz App")
   root.geometry("600x500")
   style = Style(theme="flatly")
   ```

4. **Create labels for the question, feedback, and score**:

   ```python
   # Create the question label
   qs_label = ttk.Label(
       root,
       anchor="center",
       wraplength=500,
       padding=10
   )
   qs_label.pack(pady=10)
   
   # Create the feedback label
   feedback_label = ttk.Label(
       root,
       anchor="center",
       padding=10
   )
   feedback_label.pack(pady=10)

   # Create the score label
   score_label = ttk.Label(
       root,
       text="Score: 0/{}".format(len(quiz_data)),
       anchor="center",
       padding=10
   )
   score_label.pack(pady=10)
   ```

5. **Create choice buttons for answering questions**:

   ```python
   # Create choice buttons for answering questions
   choice_btns = []
   for i in range(4):
       button = ttk.Button(
           root,
           command=lambda i=i: check_answer(i)
       )
       button.pack(pady=5)
       choice_btns.append(button)
   ```

6. **Initialize the score and set up the "Next" button for navigation**:

   ```python
   # Initialize the score
   score = 0

   # Create the next button
   next_btn = ttk.Button(
       root,
       text="Next",
       command=next_question,
       state="disabled"
   )
   next_btn.pack(pady=10)
   ```

7. **Initialize the current question index and show the first question**:

   ```python
   # Initialize the current question index
   current_question = 0

   # Show the first question
   show_question()
   ```

8. **Start the main event loop**:

   ```python
   root.mainloop()
   ```

## **How It Works**

- Questions and choices are defined in an external **quiz_data.py** file, which you can customize to create your quiz.

- Users click on choice buttons to answer questions.

- The application provides immediate feedback on whether the answer is correct or incorrect and updates the user's score.

- Once all

 questions are answered, a message box displays the final score, and the quiz ends.

Feel free to **modify the quiz_data.py** file to create your quiz content. Enjoy using and customizing this quiz app!



# Astronomy README

## Overview

This MCQ (Multiple Choice Questions) Quiz Application is a simple Python program designed to create an interactive quiz experience for users. It includes a graphical user interface (GUI) built using the Tkinter library and provides a quiz with questions, options, and images downloaded from the internet.

**Important**: This quiz requires an internet connection to download images for questions.

## Prerequisites

Before running the MCQ Quiz Application, ensure you have the required libraries installed. You can install these libraries using pip:

```bash
pip3 install requests pillow
```

- `Tkinter`: Tkinter is a standard Python library used for creating graphical user interfaces (GUIs). It provides widgets like buttons, labels, text fields, and frames for building interactive applications.

- `JSON Library`: The JSON library is used to work with JSON (JavaScript Object Notation) data, which stores questions, options, and answers for the quiz.

- `Requests Library`: The Requests library is used for making HTTP requests to retrieve data from external sources, such as images. It is used to download images for the quiz questions.

- `Pillow (PIL) Library`: Pillow, often referred to as the Python Imaging Library (PIL), is used for opening, manipulating, and displaying images. It allows you to work with various image formats and perform operations like resizing and displaying images.

- `BytesIO from io Library`: The BytesIO module from the io library is used to handle binary data as if it were a file. It is used to convert binary image data (from the Requests library) into an image format compatible with Pillow and Tkinter.

- `OS Library`: The OS library provides a way to interact with the operating system, including file and directory operations. It is used to change the working directory to the one containing the quiz data (questions.json).

**Optional**:

- `BeautifulSoup (bs4)`: BeautifulSoup is a library used for web scraping and parsing HTML and XML documents. While not required for basic functionality, you may need it if you plan to scrape data from web pages to generate quiz questions programmatically.

## Usage

1. Clone this repository to your local machine or download the source code.

2. Install the required libraries if you haven't already (Tkinter, JSON, Requests, Pillow).

```bash
pip3 install requests pillow
```

3. Open your terminal or command prompt and navigate to the directory containing the MCQ Quiz Application files.

4. Run the application by executing the Python script:

```bash
python3 mcq_quiz.py
```

5. The application will launch with a GUI for entering user details, including name and age. Ensure you have an internet connection.

6. After entering your details, click the "DONE" button to start the quiz.

7. Answer the quiz questions using the provided options and click the "NEXT" button to move to the next question. You can also use the "BACK" button to go back to previous questions.

8. Once you've completed all the questions, a "Submit Quiz" button will appear. Click it to see your results.

9. The application will display the number of correct and incorrect answers. Additionally, it will list the questions you answered incorrectly.

10. Your quiz details, including your name, age, and score, will be saved in a text file called "details.txt" for reference.

## Important Notes

- This quiz assumes that the user is 15 years old. If the age entered is not 15, the application will display an error message and exit.

- Users can only play the quiz once, as their name is checked against the "details.txt" file to prevent multiple attempts.

- Ensure you have a stable internet connection to download images for the quiz questions.

- The quiz consists of multiple-choice questions with images. Users can navigate through questions using the "NEXT" and "BACK" buttons.


Enjoy the quiz!

## **Author**

Shubh Patel
```
