planes = {
    'F001': ['Plan Basico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, False, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, False, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}

inscripciones = {
    #precio #cupo
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
}
#modelo = plan
#productos = planes
#
def leer_opcion():
    opcion = input("Ingrrese una opcion del 1 al 6: ");
    try:
        opcion = int(opcion)
        if opcion < 1 or opcion > 6:
            print("Opcion no invalida, igrese un numero del 1 al 6");
            return -1
        return opcion
    except:
        print("")
        print("caracter invalido")
        print("")
        return

def cupos_tipo(tipo):
    total = 0
    for plan in planes:
        tipo_plan = planes[plan][1]
        if tipo_plan.lower() == tipo.lower():
            total = total + inscripciones
    print (f"Hay {total} cupos de este plan")


def busqueda_precio(p_min, p_max):
        resultado = []
        for plan in inscripciones:
            precio = inscripciones[plan][0]
            tipo = inscripciones[plan][1]
        if precio >= p_min and precio <= p_max and cupos != 0:
            texto = cupos_tipo + "--" + plan
            resultado.append(texto)
        resultado.stor()
        if len(resultado) == 0:
            print("No hay planes dentro de ese rango de precio")
        else:
            print(f"los planes dentro de este rango de precio son: {resultado}")

def actualizar_precio(plan, p):
    if plan in planes:
        inscripciones[plan][0] = p

def validar_codigo(codigo):
   if codigo.strip() == "" "":
       return False
   return True

def validar_nombre_plan(nombre):
    if nombre.strip():
        return False
    return True

def menu():
    
    print("========== MENU PRINCIPAL ==========");
    print("1. Cupos por tipos de plan");
    print("2. Busqueda de planes por rango de precio");
    print("3. Actualizar precio de plan");
    print("4. Agregar plan");
    print("5. Eliminar Plan");
    print("6. salir");
    print("=====================================");

def main_menu():
    while True:
        menu ()
        opcion = leer_opcion()

        if opcion == 1:
            tipo = input("Ingrese el tipo de plan que desea buscar: ")


        elif opcion == 2:
            while True:
               try:
                   p_min = int(input("Ingrese precio minimo: "))
                   p_max = int(input("Ingrese el precio maximo: "))
                   break
               except ValueError:
                   print("Debe ingresae Valores Enteros");
            busqueda_precio(p_min, p_max)
    return


main_menu()