import time
import tkinter as tk
from tkinter import messagebox 
from database_conn import MieTrak
import logging

logger = logging.getLogger(__name__)

class SearchBar(tk.Toplevel):
    def __init__(self, parent, callback):
        logger.info("search app started")
        super().__init__(parent)
        self.callback = callback  # main app function
        self.title("Search Bar")
        self.geometry("500x500")
        self.lift()
        self.focus_force()
        self.bind("<Escape>", lambda e: e.widget.quit())

        for i in range(3):
            self.columnconfigure(i, weight=1)

        tk.Button(self, text="search", command=self.get_data, background="white").grid(row=0, column=2, sticky="EW")

        self.text_enter_widget()
        self.results_box = tk.Listbox(self, width=100, height=40, selectmode="SINGLE", background="white")
        self.results_box.bind("<<ListboxSelect>>", self.get_selection)
        self.results_box.grid(row=1, column=0, rowspan=10, columnspan=3, sticky="NSEW")
        self.results_box.insert("0", ("Part Number   |   Drawing number   |  Description"))

    def text_enter_widget(self):
        self.text_enter_bar = tk.Entry(self, width=50, background="white")
        self.text_enter_bar.grid(row=0, column=0, columnspan=2, sticky="NSEW")
        
    def get_data(self):
        self.results = []
        value = self.text_enter_bar.get()
        database = MieTrak()
        self.part_num_list = database.pull_part_numbers(value)
        # we put those results after prettifying it in the database
        self.update_results(self.part_num_list)  # Display function - index corresponds to the same element

    def update_results(self, list_to_insert):
        self.results_box.delete("1", tk.END)
        if len(list_to_insert) > 0:
            for item in list_to_insert:
                line = f"{item[1]}   |   {item[2]}   |   {item[3]}"
                self.results_box.insert(tk.END, line) 
        else:
            messagebox.showinfo(title="No result found", message="Try another query")

    def get_selection(self, event):
        try:
            part_number_index = event.widget.curselection()[0]
            if part_number_index or part_number_index == 0:  # without zero, python thinks this statement is false
                part = self.part_num_list[part_number_index - 1]
                if messagebox.askokcancel(title="confirm", message=f"Part Number - {part[1]}, description - {part[2]}"):
                    self.callback(part)  # we run that function before we destory the widget
                    logger.info(f"part selected by user - {part}")
                    self.destroy()
        except IndexError as e:  # in case someone clicks on an empty list box without it being populated
            logger.error("user clicked on empty list box")
            print(f"Index out of range, try again - {e}")
