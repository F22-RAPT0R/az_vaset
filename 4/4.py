import tkinter as tk
from tkinter import messagebox
import shelve

class database:
    def __init__(self,username=""):
        self.username=username
        # self.database_path="Z:/AZD/az_vaset/source_code/DB/db"
        self.database_path="4/DB4/db"
        self.fields=["image", "password", "birthday", "bio", "link"]

    def print_database(self):
        with shelve.open(self.database_path) as db:
            for username in db:
                print(username,db[username])
    
    def print_user(self):
        with shelve.open(self.database_path) as db:
                print(self.username,db[self.username])            

    def save_user(self,data):
        print("data: ",data)
        data=self.prettify_data(data)
        with shelve.open(self.database_path) as db:
            db[self.username]=data
    
    def update_user(self,data):
        info=self.get_user()
        with shelve.open(self.database_path) as db:
            for key in data:
                info[key]=data[key]

            self.save_user(info)          

    def does_username_exist(self):
        with shelve.open(self.database_path) as db:
            if self.username in db:
                return True
            else:
                return False

    def authenticate(self,password):
        with shelve.open(self.database_path) as db:
            if db[self.username]["password"]==password:
                return True
            else:
                return False

    def romove_user(self):
        with shelve.open(self.database_path) as db:
            db.pop(self.username)

    def get_user(self):
        with shelve.open(self.database_path) as db:
            return db[self.username]

    def prettify_data(self,data):
        prettified_data={}
        for field in self.fields:
            if field in data:
                prettified_data[field]=data[field]
            else:
                prettified_data[field]=""
        return prettified_data
    
    def search_user(self,username):
        result=[]
        with shelve.open(self.database_path) as db:
            for key in db:
                if username in key:
                    result.append(key)
        return result            

class signinup_ui:
    def __init__(self):
        self.signinup_window=tk.Tk()

        self.signinup_window.rowconfigure(index=[0,1,2,3], weight=1)
        self.signinup_window.columnconfigure(index=[0,1], weight=1)

        self.label_username=tk.Label(master=self.signinup_window, text="username")
        self.label_username.grid(row=0, column=0, sticky="E")

        self.label_password=tk.Label(master=self.signinup_window, text="password")
        self.label_password.grid(row=1, column=0, sticky="E")

        self.entry_username=tk.Entry(master=self.signinup_window)
        self.entry_username.grid(row=0,column=1, sticky="W")

        self.entry_password=tk.Entry(master=self.signinup_window)
        self.entry_password.grid(row=1,column=1, sticky="W")

        self.button_signin=tk.Button(master=self.signinup_window,text="signin", command=self.signin_command)
        self.button_signin.grid(row=2, column=0, columnspan=2)

        self.button_signup=tk.Button(master=self.signinup_window,text="dont have an account?\nsignup", command=self.signup_command)
        self.button_signup.grid(row=3, column=0, columnspan=2)

        self.signinup_window.mainloop()

    def signin_command(self):
        username=self.entry_username.get()
        password=self.entry_password.get()

        if username=="":   
            messagebox.showinfo("","USERNAME IS EMPTY")
        else: 
            if database(username).does_username_exist()==True:
                if self.signin_check_password(username, password)==True:
                    self.signinup_window.destroy()
                    # profile_ui(username)
                    messagebox.showinfo("", f"welcome {username}")
                else:
                    messagebox.showinfo("","WRONG PASSWORD")
            else:
                messagebox.showinfo("","USER DOES NOT EXIST")

    def signup_command(self):
        username=self.entry_username.get()
        password=self.entry_password.get()

        if self.signup_check_username(username, password)==True and self.signup_check_password(password)==True:
            data={
                "password":password,
                "bio":""
                }
            database(username).save_user(data)
            messagebox.showinfo("","SUCCESSFULLY SIGNED UP\nSIGN IN NOW")

    def signup_check_username(self, username, password):
        if username=="":
            messagebox.showinfo("","USERNAME IS EMPTY")
            return False
        elif database(username).does_username_exist()==True:
            messagebox.showinfo("","USERNAME IS ALREADY TAKEN")
            return False
        else:
            return True    

    def signup_check_password(self, password):
        if password=="":
            messagebox.showinfo("","PASSWORD IS EMPTY")
            return False
        else:
            return True
        
    def signin_check_password(self, username, password):
        return database(username).authenticate(password)

if __name__=="__main__":
    database().print_database()
    signinup_ui()