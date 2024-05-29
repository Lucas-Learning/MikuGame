import time
import datetime
class mikuGame():
    def __init__(self):
        print("Velkomme til project diva!\n")
    def rhythmGame():
        while(True):
          Game = input("Spil rhythm game - tryk 1\nClose project diva - tryk 2\n")
          if Game == "1":
            print("Song list:\n oha yo del - 1\n\n spillet går ud på at have en hurtig reactions tid\n hvor spillet tæller for hvor hurtigt noden kommer til du trykker enter\n\n tryk 1 for at starte")
            songChoice = input()
            if songChoice == "1":
                rhythm = "Ta"
                print("Du spiller oha yo del med: ",Chr.OutfitNavn)
                while(True):
                   time.sleep(2)
                   then = datetime.datetime.now()
                   t = input(rhythm)
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time1 = round(abs(diff.total_seconds()), 2)

                   time.sleep(0.8)
                   then = datetime.datetime.now()
                   t = input(rhythm)
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time2 = round(abs(diff.total_seconds()), 2)

                   time.sleep(0.8)
                   then = datetime.datetime.now()
                   t = input(rhythm)
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time3 = round(abs(diff.total_seconds()), 2)

                   time.sleep(0.5)
                   then = datetime.datetime.now()
                   t = input("du")
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time4 = round(abs(diff.total_seconds()), 2)

                   time.sleep(0.3)
                   then = datetime.datetime.now()
                   t = input("du")
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time5 = round(abs(diff.total_seconds()), 2) 

                   time.sleep(0.3)
                   then = datetime.datetime.now()
                   t = input("du")
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time6 = round(abs(diff.total_seconds()), 2)

                   print("")
                   time.sleep(0.8)
                   then = datetime.datetime.now()
                   t = input(rhythm)
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time7 = round(abs(diff.total_seconds()), 2) 

                   time.sleep(0.8)
                   then = datetime.datetime.now()
                   t = input(rhythm)
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time8 = round(abs(diff.total_seconds()), 2) 

                   time.sleep(0.8)
                   then = datetime.datetime.now()
                   t = input(rhythm)
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time9 = round(abs(diff.total_seconds()), 2)  

                   time.sleep(0.5)
                   then = datetime.datetime.now()
                   t = input("du")
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time10 = round(abs(diff.total_seconds()), 2)    

                   time.sleep(0.3)
                   then = datetime.datetime.now()
                   t = input("du")
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time11 = round(abs(diff.total_seconds()), 2) 

                   time.sleep(0.3)
                   then = datetime.datetime.now()
                   t = input("du")
                   now = datetime.datetime.now()
                   diff = then-now
                   reaction_time12 = round(abs(diff.total_seconds()), 2) 

                   endelig = reaction_time1+reaction_time2+reaction_time3+reaction_time4+reaction_time5+reaction_time6+reaction_time7+reaction_time8+reaction_time9+reaction_time10+reaction_time11+reaction_time12
                   if endelig<2:
                      print(f"perfect - du klarede den på {endelig}")
                   elif endelig<3:
                      print(f"excellent - du klarede den på {endelig}")
                   elif endelig<4:
                      print(f"great - du klarede den på {endelig}")
                   elif endelig<5:
                      print(f"clear - du klarede den på {endelig}")
                   elif endelig<6:
                      print(f"you're soooo bad - du klarede den på {endelig}")
                   break    
          elif Game == "2":
            print("See you next time")
            return
class createChr:
    def __init__(self, OutfitNavn, Gender, HairColor, Hat, Glasses, Wings):
        self.OutfitNavn = OutfitNavn
        self.Gender = Gender
        self.HairColor = HairColor
        self.Hat = Hat
        self.Glasses = Glasses
        self.Wings = Wings

        print(f"Du har oprettet en {self.Gender} karakter med følgende attributter:")
        print(f"- Outfit navn: {self.OutfitNavn}")
        print(f"- Hår farve: {self.HairColor}")
        print(f"- Hat: {self.Hat}")
        print(f"- Briller: {self.Glasses}")
        print(f"- Vinger: {self.Wings}\n")
mikuGame()
Chr = createChr(input("Skriv outfit navn: "),
                      input("Mand eller kvinde\nSkriv køn: "),
                      input("Skriv hår farve: "),
                      input("Vil du have en hat?\nja/nej\n"),
                      input("Vil du have briller?\nja/nej\n"),
                      input("Vil du have vinger?\nja/nej\n"))
mikuGame.rhythmGame()