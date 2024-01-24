import pyodbc
from tkinter import messagebox

class MieTrak:
    def __init__(self):
        _conn_string = "DRIVER={SQL Server};SERVER=ETZ-SQL;DATABASE=SANDBOX;Trusted_Connection=yes;"
        self.conn = pyodbc.connect(_conn_string)
        self.cursor = self.conn.cursor()
    
    def pull_part_numbers(self, part_number: str) -> list:
        """Uses the LIKE keyword in SQL to pull data from MieTrak. Only looks at Item table, returns all results"""
        query = "SELECT ItemPK, PartNumber, Description, DrawingNumber, PartyFK FROM item WHERE PartNumber LIKE (?)"
        self.cursor.execute(query, f"%{part_number}%")
        return self.cursor.fetchall()
    
    def pull_data(self, table_name: str, column_name="*") -> list:
        query = f"SELECT {column_name} FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    @staticmethod
    def prettyify(list_to_print):
        return_list = []
        for item in list_to_print:
            string_to_append = f"Part Number - {item[1]}, Drawing Number - {item[2]}, Description - {item[3]}"
            return_list.append(string_to_append)
        return return_list
    
    def push_finish_code_itemclass(self, code, itempk):
        query = "SELECT itemclassPK FROM itemclass WHERE name=(?)"
        self.cursor.execute(query, code)
        results = self.cursor.fetchall()
        if len(results) > 0:
            self.itemclassfk = results[0][0]  # enter it into the database
        else:
            insert_code = "INSERT INTO itemclass (name) VALUES (?)"
            self.cursor.execute(insert_code, code)
            self.conn.commit()
            get_code = "SELECT itemclassPK FROM itemclass WHERE name=(?)"  # pass code
            self.cursor.execute(get_code, code)  # this could give errors
            self.itemclassfk = self.cursor.fetchall()[0][0]
        
        # updating item 
        description = "OP HT" if len(code) < 22 else "OP"
        query_to_update_item = "UPDATE item SET itemclassFK=(?), description=(?) WHERE itemPK=(?);"
        self.cursor.execute(query_to_update_item, (self.itemclassfk, description, itempk))
        self.conn.commit()
        messagebox.showinfo(title="Success!", message="Import Successfull!")


# testing - do not change or touch
if __name__=="__main__":
    m = MieTrak()
    m.push_finish_code_itemclass('0601010100000200000999', 707)
