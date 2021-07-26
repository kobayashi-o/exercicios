#O design da janela ficou bem feio. Fiz esse projeto para praticar.
from tkinter import *

def Button_Click(): #Definindo o que vai acontecer quando o botão for ativado
    print('Login: ' + login_entry.get())
    print('Senha: ' + password_entry.get())
    print('Lembre-se de mim foi pressionado?', checkbox_var.get())

root = Tk()
checkbox_var = BooleanVar()

#Propriedades da janela
root.title('Login')
root.geometry('350x150')
root.resizable(False, False)

#Conteúdo da janela

#Definindo as textbox
login_entry = Entry(root)
password_entry = Entry(root)
login_entry.place(x=130, y=50)
password_entry.place(x=130, y=80)

#Definindo os Labels que ficam ao lado das textbox
login_label = Label(root, text='Login:')
password_label = Label(root,  text='Senha:')
login_label.place(x=85, y=50)
password_label.place(x=80, y=80)

#Definindo o botão "Fazer login"
login_button = Button(root, text='Fazer login.', padx=5, command=Button_Click)
login_button.place(x=250, y=110)

#Definindo a checkbutton "lembre-se de mim."
rememberme_cb = Checkbutton(root, text='Lembre-se de mim.', variable=checkbox_var)
rememberme_cb.place(x=90, y=115)

root.mainloop()
