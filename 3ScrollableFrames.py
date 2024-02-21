
import os
import customtkinter as ctk



class scollable_checkbox_frame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value, in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scrollable Frame - M")

        window_width = 600
        window_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.my_scollable_checkbox_frame_1 = scollable_checkbox_frame(self, title="One", values=[f"Check {i}" for i in range(50)])
        self.my_scollable_checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="news")

        self.my_scollable_checkbox_frame_2 = scollable_checkbox_frame(self, title="Two", values=[f"Check {i}" for i in range(10)])
        self.my_scollable_checkbox_frame_2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="news")

        self.button = ctk.CTkButton(self, text = "This button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="we", columnspan=2)

    def button_callback(self):
        print("I can't believe this is real.")
        print("Checkbox_frame 1 : ", self.my_scollable_checkbox_frame_1.get())
        print("Checkbox_frame 2 : ", self.my_scollable_checkbox_frame_2.get())

        #print("Radiobutton_frame: ", self.radiobutton_frame.get())



window = Window()
window.mainloop()