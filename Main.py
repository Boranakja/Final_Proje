from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd
#Kullanılacak dosyaları aktarıyoruz.
try:
    personel1 = Personel(1, "Ahmet", "Yılmaz", "Yönetim", 5000)
    personel2 = Personel(2, "Ayşe", "Kara", "İdari", 4500)
    print(personel1)
    print(personel2)
#Personelleri ve ilgli bilgilerini giriyoruz
    doktor1 = Doktor(3, "Ali", "Can", "Cerrahi", 7000, "Kalp", 10, "Ankara Hastanesi")
    doktor2 = Doktor(4, "Mehmet", "Tan", "Dahiliye", 6500, "Gastroenteroloji", 8, "İstanbul Hastanesi")
    doktor3 = Doktor(5, "Sinem", "Öztürk", "Pediatri", 7200, "Çocuk Sağlığı", 6, "İzmir Hastanesi")
    print(doktor1)
    print(doktor2)
    print(doktor3)
#Doktorları ve ilgili bilgilerini giriyoruz
    hemsire1 = Hemsire(6, "Zeynep", "Aydın", "Servis", 3000, 40, "Yoğun Bakım", "Ankara Hastanesi")
    hemsire2 = Hemsire(7, "Cem", "Demir", "Servis", 3200, 35, "Ameliyathane", "İstanbul Hastanesi")
    hemsire3 = Hemsire(8, "Elif", "Çelik", "Poliklinik", 2800, 30, "Poliklinik", "İzmir Hastanesi")
    print(hemsire1)
    print(hemsire2)
    print(hemsire3)
#Hemsireleri ve ilgili bilgileri giriyoruz
    hasta1 = Hasta(9, "Ece", "Yılmaz", "1990-01-01", "Grip", "İlaç Tedavisi")
    hasta2 = Hasta(10, "Can", "Kaya", "1985-05-05", "Kırık", "Ameliyat")
    hasta3 = Hasta(11,"Banu", "Demir", "2000-08-15", "Kanser", "Kemoterapi")
    print(hasta1)
    print(hasta2)
    print(hasta3)

    data = [
        [personel1.get_personel_no(), personel1.get_ad(), personel1.get_soyad(), personel1.get_departman(), personel1.get_maas(), None, None, None, None, None, None, None, None, None],
        [personel2.get_personel_no(), personel2.get_ad(), personel2.get_soyad(), personel2.get_departman(), personel2.get_maas(), None, None, None, None, None, None, None, None, None],
        [doktor1.get_personel_no(), doktor1.get_ad(), doktor1.get_soyad(), doktor1.get_departman(), doktor1.get_maas(), doktor1.get_uzmanlik(), doktor1.get_deneyim_yili(), doktor1.get_hastane(), None, None, None, None, None, None],
        [doktor2.get_personel_no(), doktor2.get_ad(), doktor2.get_soyad(), doktor2.get_departman(), doktor2.get_maas(), doktor2.get_uzmanlik(), doktor2.get_deneyim_yili(), doktor2.get_hastane(), None, None, None, None, None, None],
        [doktor3.get_personel_no(), doktor3.get_ad(), doktor3.get_soyad(), doktor3.get_departman(), doktor3.get_maas(), doktor3.get_uzmanlik(), doktor3.get_deneyim_yili(), doktor3.get_hastane(), None, None, None, None, None, None],
        [hemsire1.get_personel_no(), hemsire1.get_ad(), hemsire1.get_soyad(), hemsire1.get_departman(), hemsire1.get_maas(), None, None, None, hemsire1.get_calisma_saati(), hemsire1.get_sertifika(), hemsire1.get_hastane(), None, None, None],
        [hemsire2.get_personel_no(), hemsire2.get_ad(), hemsire2.get_soyad(), hemsire2.get_departman(), hemsire2.get_maas(), None, None, None, hemsire2.get_calisma_saati(), hemsire2.get_sertifika(), hemsire2.get_hastane(), None, None, None],
        [hemsire3.get_personel_no(), hemsire3.get_ad(), hemsire3.get_soyad(), hemsire3.get_departman(), hemsire3.get_maas(), None, None, None, hemsire3.get_calisma_saati(), hemsire3.get_sertifika(), hemsire3.get_hastane(), None, None, None],
        [hasta1.get_hasta_no(), hasta1.get_ad(), hasta1.get_soyad(), None, None, None, None, None, None, None, None, hasta1.get_dogum_tarihi(), hasta1.get_hastalik(), hasta1.get_tedavi()],
        [hasta2.get_hasta_no(), hasta2.get_ad(), hasta2.get_soyad(), None, None, None, None, None, None, None, None, hasta2.get_dogum_tarihi(), hasta2.get_hastalik(), hasta2.get_tedavi()],
        [hasta3.get_hasta_no(), hasta3.get_ad(), hasta3.get_soyad(), None, None, None, None, None, None, None, None, hasta3.get_dogum_tarihi(), hasta3.get_hastalik(), hasta3.get_tedavi()]
    ]
# Data Frame oluşturmak için 'Hemsire','Doktor','Personel','Hasta' sınıflarından oluşturulmuş nesnelerin özelliklerini içeren bir veri listesi oluşturulur. Daha sonra bu pandas ile DataFrame'e dönüştürülür
    df = pd.DataFrame(data, columns=['No', 'Ad', 'Soyad', 'Departman', 'Maas', 'Uzmanlik', 'Deneyim Yili', 'Hastane', 'Calisma Saati', 'Sertifika', 'Hastane', 'Dogum Tarihi', 'Hastalik', 'Tedavi'])

    # Boş olan değişken değerleri için 0 atanır.
    df.fillna(0, inplace=True)

    # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplar ve yazar
    doktor_grup = df[df['Uzmanlik'] != 0].groupby('Uzmanlik').size()
    print("Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısı:")
    print(doktor_grup)

    # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulur.
    deneyim_5_yil_ustu = df[(df['Deneyim Yili'] > 5)].shape[0]
    print(f"5 yıldan fazla deneyime sahip doktorların toplam sayısı: {deneyim_5_yil_ustu}")

    # Hasta adına göre DataFrame’i alfabetik olarak sıralar ve yazar.
    df_hastalar = df[df['Dogum Tarihi'] != 0].sort_values(by='Ad')
    print("Hasta adına göre sıralanmış DataFrame:")
    print(df_hastalar)

    # Maaşı 7000 TL üzerinde olan personelleri bulur ve yazar
    maas_7000_ustu = df[df['Maas'] > 7000]
    print("Maaşı 7000 TL üzerinde olan personeller:")
    print(maas_7000_ustu)

    # Doğum tarihi 1990 ve sonrası olan hastaları gösterir.
    df['Dogum Tarihi'] = pd.to_datetime(df['Dogum Tarihi'], errors='coerce')
    dogum_1990_sonrasi = df[(df['Dogum Tarihi'] >= '1990-01-01')]
    print("Doğum tarihi 1990 ve sonrası olan hastalar:")
    print(dogum_1990_sonrasi)

    # Var olan DataFrame’den ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi bilgilerini içeren yeni bir DataFrame elde ediniz ve yazdırır.
    yeni_df = df[['Ad', 'Soyad', 'Departman', 'Maas', 'Uzmanlik', 'Deneyim Yili', 'Hastalik', 'Tedavi']]
    print("Yeni DataFrame:")
    print(yeni_df)

except Exception as e:
    print(f"Bir hata oluştu: {e}")
