import tkinter as tk
from tkinter import messagebox

def displayData():
    firstName= entFirst.get()
    lastName = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()
    message = "Welcome to tkinter, " + entFirst.get() + "\nYou entered: \nName:" + firstName + lastName + "\nEmail:" + email + "\nPhone:" + phone
    messagebox.showinfo("Submision", message)
    return None

def clearData():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)
    return None

root = tk.Tk()
root.title("tkinter From")
root.minsize(500,300)

lblFrPerson = tk.LabelFrame(root, text="Personal Information")
lblFrPerson.pack()

lblFirst = tk.Label(lblFrPerson, text="*First Name:", bg="blue", fg="white")
lblFirst.grid(row=0, column=0)

entFirst = tk.Entry(lblFrPerson)
entFirst.grid(row=0, column=1)

lblLast =tk.Label(lblFrPerson, text="*Last Name:", bg="blue", fg="white")
lblLast.grid(row=1, column=0)

entLast = tk.Entry(lblFrPerson)
entLast.grid(row=1, column=1)

lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(row=2, column=0)

entEmail = tk.Entry(lblFrPerson)
entEmail.grid(row=2, column=1)

lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(row=3, column=0)

entPhone = tk.Entry(lblFrPerson)
entPhone.grid(row=3, column=1)

fraButtons = tk.Frame(root)
fraButtons.pack()

quitButton = tk.Button(root, text="Quit", width=5, command=root.destroy)
quitButton.pack(side= tk.LEFT)

displayButton = tk.Button(root, text="Submit", width=5, command=displayData)
displayButton.pack(side=tk.LEFT)

clearButton = tk.Button(root, text="Clear", width = 5, command=clearData)
clearButton.pack(side=tk.LEFT)

root.mainloop()