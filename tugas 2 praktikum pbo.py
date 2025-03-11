import random

class Mobil:
    def __init__(self, nama):  
        self.nama = nama
        self.jarak = 0

    def maju(self):
        kecepatan = random.randint(5, 15)  
        self.jarak += kecepatan
        print(f"{self.nama} melaju sejauh {kecepatan} km!")

def balapan(mobil1, mobil2):
    while mobil1.jarak < 100 and mobil2.jarak < 100:
        print(f"\n{mobil1.nama} [Jarak: {mobil1.jarak} km] | {mobil2.nama} [Jarak: {mobil2.jarak} km]")

        input(f"{mobil1.nama}, tekan ENTER untuk melaju...")
        mobil1.maju()

        input(f"{mobil2.nama}, tekan ENTER untuk melaju...")
        mobil2.maju()

    pemenang = mobil1 if mobil1.jarak >= 100 else mobil2
    print(f"\n{pemenang.nama} mencapai garis finis dan menang!")


mobil1 = Mobil("Porsche")  
mobil2 = Mobil("Mustang")


balapan(mobil1, mobil2)