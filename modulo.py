bgcolors = ["#FBB460", "#FBE360", "#BCFB60", "#7EFB60", "#60FBBC","#607EFB", "#8960FB", "#FB60E3"]
pares= {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "|" : "¦"
}
invpares= {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    "¦" : "|"
}
frases= {
    "a la ": "e",
    "ala ": "e", 
    "al cuadrado" : "²",
    "al cubo" : "³",
    "elevado a": "^(",
    "raíz ": "r",
    "valor absoluto de": "vabs",
    "de": "(",    
    "es igual a": "=",
    "es mayor a": ">",
    "es menor a" : "<",
    "es menor o igual a" : u"\u2264",
    "es mayor o igual a" : u"\u2265"
}
palabras = {
    #Simples
    "más" : "+",
    "menos" : "-",
    "por" : "*",
    "entre": "/",
    "abre" : "(",
    "paréntesis" : "(",
    "llave": "{",
    "corchete": "[",
    "cierra" : "#", #Elemento de cierre
    "sierra" : "#",
    "alfa" : "α",
    "beta" : "β" ,
    "teta" : "θ" ,
    "landa" : "λ" ,
    "cuadrado" : "²",
    "cubo" : "³",
    "ecuarta" : u"\u2074",
    "ecuatro" : u"\u2074",
    "equinta" : u"\u2075",
    "esexta" : u"\u2076",
    "eséptima" : u"\u2077",
    "eoctava" : u"\u2078",
    "enovena" : u"\u2079",
    #Funciones
    "coseno" : "cos",
    "cotangente" : "cot",
    "cosecante" : "csc",
    "seno" : "sin",
    "tangente" : "tan",
    "secante" : "sec",

    #Arcos
    "arcocoseno" : "cos" + u"\u207B" + u"\u00B9",
    "arcocotangente" : "cot" + u"\u207B" + u"\u00B9",
    "arcocosecante" : "csc" + u"\u207B" + u"\u00B9",
    "arcoseno" : "sin" + u"\u207B" + u"\u00B9",
    "arcotangente" : "tan" + u"\u207B" + u"\u00B9",
    "arcosecante" : "sec" + u"\u207B" + u"\u00B9",

    "hiperbólico": "h",
    "hiperbólica": "h",
    "arco": "arc",
    "rcuadrada" : u"\u221A",
    "rde" : u"\u221A",
    "rcúbica" : u"\u221B",
    "rcuarta" : u"\u221C",
    "vabs" : "|"
}

latex = {
    "sinh" : "\sinh",
    "cosh" : "\cosh",
    "tanh" : "\tanh",
    "coth" : "\coth",
    "sech" : "\sech",
    "csch" : "\csch",
    "sin⁻¹" : "\sin^(-1)",
    "cos⁻¹" : "\cos^(-1)",
    "tan⁻¹" : "\tan^(-1)",
    "cot⁻¹" : "\cot^(-1)",
    "sec⁻¹" : "\sec^(-1)",
    "csc⁻¹" : "\csc^(-1)",
    "sin" : "\sin",
    "cos" : "\cos",
    "tan" : "\tan",
    "cot" : "\cot",
    "sec" : "\sec",
    "csc" : "\csc",
    #Raices y exponentes
    u"\u221A" : "\sqrt[2]",
    u"\u221B" : "\sqrt[3]",
    u"\u221C" : "\sqrt[4]",
    "⁻¹" : "^(-1)",
    "²" : "^(2)",
    "³" : "^(3)",
    u"\u2074" : "^(4)",
    u"\u2075" : "^(5)",
    u"\u2076" : "^(6)",
    u"\u2077" : "^(7)",
    u"\u2078" : "^(8)",
    u"\u2079" : "^(9)",
    #Letras griegas
    "α" : "\\" + "alpha",
    "β" : "\\" + "beta",
    "θ" : "\\" + "theta",
    "λ" : "\\" + "lambda",
    #Caracteres
    u"\u2264" : "\leq",
    u"\u2265" : "\geq"
}

funcComplet=["\sqrt[3]", "\sqrt[4]", "\sqrt[2]", "^"]

def aLatex(txt = ""):
    for frase in latex:
        txt= txt.replace(frase, latex.get(frase))
    for x in range(txt.count("/")):
        txt= completarFrac(txt)
    for f in funcComplet:
        for x in range(txt.count(f)):
            txt= completarFunc(txt, f)
    txt= txt.replace("$", "{")
    txt= txt.replace("#", "}")
    txt= txt.replace("\\" + "\\", "\\")
    return txt

def completarFrac(txt= ""):
    #Entrada: $ , Salida: #
    opers= "+-*/"
    med= txt.find("/")
    txt1= txt[: med]
    txt2= txt[(med+1):]
    txt1= txt1[::-1] 
    i= 0
    #hacia atras
    conf= False
    for aux in txt1:
        if conf:
            if aux== c:
                cont+= 1
            elif aux== c2:
                cont-= 1
                if cont== 0:
                    conf= False
        else:
            if invpares.get(aux) != None:
                conf= True
                c= aux
                c2= invpares.get(c)
                cont= 1
            elif opers.find(aux)> -1:
                break
        i+= 1
    
    txt1= "#" + txt1[:i] + "$" + txt1[i:]
    txt1= txt1[::-1]

    #hacia adelante
    i= 0
    conf= False
    for aux in txt2:
        if conf:
            if aux== c:
                cont+= 1
            elif aux== c2:
                cont-= 1
            if cont== 0:
                conf= False
        else:
            if pares.get(aux) != None:
                conf= True
                c= aux
                c2= pares.get(c)
                cont= 1
            elif opers.find(aux)> -1:
                break
        i+= 1
    txt2= "$" + txt2[:i] + "#" + txt2[i:]
    
    return "\frac" + txt1 + txt2

def completarFunc(txt= "", func= "f"):
    i= txt.find(func + "(") + len(func) + 1
    txt2= txt[i:]
    ini= txt[:(i-1)]
    cont= 1

    i= 0
    for c in txt2:
        if c == "(":
            cont+= 1
        elif c == ")":
            cont-= 1

        if cont== 0:
            break
        i+= 1
    
    txt= ini + "{" + txt2[:i] + "}" + txt2[(i+1):]
    return txt