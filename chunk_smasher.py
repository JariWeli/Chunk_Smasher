#Chunk machine

import os.path

def valikko():
    while True:
        print("Valitse haluamasi toiminto:")
        print("1) Tulosta kenttä")
        print("2) Lisää oikealle")
        print("3) Lisää alaspäin")
        print("4) Korvaa chunk")
        print("5) Tyhjennä chunk")
        print("6) Poista chunk")
        print("7) Tactical nuke")
        print("0) Lopeta")
        valinta=input("Anna valintasi: ")
        if valinta.isdigit() and 0<=int(valinta)<=7:
            valinta=int(valinta)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
            continue
        return valinta

def kysyNimi(viesti):
    nimi=input(viesti)
    nimi+=".txt"
    return nimi

def lueTiedosto(nimi):
    file=open(nimi,"r",encoding="utf-8")
    level=file.readlines()
    file.close()
    file=open(nimi,"r",encoding="utf-8")
    counter=0
    for rivi in file:
        counter+=1
    file.close()
    return level,counter-1

def tulostaKentta(nimi,sivu):
    file=open(nimi,"r",encoding="utf-8")
    rivi_counter=0
    for rivi in file:
        rivi_counter+=1
    file.close()
    rivit=int(rivi_counter/sivu)
    file=open(nimi,"r",encoding="utf-8")
    lines=file.readlines()
    file.close()
    for i in range(rivit):
        pituus=lines[(sivu-1)*(i+1)].split(" ")
        chunk=int(len(pituus)/sivu)
        print("Rivillä",i+1,"on",chunk,"chunkkia")
    return None

def kirjoitaOikealle(nimi,sivu):
    file=open(nimi,"r",encoding="utf-8")
    alku=file.readlines()
    file.close()
    rivien_maara=len(alku)/sivu
    while True:
        try:
            rivi=input("Mille riville haluat lisätä (palaa: enter): ")
            if rivi=="":
                return None
            else:
                rivi=int(rivi)
            if rivi<=rivien_maara:
                break
            else:
                print("Riviä ei ole olemassa!")
        except:
            print("Ei ole numero!")
    while True:
        try:
            nim=kysyNimi("Anna lisättävän tiedoston nimi: ")
            if nim==".txt":
                return None
            else:
                file=open(nim,"r",encoding="utf-8")
                break
        except:
            print("Tiedostoa ei löydy!")
    rivit=file.readlines()
    file.close()
    a=0
    for i in range((rivi-1)*sivu,rivi*sivu):
        riv=rivit[a]
        alk=alku[i]
        alk=alk.replace("\n","")
        final=alk+riv
        replace_line(nimi,i,final)
        a+=1
    print("Chunk kirjoitettu!")
    return None

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def kirjoitaAlaspain(nimi):
    while True:
        try:
            syote=kysyNimi("Anna lisättävän tiedoston nimi (palaa: enter): ")
            if syote==".txt":
                return None
            else:
                file=open(syote,"r",encoding="utf-8")
                break
        except:
            print("Tiedostoa ei löydy!")
    rivit=file.readlines()
    file.close()
    kirj=open(nimi,"a",encoding="utf-8")
    for i in rivit:
        kirj.write(i)
    kirj.close()
    print("Chunk kirjoitettu!")
    return None

def korvaaChunk(nimi,sivu):
    file=open(nimi,"r",encoding="utf-8")
    rows=file.readlines()
    file.close()
    rivien_maara=len(rows)/sivu
    while True:
        try:
            rivi=input("Miltä riviltä haluat vaihtaa chunkin (palaa: enter): ")
            if rivi=="":
                return None
            else:
                rivi=int(rivi)
            if rivi<=rivien_maara:
                break
            else:
                print("Riviä ei ole olemassa!")
        except:
            print("Ei ole numero!")
    while True:
        try:
            chunk=input("Minkä chunkin haluat vaihtaa (palaa: enter): ")
            if chunk=="":
                return None
            else:
                chunk=int(chunk)
                sarake=rows[int(rivi*(sivu-1))].split(" ")
                chunk_maara=round(len(sarake)/(sivu))
            if chunk<=chunk_maara:
                break
            else:
                print("Chunkkia ei ole olemassa!")
        except:
            print("Ei ole numero!")
    while True:
        try:
            nim=kysyNimi("Korvaavan tiedoston nimi (palaa: enter): ")
            if nim==".txt":
                return None
            else:
                file=open(nim,"r",encoding="utf-8")
                break
        except:
            print("Tiedostoa ei löydy!")
    rivit=file.readlines()
    file.close()
    a=0
    alku=loppu=[]
    for i in range((rivi-1)*sivu,rivi*sivu):
        row=rows[i]
        chunk_maara=len(row)/sivu
        sarake=row.split(" ")
        alku=sarake[0:(chunk-1)*(sivu)]
        loppu=sarake[chunk*(sivu):]
        riv=rivit[a]
        riv=riv.replace("\n","")
        if  chunk<chunk_maara:
            final=" ".join(alku)+" "+riv+" ".join(loppu)
            final=final.lstrip(" ")
        else:
            final=" ".join(alku)+" "+riv+"\n"
            final=final.lstrip(" ")
        replace_line(nimi,i,final)
        a+=1
    print("Chunk korvattu!")
    return None

