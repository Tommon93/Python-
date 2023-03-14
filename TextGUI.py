import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
import os
import re
#import win32com.client as win32

## Need to create Python GUI for work ##
# Will need to use Tkinter 
# Have the input and dropdown options on the left side of the UI
# Right side of UI to have output, i.e textbox output

# If possible create GUI using OOP paradigm

#Global Comment Variables
COMMENT_1 = "text 1"
COMMENT_2 = "text 2"
COMMENT_3 = "text 3"
COMMENT_4 = "text 4"
COMMENT_5 = "text 5"

class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        
        #Set up grid layout manager for inputs (drops downs and options for analysts)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        """ Create input widgets """
        # Label to decide analyst
        ttk.Label(self, text="Please choose an analyst:").grid(column=0, row=0, sticky=tk.W)
        # Drop down for analysts 
        selected_analyst = tk.StringVar()
        analyst_dropdown = ttk.Combobox(self, textvariable=selected_analyst)
        analyst_dropdown['values'] = ('Thomas', 'Sam', 'Michael')
        analyst_dropdown['state'] = 'readonly'
        analyst_dropdown.grid(column=0, row=1, sticky=tk.W)

        def get_analyst(self):
            a = selected_analyst.get()
            print(a)
        
        analyst_dropdown.bind('<<ComboboxSelected>>', get_analyst)

        # Radio button for pre/post-commencement BOs
        # Label for bo status
        ttk.Label(self, text="Pre-commencement Status:").grid(column=0, row=2, sticky=tk.W)
    

        bo_status = tk.StringVar()
        bo_option1 = ttk.Radiobutton(self, text="Yes", value="Y", variable=bo_status).grid(column=0, row=3, sticky=tk.W)
        bo_option2 = ttk.Radiobutton(self, text="No", value="N", variable=bo_status).grid(column=0, row=3)

        # Temporary button to see if radio button get value works
        @staticmethod
        def selected_status():
            b = bo_status.get()
            return b 
        
        #button = ttk.Button(self, text="get selected status", command=selected_status)

        # Create Issue/Quality Score 
        ttk.Label(self, text="Select Quality Score").grid(column=0, row=4, sticky=tk.W)
        #Create drop down
        selected_score = tk.StringVar()
        score_dropdown = ttk.Combobox(self, textvariable=selected_score)
        score_dropdown['values'] = (1,2,3)
        score_dropdown['state'] = 'readonly'
        score_dropdown.grid(column=0, row=5, sticky=tk.W)


        # Create entry field for email address
        ttk.Label(self, text="Enter email address:").grid(column=0, row=6, sticky=tk.W)
        
        self.email = tk.StringVar()
        email_entry = ttk.Entry(self, textvariable=self.email, width=30)
        email_entry.focus()
        email_entry.grid(column=0, row=7, sticky=tk.W)

        

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)


class OutputFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
    # Create quality score function and binding here
    # let a variable = class inputframe() to use email/quality score attributes. 
        pass
    
    


class App(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title("NAB Text Application")
        #self.iconbitmap(os.path.dirname(os.path.abspath("__file__"))+"/nab_logo.ico")
        self.geometry("500x300")
        self.resizable(0,0)

        # Root window layout
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()
    
    def __create_widgets(self):
        # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)

        # Create the output frame
        output_frame = OutputFrame(self)
        output_frame.grid(column=1, row=0)

    
if __name__=="__main__":
    app = App()
    app.mainloop()
    


