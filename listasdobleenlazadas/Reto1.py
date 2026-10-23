cabeza = None
cola = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

nodo1 = crear_nodo("Inicio")
nodo2 = crear_nodo("Continuacion")
nodo3 = crear_nodo("Final")

cabeza = nodo1
nodo1["siguiente"] = nodo2
nodo2["anterior"] = nodo1
nodo2["siguiente"] = nodo3
nodo3["anterior"] = nodo2
cola = nodo3


def buscar(dato):
    global cabeza, cola
    if cabeza is None:
        return False
    
    valizq = cabeza
    valder = cola
   
    while valizq is not None and valder is not None:
        if valizq["dato"] == dato or valder["dato"] == dato:
            return True
        
        if valizq == valder or valizq["siguiente"] == valder:
            break
            
        valizq = valizq["siguiente"]
        valder = valder["anterior"]
        
    return False

print("=Reto 1: Buscador =")
print("¿Existe Inicio?:", buscar("Inicio")) 
print("¿Existe Continuacion?:", buscar("Continuacion"))  
print("¿Existe Cetian?:", buscar("Cetian"))          