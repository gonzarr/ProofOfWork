#lab06_a1
import os
import re
from hashlib import sha256

def comprueba_expresion_regular(cadena):
    expresion_regular = r"^[0-9a-f]{6}(\t|\s)[0-9a-f]{2}(\t|\s)100$"
    return re.match(expresion_regular, cadena) is not None

directorio = os.listdir(input("Inserta el nombre del directorio: "))
file = open(input("Inserta el nombre del fichero a minar: "),mode='r')

max_ceros = 0
fich_mas_ceros = ""
hashceros = ""

ficheros_correctos = 0
texto1_lista = file.read()

for fichero in directorio:
  file2 = open("Directorio/"+fichero, mode = 'r')
  texto2_lista = file2.read()
  texto_string = "".join(texto2_lista)
  
  
  for i in range(len(texto1_lista)):
    if texto1_lista[i] != texto2_lista[i]:
      print("no coinciden")
      break

  if comprueba_expresion_regular("".join(texto2_lista[len(texto2_lista)-13:len(texto2_lista)])) :
    print("Es correcto")
    ficheros_correctos += 1
    sha256text = sha256(texto_string.encode('utf-8')).hexdigest()
    cont = 0
    for d in sha256text:
      if d == "0":
        cont += 1
      else:
        break
    if cont > max_ceros:
      max_ceros = cont
      fich_mas_ceros = fichero
      hashceros = sha256text
  else:
    print("Es incorrecto")
  file2.close()


print("\nHay " + str(ficheros_correctos) + " ficheros validos de " + str(len(directorio)) + " ficheros entregados.\n")
print("El fichero con más ceros es el: "+fich_mas_ceros+" con " + str(max_ceros) + " ceros y con hash:\n"+hashceros)

file.close()
