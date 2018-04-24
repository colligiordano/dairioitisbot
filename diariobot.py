#!/usr/bin/python3

##import dei vari moduli
import datetime
import pathlib
import time
import sys
import os
import glob
import telepot
import telepot.loop
import random

#tutte le funzioni che servono per verificare esistenza,lettura,scrittura dei file e delle cartelle
class Dir_file:
    def __init__(self,cartella):
        self.cartella=cartella


    def esiste(self):
        if (os.path.isdir(self.cartella)):
            return 1
        else:
            return 0


    def non_esiste(self):
        try:
            os.makedirs(self.cartella)
            print("cartella creata")
        except:
            print("errore creazione cartella")

    def cisonofile(self):
        try:
            os.listdir(self.cartella)
            return 1
        except:
            print("non ci sono file")
            return 0
    def cisonofileesatti(self):
        esiste = 0
        for x in os.listdir(self.cartella):
            if x == "domani.txt":
                esiste = esiste+1
            if x == "mese.txt":
                esiste = esiste+1
        if esiste == 2:
            return 1
        else:
            return 0

    def creafile(self):
        try:
            f = open(self.cartella + "domani.txt","w+")
            f.close()
            f = open(self.cartella + "mese.txt","w+")
            f.close()
            print("file creati correttamente")
        except:
            print("errore nella creazione dei file")

    def stampa(self):
        return self.cartella





