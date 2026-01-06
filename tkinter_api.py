
import tkinter as tk
from tkinter import scrolledtext
from api import get_recipes  # make sure this matches your api.py file


def fetch_and_show():
    food = food_entry.get()
    meals = get_recipes(food)
   
    result_text.delete(1.0, tk.END)
   
    if meals is None:
        result_text.insert(tk.END, "Recipe not found!")
    else:
        for meal in meals:
            result_text.insert(tk.END, "-------------------\n")
            result_text.insert(tk.END, f"Recipe: {meal['strMeal']}\n")
            result_text.insert(tk.END, f"Category: {meal['strCategory']}\n")
            result_text.insert(tk.END, f"Area: {meal['strArea']}\n")
            result_text.insert(tk.END, f"Instructions: {meal['strInstructions']}\n\n")


root = tk.Tk()
root.title("Recipe Finder")


tk.Label(root, text="Enter food:").pack(pady=5)
food_entry = tk.Entry(root, width=30)
food_entry.pack(pady=5)


tk.Button(root, text="Find Recipe", command=fetch_and_show).pack(pady=5)


result_text = scrolledtext.ScrolledText(root, width=60, height=20)
result_text.pack(pady=10)


root.mainloop()