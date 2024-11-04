import tkinter as tk
from tkinter import ttk

class Graphics(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = AccountOverview(container, self)
        self.frames[AccountOverview] = frame
        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(AccountOverview)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class AccountOverview(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Account Overview:", anchor='n', font='Arial 12 bold')
        label.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        description = tk.Label(self, text="Click on account to see\nindividual actions", anchor='n')
        description.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        transactionButton = tk.Button(self, text="Transaction History", anchor='n')
        transactionButton.grid(row=3, column=0, padx=5)

        quitButton = tk.Button(self, text="Quit", anchor='n')
        quitButton.grid(row=4, column=0, padx=5)

        treeview = ttk.Treeview(self, columns=("Account Name", "Balance"), show="headings")
        treeview.heading("Account Name", text="Account Name")
        treeview.heading("Balance", text="Balance")
        treeview.grid(row=0, column=1, sticky='nsew', padx=5, pady=5, rowspan=6)