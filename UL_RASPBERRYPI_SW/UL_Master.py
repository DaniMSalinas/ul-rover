# utf-8
#####################################################################################################
#   UL_Master.py specification                                                                      #   
#                                                                                                   #
#   Modulo principal del rover que se encarga de orquestar la recepcion de mensajes por parte       #
#   del cloud para parsearlo y convertirlo en comandos que se ejecutan en el rover.                 #
#   Esta clase sera un servicio del propio sistema operativo que se iniciará cuando se arranque la  #
#   propia placa y loggeara todo lo que pasa en el rover.                                           #
#                                                                                                   #       
#   INPUT: mensajes que llegan del cloud para que sean parseados y traducidos a comandos            #
#   OUTPUT: movimiento del rover                                                                    #
#                                                                                                   #
#   Autor: Daniel Maldonado Salinas <danielmaldonado@correo.ugr.es>                                 #
#####################################################################################################


from UL_Pika import _connect as open_connection
from UL_Pika import _consume as start_consuming
from UL_Parser import command_parser

user='rover'
password='Rover2019.'
host='localhost'
vhost='ROVER'
heartbeat=60
queue='GPIO_COMMANDS'
consumer_tag='rover_client'

def callback_function(channel, method, properties, body):
    sys.stdout.write("# Message received at: " + str(datetime.now()) + "\n")
    command_parser(body)
    channel.basic_ack(method.delivery_tag)
    
channel = open_connection(user, password, host, vhost, heartbeat)
start_consuming(callback_function, channel, queue, consumer_tag)