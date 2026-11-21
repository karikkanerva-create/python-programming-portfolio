def LueLuku(tiedosto,lista,tiedostonNimi):
    while(True):
        rivi = tiedosto.readline()
        if (len(rivi) == 0):
            break
        else:
            lisataan=int(rivi)
            #print(lisataan,"Lisataan.\n")
            lista.append(lisataan)
    printtaa="'"+tiedostonNimi+"'."
    print("Luettu tiedosto",printtaa)    
    return lista

def summa(eka,toka):
    summa=eka+toka
    palautus="Summa "+str(eka)+" + "+str(toka)+" = "+str(summa)
    return palautus

def osamaara(eka,toka):
    if(toka==0):
        #print("Nollalla ei voi jakaa.")
        opalautus="Nollalla ei voi jakaa."
    else:
        osamaara=round(eka/toka,2)
        opalautus="Osamäärä "+str(eka)+" / "+str(toka)+" = "+str(osamaara)
        #opalautus="kyllä kyllä"
        #print("Osamäärä",eka,"/",toka,"=",osamaara)
    return opalautus

def TalletaLista(tiedostoKirjoitettava,lista):
    for i in lista:
        #print(i)
        #print("juuukkkk")
        kirjoitatama=str(i)
        #print(kirjoitatama,"jooko")
        tiedostoKirjoitettava.write(i)
        tiedostoKirjoitettava.write("\n")
