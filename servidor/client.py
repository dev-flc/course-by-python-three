clients = "fernando, arlette, "


def crear_cliente(name):
    # accedemos a la variable global clients
    global clients
    if name not in clients:
        clients += name
        _add_comma()
    else:
        print("el cliente ya existe")

def list_clients():
    global clients
    print( ">", clients )


def _add_comma():
    global clients
    clients += ","

def _print_welcome():
    print("*"*50)
    print("WELCOME FOREVER TU CODE")
    print("*"*50)
    print("que quieres hacer")
    print("[A] crear un cliente")
    print("[B] eliminar cliente")


if __name__ == "__main__":
    #list_clients()
    #crear_cliente("fer")
    #list_clients()
    _print_welcome()
    command = input()

    if command == "A":
        client_name = input('Cual es el nombre del cliente >  ')
        crear_cliente(client_name)
        list_clients()
    elif command == "B":
        pass
    else:
        print("El comando es invalido")