class Query_message:
    premuto = 0
    scuolapremuto = 0
    domanipiupremuto = 0
    mesepiupremuto = 0
    chatpremuto = 0
    argomentipremuto = 0
    argomentipiupremuto = 0
    materiapiupremuto = 0
    tempdir = ""
    photoidtemp = ""
    eventipiupremuto = 0
    appuntipremuto = 0
    classepremuto = 0

    def __init__(self,msg,chat,bot):
        self.msg = msg
        self.chat = chat
        self.bot = bot
        self.text = ""
    
    def tipo(self):
        try:
            self.idphoto = ((self.msg["photo"])[-1])["file_id"]
            return "photo"
        except:
            try:
                self.idfile = (self.msg["document"])["file_id"]
                self.namefile = ((self.msg)["document"])["file_name"]
                return "file"
            except:
                self.text = (self.msg["text"]).lower()
                return "text"
    

    def orario(self,cartella):
        if self.text == "/orario" or self.text == "/orario@diarioitisbot":
            if os.path.isfile(cartella + "orario.jpg"):
                self.bot.sendPhoto(self.chat,open(cartella + "orario.jpg","rb"))
            else:
                self.bot.sendMessage(self.chat,"orario.jpg non esiste, utilizzare la funzione /orariopiu")

    def orariopiu(self):
        if self.text == "/orariopiu" or self.text == "/orariopiu@diarioitisbot":
            self.bot.sendMessage(self.chat, "inviare la foto dell'orario")
            Query_message.premuto=1
            Query_message.chatpremuto=self.chat

    def orariopiubis(self,cartella,tipo):
        if tipo == "file": 
            try:
                self.bot.download_file(self.idfile, cartella + "orario.jpg")
                self.bot.sendMessage(self.chat, "file correttamente caricato,testalo con /orario")
            except:
                self.bot.sendMessage(self.chat,"invia un'immagine valida!!")
        elif tipo == "photo":
            try:
                self.bot.download_file(self.idphoto, cartella + "orario.jpg")
                self.bot.sendMessage(self.chat, "file correttamente caricato,testalo con /orario")
            except:
                self.bot.sendMessage(self.chat,"invia un'immagine valida!!")
        elif tipo == "text":
            if not self.text.startswith("/"):
                print("")
        else:
            self.bot.sendMessage(self.chat, "invia un'immagine")
        Query_message.premuto=0

    def scuolalavoro(self,cartella):
        if self.text == "/scuolalavoro" or self.text == "/scuolalavoro@diarioitisbot":
            if os.path.isfile(cartella + "scuolalavoro.jpg"):
                self.bot.sendPhoto(self.chat,open(cartella + "scuolalavoro.jpg","rb"))
            else:
                self.bot.sendMessage(self.chat,"scuolalavoro.jpg non esiste, utilizzare la funzione /scuolalavoropiu")

    def scuolalavoropiu(self):
        if self.text == "/scuolalavoropiu" or self.text == "/scuolalavoropiu@diarioitisbot":
            self.bot.sendMessage(self.chat, "inviare la foto dell'orario")
            Query_message.scuolapremuto=1
            Query_message.chatpremuto=self.chat

    def scuolalavoropiubis(self,cartella,tipo):
        if tipo == "file":
            try:
                self.bot.download_file(self.idfile, cartella + "scuolalavoro.jpg")
                self.bot.sendMessage(self.chat, "file correttamente caricato,testalo con /scuolalavoro")
            except:
                self.bot.sendMessage(self.chat,"invia un'immagine valida!!")
        elif tipo == "photo":
            try:
                self.bot.download_file(self.idphoto, cartella + "scuolalavoro.jpg")
                self.bot.sendMessage(self.chat, "file correttamente caricato,testalo con /scuolalavoro")
            except:
                self.bot.sendMessage(self.chat,"invia un'immagine valida!!")
        elif tipo == "text":
            if not self.text.startswith("/"):
                print("")
        else:
            self.bot.sendMessage(self.chat, "invia un'immagine")
        Query_message.scuolapremuto=0


    def domani(self,cartella):
        if self.text == "/domani" or self.text == "/domani@diarioitisbot":
            if (str(open(cartella + "domani.txt","r").read()) == ""):
                f = open(cartella + "domani.txt","w")
                f.write(str(datetime.datetime.now().strftime("%d" +"/"+ "%m" + "/" + "%Y")))
                f.close()
            try:
                f = str(open(cartella + "domani.txt","r").read())
                self.bot.sendMessage(self.chat, f)
            except:
                self.bot.sendMessage(self.chat, "c'e' stato un problema con il file")

    def domanipiu(self):
        if self.text == "/domanipiu" or self.text == "/domanipiu@diarioitisbot":
            self.bot.sendMessage(self.chat,"inserire il compito")
            Query_message.domanipiupremuto = 1
            Query_message.chatpremuto = self.chat

    def domanipiubis(self,cartella,tipo):
        if tipo == "text":
            if not self.text.startswith("/"):
                try:
                    f = open(cartella + "domani.txt","a")
                    f.write("\n" + self.text)
                    self.bot.sendMessage(self.chat, "domani scritto con successo,stampa /domani")
                except:
                    self.bot.sendMessage(self.chat, "errore scrittura")
        else:
            self.bot.sendMessage(self.chat,"inserire testo")
        Query_message.domanipiupremuto = 0

    def mese(self,cartella):
        if self.text == "/mese" or self.text == "/mese@diarioitisbot":
            if (str(open(cartella + "mese.txt","r").read()) == ""):
                f = open(cartella + "mese.txt","w")
                f.write(str(datetime.datetime.now().strftime("%m" + "/" + "%Y")))
                f.close()
            try:
                f = str(open(cartella + "mese.txt","r").read())
                self.bot.sendMessage(self.chat, f)
            except:
                self.bot.sendMessage(self.chat, "c'e' stato un problema con il file")

    def mesepiu(self):
        if self.text == "/mesepiu" or self.text == "/mesepiu@diarioitisbot":
            self.bot.sendMessage(self.chat,"inserire l'avvenimento")
            Query_message.mesepiupremuto = 1
            Query_message.chatpremuto = self.chat

    def mesepiubis(self,cartella,tipo):
        if tipo == "text":
            if not self.text.startswith("/"):
                try:
                    f = open(cartella + "mese.txt","a")
                    f.write("\n" + self.text)
                    self.bot.sendMessage(self.chat, "mese scritto con successo,stampa /mese")
                except:
                    self.bot.sendMessage(self.chat, "errore scrittura")
        else:
            self.bot.sendMessage(self.chat,"inserire testo")
            
        Query_message.mesepiupremuto = 0
    
    def argomenti(self,cartella):
        if (self.text == "/argomenti" or self.text == "/argomenti@diarioitisbot"):
            try:
                f = open(cartella + "argomenti.txt","w+")
            except:
                print("c'e' stato un problema con il file")
            for x in os.listdir(cartella):
                if (x != "domani.txt" and x != "mese.txt" and x != "scuolalavoro.jpg" and x != "orario.jpg" and x != "argomenti.txt" and x != "temp" and x != "alunni"):
                    f.write(x + "\n")
                    f.close()
            f = open(cartella + "argomenti.txt","r")
            stringa = str(f.read())
            try:
                self.bot.sendMessage(self.chat,stringa)
                self.bot.sendMessage(self.chat,"inserire la materia")
                Query_message.argomentipremuto = 1
            except:
                self.bot.sendMessage(self.chat, "nessun argomento,aggiungilo con /argomentipiu")
                Query_message.argomentipremuto = 0 
            Query_message.chatpremuto = self.chat

    def argomentibis(self,cartella,tipo):
        if os.path.isdir(cartella + self.text) and not self.text.startswith("/"):
            if not os.path.isfile(cartella + "temp"):
                f = open(cartella + "temp","w+")
                f.close()
            if tipo == "text":
                f = open(cartella + "temp","a") 
                for x in os.listdir(cartella + self.text):
                    f.write("\n" + x)
                f.close()
                f = str(open(cartella + "temp","r").read())
                try:
                    self.bot.sendMessage(self.chat,f)
                    self.bot.sendMessage(self.chat,"inserire l'evento")
                    Query_message.argomentipremuto = 2
                    Query_message.tempdir = cartella + self.text + "/"
                except:
                    self.bot.sendMessage(self.chat,"non ci sono eventi")
                    Query_message.argomentipremuto = 0
            else:
                self.bot.sendMessage(self.chat,"inserire del testo")
                Query_message.argomentipremuto = 0
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
        elif self.text.startswith("/"):
            Query_message.argomentipremuto = 0
        else:
            self.bot.sendMessage(self.chat,"non ci sono materie")
            Query_message.argomentipremuto = 0
    def argomentibisbis(self,cartella):
        if os.path.isdir(Query_message.tempdir + self.text) and not self.text.startswith("/"):
                f = open(cartella + "temp","w")
                f.close()
                f = open(cartella + "temp","a")
                for x in os.listdir(Query_message.tempdir + self.text):
                    f.write("\n" + x)
                f.close()
                try:
                    f = str(open(cartella + "temp","r").read())
                    self.bot.sendMessage(self.chat, f)
                except:
                    self.bot.sendMessage(self.chat, "non ci sono argomenti")
                Query_message.argomentipremuto = 0
                if os.path.isfile(cartella + "temp"):
                    os.remove(cartella + "temp")

        else:
            self.bot.sendMessage(self.chat,"l'evento non esiste")
            Query_message.argomentipremuto = 0
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
    
    def materiapiu(self):
        if self.text == "/materiapiu" or self.text == "/materiapiu@diarioitisbot":
            self.bot.sendMessage(self.chat,"inserisci la materia")
            Query_message.materiapiupremuto = 1
            Query_message.chatpremuto = self.chat
    def materiapiubis(self,cartella,tipo):
        if tipo == "text":
            if not self.text.startswith("/"):
                if os.path.isdir(cartella + self.text):
                    self.bot.sendMessage(self.chat,"la materia esiste gia'")
                else:
                    os.makedirs(cartella + self.text)
                    self.bot.sendMessage(self.chat,"materia " + self.text + " creata con successo")
        else:
            self.bot.sendMessage(self.chat,"invia del testo")
        Query_message.materiapiupremuto = 0

    def argomentipiu(self,cartella):
        if self.text == "/argomentipiu" or self.text == "/argomentipiu@diarioitisbot": 
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
            f = open(cartella + "temp", "w+")
            f.close()
            f = open(cartella + "temp", "a")
            for x in os.listdir(cartella):
                if x != "domani.txt" and x != "mese.txt" and x != "scuolalavoro.jpg" and x != "orario.jpg" and x != "argomenti.txt" and x != "temp" and x != "alunni":
                    f.write("\n" + x)
            f.close()
            f = str(open(cartella + "temp","r").read())
            try:
                self.bot.sendMessage(self.chat,f)
                self.bot.sendMessage(self.chat, "seleziona la materia")
                Query_message.argomentipiupremuto = 1
            except:
                self.bot.sendMessage(self.chat,"non ci sono materie, inserirle con /materiapiu")
                Query_message.argomentipiupremuto = 0
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
            Query_message.chatpremuto = self.chat

    def argomentipiubis(self,cartella):
        if os.path.isdir(cartella + self.text):
            if os.path.isfile(cartella + "temp") == 0:
                f = open(cartella + "temp", "w+")
                f.close()
            f = open(cartella + "temp","w")
            for x in os.listdir(cartella + self.text):
                f.write(x)
                f.write("\n")
            f.close()
            f = str(open(cartella + "temp","r").read())
            try:
                self.bot.sendMessage(self.chat,f)
                self.bot.sendMessage(self.chat,"selezionare l'evento")
                Query_message.argomentipiupremuto = 2
                Query_message.tempdir = cartella + self.text + "/"
            except:
                self.bot.sendMessage(self.chat,"evento inesistente, creane uno con /eventipiu")
                Query_message.argomentipiupremuto = 0
            os.remove(cartella + "temp")
        else:
            self.bot.sendMessage(self.chat, "la materia non esiste, creane una con /materiapiu")
            Query_message.argomentipiupremuto = 0

    def argomentipiubisbis(self,cartella):
        if os.path.isdir(Query_message.tempdir + self.text):
            if os.path.isfile(cartella + "temp") == 0:
                f = open(cartella + "temp", "w+")
                f.close()
            f = open(cartella + "temp","w")
            for x in os.listdir(Query_message.tempdir + self.text):
                f.write(x)
                f.write("\n")
            f.close()
            f = str(open(cartella + "temp","r").read())
            try:
                self.bot.sendMessage(self.chat,f)
                self.bot.sendMessage(self.chat,"inserisci l'argomento da aggiungere(file/photo)")
            except:
                self.bot.sendMessage(self.chat,"non ci sono argomenti")
                self.bot.sendMessage(self.chat,"inserisci l'argomento da aggiungere(file/photo)")
            Query_message.argomentipiupremuto = 3
            Query_message.tempdir = Query_message.tempdir + self.text + "/"
            os.remove(cartella + "temp")
        else:
            self.bot.sendMessage(self.chat, "l'evento non esiste")
            Query_message.argomentipiupremuto = 0

    def argomentipiubisbisbis(self,cartella,tipo):
        try:
            if tipo == "photo":
                self.bot.sendMessage(self.chat,"inserire il nome della foto(argomento)")
                Query_message.argomentipiupremuto = 4
                Query_message.photoidtemp = self.idphoto
            elif tipo == "file":
                self.bot.download_file(self.idfile, Query_message.tempdir + self.namefile)
                self.bot.sendMessage(self.chat,"l'argomento " + self.namefile + " e' stato aggiunto")
                Query_message.argomentipiupremuto = 0
            else:
                self.bot.sendMessage(self.chat,"file non supportato")
                Query_message.argomentipiupremuto = 0

        except:
            self.bot.sendMessage(self.chat,"argomento gia' esistente")
            Query_message.argomentipiupremuto = 0

    def argomentipiuphoto(self,cartella):
        try:
            self.bot.download_file(Query_message.photoidtemp, Query_message.tempdir + self.text)
            self.bot.sendMessage(self.chat, "argomento inserito con successo")
            Query_message.argomentipiupremuto = 0
        except:
            self.bot.sendMessage(self.chat, "argomento gia' esistente")
            Query_message.argomentipiupremuto = 0



    def eventipiu(self,cartella):
        if self.text == "/eventipiu" or self.text == "/eventipiu@diarioitisbot": 
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
            f = open(cartella + "temp", "w+")
            f.close()
            f = open(cartella + "temp", "a")
            for x in os.listdir(cartella):
                if x != "domani.txt" and x != "mese.txt" and x != "scuolalavoro.jpg" and x != "orario.jpg" and x != "argomenti.txt" and x != "temp" and x != "alunni":
                    f.write("\n" + x)
            f.close()
            f = str(open(cartella + "temp","r").read())
            try:
                self.bot.sendMessage(self.chat,f)
                self.bot.sendMessage(self.chat, "seleziona la materia")
                Query_message.eventipiupremuto = 1
            except:
                self.bot.sendMessage(self.chat,"non ci sono materie, inserirle con /materiapiu")
                Query_message.eventipiupremuto = 0
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
            Query_message.chatpremuto = self.chat
        
    def eventipiubis(self,cartella):
        if os.path.isdir(cartella + self.text):
            if os.path.isfile(cartella + "temp") == 0:
                f = open(cartella + "temp", "w+")
                f.close()
            f = open(cartella + "temp","w")
            for x in os.listdir(cartella + self.text):
                f.write(x)
                f.write("\n")
            f.close()
            f = str(open(cartella + "temp","r").read())
            try:
                self.bot.sendMessage(self.chat,f)
                self.bot.sendMessage(self.chat,"inserire l'evento da creare")
                Query_message.eventipiupremuto = 2
                Query_message.tempdir = cartella + self.text + "/"
            except:
                self.bot.sendMessage(self.chat,"nessun evento")
                self.bot.sendMessage(self.chat,"inserire l'evento da creare")
                Query_message.tempdir = cartella + self.text + "/"
                Query_message.eventipiupremuto = 2
            os.remove(cartella + "temp")
        else:
            self.bot.sendMessage(self.chat, "la materia non esiste, creane una con /materiapiu")
            Query_message.eventipiupremuto = 0

    def eventipiubisbis(self,cartella,tipo):
        if tipo == "text":
            if os.path.isdir(Query_message.tempdir + self.text):
                self.bot.sendMessage(self.chat,"l'evento esiste gia'")
                Query_message.eventipiupremuto = 0
            else:
                try:
                    os.makedirs(Query_message.tempdir + self.text)
                    self.bot.sendMessage(self.chat, "l'evento " + self.text + " e' stato creato")
                    Query_message.eventipiupremuto = 0
                except:
                    self.bot.sendMessage(self.chat,"inserire del testo")
                    Query_message.eventipiupremuto = 0
        else:
            self.bot.sendMessage("inviare del testo")
            Query_message.eventipiupremuto = 0
    
    def appunti(self,cartella):
        if self.text == "/appunti" or self.text == "/appunti@diarioitisbot": 
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
            f = open(cartella + "temp", "w+")
            f.close()
            f = open(cartella + "temp", "a")
            for x in os.listdir(cartella):
                if x != "domani.txt" and x != "mese.txt" and x != "scuolalavoro.jpg" and x != "orario.jpg" and x != "argomenti.txt" and x != "temp" and x != "alunni":
                    f.write("\n" + x)
            f.close()
            f = str(open(cartella + "temp","r").read())
            try:
                self.bot.sendMessage(self.chat,f)
                self.bot.sendMessage(self.chat, "seleziona la materia")
                Query_message.appuntipremuto = 1
            except:
                self.bot.sendMessage(self.chat,"non ci sono materie, inserirle con /materiapiu")
                Query_message.appuntipremuto = 0
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")
            Query_message.chatpremuto = self.chat
    
    def appuntibis(self,cartella,tipo): 
        if os.path.isdir(cartella + self.text) and not self.text.startswith("/"):
            if not os.path.isfile(cartella + "temp"):
                f = open(cartella + "temp","w+")
                f.close()
            if tipo == "text":
                f = open(cartella + "temp","a") 
                for x in os.listdir(cartella + self.text):
                    f.write("\n" + x)
                f.close()
                f = str(open(cartella + "temp","r").read())
                try:
                    self.bot.sendMessage(self.chat,f)
                    self.bot.sendMessage(self.chat,"inserire l'evento")
                    Query_message.appuntipremuto= 2
                    Query_message.tempdir = cartella + self.text + "/"
                except:
                    self.bot.sendMessage(self.chat,"non ci sono eventi")
                    Query_message.appuntipremuto = 0
            else:
                self.bot.sendMessage(self.chat,"inserire del testo")
                Query_message.appuntipremuto = 0
        elif self.text.startswith("/"):
            Query_message.appuntipremuto = 0
        else:
            self.bot.sendMessage(self.chat,"non ci sono materie")
            Query_message.appuntipremuto = 0
        if os.path.isfile(cartella + "temp"):
            os.remove(cartella + "temp")

    def appuntibisbis(self,cartella,tipo):
        if os.path.isdir(Query_message.tempdir + self.text) and not self.text.startswith("/"):
            for x in (os.listdir(Query_message.tempdir + self.text)):
                if tipo == "text":
                    try:
                        self.bot.sendDocument(self.chat, open(Query_message.tempdir + self.text + "/" + x,"rb"))
                    except:
                        self.bot.sendMessage(self.chat, "non ci sono argomenti, inseriscili con /argomentipiu")
                else:
                    self.bot.sendMessage(self.chat, "inserire del testo")
            Query_message.appuntipremuto = 0
        else:
            self.bot.sendMessage(self.chat,"l'evento non esiste")
            Query_message.appuntipremuto = 0
            if os.path.isfile(cartella + "temp"):
                os.remove(cartella + "temp")

    def classe(self):
        if self.text == "/classe" or self.text == "/classe@diarioitisbot":
            self.bot.sendMessage(self.chat,"inserire tutti i cognomi della classe separati da uno spazio")
            Query_message.classepremuto = 1
            Query_message.chatpremuto = self.chat
    def classebis(self,cartella,tipo):
        if os.path.isfile(cartella + "alunni"):
            os.remove(cartella + "alunni")
            open(cartella + "alunni","w+")
        else:
            open(cartella + "alunni","w+")
        f = open(cartella + "alunni","w")
        if tipo == "text":
            array = self.text.split(" ")[:]
            for x in array:
                f.write(x + "\n")
            f.close()
            self.bot.sendMessage(self.chat,"la classe e' stata salvata")
        else:
            self.bot.sendMessage(self.chat, "inviare del testo")
        Query_message.classepremuto = 0

    def random(self,cartella):
        if self.text == "/random" or self.text == "/random@diarioitisbot":
            if os.path.isfile(cartella + "alunni"):
                contatore = 0
                cicli = 0
                alunni = []
                f = open(cartella + "alunni","r")
                for x in f.readlines():
                    alunni.append(x)
                    contatore = contatore + 1
                f.close()
                numeri = []
                while (cicli < contatore):
                    x = random.randint(0,contatore-1)
                    if x not in numeri:
                        numeri.append(x)
                        cicli = cicli + 1
                cicli = 0
                if os.path.isfile(cartella + "temp"):
                    os.remove(cartella + "temp")
                f = open(cartella + "temp","w+")
                while (cicli < contatore):
                    f.write(alunni[numeri[cicli]])
                    cicli = cicli+1
                f.close()
                f = open(cartella + "temp","r")
                self.bot.sendMessage(self.chat,str(f.read()))
                f.close()
            else:
                self.bot.sendMessage(self.chat, "non c'e' una classe,aggiungila con /classe")
                    


    def help(self):
        if (self.text == "/help" or self.text == "/help@diarioitisbot"):
            self.bot.sendMessage(self.chat, """ /orario - stampa l'orario della classe\n\n
/orariopiu - cambia la foto dell'orario\n\n
/scuolalavoro - stampa l'orario delle lezioni di scuola lavoro\n\n
/scuolalavoropiu - cambia la foto dell'orario di scuola lavoro\n\n
/domani - stampa cio' che c'e' 'da fare per domani\n\n
/domanipiu - aggiunge un compito da fare oggi\n\n
/mese - stampa tutti gli avvenimenti importanti del mese\n\n
/mesepiu - aggiunge un avvenimento al mese\n\n
/argomenti - stampa gli argomenti in base alla materia(testo)\n\n
/materiapiu - aggiunge una materia\n\n
/eventipiu - aggiunge un evento(interrogazioni,verifiche)\n\n
/argomentipiu - aggiunge un argomento(file)\n\n
/appunti - stampa gli appunti(file)\n\n
/classe - definisce i cognomi della classe\n\n
/random - genera una lista random di cognomi in classe\n\n
/help - stampa l'aiuto\n\n
""")

















