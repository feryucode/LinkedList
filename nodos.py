class Nodo:
    def __init__(self):
        # Estructura del nodo: INFORMACIÓN y LIGA
        self.INFO = None
        self.LIGA = None

class ListaSimplementeLigada:
    def __init__(self):
        # P apunta al inicio de la lista (NIL es None)
        self.P = None

    # =====================================================
    # ALGORITMO 5.1: Crea_inicio
    # =====================================================
    def crea_inicio(self):
        print("\n--- CREAR LISTA (Algoritmo 5.1: Crea_inicio) ---")
        self.P = Nodo()
        self.P.INFO = input("Ingrese el dato (P^.INFO): ")
        self.P.LIGA = None
        
        RES = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 -> "))
        while RES == 1:
            Q = Nodo()
            Q.INFO = input("Ingrese el dato (Q^.INFO): ")
            Q.LIGA = self.P
            self.P = Q
            RES = int(input("¿Desea ingresar más nodos a la lista? Sí: 1, No: 0 -> "))
        print("Lista creada correctamente.")

    # =====================================================
    # 5.2.2 RECORRIDO DE LA LISTA
    # =====================================================
    def recorrido(self):
        print("\n--- RECORRIDO DE LA LISTA ---")
        if self.P is None:
            print("La lista está vacía (P = NIL).")
            return
        
        Q = self.P
        nodos = []
        while Q is not None:
            nodos.append(f"[{Q.INFO}]")
            Q = Q.LIGA
        print("P -> " + " -> ".join(nodos) + " -> NIL")

    # =====================================================
    # 5.2.3 INSERCIÓN EN LISTAS SIMPLEMENTE LIGADAS
    # =====================================================
    
    # 1. Insertar al inicio
    def inserta_inicio(self, DATO):
        Q = Nodo()
        Q.INFO = DATO
        Q.LIGA = self.P
        self.P = Q
        print(f"Elemento '{DATO}' insertado al inicio de la lista.")

    # 2. Insertar al final
    def inserta_final(self, DATO):
        Q = Nodo()
        Q.INFO = DATO
        Q.LIGA = None
        
        if self.P is None:
            self.P = Q
        else:
            T = self.P
            while T.LIGA is not None:
                T = T.LIGA
            T.LIGA = Q
        print(f"Elemento '{DATO}' insertado al final de la lista.")

    # 3. Insertar antes de un nodo con valor X (Inserta_antes_X)
    def inserta_antes_x(self, DATO, X):
        if self.P is None:
            print("La lista está vacía. No se puede buscar la referencia.")
            return

        Q = self.P
        BAND = 1
        T = None

        while (Q.INFO != X) and (BAND == 1):
            if Q.LIGA is not None:
                T = Q
                Q = Q.LIGA
            else:
                BAND = 0

        if BAND == 1:
            X_NODO = Nodo()
            X_NODO.INFO = DATO
            if self.P == Q: # El nodo de referencia es el primero
                X_NODO.LIGA = self.P
                self.P = X_NODO
            else:
                T.LIGA = X_NODO
                X_NODO.LIGA = Q
            print(f"Elemento '{DATO}' insertado ANTES de '{X}'.")
        else:
            print(f"El nodo dado como referencia ('{X}') no se encuentra en la lista.")

    # 4. Insertar después (delante) de un nodo con valor X (Inserta_despues_X)
    def inserta_despues_x(self, DATO, X):
        if self.P is None:
            print("La lista está vacía. No se puede buscar la referencia.")
            return

        Q = self.P
        BAND = 1

        while (Q.INFO != X) and (BAND == 1):
            if Q.LIGA is not None:
                Q = Q.LIGA
            else:
                BAND = 0

        if BAND == 1:
            T = Nodo()
            T.INFO = DATO
            T.LIGA = Q.LIGA
            Q.LIGA = T
            print(f"Elemento '{DATO}' insertado DESPUÉS (delante) de '{X}'.")
        else:
            print(f"El nodo dado como referencia ('{X}') no se encuentra en la lista.")

    # =====================================================
    # 5.2.4 BORRADO EN LISTAS SIMPLEMENTE LIGADAS
    # =====================================================

    # 1. Eliminar el primer nodo
    def elimina_inicio(self):
        if self.P is None:
            print("La lista está vacía.")
        else:
            Q = self.P
            self.P = Q.LIGA
            print(f"Primer nodo ('{Q.INFO}') eliminado.")
            del Q

    # 2. Eliminar el último nodo
    def elimina_ultimo(self):
        if self.P is None:
            print("La lista está vacía.")
        else:
            Q = self.P
            if self.P.LIGA is None:
                self.P = None
            else:
                T = None
                while Q.LIGA is not None:
                    T = Q
                    Q = Q.LIGA
                T.LIGA = None
            print(f"Último nodo ('{Q.INFO}') eliminado.")
            del Q

    # 3. Eliminar un nodo con información X
    def elimina_x(self, X):
        if self.P is None:
            print("La lista está vacía.")
            return

        Q = self.P
        T = None
        BAND = 1

        while (Q.INFO != X) and (BAND == 1):
            if Q.LIGA is not None:
                T = Q
                Q = Q.LIGA
            else:
                BAND = 0

        if BAND == 0:
            print(f"El elemento con información '{X}' no se encuentra en la lista.")
        else:
            if self.P == Q: # Es el primer nodo
                self.P = Q.LIGA
            else:
                T.LIGA = Q.LIGA
            print(f"Nodo con información '{X}' eliminado.")
            del Q

    # 4. Eliminar el nodo anterior al nodo con información X
    def elimina_antes_x(self, X):
        if self.P is None:
            print("La lista está vacía.")
            return

        if self.P.INFO == X:
            print(f"No existe un nodo que preceda a '{X}' (es el primero de la lista).")
        else:
            Q = self.P
            T = self.P
            R = None
            BAND = 1

            while (Q.INFO != X) and (BAND == 1):
                if Q.LIGA is not None:
                    R = T
                    T = Q
                    Q = Q.LIGA
                else:
                    BAND = 0

            if BAND == 0:
                print(f"El elemento '{X}' no se encuentra en la lista.")
            else:
                if self.P.LIGA == Q: # El nodo a eliminar es el primero (P)
                    self.P = Q
                else:
                    R.LIGA = Q
                print(f"Nodo '{T.INFO}' (que estaba antes de '{X}') eliminado.")
                del T

    # =====================================================
    # 5.2.5 BÚSQUEDA EN LISTAS SIMPLEMENTE LIGADAS
    # =====================================================
    def busqueda_desordenada(self, X):
        if self.P is None:
            print("La lista está vacía.")
            return

        Q = self.P
        while (Q is not None) and (Q.INFO != X):
            Q = Q.LIGA

        if Q is None:
            print(f"El elemento '{X}' NO se encuentra en la lista.")
        else:
            print(f"El elemento '{X}' SÍ se encuentra en la lista.")


