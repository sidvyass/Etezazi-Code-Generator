import tkinter as tk
from tkinter import Frame
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

class OPframe(Frame):
    def __init__(self, parent, callback, cert_dict, op_or_ht):
        super().__init__(parent)
        self.callback = callback
        self.op_or_ht = op_or_ht
        self.cert_dict = cert_dict
        self.config(background="white")
        self.combo_box_list = []
        self.custom_font = tkFont.Font(family="Helvetica", size=11, weight="bold")        

        if self.op_or_ht == "ht":
            self.base_string_list = ["00" for i in range(5)]
            submit_button = tk.Button(self, text="Submit Code", command=self.submit)
            submit_button.grid(row=3, column=5, rowspan=1, padx=5, pady=5, sticky="NSEW")
        else:
            self.base_string_list = ["00" for i in range(11)]
            submit_button = tk.Button(self, text="Submit Code", command=self.submit)
            submit_button.grid(row=5, column=5, rowspan=2, padx=5, pady=5, sticky="NSEW")
            
        # func calls
        self.create_combox_widgets(self.cert_dict)
        self.code_display()

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(5, weight=1)

        for i in range(11):
            self.rowconfigure(i, weight=1)

    def create_combox_widgets(self, cert_dict):
        """Creates a Label and calls the make selection box. Label has the same name as the List that Combobox pulls data from"""
        for idx, key in enumerate(cert_dict.keys()):
            label1 = tk.Label(self, text=f"Select {key.upper()}", background="white", font=self.custom_font)
            label1.grid(row=idx+1, column=1, columnspan=2, sticky="EW")
            self.combo_box_list.append(self.make_selection_box(cert_dict[key], idx+1, 3, idx))

    def make_selection_box(self, item_list, row, column, idx_change): # currently builds the box and places it on the grid 
        """item list -> list from specs list to pull data from for selection widget
            idx change -> which idx gets updated in the base string list shown at the very top of the screen"""
        combo_box = ttk.Combobox(self, values=item_list, width=30, state="readonly", font=self.custom_font)
        combo_box.grid(row=row, column=column, columnspan=2, padx=5, pady=5, sticky="EW",)
        combo_box.bind("<<ComboboxSelected>>", lambda event : self.event_handler(event, item_list, idx_change))
        return combo_box

    def event_handler(self, event, item_list, pair_idx_to_change):
        """Updates the main string value as the user makes selection"""
        value = event.widget.get()
        idx = str(item_list.index(value))
        idx_replace = "0" + idx if len(idx) == 1 else idx
        self.base_string_list[pair_idx_to_change] = idx_replace
        self.set_code_display("".join(self.base_string_list)) 

    def code_display(self):
        # add weight to configure this
        self.code_display_widget = tk.Text(self, font="Helvetica 15 bold", height=1)
        self.code_display_widget.insert("1.0", "".join(self.base_string_list))
        self.code_display_widget.grid(row=0, column=2, columnspan=2, pady=5, sticky="W")

        self.code_display_widget.config(width=22) if self.op_or_ht == "op" else self.code_display_widget.config(width=10) 

    def set_code_display(self, updated_string):
        self.code_display_widget.config(state="normal")
        self.code_display_widget.delete("1.0", tk.END)
        self.code_display_widget.insert("1.0", updated_string)
        self.code_display_widget.config(state="disabled")

    def submit(self):  # used in the button to click submit
        final_code = "".join(self.base_string_list)
        if self.check_code(final_code):
            self.callback(final_code)
            for widgets in self.winfo_children():
                widgets.destroy()

    def check_code(self, code):
        if code[1] == "0":
            messagebox.showerror(title="Invalid code", message="Supplier/OEM cannot be 0")
            return False
        else:
            return True
        # we will add more checks here as the version improves