x = input("isminiz : ")
y = int(input("yasiniz : "))
z = input("egitim durumunuz : ")

degisken = (y>=19) 
degisken2 = ((z=="lise") or (z=="üniversite"))

if degisken :
    if degisken2 :
        print("ehliyet almaniz onunde resmi bir engel yok")
    else :
        print("ehliyet alamazsiniz cunku egitim seviyeniz buna uygun degil")
else : 
    print("ehliyet alamazsiniz cunku yasiniz buna uygun degil ")



