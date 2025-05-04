import tkinter as tk
from tkinter import messagebox
import shelve

class database:
    def __init__(self,username=""):
        self.username=username
        self.database_path="5/DB5/db"
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
                    profile_ui(username)
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

class profile_ui: 
    def __init__(self, username, initial_command="profile"):
        self.open_search_windows={}
        self.username=username

        self.portfolio_window=tk.Tk() 
        self.portfolio_window.title(username)

        toolbar_frame=tk.Frame(self.portfolio_window, bg="black")
        toolbar_frame.pack(expand=False, fill=tk.X)

        toolbar_button_profile=tk.Button(master=toolbar_frame, text="profile", command=self.profile_command)
        toolbar_button_profile.pack(expand=True, side=tk.LEFT)

        toolbar_button_search=tk.Button(master=toolbar_frame, text="search", command=self.search_command)
        toolbar_button_search.pack(expand=True, side=tk.LEFT)

        toolbar_button_settings=tk.Button(master=toolbar_frame, text="settings", command=self.settings_command)
        toolbar_button_settings.pack(expand=True, side=tk.LEFT)

        toolbar_button_signout=tk.Button(master=toolbar_frame, text="signout", command=self.signout_command)
        toolbar_button_signout.pack(expand=True, side=tk.LEFT)

        self.main_frame=tk.Frame(master=self.portfolio_window)
        
        map_initial_command={"profile":self.profile_command, "settings":self.settings_command, "search":self.search_command}
        map_initial_command[initial_command]()

        self.portfolio_window.mainloop()
    
    def profile_command(self,username=None):
        if(username==None):
            username=self.username
        self.set_portfolio_window_main_frame(self.display_profile(username,self.portfolio_window))

    def search_command(self):
        pass

    def settings_command(self):
        pass

    def signout_command(self):
        self.portfolio_window.destroy()
        signinup_ui()

    def set_portfolio_window_main_frame(self,new_frame):
        self.main_frame.destroy()
        self.main_frame=new_frame
        self.main_frame.pack(expand=True,fill=tk.BOTH)

    def display_profile(self, username, window):
        profile_frame=tk.Frame(master=window,bg="red")
        
        user_info=database(username).get_user()

        row_count=5
        profile_frame.rowconfigure(index=[i for i in range(row_count)], weight=1)
        profile_frame.columnconfigure(index=[0,1], weight=1)

        width1=10
        width2=20

        # image_pil = Image.open("example.png")
        # image = ImageTk.PhotoImage(image_pil)
        image=tk.PhotoImage(file="example.png", width=100, height=100)

        key="profile_image"
        row_index=0
        tk.Label(master=profile_frame, image=image).grid(row=row_index, columnspan=2)

        key="username"
        row_index+=1
        tk.Label(master=profile_frame, text=key, width=width1).grid(row=row_index, column=0, sticky="e", padx=5)
        tk.Label(master=profile_frame, text=username, width=width2).grid(row=row_index, column=1,sticky="w")

        key="birthday"
        row_index+=1
        tk.Label(master=profile_frame, text=key, width=width1).grid(row=row_index, column=0, sticky="e", padx=5)
        tk.Label(master=profile_frame, text=user_info[key], width=width2).grid(row=row_index, column=1,sticky="w")

        key="bio"
        row_index+=1
        tk.Label(master=profile_frame, text=key, width=width1).grid(row=row_index, column=0, sticky="e", padx=5)
        tk.Label(master=profile_frame, text=user_info[key], width=width2).grid(row=row_index, column=1, sticky="w")

        key="link"
        row_index+=1              
        tk.Label(master=profile_frame, text=key, width=width1).grid(row=row_index, column=0, sticky="e", padx=5)
        link_label=tk.Label(master=profile_frame, text=user_info[key], width=width2, cursor="hand2")
        link_label.grid(row=row_index, column=1, sticky="w")
        link_label.bind("<Button-1>", lambda event:self.open_link(event, user_info["link"]))

        return profile_frame

if __name__=="__main__":
    database().print_database()
    signinup_ui()