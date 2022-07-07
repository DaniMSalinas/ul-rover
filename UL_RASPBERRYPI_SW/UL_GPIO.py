#utf-8
#####################################################################################################
#   UL_GPIO.py specification                                                                        #   
#                                                                                                   #
#   Este metodo se encarga puramente de la interaccion con los motores del Rover a traves del       #
#   controlador GPIO de la raspberry y esta controlado                                              #
#   por UL_MASTER.                                                                                  #
#                                                                                                   #       
#   INPUT: comando que indique el modo de movimiento y la velocidad a la que lo ejecuta             #
#   OUTPUT: movimiento del rover                                                                    #
#                                                                                                   #
#   Autor: Daniel Maldonado Salinas <danielmaldonado@correo.ugr.es>                                 #
#####################################################################################################

from gpiozero import PWMLED, MCP3008

# Limpieza del uso de pines en el módulo SPi al iniciar el sw
PWMLED(4).close()
PWMLED(17).close()
PWMLED(27).close()
PWMLED(22).close()
PWMLED(24).close()
PWMLED(25).close()
PWMLED(5).close()
PWMLED(6).close()
PWMLED(12).close()
PWMLED(13).close()
PWMLED(16).close()
PWMLED(19).close()
PWMLED(18).close()
PWMLED(23).close()
PWMLED(20).close()
PWMLED(21).close()

## motores de la derecha
HG7881_B_IA = PWMLED(4) #E1
HG7881_B_IB = PWMLED(17) #E2

MOTOR_B_PWM = HG7881_B_IA 
MOTOR_B_DIR = HG7881_B_IB 

HG7881_B_IA2 = PWMLED(27) #E3
HG7881_B_IB2 = PWMLED(22) #E4
 
MOTOR_B_PWM2 = HG7881_B_IA2 
MOTOR_B_DIR2 = HG7881_B_IB2 

## motores de la izquierda
HG7881_B_IA3 = PWMLED(24) #E1
HG7881_B_IB3 = PWMLED(25) #E2

MOTOR_B_PWM3 = HG7881_B_IA3 
MOTOR_B_DIR3 = HG7881_B_IB3 

HG7881_B_IA4 = PWMLED(5) #E3
HG7881_B_IB4 = PWMLED(6) #E4

MOTOR_B_PWM4 = HG7881_B_IA4
MOTOR_B_DIR4 = HG7881_B_IB4

## motor de movimiento delanteros
HG7881_B_IA5 = PWMLED(12) 
HG7881_B_IB5 = PWMLED(13) 

MOTOR_B_PWM5 = HG7881_B_IA5 
MOTOR_B_DIR5 = HG7881_B_IB5 

## motor de movimiento traseros
HG7881_B_IA6 = PWMLED(16) 
HG7881_B_IB6 = PWMLED(19)

MOTOR_B_PWM6 = HG7881_B_IA7 
MOTOR_B_DIR6 = HG7881_B_IA7 

## motor de giro delantero
HG7881_B_IA7 = PWMLED(18)
HG7881_B_IB7 = PWMLED(23)

MOTOR_B_PWM7 = HG7881_B_IA7 
MOTOR_B_DIR7 = HG7881_B_IA7 

## motor de giro trasero
HG7881_B_IA8 = PWMLED(20)
HG7881_B_IB8 = PWMLED(21)

MOTOR_B_PWM8 = HG7881_B_IA8 
MOTOR_B_DIR8 = HG7881_B_IB8 


## potenciometro delantero
POT_FRONT = MCP3008(0)
POT_BACK = MCP3008(3)


## INITIAL PINOUT SETUP ##
MOTOR_B_PWM.off()
MOTOR_B_DIR.off()

MOTOR_B_PWM2.off()
MOTOR_B_DIR2.off()

MOTOR_B_PWM3.off()
MOTOR_B_DIR3.off()

MOTOR_B_PWM4.off()
MOTOR_B_DIR4.off()

MOTOR_B_PWM5.off()
MOTOR_B_DIR5.off()

MOTOR_B_PWM6.off()
MOTOR_B_DIR6.off()

MOTOR_B_PWM7.off()
MOTOR_B_DIR7.off()

MOTOR_B_PWM8.off()
MOTOR_B_DIR8.off()


## Operaciones con motores de la derecha
def forward_right_motors(PWM_SPEED):
    MOTOR_B_DIR.off()
    MOTOR_B_PWM.value = PWM_SPEED / 100

    MOTOR_B_DIR2.off()
    MOTOR_B_PWM2.value = PWM_SPEED / 100
    return 0

