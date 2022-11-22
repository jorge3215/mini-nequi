class Registro:

    def registro(self):
        print("Resgistro Nequi")
        print("")
        print("REGISTRARSE")
        self.nombre = str(input("Ingrese su nombre: "))
        self.apellidos = str(input("Ingrese sus apellidos: "))
        self.telefono = int(input("Ingrese su numero de telefono: "))
        self.edad = int(input("Ingrese su edad: "))
        self.contraseña = int(input("Ingrese su contraseña: "))
        print("REGISTRO EXITO")
    
class Logueo:

    def logueo(self):
        print("Datos Nequi")
        print("")
        print("Ingrese sus datos:")
        
        contador = 1
        while contador <= 3:
            nuemerotele = int(input ("Telefono: "))
            contraseña = int(input ("Contraseña: "))
            if nuemerotele == self.telefono and contraseña == self.contraseña:
                contador = 4
            else:
                print("Telefono o contraseña incorrecta, intentelo de nuevo.")
                if contador == 3:
                    print("Intentalo mas tarde.")
                    exit()
                contador = contador + 1

class aplicacion(Registro, Logueo):

    def datos(self):
        print("")
        print("BIENVENIDO A LA APLICACION DE NEQUI")
        print("")
        print("Bienvenido a Nequi, señor "f"{self.nombre} {self.apellidos}")
        saldo = 0
        print("Su saldo en este momento es de: $",saldo)
        print("")
        recar = int(input("¿Cuanto desea recargar?: $"))
        print("")
        print("")
        print("¿Que movimiento desea realizar?")
        print("1) Depositar")
        print("2) Retirar")
        print("3) Salir")
        print("")

        movimiento = int(input("Eliga una opcion: "))
        if movimiento == 1:
            cons = int(input(("¿Cuanto desea depositar?, recuerde que su saldo disponible es: $",recar)))
            print("Consignacion exitosa")
            print("Valor consignado: ")
            print("Saldo disponible: ",recar+cons)
            print("")
            print("GRACIAS POR USAR NUESTRA APLICACION")
            exit()
            
        if movimiento == 2:
            reti = int(input(("¿Cuanto desea retirar?, recuerde que su saldo disponible es: $",recar)))
            print("Retiro exitoso")
            print("El valor del retiro fue de: ",reti)
            print("Saldo disponible: ",recar-reti)
            print("")
            print("GRACIAS POR USAR NUESTRA APLICACION")
            exit()
        
        if movimiento == 3:
            print("Vuelva pronto.")
            print("GRACIAS POR USAR NUESTRA APLICACION")     
            exit()

jorgePa = aplicacion()
jorgePa.registro()
jorgePa.logueo()
jorgePa.datos()