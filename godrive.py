import os
import requests
import time
import sys
import subprocess
from datetime import datetime
from requests import get
import pathlib

# Parametros
localDir = str(pathlib.Path(__file__).parent.resolve())
execSh = localDir + '/godrive.sh'
# execSh = localDir + '/sleep.sh'
cloud = 'GoDrive'
chat = '-111111111111111111' # Grupo
bot='bot2075967130:ddddddddddddddddddddddddddddddddddddddd' #CRIAR BOT

def sendTel(chatMsg):
    params = (
            ('chat_id', chat),
            ('text', chatMsg),
        )

    url = 'https://api.telegram.org/{}/sendmessage'.format(bot)
    response = requests.get(url, params=params)

start = datetime.now()
inicio = cloud + ' iniciou: ' + str(start)[:-7]
sendTel(inicio)

rc = subprocess.call(execSh)

depois = datetime.now()
termino = cloud + ' terminou: ' + str(depois)[:-7]

sendTel(termino)
duracao = str(depois - start)[:-7]

finalizou = cloud + ' duração: ' + duracao
# sendTel(finalizou)

try:
    if rc == 0:
        print('Backup ' + cloud + ' Finalizado!')
        sendTel(finalizou)
except:
    error = 'Verificar a chamada do script!'
    print(error)
    sendTel(error)
    sys.exit(0)
