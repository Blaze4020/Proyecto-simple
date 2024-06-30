import tkinter as tk
from PIL import Image, ImageTk
import os

def iniciar_sesion():
    os.system('python inicios.py')

def registrarse_aqui():
    os.system('python registreseaqui.py')

def abrir_planilla():
    os.system('start excel planilla.xlsx')

root = tk.Tk()
root.title("Asistencia de Docentes")
root.geometry("800x600")

bg_image = Image.open("Setup/m.png")
bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

btn_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion, width=15, height=2)
btn_iniciar_sesion.pack(pady=50)

btn_registrarse_aqui = tk.Button(root, text="Regístrese Aquí", command=registrarse_aqui, width=15, height=2)
btn_registrarse_aqui.pack(pady=20)

lbl_mensaje = tk.Label(root, text="¿No estás registrado? Regístrate ahora ya")
lbl_mensaje.pack(pady=10)

btn_planilla = tk.Button(root, text="Planilla", command=abrir_planilla, width=10, height=2)
btn_planilla.place(relx=0.85, rely=0.85)

root.mainloop()
