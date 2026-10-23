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


def insertar_despues(referencia, dato):
    global cabeza, cola
    actual = cabeza
    
    while actual is not None:
        if actual["dato"] == referencia:
            nuevo = crear_nodo(dato)
            siguiente_nodo = actual["siguiente"]
            
            nuevo["anterior"] = actual
            nuevo["siguiente"] = siguiente_nodo
            
            actual["siguiente"] = nuevo
            if siguiente_nodo is not None:
                siguiente_nodo["anterior"] = nuevo
            else:
                
                cola = nuevo
                
            return True
        actual = actual["siguiente"]
        
    return False 

print("\n--- PRUEBAS RETO 2: INSERCIÓN ---")
print("Lista antes de insertar:")
imprimir_lista()

# Insertamos "Productos" después de "Catálogo"
resultado = insertar_despues("Catálogo", "Productos")
print(f"¿Inserción exitosa?: {resultado}")

print("Lista después de insertar:")
imprimir_lista()