import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
extencion = int(input("Cuantos caracteres deseas que tenga su contraseña:"))
contrasena = ""

for i in range (extencion):
    contrasena+= random.choice(caracteres)
print(contrasena)
