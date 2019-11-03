from tkinter import *
from tkinter import simpledialog
import sqlite3
import re

#for commit
root = Tk()
root.geometry("200x250")
root.title("Phonebook")
#root.config(bg="gray")
lbl = Label(root, text="Select menu, please:", font=("Arial Bold", 15))
lbl.grid(column=1, row=0)

def create():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(name STRING,'
                                                    'surname STRING,'
                                                    'phone STRING)');
    name=simpledialog.askstring("name", "Enter name")
    surname=simpledialog.askstring("surname", "Enter surname")
    phone=simpledialog.askstring("phone", "Enter phone number")
    data = [name, surname, phone]
    print(data)
    cursor.execute('INSERT INTO users VALUES (?, ?, ?)', data)
    conn.commit()
    cursor.close()
    conn.close()
def search():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    lookfor = simpledialog.askstring("lookfor", "Whom are you looking for? ")
    cursor.execute('SELECT * FROM users WHERE name like ?', ('%' + lookfor + '%',));
    row = cursor.fetchone()

    if row is None:
        cursor.execute('SELECT * FROM users WHERE surname like ?', ('%' + lookfor + '%',));
        row=cursor.fetchone()
        if row is None:
            cursor.execute('SELECT * FROM users WHERE phone like ?', ('%' + lookfor + '%',));
            row = cursor.fetchone()
            if row is None:
                found_cont = Tk()
                found_cont.title("Search results")
                lbl2 = Label(found_cont, text=("This contact is not exist"), font=("Arial Bold", 15))
                lbl2.pack()
            else:
                found_cont = Tk()
                found_cont.title("Search results")
                while row is not None:
                    lbl1 = Label(found_cont, text=())
                    lbl1.pack(anchor=W)
                    lbl2 = Label(found_cont, text=(row[0], row[1], row[2]), font=("Arial Bold", 15))
                    lbl2.pack(anchor=W)
                    found_name = str(row[0])
                    found_surname = str(row[1])
                    found_phone = str(row[2])

                    def edit_name():
                        conn = sqlite3.connect('phonebook.db')
                        cursor = conn.cursor()
                        new_name = simpledialog.askstring("new_name", "Enter new name")
                        cursor.execute('UPDATE users SET name = ? WHERE name = ?', (new_name, found_name,));
                        conn.commit()
                        cursor.close()
                        conn.close()

                    def edit_surname():
                        conn = sqlite3.connect('phonebook.db')
                        cursor = conn.cursor()
                        new_surname = simpledialog.askstring("new_surname", "Enter new surname")
                        cursor.execute('UPDATE users SET surname = ? WHERE surname = ?', (new_surname, found_surname,));
                        conn.commit()
                        cursor.close()
                        conn.close()

                    def edit_phone():
                        conn = sqlite3.connect('phonebook.db')
                        cursor = conn.cursor()
                        new_phone = simpledialog.askstring("new_phone", "Enter new phone number")
                        cursor.execute('UPDATE users SET phone = ? WHERE phone = ?', (new_phone, found_phone,));
                        conn.commit()
                        cursor.close()
                        conn.close()

                    def delete_contact():
                        confirm = simpledialog.askstring("confirm", "Do you want to delete this contact? (Y/N) ")
                        if confirm == "Y":
                            conn = sqlite3.connect('phonebook.db')
                            cursor = conn.cursor()
                            cursor.execute('DELETE FROM users WHERE name = ?', (found_name,));
                            conn.commit()
                            cursor.close()
                            conn.close()

                    row = cursor.fetchone()

                    btn1 = Button(found_cont, text="Edit name", font=("Arial", 10), width=15, height=1, bg="lightgray",
                                  command=edit_name)
                    btn2 = Button(found_cont, text="Edit surname", font=("Arial", 10), width=15, height=1, bg="lightgray",
                                  command=edit_surname)
                    btn3 = Button(found_cont, text="Edit phone number", font=("Arial", 10), width=15, height=1, bg="lightgray",
                                  command=edit_phone)
                    btn4 = Button(found_cont, text="Delete contact", font=("Arial", 10), width=15, bg='lightcoral',
                                  command=delete_contact)
                    btn1.pack(anchor=E)
                    btn2.pack(anchor=E)
                    btn3.pack(anchor=E)
                    btn4.pack(anchor=E)


        else:
            found_cont = Tk()
            #found_cont.geometry("300x300")
            found_cont.title("Search results")
            while row is not None:
                lbl1 = Label(found_cont, text=())
                lbl1.pack(anchor=W)
                lbl2 = Label(found_cont, text=(row[0], row[1], row[2]), font=("Arial Bold", 15))
                lbl2.pack(anchor=W)
                found_name = str(row[0])
                found_surname = str(row[1])
                found_phone = str(row[2])

                def edit_name():
                    conn = sqlite3.connect('phonebook.db')
                    cursor = conn.cursor()
                    new_name = simpledialog.askstring("new_name", "Enter new name")
                    cursor.execute('UPDATE users SET name = ? WHERE name = ?', (new_name, found_name,));
                    conn.commit()
                    cursor.close()
                    conn.close()

                def edit_surname():
                    conn = sqlite3.connect('phonebook.db')
                    cursor = conn.cursor()
                    new_surname = simpledialog.askstring("new_surname", "Enter new surname")
                    cursor.execute('UPDATE users SET surname = ? WHERE surname = ?', (new_surname, found_surname,));
                    conn.commit()
                    cursor.close()
                    conn.close()

                def edit_phone():
                    conn = sqlite3.connect('phonebook.db')
                    cursor = conn.cursor()
                    new_phone = simpledialog.askstring("new_phone", "Enter new phone number")
                    cursor.execute('UPDATE users SET phone = ? WHERE phone = ?', (new_phone, found_phone,));
                    conn.commit()
                    cursor.close()
                    conn.close()

                def delete_contact():
                    confirm = simpledialog.askstring("confirm", "Do you want to delete this contact? (Y/N) ")
                    if confirm == "Y":
                        conn = sqlite3.connect('phonebook.db')
                        cursor = conn.cursor()
                        cursor.execute('DELETE FROM users WHERE name = ?', (found_name,));
                        conn.commit()
                        cursor.close()
                        conn.close()

                row = cursor.fetchone()

                btn1 = Button(found_cont, text="Edit name", font=("Arial", 10), width=15, height=1, bg="lightgray", command=edit_name)
                btn2 = Button(found_cont, text="Edit surname", font=("Arial", 10), width=15, height=1, bg="lightgray",
                              command=edit_surname)
                btn3 = Button(found_cont, text="Edit phone number", font=("Arial", 10), width=15, height=1, bg="lightgray",
                              command=edit_phone)
                btn4 = Button(found_cont, text="Delete contact", font=("Arial", 10), width=15, bg='lightcoral',
                              command=delete_contact)
                btn1.pack(anchor=E)
                btn2.pack(anchor=E)
                btn3.pack(anchor=E)
                btn4.pack(anchor=E)
    else:
        found_cont = Tk()
        found_cont.title("Search results")
        while row is not None:
            lbl1 = Label(found_cont, text=())
            lbl1.pack(anchor=W)
            lbl2 = Label(found_cont, text=(row[0], row[1], row[2]), font=("Arial Bold", 15))
            lbl2.pack(anchor=W)
            found_name = str(row[0])
            found_surname = str(row[1])
            found_phone = str(row[2])

            def edit_name():
                conn = sqlite3.connect('phonebook.db')
                cursor = conn.cursor()
                new_name = simpledialog.askstring("new_name", "Enter new name")
                cursor.execute('UPDATE users SET name = ? WHERE name = ?', (new_name, found_name,));
                conn.commit()
                cursor.close()
                conn.close()

            def edit_surname():
                conn = sqlite3.connect('phonebook.db')
                cursor = conn.cursor()
                new_surname = simpledialog.askstring("new_surname", "Enter new surname")
                cursor.execute('UPDATE users SET surname = ? WHERE surname = ?', (new_surname, found_surname,));
                conn.commit()
                cursor.close()
                conn.close()

            def edit_phone():
                conn = sqlite3.connect('phonebook.db')
                cursor = conn.cursor()
                new_phone = simpledialog.askstring("new_phone", "Enter new phone number")
                cursor.execute('UPDATE users SET phone = ? WHERE phone = ?', (new_phone, found_phone,));
                conn.commit()
                cursor.close()
                conn.close()

            def delete_contact():
                confirm = simpledialog.askstring("confirm", "Do you want to delete this contact? (Y/N) ")
                if confirm == "Y":
                    conn = sqlite3.connect('phonebook.db')
                    cursor = conn.cursor()
                    cursor.execute('DELETE FROM users WHERE name = ?', (found_name,));
                    conn.commit()
                    cursor.close()
                    conn.close()

            row = cursor.fetchone()

            btn1 = Button(found_cont, text="Edit name", font=("Arial", 12), width=15, height=1, bg="lightgray", command=edit_name)
            btn2 = Button(found_cont, text="Edit surname", font=("Arial", 12), width=15, height=1, bg="lightgray",  command=edit_surname)
            btn3 = Button(found_cont, text="Edit phone number", font=("Arial", 12), width=15, height=1, bg="lightgray", command=edit_phone)
            btn4 = Button(found_cont, text="Delete contact", font=("Arial", 12), width=15, bg='lightcoral', command=delete_contact)
            btn1.pack(anchor=E)
            btn2.pack(anchor=E)
            btn3.pack(anchor=E)
            btn4.pack(anchor=E)
    cursor.close()
    conn.close()


def edit():
    pass
def delete():
    pass

def menu():
    btn1 = Button(root, text="Create contact", font=("Arial", 15), width=15, height=1, bg="lightgray", command=create)
    btn2 = Button(root, text="Search contact", font=("Arial", 15), width=15, height=1, bg="lightgray", command=search)
    btn3 = Button(root, text="Edit contact", font=("Arial", 15), width=15, height=1, bg="lightgray",  command=edit)
    btn4 = Button(root, text="Delete contact", font=("Arial", 15), width=15, height=1, bg="lightgray", command=delete)
    btn5 = Button(root, text="Exit", font=("Arial", 15), width=15, height=1, bg="lightgray", command=exit)
    btn1.grid(column=1, row=1)
    btn2.grid(column=1, row=2)
    btn3.grid(column=1, row=3)
    btn4.grid(column=1, row=4)
    btn5.grid(column=1, row=5)
    root.mainloop()
menu()


