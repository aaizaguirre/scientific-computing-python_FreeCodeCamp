usuarios = []
opciones = [1,2,3,4,5]

def añadir_usuario():
    while True:
        usuario_nuevo = input("Ingrese el nombre del usuario: ")
        for usuario in usuarios:
            if usuario == usuario_nuevo:
                print("Ese usuario ya existe!")
            else:
                break
        usuarios.append(usuario_nuevo)
        print(f"Usuario {usuario_nuevo} añadido!")
        break

def modificar_usuario():
    while True:
        usuario_a_modificar = input("Ingrese el nombre del usuario a modificar: ")
        usuario_nuevo = input("Ingrese el nuevo nombre de usuario: ")
        for usuario in usuarios:
            if usuario != usuario_a_modificar:
                print(f"El usuario {usuario_a_modificar} no existe.")
            else:
                break
        usuarios[usuarios.index(usuario)] = usuario_nuevo
        print(f"Usuario {usuario_a_modificar} modificado a {usuario_nuevo}.")
        break

def revisar_usuarios():
    print(usuarios)            
                
def eliminar_usuario():
    while True:
        usuario_a_eliminar = input("Ingrese el nombre del usuario: ")
        if usuario_a_eliminar not in usuarios:
            print(f"El usuario {usuario_a_eliminar} no existe.")
        else:
            usuarios.remove(usuario_a_eliminar)
            print(f"Usuario {usuario_a_eliminar} eliminado")
        break        

def menu():
    while True:
        print("Bienvenido al registro de usuarios.")
        print("1. Añadir un usuario")
        print("2. Modificar un usuario")
        print("3. Eliminar un usuario")
        print("4. Revisar usuarios creados")
        print("5. Salir")
        
        eleccion = input("Seleccione una opción: ")
        
        if eleccion == "1":
            print("Eligió añadir un usuario.")
            añadir_usuario()
        elif eleccion == "2":
            print("Eligió modificar un usuario.")
            modificar_usuario()
        elif eleccion == "3":
            print("Eligió eliminar un usuario.")
            eliminar_usuario()
        elif eleccion == "4":
            print("Eligió revisar los usuarios.")
            revisar_usuarios()
        elif eleccion != opciones:
            print("Elija una opción válida!")
        if eleccion == "5":
            print("Eligió salir. Gracias!")
            break

menu()