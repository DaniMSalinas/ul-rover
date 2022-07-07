#utf-8
#####################################################################################################
#   UL_Controller.py specification                                                                  #   
#                                                                                                   #
#   Metodo que hace de soporte al UL_Publisher.py y que se encarga de la interaccion con            #
#   el servidor AMQP instalado en la propia maquina virtual.                                        #
#                                                                                                   #       
#   Autor: Daniel Maldonado Salinas <danielmaldonado@correo.ugr.es>                                 #
#####################################################################################################

import pika

def _connect(_user, _password, _host, _vhost, _heartbeat):
    credentials = pika.PlainCredentials(_user, _password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=_host, credentials=credentials, virtual_host=_vhost, heartbeat=_heartbeat))
    return connection.channel()

def _publish(_channel, _exchange, _routing_key, _body):
    _channel.basic_publish(_exchange, _routing_key, _body, properties=None, mandatory=False)