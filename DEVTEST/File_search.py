import os
from File_decision import file_decision
class file_search:
    def __init__(self):
        self.decision = ""

    def search(self,path):
        fs = file_decision()
        extension = ("xls","xlsx","xlsm","xlst")
        
        for file in os.listdir(path):
            if file.endswith(extension):         
                fs.route = path
                fs.accepted_files=file
                fs.create_processed_folder()
                fs.accepted()
              
            else:
                if os.path.isfile(os.path.join(path, file)):
                    fs.route = path
                    fs.not_accepted_files = file
                    fs.create_not_processed_folder()
                    fs.not_accepted()

                else:
                    print("its a directory")

    

