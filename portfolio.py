#frontend and backend
import tkinter as tk
from tkinter import filedialog,messagebox
import shelve
# from PIL import Image, ImageTk
import webbrowser

class database:
    def __init__(self,username=""):
        self.username=username
        # self.database_path="Z:/AZD/az_vaset/source_code/DB/db"
        self.database_path="DB/db"
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
                if self.signin_check_password()==True:
                    self.signinup_window.destroy()
                    profile_ui(username)
                else:
                    messagebox.showinfo("","WRONG PASSWORD")
            else:
                messagebox.showinfo("","USER DOES NOT EXIST")

    def signup_command(self):
        username=self.entry_username.get()
        password=self.entry_password.get()

        if self.signup_check_username()==True and self.signup_check_password()==True:
            data={
                "password":password,
                "bio":""
            }
            database(username).save_user(data)
            messagebox.showinfo("","SUCCESSFULLY SIGNED UP\nSIGN IN NOW")

    def signup_check_username(self):
        username=self.entry_username.get()

        if username=="":
            messagebox.showinfo("","USERNAME IS EMPTY")
            return False
        elif database(username).does_username_exist()==True:
            messagebox.showinfo("","USERNAME IS ALREADY TAKEN")
            return False
        else:
            return True    

    def signup_check_password(self):
        password=self.entry_password.get()

        if password=="":
            messagebox.showinfo("","PASSWORD IS EMPTY")
            return False
        else:
            return True
        
    def signin_check_password(self):
        username=self.entry_username.get()
        password=self.entry_password.get()

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

    def settings_command(self):
        settings_frame=tk.Frame(master=self.portfolio_window,bg="green")
        
        user_info=database(self.username).get_user()

        settings_frame.rowconfigure(index=[0,1,2,3,4,5], weight=1)
        settings_frame.columnconfigure(index=[0,1], weight=1)

        row_index=0
        upload_button=tk.Button(master=settings_frame, text="upload image", command=self.upload_command)
        upload_button.grid(row=0, columnspan=2)

        labels={}
        entries={}

        key="password"
        row_index+=1
        labels[key]=tk.Label(master=settings_frame, text=key, width=8)
        labels[key].grid(row=row_index, column=0, sticky="E")
        entries[key]=tk.Entry(master=settings_frame)
        entries[key].grid(row=row_index, column=1, sticky="W")
        entries[key].insert(0,user_info[key])

        key="birthday"
        row_index+=1
        labels[key]=tk.Label(master=settings_frame, text=key, width=8)
        labels[key].grid(row=row_index, column=0, sticky="E")
        entries[key]=tk.Entry(master=settings_frame)
        entries[key].grid(row=row_index, column=1, sticky="W")
        entries[key].insert(0,user_info[key])            

        key="bio"
        row_index+=1
        labels[key]=tk.Label(master=settings_frame, text=key, width=8)
        labels[key].grid(row=row_index, column=0, sticky="E")
        entries[key]=tk.Entry(master=settings_frame)
        entries[key].grid(row=row_index, column=1, sticky="W")
        entries[key].insert(0,user_info[key]) 

        key="link"
        row_index+=1
        labels[key]=tk.Label(master=settings_frame, text=key, width=8)
        labels[key].grid(row=row_index, column=0, sticky="E")
        entries[key]=tk.Entry(master=settings_frame)
        entries[key].grid(row=row_index, column=1, sticky="W")
        entries[key].insert(0,user_info[key]) 

        row_index+=1
        saveabort_frame=tk.Frame(master=settings_frame, bg="yellow")
        saveabort_frame.grid(row=row_index, columnspan=2, sticky="S")
        save_button=tk.Button(master=saveabort_frame,text="save", command=lambda :self.save_settings_command(entries["password"].get(), entries["birthday"].get(), entries["bio"].get(), entries["link"].get()))
        save_button.pack(side=tk.LEFT)
        abort_button=tk.Button(master=saveabort_frame,text="abort", command=self.abbort_settings_command)
        abort_button.pack(side=tk.LEFT)

        self.set_portfolio_window_main_frame(settings_frame)

    def search_command(self):
        search_frame=tk.Frame(master=self.portfolio_window, bg="blue")
        search_frame.rowconfigure([0], weight=1)
        search_frame.rowconfigure([1], weight=5)
        search_frame.columnconfigure([0], weight=1)
       
        self.strvar=tk.StringVar()
        self.strvar.trace_add("write", lambda name,index,operation:self.display_search(search_entry.get(), listbox))
        search_entry=tk.Entry(master=search_frame, textvariable=self.strvar)
        search_entry.grid(row=0, column=0)

        list_frame=tk.Frame(master=search_frame)
        list_frame.grid(row=1, column=0)
        listbox=tk.Listbox(master=list_frame)
        listbox.pack(side=tk.LEFT)
        scrollbar=tk.Scrollbar(master=list_frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)
        listbox.bind("<<ListboxSelect>>", lambda event:self.listbox_item_selected(listbox))
        
        self.set_portfolio_window_main_frame(search_frame)

    def signout_command(self):
        self.portfolio_window.destroy()
        signinup_ui()

    def set_portfolio_window_main_frame(self,new_frame):
        self.main_frame.destroy()
        self.main_frame=new_frame
        self.main_frame.pack(expand=True,fill=tk.BOTH)

    def save_settings_command(self, password, birthday, bio, link):
        print("dob:",birthday)
        data={"password":password, "birthday":birthday, "bio":bio, "link":link}
        database(self.username).save_user(data)
        print("MESSAGE:\n\tuser successfully updated")    
        return self.profile_command()
    
    def abbort_settings_command(self):
        return self.profile_command()

    def upload_command(self):
        filename=filedialog.askopenfilename(initialdir="/", title="select an image", filetypes=[("image","*.png;*.jpeg;*.jpg;*.gif")])
        print("filename: "+filename)
        if filename!="":
            pass

    def open_link(self, event, link):
        if link!="":
            webbrowser.open(link)

    def display_search(self, input, listbox):
        listbox.delete(0,tk.END)
        for username in database().search_user(input):
            listbox.insert(tk.END,username)
        
        listbox.bind("<<ListboxSelect>>", lambda event:self.listbox_item_selected(listbox))

    def listbox_item_selected(self, listbox):
        selected_indices=listbox.curselection()
        if len(selected_indices)!=0:
            for selected_index in selected_indices:
                self.visit_profile(listbox.get(selected_index))

    def visit_profile(self, username):
        if username in self.open_search_windows:
            pass
        else:
            search_window=tk.Toplevel(master=self.portfolio_window)
            search_window.title(username)
            self.search_window_opened(username, search_window)
            search_window.protocol("WM_DELETE_WINDOW", lambda :self.search_window_closed(username,search_window))
            self.display_profile(username,search_window).pack(expand=True, fill=tk.BOTH)

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

    def search_window_opened(self, username, search_window):
        self.open_search_windows[username]=search_window

    def search_window_closed(self, username, search_window):
        self.open_search_windows.pop(username)
        search_window.destroy()

    # def close_search_windows(self):
    #     for search_window in self.open_search_windows:
    #         search_window.destroy()

#driver code
if __name__ == "__main__":
    # database("reza34").romove_user()
    # database("rezaya").save_user({"bio": "ajdkfl;"})
    # database("reza").update_user({"bio":"to be or not to be"})
    # database("reza").update_user({"link":"www.example.com"})
    database().print_database()
    signinup_ui()
    # profile_ui("reza",initial_command="settings")
    # profile_ui("reza", initial_command="search")
    # profile_ui("reza", initial_command="search")
