from csv import excel
import sys
from File_search import file_search
from Excel_process import excel_process

class monitor:
    def __init__(self):
        self.path = ""
        
    def menu():
        print("************Excel Monitor**************")
        print()
        try:
            choice = input("""
                                a: Monitor a directory
                                b: Exit

                                Please enter your choice: """)

            if choice == "A" or choice =="a":
                monitor.send_path()
                excel = excel_process()
                excel.path = monitor.path
                excel.combine_sheets()
                monitor.menu()

            elif choice == "B" or choice =="b":
                sys.exit
            else:
                print("You must only select either a or b")
                print("Please try again")
                monitor.menu()
        except:
            monitor.menu()

    
    def send_path():
        path = file_search()
        print()
        text = input("Write your path here: ")
        path.search(text)
        monitor.path = text

#-------------------------------------------------------Main---------------------------------------------------------------------       
if __name__ == "__main__":
    monitor.menu()