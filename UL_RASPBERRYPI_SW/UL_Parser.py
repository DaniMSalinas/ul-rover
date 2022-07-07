#utf-8
#####################################################################################################
#   UL_Pika.py specification                                                                        #   
#                                                                                                   #
#   Este metodo esta bajo el control del UL_Master y se encarga de parsear los mensajes en formato  #
#   JSON para transformarlos en senales I/O que se usaran para controlar la GPIO de la raspberry    #
#   y asi ejecutar los movimientos del rover.                                                       #
#                                                                                                   #       
#   INPUT: input el json que le da el UL_MASTER para que parsee.                                    #
#   OUTPUT: comando que devuelve para que el UL_MASTER se lo pase a los motores del rover.          #
#                                                                                                   #
#   Autor: Daniel Maldonado Salinas <danielmaldonado@correo.ugr.es>                                 #
##################################################################################################### 

from UL_GPIO import switch
import json
from collections import OrderedDict
import time

def command_parser(input_json):
    json_parsed = json.loads(input_json, object_pairs_hook = OrderedDict)

    for movement in json_parsed:
        speed = 0
        grades = 0

        if json_parsed[movement]['action'] == "move_forward":
            action = "forward"
            speed = json_parsed[movement]["speed"]
        elif json_parsed[movement]["action"] == "move_reverse":
            action = "reverse"
            speed = json_parsed[movement]["speed"]
        elif json_parsed[movement]["action"] == "turn_right":
            action = "turn_right"
            grades = json_parsed[movement]["grades"]
        elif json_parsed[movement]["action"] == "turn_left":
            action = "turn_left"
            grades = json_parsed[movement]["grades"]
        elif json_parsed[movement]["action"] == "stop":
            action = "stop"

        if (speed != 0 and grades == 0):
            if (speed > 100):
                speed = 100
            if (speed < 0):
                speed = 0
            switch(action, speed)
            time.sleep(json_parsed[movement]["time_to_wait"])
            switch("soft_stop")
        elif (speed == 0 and grades != 0):
            if (grades > 75):
                grades = 75
            if (grades < -75):
                grades = -75
            switch(action, grades)
        elif (speed == 0 and grades == 0):
            switch(action)  

