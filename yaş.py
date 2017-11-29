ad=input("adın:")
soyad=input("soyadın:")
yas=int(input("yaşınız:"))
if(yas<=2):
    print(ad, soyad, "bebeksiniz")
elif(yas<=6):
    print(ad, soyad, "çocuksunuz")
elif(yas<=19):
    print(ad, soyad, "ergensiniz")
elif(yas<=35):
    print(ad, soyad, "gençsiniz")
elif(yas<=55):
    print(ad, soyad, "orta yaşlısınız")
elif(yas<=65):
    print(ad, soyad, "yaşlısınız")
else:
    print(ad, soyad, "çınar gibisiniz.")
 
