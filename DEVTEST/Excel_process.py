import glob
import os
import pandas as pd

class excel_process:
    def __init__(self):
        self.path = ""
    
    
    def combine_sheets(self):
        afp = self.path+"\\processed\\" #acceptable file path
        file_list = glob.glob(afp + "*.xls")+glob.glob(afp + "*.xlsx")+glob.glob(afp + "*.xlsm")+glob.glob(afp + "*.xlst")
        df_total = pd.DataFrame()
        for file in file_list:
            excel_file = pd.ExcelFile(f'{file}')
            sheets = excel_file.sheet_names
            for sheet in sheets:
                df = excel_file.parse(sheet_name=sheet)
                df_total = df_total.append(df)

        df_total.to_excel(afp+'total_sales.xlsx')