class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas
#Personel sınıfı ve bu sınıfın özniteliklerini oluşturuyoruz
    def get_personel_no(self):
        return self.__personel_no
#personel no'sıyla yeni fonksiyon tanımlıyoruz.
    def set_personel_no(self, personel_no):
        self.__personel_no = personel_no
#personel no değişkenine yeni değer atamak için fonksiyon
    def get_ad(self):
        return self.__ad
#ad'la çağırmak için fonksiyon
    def set_ad(self, ad):
        self.__ad = ad
#ad'a yeni değer atamak için
    def get_soyad(self):
        return self.__soyad
#soyadı çağırmak için
    def set_soyad(self, soyad):
        self.__soyad = soyad
#soyad'a yeni değer atamak için
    def get_departman(self):
        return self.__departman
#departmanı çağır
    def set_departman(self, departman):
        self.__departman = departman
#departmana yeni değer ata
    def get_maas(self):
        return self.__maas
#maas'ı cağır
    def set_maas(self, maas):
        self.__maas = maas
#maas'a yeni değer ata
    def __str__(self):
        return f"Personel No: {self.__personel_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Departman: {self.__departman}, Maaş: {self.__maas}"
