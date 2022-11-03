from tkinter import *

class Converter:
    def __init__(self):
        self.window = Tk()
        self.window.title("°C to °F Temp Converter")
        self.window.minsize(width=300, height=180)
        self.window.config(padx=20, pady=20)

        self.number_C = Entry(width=5)
        self.number_C.focus()
        self.number_C.grid(column=1, row=0)

        C_label = Label(text="°C degrees", font=("Helvetica", 12))
        C_label.config(padx=10, pady=10)
        C_label.grid(column=2, row=0)

        is_equal_label = Label(text="is equal to", font=("Helvetica", 12))
        is_equal_label.config(padx=10, pady=5)
        is_equal_label.grid(column=0, row=1)

        self.number_F = Entry(width=5)
        self.number_F.insert(END, string="0") #Add some text to begin with
        self.number_F.grid(column=1, row=1)

        F_label = Label(text="°F degrees", font=("Helvetica", 12))
        F_label.config(padx=10, pady=10)
        F_label.grid(column=2, row=1)

        convert_button = Button(text="Convert", command=self.button_clicked)
        convert_button.config(padx=5, pady=10)
        convert_button.grid(column=1, row=3)

    def button_clicked(self):
        self.number_F.delete(0, END) # https://stackoverflow.com/questions/2260235/how-to-clear-the-entry-widget-after-a-button-is-pressed-in-tkinter
        C_to_F = (int(self.number_C.get()) * 9/5) + 32
        self.number_F.insert(END, string=str(C_to_F))


converter = Converter()

converter.window.mainloop()
