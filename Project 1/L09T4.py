import L09T4Kirjasto
import sys

def valikko(lopeta,lopetusteksti):
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    if(lopeta):
        print("Valitse toiminto (0-3): ",end="")
        print(lopetusteksti)
        sys.exit(0)
    else:
        valinta=int(input("Valitse toiminto (0-3): "))
    return valinta
    
def paaohjelma():
    
    lopeta=False
    lopeta1=False
    lopetusteksti=""
    lopetusteksti1=""
    tiedostonNimi=input("Anna luettavan tiedoston nimi: ")    

    try:
        tiedosto=open(tiedostonNimi, 'r', encoding="utf-8")
    except:
        #print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostonNimi))
        lopeta=True
        lopetusteksti="Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostonNimi)

    tiedostonNimi1=input("Anna kirjoitettavan tiedoston nimi: ")    

    try:
        tiedostoKirjoitettava=open(tiedostonNimi1, 'w', encoding="utf-8")
    except:
        #print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoKirjoitettava))
        lopeta1=True
        lopetusteksti1="Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostonNimi1)

    ListaLuvut=[]
    ListaTulokset=[]
    ListanPituus=0
    eka=0
    toka=0
    apu=0
    luettu = True
    while(True):
        valinta=valikko(lopeta,lopetusteksti)
        if(valinta==1):
            if(luettu):
                ListaLuvut=L09T4Kirjasto.LueLuku(tiedosto,ListaLuvut,tiedostonNimi)
                luettu=False
            #print("tästä")
            #for i in ListaLuvut:
            #    print(i,end=" ")
            #    print("\n")
            ListanPituus=len(ListaLuvut)
            if(apu<ListanPituus):
                eka=ListaLuvut[apu]
                apu=apu+1
                toka=ListaLuvut[apu]
                apu=apu+1
                print("Luettiin luvut",eka,"ja",toka)
            else:
                print("Luvut loppuivat, lopeta ohjelma.")
                
        elif(valinta==2):
            tuloste=L09T4Kirjasto.summa(eka,toka)
            ListaTulokset.append(tuloste)
            print("Tulos lisätty listaan.")
            #tiedostoKirjoitettava.write(tuloste)
            #tiedostoKirjoitettava.write("\n")
            #print("Tulos tallennettu tiedostoon.")         
        elif(valinta==3):
            otulostus=L09T4Kirjasto.osamaara(eka,toka)
            ListaTulokset.append(otulostus)
            #tiedostoKirjoitettava.write(otulostus)
            #tiedostoKirjoitettava.write("\n")
            print("Tulos lisätty listaan.")
        elif(valinta==0):

            if(len(ListaTulokset)==0):
                print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.")
            else:
                if(lopeta1):
                    print(lopetusteksti1)
                    sys.exit(0)
                else:
                    L09T4Kirjasto.TalletaLista(tiedostoKirjoitettava,ListaTulokset)
                    printtaa1="'"+tiedostonNimi1+"'."
                    print("Tallennettu tiedosto",printtaa1)
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
    tiedosto.close()
    tiedostoKirjoitettava.close()

paaohjelma()
print("Kiitos ohjelman käytöstä.")
