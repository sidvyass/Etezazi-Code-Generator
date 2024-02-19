import tkinter as tk
from PIL import ImageTk, Image
from search_bar import SearchBar
from OPwindow import OPframe
from database_conn import MieTrak
import pulling_specs
from main_specs import certs_dict, ht_certs_dict  # change this so that it lives in configs
from tkinter import messagebox
import logging
from resource_paths import logo_path

logger = logging.getLogger(__name__)

class MainApp(tk.Tk):
    def __init__(self):
        logger.info("Starting the application")
        super().__init__()
        self.title("Code Gen")
        self.geometry("1000x800")
        self.configure(background='white')
        self.bind("<Escape>", lambda e: e.widget.quit())
        self.part_number = None
        
        self.db_handler = MieTrak()

        self.op_frame_status = False
        self.ht_frame_status = False

        for i in range(10):
            self.grid_columnconfigure(i, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=1)

        self.upper_frame_config()
        self.middle_frame_config()
        self.lower_frame_config()

    def search(self):
        self.search_bar = SearchBar(self, self.get_selection_from_search)  # get selection will get values back

    def get_selection_from_search(self, part_num):  # here we are assiging value to our class variable
        self.part_number = part_num   # this should give us a list
        self.itempk = self.part_number[0]
        string_to_update = f"Part Number - {self.part_number[1]}, Description - {self.part_number[2]}, Drawing Number - {self.part_number[3]}"
        self.text_bar.config(state="normal")
        self.text_bar.delete("1.0", tk.END)
        self.text_bar.insert("1.0", string_to_update)
        self.text_bar.config(state="disabled")

    def upper_frame_config(self):
        self.upper_frame = tk.Frame(self, height=10, bg="white")

        # main grid placement
        self.upper_frame.grid(row=0, column=0, sticky="NSEW", columnspan=10)
        
        self.upper_frame.columnconfigure(0, weight=1)
        self.upper_frame.columnconfigure(1, weight=6)
        self.upper_frame.columnconfigure(2, weight=3)

        image = Image.open(logo_path, mode='r')
        final_image = image.resize((70, 50))
        self.tk_image = ImageTk.PhotoImage(final_image)
        tk.Label(self.upper_frame, image=self.tk_image, background="white").grid(row=0, column=0, sticky="WE", padx=5)

        tk.Button(self.upper_frame, text="Search", command=self.search, height=1).grid(row=0, column=2, sticky="WE")  # need to pack this into the upper frame
        self.text_bar = tk.Text(self.upper_frame, height=1, state="disabled", font="Helvetica 15 bold")
        self.text_bar.grid(row=0, column=1, sticky="WE", padx=5)  # logo goes here

    def middle_frame_config(self):
        """Default middle frame"""
        self.middle_frame = tk.Frame(self, background="white")
        self.middle_frame.grid(row=1, column=0, sticky="NSEW", columnspan=10, padx=5, pady=5)

    def op(self):
        self.middle_frame.destroy()
        self.middle_frame = OPframe(self, self.get_code_from_op_ht, certs_dict, "op")
        self.middle_frame.grid(row=1, column=0, sticky="NSEW", columnspan=10, padx=5, pady=5)
        self.op_button.config(state="disabled", background="grey")
        self.ht_button.config(state="normal", background="white")
    
    def ht(self):
        self.middle_frame.destroy()
        self.middle_frame = OPframe(self, self.get_code_from_op_ht, ht_certs_dict, "ht")
        self.middle_frame.grid(row=1, column=0, sticky="NSEW", columnspan=10, padx=5, pady=5)
        self.ht_button.config(state="disabled", background="grey")
        self.op_button.config(state="normal", background="white")

    def get_code_from_op_ht(self, code):
        if self.part_number:
            self.code = code
            self.db_handler.push_finish_code_itemclass(self.code, self.itempk)
            logging.info(f"Pushed to database, ItemPK - {self.itempk}, Code generated - {self.code}")
            self.middle_frame_config()
            self.ht_button.config(state="normal", background="white")
            self.op_button.config(state="normal", background="white")
            return True
        else:
            messagebox.showerror(title="No part number", message="Search for a part number and then try submitting")

    def lower_frame_config(self):
        self.lower_frame = tk.Frame(self, background="white")
        # main grid placement
        self.lower_frame.grid(row=2, column=0, sticky="NSEW", columnspan=10, padx=5, pady=5)

        self.lower_frame.columnconfigure(0, weight=1)
        self.lower_frame.columnconfigure(5, weight=1)

        self.lower_frame.rowconfigure(0, weight=1)

        self.op_button = tk.Button(self.lower_frame, text="OP", command=self.op, background="white")
        self.op_button.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")
        self.ht_button = tk.Button(self.lower_frame, text="HT", command=self.ht, background="white")
        self.ht_button.grid(row=0, column=5, padx=5, pady=5, sticky="NSEW")
