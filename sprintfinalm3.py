import random
import string

usuarios = ["Usuario1", "Usuario2", "Usuario3", "Usuario4", "Usuario5", "Usuario6", "Usuario7", "Usuario8", "Usuario9", "Usuario10"]

#Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).

for usuario in usuarios:
    print(usuario)

# Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def nueva_cuenta(usuarios):
    cuentas = {}
    for usuario in usuarios:
        contraseña = password()
        telefono = numerotelefono(usuario)
        cuentas[usuario] = {'contraseña': contraseña, 'teléfono': telefono}
    return cuentas
    

#Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
def password():
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(8))
    return contraseña

#El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un número de contacto asignado.
def numerotelefono(usuario):
    while True:
        telefono = input(f"Por favor {usuario} ingrese su número de teléfono de 8 dígitos: ")
        if len(telefono) == 8 and telefono.isdigit():
            return telefono
        else:
            print("El número de teléfono debe tener 8 dígitos")


cuentas_usuarios = nueva_cuenta(usuarios)

#finalmente se devolveran las cuentas de usuario
for usuario, cuenta in cuentas_usuarios.items():
    print(f"Cuenta de {usuario}:")
    print(f"Contraseña: {cuenta['contraseña']}")
    print(f"Teléfono: {cuenta['teléfono']}")
    print()