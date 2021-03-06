# -*- coding:utf-8 -*-
import sys

import redis
from metodos import sendMessage
import config
from plug.ia import conversa
from plug import banhammer,comands,myid,newmember,printar,promover,start,tradutor,regras,qr

''' caso você use linux, mantenha o sisteminha encode abaixo...'''

## default encoding
reload(sys)
sys.setdefaultencoding('utf8')

### redis server
redis = redis.StrictRedis(host=config.redis['host'], port=config.redis['port'], db=config.redis['db'])

### plugins
def comandos(msg):
    if 'text' in msg:

        if msg['text'].startswith('/run'):
            if msg['from']['id'] == config.sudo:
                cmd = msg['text'].replace('/run ','')
                redis.hset('run', 'status', '{}'.format(cmd))
                sendMessage(msg['chat']['id'], 'Alterando as configurações para *{}*'.format(cmd),"markdown")
                return

        if redis.hgetall('run')['status'] == 'on':

            regras.regras(msg) # modulo de regras

            myid.my_id(msg) # modulo do comando /id

            newmember.welcome(msg) # modulo de boas vindas

            promover.promover(msg) # mudulo de divulgação

            start.start(msg) # modulo de inicialização

            banhammer.banhammer(msg) # modulo de administração

            printar.printar(msg) # modulo do comando /print

            comands.comands(msg) # modulo do comando /comandos

            conversa(msg) # modulo de inteligencia artificial

            tradutor.traduzir(msg) #modulo de tradução

            qr.make_qr(msg) #  modulo co comando /qr
