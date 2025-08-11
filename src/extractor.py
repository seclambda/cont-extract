# Lógica del extractor

import pyperclip
from re import compile
from humre import exactly, DIGIT # Expresiones regulares legibles para humanos

# Para encontrar patrones en el texto del portapapeles (copy-paste)
text = str(pyperclip.paste())

matches_phone = []
matches_email = []

phone_regex = (exactly(3, DIGIT) + '-'+ exactly(3, DIGIT)  
                + '-' + exactly(4, DIGIT))

pattern = compile(phone_regex)
for number in matches_phone.findall(text):
    print(f"{pattern.search(number)}")

# TO DO: Crear regex para las direacciones de email

