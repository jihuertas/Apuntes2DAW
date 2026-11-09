from pathlib import Path
import json

tareas=[]
FICHLOG = "log_tareas.txt"
FICHDATA = "tareas.json"

def guardar_log(contenido):
    ruta = Path('datos4')
    if not ruta.exists():
        ruta.mkdir()
    print(ruta.parent)
    fich = ruta / FICHLOG
    with open(fich,'a', encoding='utf-8') as fichero:
        fichero.write(contenido)

def carga_datos():
    try:
        with open(FICHDATA,'r', encoding='utf-8') as fichero:
            global tareas
            tareas= json.load(fichero)
            print("Datos cargados correctamente")
    except FileNotFoundError:
        print("No hay fichero con datos para cargar")
    except json.JSONDecodeError:
        print("El fichero JSON está dañado")
    
def guarda_datos():
    with open(FICHDATA,'w', encoding='utf-8') as fichero:
        json.dump(tareas,fichero,ensure_ascii=False, indent=3)
        print("Datos guardados correctamente")

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes introducir un número.")
    
def menu():
    print("*****Menú de tareas*****")
    print("0. Salir")
    print("1. Añadir tarea")
    print("2. Eliminar tarea")
    print("3. Buscar tarea")
    print("4. Editar tarea")
    print("5. Listar tareas")
    print("6. Marcar completada")
    print("7. Buscar nombre")

    opcion = int(input("Seleccione una opción: "))
    return opcion

def listar_tareas():
    print("Listado de tareas")
    print(tareas)

def buscar_nombre(nombre):
    tareas_nombre=[]
    for tarea in tareas:
        if str(tarea["nombre"]).lower().__contains__(nombre.lower()):
            tareas_nombre.append(tarea)
    return tareas_nombre

def buscar_tarea(codigo):
    tareas_cod=[]
    for tarea in tareas:
        if tarea["codigo"] == codigo:
            tareas_cod.append(tarea)
    return tareas_cod

def nueva_tarea():
    t_nombre = input("Ingrese el nombre para la tarea: ")
    t_tiempo = pedir_entero("Ingrese el tiempo en minutos estimado para la tarea: ")
    t_estado = False

    tarea={"codigo": len(tareas)+1,
           "nombre": t_nombre,
           "tiempo_estimado": t_tiempo, 
           "estado": t_estado}
    
    tareas.append(tarea)
    print("Tarea añadida correctamente")

    guardar_log(f"Nueva tarea {tarea}")

def marcar_tarea(tarea):
    tarea["estado"] = True

def main():
    carga_datos()
    while True:
        opcion = menu()

        if opcion == 0:
            break
        elif opcion == 1:
            nueva_tarea()

        elif opcion== 2:
            listar_tareas()
            t_codigo = pedir_entero("Ingrese el código de la tarea a eliminar: ")
            tarea = buscar_tarea(t_codigo)
            if tarea:
                tareas.remove(tarea)
                print("Tarea eliminada correctamente")
            else:
                print("Tarea no encontrada")
       
            
        elif opcion== 3:
            t_codigo = pedir_entero("Ingrese el código de la tarea a buscar: ")
            tarea = buscar_tarea(t_codigo)
            if not tarea:
                print("Tarea no encontrada")
            else:
                print(f"Tarea encontrada: {tarea}")

        elif opcion== 4:
            t_codigo = pedir_entero("Ingrese el código de la tarea a editar: ")
            tarea = buscar_tarea(t_codigo)
            if tarea:
                t_nombre = input("Ingrese el nuevo nombre para la tarea: ")
                t_tiempo = pedir_entero("Ingrese el nuevo tiempo en minutos estimado para la tarea: ")
                tarea["nombre"] = t_nombre
                tarea["tiempo_estimado"] = t_tiempo      
                print("Tarea editada correctamente")
            else:
                print("Tarea no encontrada")
        elif opcion== 5:
            listar_tareas()
        elif opcion== 6:
            t_codigo = pedir_entero("Ingrese el código de la tarea a marcar: ")
            tarea = buscar_tarea(t_codigo)

            marcar_tarea(tarea)
        elif opcion == 7:
            t_nombre = input("Dame una parte del texto del nombre: ")
            tareas_nombre = buscar_nombre(t_nombre)
            if tareas_nombre:
                print(tareas_nombre)
    guarda_datos()
    print("Guardando tareas en archivo...")

if __name__ == "__main__":
    main()