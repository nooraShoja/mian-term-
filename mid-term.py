import json
import tkinter as Tk
islogin=False


def login():
    global islogin
    user = input_user.get()
    password = input_pasw.get()

    if (islogin):
        output.configure(text="you are already logged in", fg="red")
        return
    else:

        with open("info.json") as f:
            users_dct = json.load(f)
        if user in users_dct and users_dct[user] == password:
            output.configure(text="welcome", fg="green")
            islogin = user
            logincount()
        else:
            output.configure(text="wrong username or password", fg="blue")


def logincount():
    global islogin
    with open("logincount.json") as f:
        logincount = json.load(f)
    if islogin in logincount:
        logincount[islogin] +=1
    else:
        logincount[islogin] =1
    with open("logincount.json", "w") as f:
        json.dump(logincount, f)


def submit():
    user = input_user.get()
    password = input_pasw.get()

    with open("info.json") as f:
        users_dct = json.load(f)
    if user in users_dct:
        output_submit.configure(text="username already exisZ", fg="red")
    elif len (password) < 5 or password.isalpha():
        output_submit.configure(text="please correct your password", fg="red")
    else:
        users_dct[user] = password
        with open("info.json", "w") as f:
            json.dump(users_dct, f)
        output_submit.configure(text="submit is done", fg="green")


def showlogincount():
    global islogin

    if islogin != "admin":
        output_count.configure(text="you are not allowed to enter", fg="red")
        return
    else:
        with open("logincount.json") as f:
            logincount = json.load(f)
        output_count.configure(text=logincount)


def logout():
    global islogin
    if not islogin:
        output_logout.configure(text="you are already logged out", fg="red")
    else:
        confirm = input("Are you want to delete your account? y/n")
        if confirm == "y":
            islogin = False
            output_logout.configure(text="logged out successfully", fg="green")
        else:
            output_logout.configure(text="logout canceled", fg="red")


def delete():
    global islogin

    if not (islogin):
        output_btn.configure(text="login first in order to delete your account", fg="red")
    else:
        with open("info.json") as f:
            users_dct = json.load(f)
        confirm = input("Are you want to delete your account? y/n")
        if confirm == "y":
            users_dct.pop(islogin)
            with open("info.json", "w") as f:
                json.dump(users_dct, f)
            output_Delete.configure(text="your account is deleted", fg="green")
        else:
            output_Delete.configure(text="delete was canceled", fg="red")


def userslist():
    global islogin
    if islogin != "admin":
        output_userslist.configure(text="you are not allowed to enter", fg="red")
        return
    else:
        with open("info.json") as f:
            userslist = json.load(f)
        user_lst = str(list(userslist.keys()))
        lst_box.insert("end", user_lst)




win=Tk.Tk()
win.title("win1")
win.geometry("400x660")





################################### submit
##

lbl_submit = Tk.Label(win, text="Submit")
lbl_submit.pack()

lbl_user = Tk.Label(win, text="new username:")
lbl_user.pack()

input_user = Tk.Entry(win, width=35)
input_user.pack()

lbl_pasw = Tk.Label(win, text="new password:")
lbl_pasw.pack()

input_pasw = Tk.Entry(win, width=35)
input_pasw.pack()

output_submit = Tk.Label(win, text=" ")
output_submit.pack()

Tk.Button(win, text="Submit", command=submit).pack()




#######################################login

lbl_login = Tk.Label(win, text="login")
lbl_login.pack()

lbl_user = Tk.Label(win, text="username:")
lbl_user.pack()

input_user = Tk.Entry(win, width=35)
input_user.pack()

lbl_pasw = Tk.Label(win, text="password:")
lbl_pasw.pack()

input_pasw = Tk.Entry(win, width=35)
input_pasw.pack()

output = Tk.Label(win, text="")
output.pack()

Tk.Button(win, text="login", command=login).pack()





###################################
output_logout = Tk.Label(win, text=" ")
output_logout.pack()

Tk.Button(win, text="logout", command=logout).pack()

###################################
output_Delete = Tk.Label(win, text=" ")
output_Delete.pack()

Tk.Button(win, text="Delete", command=delete).pack()
#####################################
output_count = Tk.Label(win, text=" ")
output_count.pack()

Tk.Button(win, text="login count", command=showlogincount).pack()

###################################

output_userslist = Tk.Label(win, text=" ")
output_userslist.pack()

Tk.Button(win, text="users list", command=userslist).pack()

lst_box = Tk.Listbox(win, height=10)
lst_box.pack()


win.mainloop()


