# =====================================================
# MENÚ PRINCIPAL INTERACTIVO
# =====================================================
def menu():
    lista = ListaSimplementeLigada()

    while True:
        print("\n==================================================")
        print("       OPERACIONES CON LISTAS LIGADAS (Cap. 5)    ")
        print("==================================================")
        print("1. Crear lista al inicio (Algoritmo 5.1 Crea_inicio)")
        print("2. Recorrido de la lista (Mostrar nodos)")
        print("3. Insertar un elemento (Opciones de 5.2.3)")
        print("4. Borrar un elemento   (Opciones de 5.2.4)")
        print("5. Buscar un elemento   (Opciones de 5.2.5)")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            lista.crea_inicio()

        elif opcion == "2":
            lista.recorrido()

        elif opcion == "3":
            print("\n--- SUBMENÚ DE INSERCIÓN (5.2.3) ---")
            print("a) Insertar al inicio")
            print("b) Insertar al final")
            print("c) Insertar ANTES de un elemento X")
            print("d) Insertar DESPUÉS (delante) de un elemento X")
            sub = input("Elija cómo desea insertar (a/b/c/d): ").lower()

            if sub == "a":
                dato = input("Ingrese el nuevo dato a insertar (DATO): ")
                lista.inserta_inicio(dato)
            elif sub == "b":
                dato = input("Ingrese el nuevo dato a insertar (DATO): ")
                lista.inserta_final(dato)
            elif sub == "c":
                dato = input("Ingrese el nuevo dato a insertar (DATO): ")
                x = input("¿ANTES de qué elemento (X) lo quiere poner?: ")
                lista.inserta_antes_x(dato, x)
            elif sub == "d":
                dato = input("Ingrese el nuevo dato a insertar (DATO): ")
                x = input("¿DESPUÉS (delante) de qué elemento (X) lo quiere poner?: ")
                lista.inserta_despues_x(dato, x)
            else:
                print("Opción no válida.")

        elif opcion == "4":
            print("\n--- SUBMENÚ DE BORRADO (5.2.4) ---")
            print("a) Eliminar el primer nodo")
            print("b) Eliminar el último nodo")
            print("c) Eliminar un nodo con información X")
            print("d) Eliminar el nodo ANTERIOR al nodo con información X")
            sub = input("Elija cómo desea borrar (a/b/c/d): ").lower()

            if sub == "a":
                lista.elimina_inicio()
            elif sub == "b":
                lista.elimina_ultimo()
            elif sub == "c":
                x = input("Ingrese el elemento (X) que desea eliminar: ")
                lista.elimina_x(x)
            elif sub == "d":
                x = input("¿Eliminar el nodo anterior a qué elemento (X)?: ")
                lista.elimina_antes_x(x)
            else:
                print("Opción no válida.")

        elif opcion == "5":
            x = input("Ingrese el elemento (X) que desea buscar: ")
            lista.busqueda_desordenada(x)

        elif opcion == "6":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()