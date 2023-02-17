import sqlite3
from tkinter import *
from tkinter import messagebox
pm = Tk()
pm.title("PMS")


def user():
    global frame1
    global label1

    def pick(value):
        issue_entry.insert(END, value)

    def book():
        global fc
        global cursor_1
        heal = issue_entry.get()
        name = f_name_entry.get()
        if heal == "Family medicine":

            fc = sqlite3.connect("PMS.db")
            cursor_1 = fc.cursor()
            cursor_1.execute("SELECT *, oid FROM Doctors WHERE (Department = 'Family medicine' AND Patients < 10)")
            records = cursor_1.fetchone()
            increment_value = records[2]
            cursor_1.execute("UPDATE Doctors SET Patients = ? WHERE Name = ?",
                             (increment_value + 1, records[0]))
            messagebox.showinfo("Booked", f"{name} is appointed to {records[0]} and your number is {increment_value}")

            cursor_1.execute("INSERT INTO Patients VALUES (:First_Name, :Last_Name, :Dep_Visited, :Doctor, :Number)",
                             {
                                 'First_Name': name,
                                 'Last_Name': l_name_entry.get(),
                                 'Dep_Visited': issue_entry.get(),
                                 'Doctor': records[0],
                                 'Number': increment_value
                             }
                             )
            fc.commit()
            fc.close()
            f_name_entry.delete(0, END)
            l_name_entry.delete(0, END)
            issue_entry.delete(0, END)

        elif heal == "Dentistry":

            fc = sqlite3.connect("PMS.db")
            cursor_1 = fc.cursor()
            cursor_1.execute("SELECT *, oid FROM Doctors WHERE (Department = 'Dentistry' AND Patients < 10)")
            records = cursor_1.fetchone()
            increment_value = records[2]
            cursor_1.execute("UPDATE Doctors SET Patients = ? WHERE Name = ?",
                             (increment_value + 1, records[0]))
            messagebox.showinfo("Booked", f"{name} appointed to {records[0]} and your number is {increment_value}")
            cursor_1.execute("INSERT INTO Patients VALUES (:First_Name, :Last_Name, :Dep_Visited, :Doctor, :Number)",
                             {
                                 'First_Name': name,
                                 'Last_Name': l_name_entry.get(),
                                 'Dep_Visited': issue_entry.get(),
                                 'Doctor': records[0],
                                 'Number': increment_value
                             }
                             )
            fc.commit()
            fc.close()
            f_name_entry.delete(0, END)
            l_name_entry.delete(0, END)
            issue_entry.delete(0, END)

        elif heal == "Cardio":

            fc = sqlite3.connect("PMS.db")
            cursor_1 = fc.cursor()
            cursor_1.execute("SELECT *, oid FROM Doctors WHERE (Department = 'Cardio' AND Patients < 10)")
            records = cursor_1.fetchone()
            increment_value = records[2]
            cursor_1.execute("UPDATE Doctors SET Patients = ? WHERE Name = ?",
                             (increment_value + 1, records[0]))
            messagebox.showinfo("Booked", f"{name} appointed to {records[0]} and your number is {increment_value}")
            cursor_1.execute("INSERT INTO Patients VALUES (:First_Name, :Last_Name, :Dep_Visited, :Doctor, :Number)",
                             {
                                 'First_Name': name,
                                 'Last_Name': l_name_entry.get(),
                                 'Dep_Visited': issue_entry.get(),
                                 'Doctor': records[0],
                                 'Number': increment_value
                             }
                             )
            fc.commit()
            fc.close()
            f_name_entry.delete(0, END)
            l_name_entry.delete(0, END)
            issue_entry.delete(0, END)

        elif heal == "Ophthalmology":

            fc = sqlite3.connect("PMS.db")
            cursor_1 = fc.cursor()
            cursor_1.execute("SELECT *, oid FROM Doctors WHERE (Department = 'Ophthalmology' AND Patients < 10)")
            records = cursor_1.fetchone()
            increment_value = records[2]
            cursor_1.execute("UPDATE Doctors SET Patients = ? WHERE Name = ?",
                             (increment_value + 1, records[0]))
            messagebox.showinfo("Booked", f"{name} appointed to {records[0]} and your number is {increment_value}")
            cursor_1.execute("INSERT INTO Patients VALUES (:First_Name, :Last_Name, :Dep_Visited, :Doctor, :Number)",
                             {
                                 'First_Name': name,
                                 'Last_Name': l_name_entry.get(),
                                 'Dep_Visited': issue_entry.get(),
                                 'Doctor': records[0],
                                 'Number': increment_value
                             }
                             )
            fc.commit()
            fc.close()
            f_name_entry.delete(0, END)
            l_name_entry.delete(0, END)
            issue_entry.delete(0, END)

        elif heal == "ENT":

            fc = sqlite3.connect("PMS.db")
            cursor_1 = fc.cursor()
            cursor_1.execute("SELECT *, oid FROM Doctors WHERE (Department = 'ENT' AND Patients < 10)")
            records = cursor_1.fetchone()
            increment_value = records[2]
            cursor_1.execute("UPDATE Doctors SET Patients = ? WHERE Name = ?",
                             (increment_value + 1, records[0]))
            messagebox.showinfo("Booked", f"{name} appointed to {records[0]} and your number is {increment_value}")
            cursor_1.execute("INSERT INTO Patients VALUES (:First_Name, :Last_Name, :Dep_Visited, :Doctor, :Number)",
                             {
                                 'First_Name': name,
                                 'Last_Name': l_name_entry.get(),
                                 'Dep_Visited': issue_entry.get(),
                                 'Doctor': records[0],
                                 'Number': increment_value
                             }
                             )
            fc.commit()
            fc.close()
            f_name_entry.delete(0, END)
            l_name_entry.delete(0, END)
            issue_entry.delete(0, END)

    # New window
    users = Toplevel()

    #  Frame 1
    frame1 = LabelFrame(users, padx=5, pady=5)
    frame1.pack(padx=10, pady=10)

    label1 = Label(frame1, text="PHARMACY MANAGEMENT SYSTEM", font=("Cambria", 20))
    label1.pack()

    # Frame 3
    frame3 = LabelFrame(users, padx=5, pady=5)
    frame3.pack(padx=10, pady=10)

    f_name_label = Label(frame3, text=" First Name:", font=("Cambria", 15))
    f_name_label.grid(row=0, column=0, padx=10)

    f_name_entry = Entry(frame3, width=30)
    f_name_entry.grid(row=0, column=1)

    l_name_label = Label(frame3, text=" Last Name:", font=("Cambria", 15))
    l_name_label.grid(row=1, column=0, padx=10)

    l_name_entry = Entry(frame3, width=30)
    l_name_entry.grid(row=1, column=1)

    issue_label = Label(frame3, text="Our services:", font=("Cambria", 15))
    issue_label.grid(row=2, column=0)

    button3 = Button(frame3, text="Family medicine", font=("Cambria", 10), width=25,
                     command=lambda: pick("Family medicine"))
    button3.grid(row=2, column=1)

    button3 = Button(frame3, text="Dentistry", font=("Cambria", 10), width=25,
                     command=lambda: pick("Dentistry"))
    button3.grid(row=3, column=1)

    button3 = Button(frame3, text="Cardio", font=("Cambria", 10), width=25,
                     command=lambda: pick("Cardio"))
    button3.grid(row=4, column=1)

    button3 = Button(frame3, text="Ophthalmology", font=("Cambria", 10), width=25,
                     command=lambda: pick("Ophthalmology"))
    button3.grid(row=5, column=1)

    button3 = Button(frame3, text="ENT", font=("Cambria", 10), width=25,
                     command=lambda: pick("ENT"))
    button3.grid(row=6, column=1)

    issue_entry = Entry(frame3, width=30)
    issue_entry.grid(row=7, column=1, columnspan=2, pady=10)

    button_1 = Button(frame3, text="Book", font=("Cambria", 12), pady=5, command=book)
    button_1.grid(row=8, column=1, columnspan=2)

    users.mainloop()


