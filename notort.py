import tkinter as tk
from tkinter import *
def bilgiekle():
    ad = adtext.get()
    soyad = soyadtext.get()
    not1 = not1text.get()
    not2 = not2text.get()
    adtext.delete(0, END)
    soyadtext.delete(0, END)
    not1text.delete(0, END)
    not2text.delete(0, END)

    with open("notlistesi.txt", "a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+"\n")
        file.close()
def ortalama():
    sonuc.delete(1.0,END)
    with open("notlistesi.txt", "r", encoding="utf-8") as file:
        for veri in file:
            liste = veri.split(":")
            ogrenci = liste[0]
            notlar = liste[1]
            notlar = notlar.split(",")
            not1 = int(notlar[0])
            not2 = int(notlar[1])
            ogrort: float= ((0.4*not1)+(0.6*not2))
            if ogrort>=90 and ogrort<=100:
                harf="AA Geçti"
            elif ogrort>=80 and ogrort<=89:
                harf = "BA Geçti"
            elif ogrort>=70 and ogrort<=79:
                harf = "BB Geçti"
            elif ogrort>=60 and ogrort<=69:
                harf = "CB Geçti"
            elif ogrort>=50 and ogrort<=59:
                harf = "CC Geçti"
            elif ogrort>=40 and ogrort<=49:
                harf = "DC Sorumlu"
            elif ogrort>=30 and ogrort<=39:
                harf = "DD Kaldı"
            else:
                harf = "FF Kaldı"

            sonuc.insert(tk.END, f"{ogrenci}: {ogrort} / {harf}\n")
def sınıfort():
    sonuc.delete(1.0, END)
    with open("notlistesi.txt", "r", encoding="utf-8") as file:
        satirsayisi= len(file.readlines())

    with open("notlistesi.txt", "r", encoding="utf-8") as file:
        toplam=0

        for veri in file:

            liste = veri.split(":")

            notlar = liste[1]
            notlar = notlar.split(",")
            not1 = int(notlar[0])
            not2 = int(notlar[1])
            ogrort = float((0.4 * not1) + (0.6 * not2))
            toplam += ogrort

        sinifortalamasi: float= toplam / satirsayisi

        if sinifortalamasi >= 90 and sinifortalamasi <= 100:
            harf = "AA"
        elif sinifortalamasi >= 80 and sinifortalamasi <= 89:
            harf = "BA"
        elif sinifortalamasi >= 70 and sinifortalamasi <= 79:
            harf = "BB"
        elif sinifortalamasi >= 60 and sinifortalamasi <= 69:
            harf = "CB"
        elif sinifortalamasi >= 50 and sinifortalamasi <= 59:
            harf = "CC"
        elif sinifortalamasi >= 40 and sinifortalamasi <= 49:
            harf = "DC"
        elif sinifortalamasi >= 30 and sinifortalamasi <= 39:
            harf = "DD"
        else:
            harf = "FF"

        sonuc.insert(tk.END, f"Toplam Öğrenci Sayısı: {satirsayisi}\nSınıf Ortalaması: {sinifortalamasi}\nHarf Notu: {harf}\n")

def sil():
    with open("notlistesi.txt", "w", encoding="utf-8") as file:
        file.close()
    sonuc.delete(1.0, END)


pencere = tk.Tk()
pencere.geometry("400x820")
pencere.title("Not Ortalaması")
adlabel = tk.Label(text="Ad:")
soyadlabel = tk.Label(text="Soyad:")
not1label = tk.Label(text= "1.Not:")
not2label = tk.Label(text= "2.Not:")
adtext = tk.Entry()
soyadtext = tk.Entry()
not1text = tk.Entry()
not2text = tk.Entry()
ekle = tk.Button(text="Ekle",width=10,command=bilgiekle)
ortalama= tk.Button(text="Ortalama",width=10,command=ortalama)
sınıfortalama= tk.Button(text="Sınıf Ortalaması",width=10,command=sınıfort)
listesil = tk.Button(text="Listeyi Sil",width=10,command=sil)
sonuc= tk.Text(pencere,width=55,height=50)
sonuclabel = tk.Label(text="SONUC")

adlabel.grid(row=0, column=0, pady=1, padx=5)
soyadlabel.grid(row=1, column=0, pady=1, padx=5)
not1label.grid(row=2, column=0, pady=1, padx=5)
not2label.grid(row=3, column=0, pady=1, padx=5)
adtext.grid(row=0, column=1, pady=1, padx=5)
soyadtext.grid(row=1,column=1,pady=1,padx=5)
not1text.grid(row=2,column=1,pady=1,padx=5)
not2text.grid(row=3,column=1,pady=1,padx=5)
ekle.grid(row=0, column=3, pady=1, padx=5)
ortalama.grid(row=1, column=3, pady=1, padx=1)
sınıfortalama.grid(row=2, column=3, pady=1, padx=1)
listesil.grid(row=3, column=3, pady=1, padx=1)
sonuc.place(x=5,y=150)
sonuclabel.grid(row=4, column=0, columnspan=4)

pencere.mainloop()