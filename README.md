# PyQt6 Calculator

This is a simple calculator application built using PyQt6. The application supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Classes and Methods

### `Calculator` Class
- **Purpose**: This class represents the main window of the calculator application.
- **Methods**:
  - `__init__(self)`: Initializes the calculator window and sets up the UI.
  - `initUI(self)`: Connects the buttons to their respective functions.
  - `append_number(self, number)`: Appends a number to the display.
  - `append_operator(self, operator)`: Appends an operator to the display.
  - `calculate_result(self)`: Evaluates the expression and displays the result.
  - `clear_display(self)`: Clears the display.
  - `change_sign(self)`: Changes the sign of the current number.
  - `delete_number(self)`: Deletes the last character from the display.

## How to Run

1. Ensure you have Python and PyQt6 installed. You can install PyQt6 using pip:
   ```sh
   pip install PyQt6
    ```
2. Run the `main.py` file:
    ```sh
   python main.py
    ```

## Sample Input/Output
### Example 1
**Input**: 5 + 3 = **Output**: 8
<img width="387" alt="Снимок экрана 2025-03-11 в 11 38 06" src="https://github.com/user-attachments/assets/ae3b4920-8e7b-46a2-94f7-bd101c791b73" />

### Example 2
**Input**: 10 / 2 = **Output**: 5
<img width="384" alt="Снимок экрана 2025-03-11 в 11 38 27" src="https://github.com/user-attachments/assets/4f059c5f-5e72-45cb-830b-b2b40eb07746" />

### Example 3
**Input**: 7*6 = **Output**: 42
<img width="388" alt="Снимок экрана 2025-03-11 в 11 38 49" src="https://github.com/user-attachments/assets/40411c57-926c-4741-9555-d5afbd8e6959" />

### Example 4
**Input**: 10 / 0 = **Output**: undefined
<img width="382" alt="Снимок экрана 2025-03-11 в 11 40 53" src="https://github.com/user-attachments/assets/7926f164-383b-4d33-a8f4-4375853dd65e" />

