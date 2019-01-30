from tkinter import *
from tkinter import messagebox
from Transpostion import *

class GUI:

    transpostion = Traspostion()

    def __init__(self, window):
        self.window = window
        window.geometry('900x450+200+50')
        window.title('Transposition')
        window.configure(bg='#FFBF00')
        window.overrideredirect(1)

        self.main_label = Label(text='Trasposition', fg='white', bg='#FFBF00',
                           font=("Times New Roman", 30, "bold"))
        self.main_label.pack(pady=30)
        self.plain_label = Label(text='Plain Text : ', fg='white', bg='#FFBF00', font=("Times New Roman", 18, "bold"))
        self.plain_label.place(x=50, y=130)
        self.key_label = Label(text='Key : ', fg='white', bg='#FFBF00', font=("Times New Roman", 18, "bold"))
        self.key_label.place(x=50, y=200)
        self.cipher_label = Label(text='cipher text : ', fg='white', bg='#FFBF00', font=("Times New Roman", 18, "bold"))
        self.cipher_label.place(x=50, y=270)

        self.plain = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.plain.place(x=200, y=130)
        self.key = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.key.place(x=200, y=200)
        self.cipher = Entry(window, width=65, fg='black', bd='8', font=("Times New Roman", 15, "bold"))
        self.cipher.place(x=200, y=270)

        self.encryption = Button(text='ENCRYPTION', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='green',
                            fg='white', bd=14, cursor='pirate', activebackground='red', activeforeground='black',
                            command=self.encryption_)
        self.encryption.place(x=300, y=350)

        self.decryption = Button(text='DECRYPTION', font=("Times New Roman", 14, "bold"), width=15, height=1, bg='red',
                            fg='white', bd=14, cursor='heart', activebackground='green', activeforeground='black',
                            command=self.decryprion_)
        self.decryption.place(x=550, y=350)

        self.close = Button(text='X', font=("Times New Roman", 14, "bold"), width=3, height=1, bg='red', fg='white',
                       cursor='pirate', activebackground='green', activeforeground='black', command=self.close_)
        self.close.place(x=860, y=0)



    def set_text(self, var, text):
        var.delete(0, END)
        var.insert(0, text)
        return



    def encryption_(self):
        m = self.plain.get()
        k = self.key.get()
        if len(m) == 0:
            messagebox.showwarning('Warning...', 'Plain text is empty !!!')
        elif len(k) == 0:
            messagebox.showwarning('Warning...', 'Key is empty !!!')
        else:
            c = self.transpostion.encryption(k, m)
            print(c)
            self.set_text(self.cipher, c)



    def decryprion_(self):
        c = self.cipher.get()
        k = self.key.get()
        if len(c) == 0:
            messagebox.showwarning('Warning...', 'Cipher text is empty !!!')
        elif len(k) == 0:
            messagebox.showwarning('Warning...', 'Key is empty !!!')
        else:
            m = self.transpostion.decryption(k, c)


            print(m)
            self.set_text(self.plain, m)



    def close_(self):
        self.window.destroy()


window = Tk()
gui = GUI(window)
window.mainloop()

