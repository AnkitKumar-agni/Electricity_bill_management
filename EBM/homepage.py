from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import webbrowser
import datetime




class AdminPageclass:



    def __init__(self, adminname1):

        self.root = ''
        self.my_frame1 = ''
        self.my_frame2 = ''
        self.my_frame3 = ''
        self.my_frame4 = ''
        self.my_frame5 = ''
        self.my_frame6 = ''
        self.my_frame7 = ''
        self.my_frame11 = ""
        self.my_frame12 = ""
        self.my_frame13 = ""
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

        global disp_label


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
        self.my_frame4 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame5 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame6 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame7 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame11 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame12 = Frame(self.my_ntbk, width=840, height=540)
        self.my_frame13 = Frame(self.my_ntbk, width=840, height=540)


        self.my_frame1.pack(fil="both", expand=1)
        self.my_frame2.pack(fil="both", expand=1)
        self.my_frame3.pack(fil="both", expand=1)
        self.my_frame4.pack(fil="both", expand=1)
        self.my_frame5.pack(fil="both", expand=1)
        self.my_frame6.pack(fil="both", expand=1)
        self.my_frame7.pack(fil="both", expand=1)
        self.my_frame11.pack(fil="both", expand=1)
        self.my_frame12.pack(fil="both", expand=1)
        self.my_frame13.pack(fil="both", expand=1)


        self.my_ntbk.add(self.my_frame1, text="Homepage")
        self.my_ntbk.add(self.my_frame2, text="Change Password")
        self.my_ntbk.add(self.my_frame3, text="Add Customer")
        self.my_ntbk.add(self.my_frame4, text="Search Records")
        self.my_ntbk.add(self.my_frame5, text="Search Customer")
        self.my_ntbk.add(self.my_frame6, text="See List")
        self.my_ntbk.add(self.my_frame7, text="Generate Bill")
        self.my_ntbk.add(self.my_frame11, text="Search Bill")
        self.my_ntbk.add(self.my_frame12, text="Search Bill")
        self.my_ntbk.add(self.my_frame13, text="Payment")



        home_label = Label(self.my_frame1, image=home_image)
        home_label.place(x=0, y=0)

        back_label2 = Label(self.my_frame2, image=backimg)
        back_label2.place(x=0, y=0)

        back_label2 = Label(self.my_frame3, image=backimg)
        back_label2.place(x=0, y=0)

        home_label = Label(self.my_frame4, image=home_image)
        home_label.place(x=0, y=0)

        back_label2 = Label(self.my_frame5, image=backimg)
        back_label2.place(x=0, y=0)

        back_label2 = Label(self.my_frame6, image=backimg)
        back_label2.place(x=0, y=0)

        back_label2 = Label(self.my_frame7, image=home_image)
        back_label2.place(x=0, y=0)

        back_label3 = Label(self.my_frame11, image=backimg)
        back_label3.place(x=0, y=0)

        back_label3 = Label(self.my_frame12, image=backimg)
        back_label3.place(x=0, y=0)

        back_label3 = Label(self.my_frame13, image=home_image)
        back_label3.place(x=0, y=0)


        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)

        Manage_menu = Menu(my_menu)
        my_menu.add_cascade(label="Change Password", menu=Manage_menu)
        Manage_menu.add_command(label="Change password", command=self.change_passwd)
        self.my_ntbk.hide(1)
        self.my_ntbk.hide(2)
        self.my_ntbk.hide(3)
        self.my_ntbk.hide(4)
        self.my_ntbk.hide(5)
        self.my_ntbk.hide(6)
        self.my_ntbk.hide(7)
        self.my_ntbk.hide(8)
        self.my_ntbk.hide(9)

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
        cus_button.place(x=50, y=120)

        # view records Button

        record_img = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\record.png")
        record_img = record_img.resize((25, 25), Image.ANTIALIAS)
        record_img = ImageTk.PhotoImage(record_img)

        view_button = Button(self.my_frame1, text="RECORDS", font=("Algerian", 18, "bold"),
                             padx=10, pady=5, fg="#2730e3", bg="black", image=record_img, compound="left",
                             command=self.Records)
        view_button.place(x=50, y=190)

        # generate bill Button

        generate_icon = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\generate.png")
        generate_icon = generate_icon.resize((35, 35), Image.ANTIALIAS)
        generate_icon = ImageTk.PhotoImage(generate_icon)

        generate_button = Button(self.my_frame1, text="GENERATE BILL", font=("Algerian", 18, "bold"),
                                 padx=10, pady=5, fg="#2730e3", bg="black", image=generate_icon, compound="left",
                                 command=self.generate_bill)
        generate_button.place(x=50, y=260)

        # Payment Page

        payment_img = Image.open("C:\\Users\\dell\\PycharmProjects\\EBM\\icons\\payment.png")
        payment_img = payment_img.resize((25, 25), Image.ANTIALIAS)
        payment_img = ImageTk.PhotoImage(payment_img)

        payment_button = Button(self.my_frame1, text="Payment", font=("Algerian", 18, "bold"),
                                padx=10, pady=5, fg="#2730e3", bg="black", image=payment_img, compound="left",
                                command=self.open_payment)
        payment_button.place(x=50, y=320)

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
        ################################################################################################################

        # Viewing Records

        view_head_label = Label(self.my_frame4, text="SEARCH RECORD", font=("Helvetica", 30, "bold"), fg="blue",
                                bg="black", padx=20, pady=20)
        view_head_label.grid(row=0, column=0)

        search_0ne_button = Button(self.my_frame4, text="Search One Customer", font=("Helvetica", 15, "bold"),
                                   fg="yellow", bg="black", padx=20, pady=10, command=self.See_one_customer)
        search_0ne_button.place(x=150, y=200)

        search_list_button = Button(self.my_frame4, text="See Customer List", font=("Helvetica", 15, "bold"),
                                    fg="yellow", bg="black", padx=20, pady=10, command=self.See_list)
        search_list_button.place(x=150, y=280)

        search_bill_button = Button(self.my_frame4, text="Search Bill Through Bill No", font=("Helvetica", 15, "bold"),
                                    fg="yellow", bg="black", padx=20, pady=10, command=self.open_search_bill)
        search_bill_button.place(x=150, y=350)

        search_bill_con_button = Button(self.my_frame4, text="Search Bill Through Consumer No",
                                        font=("Helvetica", 15, "bold"),
                                        fg="yellow", bg="black", padx=20, pady=10, command=self.open_search_conbill)
        search_bill_con_button.place(x=150, y=420)

        closesearch_button = Button(self.my_frame4, text=" X Close", font=("Helvetica", 10, "bold"),
                                    fg="black", bg="red", command=lambda: self.close(3))
        closesearch_button.place(x=680, y=50)

        disp_label = Label(self.my_frame5, text="", font=("Helvetica", 10, "bold"), fg="white", bg="black")
        disp_label.place(x=120, y=220)

        #########################################################################################################

        # search One Customer

        view_head_label = Label(self.my_frame5, text="SEARCH CUSTOMER", font=("Helvetica", 30, "bold"), fg="blue",
                                bg="black", padx=20, pady=20)
        view_head_label.grid(row=0, column=0)

        view_con_label = Label(self.my_frame5, text="Consumer No:", font=("Helvetica", 10, "bold"), fg="white",
                               bg="black", padx=20, pady=20)
        view_con_label.grid(row=1, column=0)

        self.con = Entry(self.my_frame5, width=30)
        self.con.grid(row=1, column=2, padx=20)

        search_record_button = Button(self.my_frame5, text="Search", font=("Helvetica", 10, "bold"), fg="black",
                                      bg="green", padx=30, command=self.search_one_customer)
        search_record_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        close_one_button = Button(self.my_frame5, text=" X Close", font=("Helvetica", 10, "bold"),
                                  fg="black", bg="red", command=lambda: self.close(4))
        close_one_button.place(x=680, y=30)

        ################################################################################################################

        # search list of customers

        view_head_label = Label(self.my_frame6, text="SEARCH CUSTOMER", font=("Helvetica", 30, "bold"), fg="blue",
                                bg="black", padx=20, pady=20)
        view_head_label.grid(row=0, column=0)

        view_list_label = Label(self.my_frame6, text="Search", font=("Helvetica", 12, "bold"), fg="white",
                                bg="black")
        view_list_label.grid(row=1, column=0)

        self.view_list_entry = Entry(self.my_frame6, width=30)
        self.view_list_entry.grid(row=1, column=1, padx=10)

        self.drop = ttk.Combobox(self.my_frame6, values=["Search By..", "Division", "Name", "Zipcode", "Tariff"])
        self.drop.current(0)
        self.drop.grid(row=1, column=2)

        search_consumer_button = Button(self.my_frame6, text="Search", font=("Helvetica", 10), bg="green", fg="black",
                                        command=self.search_list)
        search_consumer_button.grid(row=2, column=0)

        # my_tree = ttk.Treeview(self.my_frame9)
        #
        # my_tree['columns'] = ("NAME", "Consumer No", "Meter No")
        #
        # my_tree.column("#0", anchor=W, width=0)
        # my_tree.column("NAME", anchor=W, width=120)
        # my_tree.column("Consumer No", anchor=W, width=120)
        # my_tree.column("Meter No", anchor=W, width=120)
        #
        # my_tree.heading("NAME", text="Name", anchor=W)
        # my_tree.heading("Consumer No", text="Consumer No", anchor=W)
        # my_tree.heading("Meter No", text="Meter No", anchor=W)
        # my_tree.grid(row=3, column=0, padx=20, pady=20)

        close_list_button = Button(self.my_frame6, text=" X Close", font=("Helvetica", 10, "bold"),
                                   fg="black", bg="red", command=lambda: self.close(5))
        close_list_button.place(x=680, y=30)

        ########################################################################################################################

        search_bill_label = Label(self.my_frame11, text="Search Bill", font=("Helvetica", 30, "bold"), fg="blue",
                                  bg="black", padx=20, pady=20)
        search_bill_label.grid(row=0, column=0)

        entry_bill_label = Label(self.my_frame11, text="Bill No. ", font=("Helvetica", 12, "bold"), fg="white",
                                 bg="black", padx=20, pady=20)
        entry_bill_label.grid(row=1, column=0)

        self.search_bill_no = Entry(self.my_frame11, width=30)
        self.search_bill_no.grid(row=1, column=1)

        sub_button = Button(self.my_frame11, text="Submit", font=("Helvetica", 12, "bold"), fg="black",
                            bg="green", padx=10, command=self.search_billno)
        sub_button.grid(row=2, column=1, columnspan=2)

        close_bill_search_button = Button(self.my_frame11, text=" X Close", font=("Helvetica", 10, "bold"),
                                          fg="black", bg="red", command=lambda: self.close(7))
        close_bill_search_button.place(x=680, y=30)
