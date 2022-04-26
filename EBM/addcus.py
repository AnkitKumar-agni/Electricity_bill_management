from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

global window
global home1
global meterno
global name
global zipcode
global address
global tariff
global division
global email
global phno


def cus():

    global home1

    home1.destroy()
    Customer()

def exit():

    global home1

    var = messagebox.askyesno("EXIT", "Are You Sure")

    if var == 1:
        home1.destroy()

    else:

        pass



def backtohomepagemaster():
    global window
    global home1

    window.destroy()
    home1 = Tk()
    home1.geometry("840x540")
    home1.title("Electricity Bill Management | Homepage")

    home_image = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\Icons\\label_image.png")
    home_image = home_image.resize((840, 540), Image.ANTIALIAS)
    home_image = ImageTk.PhotoImage(home_image)

    my_menu = Menu(home1)
    home1.config(menu=my_menu)

    Manage_menu = Menu(my_menu)
    my_menu.add_cascade(label="Manage Admins", menu=Manage_menu)
    Manage_menu.add_command(label="List Of Admins")
    Manage_menu.add_separator()
    Manage_menu.add_command(label="Delete Admin")

    changepasswd_menu = Menu(my_menu)
    my_menu.add_cascade(label="Change Password", menu=changepasswd_menu)
    changepasswd_menu.add_command(label="Change Password")

    logout_menu = Menu(my_menu)
    my_menu.add_cascade(label="Logout", menu=logout_menu)
    logout_menu.add_command(label="Logout")


    home_label = Label(home1, image=home_image)
    home_label.place(x=0, y=0)

    label_1 = Label(home1,
                    text="Electricity Bill Management",
                    padx=150,
                    pady=20,
                    font=('Garamond', 40, "bold"),
                    bg="black", fg="Blue")

    label_1.grid(row=0, column=0)

    # Customer Button

    cus_img = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\user.png")
    cus_img = cus_img.resize((25, 25), Image.ANTIALIAS)
    cus_img = ImageTk.PhotoImage(cus_img)

    cus_button = Button(home1, text="CUSTOMER", font=("Algerian", 18, "bold"),
                        padx=10, pady=5, fg="#2730e3", bg="black", image=cus_img, compound="left", command=cus)
    cus_button.place(x=50, y=180)

    # view records Button

    record_img = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\record.png")
    record_img = record_img.resize((25, 25), Image.ANTIALIAS)
    record_img = ImageTk.PhotoImage(record_img)

    view_button = Button(home1, text="RECORDS", font=("Algerian", 18, "bold"),
                         padx=10, pady=5, fg="#2730e3", bg="black", image=record_img, compound="left")
    view_button.place(x=50, y=250)

    # generate bill Button

    generate_icon = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\generate.png")
    generate_icon = generate_icon.resize((35, 35), Image.ANTIALIAS)
    generate_icon = ImageTk.PhotoImage(generate_icon)

    generate_button = Button(home1, text="GENERATE BILL", font=("Algerian", 18, "bold"),
                             padx=10, pady=5, fg="#2730e3", bg="black", image=generate_icon, compound="left")
    generate_button.place(x=50, y=320)

    # exit Button

    exit_icon = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\exiticon.png")
    exit_icon = exit_icon.resize((25, 25), Image.ANTIALIAS)
    exit_icon = ImageTk.PhotoImage(exit_icon)

    exit_button = Button(home1, text="Exit", font=("Algerian", 18, "bold"),
                         padx=40, pady=5, fg="#e32727", bg="black", image=exit_icon, compound="left",
                         command=exit)
    exit_button.place(x=50, y=420)

    home1.mainloop()







def clear():

    global meterno
    global name
    global zipcode
    global address
    global tariff
    global division
    global email
    global phno

    meterno.delete(0, END)
    name.delete(0, END)
    zipcode.delete(0, END)
    address.delete(0, END)
    tariff.delete(0, END)
    division.delete(0, END)
    email.delete(0, END)
    phno.delete(0, END)



