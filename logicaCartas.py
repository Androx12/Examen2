import json
import random


class logicaCartas:

    def __init__(self):
        self.barajaJson = 'baraja.json'
        self.barajaManoJson = 'barajaMano.json'


    def mGuardarBarajaJson (self, nuevo):
        with open (self.barajaJson, "w") as paqueteCartas: 
            json.dump(nuevo, paqueteCartas, indent=4)


    def mGuardarManoJson (self, nuevo):
        with open (self.barajaManoJson, "w") as paqueteCartas: 
            json.dump(nuevo, paqueteCartas, indent=4)

    
    def mCrearBaraja(self):
        cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        tipos = ["♠","♦","♣","♥"]
        baraja = []

        for carta in cartas:
            for tipo in tipos:
                cartajson = {"carta": "{}".format(carta),"tipo": "{}".format(tipo)}
                baraja.append(cartajson)
        self.mGuardarBarajaJson(baraja)


    def mCargarCartasNuevas(self):
        with open (self.barajaJson) as paqueteCartas: 
            paquete = json.load(paqueteCartas) 

            if(len(paquete)>0):   

                return self.barajaJson

                '''
                contador = 0 

                for cartaPaquete in paquete:
                    contador = contador + 1
                    print ("Carta N° {} : {}".format(contador, cartaPaquete.get('carta')))'''


    def mCargarCartasTomadas(self):
        
        with open (self.barajaManoJson) as paqueteCartas: 
            paquete = json.load(paqueteCartas)    

            if(len(paquete)>0):
                contador = 0     

                for cartaPaquete in paquete:
                    contador = contador + 1
                    print ("Carta N° {} : {}".format(contador, cartaPaquete.get('carta')))


    def mCartasShuffle(self):
        with open (self.barajaJson) as paqueteCartas: 
            paquete = json.load(paqueteCartas)
            random.shuffle(paquete)
            self.mGuardarBarajaJson(paquete)


    def mTomarCartas(self):

        with open (self.barajaJson) as paqueteCartas:
            paquete = json.load(paqueteCartas)
            
            if(len(paquete)>0):
                cambio = paquete.pop(0)
                self.mGuardarBarajaJson(paquete)

        with open (self.barajaManoJson) as paqueteCartas:
            paquete = json.load(paqueteCartas)
            paquete.append(cambio)
            self.mGuardarManoJson(paquete)


    def mVerificarJuego(self):
        with open (self.barajaManoJson) as paqueteCartas: 
            paquete = json.load(paqueteCartas) 
        
        bEscaleraReal = False
        bEscaleraColor = False
        bPoker = False
        bFull = False
        bColor = False
        bEscalera = False
        bTrio = False
        bDoblePar = False
        bPar1 = False

        if(len(paquete) > 0):

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

            contador = 0
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

            for carta in paquete:
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
            
            if(bEscaleraReal == True):
                print("Escalera Real")
            if(bEscaleraColor == True):
                print("Escalera Color")
            if(bPoker == True):
                print("Poker")
            
            if(bColor == True):
                print("Color")
            if(bEscalera == True):
                print("Escalera")


            if(bTrio == True):          #Valida TRIO y FULL
                if(bPar1 == True):
                    bFull = True
                    bPar1 = False
                    if(bFull == True):
                        print("Full")
                else:
                    print("Trio")



            if(bDoblePar == True):      #Valida PAR y DOBLE PAR
                print("Doble Par")
            else:
                if(bPar1 == True):
                    print("Par")

        else:
            print('No hay cartas en mano')
'''
if __name__ == '__main__':

    objeinst = logicaCartas()
    objeinst.mVerificarJuego()
    objeinst.mTomarCartas()
    objeinst.mCrearBaraja()
    objeinst.mCartasShuffle()
    objeinst.mCargarCartasTomadas()
    objeinst.mCargarCartasNuevas()'''
 

    

