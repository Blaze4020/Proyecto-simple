import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import pandas as pd
import datetime

def reconocimiento_facial():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_color = frame[y:y+h, x:x+w]
            if cv2.waitKey(1) & 0xFF == ord(' '):
                nombre = entry_nombre.get()
                if nombre:
                    filename = f"{nombre}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                    cv2.imwrite(f"imagenes/{filename}", roi_color)
                    data = pd.read_excel("usuarios.xlsx")
                    new_data = {
                        "Nombre": nombre,
                        "CI": entry_ci.get(),
                        "Curso": entry_curso.get(),
                        "Actividad": entry_actividad.get(),
                        "Fecha y Hora": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    data = data.append(new_data, ignore_index=True)
                    data.to_excel("usuarios.xlsx", index=False)
                    messagebox.showinfo("Éxito", "Datos guardados exitosamente")
                else:
                    messagebox.showwarning("Advertencia", "Ingrese un nombre antes de tomar la foto")
        cv2.imshow('Reconocimiento Facial', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("Iniciar Sesión")
root.geometry("800x600")

bg_image = Image.open("Setup/i.png")
bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl_nombre = tk.Label(root, text="Nombre")
lbl_nombre.pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

lbl_ci = tk.Label(root, text="CI")
lbl_ci.pack(pady=5)
entry_ci = tk.Entry(root)
entry_ci.pack(pady=5)

lbl_curso = tk.Label(root, text="Curso")
lbl_curso.pack(pady=5)
entry_curso = tk.Entry(root)
entry_curso.pack(pady=5)

lbl_actividad = tk.Label(root, text="Actividad")
lbl_actividad.pack(pady=5)
entry_actividad = tk.Entry(root)
entry_actividad.pack(pady=5)

btn_reconocimiento_facial = tk.Button(root, text="Reconocimiento Facial", command=reconocimiento_facial, width=20, height=2)
btn_reconocimiento_facial.pack(pady=20)

root.mainloop()