def tyhjennaChunk(nimi,sivu):
    file=open(nimi,"r",encoding="utf-8")
    rows=file.readlines()
    file.close()
    rivien_maara=len(rows)/sivu
    while True:
        try:
            rivi=input("Miltä riviltä haluat tyhjentää chunkin (palaa: enter): ")
            if rivi=="":
                return None
            else:
                rivi=int(rivi)
            if rivi<=rivien_maara:
                break
            else:
                print("Riviä ei olemassa!")
        except:
            print("Ei ole numero!")
    while True:
        try:
            chunk=input("Minkä chunkin haluat tyhjentää (palaa: enter): ")
            if chunk=="":
                return None
            else:
                chunk=int(chunk)
                sarake=rows[int(rivi*(sivu-1))].split(" ")
                chunk_maara=round(len(sarake)/(sivu))
            if chunk<=chunk_maara:
                break
            else:
                print("Chunkkia ei olemassa!")
        except:
            print("Ei ole numero!")
    base=""
    for i in range(0,sivu):
        base+="0 "
    a=0
    for i in range((rivi-1)*sivu,rivi*sivu):
        row=rows[i]
        sarake=row.split(" ")
        alku=sarake[0:((chunk-1)*(sivu))]
        loppu=sarake[chunk*(sivu):]
        final=" ".join(alku)+" "+base+" ".join(loppu)
        final=final.lstrip(" ")
        replace_line(nimi,i,final)
        a+=1
    print("Chunk tyhjennetty!")
    return None

def luoChunk(nimi,sivu):
    base=""
    for i in range(0,sivu):
        base+="0 "
    file=open(nimi,"w",encoding="utf-8")
    for i in range(0,sivu):
        file.write(base+"\n")
    file.close()
    return None

def poistaChunk(nimi,sivu):
    file=open(nimi,"r",encoding="utf-8")
    rows=file.readlines()
    file.close()
    rivien_maara=len(rows)/sivu
    while True:
        try:
            rivi=input("Miltä riviltä haluat poistaa chunkin (palaa: enter): ")
            if rivi=="":
                return None
            else:
                rivi=int(rivi)
            if rivi<=rivien_maara:
                break
            else:
                print("Riviä ei olemassa!")
        except:
            print("Ei ole numero!")
    while True:
        try:
            chunk=input("Minkä chunkin haluat poistaa: ")
            if chunk=="":
                return None
            else:
                chunk=int(chunk)
                sarake=rows[int(rivi*(sivu-1))].split(" ")
                chunk_maara=round(len(sarake)/(sivu))
            if chunk<=chunk_maara:
                break
            else:
                print("Chunkkia ei olemassa!")
        except:
            print("Ei ole numero!")
    a=0
    for i in range((rivi-1)*sivu,rivi*sivu):
        row=rows[i]
        sarake=row.split(" ")
        alku=sarake[0:(chunk-1)*(sivu)]
        loppu=sarake[chunk*(sivu):]
        final=" ".join(alku)+" "+" ".join(loppu)
        final=final.lstrip(" ")
        replace_line(nimi,i,final)
        a+=1
    print("Chunk poistettu!")
    return None

def tacticalNuke(nimi,sivu):
    paatos=input("Oletko varma? y/n: ")
    if "y" in paatos:
        file=open(nimi,"w")
        file.close()
        luoChunk(nimi,sivu)
    else:
        return None
    return None

def main():
    sivu=32
    print("Tervetuloa käyttämään Chunk Smasher 1.0")
    nimi=kysyNimi("Anna muokattavan tiedoston nimi: ")
    if os.path.isfile(nimi):
        print("Tiedosto löytyi!")
    else:
        luoChunk(nimi,sivu)
        print("Tiedosto luotiin!")
    #sivu=int(input("Anna chunkin koko: ")) #ota käyttöön jos chunk koko vaihtuu!!
    i=1
    while i!=0:
        i=valikko()
        if i==1:
            tulostaKentta(nimi,sivu)
        elif i==2:
            kirjoitaOikealle(nimi,sivu)
        elif i==3:
            kirjoitaAlaspain(nimi)
        elif i==4:
            korvaaChunk(nimi,sivu)
        elif i==5:
            tyhjennaChunk(nimi,sivu)
        elif i==6:
            poistaChunk(nimi,sivu)
        elif i==7:
            tacticalNuke(nimi,sivu)
        elif i==0:
            print("Lopetetaan.")
        print()
    print("Kiitos ohjelman käytöstä.")
    return None

main()
