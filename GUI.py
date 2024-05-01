import tkinter as tk
from tkinter import ttk
import time
from dynamic_program import min_edit_distance_dp
from dynamic_program_space import min_edit_distance_space_optimized
from recursive import med_recursive
from divide_n_conquer import divide_and_conquer


class GUI:

    def __init__(self,root):
        self.root = root
        self.root.title("Minimum Edit Distance")
        self.root.geometry("300x300")

        self.label1 = tk.Label(self.root, text="String 1")
        self.label1.pack()
        self.str1 = tk.Entry(self.root, width=20)
        self.str1.pack(pady=10)

        self.label2 = tk.Label(self.root, text="String 2")
        self.label2.pack()
        self.str2 = tk.Entry(self.root, width=20)
        self.str2.pack(pady=10)

        self.label3 = tk.Label(self.root, text="Method")
        self.label3.pack()
        self.method = ttk.Combobox(self.root, values=["Dynamic Programming", "Space Optimized DP", "Recursive", "Divide and Conquer"])
        self.method.pack(pady=10)


        self.calculate = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate.pack(pady=10)


        self.result = tk.Label(self.root, text="")
        self.result.pack()

    def calculate(self):
        s1 = self.str1.get()
        s2 = self.str2.get()
        method = self.method.get()

        if method == "Dynamic Programming":
            start = time.time()
            result = min_edit_distance_dp(s1, s2)
            end = time.time()
        elif method == "Space Optimized DP":
            start = time.time()
            result = min_edit_distance_space_optimized(s1, s2)
            end = time.time()
        elif method == "Recursive":
            start = time.time()
            result = med_recursive(s1, s2)
            end = time.time()
        elif method == "Divide and Conquer":
            start = time.time()
            result = divide_and_conquer(s1, s2)
            end = time.time()

        self.result.config(text=f"Result: {result}\nTime: {end-start:.5f} seconds")


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()