from tkinter import messagebox, Label, Text, Button, StringVar
from tkinter import Listbox, Scrollbar, Menu, END, Tk
from tkinter.messagebox import askyesno
import random
import modulo
import transcribirVoz
import data
import pyperclip as clipboard

class Interfaz:
    def __init__(self, ventana):
        # --------------- GENERAL ----------------------
        self.ventana= ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.salir)
        self.ventana.title("MATH-Voice🎤")
        self.ventana.resizable(False,False)
        self.ventana.iconbitmap("Images/icono.ico")
        self.ventana.geometry("550x680")
        c= random.randrange(1,8,1) #8 colores
        self.fondo= modulo.bgcolors[c]
        self.ventana.configure(bg=self.fondo)
        
        #  ---------------------- VENTANA ---------------------
        titulo= Label(self.ventana, text= "MATH-Voice🎤", font= ("Consolas", 35, "bold"), bg= self.fondo)
        titulo.place(x=135,y= 20)
        titulo= Label(self.ventana, text= "Ingrese una expresión mediante voz:", font= ("Consolas", 14), bg= self.fondo)
        titulo.place(x=25,y= 100)
        self.simbolo= Text(self.ventana, state="disabled", width=40, height=1, pady=8, font=("Mathcad UniMath",12), padx= 15)
        self.simbolo.place(x= 70, y= 140)
        self.btEscuchar= Button(self.ventana, text = "Escuchar 🎤", command= lambda:self.ingresar(), height=1, width=12, font= ("Consolas", 14))
        self.btEscuchar.place(x = 70,y = 190)
        añadir= Button(self.ventana, text = "Añadir", command= lambda:self.añadir(), height=1, width=10, font= ("Consolas", 14))
        añadir.place(x = 370,y = 190)
        self.aviso = StringVar()
        self.lblgrabar= Label(self.ventana, textvariable= self.aviso, font= ("Consolas", 12, "bold"), bg= self.fondo)
        self.aviso.set("")
        self.lblgrabar.place(x= 70, y= 240)
        self.lista= Listbox(self.ventana, width=44, height=15, font=("Mathcad UniMath",12), selectmode= "extended")
        self.lista.place(x = 70,y = 270)
        barra = Scrollbar(self.ventana)
        barra.place(x = 470,y = 270, height= 304)
        self.lista.config(yscrollcommand= barra.set)
        barra.config(command= self.lista.yview)

        # ----------------------- Botones adicionales -------------------
        self.btModificar= Button(self.ventana, text = "Modificar", command= lambda:self.modificar(), height=1, width=10, font= ("Consolas", 14))
        self.btModificar.place(x = 70,y = 600)
        self.btEliminar= Button(self.ventana, text = "Eliminar", command= lambda:self.eliminar(), height=1, width=10, font= ("Consolas", 14))
        self.btEliminar.place(x = 220,y = 600)
        btCopiar= Button(self.ventana, text = "Copiar", command= lambda:self.copiar(), height=1, width=10, font= ("Consolas", 14))
        btCopiar.place(x = 370,y = 600)
        self.modo= StringVar()
        btLatex= Button(self.ventana, textvariable= self.modo, command= lambda:self.formatLatex(), height=1, width=6, font= ("Mathcad UniMath", 14, "bold"))
        btLatex.place(x = 240,y = 220)
        self.modo.set("LATEX")
        self.respaldo= dict()
        data.cargar(self.lista)

        #  ---------------------- OPCIONES ---------------------
        barra= Menu(self.ventana)
        archivo= Menu(barra, tearoff= 0)
        archivo.add_command(label = "Guardar", command = self.guardar)
        archivo.add_command(label = "Guardar y salir", command= self.guardarSalir)
        archivo.add_command(label = "Exportar")
        archivo.add_separator()
        archivo.add_command(label = "Salir", command = self.salir)
        barra.add_cascade(label = "Archivo", menu = archivo)

        herram= Menu(barra, tearoff= 0)
        herram.add_command(label= "Copiar todo...", command= self.copiarTodo)
        herram.add_command(label= "Eliminar todo...", command= self.eliminarTodo)        
        herram.add_separator()
        herram.add_command(label="Deshacer Eliminar", command= self.restaurar)
        barra.add_cascade(label= "Herramientas", menu= herram)

        ayuda= Menu(barra, tearoff= 0)
        ayuda.add_command(label = "Manual de Uso")
        ayuda.add_command(label = "Contacto")
        ayuda.add_separator()
        ayuda.add_command(label = "Acerca de ...")
        barra.add_cascade(label= "Ayuda", menu= ayuda)

        self.ventana.config(menu= barra)

        return

    def ingresar(self):
        self.btEscuchar.configure(state="disabled")
        self.ventana.grab_set()
        self.limpiar()
        str= transcribirVoz.entrada(self.aviso)
        if str.strip() == "" :
            self.mensaje("¡No se escuchó!")
            self.btEscuchar.configure(state="normal")
            return
        str= str.lower()
        str= transcribirVoz.proceso(str)
        self.simbolo.configure(state="normal")
        self.simbolo.insert(END, str)
        self.simbolo.configure(state="disabled")
        self.btEscuchar.configure(state="normal")
        return
    
    def añadir(self):
        txt= self.simbolo.get("1.0", END)
        if txt.strip() != "":
            self.lista.insert(END, self.simbolo.get("1.0",END))
            self.lista.select_clear(0,END)
            self.lista.select_set(self.lista.size() - 1)
            self.lista.see(self.lista.size() - 1)
        else:
            self.mensaje("¡Ingrese una expresión primero!")
        return

    def limpiar(self):
        self.simbolo.configure(state="normal")
        self.simbolo.delete("1.0",END)
        self.simbolo.configure(state="disabled")
        return

    def eliminar(self):
        lst= self.lista.curselection()
        if(len(lst)> 0):
            aux= 0 # Corrige el indice cada que se elimina un elemento
            self.respaldo.clear()
            for i in lst:
                self.respaldo[i]= self.lista.get(i-aux)
                self.lista.delete(i - aux)
                aux+= 1
            if lst[0]> 0 and len(lst) == 1: #Para que se mueva la seleccion al siguiente elemento
                if(self.lista.size() == lst[0]):
                    self.lista.select_set(lst[0] - 1)
                else:
                    self.lista.select_set(lst[0])
        else:
            self.mensaje("¡Nada Seleccionado!")
        return

    def eliminarTodo(self):
        answer = askyesno(title='Confirmación', message='¿Estas seguro(a) de quieres eliminar toda la lista de ecuaciones?')
        if answer:
            self.respaldo.clear()
            datos= self.lista.get("0", END)
            i= 0
            for ec in datos:
                self.respaldo[i]= ec
                i+= 1
            self.lista.delete("0", END)
        return

    def restaurar(self):
        if(len(self.respaldo)> 0):
            for i, ec in self.respaldo.items():
                self.lista.insert(i, ec)
            self.respaldo.clear()
        else:
            self.mensaje("¡No se elimino nada!")
        return

    def mensaje(self, txt):
        messagebox.showinfo("MATH-VOICE", txt)
        return
    
    def modificar(self):
        txt= self.simbolo.get("1.0", END)
        if txt.strip() != "":
            lst= self.lista.curselection()
            if(len(lst)> 0):
                self.lista.delete(lst[0])
                self.lista.insert(lst[0], self.simbolo.get("1.0",END))
                self.mensaje("¡Ecuación modificada!")
            else:
                self.mensaje("¡Nada Seleccionado!")                
        else:
            self.mensaje("¡Ingrese una expresión primero!")
        
        return
    
    def copiar(self):
        lst= self.lista.curselection()
        if(len(lst)> 0):
            str= ""
            for i in lst:
                str+= self.lista.get(i)
            clipboard.copy(str)
            self.mensaje("¡Se copiaron las ecuaciones seleccionadas!")
        else:
            self.mensaje("¡Nada Seleccionado!")
        return

    def copiarTodo(self): #Para copiar al portapapeles
        str= ""
        datos= self.lista.get("0", END)
        for txt in datos:
            str+= txt
        clipboard.copy(str)
        self.mensaje("¡Se copio todo!")
        return

    def salir(self):
        answer = askyesno(title='Confirmación', message='¿Estas seguro(a) de que quieres salir?\nSe recomienda guardar antes de salir')
        if answer:
            self.ventana.destroy()
        return
    
    def guardar(self):
        data.guardar(self.lista)
        self.mensaje("¡Se guardo exitosamente!")
        return

    def guardarSalir(self):
        self.guardar()
        self.ventana.destroy()
        return

    def formatLatex(self):
        if(self.modo.get() == "Unicode"):
            self.lista.delete("0", END)
            data.cargar(self.lista)
            self.modo.set("LATEX")
            return
        self.mensaje("Primero se guardarán los datos")
        data.guardar(self.lista)
        datos= self.lista.get("0", END)
        
        i= 0
        if(len(datos)> 0):
            for e in datos:
                self.lista.delete(i)
                self.lista.insert(i, modulo.aLatex(e))
                i+= 1
            self.modo.set("Unicode")
        else:
            self.mensaje("¡No hay ecuaciones!")
        return

principal= Tk()
mathVoice= Interfaz(principal)
principal.mainloop()
#CAMBIAR A pyw