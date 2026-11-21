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

class TUOTE:
    tuotetunniste = ""
    tuotteidenmaara = ""
    hinta = 0

def LueTiedosto(tiedostonNimi):
    tiedosto=open(tiedostonNimi, 'r', encoding="utf-8")
    riviListaan=[]
    oliot=[]
    riveja=0
    while(True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        else:
            #splittaa tässä rivi ja laita olioon
            riviListaan = rivi.split(';')
            uusituote=TUOTE()
            uusituote.tuotetunniste=riviListaan[0]
            #print("eka",riviListaan[0])
            #print("toka",riviListaan[1])
            #print("kolmas",riviListaan[2])
            
            uusituote.tuotteidenmaara=riviListaan[1]
            uusituote.hinta=riviListaan[2]
            #lisataan=int(rivi)
            #print(lisataan,"Lisataan.\n")
            oliot.append(uusituote)
            riveja=riveja+1
    printtaa="'"+tiedostonNimi+"'"
    #print("Luettu tiedosto",printtaa)

    print("Tiedosto",printtaa,"luettu,",riveja,"riviä.")
    tiedosto.close()
    return oliot

def analysoiTiedot(kaikkiOliot):
    arvolista=[]
    kokonaisarvo=0

    for TUOTE in kaikkiOliot:
        maara=int(TUOTE.tuotteidenmaara)

        apuhinta=(TUOTE.hinta)
        #print(apuhinta)
        apuhinta=apuhinta[::1]
        #print("apuhinta",apuhinta)
        yksikkoHinta=float(apuhinta)
        arvo=maara*yksikkoHinta

        s = "{0:.2f}".format(arvo)
        #print("s",s)
        #lisaa=round(arvo,2)
        arvolista.append(s);
        #print("lisätty",s)
        kokonaisarvo=kokonaisarvo+arvo
        arvoo = "{0:.2f}".format(kokonaisarvo)
        
    print("Tiedot analysoitu, varaston arvo on",arvoo,"EUR.")
    return arvolista

def talletaArvolistaTiedostoon(tiedostonNimiKirjoitettava,lista):
    tiedostoKirjoitettava=open(tiedostonNimiKirjoitettava, 'w', encoding="utf-8")
    for i in lista:
        #print(i)
        #print("juuukkkk")
        #pyoristetty=float(round(i,2))
        kirjoitatama=str(i)
        #print(kirjoitatama,"jooko")
        tiedostoKirjoitettava.write(kirjoitatama)
        tiedostoKirjoitettava.write("\n")
    tiedostoKirjoitettava.close()
    printtaa="'"+tiedostonNimiKirjoitettava+"'."
    print("Tulokset tallennettu tiedostoon",printtaa)
