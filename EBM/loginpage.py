from tkinter import ttk
from tkinter import messagebox
from homepagemaster import HomePageMaster
import mysql.connector
from homepage import *

global user_entry
global password_entry
global login
global sign_page
global admin
global name
global passwd
global user_entry2
global password_entry2
global user_name
global password


def tab_fun():
    global user_entry
    global password_entry
    global login
    global user_entry2
    global password_entry2

    login = Tk()
    login.geometry("540x360")
    login.title("LOGIN")
    login.iconphoto(True, PhotoImage(file="C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\title1.png"))

    login_image = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\login.png")
    login_image = login_image.resize((200, 200), Image.ANTIALIAS)
    login_image = ImageTk.PhotoImage(login_image)



    my_ntbk = ttk.Notebook(login)
    my_ntbk.pack(pady=15)

    my_frame1 = Frame(my_ntbk, width=500, height=500)
    my_frame2 = Frame(my_ntbk, width=500, height=500)

    my_frame1.pack(fil="both", expand=1)
    my_frame2.pack(fil="both", expand=1)

    my_ntbk.add(my_frame1, text="Master Login")
    my_ntbk.add(my_frame2, text="Login")


    # login Image

    icon_label = Label(my_frame1, image=login_image)
    icon_label.place(x=40, y=100)

    # login Image
    icon_label = Label(my_frame2, image=login_image)
    icon_label.place(x=40, y=100)


    # Username
    username = Label(my_frame1, text="Username", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    username.place(x=250, y=100)

    user_entry = Entry(my_frame1, width=20, font=("Helvetica", 8))
    user_entry.place(x=350, y=107)


    # Password
    password = Label(my_frame1, text="Password", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    password.place(x=250, y=170)

    password_entry = Entry(my_frame1, width=20, font=("Helvetica", 8))
    password_entry.place(x=350, y=177)


    login_button = Button(my_frame1, text="LOGIN", font=("Helvetica", 10, "bold"), padx=10, pady=5,
                          fg="white", bg="black", command=submit)
    login_button.place(x=300, y=230)

    signup_button = Button(my_frame1, text="ADD ADMIN", font=("Helvetica", 10, "bold"), padx=10, pady=5,
                           fg="white", bg="black", command=add_button)
    signup_button.place(x=380, y=230)


    # Login TAB

    username2 = Label(my_frame2, text="Username", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    username2.place(x=250, y=100)

    user_entry2 = Entry(my_frame2, width=20, font=("Helvetica", 8))
    user_entry2.place(x=350, y=107)

    # Password
    password2 = Label(my_frame2, text="Password", font=("Helvetica", 12, "bold"), padx=10, pady=5)
    password2.place(x=250, y=170)

    password_entry2 = Entry(my_frame2, width=20, font=("Helvetica", 8))
    password_entry2.place(x=350, y=177)

    login_button2 = Button(my_frame2, text="LOGIN", font=("Helvetica", 10, "bold"), padx=10, pady=5,
                           fg="white", bg="black", command=submit_logintab)
    login_button2.place(x=350, y=230)



    login.mainloop()



def clear_page():
    global admin
    global name
    global passwd

    admin.delete(0, END)
    name.delete(0, END)
    passwd.delete(0, END)


def add_admin():
    global admin
    global name
    global passwd

    try:

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Iamankit@02",
            database="ebm"
        )


        cursor = db.cursor()



        cursor.execute("CREATE TABLE IF NOT EXISTS ADMIN(Admin VARCHAR(50), Name VARCHAR(50), Password VARCHAR(20),"
                       "AdminNo INT AUTO_INCREMENT PRIMARY KEY)")



        sql_command = "INSERT INTO ADMIN(Admin, Name, Password) VALUES(%s,%s,%s)"
        values = (admin.get(), name.get(),
                  passwd.get())
        cursor.execute(sql_command, values)

        db.commit()
        clear_page()
        messagebox.showinfo("Successful", "Submitted")

    except:

        messagebox.showerror("Error", "Invalid Entry")


def backtologin():

    global sign_page
    sign_page.destroy()
    tab_fun()


def add_button():

    global user_entry
    global password_entry
    global user_name
    global password
    global login

    if user_entry.get() == "":
        messagebox.showerror("ERROR", "Invalid Entry")

    elif password_entry.get() == "":
        messagebox.showerror("ERROR", "Invalid Entry")

    else:


        try:

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Iamankit@02",
                database="ebm"
            )

            mycursor = db.cursor()

            # submit_values = (user_entry.get(), password_entry.get())
            mycursor.execute(f'SELECT password from master where adminname="{user_entry.get()}"')
            password = str(mycursor.fetchone())


            if password[2:-3] == password_entry.get():

                login.destroy()
                create_page()

            else:

                user_entry.delete(False, END)
                password_entry.delete(False, END)
                messagebox.showerror("Error", "Wrong Password Or Username")

        except:

            messagebox.showerror("ERROR", "Invalid Username")


def create_page():

    global sign_page
    global login
    global admin
    global name
    global passwd


    sign_page = Tk()
    sign_page.geometry("480x540")
    sign_page.title("Create Admin")

    back = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\backcus.png")
    back = back.resize((480, 540), Image.ANTIALIAS)
    back = ImageTk.PhotoImage(back)

    mainlabel = Label(sign_page, image=back)
    mainlabel.place(x=0, y=0)

    title_label = Label(sign_page, text="ADD ADMINISTRATOR", font=("Helvetica", 30, "bold"), fg="#2730e3", bg="black")
    title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=30)

    # Fill options

    # consumer_label = Label(window, text="CONSUMER NO.", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    # consumer_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)

    admin_label = Label(sign_page, text="ADMIN NAME", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    admin_label.grid(row=2, column=0, sticky="w", padx=20, pady=10)

    name_label = Label(sign_page, text="NAME", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    name_label.grid(row=3, column=0, sticky="w", padx=20, pady=10)

    passwd_label = Label(sign_page, text="PASSWORD", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    passwd_label.grid(row=4, column=0, sticky="w", padx=20, pady=10)



    # Entry boxes

    admin = Entry(sign_page, width=30)
    admin.grid(row=2, column=1, padx=20)

    name = Entry(sign_page, width=30)
    name.grid(row=3, column=1, padx=20)

    passwd = Entry(sign_page, width=30)
    passwd.grid(row=4, column=1, padx=20)



    # Submit Button

    submit_button = Button(sign_page, text="SUBMIT", font=("Helvetica", 10, "bold"), fg="black", bg="green",
                           command=add_admin)
    submit_button.grid(row=10, column=1, padx=20, pady=20, columnspan=1)

    # Clear Fields

    clear_button = Button(sign_page, text="CLEAR", font=("Helvetica", 10, "bold"), fg="black", bg="grey",
                          command=clear_page)
    clear_button.grid(row=10, column=0, padx=20, columnspan=2)

    # Back Button
    back_button = Button(sign_page, text="<<BACK<<", font=("Helvetica", 10, "bold"), fg="black", bg="grey",
                         command=backtologin)
    back_button.grid(row=10, column=1, sticky="e")

    sign_page.mainloop()


def submit():

    global user_entry
    global password_entry
    global user_name
    global password
    global login

    if user_entry.get() == "":
        messagebox.showerror("ERROR", "Invalid Entry")

    elif password_entry.get() == "":
        messagebox.showerror("ERROR", "Invalid Entry")

    else:


        try:

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Iamankit@02",
                database="ebm"
            )

            cursor = db.cursor()

            name_admin = user_entry.get()
            cursor.execute(f'SELECT password from master where adminname="{name_admin}"')
            password = str(cursor.fetchone())


            if password[2:-3] == password_entry.get():

                login.destroy()
                d = HomePageMaster(name_admin)
                d.mainhomepage()

            else:

                user_entry.delete(False, END)
                password_entry.delete(False, END)
                messagebox.showerror("Error", "Wrong Password Or Username")

        except EXCEPTION as e:

            messagebox.showerror("ERROR", "Invalid Username")


def submit_logintab():

    global user_entry2
    global password_entry2
    global login

    if user_entry2.get() == "":
        messagebox.showerror("ERROR", "Invalid Entry")

    elif password_entry2.get() == "":
        messagebox.showerror("ERROR", "Invalid Entry")

    else:


        try:

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Iamankit@02",
                database="ebm"
            )

            cursor = db.cursor()

            admin_name = user_entry2.get()
            cursor.execute(f'SELECT password from admin where admin="{admin_name}"')
            password = str(cursor.fetchone())

            if password[2:-3] == password_entry2.get():

                login.destroy()
                x = AdminPageclass(admin_name)
                x.AdminPage()


            else:

                user_entry2.delete(False, END)
                password_entry2.delete(False, END)
                messagebox.showerror("Error", "Wrong Password Or Username")

        except EXCEPTION as e:

            messagebox.showerror("ERROR", "Invalid Username")




tab_fun()

