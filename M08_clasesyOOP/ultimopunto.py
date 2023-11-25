class Tools:
    def __init__(self, lista1):
        self.lista = lista1
    def ejerc(self):
        for i in self.lista:
            if(self.__ejerc(i)):
                print('ELEMENTO',i,'ES PRIMO')
            else:
                print('ELEMENTO',i,'NO ES PRIMO')

    def __ejerc(self,num):
        primo = True
        for i in range(2, num):
            if num%i==0:
                primo=False
                break
        return primo

    def modalista(self,lista, menor):
        primeralista = []
        listarepetidos = []
        if len(lista) == 0:
            print('NO HAY VALORES EN LISTA')
        if (menor):
            lista.sort()
        else:
            lista.sort(reverse=True)
        for elemento in lista:
            if elemento in primeralista:
                i = primeralista.index(elemento)
                listarepetidos[i] += 1
            else:
                primeralista.append(elemento)
                listarepetidos.append(1)
        moda = primeralista[0]
        total = listarepetidos[0]
        for i, elemento in enumerate(primeralista):
            if listarepetidos[i] > total:
                moda = primeralista[i]
                total = listarepetidos[i]
        
        print('MODA:',moda,' TOTAL REPETICIONES:',total)
    def conversion(self,temp, origen, destino):
        for i in self.lista:
            print(i)
    def __conversion(self,temp, origen, destino):
        nuevatemp = 0
        if origen=='CELSIUS':
            if destino=='CELSIUS':
                print(temp,'GRADOS CELCIUS')
            elif destino=='FARENHEIT':
                nuevatemp = (temp *9/5)+32
                print('SISTEMA ORIGEN:',origen,' TEMPERATURA INICIAL:',temp,' SISTEMA DESTINO:',destino,' TEMPERATURA FINAL:',nuevatemp)
            elif destino=='KELVIN':
                nuevatemp = (temp +273.15)
                print('SISTEMA ORIGEN:',origen,' TEMPERATURA INICIAL:',temp,' SISTEMA DESTINO:',destino,' TEMPERATURA FINAL:',nuevatemp)
            else:
                print('SISTEMA DE TEMPERATURA DESTINO NO RECONOCIDO')

        elif origen=='FARENHEIT':
            if destino=='CELSIUS':
                nuevatemp=(temp-32)/(9/5)
                print('SISTEMA ORIGEN:',origen,' TEMPERATURA INICIAL:',temp,' SISTEMA DESTINO:',destino,' TEMPERATURA FINAL:',nuevatemp)

            elif destino=='FARENHEIT':
                print(temp,'GRADOS FARENHEIT')

            elif destino=='KELVIN':
                nuevatemp=((temp-32)/(9/5))+273.15
                print('SISTEMA ORIGEN:',origen,' TEMPERATURA INICIAL:',temp,' SISTEMA DESTINO:',destino,' TEMPERATURA FINAL:',nuevatemp)

            else:
                print('SISTEMA DE TEMPERATURA DESTINO NO RECONOCIDO')
        elif origen =='KELVIN':
            if destino=='CELSIUS':
                nuevatemp=temp-273.15
                print('SISTEMA ORIGEN:',origen,' TEMPERATURA INICIAL:',temp,' SISTEMA DESTINO:',destino,' TEMPERATURA FINAL:',nuevatemp)
            elif destino=='FARENHEIT':
                nuevatemp=((temp-273.15)*9/5)+32
                print('SISTEMA ORIGEN:',origen,' TEMPERATURA INICIAL:',temp,' SISTEMA DESTINO:',destino,' TEMPERATURA FINAL:',nuevatemp)

            elif destino=='KELVIN':
                print(temp,'GRADOS KELVIN')

            else:
                print('SISTEMA DE TEMPERATURA DESTINO NO RECONOCIDO')
        else:
            print('SISTEMA DE TEMPERATURA ORIGEN NO RECONOCIDO')
    def factorial(self):
        for i in self.lista:
            print('RESULTADO DE',i,':',self.__factorial(i))
    def __factorial(self,num):
        resnum = num 
        if(type(num)==int):
            if(num<=0):
                print('NUMERO NEGATIVO O IGUAL A 0')

            else:
                for i in range(1, num):
                    resnum=resnum*(num-1)
                    num -=1
        else:
            print('NUMERO NO ENTERO')
    