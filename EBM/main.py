# from tkinter import *
# from PIL import Image, ImageTk
# from addcus import *
#
# def mainpage():
#
#     window = Tk()
#
#     # window.iconphoto(True, PhotoImage(file='C:\\Users\\dell\\PycharmProjects\\EBG\\Icons\\icon-title.png'))
#     window.title("EBG(Electricity Bill Generator)")
#
#     window.geometry('840x600')
#     label_img = Image.open('C:\\Users\\dell\\PycharmProjects\\EBG\\Icons\\label_image.png')
#     label_img = label_img.resize((840, 600), Image.ANTIALIAS)
#     label_img = ImageTk.PhotoImage(label_img)
#
#     option_img = Image.open("C:\\Users\\dell\\PycharmProjects\\EBG\\Icons\\options.png")
#     option_img = option_img.resize((50, 50), Image.ANTIALIAS)
#     option_img = ImageTk.PhotoImage(option_img)
#
#     add_cus = Add_customer()
#
#
#     def add_customer_fun():
#
#         add_cus.Details()
#
#
#     # Main Label
#     main_label = Label(window, image=label_img)
#     main_label.place(x=0, y=0, relwidth=1, relheight=1)
#
#     # Text Label
#     label_1 = Label(window,
#                     text="Electricity Bill Generator",
#                     padx=150,
#                     pady=20,
#                     font=('Garamond', 40, "bold"),
#                     bg="black",
#                     fg="Blue")
#
#     label_1.grid(row=0, column=0, columnspan=2)
#
#     # Creating Buttons
#
#     button_Generate_bill = Button(window,
#                                   text="GENERATE BILL",
#                                   fg="blue",
#                                   bg="#2a282b",
#                                   padx=20, pady=10,
#                                   font=("Arial Black", 17, "bold"))
#
#     button_Generate_bill.place(x=300, y=150)
#
#
#     button_add_customer = Button(window,
#                                  text="ADD CUSTOMER",
#                                  fg="blue",
#                                  bg="#2a282b",
#                                  padx=20, pady=10,
#                                  font=("Arial Black", 17, "bold"),
#                                  command=add_customer_fun)
#
#     button_add_customer.place(x=80, y=300)
#
#
#     button_View_record = Button(window,
#                                 text="VIEW RECORD",
#                                 fg="blue",
#                                 bg="#2a282b",
#                                 padx=32, pady=10,
#                                 font=("Arial Black", 17, "bold"))
#
#     button_View_record.place(x=80, y=450)
#
#
#     button_Report = Button(window,
#                            text="REPORT",
#                            fg="blue",
#                            bg="#2a282b",
#                            padx=60, pady=10,
#                            font=("Arial Black", 17, "bold"))
#
#     button_Report.place(x=500, y=300)
#
#
#     button_Delete = Button(window,
#                            text="DELETE",
#                            fg="blue",
#                            bg="#2a282b",
#                            padx=64, pady=10,
#                            font=("Arial Black", 17, "bold"))
#
#     button_Delete.place(x=500, y=450)
#
#
#     window.mainloop()
#
#
# mainpage()


import datetime
import time


d = datetime.datetime.now()
n = d.strftime("%X")
print(type(d))
print(n)
print(type(n))