def login():
    used = Toplevel()
    global frame1
    global label1
    frame1 = LabelFrame(used, padx=5, pady=5)
    frame1.pack(padx=10, pady=10)

    label1 = Label(frame1, text="PHARMACY MANAGEMENT SYSTEM", font=("Cambria", 20))
    label1.pack()

    # frame 4
    def signin():
        global fc
        global cursor_1

        name_1 = username_e.get()
        password = password_e.get()

        fc = sqlite3.connect("PMS.db")
        cursor_1 = fc.cursor()

        cursor_1.execute("SELECT *, oid FROM login_d WHERE (username = ? AND password = ?)",
                         (name_1, password))
        sign = cursor_1.fetchone()
        try:
            if name_1 == sign[0] and password == sign[1]:
                cursor_1.execute(f"SELECT *, oid FROM Doctors WHERE (Name ='{name_1}' AND Patients < 11)")
                sign_1 = cursor_1.fetchone()
                label2 = Label(frame4, text=f"Welcome {name_1}, You have {sign_1[2]} patients", font=("Cambria", 12))
                label2.grid(row=3, column=1)
                try:
                    if sign_1[2] > 0:
                        button3 = Button(frame4, text="See", font=("Cambria", 12), pady=5, command=see)
                        button3.grid(row=4, column=1)
                except EXCEPTION as e:
                    messagebox.showerror("You have no patient")

        except TypeError:
            messagebox.showerror("Error", "Username or Password Incorrect")

        fc.commit()
        fc.close()

    frame4 = LabelFrame(used, padx=5, pady=5)
    frame4.pack(padx=10, pady=10)

    username_l = Label(frame4, text="Username:", font=("Cambria", 15))
    username_l.grid(row=0, column=0, padx=10)

    username_e = Entry(frame4, width=30)
    username_e.grid(row=0, column=1)

    password_l = Label(frame4, text=" Password:", font=("Cambria", 15))
    password_l.grid(row=1, column=0, padx=10)

    password_e = Entry(frame4, width=30, show='\u2022')
    password_e.grid(row=1, column=1)

    button_1 = Button(frame4, text="Login", font=("Cambria", 12), pady=5, command=signin)
    button_1.grid(row=2, column=1, columnspan=2)

    # frame 5
    def see():
        global fc
        global cursor_1
        fc = sqlite3.connect("PMS.db")
        cursor_1 = fc.cursor()
        name_1 = username_e.get()

        cursor_1.execute(f"SELECT *, oid FROM Patients WHERE Doctor ='{name_1}'")
        sign_1 = cursor_1.fetchone()

        label = Label(frame5, text=sign_1, font=("Cambria", 12))
        label.grid(row=0, column=0)

        button4 = Button(frame5, text="Checkout", font=("Cambria", 12), pady=5, command=checkout)
        button4.grid(row=1, column=1)

        fc.commit()
        fc.close()

    def checkout():
        global fc
        global cursor_1
        fc = sqlite3.connect("PMS.db")
        cursor_1 = fc.cursor()
        name_1 = username_e.get()
        name_2 = entry.get()

        cursor_1.execute(f"DELETE FROM Patients WHERE (First_Name = '{name_2}' AND Doctor = '{name_1}')")
        cursor_1.execute(f"SELECT *, oid FROM Doctors WHERE Name = '{name_1}'")
        records = cursor_1.fetchone()
        increment_value = records[2]
        cursor_1.execute("UPDATE Doctors SET Patients = ? WHERE Name = ?",
                         (increment_value - 1, records[0]))
        entry.delete(0, END)
        messagebox.showinfo("Checked", f"Patient {name_2} checked out")

        fc.commit()
        fc.close()

    frame5 = LabelFrame(used, padx=5, pady=5)
    frame5.pack(padx=10, pady=5)

    entry = Entry(frame5, width=20)
    entry.grid(row=1, column=0)


