## RomanNumeralConverter

### Table of Contents
- [Description](#Description)
- [Application](#Application)
- [Tkinter](#Tkinter)
- [Running](#Running)

---

### Description

This project utilizes Python and Tkinter to create an application for converting Roman Numeral data into Numerical Data, displaying the result within the application's interface. The goal is to provide users with a Graphical User Interface (GUI) where they can input a valid Roman Numeral and receive its corresponding Decimal Number. The application verifies the validity of the input and provides feedback if the input is invalid.

---

### Application

The project consists of three main files: "RomanNumeral.py" as the driver, "GUI.py" managing the GUI and data, and "Converter.py" processing user input.

- **RomanNumeral.py**: This file imports the GUI class from "GUI.py" to construct the GUI and initiates the application by invoking the GUI constructor.

- **GUI.py**: This module imports the `tkinter` module for GUI construction, along with necessary functionality from "Converter.py" for Roman Numeral to Decimal conversions. The GUI class is defined here, setting up the application window, labels, entry fields, buttons, and the mainloop function to run the application.

- **Converter.py**: This file imports the `re` module for pattern matching and text manipulation. The Converter class within includes a dictionary variable for Roman Numeral scoring (e.g., I = 1, V = 5, X = 10, L = 50, etc.) and methods to validate and convert Roman Numerals to Decimal values.

  - `valid_input`: This method uses the `re` module to validate Roman Numeral inputs entered by users.
  
  - `RomanNumeralToDecimal`: This method performs the conversion by iterating through the string and comparing values to calculate the Decimal result.

---

### Tkinter

Tkinter is a standard Python library used to create graphical user interfaces (GUIs). It provides a set of tools and widgets to design desktop applications with elements such as windows, buttons, labels, and text boxes. Tkinter simplifies GUI design, event handling, and user interactions.

Developers can customize widgets, handle user input, display data, and interact with other Python modules. Tkinter's simplicity makes it suitable for both beginners and experienced developers.

Tkinter is included in Python's standard library, making it readily available without external dependencies.

---

### Running

To run the application, download the executable file from the "Releases" section of the repository. Double-click the executable to execute the application on your operating system. This application is designed to work on all major operating systems (e.g., Windows, Mac, Linux).

