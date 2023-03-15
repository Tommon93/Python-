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
        self.selected_analyst = tk.StringVar()
        analyst_dropdown = ttk.Combobox(self, textvariable=self.selected_analyst)
        analyst_dropdown['values'] = ('Thomas', 'Sam', 'Michael')
        analyst_dropdown['state'] = 'readonly'
        analyst_dropdown.grid(column=0, row=1, sticky=tk.W)

        def get_analyst(self):
            a = self.selected_analyst.get()
            return a 
        
        analyst_dropdown.bind('<<ComboboxSelected>>', get_analyst)

        # Radio button for pre/post-commencement BOs
        # Label for bo status
        ttk.Label(self, text="Pre-commencement Status:").grid(column=0, row=2, sticky=tk.W)
    

        self.bo_status = tk.StringVar()
        bo_option1 = ttk.Radiobutton(self, text="Yes", value="Y", variable=self.bo_status).grid(column=0, row=3, sticky=tk.W)
        bo_option2 = ttk.Radiobutton(self, text="No", value="N", variable=self.bo_status).grid(column=0, row=3)

        # Temporary button to see if radio button get value works
        
        def selected_status():
            b = self.bo_status.get()
            return b 
        
        #button = ttk.Button(self, text="get selected status", command=selected_status)

        # Create Issue/Quality Score 
        ttk.Label(self, text="Select Quality Score").grid(column=0, row=4, sticky=tk.W)
        #Create drop down
        self.selected_score = tk.StringVar()
        score_dropdown = ttk.Combobox(self, textvariable=self.selected_score)
        score_dropdown['values'] = ("1","2","3")
        score_dropdown['state'] = 'readonly'
        score_dropdown.grid(column=0, row=5, sticky=tk.W)


        # Create entry field for email address
        ttk.Label(self, text="Enter email address:").grid(column=0, row=6, sticky=tk.W)
        
        self.email = tk.StringVar()
        email_entry = ttk.Entry(self, textvariable=self.email, width=30)
        email_entry.focus()
        email_entry.grid(column=0, row=7, sticky=tk.W, columnspan=2)

        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)


class OutputFrame(ttk.Frame):
    def __init__(self, container, email, bo_status, selected_score, selected_analyst):
        super().__init__(container)

        self.analyst_var = selected_analyst
        self.email_var = email 
        self.bo_var = bo_status
        self.score_var = selected_score

        self.columnconfigure(0, weight=1)
        self.__create_widgets()

    def __create_widgets(self):
        
        def get_text(): # Change to button function to generate text
            a = self.analyst_var.get()
            b = self.bo_var.get()
            s = self.score_var.get()
            e = self.email_var.get()

            if b == "Y":
                standard_text.insert('1.0', COMMENT_1)
            
    

        standard_text = tk.Text(self, height=20,  font=('Helvetica',10  ))
        standard_text.grid(column=0, row=0)

        generate_text = ttk.Button(self, text="Generate Text", command=get_text).grid(column=0, row=6, sticky=tk.W)

        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

        

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("NAB Text Application")
        #self.iconbitmap(os.path.dirname(os.path.abspath("__file__"))+"/nab_logo.ico")
        self.geometry("600x320")
        #self.resizable(0,0)

        # Root window layout
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=4)

        self.__create_widgets()
    
    def __create_widgets(self):
         # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=0, row=0)

        # Create the output frame after input_frame has been initialized
        output_frame = OutputFrame(self, input_frame.email, input_frame.bo_status, input_frame.selected_score, input_frame.selected_analyst)
        output_frame.grid(column=1, row=0)


    
if __name__=="__main__":
    app = App()
    app.mainloop()
    