#######################################################################################################################
        # Search bill through Consumer No

        search_bill_label12 = Label(self.my_frame12, text="Search Bill", font=("Helvetica", 30, "bold"), fg="blue",
                                    bg="black", padx=20, pady=20)
        search_bill_label12.grid(row=0, column=0)

        entry_bill_label12 = Label(self.my_frame12, text="Consumer No.", font=("Helvetica", 12, "bold"), fg="white",
                                   bg="black", padx=20, pady=20)
        entry_bill_label12.grid(row=1, column=0)

        self.bill_conentry = Entry(self.my_frame12, width=30)
        self.bill_conentry.grid(row=1, column=1)

        month_label = Label(self.my_frame12, text="Month", font=("Helvetica", 12, "bold"), fg="white",
                            bg="black", padx=20, pady=20)
        month_label.grid(row=2, column=0)

        v = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]

        self.drop1 = ttk.Combobox(self.my_frame12, values=v)
        self.drop1.current(0)
        self.drop1.grid(row=2, column=1)

        year_label = Label(self.my_frame12, text="Year", font=("Helvetica", 12, "bold"), fg="white",
                           bg="black", padx=20, pady=20)
        year_label.grid(row=3, column=0)

        self.bill_yearentry = Entry(self.my_frame12, width=30)
        self.bill_yearentry.grid(row=3, column=1)

        sub_billbutton = Button(self.my_frame12, text="Submit", font=("Helvetica", 12, "bold"), fg="black",
                                bg="green", padx=10, command=self.search_bill_con)
        sub_billbutton.grid(row=4, column=2, columnspan=2)

        close_bill_search_button = Button(self.my_frame12, text=" X Close", font=("Helvetica", 10, "bold"),
                                          fg="black", bg="red", command=lambda: self.close(8))
        close_bill_search_button.place(x=680, y=30)

