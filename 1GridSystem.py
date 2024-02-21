



import customtkinter as ctk

def button_callback():
    print("ok now")

app = ctk.CTk()
app.title("M's App")
app.geometry("750x200+1100+700")

    # Button 1
button1 = ctk.CTkButton(app, text="Button1", command=button_callback)
button1.grid(row=0, column=0, sticky="we", padx=10, pady=10, columnspan=4)

    # Checkboxes
checkbox1 = ctk.CTkCheckBox(app, text="Checkbox 1", command=lambda: print("Checkbox1 clicked"))
checkbox1.grid(row=1, column=0, padx=10, pady=(0,20), sticky="w")

checkbox2 = ctk.CTkCheckBox(app, text="Checkbox 2", command=lambda: print("checkbox2 clicked"))
checkbox2.grid(row=1, column=1, padx=10, pady=(0,20), sticky="w")

checkbox3 = ctk.CTkCheckBox(app, text="Checkbox 3", command=lambda: print("checkbox3 clicked"))
checkbox3.grid(row=1, column=2, padx=10, pady=(0,20), sticky="w")

checkbox3 = ctk.CTkCheckBox(app, text="Checkbox 4", command=lambda: print("checkbox4 clicked"))
checkbox3.grid(row=1, column=3, padx=10, pady=(0,20), sticky="w")

app.grid_columnconfigure((0,1), weight=1) #This makes the widgets in the center of left right
app.grid_columnconfigure((1,2), weight=1) #This makes the widgets in the center of left right

    # Button 1
#button2 = ctk.CTkButton(app, text="Button2", command=button_callback)
#button2.grid(row=1, column=1, sticky="ew", padx=0, pady=0)
#app.grid_columnconfigure(1, weight=1) #This makes the widgets in the center of left right
#app.grid_rowconfigure(1, weight=1) #This makes the widgets in the center of up down

app.mainloop()


