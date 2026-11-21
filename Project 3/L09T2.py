######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Kari Kanerva
# Opiskelijanumero:
# Päivämäärä: 30.1.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################

def valikko(eka):
    #if(eka==0):
    #    print("Mitä haluat tehdä:")
    #if(eka==1):
    #    print("\nMitä haluat tehdä:")
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    
    print("0) Lopeta")
    digit=""
    while(True):
        try:
            digit=int(input("Valintasi: "))
            break
        except ValueError:
            print("Anna valinta kokonaislukuna.")
            #digit=int(input("Valintasi: "))
    return digit

def testaaValueError(valinta):
    print("Valikko-ohjelma testaa ValueError'n.")
    
def testaaIndexError():
        indeksi=int(input("Anna indeksi 0-4: "))
        sana="olavi"
        lista=[]
        lista.append("11")
        lista.append("22")
        lista.append("33")
        lista.append("44")
        lista.append("55")
        
        try:
            numero=lista[indeksi]
            print("Listan arvo on {0} indeksillä {1}.".format(lista[indeksi],indeksi))
        except IndexError:
            print("Tuli IndexError, indeksi {0}.".format(indeksi))
    
def testaaZeroDivisionError():
    jakaja=int(input("Anna jakaja: "))
    x=4
    try:
        osamaara=x/jakaja
        print("{0}/{1} on {2:.2f}.".format(x,jakaja,osamaara))
        
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja 0.")
    
def testaaTypeError():
    tuloste="juuuuu"
    numero=input("Anna numero: ")
    tulo=0
    digit=0
    tuloste=numero+"*"+numero
    try:
        #digit=int(numero)
        #digit=numero
        tulo=numero*numero
    except (TypeError,ValueError):
        print("Tuli TypeError,",tuloste,"merkkijonoilla ei onnistunut.")

def paaohjelma():
    eka=0
    toka=0
    apu=0
    kysyValikko=True
    while(True):
        if(kysyValikko):
            valinta=valikko(eka)
        else:
            kysyValikko=True
        

        if(valinta==1):
            testaaValueError(valinta)
            kysyValikko=True
        elif(valinta==2):
            testaaIndexError()
            kysyValikko=True
        elif(valinta==3):
            testaaZeroDivisionError()
            kysyValikko=True
        elif(valinta==4):
            testaaTypeError()
            kysyValikko=True
        elif(valinta==0):            
            break
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")

paaohjelma()
print("Kiitos ohjelman käytöstä.")
