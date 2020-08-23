from logicaCartas import logicaCartas
from flask import Flask, jsonify
import random
import msvcrt
import json

class ejecucionSistemaControl:

    def __init__(self):
        self.barajaJson = 'baraja.json'
        self.barajaManoJson = 'barajaMano.json'

    api = Flask(__name__)
   
    @api.route("/deck/new", methods = ['GET'])
    def mCrearBaraja():

        cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        tipos = ["♣","♥","♠","♦"]
        baraja = []
        barajaMano = []

        for carta in cartas:        #Se crea un ciclo para que recorra las dos listas de cartas y tipos
            for tipo in tipos:      #va creando una carta de cata tipo
                cartajson = {"carta": "{}".format(carta),"tipo": "{}".format(tipo)}
                baraja.append(cartajson)    #Se crea una carta en formato json y se guarda en una lista de json
            
        with open ('baraja.json', "w") as paqueteCartas:    #Se abre el archivo de baraja json y se guarda
            json.dump(baraja, paqueteCartas, indent=4)

        
        with open ('barajaMano.json', "w") as paqueteCartas:    #Se abre el archivo de baraja en mano json y se guarda
            json.dump(barajaMano, paqueteCartas, indent=4)      #y se inicializa cada vez que se crea una nueva baraja

        maso = []               #Se crea una presentación para mostrar en html las cartas creadas
        for carta in baraja:
            cartajson = ("{}{}".format(carta.get('carta'),carta.get('tipo')))
            maso.append(cartajson)

        return '<h3>BARAJA CREADA</h3> \n <h5>{}</h5>'.format(maso)


    @api.route("/deck/shuffle", methods = ['GET'])
    def mCartasShuffle():

        with open ('baraja.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas)

        if(len(paquete)>0):
            random.shuffle(paquete) #Se valida que existan cartas y se revuelven
            
            with open ('baraja.json', "w") as paqueteCartas: #Luego se vuelve a abrir el archivo para guardar
                json.dump(paquete, paqueteCartas, indent=4)
            
            maso = []               #Se crea una presentación para mostrar en html las cartas revueltas
            for carta in paquete:
                cartajson = ("{}{}".format(carta.get('carta'),carta.get('tipo')))
                maso.append(cartajson)

            return '<h3>BARAJANDO CARTAS</h3> \n <h5>{}</h5>'.format(maso)
        else:
            return '<h3>NO QUEDAN CARTAS DISPONIBLES</h3>'


    @api.route("/deck/show/remain", methods = ['GET'])
    def mCargarCartasNuevas():

        with open ('baraja.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas) 

        if(len(paquete)>0):     #Se valida que existan cartas y se trabajan

            maso = []               #Se crea una presentación para mostrar en html las cartas en la baraja
            for carta in paquete:
                cartajson = ("{}{}".format(carta.get('carta'),carta.get('tipo')))
                maso.append(cartajson)
            return '<h3>CARTAS DISPONIBLES</h3> \n <h5>{}</h5>'.format(maso)
        else:
            return '<h3>NO QUEDAN CARTAS DISPONIBLES</h3>'


    @api.route("/user/show/hand", methods = ['GET'])
    def mCargarCartasTomadas():
        with open ('barajaMano.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas)    

            if(len(paquete)>0):     #Se valida que existan cartas y se trabajan

                maso = []               #Se crea una presentación para mostrar en html las cartas en la mano
                for carta in paquete:
                    cartajson = ("{}{}".format(carta.get('carta'),carta.get('tipo')))
                    maso.append(cartajson)
                return '<h3>CARTAS EN MANO</h3> \n <h5>{}</h5>'.format(maso)
            else:
                return '<h3>NO HAS TOMADO NINGUNA CARTA</h3>'
    

    @api.route("/deck/pickone", methods = ['GET'])
    def mTomarCartas():

        with open ('baraja.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas)
            
            if(len(paquete)>0):         #Se valida que existan cartas y se realiza un POP que elimina la primera carta
                cambio = paquete.pop(0) #es decir la que esta arriba de la baraja

                with open ('baraja.json', "w") as paqueteCartas:    #Guardamos en el json baraja la nueva baraja es decir
                    json.dump(paquete, paqueteCartas, indent=4)     #eliminando el dato que acabamos de tomar

                with open ('barajaMano.json') as paqueteCartas:     #Guardamos en el jason Baraja en Mano los valores que
                    paquete.append(cambio)                          #ya tenía más el valor que acabamos de tomar del otro  
                                                                    #archivo json
                with open ('barajaMano.json', "w") as paqueteCartas: 
                    json.dump(paquete, paqueteCartas, indent=4)

                return '<h3>HA TOMADO UNA CARTA</h3> \n <h5> Carta tomada → {}{}</h5>'.format(cambio.get('carta'),cambio.get('tipo'))
            else:
                return '<h3>NO QUEDAN CARTAS DISPONIBLES</h3>'

    @api.route("/user/play", methods = ['GET'])
    def mVerificarJuego():
        with open ('barajaMano.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas) 
        
        variableReturn = ''     #Se crea un objeto para almacenar y concatenar el return
        bEscaleraReal = False   #ademas de otras variables que se utilizan en la logica de
        bEscaleraColor = False  #la validacion de jugadas de poker
        bPoker = False
        bFull = False
        bColor = False
        bEscalera = False
        bTrio = False
        bDoblePar = False
        bPar1 = False

        if(len(paquete) > 0):               #Algoritmo creado para validar la existencia de Poker
                                            #trios, par o doble par
            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="A"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="2"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="3"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="4"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="5"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="6"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="7"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="8"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="9"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="10"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="J"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="Q"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0
            for carta in paquete:
                if(carta.get('carta')=="K"):
                    contador = contador + 1
            if contador == 4:
                bPoker = True
            if contador >= 3:
                bTrio = True
            if contador >= 2:
                if(bPar1 == True):
                    bDoblePar = True
                else:
                    bPar1 = True

            contador = 0                    #Algoritmo creado para validar la existencia de Colores
            for carta in paquete:
                if(carta.get('tipo')=="♣"):
                    contador = contador + 1
                if(contador == 5):
                    bColor = True

            contador = 0
            for carta in paquete:
                if(carta.get('tipo')=="♥"):
                    contador = contador + 1
                if(contador == 5):
                    bColor = True

            contador = 0
            for carta in paquete:
                if(carta.get('tipo')=="♠"):
                    contador = contador + 1
                if(contador == 5):
                    bColor = True

            contador = 0
            for carta in paquete:
                if(carta.get('tipo')=="♦"):
                    contador = contador + 1
                if(contador == 5):
                    bColor = True

            for carta in paquete:   #Algoritmo creado para validar la existencia de Escalera Real
                if(carta.get('carta')=="A" and carta.get('tipo')=="♥"):
                    for carta in paquete:
                        if(carta.get('carta')=="K" and carta.get('tipo')=="♥"):
                            for carta in paquete:
                                if(carta.get('carta')=="Q" and carta.get('tipo')=="♥"):
                                    for carta in paquete:
                                        if(carta.get('carta')=="J" and carta.get('tipo')=="♥"):
                                            for carta in paquete:
                                                if(carta.get('carta')=="10" and carta.get('tipo')=="♥"):
                                                    bEscaleraReal = True
            
            if(bEscaleraReal == True):  #Validaciones de booleanos para concatenar los resultados
                variableReturn = variableReturn +"Escalera Real →\n"
            if(bEscaleraColor == True):
                variableReturn = variableReturn +"Escalera Color →\n"
            if(bPoker == True):
                variableReturn = variableReturn +"Poker →\n"
            if(bColor == True):
                variableReturn = variableReturn +"Color →\n"
            if(bEscalera == True):
                variableReturn = variableReturn +"Escalera →\n"


            if(bTrio == True):          #Valida TRIO y FULL
                if(bPar1 == True):
                    bFull = True
                    bPar1 = False
                    if(bFull == True):
                        variableReturn = variableReturn +"Full →\n"
                else:
                    variableReturn = variableReturn +"Trio →\n"



            if(bDoblePar == True):      #Valida PAR y DOBLE PAR
                variableReturn = variableReturn +"Doble Par →\n"
            else:
                if(bPar1 == True):
                    variableReturn = variableReturn +"Par →\n"

        else:
            variableReturn = variableReturn +"No hay cartas en mano \n"

        return '<h3>Jugadas en mano</h3> \n <h5>{}</h5>'.format(variableReturn)