#######################################################################################################
        # Generate Bill

        generate_head_label = Label(self.my_frame7, text="BILL GENERATION", font=("Helvetica", 30, "bold"), fg="blue",
                                    bg="black", padx=20, pady=20)
        generate_head_label.grid(row=0, column=0)

        generate_label = Label(self.my_frame7, text="Consumer No:", font=("Helvetica", 10, "bold"), fg="white",
                               bg="black", padx=20)
        generate_label.grid(row=1, column=0, pady=10)

        generate_label1 = Label(self.my_frame7, text="Current Reading", font=("Helvetica", 10, "bold"), fg="white",
                                bg="black", padx=20)
        generate_label1.grid(row=2, column=0, pady=10)

        self.consumer_no = Entry(self.my_frame7, width=30)
        self.consumer_no.grid(row=1, column=1)

        self.cur = Entry(self.my_frame7, width=30)
        self.cur.grid(row=2, column=1, padx=20, pady=10)

        generate_bill_button = Button(self.my_frame7, text="Generate Bill", font=("Helvetica", 10, "bold"), fg="black",
                                      bg="green", padx=30, command=self.generate_bill_fun)
        generate_bill_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        close_list_button = Button(self.my_frame7, text=" X Close", font=("Helvetica", 10, "bold"),
                                   fg="black", bg="red", command=lambda: self.close(6))
        close_list_button.place(x=680, y=30)

        ######################################################################################################################

        # Payment

        view_head_label_payment = Label(self.my_frame13, text="PAYMENT", font=("Helvetica", 30, "bold"),
                                        fg="yellow", bg="black", padx=20, pady=20)
        view_head_label_payment.grid(row=0, column=0)

        consumer_entry_label = Label(self.my_frame13, text="Consumer No:", font=("Helvetica", 10, "bold"), fg="white",
                                     bg="black", padx=20, pady=20)
        consumer_entry_label.grid(row=1, column=0)

        amount_entry_label = Label(self.my_frame13, text="Amount", font=("Helvetica", 10, "bold"), fg="white",
                                   bg="black", padx=20, pady=20)
        amount_entry_label.grid(row=2, column=0)

        self.paycon = Entry(self.my_frame13, width=30)
        self.paycon.grid(row=1, column=1)

        self.payamt = Entry(self.my_frame13, width=30)
        self.payamt.grid(row=2, column=1)

        pay_submit = Button(self.my_frame13, text="Submit", font=("Helvetica", 12, "bold"), bg="green", fg='black',
                            padx=20, pady=5, command=self.pay_and_save)
        pay_submit.grid(row=3, column=1, columnspan=2)

        close_pay_button = Button(self.my_frame13, text=" X Close", font=("Helvetica", 10, "bold"),
                                  fg="black", bg="red", command=lambda: self.close(9))
        close_pay_button.place(x=680, y=30)


        self.root.mainloop()



    def change_passwd(self):


        self.my_ntbk.select(1)


    def add_customer(self):

        self.my_ntbk.select(2)

    def Records(self):

        self.my_ntbk.select(3)

    def See_one_customer(self):

        self.my_ntbk.select(4)


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
                    values = (int(self.meterno.get()), self.name.get(), int(self.zipcode.get()), self.address.get(), int(self.tariff.get()),
                              self.division.get(), self.email.get(), int(self.phno.get()))

                    cursor.execute(sql_command, values)

                    db.commit()
                    self.clear(2)
                    messagebox.showinfo("SAVE", "SUCCESS")

                except:

                    messagebox.showerror("Error", "Invalid Entry")


            else:

                pass

    def search_one_customer(self):

        global disp_label

        disp_label.place_forget()


        consumer_no = self.con.get()


        if consumer_no == "":
            messagebox.showerror("ERROR", "Invalid entry")

        elif consumer_no == " ":
            messagebox.showerror("ERROR", "Invalid entry")

        else:

            consumer_no = int(consumer_no)

            try:

                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Iamankit@02",
                    database="ebm"
                )

                cursor = db.cursor()
                cursor.execute(f'SELECT * from customer where consumerno={consumer_no}')
                search_result = cursor.fetchall()


                if search_result == []:

                    messagebox.showwarning("Warning", "No Data Found")
                else:


                    text = str()

                    for result1 in search_result:

                        text = f' NAME :                  {result1[1]} \n\n CONSUMER NO :    {result1[8]} \n\n METER NO :            {result1[0]} \n\n ' \
                               f'ADDRESS :             {result1[3]} \n\n ZIPCODE :               {result1[2]} \n\n DIVISION :               {result1[5]} \n\n ' \
                               f'TARIFF :                  {result1[4]} \n\n PHONE NO. :           {result1[7]} \n\n EMAIL :                  {result1[6]}'


                    disp_label = Label(self.my_frame5, text=text, font=("Helvetica", 10, "bold"), fg="white", bg="black",
                                       justify=LEFT)
                    disp_label.place(x=170, y=200)





            except:

                messagebox.showerror("ERROR", "!!ERROR!!")

    def See_list(self):

        self.my_ntbk.select(5)

    def search_list(self):

        global my_tree

        my_tree = ttk.Treeview(self.my_frame6)

        my_tree['columns'] = ("NAME", "Consumer No", "Meter No")

        my_tree.column("#0", anchor=W, width=0)
        my_tree.column("NAME", anchor=W, width=120)
        my_tree.column("Consumer No", anchor=W, width=120)
        my_tree.column("Meter No", anchor=W, width=120)

        my_tree.heading("NAME", text="Name", anchor=W)
        my_tree.heading("Consumer No", text="Consumer No", anchor=W)
        my_tree.heading("Meter No", text="Meter No", anchor=W)
        my_tree.grid(row=3, column=0, padx=20, pady=20)


        selected = self.drop.get()
        value = self.view_list_entry.get()

        if value == "":
            messagebox.showerror("ERROR", "Invalid Entry")

        elif value == " ":
            messagebox.showerror("ERROR", "Invalid Entry")

        else:

            if selected == "Search by...":

                messagebox.showwarning("WARNING", "Invalid Selection")


            elif selected == "Division":



                if value == "":
                    messagebox.showerror("ERROR", "Invalid entry")

                elif value == " ":

                    messagebox.showerror("ERROR", "Invalid entry")

                else:



                    try:

                        db = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="Iamankit@02",
                            database="ebm"
                        )

                        cursor = db.cursor()
                        cursor.execute(f'SELECT * from customer where division="{value}"')
                        search_result = cursor.fetchall()

                        if search_result == []:

                            messagebox.showwarning("Warning", "No Data Found")
                        else:


                            i = 0

                            for result1 in search_result:

                                my_tree.insert(parent="", index='end', iid=i, values=(result1[1], result1[8], result1[0]))
                                i += 1



                    except:

                        messagebox.showerror("ERROR", "!!ERROR!!")


            elif selected == "Name":

                if value == "":
                    messagebox.showerror("ERROR", "Invalid entry")

                elif value == " ":

                    messagebox.showerror("ERROR", "Invalid entry")

                else:

                    try:

                        db = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="Iamankit@02",
                            database="ebm"
                        )

                        cursor = db.cursor()
                        cursor.execute(f'SELECT * from customer where Name="{value}"')
                        search_result = cursor.fetchall()

                        if search_result == []:

                            messagebox.showwarning("Warning", "No Data Found")
                        else:


                            i = 0

                            for result1 in search_result:
                                my_tree.insert(parent="", index='end', iid=i, values=(result1[1], result1[8], result1[0]))
                                i += 1



                    except:

                        messagebox.showerror("ERROR", "!!ERROR!!")


            elif selected == "Zipcode":

                if value == "":
                    messagebox.showerror("ERROR", "Invalid entry")

                elif value == " ":

                    messagebox.showerror("ERROR", "Invalid entry")

                else:

                    value = int(value)

                    try:

                        db = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="Iamankit@02",
                            database="ebm"
                        )

                        cursor = db.cursor()
                        cursor.execute(f'SELECT * from customer where Zipcode="{value}"')
                        search_result = cursor.fetchall()

                        if search_result == []:

                            messagebox.showwarning("Warning", "No Data Found")
                        else:


                            i = 0

                            for result1 in search_result:
                                my_tree.insert(parent="", index='end', iid=i, values=(result1[1], result1[8], result1[0]))
                                i += 1

                    except:

                        messagebox.showerror("ERROR", "!!ERROR!!")


            elif selected == "Tariff":

                if value == "":
                    messagebox.showerror("ERROR", "Invalid entry")

                elif value == " ":

                    messagebox.showerror("ERROR", "Invalid entry")

                else:

                    value = int(value)

                    try:

                        db = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            passwd="Iamankit@02",
                            database="ebm"
                        )

                        cursor = db.cursor()
                        cursor.execute(f'SELECT * from customer where Tariff="{value}"')
                        search_result = cursor.fetchall()

                        if search_result == []:

                            messagebox.showwarning("Warning", "No Data Found")
                        else:

                            i = 0

                            for result1 in search_result:
                                my_tree.insert(parent="", index='end', iid=i, values=(result1[1], result1[8], result1[0]))
                                i += 1

                    except:

                        messagebox.showerror("ERROR", "!!ERROR!!")

            else:

                messagebox.showwarning("WARNING", "No Data Found")

    def generate_bill(self):

        self.my_ntbk.select(6)


    def generate_bill_fun(self):


        global d
        global consumer
        global total
        global current_reading
        global tariff
        global curr_date
        global curr_month
        global outstanding
        global prev_reading
        global rate
        global fixd_charge
        global phone
        global curr_year
        global net
        tariff = 0
        current_reading = self.cur.get()
        consumer = self.consumer_no.get()
        d = datetime.datetime.now()
        curr_date = d.strftime("%x")
        curr_month = d.strftime("%B")
        curr_year = d.strftime("%Y")
        cur_time = d.strftime("%X")

        outstanding = 0
        prev_reading = 0
        rate = 0
        fixd_charge = 0
        phone = 0
        division = ''
        add = ''
        name = ''
        meterno = 00
        net = 0


        if current_reading == "":

            messagebox.showerror("ERROR", "Invalid Entry")

        elif consumer == "":
            messagebox.showerror("ERROR", "Invalid Entry")


        else:

            consumer = int(consumer)
            current_reading = int(current_reading)

            try:

                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Iamankit@02",
                    database="ebm"
                )

                root1 = Tk()
                root1.title('BILL')

                root1.geometry("400x680")

                # Create A Main Frame
                main_frame = Frame(root1)
                main_frame.pack(fill=BOTH, expand=1)

                # Create A Canvas
                my_canvas = Canvas(main_frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

                # Add A Scrollbar To The Canvas
                my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # Configure The Canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

                # Create ANOTHER Frame INSIDE the Canvas
                second_frame = Frame(my_canvas)

                # Add that New frame To a Window In The Canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


                cursor = db.cursor()

                try:

                    cursor.execute(f'SELECT * from customer where ConsumerNO={consumer}')
                    search_result = cursor.fetchall()

                    for data in search_result:

                        tariff = data[4]
                        phone = data[7]
                        division = data[5]
                        add = data[3]
                        name = data[1]
                        meterno = data[0]

                except:

                    messagebox.showwarning("Warning", "No Data found")



                try:


                    cursor.execute(f'SELECT * from tariff where T_id="{int(tariff)}"')
                    tariff_result = cursor.fetchall()

                    for i in tariff_result:
                        fixd_charge = int(i[2])
                        rate = int(i[1])

                except:

                    messagebox.showwarning("Warning", "No Data found")



                try:
                    cursor.execute(f'SELECT dob, reading as last FROM reading where con_no={consumer} ORDER BY dob DESC LIMIT 1')
                    reading_data = cursor.fetchall()

                    for read in reading_data:
                        prev_date = read[0]
                        prev_reading = int(read[1])
                        print(prev_reading)
                        print(prev_date)

                except:

                    messagebox.showwarning("Warning", "No Data found")

                try:
                     cursor.execute(f'SELECT out_amount as last FROM outstanding_amt where con_no={consumer} ORDER BY date_reading DESC LIMIT 1')
                     out = cursor.fetchall()

                     for outamt in out:
                         outstanding = outamt[0]

                except:

                    messagebox.showwarning("Warning", "No Data found")


                diff_reading = current_reading - prev_reading
                energy_charge = diff_reading * rate
                total = energy_charge + fixd_charge
                net = total + outstanding



                bill_content = f' Electricity Department \n\n\n Bill \n\n\n\n\n' \
                               f'Division : {division} \n\n Consumer No. : {consumer} \n\n Name : {name} \n\n ' \
                               f'Address : {add} \n\n Phone No. : {phone}' \
                               f'\n\n\n --------Comercial Detaills-------- \n\n\n ' \
                               f'Tariff : {tariff} \n\n Load : 220V \n\n' \
                               f'--------Meter Details-------- \n\n\n' \
                               f'Meter No. : {meterno} \n\n ' \
                               f'--------Billing Parameter-------- \n\n\n' \
                               f'Bill Issue Date : {curr_date} \n\n Bill Month : {curr_month} \n\n Time : {cur_time} \n\n Date Of Previous Reading' \
                               f' : {prev_date} \n\n Previous Reading : {prev_reading} \n\n Current Reading : {current_reading} \n\n ' \
                               f'Difference : {diff_reading} \n\n ' \
                               f'--------Current Assessment--------\n\n\n' \
                               f'Energy Charge : {energy_charge} \n\n Fixed Charge = {fixd_charge} \n\n ' \
                               f'--------Net Demand-------- \n\n\n' \
                               f'Total Amount : {total} \n\n Outstanding Amt : {outstanding} \n\n Net Payable: {net}'


                bill_label = Label(second_frame, text=bill_content, font=("Helvetica", 12, "bold"), justify=LEFT)
                bill_label.grid(row=0, columnspan=2, column=0)
                bill_button = Button(second_frame, text="SAVE", font=("Helvetica", 12, "bold"), bg="green", fg="black",
                                     command=self.save_bill)
                bill_button.grid(row=1, column=0, padx=40)
                pay_save_button = Button(second_frame, text="PAY & SAVE", font=("Helvetica", 12, "bold"), bg="green",
                                         fg="black", command=self.pay_and_save)
                pay_save_button.grid(row=1, column=1, padx=40)

                # try:
                #
                #     sql_command = "INSERT INTO reading(dob, con_no, reading) VALUES(%s,%s,%s)"
                #     values = (d, consumer, current_reading)
                #     cursor.execute(sql_command, values)
                #
                #     db.commit()
                #
                #
                # except EXCEPTION as ee:
                #
                #     messagebox.showerror("ERROR", "Unable to update reading")
                #     print(ee)



                root1.mainloop()

            except EXCEPTION as e:

                messagebox.showerror("ERROR", "!!ERROR!!")
                print(e)

    def save_bill(self):

        global consumer
        global d
        global current_reading
        global total
        global prev_reading
        global outstanding
        global curr_month
        global curr_year
        global net

        try:

            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Iamankit@02",
                database="ebm"
            )
            cursor = db.cursor()

            sql_command = "INSERT INTO reading(dob, con_no, reading) VALUES(%s,%s,%s)"
            values = (d, consumer, current_reading)

            sql_command1 = "INSERT INTO bill(bill_date, tot_amt, con_no, current_reading, previous_reading, " \
                           "outstanding_amt, bill_month, year) VALUES(%s,%s,%s,%s,%s,%s, %s)"
            values1 = (d, total, consumer, current_reading, prev_reading, outstanding, curr_month, curr_year)



            sql_command2 = "INSERT INTO outstanding_amt(con_no, date_reading, out_amount, tot_amt, out_month)" \
                           "values(%s,%s,%s,%s,%s)"
            values2 = (consumer, d, net, total, curr_month)


            cursor.execute(sql_command, values)
            cursor.execute(sql_command1, values1)
            cursor.execute(sql_command2, values2)

            db.commit()




        except EXCEPTION as ee:

            messagebox.showerror("ERROR", "Unable to Save")
            print(ee)

    def open_search_bill(self):

        self.my_ntbk.select(7)

    def open_search_conbill(self):

        self.my_ntbk.select(8)

    def open_payment(self):

        self.my_ntbk.select(9)


    def search_billno(self):

        global root1


        bill_no = self.search_bill_no.get()

        if bill_no == "":

            messagebox.showerror("ERROR", "Invalid Entry")

        elif bill_no == " ":
            messagebox.showerror("ERROR", "Invalid Entry")


        else:

            bill_no = int(bill_no)

            try:

                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Iamankit@02",
                    database="ebm"
                )

                root1 = Tk()
                root1.title('BILL')

                root1.geometry("400x680")

                # Create A Main Frame
                main_frame = Frame(root1)
                main_frame.pack(fill=BOTH, expand=1)

                # Create A Canvas
                my_canvas = Canvas(main_frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

                # Add A Scrollbar To The Canvas
                my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # Configure The Canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

                # Create ANOTHER Frame INSIDE the Canvas
                second_frame = Frame(my_canvas)

                # Add that New frame To a Window In The Canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


                cursor = db.cursor()

                try:

                    cursor.execute(f'SELECT * from bill where BillNo={bill_no}')
                    search_result = cursor.fetchall()

                    for data in search_result:
                        bill_sdate = data[1]
                        tot_samt = data[2]
                        scon = int(data[3])
                        scurrent_reading = data[4]
                        sprev_reading = data[5]
                        sout_amt = data[6]
                        sbill_month = data[7]
                        sbill_year = data[8]
                        sdiff = data[9]
                        senergy_charge = data[10]


                except:

                    messagebox.showwarning("Warning", "No Data found")


                try:

                    cursor.execute(f'SELECT * from customer where ConsumerNo={scon}')
                    customer_result = cursor.fetchall()

                    for search_data in customer_result:


                        stariff = search_data[4]
                        sphone = search_data[7]
                        sdivision = search_data[5]
                        sadd = search_data[3]
                        sname = search_data[1]
                        smeterno = search_data[0]

                except:

                    messagebox.showwarning("Warning", "No Data found")



                try:

                    cursor.execute(f'SELECT * from tariff where T_id="{int(stariff)}"')
                    tariff_result = cursor.fetchall()

                    for i in tariff_result:
                        sfixd_charge = int(i[2])

                except:

                    messagebox.showwarning("Warning", "No Data found")




                bill_content = f' Electricity Department \n\n\n Bill \n\n\n\n\n' \
                               f'Division : {sdivision} \n\n Consumer No. : {scon} \n\n Name : {sname} \n\n ' \
                               f'Address : {sadd} \n\n Phone No. : {sphone}' \
                               f'\n\n\n --------Comercial Detaills-------- \n\n\n ' \
                               f'Tariff : {stariff} \n\n Load : 220V \n\n' \
                               f'--------Meter Details-------- \n\n\n' \
                               f'Meter No. : {smeterno} \n\n ' \
                               f'--------Billing Parameter-------- \n\n\n' \
                               f'Bill Issue Date : {bill_sdate} \n\n Bill Month : {sbill_month} ' \
                               f'\n\n Previous Reading : {sprev_reading} \n\n Current Reading : {scurrent_reading} \n\n ' \
                               f'Difference : {sdiff} \n\n ' \
                               f'--------Current Assessment--------\n\n\n' \
                               f'Energy Charge : {senergy_charge} \n\n Fixed Charge = {sfixd_charge} \n\n ' \
                               f'--------Net Demand-------- \n\n\n' \
                               f'Total Amount : {tot_samt} \n\n Outstanding Amt : {sout_amt} \n\n Net Payable: {tot_samt + sout_amt}'


                bill_label = Label(second_frame, text=bill_content, font=("Helvetica", 12, "bold"), justify=LEFT)
                bill_label.grid(row=0, columnspan=2, column=0)



                # try:
                #
                #     sql_command = "INSERT INTO reading(dob, con_no, reading) VALUES(%s,%s,%s)"
                #     values = (d, consumer, current_reading)
                #     cursor.execute(sql_command, values)
                #
                #     db.commit()
                #
                #
                # except EXCEPTION as ee:
                #
                #     messagebox.showerror("ERROR", "Unable to update reading")
                #     print(ee)



                root1.mainloop()

            except:

                messagebox.showerror("ERROR", "!!ERROR!!")


    def search_bill_con(self):

        global root1

        consu_no = self.bill_conentry.get()
        bill_mon = self.drop1.get()
        year = self.bill_yearentry.get()

        if consu_no == "":

            messagebox.showerror("ERROR", "Invalid Entry")

        elif consu_no == " ":
            messagebox.showerror("ERROR", "Invalid Entry")


        else:

            consu_no = int(consu_no)
            year = int(year)

            try:

                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Iamankit@02",
                    database="ebm"
                )

                root1 = Tk()
                root1.title('BILL')

                root1.geometry("400x680")

                # Create A Main Frame
                main_frame = Frame(root1)
                main_frame.pack(fill=BOTH, expand=1)

                # Create A Canvas
                my_canvas = Canvas(main_frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

                # Add A Scrollbar To The Canvas
                my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                # Configure The Canvas
                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

                # Create ANOTHER Frame INSIDE the Canvas
                second_frame = Frame(my_canvas)

                # Add that New frame To a Window In The Canvas
                my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

                cursor = db.cursor()

                try:

                    cursor.execute(f'SELECT * from bill where con_no={consu_no} AND bill_month="{bill_mon}" AND year={year}')
                    search_result = cursor.fetchall()

                    for data in search_result:
                        billnum = data[0]
                        bill_sdate = data[1]
                        tot_samt = data[2]
                        scurrent_reading = data[4]
                        sprev_reading = data[5]
                        sout_amt = data[6]
                        sbill_month = data[7]
                        sbill_year = data[8]
                        sdiff = data[9]
                        senergy_charge = data[10]


                except:

                    messagebox.showwarning("Warning", "No Data found")

                try:

                    cursor.execute(f'SELECT * from customer where ConsumerNo={consu_no}')
                    customer_result = cursor.fetchall()

                    for search_data in customer_result:
                        stariff = search_data[4]
                        sphone = search_data[7]
                        sdivision = search_data[5]
                        sadd = search_data[3]
                        sname = search_data[1]
                        smeterno = search_data[0]

                except:

                    messagebox.showwarning("Warning", "No Data found")

                try:

                    cursor.execute(f'SELECT * from tariff where T_id="{int(stariff)}"')
                    tariff_result = cursor.fetchall()

                    for i in tariff_result:
                        sfixd_charge = int(i[2])

                except:

                    messagebox.showwarning("Warning", "No Data found")

                bill_content = f' Electricity Department \n\n\n Bill \n\n\n\n\n' \
                               f'Division : {sdivision} \n\n Consumer No. : {consu_no} \n\n Name : {sname} \n\n ' \
                               f'Address : {sadd} \n\n Phone No. : {sphone}' \
                               f'\n\n\n --------Comercial Detaills-------- \n\n\n ' \
                               f'Tariff : {stariff} \n\n Load : 220V \n\n' \
                               f'--------Meter Details-------- \n\n\n' \
                               f'Meter No. : {smeterno} \n\n ' \
                               f'--------Billing Parameter-------- \n\n\n' \
                               f'Bill Issue Date : {bill_sdate} \n\n Bill Month : {sbill_month} ' \
                               f'\n\n Previous Reading : {sprev_reading} \n\n Current Reading : {scurrent_reading} \n\n ' \
                               f'Difference : {sdiff} \n\n ' \
                               f'--------Current Assessment--------\n\n\n' \
                               f'Energy Charge : {senergy_charge} \n\n Fixed Charge = {sfixd_charge} \n\n ' \
                               f'--------Net Demand-------- \n\n\n' \
                               f'Total Amount : {tot_samt} \n\n Outstanding Amt : {sout_amt} \n\n Net Payable: {tot_samt + sout_amt}'

                bill_label = Label(second_frame, text=bill_content, font=("Helvetica", 12, "bold"), justify=LEFT)
                bill_label.grid(row=0, columnspan=2, column=0)

                # try:
                #
                #     sql_command = "INSERT INTO reading(dob, con_no, reading) VALUES(%s,%s,%s)"
                #     values = (d, consumer, current_reading)
                #     cursor.execute(sql_command, values)
                #
                #     db.commit()
                #
                #
                # except EXCEPTION as ee:
                #
                #     messagebox.showerror("ERROR", "Unable to update reading")
                #     print(ee)

                root1.mainloop()

            except:

                messagebox.showerror("ERROR", "!!ERROR!!")






    def pay_and_save(self):

        consumer_no = self.paycon.get()
        amount = self.payamt.get()
        d = datetime.date.today()
        month = d.strftime("%B")

        if consumer_no == "":
            messagebox.showerror("ERROR", "Invalid Entry")

        elif consumer_no == " ":
            messagebox.showerror("ERROR", "Invalid Entry")

        elif amount == "":
            messagebox.showerror("ERROR", "Invalid Entry")

        elif amount == " ":
            messagebox.showerror("ERROR", "Invalid Entry")

        elif int(amount) == 0:
            messagebox.showwarning("Warning", "Cannot Be Zero")

        else:

            consumer_no = int(consumer_no)
            amount = int(amount)

            try:

                db = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Iamankit@02",
                    database="ebm"
                )
                cursor = db.cursor()

                cursor.execute(f'SELECT out_amount as last FROM outstanding_amt where con_no={consumer_no} ORDER BY date_reading DESC LIMIT 1')
                payresult = cursor.fetchall()

                for i in payresult:
                    outamt = i[0]

                out_push = outamt - amount

                sql_command = "INSERT INTO payment(payment_status, Amount, Con_no) Values(%s,%s,%s)"
                values = ("success", amount, consumer_no)

                sql_command2 = "INSERT INTO outstanding_amt(con_no, date_reading, out_amount, tot_amt, out_month)" \
                               "values(%s,%s,%s,%s,%s)"
                values2 = (consumer_no, d, out_push, amount, month)

                cursor.execute(sql_command, values)
                cursor.execute(sql_command2, values2)

                db.commit()

                webbrowser.open("https://rzp.io/l/uqQgiTS")
                self.my_ntbk.hide(9)


            except EXCEPTION as e:

                messagebox.showerror("ERROR", "Error")
                print(e)







# adminname = "ankit@ankit"
# x = AdminPageclass(adminname)
# x.AdminPage()
