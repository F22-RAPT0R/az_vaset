import tkinter as tk


class signinup_ui():
    def __init__(self):
        self.signinup_window=tk.Tk()
        self.gui()
        self.signinup_window.mainloop()

    def gui(self):
        self.username_frame=tk.Frame(master=self.signinup_window)
        self.username_frame.pack(expand=True, side=tk.TOP, fill=tk.NONE, anchor=tk.CENTER)
        
        self.username_label=tk.Label(master=self.username_frame, text="username", bg="black", fg="white")
        self.username_entry=tk.Entry(master=self.username_frame)
        self.username_label.pack(expand=False, side=tk.LEFT, fill=tk.NONE, anchor=tk.CENTER)
        self.username_entry.pack(expand=False, side=tk.LEFT, fill=tk.NONE, anchor=tk.CENTER)

        self.password_frame=tk.Frame(master=self.signinup_window)
        self.password_frame.pack(expand=True, side=tk.TOP, fill=tk.NONE, anchor=tk.CENTER)

        self.password_label=tk.Label(master=self.password_frame, text="password", bg="black", fg="white")
        self.password_entry=tk.Entry(master=self.password_frame)
        self.password_label.pack(expand=False, side=tk.LEFT, fill=tk.NONE, anchor=tk.CENTER)
        self.password_entry.pack(expand=False, side=tk.LEFT, fill=tk.NONE, anchor=tk.CENTER)

if __name__=="__main__":
    signinup_ui()