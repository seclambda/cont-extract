# Lógica del script
import re
import pyperclip

# Obtener texto del portapapeles
text = pyperclip.paste()

# Expresión regular para los números telefónicos
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?       # Código de área (grupo 2)
    (\s|-|\.)?               # Separador (grupo 3)
    (\d{3})                  # Primeros 3 dígitos (grupo 4)
    (\s|-|\.)                # Separador (grupo 5)
    (\d{4})                  # Últimos 4 dígitos (grupo 6)
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extensión (grupo 7, 8 y 9)
)''', re.VERBOSE)

#To-Do Crear expresión regular para los correos electronicos y 
# crear un bucle para encontrar los patrones
email_regex = re,compile()

matches_phone = []  # Lista para almacenar los números encontrados

for match in phone_regex.findall(text):
   
    # To-do: Limpia el código de área (es decir quita paréntesis)
    if match[1]:
        area_code = match[1].replace('(', '').replace(')', '') 
    else:
        area_code = ''
    # Construye el número base
    if area_code:
        phone_num = '-'.join([area_code, match[3], match[5]])
    else:
        phone_num = '-'.join([match[3], match[5]])
    
    # Se agrega la extensión si existe (El grupo 9 contiene los dígitos de extensión)
    if match[8]:
        phone_num += ' x' + match[8]
    
    matches_phone.append(phone_num)

# Salidas
if matches_phone:
    result = '\n'.join(matches_phone)
    pyperclip.copy(result)
    print('Números encontrados:')
    print(result)
else:
    print('Ningún número de teléfono fue encontrado.')

