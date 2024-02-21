



#5. This has radio buttons so right column can only have one item selected while left is checkboxes so any amount can be selected. 

import customtkinter as ctk

class MyRadioButtonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title 
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew") 

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w") 
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)   


class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values): 
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6) 
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew") 

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w") 
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("m's app")
                
        # Calculate window position to center the GUI in the middle of the users screen dynamically
        window_width = 400
        window_height = 220
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


        self.grid_columnconfigure((0,1), weight=1) 
        self.grid_rowconfigure(0, weight=1)


        #Left column Checkbox
        self.checkbox_frame_1 = MyCheckboxFrame(self, "Left Value", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
       
        #Right column Radio
        self.radiobutton_frame_2 = MyRadioButtonFrame(self, "Right Option", values=["option A", "option B", "option C"]) 
        self.radiobutton_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        #self.radiobutton_frame_2.configure(fg_color="transparent")

        self.button = ctk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="we", columnspan=2)

    def button_callback(self):
        print("Bot button pressed")
        print("Checkbox_1: ", self.checkbox_frame_1.get())
        print("Radiobutton_2: ", self.radiobutton_frame_2.get())


#Starts the app from the class
app = App()
app.mainloop()



"""
#1. HARDCODED CHECKBOXES



import customtkinter as ctk

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


        self.checkbox1 = ctk.CTkCheckBox(self, text="checkbox - 1", command=lambda: print("c1"))
        self.checkbox1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox2 = ctk.CTkCheckBox(self, text="checkbox - 2", command=lambda: print("c2"))
        self.checkbox2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        self.checkbox3 = ctk.CTkCheckBox(self, text="checkbox - 3", command=lambda: print("c3"))
        self.checkbox3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")

    def get(self):
        checked_checkboxes = []
        if self.checkbox1.get() == 1:
            checked_checkboxes.append(self.checkbox1.cget("text"))
        if self.checkbox2.get() == 1:
            checked_checkboxes.append(self.checkbox2.cget("text"))
        if self.checkbox3.get() == 1:
            checked_checkboxes.append(self.checkbox3.cget("text"))
        return checked_checkboxes   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("mike's app")
        self.geometry("400x200+1100+700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)



        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")


        self.button = ctk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

    def button_callback(self):
        print("top button pressed", self.checkbox_frame.get())


#Starts the app from the class
app = App()
app.mainloop()

"""














"""
#2. DYNAMIC CHECKBOXES 

import customtkinter as ctk

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)

        self.values = values
        self.checkboxes = []
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("mike's app")
        self.geometry("400x200+1100+700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)



        self.checkbox_frame = MyCheckboxFrame(self, values=["value 1", "value 2", "value 3", "final"])
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")


        self.button = ctk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

    def button_callback(self):
        print("top button pressed", self.checkbox_frame.get())


#Starts the app from the class
app = App()
app.mainloop()

"""


















"""
#3. DYNAMIC CHECKBOXES AND MULTIPLE INSTANCES OF FRAMES 


import customtkinter as ctk

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)

        self.values = values
        self.checkboxes = []
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("mike's app")
        self.geometry("400x200+1100+700")
        self.grid_columnconfigure((0,1), weight=1) #Change left parameter to (0,1) because two columns are used
        self.grid_rowconfigure(0, weight=1)


        #Left column
        self.checkbox_frame_1 = MyCheckboxFrame(self, values=["value 1", "value 2", "value 3"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
       
        #Right column
        self.checkbox_frame_2 = MyCheckboxFrame(self, values=["option A", "option B"])
        self.checkbox_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")


        self.button = ctk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="we", columnspan=2)

    def button_callback(self):
        print("Bot button pressed")
        print("Checkbox_1: ", self.checkbox_frame_1.get())
        print("Checkbox_2: ", self.checkbox_frame_2.get())


#Starts the app from the class
app = App()
app.mainloop()

"""


















"""
#4. TWO FRAMES WITH UNQIUE FRAME TITLES


import customtkinter as ctk

class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values): #added in new title param
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title #assigning new title param
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6) #New title
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew") #new TItle

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w") #Made the row +1 now becuase the frame label is in the first row
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("mike's app")
        self.geometry("400x220+1100+700")
        self.grid_columnconfigure((0,1), weight=1) 
        self.grid_rowconfigure(0, weight=1)


        #Left column
        self.checkbox_frame_1 = MyCheckboxFrame(self, "Left Value", values=["value 1", "value 2", "value 3"]) #Added new title sending
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
       
        #Right column
        self.checkbox_frame_2 = MyCheckboxFrame(self, "Right Option", values=["option A", "option B"]) #Added new title sending
        self.checkbox_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")
        self.checkbox_frame_2.configure(fg_color="transparent") #Makes the background blank

        self.button = ctk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="we", columnspan=2)

    def button_callback(self):
        print("Bot button pressed")
        print("Checkbox_1: ", self.checkbox_frame_1.get())
        print("Checkbox_2: ", self.checkbox_frame_2.get())


#Starts the app from the class
app = App()
app.mainloop()


"""