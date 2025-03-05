# PACK GEOMETRY MANAGER
# simple but confusing
# requires trial and error

import tkinter as tk

window=tk.Tk()
window2=tk.Tk()
window.title("az vaset")

# label widget
# username_label=tk.Label(master=window, text="username")
# username_label.pack(side=tk.TOP)

# label color
# username_label=tk.Label(master=window, text="username", bg="green", fg="white")
# username_label.pack(side=tk.TOP)

# .pack(side=...)
# label1=tk.Label(master=window, text="TOP", bg="red")
# label1.pack(side=tk.TOP)
# label2=tk.Label(master=window, text="BOTTOM", bg="green")
# label2.pack(side=tk.BOTTOM)
# label3=tk.Label(master=window, text="LEFT", bg="blue")
# label3.pack(side=tk.LEFT)
# label4=tk.Label(master=window, text="RIGHT", bg="purple")
# label4.pack(side=tk.RIGHT)

# frame
# frame=tk.Frame(master=window, bg="red", width=100, height=100)
# frame.pack(side=tk.TOP)

# 2 frames TOP
# frame1=tk.Frame(master=window, bg="red", width=100, height=100)
# frame2=tk.Frame(master=window, bg="green", width=100, height=100)
# frame1.pack(side=tk.TOP)
# frame2.pack(side=tk.TOP)

# 2 frames LEFT
# frame1=tk.Frame(master=window, bg="red", width=100, height=100)
# frame2=tk.Frame(master=window, bg="green", width=100, height=100)
# frame1.pack(side=tk.LEFT)
# frame2.pack(side=tk.LEFT)

# .pack(expand=...) [ RESPONSIVE ]
# frame1=tk.Frame(master=window, bg="red", width=100, height=100)
# frame2=tk.Frame(master=window, bg="green", width=100, height=100)
# frame1.pack(expand=True, side=tk.TOP)
# frame2.pack(expand=True, side=tk.TOP)

# .pack(expand=...) [ RESPONSIVE ] [ WITH FILL ]
# frame1=tk.Frame(master=window, bg="red", width=100, height=100)
# frame2=tk.Frame(master=window, bg="green", width=100, height=100)
# frame1.pack(expand=True, side=tk.TOP, fill=tk.BOTH)
# frame2.pack(expand=True, side=tk.TOP, fill=tk.BOTH)

## signin/signup form
# over and under
# username_label=tk.Label(master=window, text="username", bg="black", fg="white")
# username_entry=tk.Entry(master=window)
# username_label.pack(side=tk.TOP)
# username_entry.pack(side=tk.TOP)

# side by side [ NON-RESPONSIVE ]
# username_label=tk.Label(master=window, text="username", bg="black", fg="white")
# username_entry=tk.Entry(master=window)
# username_label.pack(side=tk.LEFT)
# username_entry.pack(side=tk.LEFT)

# side by side [ NON-RESPONSIVE ] [ WITH PADDING ]
# username_label=tk.Label(master=window, text="username", bg="black", fg="white")
# username_entry=tk.Entry(master=window)
# username_label.pack(side=tk.LEFT, padx=5)
# username_entry.pack(side=tk.LEFT, padx=5)

# side by side [ HALF-RESPONSIVE ]
# username_label=tk.Label(master=window, text="username", bg="black", fg="white")
# username_entry=tk.Entry(master=window)
# username_label.pack(expand=True, side=tk.LEFT, padx=5)
# username_entry.pack(expand=True, side=tk.LEFT, padx=5)

# side by side [ FULL-RESPONSIVE ] 
# .pack(anchor=...)
# username_label=tk.Label(master=window, text="username", bg="black", fg="white")
# username_entry=tk.Entry(master=window)
# username_label.pack(expand=True, side=tk.LEFT, anchor="e", padx=5)
# username_entry.pack(expand=True, side=tk.LEFT, anchor="w", padx=5)

