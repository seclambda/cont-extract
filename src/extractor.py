# Lógica del script
import re
import re
from typing import Tuple, List

class DataExtractor:
    def __init__(self):
        # Regex para los telefonos
        self.phone_regex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?       # Código de área (grupo 2)
            (\s|-|\.)?               # Separador (grupo 3)
            (\d{3})                  # Primeros 3 dígitos (grupo 4)
            (\s|-|\.)                # Separador '' (grupo 5)
            (\d{4})                  # Últimos 4 dígitos (grupo 6)
            (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extensión (grupo 7, 8 y 9)
        )''', re.VERBOSE)
        # regex para los correos electronicos
        self.email_regex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+       # Nombre de usuario
            @                       # Simbolo arroba @
            [a-zA-Z0-9.-]+          # Nombre de dominio
            (\.[a-zA-Z]{2,4})       # .es .com etc  
        )''', re.VERBOSE)

    def extract_phones(self, text: str) -> List[str]:
        """Extrae números de teléfono del texto proporcionado"""
        matches = []
        for match in self.phone_regex.findall(text):
            if match[1]:
                area_code = match[1].replace('(', '').replace(')', '')
            else:
                area_code = ''
                
            phone_num = '-'.join([area_code, match[3], match[5]]) if area_code else '-'.join([match[3], match[5]])
            
            if match[8]:
                phone_num += ' x' + match[8]
            
            matches.append(phone_num)
        return matches

    def extract_emails(self, text: str) -> List[str]:
        """Extrae direcciones de email del texto proporcionado"""
        return [email[0] for email in self.email_regex.findall(text)]

    def extract_all(self, text: str) -> Tuple[List[str], List[str]]:
        """Extrae tanto teléfonos como los correos de una vez """
        return (self.extract_phones(text), self.extract_emails(text))
