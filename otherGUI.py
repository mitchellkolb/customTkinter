



#Button disappearing app that makes the buttons disappear when clicked and come back when dummy is clicked
import customtkinter as ctk

def button_callback(num):
    print("Button is pressed: " + str(num))

def toggle_visibility(target_button):
    if target_button.winfo_viewable():
        target_button.grid_remove()
    else:
        target_button.grid()

def show_all_buttons():
    # This function will make sure all buttons are visible
    button1.grid()
    button2.grid()
    button3.grid()

app = ctk.CTk()
app.title("M's App")
app.geometry("350x200+1100+700")
app.grid_columnconfigure(0, weight=1) #This makes all the buttons in the center


# Button 1
button1 = ctk.CTkButton(app, text="Button1", command=lambda: [button_callback(1), toggle_visibility(button1)])
button1.grid(row=1, column=0, padx=5, pady=5)

# Button 2
button2 = ctk.CTkButton(app, text="Button2", command=lambda: [button_callback(2), toggle_visibility(button2)])
button2.grid(row=2, column=0, padx=5, pady=5)

# Button 3
button3 = ctk.CTkButton(app, text="Button3", command=lambda: [button_callback(3), toggle_visibility(button3)])
button3.grid(row=3, column=0, padx=5, pady=5)


# Adding a dummy widget to show grid effect
dummy_button = ctk.CTkButton(app, text="Dummy", command=lambda: [print("Dummy pressed"), show_all_buttons()])
dummy_button.grid(row=0, column=0, padx=5, pady=5)  # This will show the effect of grid spacing

app.mainloop()