def submit():

    global meterno
    global name
    global zipcode
    global address
    global tariff
    global division
    global email
    global phno

    try:

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Iamankit@02",
            database="ebm"
        )

        cursor = db.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS customer(Meterno INT(10), Name VARCHAR(50), Zipcode INT(8), "
                       "Address VARCHAR(80),Tariff INT(10), Division VARCHAR(20), Email VARCHAR(40), Phno INT(10),"
                       "ConsumerNO INT AUTO_INCREMENT PRIMARY KEY)")


        sql_command = "INSERT INTO customer(Meterno, name, zipcode, address, Tariff, division, Email, phno) " \
                      "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (meterno.get(), name.get(), zipcode.get(), address.get(), tariff.get(), division.get(), email.get(),
                  phno.get())
        cursor.execute(sql_command, values)

        db.commit()
        clear()

    except:

        messagebox.showerror("Error", "Invalid Entry")



def Customer():

    global window
    global meterno
    global name
    global zipcode
    global address
    global tariff
    global division
    global email
    global phno
    # global home1

    window = Tk()

    window.title("CUSTOMER")
    window.geometry("480x540")

    back = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\backcus.png")
    back = back.resize((480, 540), Image.ANTIALIAS)
    back = ImageTk.PhotoImage(back)

    mainlabel = Label(window, image=back)
    mainlabel.place(x=0, y=0)

    title_label = Label(window, text="ADD DETAILS", font=("Helvetica", 30, "bold"), fg="#2730e3", bg="black")
    title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=30)



    # Fill options

    # consumer_label = Label(window, text="CONSUMER NO.", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    # consumer_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)

    meter_label = Label(window, text="METER NO.", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    meter_label.grid(row=2, column=0, sticky="w", padx=20, pady=10)

    name_label = Label(window, text="NAME", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    name_label.grid(row=3, column=0, sticky="w", padx=20, pady=10)

    address_label = Label(window, text="ADDRESS", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    address_label.grid(row=4, column=0, sticky="w", padx=20, pady=10)

    zipcode_label = Label(window, text="ZIPCODE", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    zipcode_label.grid(row=5, column=0, sticky="w", padx=20, pady=10)

    division_label = Label(window, text="DIVISION", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    division_label.grid(row=6, column=0, sticky="w", padx=20, pady=10)

    phno_label = Label(window, text="PHONE NO.", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    phno_label.grid(row=7, column=0, sticky="w", padx=20, pady=10)

    tariff_label = Label(window, text="TARIFF", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    tariff_label.grid(row=8, column=0, sticky="w", padx=20, pady=10)

    email_label = Label(window, text="EMAIL", font=("Helvetica", 10, "bold"), fg="White", bg="black")
    email_label.grid(row=9, column=0, sticky="w", padx=20, pady=10)


    # Entry boxes

    meterno = Entry(window, width=30)
    meterno.grid(row=2, column=1, padx=20)

    name = Entry(window, width=30)
    name.grid(row=3, column=1, padx=20)

    address = Entry(window, width=30)
    address.grid(row=4, column=1, padx=20)

    zipcode = Entry(window, width=30)
    zipcode.grid(row=5, column=1, padx=20)

    division = Entry(window, width=30)
    division.grid(row=6, column=1, padx=20)

    phno = Entry(window, width=30)
    phno.grid(row=7, column=1, padx=20)

    tariff = Entry(window, width=30)
    tariff.grid(row=8, column=1, padx=20)

    email = Entry(window, width=30)
    email.grid(row=9, column=1, padx=20)



    # Submit Button

    submit_button = Button(window, text="SUBMIT", font=("Helvetica", 10, "bold"), fg="black", bg="green",
                           command=submit)
    submit_button.grid(row=10, column=1, padx=20, pady=20, columnspan=2)

    # Clear Fields

    clear_button = Button(window, text="CLEAR", font=("Helvetica", 10, "bold"), fg="black", bg="grey", command=clear)
    clear_button.grid(row=10, column=0, padx=20, columnspan=2)


    # Back Button
    back_button = Button(window, text="<<BACK<<", font=("Helvetica", 10, "bold"), fg="black", bg="grey",
                         command=backtohomepagemaster)
    back_button.grid(row=10, column=2, sticky="e")


    window.mainloop()

