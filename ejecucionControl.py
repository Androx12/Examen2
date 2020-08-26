from flask import Flask, jsonify, render_template
import random
import msvcrt
import json

class ejecucionSistemaControl:

    def __init__(self):
        self.barajaJson = 'baraja.json'
        self.barajaManoJson = 'barajaMano.json'

    api = Flask(__name__)
   
   
    @api.route("/", methods = ['GET'])
    def mInicio():
        return render_template("nuevo.html")

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

        link1 = "window.location.href='http://127.0.0.1:5000/deck/new'"
        link2 = "window.location.href='http://127.0.0.1:5000/deck/shuffle'"
        link3 = "window.location.href='http://127.0.0.1:5000/deck/show/remain'"
        link4 = "window.location.href='http://127.0.0.1:5000/deck/pickone'"
        link5 = "window.location.href='http://127.0.0.1:5000/user/show/hand'"
        link6 = "window.location.href='http://127.0.0.1:5000/user/play'"
        link7 = "window.location.href='http://127.0.0.1:5000'"

        return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> BARAJA CREADA </H1><H3>{}</H3><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button></div><button class='C1' onclick={}>Menú Principal</button></div>".format(maso,link1, link2, link3, link4, link5, link6, link7)


    @api.route("/deck/shuffle", methods = ['GET'])
    def mCartasShuffle():

        link1 = "window.location.href='http://127.0.0.1:5000/deck/new'"
        link2 = "window.location.href='http://127.0.0.1:5000/deck/shuffle'"
        link3 = "window.location.href='http://127.0.0.1:5000/deck/show/remain'"
        link4 = "window.location.href='http://127.0.0.1:5000/deck/pickone'"
        link5 = "window.location.href='http://127.0.0.1:5000/user/show/hand'"
        link6 = "window.location.href='http://127.0.0.1:5000/user/play'"
        link7 = "window.location.href='http://127.0.0.1:5000'"

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

            return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> Revolviendo Baraja... </H1><H3>{}</H3><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div></div>".format(maso,link1, link2, link3, link4, link5, link6, link7)
        else:
            return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> No hay cartas para revolver </H1><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div></div>".format(link1, link2, link3, link4, link5, link6, link7)


    @api.route("/deck/show/remain", methods = ['GET'])
    def mCargarCartasNuevas():

        link1 = "window.location.href='http://127.0.0.1:5000/deck/new'"
        link2 = "window.location.href='http://127.0.0.1:5000/deck/shuffle'"
        link3 = "window.location.href='http://127.0.0.1:5000/deck/show/remain'"
        link4 = "window.location.href='http://127.0.0.1:5000/deck/pickone'"
        link5 = "window.location.href='http://127.0.0.1:5000/user/show/hand'"
        link6 = "window.location.href='http://127.0.0.1:5000/user/play'"
        link7 = "window.location.href='http://127.0.0.1:5000'"

        with open ('baraja.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas) 

        if(len(paquete)>0):     #Se valida que existan cartas y se trabajan

            maso = []               #Se crea una presentación para mostrar en html las cartas en la baraja
            for carta in paquete:
                cartajson = ("{}{}".format(carta.get('carta'),carta.get('tipo')))
                maso.append(cartajson)
            return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> Cartas Disponibles </H1><H3>{}</H3><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div></div>".format(maso,link1, link2, link3, link4, link5, link6, link7)
        else:
            return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> No hay cartas disponibles </H1><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div></div>".format(link1, link2, link3, link4, link5, link6, link7)


    @api.route("/user/show/hand", methods = ['GET'])
    def mCargarCartasTomadas():

        link1 = "window.location.href='http://127.0.0.1:5000/deck/new'"
        link2 = "window.location.href='http://127.0.0.1:5000/deck/shuffle'"
        link3 = "window.location.href='http://127.0.0.1:5000/deck/show/remain'"
        link4 = "window.location.href='http://127.0.0.1:5000/deck/pickone'"
        link5 = "window.location.href='http://127.0.0.1:5000/user/show/hand'"
        link6 = "window.location.href='http://127.0.0.1:5000/user/play'"
        link7 = "window.location.href='http://127.0.0.1:5000'"

        with open ('barajaMano.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas)    

            if(len(paquete)>0):     #Se valida que existan cartas y se trabajan

                maso = []               #Se crea una presentación para mostrar en html las cartas en la mano
                for carta in paquete:
                    cartajson = ("{}{}".format(carta.get('carta'),carta.get('tipo')))
                    maso.append(cartajson)
                return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> Cartas en Mano... </H1><H3>{}</H3><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div></div>".format(maso,link1, link2, link3, link4, link5, link6, link7)
            else:
                return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> No has tomado ninguna carta </H1><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div></div>".format(link1, link2, link3, link4, link5, link6, link7)
    

    @api.route("/deck/pickone", methods = ['GET'])
    def mTomarCartas():

        link1 = "window.location.href='http://127.0.0.1:5000/deck/new'"
        link2 = "window.location.href='http://127.0.0.1:5000/deck/shuffle'"
        link3 = "window.location.href='http://127.0.0.1:5000/deck/show/remain'"
        link4 = "window.location.href='http://127.0.0.1:5000/deck/pickone'"
        link5 = "window.location.href='http://127.0.0.1:5000/user/show/hand'"
        link6 = "window.location.href='http://127.0.0.1:5000/user/play'"
        link7 = "window.location.href='http://127.0.0.1:5000'"

        with open ('baraja.json') as paqueteCartas: #Se abre el archivo de baraja json para manipular los datos
            paquete = json.load(paqueteCartas)
            
            if(len(paquete)>0):         #Se valida que existan cartas y se realiza un POP que elimina la primera carta
                cambio = paquete.pop(0) #es decir la que esta arriba de la baraja

                with open ('baraja.json', "w") as paqueteCartas:    #Guardamos en el json baraja la nueva baraja es decir
                    json.dump(paquete, paqueteCartas, indent=4)     #eliminando el dato que acabamos de tomar

                with open ('barajaMano.json') as paqueteCartas:     #Guardamos en el jason Baraja en Mano los valores que
                    paquete = json.load(paqueteCartas)
                    paquete.append(cambio)                          #ya tenía más el valor que acabamos de tomar del otro  
                                                                    #archivo json
                with open ('barajaMano.json', "w") as paqueteCartas: 
                    json.dump(paquete, paqueteCartas, indent=4)

                return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> HA TOMADO UNA CARTA </H1><H3>Carta tomada → {}{}</H3><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div>".format(cambio.get('carta'),cambio.get('tipo'),link1, link2, link3, link4, link5, link6, link7)
            else:
                return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> No quedan cartas disponibles </H1><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div></div>".format(link1, link2, link3, link4, link5, link6, link7)

    @api.route("/user/play", methods = ['GET'])
    def mVerificarJuego():

        link1 = "window.location.href='http://127.0.0.1:5000/deck/new'"
        link2 = "window.location.href='http://127.0.0.1:5000/deck/shuffle'"
        link3 = "window.location.href='http://127.0.0.1:5000/deck/show/remain'"
        link4 = "window.location.href='http://127.0.0.1:5000/deck/pickone'"
        link5 = "window.location.href='http://127.0.0.1:5000/user/show/hand'"
        link6 = "window.location.href='http://127.0.0.1:5000/user/play'"
        link7 = "window.location.href='http://127.0.0.1:5000'"

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

        return "<div><STYLE type='text/css'></STYLE></div><div><H1 class='Tit'> Jugadas Disponibles </H1><H3>{}</H3><button class='C1' onclick={}>Nueva Baraja</button><button class='C1' onclick={}>Revolver Baraja</button><button class='C1' onclick={}>Ver Disponibles</button><button class='C1' onclick={}>Tomar Carta</button><button class='C1' onclick={}>Ver Mano</button><button class='C1' onclick={}>Mis Jugadas</button><button class='C1' onclick={}>Menú Principal</button></div>".format(variableReturn,link1, link2, link3, link4, link5, link6, link7)