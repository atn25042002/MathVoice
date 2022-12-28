from tkinter import END
def guardar(lista):
    datos= lista.get("0", END)
    if len(datos)== 0:
        return
    file= open("data.txt", "w", encoding="utf-8")
    for linea in datos:
        file.write(linea)
    
    file.close()
    return

def cargar(lista):
    file= open("data.txt", "r", encoding="utf-8")
    for linea in file:
        if(linea.strip() != ""):
            lista.insert(END, linea)
    return