# utf-8
#####################################################################################################
#   UL_Publisher.py specification                                                                   #   
#                                                                                                   #
#   Metodo que se encarga de publicar el plan de accion al Servidor AMQP.                           #
#                                                                                                   #       
#   INPUT: JSON con las acciones que va a realizar el Rover.                                        #
#   OUTPUT: Print de confirmacion de la publicacion.                                                #
#                                                                                                   #
#   Autor: Daniel Maldonado Salinas <danielmaldonado@correo.ugr.es>                                 #
#####################################################################################################

import sys
from datetime import datetime
from UL_Pika import _connect as open_connection
from UL_Pika import _publish as publish_message

user='rover'
password='Rover2019.'
host='localhost'
vhost='ROVER'
heartbeat=60
exchange='SEND_TO_ROVER_EXCHANGE'
routing_key='rover.movimiento'

with open('movements.json') as f:
  body = f.read()

channel = open_connection(user, password, host, vhost, heartbeat)
publish_message(channel, exchange, routing_key, body)
sys.stdout.write("## PUBLISHED ACTION PLAN AT " + str(datetime.now()) + "\n")
