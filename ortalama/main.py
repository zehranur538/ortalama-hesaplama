def ortalama_hesapla(sayilar):
    toplam = sum(sayilar)
    ortalama = toplam / len(sayilar)
    return ortalama

def main():
    try:
        # Kullanıcıdan kaç tane sayı gireceğini iste
        n = int(input("Kaç tane sayı gireceksiniz? "))

        # Kullanıcıdan sayıları al
        sayilar = []
        for i in range(n):
            sayi = float(input("{}. sayıyı girin: ".format(i + 1)))
            sayilar.append(sayi)

        # Ortalamayı hesapla ve ekrana yazdır
        ortalama = ortalama_hesapla(sayilar)
        print("Girdiğiniz sayıların ortalaması:", ortalama)

    except ValueError:
        print("Lütfen geçerli bir sayı girin!")

if __name__ == "__main__":
    main()