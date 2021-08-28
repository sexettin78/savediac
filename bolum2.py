import time,sys,random,os

def hatali_eksik():
    print('!Eksik ya da Hatalı tuşlama!')


print("""\033[96m\n Goblini yendikten sonra goblinin bıçağını aldın.Goblinin cebinde bir kağıt parçası ve bir maymuncuk buldun
kağıtta 3.kapı yazıyordu,biraz ilerledikten sonra önümde sıralanmış 4 tane kapı gördüm sanki herşey önceden planlanmıştı ve birileri hayatımla oynuyordu.İlerledim ve 
3. kapıyı maymuncuk ile açmayı başardım.Kapıyı açar açmaz karşıma sarı bir örümcek atladı.Canımın yandığını hissettim,Sanırım beni zehirledi! Yaşamak için Dövüş!\n""")


print("""
Sarı Örümcek;
Vuruş : 3
Can : 5
Enerji : 50
Ekipman : Zehirli Dişler

******************

Zordiac;
Vuruş : 2
Can : 7
Enerji : 70
Ekipman : Goblin Bıçağı

Rakibin canı veya enerjisi 0 altına inerse veya puanınız 100 olursa kazanırsınız.Aynısı rakip için de geçerli
""")

def nokta_ekle():
    print(".")
    time.sleep(0.4)
    print("..")
    time.sleep(0.4)
    print("...")
    time.sleep(0.4)


class oyuncu():
    def __init__(self,isim,can=7,power=70,puan=0):
        self.isim = isim
        self.can = can
        self.power = power
        self.puan = puan
        
    def bilgileri_goster(self):
        print("""
        Karakter: {}
        Can: {}
        Enerji: {}
        Puan: {}
        """.format(self.isim,self.can,self.power,self.puan)) 

        
    def saldir(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            dusman.power -= 8 
            self.power -= 4
            self.puan += 10
            dusman.can -= 2
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSaldırı Başarılı")
            
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 3
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSaldırı Başarısız")

    def  savun(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            self.power -= 4
            dusman.power -= 8
            self.puan += 10
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSavunma Başarılı")
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 3
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSavunma Başarısız")

    def saldir_savun_sayi(self):
        return random.randint(1,2)

    def exit(self):
        print("Oyun Kapatılıyor...")
        nokta_ekle()
        sys.exit()

    


oyuncu1 = oyuncu("Zordiac")
oyuncu2 = oyuncu("Sarı Örümcek")




nokta_ekle()

while True:
    hamle = input("""
    1-Saldır
    2-Savun
    3-Çık
    Hamle Seçimi:
    """)
    if(hamle=="1"):
        oyuncu1.saldir(oyuncu2)

    elif(hamle=="2"):
        oyuncu1.savun(oyuncu2)
    elif(hamle=="3"):
        oyuncu1.exit()
    else:
        hatali_eksik()


    if(oyuncu1.puan==100 or oyuncu2.can <= 0 or oyuncu2.power <= 0 ):
        print("\033[92m\nÖrümceği Yendin Hikaye devam ediyor...")
        time.sleep(3)
        import bolum3
        break
    if(oyuncu2.puan==100 or oyuncu1.can <= 0 or oyuncu1.power <= 0 ):
        hsec = input("\033[91m\nOyunu Kaybettin,Örümceğe yenildin! Bu bölüme Baştan başlamak ister misin? e/y")
        if(hsec=="e" or hsec=="E"):
            import bolum2
            break
        elif(hsec=="h" or hsec=="H"):
            sys.exit

    if(oyuncu2.can == 5 or oyuncu2.can == 3 or oyuncu2.can==6):
        oyuncu2.can -= 2
        oyuncu2.power -= 20
         
