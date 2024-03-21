import tkinter as tk
from tkinter import scrolledtext, messagebox
import nbformat
from nbconvert import PythonExporter
import io
import sys
from contextlib import redirect_stdout
import re

class MovieRecommendationApp:
    def __init__(self, master):
        self.master = master
        master.title("Movie Recommendation System")

        self.label = tk.Label(master, text="Enter a movie:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.get_recommendations)
        self.submit_button.pack()

        self.output_text = scrolledtext.ScrolledText(master, width=40, height=10)
        self.output_text.pack()

    def get_recommendations(self):
        input_movie = self.entry.get().strip()
        if not input_movie:
            messagebox.showerror("Error", "Please enter a movie.")
            return

        try:
            with open('Projectpyt.ipynb', 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
                exporter = PythonExporter()
                python_code, _ = exporter.from_notebook_node(nb)

            # Capture stdout
            stdout = io.StringIO()
            sys.stdout = stdout

            # Execute the code
            exec(python_code)

            # Get the captured output
            output = stdout.getvalue()

            # Display the recommendations
            self.output_text.delete('1.0', tk.END)
            self.output_text.insert(tk.END, output)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        # Reset stdout
        sys.stdout = sys.__stdout__

root = tk.Tk()
app = MovieRecommendationApp(root)
root.mainloop()