fc = sqlite3.connect("PMS.db")
cursor_1 = fc.cursor()
# cursor_1.execute("""CREATE TABLE login_d(
#                  username text,
#                  password text
#                  )""")
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Kingsley", "kingdrcardsley165"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Igo", "idrophgo398"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Zim", "zidrfmadm555"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Micheal", "micdreneat768"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Nino", "nidrdennotistry908"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Serbir", "serdrentbir321"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Ella", "eldrophla228"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Chimere", "chidrfmadmer789e"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Buchi", "buchdrcardi378"))
# cursor_1.execute("INSERT INTO login_d(username, password)VALUES(?, ?)",
#                  ("Oma", "odrden430ma"))
# cursor_1.execute("""CREATE TABLE Patients(
#                  First_Name text,
#                  Last_Name text,
#                  Dep_Visited text,
#                  Doctor text,
#                  Number integer)""")
# cursor_1.execute("""CREATE TABLE Doctors(
#                  Name text,
#                  Department text,
#                  Patients integer)""")
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Kingsley", "Family medicine", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Igo", "Family medicine", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Zim", "Dentistry", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Micheal", "Dentistry", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Nino", "Cardio", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Serbir", "Cardio", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Ella", "Ophthalmology", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Chimere", "Ophthalmology", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Buchi", "ENT", 0))
# cursor_1.execute("INSERT INTO Doctors(Name, Department, Patients)VALUES(?, ?, ?)",
#                  ("Dr Oma", "ENT", 0))

fc.commit()
fc.close()

frame1 = LabelFrame(pm, padx=5, pady=5)
frame1.pack(padx=10, pady=10)

label1 = Label(frame1, text="PHARMACY MANAGEMENT SYSTEM", font=("Cambria", 20))
label1.pack()

frame2 = LabelFrame(pm, padx=5, pady=5)
frame2.pack(padx=30, pady=30)

button1 = Button(frame2, text="Patient", font=("Cambria", 10), command=user)
button1.grid(row=1, column=1)

button2 = Button(frame2, text="Doctor", font=("Cambria", 10), command=login)
button2.grid(row=1, column=2)

mainloop()
