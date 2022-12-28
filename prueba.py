import tkinter as tk
from tkinter import font
import modulo

#txt= modulo.completarFunc("x+y^(x+(y+z))", "^")
#print(txt)

root = tk.Tk()
for font in font.families():
    print(font)
"""
#Ensayo
    if invpares.keys().__contains__(txt1[0]):         
        cont= 1
        c= txt1[0]
        c2= invpares.get(c)
        for aux in txt1[1:]:
            if aux == c:
                cont+= 1
            elif aux == c2:
                cont-= 1            
            if cont == 0:
                i+= 1
                break
            i+= 1
    else: 
        for aux in txt1[1:]:
            if opers.__contains__(aux):
                break
            i+= 1
    txt1= "#" + txt1[:i] + "$" + txt1[i:]
    txt1= txt1[::-1]

    i= 1
    #hacia adelante
    if pares.keys().__contains__(txt2[0]):         
        cont= 1
        c= txt2[0]
        c2= pares.get(c)
        for aux in txt2[1:]:
            if aux == c:
                cont+= 1
            elif aux == c2:
                cont-= 1            
            if cont == 0:
                i+= 1
                break
            i+= 1
    else: 
        for aux in txt2[1:]:
            if opers.__contains__(aux):
                break
            i+= 1
    txt2= "$" + txt2[:i] + "#" + txt2[i:]
"""