import tkinter as tk
from Converter import *

class GUI(object):
    
    def __init__(self):
        '''
        Constructor for the GUI class.
        Initializes the main application window and sets up GUI elements.
        '''
        # Create a window
        self.window = tk.Tk()

        # Set the window title
        self.window.title("Roman Numeral Conversion App")

        # Set the size, shape, and location of the application window
        self.Set_Geometry()

        # Create a label for the Roman Numeral entry field
        self.name_label = tk.Label(self.window, text="Enter Roman Numerals Here:")
        self.name_label.pack()

        # Create an entry field for the user to enter Roman Numerals
        self.user_entry = tk.Entry(self.window)
        self.user_entry.pack()

        # Create a button to trigger the conversion
        self.convert_button = tk.Button(self.window, text="Convert!", command=self.Convert_Value)
        self.convert_button.pack()

        # Create a label to display the conversion result
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Run the application
        self.window.mainloop()

    def Set_Geometry(self):
        '''
        Set the size, shape, and location of the application window.
        '''
        # Set the minimum size that the application window is allowed to be 
        size = 500 

        # Get the resolution of the device window that the application is running on
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Get the center X-position and the center Y-position for the application window
        x = (screen_width - size) // 2
        y = (screen_height - size) // 2

        # Set the size and location of the application
        self.window.geometry(f"{size}x{size}+{x}+{y}")

        # Set the minimum size that the application window is allowed to be 
        self.window.minsize(size, size)

    def Convert_Value(self):
        '''
        Handles the conversion of the input entered by the user.
        '''
        # Get the input entered by the user
        user_input = self.user_entry.get()

        # Check if the input entered by the user is valid
        if Converter().valid_input(user_input):
            # If input is valid, convert the Roman Numeral to Decimal
            result = Converter().RomanNumeralToDecimal(user_input)
            self.result_label.config(text=result)
        else:
            # If input is invalid, display an error message
            self.result_label.config(text='Invalid Input! Please Enter a Valid Roman Numeral!')
