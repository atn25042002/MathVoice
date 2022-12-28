from speech_recognition import Recognizer, Microphone
import modulo
from tkinter import messagebox

def entrada(aviso):
    r = Recognizer()
    aviso.set("¡Escuchando...!")
    messagebox.showinfo("MATH-Voice", "A continuación diga la expresión...")  
    with Microphone() as source:  
        audio = r.listen(source)        
        try:
            text = r.recognize_google(audio, language="es-ES")
        except:
            text= ""
    aviso.set("")
    return text

def proceso(texto):
    for frase in modulo.frases:
        texto= texto.replace(frase, modulo.frases.get(frase))
    array= texto.split()
    txt= ""
    for c in array:
        if modulo.palabras.__contains__(c):
            txt+= modulo.palabras.get(c)
        else:
            txt+= c
    txt= emparejar(txt)
    return txt

def emparejar(texto):
    lst= list()
    txt= ""
    for x in texto:
        if modulo.pares.__contains__(x):
            lst.append(x)
        if x == "#":
            txt+= modulo.pares.get(lst.pop())
        else:
            txt+= x
            
    lst.reverse()
    for c in lst:
        txt+= modulo.pares.get(c)
    
    return txt