def backward_right_motors(PWM_SPEED):
    MOTOR_B_PWM.value = PWM_SPEED / 100
    MOTOR_B_DIR.off()

    MOTOR_B_PWM2.value = PWM_SPEED / 100
    MOTOR_B_DIR2.off()
    return 0

def stop_right_motors():
    MOTOR_B_PWM.off()
    MOTOR_B_DIR.off()
    
    MOTOR_B_PWM2.off()
    MOTOR_B_DIR2.off()
    return 0


## operaciones con motores de la izquierda
def forward_left_motors(PWM_SPEED):
    MOTOR_B_DIR3.off()
    MOTOR_B_PWM3.value = PWM_SPEED / 100

    MOTOR_B_DIR4.off()
    MOTOR_B_PWM4.value = PWM_SPEED / 100
    return 0

def backward_left_motors(PWM_SPEED):
    MOTOR_B_PWM3.value = PWM_SPEED / 100
    MOTOR_B_DIR3.off()

    MOTOR_B_PWM4.value = PWM_SPEED / 100
    MOTOR_B_DIR4.off()
    return 0

def stop_left_motors():
    MOTOR_B_PWM3.off()
    MOTOR_B_DIR3.off()
    
    MOTOR_B_PWM4.off()
    MOTOR_B_DIR4.off()
    return 0

## operaciones con motor frontal
def forward_front_motors(PWM_SPEED):
    MOTOR_B_DIR5.off()
    MOTOR_B_DIR5.value = PWM_SPEED / 100
    return 0

def backward_front_motors(PWM_SPEED):
    MOTOR_B_PWM5.value = PWM_SPEED / 100
    MOTOR_B_DIR5.off()
    return 0

def stop_front_motors():
    MOTOR_B_PWM5.off()
    MOTOR_B_DIR5.off()
    return 0

## operaciones con motor trasero
def forward_back_motors(PWM_SPEED):
    MOTOR_B_DIR6.off()
    MOTOR_B_DIR6.value = PWM_SPEED / 100
    return 0

def backward_back_motors(PWM_SPEED):
    MOTOR_B_PWM6.value = PWM_SPEED / 100
    MOTOR_B_DIR6.off()
    return 0

def stop_back_motors():
    MOTOR_B_PWM6.off()
    MOTOR_B_DIR6.off()
    return 0

## operaciones con motor de giro delantero
def move_hour_front_motor():
    MOTOR_B_DIR7.on()
    MOTOR_B_PWM7.off()
    return 0

def move_antihour_front_motor():
    MOTOR_B_DIR7.off()
    MOTOR_B_PWM7.on()
    return 0

def stop_spin_front_motor():
    MOTOR_B_DIR7.off()
    MOTOR_B_PWM7.off()
    return 0

## operaciones con motor de giro trasero
def move_hour_back_motor():
    MOTOR_B_DIR8.on()
    MOTOR_B_PWM8.off()
    return 0

def move_antihour_back_motor():
    MOTOR_B_DIR8.off()
    MOTOR_B_PWM8.on()
    return 0

def stop_spin_back_motor():
    MOTOR_B_DIR8.off()
    MOTOR_B_PWM8.off()
    return 0


## movimiento de sets de motores
def move_forward(PWM_SPEED):
    forward_front_motors(PWM_SPEED)
    forward_back_motors(PWM_SPEED)
    forward_right_motors(PWM_SPEED)
    forward_left_motors(PWM_SPEED)
    return 0

def move_reverse(PWM_SPEED):
    backward_front_motors(PWM_SPEED)
    backward_back_motors(PWM_SPEED)
    backward_right_motors(PWM_SPEED)
    backward_left_motors(PWM_SPEED)
    return 0

def move_turn_right(grades):
    move_hour_front_motor()
    move_antihour_back_motor()

    while True:
        if (POT_FRONT == 0.5 + grades_pot):
            stop_spin_front_motor()
            stop_spin_back_motor()
            break

    return 0

def move_turn_left(grades):
    grades_pot = (grades*0.025)
    grades_pot = grades_pot / 75
    move_antihour_front_motor()
    move_hour_back_motor()

    while True:
        if (POT_BACK == 0.5 + grades_pot):
            stop_spin_front_motor()
            stop_spin_back_motor()
            break
    return 0

def stop():
    stop_front_motors()
    stop_back_motors()
    stop_left_motors()
    stop_right_motors()
    return 0

def switch(mode, speed):
    return {
        'forward': lambda val: move_forward(mode, speed),
        'reverse': lambda val: move_reverse(mode, speed),
        'turn_right': lambda val: move_turn_right(mode),
        'turn_left': lambda val: move_turn_left(mode),
        'stop': lambda val: stop()
    }.get(mode)(speed)