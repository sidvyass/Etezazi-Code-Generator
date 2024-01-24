import pandas as pd
import os
from main_specs import ht_certs_dict

def convert_xl_to_list(excel_filepath_folder: list):
    for root, dirs, files in os.walk(excel_filepath_folder):
        for file in files:
            if file.endswith(".xlsx"):
                full_path = os.path.join(root, file)

                basename = "".join(os.path.basename(full_path).split(".")[0])
                data = pd.read_excel(full_path)
                column = data.iloc[:, 1]
                list_to_dict = column.to_list()
                list_to_dict = [str(element) for element in list_to_dict]  # need to convert or else typecasting is a problem
                ht_certs_dict[basename] = list_to_dict

convert_xl_to_list(r"C:\Users\svyas.ETEZAZI\PycharmProjects\GUI_code_gen\code_gen\configs\HT_configs") 