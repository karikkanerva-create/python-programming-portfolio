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
import sys

def lueTiedosto(tiedostonNimi,riviListaan):

    try:
        tiedosto=open(tiedostonNimi, 'r', encoding="utf-8")
        riviListaan=[]
        while(True):
            rivi = tiedosto.readline()
            if (len(rivi) == 0):
                break
            else:
                riviListaan.append(rivi)
                #riveja=riveja+1
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostonNimi))
        sys.exit(0)
    tiedosto.close()
    return riviListaan
    
def analysoiTiedot(listaLuetutTiedot):
    listaAutomerkit=[]
    indeksi=0
    edellinen=""
    for i in listaLuetutTiedot:

        #print("iiii=",i)
        if(indeksi==0):
            #listaAutomerkit.append(i)
            edellinen=i[::1]
            #print("lisätty",i)
            #print("oli eka edellinen asetettu",edellinen)
        elif(indeksi>0):
            if(i==edellinen):
                apu=0
                #print("olivat samat",indeksi,i,edellinen)
            else:
                listaAutomerkit.append(edellinen)
                #print("lisätty elseen tuli ja edellinen oli",edellinen)
                edellinen=i
        if(indeksi+1==len(listaLuetutTiedot)):
            try:
                if(listaAutomerkit.index(i)>=0):
                    apu=0
                    #print("ei tartte lisätä")
                else:
                    apu=0
                    #print("tarvii lisätä")
            except ValueError:
                #print("iiii on",i)
                listaAutomerkit.append(i[::1])              

#            if(i==edellinen):
#                print("olivat samat",indeksi)
#                print("viimeinen")
#                for e in listaAutomerkit:
#                    if(i==e):
#                        print("ei lisätä",i,e)
#                    else:
#                        listaAutomerkit.append(i)
#                        print("lisätään",i)
#            else:
#                listaAutomerkit.append(i)
#                print("lisätty",i)
#                print("viimeinen")
            
            

        indeksi=indeksi+1
    #print("pituus",len(listaLuetutTiedot))
    return listaAutomerkit


def tulostaJaTallenna(kirjoitettavaTiedosto,listaAutomerkit):

    try:
        tiedosto=open(kirjoitettavaTiedosto, 'w', encoding="utf-8")
        for i in listaAutomerkit:
            #print(i)
            tiedosto.write(i)
            #tiedosto.write("\n")
    except Exception:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(kirjoitettavaTiedosto))
        sys.exit(0)

    tiedosto.close()
    print("Tiedostossa oli",len(listaAutomerkit),"eri automerkkiä.")
    for i in listaAutomerkit:
        print(i,end="")

def paaohjelma():

    listaLuetutTiedot=[]
    listaAutomerkit=[]
    #luettavaTiedosto="L09T3D1.txt"
    #kirjoitettavaTiedosto="L09T3T1.txt"

    luettavaTiedosto=input("Anna luettavan tiedoston nimi: ")
    kirjoitettavaTiedosto=input("Anna kirjoitettavan tiedoston nimi: ")
    
    listaLuetutTiedot=lueTiedosto(luettavaTiedosto,listaLuetutTiedot)


    if(len(listaLuetutTiedot)==0):
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        listaAutomerkit=analysoiTiedot(listaLuetutTiedot)
        tulostaJaTallenna(kirjoitettavaTiedosto,listaAutomerkit)

paaohjelma()
print("Kiitos ohjelman käytöstä.")
