from datetime import datetime

def time():
    return datetime.now().strftime("%H:%M:%S")

def today():
    return datetime.now().strftime("%d/%m/%Y")

def datahora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

"""
_______________________________________
import date

// data
nome = date.datahora()
post(nome)

// time
nome = date.time()
post(nome)

// today
nome = date.today()
post(nome)

# ou inves de post() usar return nome
________________________________________

// ou importando o metodo

import date
from date import time, today, datahora

nome = time()

nome = today()

nome = datahora()
________________________________________
"""