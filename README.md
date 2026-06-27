# 🧮 Windows Style Calculator using Python (Tkinter)

## 📌 Project Overview

This project is a **Windows-style Calculator** built using **Python** and the **Tkinter GUI library**. The application provides a clean and modern user interface inspired by the Windows Calculator and supports basic arithmetic operations along with several scientific functions.

The calculator is designed for beginners who want to learn GUI development in Python while also understanding how event-driven programming works.

---

# ✨ Features

* Modern Windows Calculator inspired UI
* Responsive button layout using Tkinter Grid
* Basic Arithmetic Operations

  * Addition (+)
  * Subtraction (-)
  * Multiplication (×)
  * Division (÷)
* Percentage (%) button (UI available)
* Square (x²)
* Square Root (√x)
* Reciprocal (1/x)
* Positive/Negative Toggle (+/-)
* Decimal Number Support
* Backspace (⌫)
* Clear Entry (CE)
* Clear All (C)
* Error Handling

  * Invalid Input
  * Division by Zero

---

# 🛠️ Technologies Used

* **Python 3**
* **Tkinter** (Python GUI Library)
* **Math Module**

---

# 📂 Project Structure

```
Calculator/
│
├── calculator.py
├── README.md
```

---

# 🚀 How to Run the Project

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Make sure **"Add Python to PATH"** is checked during installation.

---

### Step 2: Download the Project

Clone the repository or download the ZIP file.

```bash
git clone https://github.com/vedpatel31
```

---

### Step 3: Open Terminal

Navigate to the project folder.

```bash
cd calculator
```

---

### Step 4: Run the Program

```bash
python calculator.py
```

The calculator window will open.

---

# 🖥️ User Interface

The calculator consists of two main sections:

### Display Screen

Displays:

* Current input
* Mathematical expression
* Final result

### Button Panel

Contains:

* Number buttons (0–9)
* Arithmetic operators
* Scientific functions
* Clear buttons
* Equal button

The interface uses a dark theme similar to the Windows Calculator.

---

# ⚙️ Working of the Program

## 1. Tkinter Window

The application creates the main window using:

```python
root = tk.Tk()
```

It sets:

* Window title
* Window size
* Background color

---

## 2. Display

The calculator display uses a `StringVar` object.

```python
self.display_var = tk.StringVar(value="0")
```

This automatically updates the label whenever its value changes.

---

## 3. Buttons

All buttons are stored inside a list.

Example:

```python
('7', 2, 0, 'num')
```

Each tuple contains:

* Button text
* Grid row
* Grid column
* Button type

The buttons are generated dynamically using a loop, making the code cleaner and easier to maintain.

---

## 4. Button Click Events

Whenever a button is clicked, the function

```python
on_button_click()
```

is executed.

This function decides what operation should be performed depending on the button pressed.

Examples include:

* Clear screen
* Delete last character
* Perform calculations
* Square a number
* Find square root
* Toggle sign
* Display result

---

## 5. Mathematical Evaluation

The calculator converts visual operators into Python operators.

Example:

```
× → *
÷ → /
```

Then the expression is evaluated using:

```python
eval(expression)
```

The result is displayed on the screen.

---

## 6. Error Handling

The calculator handles common errors using `try-except`.

Examples:

### Division by Zero

```
Cannot divide by zero
```

### Invalid Expression

```
Invalid Input
```

After an error, the calculator resets to its default state.

---

# 📖 Functions Used

| Function            | Purpose                       |
| ------------------- | ----------------------------- |
| `__init__()`        | Initializes the calculator    |
| `create_widgets()`  | Creates display and buttons   |
| `on_button_click()` | Handles button events         |
| `clear_all()`       | Clears the calculator display |

---

# 🎨 UI Color Theme

| Component         | Color          |
| ----------------- | -------------- |
| Background        | Dark Gray      |
| Number Buttons    | #3b3b3b        |
| Operator Buttons  | #323232        |
| Equal Button      | Cyan (#00eee7) |
| Text              | White          |
| Equal Button Text | Black          |

---

# 📌 Supported Operations

| Operation         | Symbol |
| ----------------- | ------ |
| Addition          | +      |
| Subtraction       | -      |
| Multiplication    | ×      |
| Division          | ÷      |
| Square            | x²     |
| Square Root       | √x     |
| Reciprocal        | 1/x    |
| Positive/Negative | +/-    |
| Decimal           | .      |
| Backspace         | ⌫      |
| Clear             | C      |
| Clear Entry       | CE     |

---

# 💡 Concepts Covered

This project demonstrates the following Python concepts:

* Object-Oriented Programming (OOP)
* Classes and Objects
* Tkinter GUI Development
* Event Handling
* Lambda Functions
* Exception Handling
* Mathematical Operations
* Grid Layout Management
* String Manipulation
* Python `eval()` Function

---

# 📈 Future Improvements

Possible enhancements include:

* Memory Functions (MC, MR, M+, M-)
* Calculation History
* Keyboard Input Support
* Scientific Calculator Mode
* Percentage Calculation Logic
* Theme Switching (Dark/Light)
* Expression Preview
* Better Input Validation
* Parentheses Support
* Trigonometric Functions
* Logarithmic Functions

---

# 🎯 Learning Outcomes

By building this project, you will learn how to:

* Create GUI applications using Tkinter
* Organize Python projects using classes
* Handle button click events
* Perform mathematical calculations
* Manage user input
* Implement exception handling
* Design responsive layouts
* Build desktop applications in Python

---

# 👨‍💻 Author

Developed using **Python** and **Tkinter** as a desktop GUI application to demonstrate the implementation of a Windows-style calculator with a clean interface and essential mathematical functionalities.

---

# 📄 License

This project is open-source and available for educational and personal use. You are free to modify, improve, and distribute it with appropriate attribution.
