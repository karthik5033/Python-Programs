import tkinter as tk
from tkinter import messagebox, scrolledtext

# Create the main application window
root = tk.Tk()
root.title("Word Operations Tool")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Add a title label at the top
title_label = tk.Label(
    root,
    text="Word Operations Tool",
    font=("Arial", 16, "bold"),
    bg="#4682b4",
    fg="white"
)
title_label.pack(pady=10, fill=tk.X)

# Add a label and text area for paragraph input
input_label = tk.Label(
    root,
    text="Enter your paragraph:",
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#333333"
)
input_label.pack(pady=5)
input_text = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=50,
    height=10,
    font=("Arial", 10)
)
input_text.pack(pady=5)

# Add a button and label for word count operations
count_button = tk.Button(
    root,
    text="Count Words",
    bg="#5f9ea0",
    fg="white",
    font=("Arial", 10, "bold")
)
count_button.pack(pady=5)
word_count_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#333333"
)
word_count_label.pack(pady=5)

# Add a button for word frequency operations
frequency_button = tk.Button(
    root,
    text="Show Word Frequency",
    bg="#5f9ea0",
    fg="white",
    font=("Arial", 10, "bold")
)
frequency_button.pack(pady=5)

# Add a label, entry, and button for word search operations
search_label = tk.Label(
    root,
    text="Enter word to search:",
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#333333"
)
search_label.pack(pady=5)
search_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=20
)
search_entry.pack(pady=5)
search_button = tk.Button(
    root,
    text="Search Word",
    bg="#5f9ea0",
    fg="white",
    font=("Arial", 10, "bold")
)
search_button.pack(pady=5)

# Initialize variables
paragraph_text = ""
word_counts = {}

# Define functionality for counting words
count_button.config(command=lambda: count_words())

def count_words():
    global paragraph_text
    paragraph_text = input_text.get("1.0", tk.END).strip()
    word_count = len(paragraph_text.split())
    word_count_label.config(text=f"Total number of words: {word_count}")

# Define functionality for word frequency
frequency_button.config(command=lambda: word_frequency())

def word_frequency():
    global word_counts
    word_counts = {}
    words = paragraph_text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    frequency_output = "\n".join([f"{word}: {count}" for word, count in word_counts.items()])
    messagebox.showinfo("Word Frequency", frequency_output)

# Define functionality for searching a word
search_button.config(command=lambda: search_word())

def search_word():
    search_word = search_entry.get().strip()
    if search_word in paragraph_text:
        messagebox.showinfo("Search Result", f"'{search_word}' found in the paragraph.")
    else:
        messagebox.showwarning("Search Result", f"'{search_word}' not found in the paragraph.")

# Start the main event loop
root.mainloop()
