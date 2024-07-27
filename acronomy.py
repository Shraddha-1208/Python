import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def get_initials(phrase):
    """
    This function takes a phrase as input, splits it into words,
    and returns a string containing the uppercase initials of each word.
    """
    words = phrase.split()
    initials = ""
    for word in words:
        initials += word[0].upper()
    return initials

def on_submit():
    """
    Callback function to handle the submit button click event.
    """
    user_input = entry.get()
    if user_input:
        initials = get_initials(user_input)
        result_label.config(text=f"Initials: {initials}")
    else:
        messagebox.showwarning("Input Error", "Please enter a phrase.")

# Set up the main application window
root = tk.Tk()
root.title("Initials Extractor")
root.geometry("400x200")
root.configure(bg="#f0f0f0")

# Create a style for ttk widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TEntry", font=("Helvetica", 12), padding=6)
style.configure("TFrame", background="light blue")
# Create and place the widgets
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Enter a Phrase:")
label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry = ttk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5, pady=5)

submit_button = ttk.Button(frame, text="Get Initials", command=on_submit)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="Initials will be displayed here.")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

# Adjust column weights for responsiveness
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
