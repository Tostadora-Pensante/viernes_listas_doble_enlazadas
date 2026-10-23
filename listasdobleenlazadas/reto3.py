actual_pagina = None
cabeza = None
cola = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}


def visitar(dato):
    global cabeza, cola, actual_pagina
    nuevo = crear_nodo(dato)
    
    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
        actual_pagina = nuevo
    else:
        # Al visitar una nueva página tras retroceder, cortamos el historial futuro
        actual_pagina["siguiente"] = nuevo
        nuevo["anterior"] = actual_pagina
        cola = nuevo
        actual_pagina = nuevo
    print(f"Visitando: {actual_pagina['dato']}")

def retroceder():
    global actual_pagina
    if actual_pagina and actual_pagina["anterior"]:
        actual_pagina = actual_pagina["anterior"]
        print(f"Retrocediste a: {actual_pagina['dato']}")
    else:
        print("No hay páginas anteriores.")

def avanzar():
    global actual_pagina
    if actual_pagina and actual_pagina["siguiente"]:
        actual_pagina = actual_pagina["siguiente"]
        print(f"Avanzaste a: {actual_pagina['dato']}")
    else:
        print("No hay paginas siguientes.")

def mostrar_actual():
    if actual_pagina:
        print(f"Pagina actual: {actual_pagina['dato']}")
    else:
        print("El historial está vacío.")

print("=Prueba 3: Historial=")
visitar("Google")
visitar("YouTube")
visitar("GitHub")

print("\n(Retrocediendo)")
retroceder()

print("\n(visitando depues de retroceder - borra el futuro)")
visitar("ChatGPT") 

print("\n(Intentando avanzar)")
avanzar() 