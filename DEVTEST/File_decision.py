import os
class file_decision:
    def __init__(self):
        self.route = ""
        self.accepted_files = ""
        self.not_accepted_files = ""
    
    def create_processed_folder(self):
        os.makedirs(self.route+"\\processed",exist_ok=True)

    def create_not_processed_folder(self):
        os.makedirs(self.route+"\\not_applicable",exist_ok=True)
        
    def accepted(self):
        source = self.route + "\\" + self.accepted_files
        destiny = self.route + "\\processed\\"+ self.accepted_files
        self.move(source,destiny)

    def not_accepted(self):
        source = self.route + "\\" + self.not_accepted_files
        destiny = self.route + "\\not_applicable\\"+ self.not_accepted_files
        self.move(source,destiny)
    
    def move(self,source,destiny):
        try:
            os.rename(source,destiny)
        except:
            print("This file is no longer on this path")
        