# username and password [ side by side ]
# username_label=tk.Label(master=window, text="username", bg="black", fg="white")
# username_entry=tk.Entry(master=window)
# username_label.pack(expand=True, side=tk.LEFT, anchor="e", padx=5)
# username_entry.pack(expand=True, side=tk.LEFT, anchor="w", padx=5)
# password_label=tk.Label(master=window, text="password", bg="black", fg="white")
# password_entry=tk.Entry(master=window)
# password_label.pack(expand=True, side=tk.LEFT, anchor="e", padx=5)
# password_entry.pack(expand=True, side=tk.LEFT, anchor="w", padx=5)

# username and password [ over and under ]
# username_frame=tk.Frame(master=window)
# username_frame.pack(expand=True, side=tk.TOP)
# password_frame=tk.Frame(master=window)
# password_frame.pack(expand=True, side=tk.TOP)
# username_label=tk.Label(master=username_frame, text="username", bg="black", fg="white")
# username_entry=tk.Entry(master=username_frame)
# username_label.pack(expand=True, side=tk.LEFT, anchor="e", padx=5)
# username_entry.pack(expand=True, side=tk.LEFT, anchor="w", padx=5)
# password_label=tk.Label(master=password_frame, text="password", bg="black", fg="white")
# password_entry=tk.Entry(master=password_frame)
# password_label.pack(expand=True, side=tk.LEFT, anchor="e", padx=5)
# password_entry.pack(expand=True, side=tk.LEFT, anchor="w", padx=5)

# button
# button=tk.Button(master=window, text="signin")
# button.pack(side=tk.TOP)

# 2 buttons [ NON-RESPONSIVE ]
# button_signin=tk.Button(master=window, text="signin")
# button_signin.pack(side=tk.TOP)
# button_signup=tk.Button(master=window, text="dont have an account?\nsignup")
# button_signup.pack(side=tk.TOP)

# 2 buttons [ RESPONSIVE ]
# button_signin=tk.Button(master=window, text="signin")
# button_signin.pack(side=tk.TOP, expand=True)
# button_signup=tk.Button(master=window, text="dont have an account?\nsignup")
# button_signup.pack(side=tk.TOP, expand=True)

# 2 buttons [ INSIDE FRAME ]
# buttons_frame=tk.Frame(master=window)
# buttons_frame.pack(expand=True, fill=tk.BOTH)
# button_signin=tk.Button(master=buttons_frame, text="signin")
# button_signin.pack(side=tk.TOP, expand=True)
# button_signup=tk.Button(master=buttons_frame, text="dont have an account?\nsignup")
# button_signup.pack(side=tk.TOP, expand=True)

#final form
username_frame=tk.Frame(master=window)
username_frame.pack(expand=True, side=tk.TOP, fill=tk.BOTH)
password_frame=tk.Frame(master=window)
password_frame.pack(expand=True, side=tk.TOP, fill=tk.BOTH)
username_label=tk.Label(master=username_frame, text="username", bg="black", fg="white")
username_entry=tk.Entry(master=username_frame)
username_label.pack(expand=True, side=tk.LEFT, anchor="e", padx=5)
username_entry.pack(expand=True, side=tk.LEFT, anchor="w", padx=5)
password_label=tk.Label(master=password_frame, text="password", bg="black", fg="white")
password_entry=tk.Entry(master=password_frame)
password_label.pack(expand=True, side=tk.LEFT, anchor="e", padx=5)
password_entry.pack(expand=True, side=tk.LEFT, anchor="w", padx=5)
buttons_frame=tk.Frame(master=window)
buttons_frame.pack(expand=True, fill=tk.BOTH)
button_signin=tk.Button(master=buttons_frame, text="signin")
button_signin.pack(side=tk.TOP, expand=True)
button_signup=tk.Button(master=buttons_frame, text="dont have an account?\nsignup")
button_signup.pack(side=tk.TOP, expand=True)

window.mainloop()

window2.mainloop()