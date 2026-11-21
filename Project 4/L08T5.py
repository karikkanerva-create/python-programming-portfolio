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

import L08T5Kirjasto

def valikko(eka):
    if(eka==0):
        print("Mitä haluat tehdä:")
    if(eka==1):
        print("\nMitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna Tulokset")
    print("0) Lopeta")
    valinta=int(input("Valintasi: "))
    return valinta
    
def paaohjelma():
    eka=0
    tiedostonNimi=input("Anna luettavan tiedoston nimi: ")    
    tiedostonNimiKirjoitettava=input("Anna kirjoitettavan tiedoston nimi: ")    
    listaKaikkiOliot=[]
    ListaTiedostonRivit=[]
    arvoTuloslistaan=[]
    ListanPituus=0
    eka=0
    toka=0
    apu=0
    luettu = True
    while(True):
        valinta=valikko(eka)
        if(valinta==1):
            listaKaikkiOliot=L08T5Kirjasto.LueTiedosto(tiedostonNimi) 
        elif(valinta==2):
            arvoTuloslistaan=L08T5Kirjasto.analysoiTiedot(listaKaikkiOliot)
        elif(valinta==3):
            L08T5Kirjasto.talletaArvolistaTiedostoon(tiedostonNimiKirjoitettava,arvoTuloslistaan)
        elif(valinta==0):            
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        eka=1
paaohjelma()
print("Kiitos ohjelman käytöstä.")
