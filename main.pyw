from tkinter import Tk, filedialog, Button, messagebox
import sys

sys.path.append("./app/")
from Processor import Processor


# from methods.procesar_archivo import procesar_archivo


def callback():
    rutaArchivo = filedialog.askopenfilename()
    if not rutaArchivo:
        messagebox.showinfo(message="Seleccione un archivo", title="Info")
        return
    if rutaArchivo != "":
        Procesador = Processor()
        response = Procesador.procesar_archivo(rutaArchivo)

        if response["status"]:
            messagebox.showinfo(message=response["message"], title="Información")
        else:
            messagebox.showerror(message=response["message"], title="Error :/")
    else:
        messagebox.showinfo(message="Seleccione un archivo", title="Info")


ventana = Tk()
ventana.title("Neubox - Challenge 1")
ventana.geometry("600x480")


btn = Button(
    ventana,
    text="Seleccionar archivo",
    command=callback,
)
btn.place(x=175, y=135, width=150, height=36)


ventana.mainloop()
