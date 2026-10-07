tareas=[]

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
    t_tiempo = int(input("Ingrese el tiempo en minutos estimado para la tarea: "))
    t_estado = False
    
    tareas.append({"codigo": len(tareas)+1,"nombre": t_nombre,"tiempo_estimado": t_tiempo, "estado": t_estado})
    print("Tarea añadida correctamente")

def marcar_tarea(tarea):
    tarea["estado"] = True

def main():
    while True:
        opcion = menu()

        if opcion == 0:
            break
        elif opcion == 1:
            nueva_tarea()

        elif opcion== 2:
            listar_tareas()
            t_codigo = int(input("Ingrese el código de la tarea a eliminar: "))
            tarea = buscar_tarea(t_codigo)
            if tarea:
                tareas.remove(tarea)
                print("Tarea eliminada correctamente")
            else:
                print("Tarea no encontrada")
       
            
        elif opcion== 3:
            t_codigo = int(input("Ingrese el código de la tarea a buscar: "))
            tarea = buscar_tarea(t_codigo)
            if not tarea:
                print("Tarea no encontrada")
            else:
                print(f"Tarea encontrada: {tarea}")

        elif opcion== 4:
            t_codigo = int(input("Ingrese el código de la tarea a editar: "))
            tarea = buscar_tarea(t_codigo)
            if tarea:
                t_nombre = input("Ingrese el nuevo nombre para la tarea: ")
                t_tiempo = int(input("Ingrese el nuevo tiempo en minutos estimado para la tarea: "))
                tarea["nombre"] = t_nombre
                tarea["tiempo_estimado"] = t_tiempo      
                print("Tarea editada correctamente")
            else:
                print("Tarea no encontrada")
        elif opcion== 5:
            listar_tareas()
        elif opcion== 6:
            t_codigo = int(input("Ingrese el código de la tarea a marcar: "))
            tarea = buscar_tarea(t_codigo)

            marcar_tarea(tarea)
        elif opcion == 7:
            t_nombre = input("Dame una parte del texto del nombre: ")
            tareas_nombre = buscar_nombre(t_nombre)
            if tareas_nombre:
                print(tareas_nombre)

    print("Guardando tareas en archivo...")

if __name__ == "__main__":
    main()