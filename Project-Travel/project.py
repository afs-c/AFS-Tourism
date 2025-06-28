import tkinter as tk

class tourGUI:

    def __init__(self):

        
        
        root = tk.Tk()
        root.title('AFS Tourism Application')
        root.geometry('1200x785')
        root.configure(bg="#3F3F3F")

        self.frame1 = tk.Frame(root)
        self.frame1.configure(bg='#3F3F3F')
        self.frame1.pack()

        self.frame2 = tk.Frame(root)
        self.frame2.configure(bg='#3F3F3F')
        self.frame2.pack_forget()

        self.frame3 = tk.Frame(root)
        self.frame3.configure(bg='#3F3F3F')
        self.frame3.pack_forget()

        self.frame4 = tk.Frame(root)
        self.frame4.configure(bg='#3F3F3F')
        self.frame4.pack_forget()

        self.frame5 = tk.Frame(root)
        self.frame5.configure(bg='#3F3F3F')
        self.frame5.pack_forget()

        self.frame6 = tk.Frame(root)
        self.frame6.configure(bg='#3F3F3F')
        self.frame6.pack_forget()

        self.frame7 = tk.Frame(root)
        self.frame7.configure(bg='#3F3F3F')
        self.frame7.pack_forget()

        self.frame8 = tk.Frame(root)
        self.frame8.configure(bg='#3F3F3F')
        self.frame8.pack_forget()

        self.frame9 = tk.Frame(root)
        self.frame9.configure(bg='#3F3F3F')
        self.frame9.pack_forget()

        root.mainloop()

tourGUI()