#mi creo l'oggetto telepot
bot = telepot.Bot("Insert Your Token")
##ciclo con acquisizione di dati derivanti da msg
def handle(msg):
    ##acquisizione chat,text ed msg(contenente tutti i dati)
    chat = (msg["chat"])["id"]
    ##parte relativa ai file dell'utente(ogni user ha la sua cartella ed i suoi file)
    countmessaggio = 0
    countmessaggio = countmessaggio+1
    cartella_oggetto =  Dir_file(str(pathlib.Path.home()) + "/.diariobot/diario/" + str(chat) + "/")
    if countmessaggio == 1:
        if cartella_oggetto.esiste():
            if cartella_oggetto.cisonofile():
                if cartella_oggetto.cisonofileesatti():
                    print("la cartella verra' utilizzata naturalmente")
                else:
                    cartella_oggetto.creafile()
            else:
                cartella_oggetto.creafile()
        else:
            cartella_oggetto.non_esiste()
            cartella_oggetto.creafile()
    ##fine parte
    messaggio_oggetto = Query_message(msg,chat,bot)
    messaggio_oggetto.tipo()

    #log
    print(cartella_oggetto.stampa(), end=" ")
    if messaggio_oggetto.tipo() == "text":
        print(msg["text"],end=" ")
    try:
        print(msg["from"]["username"],end=" ")
    except:
        print("nousername",end=" ")
    print(str(chat), end="\n")

    #help
    messaggio_oggetto.help()

    ##relativo all'orario
    messaggio_oggetto.orario(cartella_oggetto.stampa())
    if Query_message.premuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.orariopiubis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.orariopiu()

    ##relativo a scuola lavoro
    messaggio_oggetto.scuolalavoro(cartella_oggetto.stampa())
    if Query_message.scuolapremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.scuolalavoropiubis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.scuolalavoropiu()

    ##relativo a domani 
    messaggio_oggetto.domani(cartella_oggetto.stampa())
    if Query_message.domanipiupremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.domanipiubis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.domanipiu()

    ##relativo a mese
    messaggio_oggetto.mese(cartella_oggetto.stampa())
    if Query_message.mesepiupremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.mesepiubis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.mesepiu()

    ##relativo alla stampa degli argomenti
    if Query_message.argomentipremuto == 2 and Query_message.chatpremuto == chat:
            messaggio_oggetto.argomentibisbis(cartella_oggetto.stampa())
    elif Query_message.argomentipremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.argomentibis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.argomenti(cartella_oggetto.stampa())

    #relativo all'aggiunta di materie
    if Query_message.materiapiupremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.materiapiubis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.materiapiu()

    #relativo all'aggiunta di argomenti
    if Query_message.argomentipiupremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.argomentipiubis(cartella_oggetto.stampa())
    elif Query_message.argomentipiupremuto == 2 and Query_message.chatpremuto == chat:
        messaggio_oggetto.argomentipiubisbis(cartella_oggetto.stampa())
    elif Query_message.argomentipiupremuto == 3 and Query_message.chatpremuto == chat:
        messaggio_oggetto.argomentipiubisbisbis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    elif Query_message.argomentipiupremuto == 4 and Query_message.chatpremuto == chat:
        messaggio_oggetto.argomentipiuphoto(cartella_oggetto.stampa())
    else:
        messaggio_oggetto.argomentipiu(cartella_oggetto.stampa())

    #relativo all'aggiunta degli eventi
    if Query_message.eventipiupremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.eventipiubis(cartella_oggetto.stampa())
    elif Query_message.eventipiupremuto == 2 and Query_message.chatpremuto == chat:
        messaggio_oggetto.eventipiubisbis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.eventipiu(cartella_oggetto.stampa())

    #relativo all'invio di file di appunti
    if Query_message.appuntipremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.appuntibis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    elif Query_message.appuntipremuto == 2 and Query_message.chatpremuto == chat:
        messaggio_oggetto.appuntibisbis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.appunti(cartella_oggetto.stampa())

    #relativo all'inserimento della classe
    if Query_message.classepremuto == 1 and Query_message.chatpremuto == chat:
        messaggio_oggetto.classebis(cartella_oggetto.stampa(),messaggio_oggetto.tipo())
    else:
        messaggio_oggetto.classe()

    #relativo alla generazione e stampa randomica dei nomi della classe
    messaggio_oggetto.random(cartella_oggetto.stampa())



telepot.loop.MessageLoop(bot, handle).run_as_thread()


while 1:
    time.sleep(0.001)
    if str(datetime.datetime.now().strftime("%H")) == "01": 
        for x in glob.iglob(str(pathlib.Path.home()) + "/.diariobot/diario/*/domani.txt",recursive=True ):
            f = open(x,"w")
            f.write(datetime.datetime.now().strftime("%d" +"/"+ "%m" + "/" + "%Y"))
            f.close()
    if str(datetime.datetime.now().strftime("%d")) == "01":
        for x in glob.iglob(str(pathlib.Path.home()) + "/.diariobot/diario/*/mese.txt",recursive=True ):
            f = open(x,"w")
            f.write(datetime.datetime.now().strftime("%m" + "/" + "%Y"))
            f.close()
