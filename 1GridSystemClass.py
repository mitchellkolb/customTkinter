

import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("m's app")

        # Calculate window position to center the GUI in the middle of the users screen dynamically
        window_width = 750
        window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.button = ctk.CTkButton(self, text="top button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="we", columnspan=4)

        self.checkbox1 = ctk.CTkCheckBox(self, text="checkbox1", command=lambda: print("c1"))
        self.checkbox1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        self.checkbox2 = ctk.CTkCheckBox(self, text="checkbox2", command=lambda: print("c2"))
        self.checkbox2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

        self.checkbox3 = ctk.CTkCheckBox(self, text="checkbox3", command=lambda: print("c3"))
        self.checkbox3.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="w")

        self.checkbox4 = ctk.CTkCheckBox(self, text="checkbox4", command=lambda: print("c4"))
        self.checkbox4.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="w")

        self.grid_columnconfigure((1,2), weight=1)

    def button_callback(self):
        print("top button pressed")


#Starts the app from the class
app = App()
app.mainloop()

