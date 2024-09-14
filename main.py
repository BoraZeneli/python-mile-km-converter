from tkinter import *  # Import everything from the Tkinter library for creating GUI

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(miles_input.get())  # Get the value from the entry box and convert it to float
    km = miles * 1.609  # Convert miles to kilometers (1 mile = 1.609 km)
    kilometer_result_label.config(text=f"{km}")  # Update the label with the converted value

# Create a window
window = Tk()
window.title("Miles to Kilometer Converter")  # Set the title of the window
window.config(padx=20, pady=20)  # Add padding around the window

# Entry box for inputting miles
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)  # Position the entry box on the grid

# Label for "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)  # Position the label next to the entry box

# Label that says "is equal to"
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)  # Position the label below the entry box

# Label to display the result in kilometers
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)  # Position the result label in the grid

# Label for "Km"
kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)  # Position the "Km" label next to the result

# Button to trigger the conversion
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)  # Position the button below the result label

# Run the window loop
window.mainloop()
