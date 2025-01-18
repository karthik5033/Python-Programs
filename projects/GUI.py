import tkinter as tk
from tkinter import messagebox, scrolledtext

def count_words():
    text = input_text.get("1.0", tk.END).strip()
    word_count = len(text.split())
    word_count_label.config(text=f"Total number of words: {word_count}")

def word_frequency():
    text = input_text.get("1.0", tk.END).strip()
    words = text.split()
    counts = {}
    for word in words:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1

    frequency_output = "\n".join([f"{word}: {count}" for word, count in counts.items()])
    messagebox.showinfo("Word Frequency", frequency_output)

def search_word():
    text = input_text.get("1.0", tk.END).strip()
    search_word = search_entry.get().strip()
    if search_word.lower() in text.lower():
        messagebox.showinfo("Search Result", f"'{search_word}' found in the paragraph.")
    else:
        messagebox.showwarning("Search Result", f"'{search_word}' not found in the paragraph.")

# Create main window
root = tk.Tk()
root.title("Word Operations Tool")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Title Label
title_label = tk.Label(root, text="Word Operations Tool", font=("Arial", 16, "bold"), bg="#4682b4", fg="white")
title_label.pack(pady=10, fill=tk.X)

# Input Text Area
input_label = tk.Label(root, text="Enter your paragraph:", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
input_label.pack(pady=5)
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Arial", 10))
input_text.pack(pady=5)

# Word Count Button
count_button = tk.Button(root, text="Count Words", command=count_words, bg="#5f9ea0", fg="white", font=("Arial", 10, "bold"))
count_button.pack(pady=5)

# Word Count Label
word_count_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
word_count_label.pack(pady=5)

# Word Frequency Button
frequency_button = tk.Button(root, text="Show Word Frequency", command=word_frequency, bg="#5f9ea0", fg="white", font=("Arial", 10, "bold"))
frequency_button.pack(pady=5)

# Search Word Section
search_label = tk.Label(root, text="Enter word to search:", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
search_label.pack(pady=5)
search_entry = tk.Entry(root, font=("Arial", 12), width=20)
search_entry.pack(pady=5)
search_button = tk.Button(root, text="Search Word", command=search_word, bg="#5f9ea0", fg="white", font=("Arial", 10, "bold"))
search_button.pack(pady=5)

# Run the application
root.mainloop()