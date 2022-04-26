from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk




class AdminPageclass:



    def __init__(self, adminname1):

        self.root = ''
        self.my_frame1 = ''
        self.my_frame2 = ''
        self.my_frame3 = ''
        self.my_ntbk = ''
        self.adminname1 = adminname1
        self.old_passwd = ""
        self.new_passwd = ""
        self.renew_passwd = ""
        self.meterno = ""
        self.name = ""
        self.address = ""
        self.zipcode = ""
        self.division = ""
        self.phno = ""
        self.tariff = ""
        self.email = ""


    def close(self, pageno1):

        self.my_ntbk.hide(pageno1)

    def clear(self, page):

        if page == 1:

            self.old_passwd.delete(0, END)
            self.new_passwd.delete(0, END)
            self.renew_passwd.delete(0, END)

        else:

            self.meterno.delete(0, END)
            self.name.delete(0, END)
            self.address.delete(0, END)
            self.zipcode.delete(0, END)
            self.division.delete(0, END)
            self.phno.delete(0, END)
            self.tariff.delete(0, END)
            self.email.delete(0, END)



    def AdminPage(self):


        self.root = Tk()
        self.root.title("Electricity Bill Management | Homepage")
        self.root.geometry("840x540")

        home_image = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\Icons\\label_image.png")
        home_image = home_image.resize((840, 540), Image.ANTIALIAS)
        home_image = ImageTk.PhotoImage(home_image)

        backimg = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\backcus.png")
        backimg = backimg.resize((840, 540), Image.ANTIALIAS)
        backimg = ImageTk.PhotoImage(backimg)

        self.my_ntbk = ttk.Notebook(self.root)
        self.my_ntbk.pack()

        self.my_frame1 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame2 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame3 = Frame(self.my_ntbk, width=840, height=540)


        self.my_frame1.pack(fil="both", expand=1)
        self.my_frame2.pack(fil="both", expand=1)
        self.my_frame3.pack(fil="both", expand=1)


        self.my_ntbk.add(self.my_frame1, text="Homepage")
        self.my_ntbk.add(self.my_frame2, text="Change Password")
        self.my_ntbk.add(self.my_frame3, text="Add Customer")


        home_label = Label(self.my_frame1, image=home_image)
        home_label.place(x=0, y=0)

        back_label2 = Label(self.my_frame2, image=backimg)
        back_label2.place(x=0, y=0)

        back_label2 = Label(self.my_frame3, image=backimg)
        back_label2.place(x=0, y=0)


        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)

        Manage_menu = Menu(my_menu)
        my_menu.add_cascade(label="Change Password", menu=Manage_menu)
        Manage_menu.add_command(label="Change password", command=self.change_passwd)
        self.my_ntbk.hide(1)
        self.my_ntbk.hide(2)

        main_label = Label(self.my_frame2, text="Change Password", font=("Helvetica", 40, "bold"),
                           fg="white", bg="black", padx=20, pady=80)
        main_label.grid(row=0, column=0, columnspan=2)

        oldpasswd_label = Label(self.my_frame2, text="Old Password", font=("Helvetica", 10, "bold"),
                                fg="white", bg="black")
        oldpasswd_label.grid(row=1, column=0)

        newpasswd_label = Label(self.my_frame2, text="New Password", font=("Helvetica", 10, "bold"),
                                fg="white", bg="black")
        newpasswd_label.grid(row=2, column=0)

        renewpasswd_label = Label(self.my_frame2, text="ReEnter New Password", font=("Helvetica", 10, "bold"),
                                  fg="white", bg="black")
        renewpasswd_label.grid(row=3, column=0)

        self.old_passwd = Entry(self.my_frame2, width=30)
        self.old_passwd.grid(row=1, column=1, pady=10, padx=10)

        self.new_passwd = Entry(self.my_frame2, width=30)
        self.new_passwd.grid(row=2, column=1, pady=10, padx=10)

        self.renew_passwd = Entry(self.my_frame2, width=30)
        self.renew_passwd.grid(row=3, column=1, pady=10, padx=10)

        submit_passwd = Button(self.my_frame2, text="Submit", font=("Helvetica", 10, "bold"),
                               fg="black", bg="green", command=self.submit_passwd)
        submit_passwd.grid(row=4, column=0, columnspan=2, pady=20)

        clear_passwd = Button(self.my_frame2, text="Clear", font=("Helvetica", 10, "bold"),
                              fg="black", bg="grey", command=lambda: self.clear(1))
        clear_passwd.grid(row=4, column=1, pady=20)

        close_passwd = Button(self.my_frame2, text="Close", font=("Helvetica", 10, "bold"),
                              fg="black", bg="red", command=lambda: self.close(1))
        close_passwd.grid(row=4, column=2, pady=20)



    # Main Page Options:

        cus_img = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\user.png")
        cus_img = cus_img.resize((25, 25), Image.ANTIALIAS)
        cus_img = ImageTk.PhotoImage(cus_img)


        cus_button = Button(self.my_frame1, text="CUSTOMER", font=("Algerian", 18, "bold"),
                            padx=10, pady=5, fg="#2730e3", bg="black", image=cus_img, compound="left",
                            command=self.add_customer)
        cus_button.place(x=50, y=180)

        # view records Button

        record_img = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\record.png")
        record_img = record_img.resize((25, 25), Image.ANTIALIAS)
        record_img = ImageTk.PhotoImage(record_img)

        view_button = Button(self.my_frame1, text="RECORDS", font=("Algerian", 18, "bold"),
                             padx=10, pady=5, fg="#2730e3", bg="black", image=record_img, compound="left")
        view_button.place(x=50, y=250)

        # generate bill Button

        generate_icon = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\generate.png")
        generate_icon = generate_icon.resize((35, 35), Image.ANTIALIAS)
        generate_icon = ImageTk.PhotoImage(generate_icon)

        generate_button = Button(self.my_frame1, text="GENERATE BILL", font=("Algerian", 18, "bold"),
                                 padx=10, pady=5, fg="#2730e3", bg="black", image=generate_icon, compound="left")
        generate_button.place(x=50, y=320)

        # exit Button

        exit_icon = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\exiticon.png")
        exit_icon = exit_icon.resize((25, 25), Image.ANTIALIAS)
        exit_icon = ImageTk.PhotoImage(exit_icon)

        exit_button = Button(self.my_frame1, text="Exit", font=("Algerian", 18, "bold"),
                             padx=40, pady=5, fg="#e32727", bg="black", image=exit_icon, compound="left",
                             command=self.root.destroy)
        exit_button.place(x=50, y=420)

    # Add Customer Page

        title_label = Label(self.my_frame3, text="ADD DETAILS", font=("Helvetica", 30, "bold"), fg="#2730e3",
                            bg="black")
        title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=30)

        # Fill options

        # consumer_label = Label(window, text="CONSUMER NO.", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        # consumer_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)

        meter_label = Label(self.my_frame3, text="METER NO.", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        meter_label.grid(row=2, column=0, sticky="w", padx=20, pady=10)

        name_label = Label(self.my_frame3, text="NAME", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        name_label.grid(row=3, column=0, sticky="w", padx=20, pady=10)

        address_label = Label(self.my_frame3, text="ADDRESS", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        address_label.grid(row=4, column=0, sticky="w", padx=20, pady=10)

        zipcode_label = Label(self.my_frame3, text="ZIPCODE", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        zipcode_label.grid(row=5, column=0, sticky="w", padx=20, pady=10)

        division_label = Label(self.my_frame3, text="DIVISION", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        division_label.grid(row=6, column=0, sticky="w", padx=20, pady=10)

        phno_label = Label(self.my_frame3, text="PHONE NO.", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        phno_label.grid(row=7, column=0, sticky="w", padx=20, pady=10)

        tariff_label = Label(self.my_frame3, text="TARIFF", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        tariff_label.grid(row=8, column=0, sticky="w", padx=20, pady=10)

        email_label = Label(self.my_frame3, text="EMAIL", font=("Helvetica", 10, "bold"), fg="White", bg="black")
        email_label.grid(row=9, column=0, sticky="w", padx=20, pady=10)

        # Entry boxes

        self.meterno = Entry(self.my_frame3, width=30)
        self.meterno.grid(row=2, column=1, padx=20)

        self.name = Entry(self.my_frame3, width=30)
        self.name.grid(row=3, column=1, padx=20)

        self.address = Entry(self.my_frame3, width=30)
        self.address.grid(row=4, column=1, padx=20)

        self.zipcode = Entry(self.my_frame3, width=30)
        self.zipcode.grid(row=5, column=1, padx=20)

        self.division = Entry(self.my_frame3, width=30)
        self.division.grid(row=6, column=1, padx=20)

        self.phno = Entry(self.my_frame3, width=30)
        self.phno.grid(row=7, column=1, padx=20)

        self.tariff = Entry(self.my_frame3, width=30)
        self.tariff.grid(row=8, column=1, padx=20)

        self.email = Entry(self.my_frame3, width=30)
        self.email.grid(row=9, column=1, padx=20)

        # Submit Button

        submit_button = Button(self.my_frame3, text="SUBMIT", font=("Helvetica", 10, "bold"), fg="black", bg="green",
                               command=self.submit_customer_details)
        submit_button.grid(row=10, column=1, padx=20, pady=20, columnspan=2)

        # Clear Fields

        clear_button = Button(self.my_frame3, text="CLEAR", font=("Helvetica", 10, "bold"), fg="black", bg="grey",
                              command=lambda: self.clear(2))
        clear_button.grid(row=10, column=0, padx=20, columnspan=2)

        # Back Button
        close_button = Button(self.my_frame3, text="CLOSE", font=("Helvetica", 10, "bold"), fg="black", bg="red",
                              command=lambda: self.close(2))
        close_button.grid(row=10, column=2, sticky="e")


        self.root.mainloop()



    def change_passwd(self):


        self.my_ntbk.select(1)


    def add_customer(self):

        self.my_ntbk.select(2)


    def submit_passwd(self):

        try:
            oldPassword = self.old_passwd.get()
            newPassword = self.new_passwd.get()
            renewPassword = self.renew_passwd.get()

            if oldPassword == "":
                messagebox.showerror("ERROR", "Invalid Entry")

            elif newPassword == "":
                messagebox.showerror("ERROR", "Invalid Entry")

            elif renewPassword == "":
                messagebox.showerror("ERROR", "Invalid Entry")


            else:

                if newPassword != renewPassword:

                    self.old_passwd.delete(False, END)
                    self.new_passwd.delete(False, END)
                    self.renew_passwd.delete(False, END)
                    messagebox.showwarning("Warning", "Passwords Mismatch")


                else:

                    try:


                        db = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="Iamankit@02",
                            database="ebm"
                        )

                        cursor = db.cursor()

                        cursor.execute(f'SELECT password from admin where admin="{self.adminname1}"')
                        password = str(cursor.fetchone())


                        if password[2:-3] == oldPassword:

                            cursor.execute(f'UPDATE admin SET password="{newPassword}" WHERE admin="{self.adminname1}"')
                            db.commit()
                            messagebox.showinfo("SUBMITTED", "Successful")
                            self.my_ntbk.hide(1)

                        else:

                            self.old_passwd.delete(False, END)
                            self.new_passwd.delete(False, END)
                            self.renew_passwd.delete(False, END)
                            messagebox.showerror("Error", "Wrong Password")



                    except EXCEPTION as e:

                        messagebox.showerror("ERROR", e)

        except:

            messagebox.showerror("ERROR", "Error")


    def logout(self):

        self.root.destroy()


    def submit_customer_details(self):

        lis = [self.meterno, self.name, self.address, self.zipcode, self.division, self.phno, self.tariff, self.email]
        flag = 0

        for i in lis:

            if i.get() == "":
                flag = 1
                break


        if flag == 1:
            messagebox.showerror("ERROR", "Invalid Entry")

        else:

            response = messagebox.askyesno("SUBMIT", "Are you sure")

            if response == 1:

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
                    values = (self.meterno.get(), self.name.get(), self.zipcode.get(), self.address.get(), self.tariff.get(),
                              self.division.get(), self.email.get(),
                              self.phno.get())

                    cursor.execute(sql_command, values)

                    db.commit()
                    self.clear(2)
                    messagebox.showinfo("SAVE", "SUCCESS")

                except:

                    messagebox.showerror("Error", "Invalid Entry")

            else:

                pass



adminname = "ankit@ankit"
x = AdminPageclass(adminname)
x.AdminPage()
