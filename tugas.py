import tkinter as tk
from tkinter import ttk, messagebox

def goLogin(usernameVal, passwordVal):
    try:
        username = usernameVal.get()
        password = int(passwordVal.get())
        if username.isdigit():
            messagebox.showerror("Login", "Username tidak boleh angka")     
        if username == "admin" and password == 12345678:
            messagebox.showinfo("Login", "Login Berhasil")
        else:
            messagebox.showerror("Login", "Login Gagal")
    except ValueError:
        messagebox.showerror("Login", "Password harus berupa angka")

root = tk.Tk()
root.title("Login Form")
root.geometry("400x260")
# input layot
inputFrame = ttk.LabelFrame(root, text="Selamat Datang")
inputFrame.pack(padx=10, pady=10, fill="x")

usernameVal = tk.StringVar()
passwordVal = tk.StringVar()
# usernameinput
ttk.Label(inputFrame, text="Username :").grid(row=0, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(inputFrame, textvariable=usernameVal, width=60).grid(row=1, column=0, padx=5, pady=5, sticky="w")
# password input
ttk.Label(inputFrame, text="Password :").grid(row=2, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(inputFrame, textvariable=passwordVal, width=60).grid(row=3, column=0, padx=5, pady=5, sticky="w")
#btn Login
ttk.Button(inputFrame, text="Login", command= lambda: goLogin(usernameVal, passwordVal)).grid(row=4, column=0, padx=10,pady=25, sticky="nsew")

root.mainloop()