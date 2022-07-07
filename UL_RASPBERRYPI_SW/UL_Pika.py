#utf-8
#####################################################################################################
#   UL_Controller.py specification                                                                  #   
#                                                                                                   #
#   Metodo que esta bajo el control del metodo UL_MASTER y que se encarga de la interaccion con     #
#   el servidor AMQP instalado en la propia placa. Una vez que el servidor recibe los mensajes del  #
#   cloud es este metodo quien consume esos mensajes y se los devuelve al metodo UL_MASTER para     # 
#   para que los trate.                                                                             #
#                                                                                                   #       
#   Autor: Daniel Maldonado Salinas <danielmaldonado@correo.ugr.es>                                 #
#####################################################################################################

import sys
from datetime import datetime
import pika

def _connect(_user, _password, _host, _vhost, _heartbeat):
    credentials = pika.PlainCredentials(_user, _password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=_host, credentials=credentials, virtual_host=_vhost, heartbeat=_heartbeat))
    return connection.channel()

def _consume(_callback, _channel, _queue, _consumer_tag):
    _channel.basic_consume(_queue, _callback, False, False, _consumer_tag)
    sys.stdout.write("## ROVER Ready to receive messages at " + str(datetime.now()) + "\n")
    _channel.start_consuming()