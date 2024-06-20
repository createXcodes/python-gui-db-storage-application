

import tkinter as tk
from tkinter import *

import mysql.connector    
code_root = Tk()
code_root.geometry("881x350")
code_root.title(" BAKERY DATA GENRATOR")

icon = PhotoImage(file="bakery.png")
code_root.iconphoto(False,icon)

#background = PhotoImage( file="bg.png",master=code_root)
#background_Label = Label(code_root , image=background )

#ackground_Label.place(x=0 , y=0) 

connection = mysql.connector.connect(host='localhost', user='root', password='',
                                     port='3306', database='datapy')
c = connection.cursor()



bkg = "#A0C5FA"



frame = tk.Frame(code_root, bg=bkg )

label_ordernumber = tk.Label(frame, text="Order Number: ", font=('verdana',31), bg=bkg )

entry_ordernumber = tk.Entry(frame, font=('verdana', 31) )

label_personname = tk.Label(frame, text="Person Name :", font=('verdana',31), bg=bkg)
entry_personname = tk.Entry(frame, font=('verdana',31))

label_ordeditems = tk.Label(frame, text="Orded Item : ", font=('verdana',31), bg=bkg)
entry_ordeditems = tk.Entry(frame, font=('verdana',31))

label_price = tk.Label(frame, text="Price : ", font=('verdana',31), bg=bkg)
entry_price = tk.Entry(frame, font=('verdana',31))



def insertData():
    ordernumber = entry_ordernumber.get()
    personname = entry_personname.get()
    ordeditems = entry_ordeditems.get()
    price = entry_price.get()

    insert_query = "INSERT INTO `bakery`(`ordernumber`, `personname`, `ordeditems`, `price`)  VALUES (%s,%s,%s,%s)"
    vals = (ordernumber,personname,ordeditems,price)
    c.execute(insert_query,vals)
    connection.commit()


button_insert = tk.Button(frame, text="Submit", font=('verdana',14), bg='orange',
                          command = insertData)





label_ordernumber.grid(row=0, column=0)
entry_ordernumber.grid(row=0, column=1, pady=10, padx=10)

label_personname.grid(row=1, column=0)
entry_personname.grid(row=1, column=1, pady=10, padx=10)

label_ordeditems.grid(row=2, column=0, sticky='e')
entry_ordeditems.grid(row=2, column=1, pady=10, padx=10)

label_price.grid(row=3, column=0, sticky='e')
entry_price.grid(row=3, column=1, pady=10, padx=10)

button_insert.grid(row=4,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

frame.grid(row=0, column=0)


code_root.mainloop()