from importlib.resources import path
import os


# base del disco duro
base_dir = 'C:/Users'

# posibles usuarios
path = os.listdir(base_dir)
print(path)

# emulo comando por voz
say_something = "Juan David Ruiz"

usuario = ''
# busco elemento en lista
for i in path:
    if i == say_something:
        usuario = i

#path real
path = os.path.realpath(base_dir+'/'+usuario)

print(path)

#abro directorio-carpeta
os.startfile(path)

#SE DEBE PEDIR AL USUARIO CADA DIRECTORIO O ROOT PARA LLEGAR AL ESCRITORIO
#O A LAS CARPETAS PRINCIPAL COMO ONEDRIVE O DESKTOP
