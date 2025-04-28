# sign-in back-end
import tkinter as tk
from tkinter import messagebox
import shelve

window=tk.Tk()
window.title("az vaset")

# front-end
username_frame=tk.Frame(master=window)
username_frame.pack(expand=True,fill=tk.NONE)
username_label=tk.Label(master=username_frame,text="username",fg="white",bg="black")
username_label.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)
username_entry=tk.Entry(master=username_frame,width=20)
username_entry.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)

password_frame=tk.Frame(master=window)
password_frame.pack(expand=True, fill=tk.NONE)
password_label=tk.Label(master=password_frame, text="password", fg="white", bg="black")
password_label.pack(expand=True, side=tk.LEFT)
password_entry=tk.Entry(master=password_frame, width=20)
password_entry.pack(expand=True, side=tk.LEFT)

signinup_frame=tk.Frame(master=window)
signinup_frame.pack(expand=True, fill=tk.BOTH)
signin_button=tk.Button(master=signinup_frame, text="signin", command=lambda :signin_command())
signin_button.pack(expand=True, side=tk.TOP)
signup_button=tk.Button(master=signinup_frame, text="dont have an account?\nsignup")
signup_button.pack(expand=True, side=tk.TOP)

# back-end
DB_path="3/DB3/db"

def signin_command():
    username=username_entry.get()
    password=password_entry.get()    

    if does_username_exist(username):
        if signin_check_password(username, password)==True:
            profile(username)
        else:
            messagebox.showinfo("", "password is incorrect")
    else:
        messagebox.showinfo("", "user does not exist")

def signin_check_password(username, password):
    with shelve.open(DB_path) as db:
        user=db[username]
        if user["password"]==password:
            return True
        else:
            return False

def profile(username):
    messagebox.showinfo("", f"welcome {username}")

#database
def save_user(username, password):
    with shelve.open(DB_path) as db:
        db[username]={"password": password}

def does_username_exist(username):
    with shelve.open(DB_path) as db:
        if username in db:
            return True
        else:
            return False

# save_user("ali", "111")
# save_user("hasan", "222")
# save_user("reza", "333")
    
window.mainloop()