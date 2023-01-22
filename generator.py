#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Image
from tkinter import Label
from tkinter import LabelFrame
from tkinter import font
from tkinter.ttk import Style
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from tkinter import messagebox
import random
import os
#from  openpyxl import *



######################################################################################################################################################
"""VERİTABANI OLUŞTURULUYOR..."""
######################################################################################################################################################

#isim keywords veritabanı
vt_pt1=['hid','jen','hel','yum','lit','ber','il','bor','car','kar','bon','nit','ro','ok','si','ne','on','sod','mag','nez','al','min','lis','fos','for','li','con','sul',
'fur','ar','gon','po','tas','kal','skan','di','ti','tan','va','nad','man','ga','gan','de','mir','ko','balt','ni','kel','ba','kir','gal','ger','se','nik','len',
'ton','ru','bid','it','ri','zir','kon','ob','mo','lib','den','tek','nes','ten','rod','pa','lad','kad','mi','in','ka','lay','an','mon','tel','i','yot','ki','non',
'sez','bar','haf','tal','vol','fram','ren','os','rid','la','tin','kur','biz','mut','lon','as','ta','sit','ra','don','ran','rad','rut','her','dub','gi','gen','per',
'ho','ver','mor','rov','son','lan','ser','dim','sa','mar','ev','pi','do','lin','ter','bi','dis','roz','er','tul','lu','tes','ak','tor','tak','u','nep','me','rik',
'fer','men','lev','no','bel','lav','si']

#karakter tipleri
vt_kt1=['Mimar:INTJ-A / INTJ-T','Mantıkçı:INTP-A / INTP-T','Buyurucu:ENTJ-A / ENTJ-T','Tartışmacı:ENTP-A / ENTP-T',
        'Savunucu:INFJ-A / INFJ-T','Arabulucu:INFP-A / INFP-T','Önder:ENFJ-A / ENFJ-T','Kampanyacı:ENFP-A / ENFP-T',
        'Lojistikçi:ISTJ-A / ISTJ-T','Savunmacı:ISFJ-A / ISFJ-T','Yönetici:ESTJ-A / ESTJ-T','Konsül:ESFJ-A / ESFJ-T',
        'Becerikli:ISTP-A / ISTP-T','Maceracı:ISFP-A / ISFP-T','Girişimci:ESTP-A / ESTP-T','Eğlendirici:ESFP-A / ESFP-T']

#karakter özellikleri
personalities1_mimar=["Eğlenceli", "Cesur", "İletişimde başarılı", "Pratik", "İyi gözlemci", "Orijinal", "Plansız","Kolay sıkılan", "Bencil"]
personalities2_mantikci=["Zeki", "Yaratıcı", "Mantıklı", "Dürüst", "Soğukkanlı", "Açık görüşlü", "Objektif", "Düzensiz", "Dalgın", "Alaycı"]
personalities3_buyurucu=["Özgüvenli", "Karizmatik", "Verimli", "Lider", "Stratejik", "Kararlı", "Enerjik", "İradeli", "Baskın", "Toleranssız", "Kibirli"]
personalities4_tartismaci=["Bilgili", "Enerjik", "Karizmatik", "Hızlı düşünen", "Fikir üreten", "Orijinal", "Entelektüel", "Eleştirel", "Tartışmacı", "Duyarsız"]
personalities5_savunucu=["Nazik", "Sezgisel", "Kararlı", "İdealist", "Mükemmeliyetçi", "Yaratıcı", "Hassas", "Ketum", "İnatçı"]
personalities6_arabulucu=["Açık fikirli", "Yaratıcı", "Anlayışlı", "İçten", "Sıcak", "Uyumlu", "Duygusal", "Romantik", "Hassas", "Ketum"]
personalities7_onder=["Karizmatik", "Hoşgörülü", "Lider", "Güvenilir", "Merhametli", "İkna kabiliyeti yüksek", "Özverili", "Aşırı idealist", "Hassas", "Kararsız"]
personalities8_kampanyaci=["Enerjik", "Hümanist", "Rahatlatıcı", "Anlayışlı", "Coşkulu", "Dost canlısı", "Meraklı", "Duygusal", "Odaklanmakta zorlanan", "Çabuk sinirlenen"]
personalities9_lojistikci=["Dürüst", "Açık sözlü", "Pratik", "Sakin", "İradeli", "Sorumluluk sahibi", "Bilgili", "Kapalı görüşlü", "Kuralcı", "Yargılayıcı"]
personalities10_savunmaci=["Güvenilir", "Sabırlı", "Çalışkan", "Sorumluluk sahibi", "Destekçi", "Pratik"," Aşırı mütevazı", "Alıngan", "Fazla özverili"]
personalities11_yonetici=["Lider", "İradeli", "Açık sözlü", "Dürüst", "Rasyonel", "Sadık", "Başarılı", "Yargılayıcı", "Toleranssız", "Onay arayan"]
personalities12_konsul=["Yardımsever", "Sadık", "Sıcakkanlı", "Sorumluluk sahibi", "Pratik", "İletişimde başarılı", "Fazla özverili", "Yeniliklere kapalı", "Beklentili"]
personalities13_becerikli=["Pratik", "Ssnek", "Rasyonel", "Sakin", "Doğal", "Yaratıcı", "İyimser", "Becerikli", "Çabuk sıkılan", "Ketum", "İnatçı"]
personalities14_maceraci=["Duyarlı", "Sıcakkanlı", "Çekici", "Yaratıcı", "Orijinal", "Hevesli", "Meraklı", "Stresli", "Plansız", "Rekabetçi"]
personalities15_girisimci=["Cesur", "Enerjik", "Pratik", "Dürüst", "Açık sözlü", "Mantıklı", "Becerikli", "İletişimde başarılı", "Sabırsız", "Risk alan", "Düşüncesiz"]
personalities16_eglendirici=["Eğlenceli", "Cesur", "İletişimde başarılı", "Pratik", "İyi gözlemci", "Orijinal", "Plansız", "Kolay sıkılan", "Bencil"]

aylar=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
#meslekler
meslekler=['Acentacı', 'Acil durum yönetmeni', 'Adli tabip', 'Agronomist', 'Ağ yöneticisi', 'Aşçı', 'Aşçıbaşı', 'Ahşap tekne yapımcısı', 'Aile hekimi', 'Aktar', 'Aktör', 'Aktüer', 'Aktris', 'Akustikçi', 'Albay', 'Ambalajcı', 'Ambarcı', 'Ambulans şoförü', 'Amiral', 'Anahtarcı', 'Analist', 'Anestezi uzmanı', 'Anestezi teknikeri', 'Animatör', 'Antika satıcısı', 'Antropolog', 'Araba satıcısı', 'Araba yıkayıcısı', 'Arabulucu', 'Araştırmacı', 'Arıcı', 'Arkeolog', 'Armatör', 'Arpist', 'Arşivci', 'Artist', 'Asistan', 'Asker', 'Astrofizikçi', 'Astrolog', 'Astronom', 'Astronot', 'Astsubay', 'Atlet', 'Avcı', 'Avukat', 'Ayakkabı boyacısı', 'Ayakkabı tamircisi', 'Ayakkabıcı', 'Baharatçı', 'Bahçe bitkileri uzmanı', 'Bahçıvan', 'Bakan', 'Bakıcı', 'Bakkal', 'Bakteriyolog', 'Balıkçı', 'Bankacı', 'Banker', 'Barmen', 'Basketbolcu', 'Başbakan', 'Başçavuş', 'Başhemşire', 'Başkan', 'Başkomiser', 'Başpiskopos', 'Başrahip', 'Belediye başkanı', 'Belediye meclisi üyesi', 'Benzinci', 'Berber', 'Besteci', 'Biletçi', 'Bilgisayar mühendisi', 'Bilgisayar programcısı', 'Bilgisayar tamircisi', 'Bilim insanı', 'Bilirkişi', 'Bisikletçi', 'Biyografi yazarı', 'Biyolog', 'Biyomedikal Mühendisi', 'Bomba imha uzmanı', 'Borsacı', 'Botanikçi', 'Boyacı', 'Bozacı', 'Böcekbilimci', 'Börekçi', 'Bulaşıkçı', 'Buldozer operatörü', 'Bütçe uzmanı', 'Büyükelçi', 'Besicilik', 'Bebek bakıcısı', 'Bilgi İşlemci', 'Camcı', 'Cerrah', 'Cumhurbaşkanı', 'Çamaşırcı', 'Çantacı', 'Çaycı', 'Çevirmen', 'Çevrebilimci', 'Çevre mühendisi', 'Çiçekçi', 'Çiftçi', 'Çilingir', 'Çinici', 'Çoban', 'Çocuk doktoru', 'Çorapçı', 'Çöp işçisi', 'Çöpçü', 'Çırak', 'Çevik Kuvvet', 'Dadı', 'Dalgıç', 'Danışman', 'Dedektif', 'Değirmen işçisi', 'Değirmenci', 'Demirci', 'Demiryolu işçisi', 'Denetçi', 'Denetleyici', 'Denizci', 'Depocu', 'Derici', 'Devlet memuru', 'Ebe(kadın doğum)', 'Eczacı', 'Eczacı kalfası', 'Editör', 'Eğitimci', 'Eğitmen', 'Ekonomist', 'Elektrik mühendisi', 'Elektronik mühendisi', 'Elektrik-Elektronik mühendisi', 'Elektronik ve Haberleşme mühendisi', 'Elektrikçi', 'Eleştirmen', 'Embriyolog', 'Emlakçı', 'Emniyet amiri', 'Emniyet genel müdürü', 'Endüstri mühendisi', 'Endüstri sistemleri mühendisi', 'Enstrüman imalatçısı', 'Ergonomist', 'Eskici', 'Estetisyen', 'Etolojist', 'Etimolog', 'Etnolog', 'Fabrika işçisi', 'Falcı', 'Fermantasyon işçisi', 'Fırıncı', 'Figüran', 'Film yapımcısı', 'Film yönetmeni', 'Filozof', 'Fizikçi', 'Fizyonomist', 'Fizyoterapist', 'Acil tıp teknisyeni', 'Fon yöneticisi', 'Forklift operatörü', 'Fotoğrafçı', 'Futbolcu', 'Gardiyan', 'Galerici', 'Garson', 'Gazete dağıtıcısı', 'Gazete satıcısı', 'Gazeteci', 'Gelir uzmanı', 'Gelir uzman yardımcısı', 'General', 'Genetik mühendisi', 'Gıda mühendisi', 'Gitarist', 'Gökbilimci', 'Göz doktoru', 'Gözetmen', 'Gözlükçü', 'Grafiker', 'Gramer uzmanı', 'Gümrük memuru', 'Gümrük müşaviri', 'Gümrük müşavir yardımcısı', 'Gümrük uzmanı', 'Gündelikçi', 'Güzellik uzmanı', 'Haberci', 'Hakem', 'Halıcı', 'Halkbilimci', 'Hamal', 'Hareket memuru', 'Haritacı', 'Harita mühendisi', 'Hastabakıcı', 'Hava trafikçisi', 'Hayvan bakıcısı', 'Hayvan terbiyecisi', 'Hemşire', 'Hesap uzmanı', 'Heykeltıraş', 'Hırdavatçı', 'Hırsız', 'Hizmetçi', 'Host', 'Hostes', 'Hurdacı', 'İcra memuru', 'İç mimar', 'İktisatçı', 'İlahiyatçı', 'İllüzyonist', 'İmam', 'İnsan kaynakları uzmanı', 'İnşaat mühendisi', 'İşçi', 'İşletmeci', 'İşletme mühendisi', 'İşportacı', 'İtfaiye memuru', 'Jeofizik mühendisi', 'Jeoloji mühendisi', 'Jeolog', 'Jeomorfolog', 'Jinekolog', 'Jokey', 'Kabin görevlisi', 'Kâğıtçı', 'Kahveci', 'Kâhya', 'Kalıpçı', 'Kameraman', 'Kamyoncu', 'Kapıcı', 'Kaplamacı', 'Kaportacı', 'Kaptan', 'Kardinal', 'Kardiyolog', 'Karikatürist', 'Karpuzcu', 'Kasap', 'Kasiyer', 'Kat görevlisi', 'Kâtip', 'Kayıkçı', 'Kaymakam', 'Kaynakçı', 'Kazıcı', 'Kırtasiyeci', 'Kimyager', 'Kimya mühendisi', 'Kitapçı', 'Koleksiyoncu', 'Komedyen', 'Komisyoncu', 'Komiser', 'Konsolos', 'Koreograf', 'Korgeneral', 'Koramiral', 'Koruma görevlisi', 'Komiser', 'Komiser yardımcısı', 'Kozmolog', 'Kömürcü', 'Köpek eğiticisi', 'Köşe yazarı', 'Kuaför', 'Kuru temizlemeci', 'Kuruyemişçi', 'Kurye', 'Kuşbilimci', 'Kuyumcu', 'Kütüphaneci', 'Maden işçisi', 'Makinist', 'Makine mühendisi', 'Mali hizmetler uzmanı', 'Manastır baş rahibesi', 'Manav', 'Manikürcü', 'Manken', 'Marangoz', 'Masör', 'Masöz', 'Matador', 'Matbaacı', 'Matematikçi', 'Memur', 'Menajer', 'Meteoroloji uzmanı', 'Metin yazarı', 'Mevsimlik işçi', 'Mezarcı', 'Mikrobiyolog', 'Milletvekili', 'Mimar', 'Misyoner', 'Model', 'Muhabir', 'Muhafız', 'Muhasebeci', 'Muhtar', 'Müdür', 'Müfettiş', 'Müşavir', 'Mühendis', 'Müteahhit', 'Mütercim', 'Müze müdürü', 'Müzisyen', 'Okçu', 'Oduncu', 'Okul müdürü', 'Opera Sanatçısı', 'Orgeneral', 'Orman mühendisi', 'Ornitolog(kuş bilimci)', 'Oto tamirci', 'Oyun yazarı', 'Öğretmen', 'Öğretim elemanı', 'Öğretim görevlisi', 'Öğretim üyesi', 'Özel şoför', 'Palyaço', 'Papaz', 'Paralı asker', 'Park bekçisi', 'Peyzaj mimarı', 'Peyzaj teknikeri', 'Pilot', 'Piskopos', 'Piyango satıcısı', 'Piyanist', 'Polis memuru', 'Polis şefi', 'Siyasetçi', 'Pompacı', 'Postacı', 'Profesör', 'Psikiyatr', 'Psikolog', 'Psikolojik danışmanlık ve rehberlik', 'Paramedik', 'Radyolog', 'Reklamcı', 'Rektör', 'Rektör yardımcısı', 'Ressam', 'Resepsiyon memuru', 'Radyoloji teknisyeni/teknikeri', 'Saat tamircisi', 'Sağlık teknisyeni', 'Sahil koruma', 'Sanat yönetmeni', 'Sanayici', 'Sarraf', 'Satış elemanı', 'Savcı', 'Sekreter', 'Serbest muhasebeci mali müşavir', 'Ses teknisyeni', 'Seyis', 'Sicil memuru', 'Sigortacı', 'Sihirbaz', 'Silahçı', 'Sistem mühendisi', 'Sistem yöneticisi', 'Sokak çalgıcısı', 'Sokak satıcısı', 'Sorgu hâkimi', 'Sosyal hizmet uzmanı', 'Sosyolog', 'Spiker', 'Striptizci', 'Su tesisatçısı', 'Subay', 'Sulh hâkimi', 'Sunucu', 'Şair', 'Şapel papazı', 'Şarap üreticisi', 'Şarkıcı', 'Şarkı sözü yazarı', 'Şoför', 'Taksici', 'Tarım işçisi', 'Tarihçi', 'Tasarımcı', 'Tefeci', 'Teğmen', 'Temizlikçi', 'Terapist', 'Tercüman', 'Terzi', 'Tesisatçı', 'Tiyatro yönetmeni', 'Tuğgeneral', 'Tümamiral', 'Tümgeneral', 'Uçuş teknisyeni', 'Ulaşım sorumlusu', 'Ustabaşı', 'Uydu antenci', 'Uzay mühendisi', 'Uzay bilimcisi', 'Uzman Jandarma', 'Uzman Çavuş', 'Ürolog', 'Vali', 'Vergi denetmeni', 'Vergi müfettişi', 'Vergi tahakkuk memuru', 'Veritabanı yöneticisi', 'Veri hazırlama ve kontrol işletmeni', 'Veteriner hekim', 'Veteriner sağlık teknikeri', 'Veteriner sağlık teknisyeni', 'Veznedar', 'Video editörü', 'Yarbay', 'Yardımcı hakem', 'Yardımcı hizmetli', 'Yardımcı pilot', 'Yargıç', 'Yatırım uzmanı', 'Yayıncı', 'Yazar', 'Yazı işleri müdürü', 'Yazılım mühendisi', 'Yeminli mali müşavir', 'Yeminli tercüman', 'Yönetici', 'Yönetmen', 'Zabıta', 'Zoolog']
ten_rengi=['Çok açık veya Beyaz cilt','Açık cilt veya Avrupalı','Orta açık/buğday cilt veya Güney Avrupalı','Orta koyu/esmer veya Akdenizli','Koyu cilt rengi veya kahverengi','Çok koyu cilt rengi veya siyahi tipi']
goz_rengi=['Açık kahverengi göz','Kahverengi göz','Koyu kahverengi göz / Siyah göz','Mavi göz','Yeşil göz','Ela göz','Kehribar göz','Gri göz']
burun_sekli=["Kemerli burun","Ucu düşük burun","Ucu geniş burun","Ucu dar burun","Ucu sivri uzun burun","Ucu kalkık kısa burun","Eğri burun","Sivri burun","Burun tabanı geniş","Geniş burun","Dar burun","Semer burun"]
sac_uzunlugu=["Kısa saç","Uzun saç"]
sac_tipi=["İnce telli","Normal","Kalın telli"]
sac_sekli=["Düz","Kıvırcık","Dalgalı"]
sac_rengi=["Siyah","Koyu kahve","Kahverengi","Açık kahve","Koyu sarı","Sarı","Açık sarı","Bakır","Turuncu","Kumral"]
hobiler=['Spor Yapmak', 'Yürüyüş Yapmak / Koşmak', 'Yüzmek', 'Oyun Oynamak', 'Bisiklet Sürmek', 'Kamp Yapmak', 'Balık Tutmak', 'Bahçeyle Uğraşmak', 'Mağaracılık', 'Doğa Yürüyüşü (Treking)', 'Haber, Dergi veya Makale Okumak', 'Forumlarda, Sözlüklerde Takılmak', 'e-Spor Oyunları Oynamak', 'Blog Açmak', 'Web Sitesi Kurmak', 'Kodlama Öğrenmek', 'Dizi – Film İzlemek', 'Satranç Oynamak', 'Arkadaşlarla Buluşmak', 'Tarihi Yerleri Gezmek', 'Müzeleri Gezmek', 'Kitap Okumak', 'Yazmak', 'Resim yapmak', 'Yabancı Dil Öğrenmek', 'Yemek Yapmak', 'El Sanatları', 'Şarkı Söylemek', 'Dans Etmek', 'Marangozluk', 'Fotoğrafçılık', 'Online Kurslar', 'Şarkı Dinlemek', 'Enstrüman Çalmak', 'Ata Binmek', 'Piknik Yapmak', 'Okçuluk', 'Sinemaya Gitmek', 'Yoga', 'Seramik/Ahşap Boyama', 'Teraryum Yapmak', 'Origami', 'Kaligrafi', 'Seyahat etmek', 'Paintball', 'Poker', 'Basketbol', 'Futbol', 'Voleybol']
fobiler=['Ablütofobi: Yıkanmaktan korkma', 'Agirofobi: Caddelerden ya da caddelerde karşıdan karşıya geçmekten korkma', 'Agorafobi: Açık yer ya da kalabalık korkusu', 'Ailurofobi: Kedilerden korkma', 'Akluofobi: Karanlıktan korkma', 'Akrofobi: Yüksek yerlerden korkma', 'Akustikofobi: Belirli seslerden korkma', 'Algofobi: Acı çekmekten korkmak', 'Amaksofobi: Araba (ya da taşıt)korkusu', 'Amatofobi: Toz korkusu', 'Amnezifobi: Hafızasını kaybetmekten korkma', 'Amofobi: Sivri cisim korkusu', 'Anatidaephobia: Ördekler tarafından izleniyor olma hissi / korkusu', 'Androfobi: Adamlardan korkma', 'Anemofobi: Fırtına korkusu', 'Antlofobi: Sel korkusu', 'Antropofobi: İnsanlardan korkma', 'Apifobi: Arılardan korkma', 'Arakibutirofobi: Yerfıstığı ezmesinin, yerken, damağa yapışmasından duyulan korku', 'Araknofobi: Örümceklerden korkma', 'Aritmofobi: Sayılardan korkma', 'Asimetrifobi: Simetrik olmayan şeylerden korkma', 'Astenofobi: Güçsüz olmaktan korkma', 'Astrafobi: Şimşek korkusu', 'Ataksofobi: Düzensizlikten korkma', 'Atelofobi: Mükemmel olamamaktan korkma', 'Aviofobi: uçuş korkusu', 'Ballistofobi: Silahtan ya da mermilerden korkma', 'Batofobi: Derinlik korkusu, yüksek binaların yanından geçmekten korkma', 'Batrakofobi: Kurbağa, semender gibi çiftyaşayışlı (amfibyen) hayvanlardan korkma', 'Belonefobi: İğnelerden korkma', 'Bibliyofobi: Kitaplardan korkma', 'Botanofobi: bitkilerden korkma', 'Bromidrosifobi: vücut kokusundan korkma', 'Brontofobi: gök gürültüsünden korkma', 'Datafobi: veriden korkma', 'Dentofobi: dişçiden korkma', 'Dermatopatofobi: deri hastalıklarından korkma', 'Dekatriaparaskevifobi: ayın 13’ünün cuma gününe gelmesi korkusu', 'Eisoptrofobi: aynalardan korkma', 'Elektrofobi: elektrikten korkma', 'Emetofobi: kusmaktan korkma', 'Entomofobi: böceklerden korkma', 'Endofobi: Giyecek korkusu', 'Epistaksiyofobi: burun kanamasından korkma', 'Eritrofobi: yüz kızarmasından duyulan korku', 'Erotofobi: cinsellik korkusu', 'Farmakofobi: ilaçlardan korkma', 'Fazmofobi: hayaletlerden korkma', 'Febrifobi: yüksek ateşten korkma', 'Filemafobi: öpmekten ya da öpüşmekten korkma', 'Filofobi: sevmekten, aşık olmaktan korkma', 'Fobofobi: korkmaktan korkma', 'Fotofobi: ışıktan korkma', 'Gametofobi: evlenmekten korkma', 'Gefirofobi: köprülerden geçmekten korkma', 'Gerontofobi: yaşlı insanlardan ya da yaşlanmaktan korkma', 'Glossofobi: topluluk önünde konuşmaktan korkma', 'Haptofobi: dokunulmaktan korkma', 'Harpaksofobi: hırsızlardan ya da bir suçun kurbanı olmaktan korkma', 'Helyofobi: güneş’ten korkma', 'Helshoesafobi: topuklu ayakkabılardan korkma', 'Hematofobi: kan korkusu', 'Herpetofobi: sürüngenlerden korkma', 'Heterofobi: heteroseksüellerden korkma, tiksinme', 'Hidrofobi: sudan, yüzmekten ya da boğulmaktan korkma', 'Higrofobi: nemden ya da yağmurdan korkma', 'Hipegiyafobi: sorumluluktan korkma', 'Hipnofobi: uyumaktan korkma', 'Hipofobi: atlardan korkma', 'Homiklofobi: sisten korkma', 'Homofobi: eşcinsellerden korkma', 'Hristiyanofobi: hristiyanlıktan ve hristiyanlardan korkma', 'İhtiyofobi: balıklardan korkma', 'İslamofobi: İslamdan ve müslümandan korkma', 'Jinefobi: kadınlardan korkma', 'Japonofobi: Japonlardan korkma', 'Kainatetofobi: yenilik korkusu', 'Kakofobi: çirkinlikten, çirkin seylerden korkma', 'Kakorafiyafobi: başarısız olma korkusu', 'Kanserofobi: kanser olmaktan korkma', 'Kardiyofobi: kalp hastalığından korkma', 'Karnofobi: etten korkma', 'Katagelofobi: dalga geçilmekten korkma', 'Kemofobi: kimyasal maddelerden korkma', 'Kenofobi: karanlık korkusu', 'Keymafobi: kıştan ve soğuktan korkma', 'Kimofobi: dalgalardan korkma', 'Kinofobi: köpeklerden korkma', 'Kitinofobi:böcekten korkma', 'Klimakofobi: merdivenden düşmekten ya da merdivenlerden korkma', 'Klostrofobi: kapalı yer korkusu Kapalı ve basık yerlerde duyulan korkudur. Asansör, basık tavanlı odalar, koridorlar, kapıları kapalı ve kalabalık otobüs, yeraltı çarşıları, metro, alt geçitler ve kilitli odalar onlar için korku verici yerlerdir. Hastanın temel korkusu bu sayılan yerlerde sıkışıp kalmak, nefes alamamak ve boğulmaktır.', 'Koprofobi: dışkı korkusu', 'Koulrofobi: palyaçolardan korkma', 'Koumpounophobia: düğmelerden korkma', 'Kremnofobi: yüksek yamaçlardan ya da uçurumlardan korkma', 'Kriyofobi:buzdan ya da donmaktan korkma', 'Kronomentrofobi: saatlerden korkma', 'Ksantofobi: sarı renkten korkma', 'Ksenofobi: yabancılardan korkma', 'Ksilofobi: tahta şeylerden ya da ormanlardan korkma', 'Fobi türleri nelerdir?', 'Fobiler nelerdir? İşte alfabetik olarak tüm fobi türleri ve açıklamaları.', 'Limnofobi: göllerden korkma', 'Litikafobi: davalardan ve mahkemelerden korkma', 'Logofobi: belirli kelimelerden korkma', 'Lökofobi: beyaz renkten korkma', 'Manyofobi: delirmekten korkma', 'Mastigofobi: cezalandırılmaktan korkma', 'Mekanofobi: makinelerden korkma', 'Melanofobi: siyah tonundan korkma', 'Mikrobiyofobi: mikroplardan korkma', 'Mizofobi: kirlilikten korkma', 'Monofobi: yalnızlıktan korkma', 'Musofobi: farelerden korkma', 'Nekrofobi: cesetten korkma', 'Nelofobi: camdan korkma', 'Niktofobi: geceden korkma', 'Nozokomefobi: hastanelerden korkma', 'Nüdofobi: çıplaklıktan korkma', 'Negrofobi: Siyahilerden korkma', 'Obesofobi: şişmanlamaktan korkma', 'Ofidiyofobi: yılanlardan korkma', 'Okofobi: taşıt araçlarından korkma', 'Ornitofobi: kuşlardan korkma', 'Orofobi:Yamaçtan iniş korkusu', 'Osmofobi: belirli kokulardan korkma', 'Otofobi:ıssız bir yerde kişinin tek başına olmaktan duyduğu korku', 'Panfobi: her şeyden korkma', 'Papirofobi: kâğıttan korkma', 'Paraskavedekatriafobi: ayın on üçü ve cuma olan günden korkma', 'Patofobi: hasta olmaktan korkma', 'Pedofobi: çocuklardan korkma', 'Peladofobi: kel insanlardan ya da kelleşmekten korkma', 'Penyafobi: fakirlikten korkma', 'Pirofobi: ateşten korkma', 'Plakofobi: mezar taşlarından korkma', 'Pogonofobi: sakaldan ya da sakallı kişilerden korkma', 'Politikofobi: politikacılardan korkma', 'Porfirofobi: mor renkten korkma', 'Potamofobi: ırmaklardan ya da su akıntılarından korkma', 'Potofobi: alkollü içeceklerden korkma', 'Pteronofobi: kuş tüyünden korkma', 'Pupafobi: kuklalardan korkma', 'Radyofobi: radyasyondan, x ışınlarından korkma.', 'Ranidafobi: kurbağalardan korkma', 'Selenofobi: ay’dan korkma', 'Siderofobi: yıldızlardan korkma', 'Simetrofobi: simetriden korkma', 'Skiofobi: gölgelerden korkma', 'Sosyofobi: toplumdan, genel olarak insanlardan korkma', 'Soteriofobi: başkalarına muhtaç olmaktan korkma', 'Tafefobi: diri diri gömülmekten korkma', 'Takofobi: yüksek hızdan korkma', 'Talassofobi: deniz ya da okyanus korkusu', 'Tanatofobi: ölümden korkma', 'Teknofobi: teknolojiden korkma', 'Teratofobi: gebe kadının, şekilsiz, çirkin bir çocuk doğurmaktan korkması', 'Termofobi: ısıdan korkma', 'Testofobi: testlerden ya da sınavlardan korkma', 'Tokofobi: gebe kalmaktan ya da çocuk doğurmaktan korkma', 'Tomofobi: ameliyat olmaktan korkma', 'Toksifobi: zehir korkusu', 'Topofobi: belirli yerlerden korkma', 'Transfobi: transgender ve transseksüel kimselerden korkma', 'Travmatofobi: yaralanmaktan korkma', 'Trikinofobi: gıda zehirlenmesinden korkma', 'Triskaidekafobi: 13 sayısından korkma', 'Tripanofobi: aşı ya da iğne olmaktan korkma', 'Trikopatofobi: saç hastalıklarından korkma', 'Tripofobi: deliklerden korkma', 'Ürofobi: idrardan korkma', 'Venereofobi: zührevî hastalıklardan korkma', 'Venüstrafobi: güzel kadınlardan korkma', 'Vermifobi: solucanlardan korkma', 'Xenofobi: yabancılardan korkma', 'Zelofobi: kıskançlıktan korkma', 'Zoofobi: hayvanlardan korkma', 'Zenofobi: yabancı korkusu']
hastaliklar=['Abse', 'Adale romatizması', 'Adenit', 'Ağız yaraları', 'Akciğer kanseri', 'Akdeniz Ateşi', 'Akut Böbrek İltihabı', 'Akut Bronşit', 'Albüminüri', 'Alerji', 'Altını ıslatmak', 'Amipli Dizanteri', 'Anne sütünün azlığı', 'Anus kaşıntısı', 'Apandisit', 'Arpacık', 'Astım', 'Astigmatlık', 'Ateş', 'Ayak ağrıları', 'Ayak burkulması', 'Ayak çıbanı', 'Ayak şişmesi', 'Bademcik iltihabı', 'Bağırsak iltihabı', 'Bağırsak kanaması', 'Bağırsak solucanları', 'Balgam', 'Basilli Dizanteri', 'Basur', 'Baş ağrıları', 'Baş dönmeleri', 'Bayılmalar', 'Bel ağrısı', 'Bel gevşekliği', 'Belsoğukluğu', 'Beyzbol Parmağı', 'Boğaz ağrısı', 'Boğaz iltihabı', 'Boğmaca', 'Boyun tutulması', 'Botulizm', 'Böbrek ağrısı', 'Böbrek iltihabı', 'Böbrek kumu', 'Böbrek taşı', 'Bronşit', 'Burkulmalar', 'Burun ahtapotu', 'Burun akıntısı', 'Burun kanaması', 'Burun tıkanıklığı', 'Cinsel soğukluk', 'Çıbanlar', 'Çıkıklar', 'Çiçek', 'Çift cinsiyetlilik', 'Çiller', 'Çok uyumak', 'Çürükler', 'Dalak hastalıkları', 'Damar sertliği', 'Deri iltihabı', 'Deri kanseri', 'Deri kuruluğu', 'Deri lekeleri', 'Dil büyümesi', 'Dil felci', 'Dil iltihabı', 'Dil ülseri', 'Diş ağrısı', 'Diyabet', 'Dizanteri', 'Egzama', 'Ekstrasistol', 'Enfarktüs', 'Ensefalopati', 'Epistaksis', 'Fabry', 'Fazla terlemek', 'Felç', 'Ferç kaşıntısı', 'Fıtık', 'Fil hastalığı', 'Fistül', 'Frengi', 'Gastrit', 'Gece körlüğü', 'Gıda zehirlenmeleri', 'Göğüste su toplaması', 'Göz ağrısı', 'Göz iltihabı', 'Göz kanlanması', 'Göz kaşıntısı', 'Göz sulanması', 'Gözbebekleri iltihabı', 'Gözkapağı iltihabı', 'Gözkapağı şişliği', 'Guatr', 'Guatr (Yumrulu)', 'Güneş çarpması', 'Güneş yanığı', 'Halsizlik', 'Hararet', 'Havale', 'Hazımsızlık', 'Hemofili', 'Hipokrat yüzü', 'Hipotiroidi', 'Husye torbası şişliği', 'İdrar torbası iltihabı', 'İdrar tutamamak', 'İdrar tutukluğu', 'İdrar yollarında yanma', 'İdrar zorluğu', 'İdrarda kan görülmesi', 'İdraryolları iltihabı', 'İktidarsızlık', 'İncinmek', 'İshal', 'İsilik', 'İsteri', 'İştahsızlık', 'Kabakulak', 'Kabızlık', 'Kalbin hızlı atması', 'Kalınbağırsak iltihabı', 'Kalp ağrısı', 'Kalp hastalıkları', 'Kalp romatizması', 'Kalp yetmezliği', 'Kan çıbanı', 'Kan işemek', 'Kan tükürmek', 'Kanda kolestrol yüksekliği', 'Kanser', 'Kansızlık', 'Kaonjestij Kalp Hastalığı', 'Karaciğer hastalıkları', 'Karaciğer Büyümesi', 'Karaciğer şişmesi', 'Karaciğer Yağlanması', 'Karaciğer yetersizliği', 'Katarakt', 'Kekemelik', 'Kellik', 'Kemik erimesi(Osteoproz)', 'Kemik iltihabı', 'Kemik veremi', 'Kemik yumuşaması', 'Kırıklar', 'Kısırlık', 'Kızamık', 'Kızamıkçık', 'Kızıl', 'Kloroz', 'Kolera', 'Kolesterol', 'Korona Virüs', 'Kör çıban', 'Kronik Böbrek İltihabı', 'Kronik Bronşit', 'Kuduz', 'Kulak ağrısı', 'Kulak akıntısı', 'Kulak iltihabı', 'Kulunç ağrısı', 'Kum sancıları', 'Kurdeşen', 'Kuşpalazı', 'Kuş Gribi', 'Loğusa humması', 'Lösemi', 'Lumbago', 'Lipom', 'Lyme', 'Mastitis', 'Mastositoz', 'Morfinizm', 'Morfinomani', 'Mide tembelliği', 'Mide ülseri', 'Mide yanması', 'Migren', 'Miyopluk', 'Nasır', 'Narkolepsi', 'Nefes darlığı', 'Nefrit', 'Nevralji', 'Nevrasteni', 'Nezle', 'Nikris hastalığı', 'Nörofibromatoz', 'Nöropatik osteoartropati', 'Onikiparmak bağırsağı ülseri', 'Ödem', 'Pamukçuk', 'Paratifo', 'Paslı dil', 'Panik atak', 'Parkinasan', 'Raşitizm', 'Romatizma', 'Saç ve sakal ağarması', 'Saçkıran', 'Saçların kepeklenmesi', 'Safra kesesi iltihabı', 'Safra taşları', 'Sağ Kalp Yetmezliği', 'Sağırlık', 'Sakal iltihabı', 'Salgın menenjit', 'Saman nezlesi', 'Sara', 'Sarılık', 'Sedef hastalığı', 'Ses kaybı', 'Ses kısıklığı', 'Sık sık idrara gitme', 'Sıraca', 'Sıtma', 'Siğiller', 'Sinirsel ağrılar', 'Sinirsel hazımsızlık', 'Sinirsel kusma', 'Sinüzit', 'Siroz', 'Siyatik', 'Skorbüt', 'Şarbon', 'Şeker hastalığı', 'Şirpençe', 'Tansiyon düşüklüğü', 'Tansiyon yüksekliği', 'Tavukkarası', 'Taşikardi', 'Temriye', 'Tetanoz', 'Tırnak batması', 'Tırnak iltihabı', 'Tifo', 'Tifüs', 'Titremek', 'Uçuk', 'Ur', 'Uykusuzluk', 'Uyurgezerlik', 'Uyuz', 'Üremi', 'ülser', 'Varis', 'Varis ülseri', 'Veba', 'Verem', 'Yılancık', 'Zatülcenp', 'Zatürree', 'Zollinger Ellison Sendromu', 'Zona']
zenginlik=["Fakir","Çok fakir","Açlık sınırında","Orta halli","Zengin","Çok zengin"]
en_sevilen_kitaplar=['Veba - Albert Camus', 'Yabancı - Albert Camus', 'Cesur Yeni Dünya - Aldous Huxley', 'Yüzbaşının Kızı - Aleksandr Puşkin', 'Monte Kristo Kontu - Alexandre Dumas', 'Üç Silahşörler - Alexandre Dumas', 'Kamelyalı Kadın - Alexandre Dumas', 'Küçük Prens - Antoine de Saint-Eupery', 'Vişne Bahçesi - Anton Çehov', "Sherlock Holmes'un Maceraları - Arthur Conan Doyle", 'Drakula - Bram Stoker', 'Gün Olur Asra Bedel - Cengiz Aytmatov', 'David Copperfield - Charles Dickens', 'Büyük Umutlar - Charles Dickens', 'İki Şehrin Hikayesi - Charles Dickens', 'Oliver Twist - Charles Dickens', 'Jane Eyre - Charlotte Bronte', 'Robinson Crusoe - Daniel Defoe', 'İlahi Komedya - Dante Alighieri', 'Rebecca - Daphne du Meurier', 'Otostopçunun Galaksi Rehberi - Douglas Adams', 'Uğursuz Miras - E.T.A Hoffman', 'Bütün Hikayeleri Toplu Cilt - Edgar Allan Poe', 'Cyrano de Bergerac - Edmond Rostand', 'Germinal - Emile Zola', 'Uğultulu Tepeler - Emily Bronte', 'Silahlara Veda - Ernest Hemingway', "Klimanjaro'nun Karları - Ernest Hemingway", 'İhtiyar Adam ve Deniz - Ernest Hemingway', 'Çanlar Kimin İçin Çalıyor - Ernest Hemingway', 'Dönüşüm - Franz Kafka', 'Dava - Franz Kafka', 'Böyle Buyurdu Zerdüşt - Friedrich Nietzsche', 'Budala - Fyodor Dostoyevski', 'Karamazov Kardeşler - Fyodor Dostoyevski', 'Suç ve Ceza - Fyodor Dostoyevski', 'Beyaz Geceler - Fyodor Dostoyevski', 'Cinler - Fyodor Dostoyevski', 'Delikanlı - Fyodor Dostoyevski', 'Ezilenler - Fyodor Dostoyevski', 'İnsancıklar - Fyodor Dostoyevski', 'Kumarbaz - Fyodor Dostoyevski', 'Netoçka Nezvanova - Fyodor Dostoyevski', 'Yeraltından Notlar - Fyodor Dostoyevski', 'Yüzyıllık Yalnızlık - Gabriel Garcia Marquez', 'Kolera Günlerinde Aşk - Gabriel Garcia Marquez', 'Bin dokuz yüz seksen dört - George Orwell', 'Hayvan Çiftliği - George Orwell', 'Beyaz Zambaklar Ülkesinde - Grigoriy Petrov', 'Madam Bovary - Gustave Flaubert', 'Zaman Makinesi - H.G. Wells', 'Bülbülü Öldürmek - Harper Lee', 'Kızıl ile Kara - Henri Stendhal', 'Parma Manastırı - Henri Stendhal', 'Bir Kadının Portresi - Henry James', 'Moby Dick - Herman Melville', 'Bozkırkurdu - Hermann Hesse', 'Siddartha - Hermann Hesse', 'İlyada - Homeros', 'Odysseia - Homeros', 'Vadideki Zambak - Honore de Balzac', 'Goriot Baba - Honore de Balzac', 'Eugenie Grandet - Honore de Balzac', 'Oblomov - İvan A. Gonçarov', 'Babalar ve Oğullar - İvan S. Turgenyev', 'Çavdar Tarlasında Çocuklar - J.D. Salinger', 'Vahşetin Çağrısı - Jack London', 'Beyaz Diş - Jack London', 'Ulysses - James Joyce', 'Gurur ve Önyargı - Jane Austen', 'Emma - Jane Austen', 'Akıl ve Tutku - Jane Austen', 'İkna - Jane Austen', 'Faust - Johann W. Von Goethe', "Genç Werther'in Acıları - Johann W. Von Goethe", 'Gazap Üzümleri - John Steinbeck', 'Cennetin Doğusu - John Steinbeck', 'İnci - John Steinbeck', 'Fareler ve İnsanlar - John Steinbeck', "Güliver'in Gezileri - Jonathan Swift", 'Körlük - José Saramago', '80 Günde Devr-i alem - Jules Verne', 'Denizler Altında 20.000 Fersah - Jules Verne', 'Açlık - Knut Hamsun', 'Diriliş - Lev Tolstoy', 'Savaş ve Barış - Lev Tolstoy', 'Anna Karenina - Lev Tolstoy', 'Çocukluğum - Lev Tolstoy', 'Korkunç İvan - Lev Tolstoy', 'Hacı Murat - Lev Tolstoy', "İvan İlyiç'in Ölümü - Lev Tolstoy", 'İnsan Ne İle Yaşar - Lev Tolstoy', 'Kazaklar - Lev Tolstoy', 'Alice Harikalar Diyarında - Lewis Carroll', 'Küçük Kadınlar - Louisa May Alcott', 'Ana - Maksim Gorki', 'Kıvılcım Anı - Malcolm Gladwell', 'Tom Sawyer - Mark Twain', "Huckleberry Finn'in Serüvenleri - Mark Twain", 'Frankenstein - Mary Shelley', 'Don Kişot - Miguel de Cervantes', 'Çağımızın Bir Kahramanı - Mihail Lermontov', 'Master ve Margarita - Mikhail Bulgakov', 'Varolmanın Dayanılmaz Hafifliği - Milan Kundera', 'Ölü Canlar - Nikolay V. Gogol', "Dorian Gray'in Portresi - Oscar Wilde", 'Ciddi Olmanın Önemi - Oscar Wilde', 'Devlet - Platon', 'Martı Jonathan Livingston - Richard Bach', 'Hazine Adası - Robert Louis Stevenson', 'Amerigo - Stefan Zweig', 'Amok Koşucusu - Stefan Zweig', 'Çılgın Kalabalıktan Uzak - Thomas Hardy', 'Büyülü Dağ - Thomas Mann', 'Buddenbrook Ailesi - Thomas Mann', "Venedik'te Ölüm - Thomas Mann", 'Ütopya - Thomas More', "Notre Dame'ın Kamburu - Victor Hugo", 'Sefiller - Victor Hugo', 'Lolita - Vladimir Nabokov', 'Sineklerin Tanrısı - William Golding', 'Antonius ve Kleopatra - William Shakespeare', 'Kral Lear - William Shakespeare', 'Macbeth - William Shakespeare', 'Bir Yaz Gecesi Rüyası - William Shakespeare', 'Romeo ve Jülyet - William Shakespeare', 'III. Richard  - William Shakespeare', 'Atinalı Timon - William Shakespeare', 'Othello - William Shakespeare', 'Kuru Gürültü - William Shakespeare', 'Julius Caesar - William Shakespeare', 'V. Henry  - William Shakespeare', 'Hamlet - William Shakespeare', 'Size Nasıl Geliyorsa - William Shakespeare', 'Aşkın Çabası Boşuna - William Shakespeare', "Windsor'un Şen Kadınları - William Shakespeare", 'Venedik Tüccarı - William Shakespeare', 'Yanlışlıklar Komedisi - William Shakespeare', 'Fırtına - William Shakespeare', 'Onikinci Gece - William Shakespeare', 'Kış Masalı - William Shakespeare', 'Yeter ki Sonu İyi Bitsin - William Shakespeare', '1984 - George Orwell']
en_sevilen_filmler=['1.      The Shawshank Redemption(1994)', '2.      The Godfather(1972)', '3.      The Godfather: Part II(1974)', '4.      The Dark Knight(2008)', '5.      12 Angry Men(1957)', "6.      Schindler's List(1993)", '7.      The Lord of the Rings: The Return of the King(2003)', '8.      Pulp Fiction(1994)', '9.      Il buono, il brutto, il cattivo(1966)', '10.      The Lord of the Rings: The Fellowship of the Ring(2001)', '11.      Fight Club(1999)', '12.      Forrest Gump(1994)', '13.      Inception(2010)', '14.      Star Wars: Episode V - The Empire Strikes Back(1980)', '15.      The Lord of the Rings: The Two Towers(2002)', '16.      The Matrix(1999)', '17.      Goodfellas(1990)', "18.      One Flew Over the Cuckoo's Nest(1975)", '19.      Shichinin no samurai(1954)', '20.      Se7en(1995)', '21.      Cidade de Deus(2002)', '22.      La vita è bella(1997)', '23.      Gisaengchung(2019)', '24.      The Silence of the Lambs(1991)', "25.      It's a Wonderful Life(1946)", '26.      Star Wars(1977)', '27.      Saving Private Ryan(1998)', '28.      Sen to Chihiro no kamikakushi(2001)', '29.      The Green Mile(1999)', '30.      Interstellar(2014)', '31.      Léon(1994)', '32.      The Usual Suspects(1995)', '33.      Seppuku(1962)', '34.      The Lion King(1994)', '35.      American History X(1998)', '36.      Terminator 2: Judgment Day(1991)', '37.      Back to the Future(1985)', '38.      The Pianist(2002)', '39.      Modern Times(1936)', '40.      Psycho(1960)', '41.      Gladiator(2000)', '42.      City Lights(1931)', '43.      The Intouchables(2011)', '44.      The Departed(2006)', '45.      Whiplash(2014)', '46.      Joker(2019)', '47.      The Prestige(2006)', '48.      Once Upon a Time in the West(1968)', '49.      Hotaru no haka(1988)', '50.      Casablanca(1942)', '51.      Rear Window(1954)', '52.      Nuovo Cinema Paradiso(1988)', '53.      Alien(1979)', '54.      Apocalypse Now(1979)', '55.      Raiders of the Lost Ark(1981)', '56.      Memento(2000)', '57.      The Great Dictator(1940)', '58.      The Lives of Others(2006)', '59.      1917(2019)', '60.      Django Unchained(2012)', '61.      Avengers: Infinity War(2018)', '62.      Paths of Glory(1957)', '63.      The Shining(1980)', '64.      WALL·E(2008)', '65.      Spider-Man: Into the Spider-Verse(2018)', '66.      Mononoke-hime(1997)', '67.      Sunset Blvd.(1950)', '68.      Avengers: Endgame(2019)', '69.      Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb(1964)', '70.      Oldeuboi(2003)', '71.      Witness for the Prosecution(1957)', '72.      The Dark Knight Rises(2012)', '73.      Once Upon a Time in America(1984)', '74.      Aliens(1986)', '75.      Kimi no na wa.(2016)', '76.      American Beauty(1999)', '77.      Coco(2017)', '78.      Braveheart(1995)', '79.      Das Boot(1981)', '80.      3 Idiots(2009)', '81.      Toy Story(1995)', '82.      Tengoku to jigoku(1963)', '83.      Star Wars: Episode VI - Return of the Jedi(1983)', '84.      Taare Zameen Par(2007)', '85.      Amadeus(1984)', '86.      Reservoir Dogs(1992)', '87.      Inglourious Basterds(2009)', '88.      Good Will Hunting(1997)', '89.      2001: A Space Odyssey(1968)', '90.      Requiem for a Dream(2000)', '91.      M - Eine Stadt sucht einen Mörder(1931)', '92.      Vertigo(1958)', '93.      Dangal(2016)', '94.      Eternal Sunshine of the Spotless Mind(2004)', '95.      Citizen Kane(1941)', '96.      Jagten(2012)', '97.      Full Metal Jacket(1987)', '98.      North by Northwest(1959)', '99.      A Clockwork Orange(1971)', '100.      Snatch(2000)', '101.      The Kid(1921)', '102.      Ladri di biciclette(1948)', "103.      Singin' in the Rain(1952)", '104.      Scarface(1983)', '105.      Taxi Driver(1976)', '106.      Amélie(2001)', '107.      Lawrence of Arabia(1962)', '108.      Toy Story 3(2010)', '109.      The Sting(1973)', '110.      Capharnaüm(2018)', '111.      Metropolis(1927)', '112.      Per qualche dollaro in più(1965)', '113.      Ikiru(1952)', '114.      Jodaeiye Nader az Simin(2011)', '115.      Double Indemnity(1944)', '116.      To Kill a Mockingbird(1962)', '117.      The Apartment(1960)', '118.      Indiana Jones and the Last Crusade(1989)', '119.      Incendies(2010)', '120.      Up(2009)', '121.      L.A. Confidential(1997)', '122.      Monty Python and the Holy Grail(1975)', '123.      Heat(1995)', '124.      Die Hard(1988)', '125.      Rashômon(1950)', '126.      Yôjinbô(1961)', '127.      Batman Begins(2005)', '128.      Unforgiven(1992)', '129.      Der Untergang(2004)', '130.      Green Book(2018)', '131.      Bacheha-Ye aseman(1997)', '132.      Some Like It Hot(1959)', '133.      Hauru no ugoku shiro(2004)', '134.      Idi i smotri(1985)', '135.      Ran(1985)', '136.      The Great Escape(1963)', '137.      All About Eve(1950)', '138.      A Beautiful Mind(2001)', '139.      Casino(1995)', '140.      Tonari no Totoro(1988)', "141.      Pan's Labyrinth(2006)", '142.      Raging Bull(1980)', '143.      El secreto de sus ojos(2009)', '144.      Lock, Stock and Two Smoking Barrels(1998)', '145.      The Wolf of Wall Street(2013)', '146.      The Treasure of the Sierra Madre(1948)', '147.      Judgment at Nuremberg(1961)', '148.      Three Billboards Outside Ebbing, Missouri(2017)', '149.      There Will Be Blood(2007)', '150.      Chinatown(1974)', '151.      The Gold Rush(1925)', '152.      Babam ve Oglum(2005)', '153.      Dial M for Murder(1954)', '154.      V for Vendetta(2005)', '155.      Inside Out(2015)', '156.      Det sjunde inseglet(1957)', '157.      No Country for Old Men(2007)', '158.      Warrior(2011)', '159.      Trainspotting(1996)', '160.      The Elephant Man(1980)', '161.      Shutter Island(2010)', '162.      The Sixth Sense(1999)', '163.      Room(2015)', '164.      The Thing(1982)', '165.      Gone with the Wind(1939)', '166.      Blade Runner(1982)', '167.      Jurassic Park(1993)', '168.      The Bridge on the River Kwai(1957)', '169.      The Third Man(1949)', '170.      Finding Nemo(2003)', '171.      On the Waterfront(1954)', '172.      Smultronstället(1957)', '173.      Fargo(1996)', '174.      Kill Bill: Vol. 1(2003)', '175.      Gran Torino(2008)', '176.      The Deer Hunter(1978)', '177.      The Truman Show(1998)', '178.      Tôkyô monogatari(1953)', '179.      Stalker(1979)', '180.      Eskiya(1996)', '181.      Relatos salvajes(2014)', '182.      Salinui chueok(2003)', '183.      Andhadhun(2018)', '184.      The Big Lebowski(1998)', '185.      Ford v Ferrari(2019)', '186.      Mary and Max(2009)', '187.      In the Name of the Father(1993)', '188.      Klaus(2019)', '189.      Gone Girl(2014)', '190.      Hacksaw Ridge(2016)', '191.      The Grand Budapest Hotel(2014)', '192.      Mr. Smith Goes to Washington(1939)', '193.      How to Train Your Dragon(2010)', '194.      The General(1926)', '195.      Sherlock Jr.(1924)', '196.      Before Sunrise(1995)', '197.      Persona(1966)', '198.      Catch Me If You Can(2002)', '199.      Prisoners(2013)', '200.      12 Years a Slave(2013)', '201.      Cool Hand Luke(1967)', '202.      Le salaire de la peur(1953)', '203.      Into the Wild(2007)', '204.      Network(1976)', '205.      Stand by Me(1986)', '206.      Mad Max: Fury Road(2015)', '207.      Life of Brian(1979)', '208.      Barry Lyndon(1975)', '209.      Platoon(1986)', '210.      Million Dollar Baby(2004)', "211.      Hachi: A Dog's Tale(2009)", "212.      La passion de Jeanne d'Arc(1928)", '213.      Rush(2013)', '214.      Logan(2017)', '215.      Ben-Hur(1959)', '216.      Kaze no tani no Naushika(1984)', '217.      Andrei Rublev(1966)', '218.      Rang De Basanti(2006)', '219.      Harry Potter and the Deathly Hallows: Part 2(2011)', '220.      Dead Poets Society(1989)', '221.      Les quatre cents coups(1959)', '222.      Amores perros(2000)', '223.      Hotel Rwanda(2004)', '224.      Spotlight(2015)', '225.      Rebecca(1940)', '226.      Ah-ga-ssi(2016)', '227.      Rocky(1976)', '228.      Monsters, Inc.(2001)', '229.      La haine(1995)', '230.      It Happened One Night(1934)', '231.      Ace in the Hole(1951)', '232.      The Red Shoes(1948)', '233.      The Princess Bride(1987)', '234.      Before Sunset(2004)', '235.      White Heat(1949)', '236.      Faa yeung nin wa(2000)', '237.      Lagaan: Once Upon a Time in India(2001)', '238.      The Help(2011)', '239.      Gangs of Wasseypur(2012)', '240.      The Terminator(1984)', '241.      Butch Cassidy and the Sundance Kid(1969)', '242.      Paris, Texas(1984)', '243.      Akira(1988)', '244.      PK(2014)', '245.      Contratiempo(2016)', '246.      Aladdin(1992)', '247.      Guardians of the Galaxy(2014)', '248.      Groundhog Day(1993)', '249.      Underground(1995)', '250.      Song of the Sea(2014)']
inanclar=["Ortodoks Hristiyanlık","Katolik Hristiyanlık","İslamiyet","Hinduizm","Musevilik","Budizm","Şintoizm","Ateizm","Ateizm","Deizm","Agnostisizm","Panteizm","Materyalizm","Politeizm","Disteizm"]
cinselyonelim=["Heteroseksüel","Homoseksüel","Lezbiyen","Gey","Biseksüel","Aseksüel","Transgender","Transseksüel","Travesti","Cross Dresser","Drag Queen","İnterseksüel","Diğer"]
karakteryonelimi=["Kuralcı iyi","Kuralcı tarafsız","Kuralcı kötü","Dengesel iyi","Dengeci nötr","Dengesel kötü","Kaotik iyi","Kaotik tarafsız","Kaotik kötü"]
karakteryonelimi_aciklama="""
Kuralcı iyi: Bu yönelimdeki kimseler, iyi organize olmuş bir sistemin, devletin ve kanun' un insanların çoğunun yaşamını olumlu yönde etkileyeceğini savunur. Onlara göre insanlar kanunlara saygı gösterip, onlara uydukça, hayat daha kolay ve daha güzel olacaktır. Kuralcı iyi karakterlere adil ve iyi bir kralı, düzgün bir hakimi örnek olarak verebiliriz.

Kuralcı tarafsız: Kanunlar ve organizelik bu yönelimin en ayırt edici özelliğidir. Kuralcı tarafsızlar sadece hayatın bir düzen içinde akmasını savunur. Zalim bir dikdatörlük ya da adil bir demokrasi onlar için aynıdır. Çünkü kuralcı tarafsızlar sadece kanun ve düzeni önemser. Kanun ve düzenin ne yolla sağlanığı onları ilgilendirmez. Emirleri sorgusuz sualsiz yerine getiren bir asker veya cellat kuralcı tarafsıza iyi birer örnektir.

Kuralcı kötü: Bu tür insanlar organizasyonların ve kanunların kendilerine çıkar sağlayacağını düşünür. Kuralcı kötü karakterler kanunlara uyarlar. Kuralcı kötüler yemin ederken ve söz verirken çok dikkatli olurlar. Ve eğer verdikleri sözü bozmaları gerekirse, bunu legal yollar ve sebeplerden yaparlar. Aç gözlü gaddar bir tüccarı bu yönelime örnek olarak verebiliriz. Bu kimse hem düzen tarafından malı ve canı korunduğu için, kanunları ve düzeni savunur, hem de borçlusundan parasını almak için gerekirse düzenin, kendisine haklı olduğunda yardımcı olacağını bildiğinden kanunları ve yasaları savunur.

Dengesel iyi: Bu kimseler için düzen ya da kaos' un bir anlamı yoktur. Onlar sadece iyiliğe inanır. Eğer insanların iyiliği kanunlar tarafından sağlanıyorsa, dengesel iyi yönelimdeki karakter kanunları destekler. Eğer insanların iyiliği için sisteme isyan gerekiyorsa veya sistem ve kanunlar insanların zararınaysa, dengesel iyiler tüm düzenin al aşağı edilmesini savunur. Bu yönelime örnek olarak, kralı tarafından emir aldığı halde, savaş sırasında yakaladığı silahsız masum kimseleri öldürmeyen bir general verilebilir.

Dengeci nötr: Bu yönelimdekiler güçşer arasındaki dengeye inanırlar ve eylemleri iyi ya da kötü olarak görmezler. Dengeci nötr karakterler çok nadir görülür. Bu yönelimdeki kimseler, düzen , kaos, iyilik ve kötülük tarafları arasındaki dengeyi koruma adına sürekli taraf değiştirir.

Dengesel kötü: Bu tip karakterler için sadece kendileri ve çıkarları önemlidir. Eğer bir olay kendilerine çıkar sağlayacaksa, legal ya da legal olmayan her yol onlara uygundur. Çünkü dengesel kötü karakterlerin önemsedikleri tek şey çıkarlarıdır. Bu yönelimdekiler dostluklarını çıkar ve güç üzerine kurarlar. Kendi çıkarları için otoriteye ve topluma ihanet eden bir çifte ajan, tipik bir hırsız, veya kendi çıkarları için gerekirse kanunlara uyan gerekirse illegal işler yapan ahlakız bir tüccar, dengesel kötü yönelime iyi birer örnektir.

Kaotik iyi: Bu karakterlerin davranışlarında güçlü bir fevrilik görürlür. İyilik ve doğruluğa inanmalarının yanı sıra kanunlarla veya kısıtlamalarla araları pek yoktur. Bu yönelimdeki karakterler kendilerine, neyin nasıl yapılması gerektiğinin söylenmesinden hoşnut olmazlar. Yaptıkları şeyler iyi olsa da bazen toplum tarafından hoş karşılanmayabilir. Kaotik iyiler genellikleö özgür bir ruha sahip, iyi kimseler şeklinde tanımlanmıştır.

Kaotik tarafsız: Bu yönelimdeki kimseler, kendi davranışları dahil hiç bir şeyin kontrollü olmasını istemez. Bu tip karakterler için iyi ya da kötü bir anlam ifade etmez. Davranışlarını kestirmek çok güçtür. Bu karakterler içlerinden ne geçiyorsa onu yaparlar. Bütün mal varlıklarını kumara yatırabilirler, davranışları tamamen tutarsızdır. Bu yönelim görece kontrolü en zor yönelimdir. Kaotik tarafsıza örnek olarak akıl hastaları verilebilir.

Kaotik kötü:  Bunlar, iyi ve düzenli olan her şey için bir felakettir. Kişisel kazanç ve zevk için hareket ederler. İstediklerini almak için her türlü yola başvurmakta yanlış bir yan görmezler. Kurallar ve yönetimler kendini savunamayanlar içindir. Güçlü olanlar istediğini alır, zayıflarsa ezilir. Bunlar grup oluşturduklarında birlikte hareket etme amacı gütmez, daha ziyade daha güçlü düşmanlara karşı koyarlar. Böylesi bir grup yalnızca diğerlerini emirlerini uymaya zorlayabilecek güçlü bir lider tarafından birlikte tutulabilir.Ayrıca ilk gösterdiği zayıflık belirtisinde başka birisi liderliği onun elinden alır. Suçlamaları nerdeyse hiçbir zaman kabul etmezler.

"""

karaktertipi="""
“Mimar” kişiliği        daha fazla bilgi için; https://www.16personalities.com/tr/intj-ki%C5%9Fili%C4%9Fi

Mantıkçı” kişiliği      daha fazla bilgi için; https://www.16personalities.com/tr/intp-ki%C5%9Fili%C4%9Fi

Buyurucu kişiliği       daha fazla bilgi için; https://www.16personalities.com/tr/entj-ki%C5%9Fili%C4%9Fi

Tartışmacı kişiliği     daha fazla bilgi için; https://www.16personalities.com/tr/entp-ki%C5%9Fili%C4%9Fi

Savunucu kişiliği       daha fazla bilgi için; https://www.16personalities.com/tr/infj-ki%C5%9Fili%C4%9Fi

Arabulucu kişiliği      daha fazla bilgi için; https://www.16personalities.com/tr/infp-ki%C5%9Fili%C4%9Fi

Önder kişiliği          daha fazla bilgi için; https://www.16personalities.com/tr/enfj-ki%C5%9Fili%C4%9Fi

Kampanyacı kişiliği     daha fazla bilgi için; https://www.16personalities.com/tr/enfp-ki%C5%9Fili%C4%9Fi

Lojistikçi kişiliği     daha fazla bilgi için; https://www.16personalities.com/tr/istj-ki%C5%9Fili%C4%9Fi

Savunmacı kişiliği      daha fazla bilgi için; https://www.16personalities.com/tr/isfj-ki%C5%9Fili%C4%9Fi

Yönetici kişiliği       daha fazla bilgi için; https://www.16personalities.com/tr/estj-ki%C5%9Fili%C4%9Fi

Konsül kişiliği         daha fazla bilgi için; https://www.16personalities.com/tr/esfj-ki%C5%9Fili%C4%9Fi

Becerikli kişiliği      daha fazla bilgi için; https://www.16personalities.com/tr/istp-ki%C5%9Fili%C4%9Fi

Maceracı kişiliği       daha fazla bilgi için; https://www.16personalities.com/tr/isfp-ki%C5%9Fili%C4%9Fi

Girişimci kişiliği      daha fazla bilgi için; https://www.16personalities.com/tr/estp-ki%C5%9Fili%C4%9Fi

Eğlendirici kişiliği    daha fazla bilgi için; https://www.16personalities.com/tr/esfp-ki%C5%9Fili%C4%9Fi

"""

#anapencere objesi tanımlama
anapencere=tk.Tk() #anapencere objesi oluştu
anapencere.geometry("1300x800") #anapencerenin boyutları
#anapencere.iconbitmap(r'C:\Users\burak\OneDrive\Desktop\PythonProjeler\generator\icon1.ico')
anapencere.title("Yazarlar İçin Türetici")


######################################################################################################################################################
"""SEKMELER OLUŞTURULUYOR..."""
######################################################################################################################################################

#birincil sekme objesi tanımlama(bağlı olduğu sekme;anapencere      içindekiler;Giriş,Türetici,Veritabanı,Hakkında&İletişim)
tabs1=ttk.Notebook(anapencere,width=1800,height=850)
tabs1.place(x=50,y=50)
#birincil sekme oluşturma
tab1=ttk.Frame(tabs1,width=300,height=300)
tab2=ttk.Frame(tabs1,width=300,height=300)
tab4=ttk.Frame(tabs1,width=300,height=300)
#birincil sekmeleri ekleme
tabs1.add(tab1,text="Giriş")
tabs1.add(tab2,text="Türetici") #isim türet #karakter türet #ülke türet #evren türet
tabs1.add(tab4,text="Hakkında & İletişim")
##ikincil sekme objesi tanımlama(bağlı olduğu sekme;tab2       İçindekiler;İsim Türet,Karakter Türet,Ülke Türet,Evren Türet)
tabs2=ttk.Notebook(tab2,width=1800,height=850)
tabs2.place(x=0,y=0)
##ikincil sekmeleri oluşturma
tab5=ttk.Frame(tabs2,width=300,height=300)
tab6=ttk.Frame(tabs2,width=300,height=300)  
tab7=ttk.Frame(tabs2,width=300,height=300)
##ikincil sekmeleri ekleme
tabs2.add(tab5,text="İsim Türetici")
tabs2.add(tab6,text="Karakter Türetici")
tabs2.add(tab7,text="Ülke Türetici")
###üçüncül sekme objesi tanımlama(bağlı olduğu sekme;tab6       İçindekiler;Hızlı Oluştur,Kendin Oluştur)
tabs3=ttk.Notebook(tab6,width=1800,height=850)
tabs3.place(x=0,y=0)
###üçüncül sekmeleri oluşturma
tab9=ttk.Frame(tabs3,width=300,height=300)
tab10=ttk.Frame(tabs3,width=300,height=300)
###üçüncül sekmeleri ekleme
tabs3.add(tab9,text="Hızlı Oluştur")
tabs3.add(tab10,text="Kendin Oluştur")




######################################################################################################################################################
"""TEMALAR OLUŞTURULUYOR"""
######################################################################################################################################################
backround100="gray22"
foreground100="DeepSkyBlue2"  #"DeepPink4"
background101="sky blue4"
foreground101="gray80"
background102="lemon chiffon2"
foreground102="DarkOrange1"
tema1=ttk.Style()
tema1.configure("BW.TLabel", foreground=foreground100, background="gray22",font=("Arial",12,"bold"))

######################################################################################################################################################
"""KANVASLAR OLUŞTURULUYOR"""
######################################################################################################################################################
def create_canvas():
    tema_kanvas_1=tk.Canvas(tab1,width=1800,height=850,background=backround100).place(x=0,y=0)
    tema_kanvas_4=tk.Canvas(tab4,width=1800,height=850,background=backround100).place(x=0,y=0)
    tema_kanvas_5=tk.Canvas(tab5,width=1800,height=850,background=backround100).place(x=0,y=0)
    tema_kanvas_7=tk.Canvas(tab7,width=1800,height=850,background=backround100).place(x=0,y=0) #sekme atayacağım zaman silmem gerekir
    #tema_kanvas_8=tk.Canvas(tab8,width=1000,height=550,background=backround100).place(x=0,y=0) #sekme atayacağım zaman silmem gerekir
    tema_kanvas_9=tk.Canvas(tab9,width=1800,height=850,background=backround100).place(x=0,y=0)
    tema_kanvas_10=tk.Canvas(tab10,width=1800,height=850,background=backround100).place(x=0,y=0)
    
create_canvas()
######################################################################################################################################################
"""FONKSİYONLAR OLUŞTURULUYOR"""
######################################################################################################################################################
def function_name_checkbox_generator():
    #kullanıcı kaç hece seçmiş ise listeden o kadar eleman seç
    kosul=choice_name_generator.get()
    if (kosul=="İki Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        #Yazdırılıyor
        label_name_generator3.configure(text=name)
        return name   
    elif (kosul=="Üç Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        ucuncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        #Yazdırılıyor
        label_name_generator3.configure(text=name)
        return name
    elif (kosul=="Dört Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        ucuncu_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ucuncu_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        dorduncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        #Yazdırılıyor
        label_name_generator3.configure(text=name)
        return name
    elif (kosul=="Beş Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)  
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        ucuncu_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ucuncu_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        dorduncu_hece=random.choice(vt_pt1)
        #vt_pt1.remove(dorduncu_hece)   #hece attıkça kelime türetme kaabiliyeti düşüyor
        besinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece+besinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        #Yazdırılıyor
        label_name_generator3.configure(text=name)
        return name
    elif (kosul=="Rastgele"):
        #rastgele sayı üretiyor (2 ve 5 arası hece olur)
        kosul=random.randint(2,5)
        #koşullar oluşturulur
        if (kosul==2):
            #Veri çekiyor
            ilk_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
            ikinci_hece=random.choice(vt_pt1)
            #İsim Oluşturuyor
            name=ilk_hece+ikinci_hece
            #ilk harfi büyük yapar
            name=name.capitalize() 
            #Yazdırılıyor
            label_name_generator3.configure(text=name)
            return name   
        elif (kosul==3):
            #Veri çekiyor
            ilk_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
            ikinci_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
            ucuncu_hece=random.choice(vt_pt1)
            #İsim Oluşturuyor
            name=ilk_hece+ikinci_hece+ucuncu_hece
            #ilk harfi büyük yapar
            name=name.capitalize() 
            #Yazdırılıyor
            label_name_generator3.configure(text=name)
            return name
        elif (kosul==4):
            #Veri çekiyor
            ilk_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
            ikinci_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
            ucuncu_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ucuncu_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
            dorduncu_hece=random.choice(vt_pt1)
            #İsim Oluşturuyor
            name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece
            #ilk harfi büyük yapar
            name=name.capitalize() 
            #Yazdırılıyor
            label_name_generator3.configure(text=name)
            return name
        elif (kosul==5):
            #Veri çekiyor
            ilk_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
            ikinci_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
            ucuncu_hece=random.choice(vt_pt1)
            #vt_pt1.remove(ucuncu_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
            dorduncu_hece=random.choice(vt_pt1)
            #vt_pt1.remove(dorduncu_hece)   #hece attıkça kelime türetme kaabiliyeti düşüyor
            besinci_hece=random.choice(vt_pt1)
            #İsim Oluşturuyor
            name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece+besinci_hece
            #ilk harfi büyük yapar
            name=name.capitalize() 
            #Yazdırılıyor
            label_name_generator3.configure(text=name)
            return name

def function_name_random_generator():
    kosul=random.randint(2,5)
    #koşullar oluşturulur
    if (kosul==2):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize()
        name1="İsim: {}".format(name)
        return name1   
    elif (kosul==3):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        ucuncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        name1="İsim: {}".format(name)
        return name1

    elif (kosul==4):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        ucuncu_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ucuncu_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        dorduncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        name1="İsim: {}".format(name)
        return name1
    elif (kosul==5):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ilk_hece)    #hece attıkça kelime türetme kaabiliyeti düşüyor
        ikinci_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ikinci_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        ucuncu_hece=random.choice(vt_pt1)
        #vt_pt1.remove(ucuncu_hece) #hece attıkça kelime türetme kaabiliyeti düşüyor
        dorduncu_hece=random.choice(vt_pt1)
        #vt_pt1.remove(dorduncu_hece)   #hece attıkça kelime türetme kaabiliyeti düşüyor
        besinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece+besinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        name1="İsim: {}".format(name)
        return name1

def print_notepad():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','isimler.txt') 
    a="a"
    file = open(desktop,a) # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
    veri=function_name_checkbox_generator()
    file.write(veri+"\n")
    file.close()  # Dosyayı kapatmak

def print_notepad_character():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','karakter.txt') 
    a="a"
    file = open(desktop,a) # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
    veri1=function_name_random_generator()
    veri2=function_age_generator()
    veri3=function_character_sex_generator()
    veri4=function_character_physical_attribute_generator()
    veri5=function_character_job_generator()
    veri6=function_character_luckiness_generator()
    veri7=function_characterclass_generator()
    veri8=function_character_hobies_generator()
    veri10=function_random_generator_cinselyonelim()
    veri11=function_random_generator_karakteryonelimi()
    veri9=function_guzel_bastirmak()
    file.write(veri1+"\n")  
    file.write(veri2+"\n")
    file.write(veri3+"\n")
    file.write(veri4+"\n")
    file.write(veri5+"\n")
    file.write(veri6+"\n")
    file.write(veri7+"\n")
    file.write(veri8+"\n")
    file.write(veri10+"\n")
    file.write(veri11+"\n")
    file.write(veri9+"\n")
    file.close()





#karakter tiplerini yaratır ve 2 tane baskın özellik seçer
def function_characterclass_generator():
    kosul=random.choice(vt_kt1)
    if (kosul=='Mimar:INTJ-A / INTJ-T'):
        secim1=random.choice(personalities1_mimar)
        personalities1_mimar.remove(secim1)
        secim2=random.choice(personalities1_mimar)
        a="Karakter tipi: Mimar = INTJ-A / INTJ-T\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Mantıkçı:INTP-A / INTP-T'):
        secim1=random.choice(personalities2_mantikci)
        personalities2_mantikci.remove(secim1)
        secim2=random.choice(personalities2_mantikci)
        a="Karakter tipi: 'Mantıkçı = INTP-A / INTP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Buyurucu:ENTJ-A / ENTJ-T'):
        secim1=random.choice(personalities3_buyurucu)
        personalities3_buyurucu.remove(secim1)
        secim2=random.choice(personalities3_buyurucu)
        a="Karakter tipi: 'Buyurucu = ENTJ-A / ENTJ-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Tartışmacı:ENTP-A / ENTP-T'):
        secim1=random.choice(personalities4_tartismaci)
        personalities4_tartismaci.remove(secim1)
        secim2=random.choice(personalities4_tartismaci)
        a="Karakter tipi: 'Tartışmacı:ENTP-A / ENTP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Savunucu:INFJ-A / INFJ-T'):
        secim1=random.choice(personalities5_savunucu)
        personalities5_savunucu.remove(secim1)
        secim2=random.choice(personalities5_savunucu)
        a="Karakter tipi: 'Savunucu = INFJ-A / INFJ-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Arabulucu:INFP-A / INFP-T'):
        secim1=random.choice(personalities6_arabulucu)
        personalities6_arabulucu.remove(secim1)
        secim2=random.choice(personalities6_arabulucu)
        a="Karakter tipi: 'Arabulucu = INFP-A / INFP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Önder:ENFJ-A / ENFJ-T'):
        secim1=random.choice(personalities7_onder)
        personalities7_onder.remove(secim1)
        secim2=random.choice(personalities7_onder)
        a="Karakter tipi: 'Önder = ENFJ-A / ENFJ-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Kampanyacı:ENFP-A / ENFP-T'):
        secim1=random.choice(personalities8_kampanyaci)
        personalities8_kampanyaci.remove(secim1)
        secim2=random.choice(personalities8_kampanyaci)
        a="Karakter tipi: 'Kampanyacı = ENFP-A / ENFP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Lojistikçi:ISTJ-A / ISTJ-T'):
        secim1=random.choice(personalities9_lojistikci)
        personalities9_lojistikci.remove(secim1)
        secim2=random.choice(personalities9_lojistikci)
        a="Karakter tipi: 'Lojistikçi = ISTJ-A / ISTJ-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Savunmacı:ISFJ-A / ISFJ-T'):
        secim1=random.choice(personalities10_savunmaci)
        personalities10_savunmaci.remove(secim1)
        secim2=random.choice(personalities10_savunmaci)
        a="Karakter tipi: 'Savunmacı = ISFJ-A / ISFJ-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Yönetici:ESTJ-A / ESTJ-T'):
        secim1=random.choice(personalities11_yonetici)
        personalities11_yonetici.remove(secim1)
        secim2=random.choice(personalities11_yonetici)
        a="Karakter tipi: 'Yönetici = ESTJ-A / ESTJ-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Konsül:ESFJ-A / ESFJ-T'):
        secim1=random.choice(personalities12_konsul)
        personalities12_konsul.remove(secim1)
        secim2=random.choice(personalities12_konsul)
        a="Karakter tipi: 'Konsül = ESFJ-A / ESFJ-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Becerikli:ISTP-A / ISTP-T'):
        secim1=random.choice(personalities13_becerikli)
        personalities13_becerikli.remove(secim1)
        secim2=random.choice(personalities13_becerikli)
        a="Karakter tipi: 'Becerikli = ISTP-A / ISTP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Maceracı:ISFP-A / ISFP-T'):
        secim1=random.choice(personalities14_maceraci)
        personalities14_maceraci.remove(secim1)
        secim2=random.choice(personalities14_maceraci)
        a="Karakter tipi: 'Maceracı = ISFP-A / ISFP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Girişimci:ESTP-A / ESTP-T'):
        secim1=random.choice(personalities15_girisimci)
        personalities15_girisimci.remove(secim1)
        secim2=random.choice(personalities15_girisimci)
        a="Karakter tipi: 'Girişimci = ESTP-A / ESTP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b
    elif (kosul=='Eğlendirici:ESFP-A / ESFP-T'):
        secim1=random.choice(personalities16_eglendirici)
        personalities16_eglendirici.remove(secim1)
        secim2=random.choice(personalities16_eglendirici)
        a="Karakter tipi: 'Eğlendirici = ESFP-A / ESFP-T'\n"
        b="Karakterin baskın özellikleri: {},{}".format(secim1,secim2)
        return a+b

#Kadın-Erkek, Boy, Kilo, Vücut Kitle Endeksi Yaratır
def function_character_sex_generator():
    sex=random.randint(1,2)
    if sex==1:
        kilo=random.randint(1,3) #üç kategoride şişmanlık derecesi
        if kilo==1:
            a=random.randint(45,55)
        elif kilo==2:
            a=random.randint(56,75)
        elif kilo==3:
            a=random.randint(76,90)
        boy=random.randint(1,3)
        if boy==1:
            b=random.randint(150,160)
        elif boy==2:
            b=random.randint(161,180)
        elif boy==3:
            b=random.randint(181,199)
        indeks=a/((b/100)**2)
        if (indeks<=20):
            c="Zayıf"
        elif (20<=indeks<=25):
            c="Normal"
        elif (25<=indeks<=30):
            c="Aşırı kilolu"
        elif (30<=indeks<=40):
            c="Obez"
        elif (40<=indeks):
            c="Aşırı obez"
        sonuc=("Cinsiyet: Kadın, Kilo: {}, Boy: {}, Vücut Kitle Endeksi: {} Sonuç: {}".format(a,b,round(indeks,2),c))
        return sonuc
    if sex==2:
        kilo=random.randint(1,3) #üç kategoride şişmanlık derecesi
        if kilo==1:
            a=random.randint(50,65)
        elif kilo==2:
            a=random.randint(66,80)
        elif kilo==3:
            a=random.randint(81,105)
        boy=random.randint(1,3)
        if boy==1:
            b=random.randint(150,160)
        elif boy==2:
            b=random.randint(161,180)
        elif boy==3:
            b=random.randint(181,199)
        indeks=a/((b/100)**2)
        if (indeks<=20):
            c="Zayıf"
        elif (20<=indeks<=25):
            c="Normal"
        elif (25<=indeks<=30):
            c="Aşırı kilolu"
        elif (30<=indeks<=40):
            c="Obez"
        elif (40<=indeks):
            c="Aşırı obez"
        sonuc=("Cinsiyet: Erkek, Kilo: {}, Boy: {}, Vücut Kitle Endeksi: {} Sonuç: {}".format(a,b,round(indeks,2),c))
        return sonuc

#meslek ve servet
def function_character_job_generator():
    #57.satır
    #68.satır
    a=random.choice(meslekler) #meslek
    b=random.randint(1,100)
    if 1<=b<20:
        c="Çok fakir"
    elif 21<=b<40:
        c="Fakir"
    elif 41<=b<80:
        c="Orta halli"
    elif 81<=b<96:
        c="Zengin"
    elif 96<=b<101:
        c="Çok zengin"
    asd="Meslek: {}\nMaddi durum: {}".format(a,c)
    return asd

#hobiler,fobiler, kitap ve film
def function_character_hobies_generator():
    a=random.choice(hobiler) #hobi
    hobiler.remove(a)
    b=random.choice(hobiler) #hobi
    c=random.choice(fobiler) #fobiler
    fobiler.remove(c)
    d=random.choice(fobiler) #fobiler
    e=random.choice(en_sevilen_kitaplar) #en sevilen kitaplar
    en_sevilen_kitaplar.remove(e)
    f=random.choice(en_sevilen_kitaplar) #en sevilen kitaplar
    g=random.choice(en_sevilen_filmler) #en sevilen filmler
    en_sevilen_filmler.remove(g)
    h=random.choice(en_sevilen_filmler) #en sevilen filmler
    j=random.choice(inanclar) #din
    i="Hobiler: {}, {}\nFobiler: {}, {}\nEn sevilen kitaplar: {}, {}\nEn sevilen filmler: {}, {}\nİnanç: {}".format(a,b,c,d,e,f,g,h,j)
    return i

#ten rengi,göz,burun saç vs.
def function_character_physical_attribute_generator():
    a=random.choice(ten_rengi)
    b=random.choice(goz_rengi)
    c=random.choice(burun_sekli)
    d=random.choice(sac_rengi)
    e=random.choice(sac_sekli)
    f=random.choice(sac_tipi)
    g=random.choice(sac_uzunlugu)
    h="Ten rengi: {}\nGöz rengi: {}\nBurun şekli: {}\nSaç rengi: {}\nSaç şekli: {}\nSaç tipi: {}\nSaç uzunluğu: {}".format(a,b,c,d,e,f,g)
    return h

#Sağlık durumu
def function_character_luckiness_generator():
    luckiness=random.randint(1,3)
    if luckiness==1:
        a=random.choice(hastaliklar)
        health="Hastalıklar: {}".format(a)
        return health
    elif luckiness==2:
        a=random.choice(hastaliklar)
        hastaliklar.remove(a)
        b=random.choice(hastaliklar)
        health="Hastalıklar: {}, {}".format(a,b)
        return health
    elif luckiness==3:
        a=random.choice(hastaliklar)
        hastaliklar.remove(a)
        b=random.choice(hastaliklar)
        hastaliklar.remove(b)
        c=random.choice(hastaliklar)
        health="Hastalıklar: {}, {}, {}".format(a,b,c)
        return health
    
def function_age_generator():
    a=random.randint(1,3) #(Genç,Yetişkin,Yaşlı)
    if a==1:
        b=random.randint(18,30)
        dogum_tarihi=random.randint(1,28)
        dogum_ayi=random.choice(aylar)
        c="Doğum Tarihi: {} {}, Yaş: {}, Durum: Genç".format(dogum_tarihi,dogum_ayi,b)
        return c
    elif a==2:
        b=random.randint(31,60)
        dogum_tarihi=random.randint(1,28)
        dogum_ayi=random.choice(aylar)
        c="Doğum Tarihi: {} {}, Yaş: {}, Durum: Orta yaşlı".format(dogum_tarihi,dogum_ayi,b)
        return c
    elif a==3:
        b=random.randint(61,100)
        dogum_tarihi=random.randint(1,28)
        dogum_ayi=random.choice(aylar)
        c="Doğum Tarihi: {} {}, Yaş: {}, Durum: Yaşlı".format(dogum_tarihi,dogum_ayi,b)
        return c

def function_guzel_bastirmak():
    a="""
*****************************************************************************************************************************************

*****************************************************************************************************************************************"""
    return a

def function_random_generator_cinselyonelim():
    a=random.choice(cinselyonelim)
    sonuc="Cinsel yönelim: {}".format(a)
    return sonuc

def function_random_generator_karakteryonelimi():
    a=random.choice(karakteryonelimi)
    sonuc="Karakter yönelimi: {}".format(a)
    return sonuc
###############################################################################################################################################
def turet_ve_yazdir():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','karakter.txt') 
    a="a"
    file = open(desktop,a) # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
    veri1=function_name_kendinolustur_generator()
    veri2=function_character_kendinhazirla_yas()
    veri3=function_character_kendinhazirla_dogumtarihi()
    veri4=function_character_kendinhazirla_cinsiyet()
    veri5=function_character_kendinhazirla_kvb()
    veri6=function_character_kendinhazirla_ten()
    veri7=function_character_kendinhazirla_goz()
    veri8=function_character_kendinhazirla_burun()
    veri9=function_character_kendinhazirla_sacrengi()
    veri10=function_character_kendinhazirla_sacsekli()
    veri11=function_character_kendinhazirla_sactipi()
    veri12=function_character_kendinhazirla_sacuzunluk()
    veri13=function_character_kendinhazirla_meslek()
    veri14=function_character_kendinhazirla_servet()
    veri15=function_character_kendinhazirla_kartipi()
    veri16=function_character_kendinhazirla_ko()
    veri17=function_character_kendinhazirla_hobiler()
    veri18=function_character_kendinhazirla_fobiler()
    veri19=function_character_kendinhazirla_filmler()
    veri20=function_character_kendinhazirla_kitaplar()
    veri21=function_character_kendinhazirla_inanc()
    veri22=function_character_kendinhazirla_cy()
    veri23=function_character_kendinhazirla_ky()
    veri24=function_character_kendinhazirla_zeka()
    veri30=function_guzel_bastirmak()
    file.write(veri1+"\n")  
    file.write(veri2+"\n")
    file.write(veri3+"\n")
    file.write(veri4+"\n")
    file.write(veri5+"\n")
    file.write(veri6+"\n")
    file.write(veri7+"\n")
    file.write(veri8+"\n")
    file.write(veri9+"\n")
    file.write(veri10+"\n")
    file.write(veri11+"\n")
    file.write(veri12+"\n")
    file.write(veri13+"\n")
    file.write(veri14+"\n")
    file.write(veri15+"\n")
    file.write(veri16+"\n")
    file.write(veri17+"\n")
    file.write(veri18+"\n")
    file.write(veri19+"\n")
    file.write(veri20+"\n")
    file.write(veri21+"\n")
    file.write(veri22+"\n")
    file.write(veri23+"\n")
    file.write(veri24+"\n")
    file.write(veri30+"\n")
    file.close()
###############################################################################################################################################

def function_name_kendinolustur_generator():
    kosul=combobox_veri_cekici_isim2.get()
    if (kosul=="İki Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize()
        name1="İsim: {}".format(name)
        return name1   
    elif (kosul=="Üç Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        vt_pt1.remove(ikinci_hece)
        ucuncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        name1="İsim: {}".format(name)
        return name1

    elif (kosul=="Dört Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        vt_pt1.remove(ikinci_hece)
        ucuncu_hece=random.choice(vt_pt1)
        vt_pt1.remove(ucuncu_hece)
        dorduncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        name1="İsim: {}".format(name)
        return name1
    elif (kosul=="Beş Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        vt_pt1.remove(ikinci_hece)
        ucuncu_hece=random.choice(vt_pt1)
        vt_pt1.remove(ucuncu_hece)
        dorduncu_hece=random.choice(vt_pt1)
        vt_pt1.remove(dorduncu_hece)
        besinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece+besinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        name1="İsim: {}".format(name)
        return name1

def function_character_kendinhazirla_yas():
    kosul=combobox_veri_cekici3.get()
    if kosul=="Genç":
        a=random.randint(18,30)
        durum="Genç"
        sonuc="Yaş: {}, Durum: {}".format(a,durum)
        return sonuc
    elif kosul=="Orta yaşlı":
        a=random.randint(31,60)
        durum="Orta yaşlı"
        sonuc="Yaş: {}, Durum: {}".format(a,durum)
        return sonuc
    elif kosul=="Yaşlı":
        a=random.randint(61,100)
        durum="Yaşlı"
        sonuc="Yaş: {}, Durum: {}".format(a,durum)
        return sonuc
    elif kosul=="Rastgele":
        rastgele=random.randint(1,3)
        if rastgele==1:
            a=random.randint(18,30)
            durum="Genç"
            sonuc="Yaş: {}, Durum: {}".format(a,durum)
            return sonuc
        elif rastgele==2:
            a=random.randint(31,60)
            durum="Orta yaşlı"
            sonuc="Yaş: {}, Durum: {}".format(a,durum)
            return sonuc
        elif rastgele==3:
            a=random.randint(61,100)
            durum="Yaşlı"
            sonuc="Yaş: {}, Durum: {}".format(a,durum)
            return sonuc

def function_character_kendinhazirla_dogumtarihi():
    gun=entry_karakter_kendin_yap_dogumtarihi.get()
    g=int(gun)
    ay=entry_karakter_kendin_yap_dogumtarihi_2.get()
    yil=entry_karakter_kendin_yap_dogumtarihi_3.get()
    yil=int(yil)
    sonuc="Doğum Tarihi: {}/{}/{}".format(g,ay,yil)
    return sonuc
    
def function_character_kendinhazirla_cinsiyet():
    kosul=combobox_veri_cekici4.get()
    if kosul=="Erkek":
        sonuc="Cinsiyet: Erkek"
        return sonuc
    elif kosul=="Kadın":
        sonuc="Cinsiyet: Kadın"
        return sonuc
    
def function_character_kendinhazirla_kvb():
    kilo=float(entry_karakter_kendin_yap_kvb.get())
    kilo=round(kilo,2)
    boy=float(entry_karakter_kendin_yap_kvb_2.get())
    boy=round(boy,2)
    a="Zayıf"
    b="Normal"
    c="Şişman"
    d="Obez"
    e="Aşırı obez"
    indeks=kilo/((boy/100)**2)
    indeks=round(indeks,2)
    if 0<indeks<=20:
        sonuc="Kilo: {}, Boy: {}, Vücut kitle indeksi: {}, Sonuç: {}".format(kilo,boy,indeks,a)
        return sonuc
    elif 20<indeks<=25:
        sonuc="Kilo: {}, Boy: {}, Vücut kitle indeksi: {}, Sonuç: {}".format(kilo,boy,indeks,b)
        return sonuc
    elif 25<indeks<=30:
        sonuc="Kilo: {}, Boy: {}, Vücut kitle indeksi: {}, Sonuç: {}".format(kilo,boy,indeks,c)
        return sonuc
    elif 30<=indeks<=40:
        sonuc="Kilo: {}, Boy: {}, Vücut kitle indeksi: {}, Sonuç: {}".format(kilo,boy,indeks,d)
        return sonuc
    elif 40<indeks:
        sonuc="Kilo: {}, Boy: {}, Vücut kitle indeksi: {}, Sonuç: {}".format(kilo,boy,indeks,e)
        return sonuc

def function_character_kendinhazirla_ten():
    kosul=combobox_veri_cekici_ten.get()
    if kosul=='Çok açık veya Beyaz cilt':
        a='Çok açık veya Beyaz cilt'
        sonuc="Ten rengi: {}".format(a)
        return sonuc
    
    elif kosul=='Açık cilt veya Avrupalı':
        a='Açık cilt veya Avrupalı'
        sonuc="Ten rengi: {}".format(a)
        return sonuc

    elif kosul=='Orta açık/buğday cilt veya Güney Avrupalı':
        a='Orta açık/buğday cilt veya Güney Avrupalı'
        sonuc="Ten rengi: {}".format(a)
        return sonuc

    elif kosul=='Orta koyu/esmer veya Akdenizli':
        a='Orta koyu/esmer veya Akdenizli'
        sonuc="Ten rengi: {}".format(a)
        return sonuc

    elif kosul=='Koyu cilt rengi veya kahverengi':
        a='Koyu cilt rengi veya kahverengi'
        sonuc="Ten rengi: {}".format(a)
        return sonuc

    elif kosul=='Çok koyu cilt rengi veya siyahi tipi':
        a='Çok koyu cilt rengi veya siyahi tipi'
        sonuc="Ten rengi: {}".format(a)
        return sonuc

def function_character_kendinhazirla_goz():
    kosul=combobox_veri_cekici_goz.get()
    if kosul=='Açık kahverengi göz':
        a='Açık kahverengi göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc
    elif kosul=='Kahverengi göz':
        a='Kahverengi göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc
    elif kosul=='Koyu kahverengi göz / Siyah göz':
        a='Koyu kahverengi göz / Siyah göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc
    elif kosul=='Mavi göz':
        a='Mavi göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc
    elif kosul=='Yeşil göz':
        a='Yeşil göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc
    elif kosul=='Ela göz':
        a='Ela göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc
    elif kosul=='Kehribar göz':
        a='Kehribar göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc
    elif kosul=='Gri göz':
        a='Gri göz'
        sonuc="Göz rengi: {}".format(a)
        return sonuc

def function_character_kendinhazirla_burun():
    kosul=combobox_veri_cekici_burun.get()
    if kosul=="Kemerli burun":
        a="Kemerli burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Ucu düşük burun":
        a="Ucu düşük burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Ucu geniş burun":
        a="Ucu geniş burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Ucu dar burun":
        a="Ucu dar burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Ucu sivri uzun burun":
        a="Ucu sivri uzun burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Ucu kalkık kısa burun":
        a="Ucu kalkık kısa  burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Eğri burun":
        a="Eğri burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Sivri burun":
        a="Sivri burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Burun tabanı geniş":
        a="Burun tabanı geniş"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Geniş burun":
        a="Geniş burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Dar burun":
        a="Dar burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc
    elif kosul=="Semer burun":
        a="Semer burun"
        sonuc="Burun şekli: {}".format(a)
        return sonuc

def function_character_kendinhazirla_sacrengi():
    kosul=combobox_veri_cekici_sacrengi.get()
    if kosul=="Siyah":
        sac="Saç rengi: Siyah"
        return sac
    elif kosul=="Koyu kahve":
        sac="Saç rengi: Koyu kahve"
        return sac
    elif kosul=="Kahverengi":
        sac="Saç rengi: Kahverengi"
        return sac
    elif kosul=="Açık kahve":
        sac="Saç rengi: Açık kahve"
        return sac
    elif kosul=="Koyu sarı":
        sac="Saç rengi: Koyu sarı"
        return sac
    elif kosul=="Sarı":
        sac="Saç rengi: Sarı"
        return sac
    elif kosul=="Açık sarı":
        sac="Saç rengi: Açık sarı"
        return sac
    elif kosul=="Bakır":
        sac="Saç rengi: Bakır"
        return sac
    elif kosul=="Turuncu":
        sac="Saç rengi: Turuncu"
        return sac
    elif kosul=="Kumral":
        sac="Saç rengi: Kumral"
        return sac

def function_character_kendinhazirla_sacuzunluk():
    kosul=combobox_veri_cekici_sacuzunluk.get()
    if kosul=="Kısa saç":
        sac="Saç uzunluğu: Kısa saç"
        return sac
    elif kosul=="Uzun saç":
        sac="Saç uzunluğu: Uzun saç"
        return sac
    
def function_character_kendinhazirla_sactipi():
    kosul=combobox_veri_cekici_sactipi.get()
    if kosul=="İnce telli":
        sac="Saç tipi: İnce telli"
        return sac
    elif kosul=="Normal":
        sac="Saç tipi: Normal"
        return sac
    elif kosul=="Kalın telli":
        sac="Saç tipi: Kalın telli"
        return sac
    
def function_character_kendinhazirla_sacsekli():
    kosul=combobox_veri_cekici_sacsekli.get()
    if kosul=="Düz":
        sac="Saç şekli: Düz"
        return sac
    elif kosul=="Kıvırcık":
        sac="Saç şekli: Kıvırcık"
        return sac
    elif kosul=="Dalgalı":
        sac="Saç şekli: Dalgalı"
        return sac

def function_character_kendinhazirla_meslek():
    meslek=entry_karakter_kendin_yap_meslek.get()
    sonuc="Meslek: {}".format(meslek)
    return sonuc

def function_character_kendinhazirla_servet():
    kosul=combobox_veri_cekici_servet.get()
    a="Fakir"
    b="Çok fakir"
    c="Açlık sınırında"
    d="Orta halli"
    e="Zengin"
    f="Çok zengin"
    if kosul=="Fakir":
        sonuc="Maddi durum: {}".format(a)
        return sonuc
    elif kosul=="Çok fakir":
        sonuc="Maddi durum: {}".format(b)
        return sonuc
        
    elif kosul=="Açlık sınırında":
        sonuc="Maddi durum: {}".format(c)
        return sonuc
        
    elif kosul=="Orta halli":
        sonuc="Maddi durum: {}".format(d)
        return sonuc
        
    elif kosul=="Zengin":
        sonuc="Maddi durum: {}".format(e)
        return sonuc
        
    elif kosul=="Çok zengin":
        sonuc="Maddi durum: {}".format(f)
        return sonuc
        
def function_character_kendinhazirla_hastalık():
    hastalık=entry_karakter_kendin_yap_meslek.get()
    sonuc="Hastalık: {}".format(hastalık)
    return sonuc

def function_character_kendinhazirla_kartipi():
    kosul=combobox_veri_cekici_kartipi.get()
    if kosul=='Mimar: INTJ-A / INTJ-T':
        sonuc="Karakter tipi: Mimar:INTJ-A / INTJ-T"
        return sonuc
    elif kosul=='Mantıkçı: INTP-A / INTP-T':
        sonuc="Karakter tipi: Mimar:INTJ-A / INTJ-T"
        return sonuc
    elif kosul=='Buyurucu: ENTJ-A / ENTJ-T':
        sonuc="Karakter tipi: Buyurucu:ENTJ-A / ENTJ-T"
        return sonuc
    elif kosul=='Tartışmacı: ENTP-A / ENTP-T':
        sonuc="Karakter tipi: Tartışmacı:ENTP-A / ENTP-T"
        return sonuc
    elif kosul=='Savunucu: INFJ-A / INFJ-T':
        sonuc="Karakter tipi:Savunucu:INFJ-A / INFJ-T"
        return sonuc
    elif kosul=='Arabulucu: INFP-A / INFP-T':
        sonuc="Karakter tipi: Arabulucu:INFP-A / INFP-T"
        return sonuc
    elif kosul=='Önder: ENFJ-A / ENFJ-T':
        sonuc="Karakter tipi: Önder:ENFJ-A / ENFJ-T"
        return sonuc
    elif kosul=='Kampanyacı: ENFP-A / ENFP-T':
        sonuc="Karakter tipi: Kampanyacı:ENFP-A / ENFP-T"
        return sonuc
    elif kosul=='Lojistikçi: ISTJ-A / ISTJ-T':
        sonuc="Karakter tipi: Lojistikçi:ISTJ-A / ISTJ-T"
        return sonuc
    elif kosul=='Savunmacı: ISFJ-A / ISFJ-T':
        sonuc="Karakter tipi: Savunmacı:ISFJ-A / ISFJ-T"
        return sonuc
    elif kosul=='Yönetici: ESTJ-A / ESTJ-T':
        sonuc="Karakter tipi: Yönetici:ESTJ-A / ESTJ-T"
        return sonuc
    elif kosul=='Konsül: ESFJ-A / ESFJ-T':
        sonuc="Karakter tipi: Konsül:ESFJ-A / ESFJ-T"
        return sonuc
    elif kosul=='Becerikli: ISTP-A / ISTP-T':
        sonuc="Karakter tipi: Becerikli:ISTP-A / ISTP-T"
        return sonuc
    elif kosul=='Maceracı: ISFP-A / ISFP-T':
        sonuc="Karakter tipi: Maceracı:ISFP-A / ISFP-T"
        return sonuc
    elif kosul=='Girişimci: ESTP-A / ESTP-T':
        sonuc="Karakter tipi: Girişimci:ESTP-A / ESTP-T"
        return sonuc
    elif kosul=='Eğlendirici: ESFP-A / ESFP-T':
        sonuc="Karakter tipi: Eğlendirici:ESFP-A / ESFP-T"
        return sonuc
    
def function_character_kendinhazirla_ko():
    ko=entry_karakter_kendin_yap_ko.get()
    sonuc1="Karakter özellikleri: {}".format(ko)
    return sonuc1

def function_character_kendinhazirla_hobiler():
    hobiler=entry_karakter_kendin_yap_hastalık.get()
    sonuc="Hobiler: {}".format(hobiler)
    return sonuc

def function_character_kendinhazirla_fobiler():
    fobiler=entry_karakter_kendin_yap_fobiler.get()
    sonuc="Fobiler: {}".format(fobiler)
    return sonuc

def function_character_kendinhazirla_filmler():
    filmler=entry_karakter_kendin_yap_filmler.get()
    sonuc="Filmler: {}".format(filmler)
    return sonuc

def function_character_kendinhazirla_kitaplar():
    kitaplar=entry_karakter_kendin_yap_kitap.get()
    sonuc="Kitaplar: {}".format(kitaplar)
    return sonuc

def function_character_kendinhazirla_inanc():
    inanc=entry_karakter_kendin_yap_inanc.get()
    sonuc="İnanç: {}".format(inanc)
    return sonuc

def function_character_kendinhazirla_cy():
    kosul=combobox_veri_cekici_cy.get()
    if kosul=="Heteroseksüel":
        cy="Cinsel Yönelim: Heteroseksüel"
        return cy
    elif kosul=="Homoseksüel":
        cy="Cinsel Yönelim: Homoseksüel"
        return cy
    elif kosul=="Lezbiyen":
        cy="Cinsel Yönelim: Lezbiyen"
        return cy
    elif kosul=="Gey":
        cy="Cinsel Yönelim: Gey"
        return cy
    elif kosul=="Biseksüel":
        cy="Cinsel Yönelim: Biseksüel"
        return cy
    elif kosul=="Aseksüel":
        cy="Cinsel Yönelim: Aseksüel"
        return cy
    elif kosul=="Transgender":
        cy="Cinsel Yönelim: Transgender"
        return cy
    elif kosul=="Transseksüel":
        cy="Cinsel Yönelim: Transseksüel"
        return cy
    elif kosul=="Travesti":
        cy="Cinsel Yönelim: Travesti"
        return cy
    elif kosul=="Cross Dresser":
        cy="Cinsel Yönelim: Cross Dresser"
        return cy
    elif kosul=="Drag Queen":
        cy="Cinsel Yönelim: Drag Queen"
        return cy
    elif kosul=="İnterseksüel":
        cy="Cinsel Yönelim: İnterseksüel"
        return cy
    elif kosul=="Diğer":
        cy="Cinsel Yönelim: Diğer"
        return cy

def function_character_kendinhazirla_ky():
    kosul=combobox_veri_cekici_ky.get()
    if kosul=="Kuralcı iyi":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Kuralcı tarafsız":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Kuralcı kötü":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Dengesel iyi":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Dengeci nötr":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Dengesel kötü":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Kaotik iyi":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Kaotik tarafsız":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc
    elif kosul=="Kaotik kötü":
        sonuc="Karakter yönelimi: {}".format(kosul)
        return sonuc

def function_character_kendinhazirla_zeka():
    kosul=combobox_veri_cekici_zeka.get()
    if kosul=="Zeka geriliği":
        sonuc="Zeka: {}".format(kosul)
        return sonuc
    elif kosul=="Çok düşük":
        sonuc="Zeka: {}".format(kosul)
        return sonuc
    elif kosul=="Düşük":
        sonuc="Zeka: {}".format(kosul)
        return sonuc
    elif kosul=="Normal":
        sonuc="Zeka: {}".format(kosul)
        return sonuc
    elif kosul=="Zeki":
        sonuc="Zeka: {}".format(kosul)
        return sonuc
    elif kosul=="Çok zeki":
        sonuc="Zeka: {}".format(kosul)
        return sonuc
    elif kosul=="Dahi":
        sonuc="Zeka: {}".format(kosul)
        return sonuc





################################
"""
def on_entry_click_kilo(event):
    if entry_karakter_kendin_yap_kvb.get() == 'Kilo':
       entry_karakter_kendin_yap_kvb.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_kvb.insert(0, '') #Insert blank for user input

def on_focusout_kilo(event):
    if entry_karakter_kendin_yap_kvb.get() == '':
        entry_karakter_kendin_yap_kvb.insert(0, 'Kilo')
        entry_karakter_kendin_yap_kvb.config(fg = 'Black')

def on_entry_click_boy(event):
    if entry_karakter_kendin_yap_kvb_2.get() == 'Boy(cm)':
       entry_karakter_kendin_yap_kvb_2.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_kvb_2.insert(0, '') #Insert blank for user input

def on_focusout_boy(event):
    if entry_karakter_kendin_yap_kvb_2.get() == '':
        entry_karakter_kendin_yap_kvb_2.insert(0, 'Boy(cm)')
        entry_karakter_kendin_yap_kvb_2.config(fg = 'Black')

def on_entry_click_gun(event):
    if entry_karakter_kendin_yap_dogumtarihi.get() == 'Gün':
       entry_karakter_kendin_yap_dogumtarihi.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_dogumtarihi.insert(0, '') #Insert blank for user input

def on_focusout_gun(event):
    if entry_karakter_kendin_yap_dogumtarihi.get() == '':
        entry_karakter_kendin_yap_dogumtarihi.insert(0, 'Gün')
        entry_karakter_kendin_yap_dogumtarihi.config(fg = 'Black')

def on_entry_click_ay(event):
    if entry_karakter_kendin_yap_dogumtarihi_2.get() == 'Ay':
       entry_karakter_kendin_yap_dogumtarihi_2.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_dogumtarihi_2.insert(0, '') #Insert blank for user input

def on_focusout_ay(event):
    if entry_karakter_kendin_yap_dogumtarihi_2.get() == '':
        entry_karakter_kendin_yap_dogumtarihi_2.insert(0, 'Ay')
        entry_karakter_kendin_yap_dogumtarihi_2.config(fg = 'Black')

def on_entry_click_yil(event):
    if entry_karakter_kendin_yap_dogumtarihi_3.get() == 'Yıl':
       entry_karakter_kendin_yap_dogumtarihi_3.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_dogumtarihi_3.insert(0, '') #Insert blank for user input

def on_focusout_yil(event):
    if entry_karakter_kendin_yap_dogumtarihi_3.get() == '':
        entry_karakter_kendin_yap_dogumtarihi_3.insert(0, 'Yıl')
        entry_karakter_kendin_yap_dogumtarihi_3.config(fg = 'Black')

def on_entry_click_meslek(event):
    if entry_karakter_kendin_yap_meslek.get() == 'Meslek':
       entry_karakter_kendin_yap_meslek.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_meslek.insert(0, '') #Insert blank for user input

def on_focusout_meslek(event):
    if entry_karakter_kendin_yap_meslek.get() == '':
        entry_karakter_kendin_yap_meslek.insert(0, 'Meslek')
        entry_karakter_kendin_yap_meslek.config(fg = 'Black')

def on_entry_click_hastalık(event):
    if entry_karakter_kendin_yap_hastalık.get() == 'Hastalık':
       entry_karakter_kendin_yap_hastalık.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_hastalık.insert(0, '') #Insert blank for user input

def on_focusout_hastalık(event):
    if entry_karakter_kendin_yap_hastalık.get() == '':
        entry_karakter_kendin_yap_hastalık.insert(0, 'Hastalık')
        entry_karakter_kendin_yap_hastalık.config(fg = 'Black')

def on_entry_click_ko(event):
    if entry_karakter_kendin_yap_ko.get() == 'Örn: Şakacı, asabi...':
       entry_karakter_kendin_yap_ko.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_ko.insert(0, '') #Insert blank for user input

def on_focusout_ko(event):
    if entry_karakter_kendin_yap_ko.get() == '':
        entry_karakter_kendin_yap_ko.insert(0, 'Örn: Şakacı, asabi...')
        entry_karakter_kendin_yap_ko.config(fg = 'Black')

def on_entry_click_hobiler(event):
    if entry_karakter_kendin_yap_hobiler.get() == 'Hobiler':
       entry_karakter_kendin_yap_hobiler.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_hobiler.insert(0, '') #Insert blank for user input

def on_focusout_hobiler(event):
    if entry_karakter_kendin_yap_hobiler.get() == '':
        entry_karakter_kendin_yap_hobiler.insert(0, 'Hobiler')
        entry_karakter_kendin_yap_hobiler.config(fg = 'Black')

def on_entry_click_fobiler(event):
    if entry_karakter_kendin_yap_fobiler.get() == 'Fobiler':
       entry_karakter_kendin_yap_fobiler.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_fobiler.insert(0, '') #Insert blank for user input

def on_focusout_fobiler(event):
    if entry_karakter_kendin_yap_fobiler.get() == '':
        entry_karakter_kendin_yap_fobiler.insert(0, 'Fobiler')
        entry_karakter_kendin_yap_fobiler.config(fg = 'Black')

def on_entry_click_filmler(event):
    if entry_karakter_kendin_yap_filmler.get() == 'Filmler':
       entry_karakter_kendin_yap_filmler.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_filmler.insert(0, '') #Insert blank for user input

def on_focusout_filmler(event):
    if entry_karakter_kendin_yap_filmler.get() == '':
        entry_karakter_kendin_yap_filmler.insert(0, 'Filmler')
        entry_karakter_kendin_yap_filmler.config(fg = 'Black')

def on_entry_click_kitaplar(event):
    if entry_karakter_kendin_yap_kitap.get() == 'Kitaplar':
       entry_karakter_kendin_yap_kitap.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_kitap.insert(0, '') #Insert blank for user input

def on_focusout_kitaplar(event):
    if entry_karakter_kendin_yap_kitap.get() == '':
        entry_karakter_kendin_yap_kitap.insert(0, 'Kitaplar')
        entry_karakter_kendin_yap_kitap.config(fg = 'Black')

def on_entry_click_inanc(event):
    if entry_karakter_kendin_yap_inanc.get() == 'İnanç':
       entry_karakter_kendin_yap_inanc.delete(0, "end") # delete all the text in the entry
       entry_karakter_kendin_yap_inanc.insert(0, '') #Insert blank for user input

def on_focusout_inanc(event):
    if entry_karakter_kendin_yap_inanc.get() == '':
        entry_karakter_kendin_yap_inanc.insert(0, 'İnanç')
        entry_karakter_kendin_yap_inanc.config(fg = 'Black')

"""
#######################################







######################################################################################################################################################
"""İSİM TÜRETİCİ SEKMESİ OBJELERİ OLUŞTURULUYOR"""
######################################################################################################################################################
#kullanıcıdan input için label ekleniyor
label_name_generator1=ttk.Label(tab5,text="İsim Kaç Heceli Olsun?",style="BW.TLabel").place(x=10,y=20)
#isim:
label_name_generator2=ttk.Label(tab5,text="İsim:",style="BW.TLabel").place(x=10,y=70)
#Sonucu yazdıracağımız Labeli oluşturuyoruz
label_name_generator3=ttk.Label(tab5,text="",background=backround100,foreground="DarkOrange1",font=("Arial",12,"bold"))
#Sonucu yazdıracağımız label'i ekliyoruz
label_name_generator3.place(x=60,y=70)
#combobox seçimi için str oluşturulur
choice_name_generator=tk.StringVar()
#combobox alanı oluşturuyoruz
combobox_name_generator1=ttk.Combobox(tab5,textvariable=choice_name_generator,values=("İki Heceli","Üç Heceli","Dört Heceli","Beş Heceli","Rastgele"),state="readonly",width=10)
#combobox yerleştiriyoruz
combobox_name_generator1.place(x=245,y=22)

######################################################################################################################################################
"""KARAKTER TÜRETİCİ SEKMESİ OBJELERİ OLUŞTURULUYOR"""
######################################################################################################################################################

###################################### İ S İ M ########################################################
label_karakter_kendin_isim1=ttk.Label(tab10,text="İsim Kaç Heceli Olsun?",style="BW.TLabel").place(x=10,y=20)
combobox_veri_cekici_isim2=tk.StringVar()
combobox_karakter_kendin_yap_isim=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_isim2,values=("İki Heceli","Üç Heceli","Dört Heceli","Beş Heceli"),state="readonly",width=10)
combobox_karakter_kendin_yap_isim.place(x=240,y=20)

###################################### Y A Ş ##########################################################
label_karakter_kendin_yap_yas = ttk.Label(tab10, text="Yaş", style="BW.TLabel").place(x=10, y=60)
combobox_veri_cekici3= tk.StringVar()
combobox_karakter_kendin_yap_yas = ttk.Combobox(tab10, textvariable=combobox_veri_cekici3,values=("Genç","Orta yaşlı","Yaşlı","Rastgele"),state="readonly", width=10)
combobox_karakter_kendin_yap_yas.place(x=240, y=60)

###################################### D O Ğ U M     T A R İ H İ ######################################
label_karakter_kendin_yap_dog = ttk.Label(tab10, text="Gün-Ay-Yıl", style="BW.TLabel").place(x=530, y=20)

#Gün
entry_karakter_kendin_yap_dogumtarihi=tk.Entry(tab10,width=5,background=background102)
#entry_karakter_kendin_yap_dogumtarihi.insert(0, 'Gün')
#entry_karakter_kendin_yap_dogumtarihi.bind('<FocusIn>', on_entry_click_gun)
#entry_karakter_kendin_yap_dogumtarihi.bind('<FocusOut>', on_focusout_gun)
entry_karakter_kendin_yap_dogumtarihi.place(x=730,y=20)
#Ay
entry_karakter_kendin_yap_dogumtarihi_2=tk.Entry(tab10,width=5,background=background102)
#entry_karakter_kendin_yap_dogumtarihi_2.insert(0, 'Ay')
#entry_karakter_kendin_yap_dogumtarihi_2.bind('<FocusIn>', on_entry_click_ay)
#entry_karakter_kendin_yap_dogumtarihi_2.bind('<FocusOut>', on_focusout_ay)
entry_karakter_kendin_yap_dogumtarihi_2.place(x=785,y=20)
#Yıl
entry_karakter_kendin_yap_dogumtarihi_3=tk.Entry(tab10,width=6,background=background102)
#entry_karakter_kendin_yap_dogumtarihi_3.insert(0, 'Yıl')
#entry_karakter_kendin_yap_dogumtarihi_3.bind('<FocusIn>', on_entry_click_yil)
#entry_karakter_kendin_yap_dogumtarihi_3.bind('<FocusOut>', on_focusout_yil)
entry_karakter_kendin_yap_dogumtarihi_3.place(x=840,y=20)

###################################### C İ N S İ Y E T ######################################
label_karakter_kendin_yap_cinsiyet = ttk.Label(tab10, text="Cinsiyet", style="BW.TLabel").place(x=10, y=100)
combobox_veri_cekici4= tk.StringVar()
combobox_karakter_kendin_yap_cinsiyet = ttk.Combobox(tab10, textvariable=combobox_veri_cekici4,values=("Erkek","Kadın"),state="readonly", width=10)
combobox_karakter_kendin_yap_cinsiyet.place(x=240,y=100)

###################################### K İ L O - B O Y - S O N U Ç ######################################
#Birinci entry
label_karakter_kendin_yap_kvb=ttk.Label(tab10,text="Kilo-Boy",style="BW.TLabel").place(x=530, y=260)
entry_karakter_kendin_yap_kvb=tk.Entry(tab10,width=5,background=background102)
#entry_karakter_kendin_yap_kvb.insert(0, 'Kilo')
#entry_karakter_kendin_yap_kvb.bind('<FocusIn>', on_entry_click_kilo)
#entry_karakter_kendin_yap_kvb.bind('<FocusOut>', on_focusout_kilo)
entry_karakter_kendin_yap_kvb.place(x=730,y=260)
#İkinci entry
entry_karakter_kendin_yap_kvb_2=tk.Entry(tab10,width=7,background=background102)
#entry_karakter_kendin_yap_kvb_2.insert(0, 'Boy(cm)')
#entry_karakter_kendin_yap_kvb_2.bind('<FocusIn>', on_entry_click_boy)
#entry_karakter_kendin_yap_kvb_2.bind('<FocusOut>', on_focusout_boy)
entry_karakter_kendin_yap_kvb_2.place(x=780,y=260)

###################################### T E N ######################################
label_karakter_kendin_yap_ten=ttk.Label(tab10,text="Ten Rengi",style="BW.TLabel").place(x=10,y=380)
combobox_veri_cekici_ten=tk.StringVar()
combobox_karakter_kendin_yap_ten=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_ten,values=('Çok açık veya Beyaz cilt','Açık cilt veya Avrupalı','Orta açık/buğday cilt veya Güney Avrupalı','Orta koyu/esmer veya Akdenizli','Koyu cilt rengi veya kahverengi','Çok koyu cilt rengi veya siyahi tipi'),state="readonly",width=33)
combobox_karakter_kendin_yap_ten.place(x=150,y=380)

###################################### G Ö Z ######################################
label_karakter_kendin_yap_goz=ttk.Label(tab10,text="Göz Rengi",style="BW.TLabel").place(x=10,y=460)
combobox_veri_cekici_goz=tk.StringVar()
combobox_karakter_kendin_yap_goz=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_goz,values=('Açık kahverengi göz','Kahverengi göz','Koyu kahverengi göz / Siyah göz','Mavi göz','Yeşil göz','Ela göz','Kehribar göz','Gri göz'),state="readonly",width=25)
combobox_karakter_kendin_yap_goz.place(x=214,y=460)

###################################### B U R U N ######################################
label_karakter_kendin_yap_burun=ttk.Label(tab10,text="Burun Şekli",style="BW.TLabel").place(x=10,y=500)
combobox_veri_cekici_burun=tk.StringVar()
combobox_karakter_kendin_yap_burun=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_burun,values=("Kemerli burun","Ucu düşük burun","Ucu geniş burun","Ucu dar burun","Ucu sivri uzun burun","Ucu kalkık kısa burun","Eğri burun","Sivri burun","Burun tabanı geniş","Geniş burun","Dar burun","Semer burun"),state="readonly",width=20)
combobox_karakter_kendin_yap_burun.place(x=254,y=500)

###################################### S A Ç ######################################

#renk
label_karakter_kendin_yap_sacrengi=ttk.Label(tab10,text="Saç Rengi",style="BW.TLabel").place(x=10,y=180)
combobox_veri_cekici_sacrengi=tk.StringVar()
combobox_karakter_kendin_yap_sacrengi=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_sacrengi,values=("Siyah","Koyu kahve","Kahverengi","Açık kahve","Koyu sarı","Sarı","Açık sarı","Bakır","Turuncu","Kumral"),state="readonly",width=10)
combobox_karakter_kendin_yap_sacrengi.place(x=240,y=180)
#şekil
label_karakter_kendin_yap_sacsekli=ttk.Label(tab10,text="Saç Şekli",style="BW.TLabel").place(x=12,y=220)
combobox_veri_cekici_sacsekli=tk.StringVar()
combobox_karakter_kendin_yap_sacsekli=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_sacsekli,values=("Düz","Kıvırcık","Dalgalı"),state="readonly",width=6)
combobox_karakter_kendin_yap_sacsekli.place(x=240,y=220)
#tip
label_karakter_kendin_yap_sactipi=ttk.Label(tab10,text="Saç Tipi",style="BW.TLabel").place(x=10,y=260)
combobox_veri_cekici_sactipi=tk.StringVar()
combobox_karakter_kendin_yap_sactipi=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_sactipi,values=("İnce telli","Normal","Kalın telli"),state="readonly",width=8)
combobox_karakter_kendin_yap_sactipi.place(x=240,y=260)
#uzunluk
label_karakter_kendin_yap_sacuzunluk=ttk.Label(tab10,text="Saç Uzunluğu",style="BW.TLabel").place(x=10,y=300)
combobox_veri_cekici_sacuzunluk=tk.StringVar()
combobox_karakter_kendin_yap_sacuzunluk=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_sacuzunluk,values=("Kısa saç","Uzun saç"),state="readonly",width=8)
combobox_karakter_kendin_yap_sacuzunluk.place(x=240,y=300)

###################################### M E S L E K ######################################
label_karakter_kendin_yap_meslek=ttk.Label(tab10,text="Meslek",style="BW.TLabel").place(x=530,y=300)
entry_karakter_kendin_yap_meslek=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_meslek.insert(0, 'Meslek')
#entry_karakter_kendin_yap_meslek.bind('<FocusIn>', on_entry_click_meslek)
#entry_karakter_kendin_yap_meslek.bind('<FocusOut>', on_focusout_meslek)
entry_karakter_kendin_yap_meslek.place(x=730,y=300)

###################################### Z E N G İ N L İ K ######################################
label_karakter_kendin_yap_servet=ttk.Label(tab10,text="Servet",style="BW.TLabel").place(x=10,y=140)
combobox_veri_cekici_servet=tk.StringVar()
combobox_karakter_kendin_yap_servet=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_servet,values=("Fakir","Çok fakir","Açlık sınırında","Orta halli","Zengin","Çok zengin"),state="readonly",width=10)
combobox_karakter_kendin_yap_servet.place(x=240,y=140)

###################################### H A S T A L I K ######################################
label_karakter_kendin_yap_hastalık=ttk.Label(tab10,text="Hastalık",style="BW.TLabel").place(x=530,y=340)
entry_karakter_kendin_yap_hastalık=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_hastalık.insert(0, 'Hastalık')
#entry_karakter_kendin_yap_hastalık.bind('<FocusIn>', on_entry_click_hastalık)
#entry_karakter_kendin_yap_hastalık.bind('<FocusOut>', on_focusout_hastalık)
entry_karakter_kendin_yap_hastalık.place(x=730,y=340)

###################################### K A R A K T E R      T İ P İ ######################################
label_karakter_kendin_yap_kartipi=ttk.Label(tab10,text="Karakter Tipi",style="BW.TLabel").place(x=10,y=420)
combobox_veri_cekici_kartipi=tk.StringVar()
combobox_karakter_kendin_yap_kartipi=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_kartipi,values=(
        'Mimar: INTJ-A / INTJ-T','Mantıkçı: INTP-A / INTP-T','Buyurucu: ENTJ-A / ENTJ-T','Tartışmacı: ENTP-A / ENTP-T',
        'Savunucu: INFJ-A / INFJ-T','Arabulucu: INFP-A / INFP-T','Önder: ENFJ-A / ENFJ-T','Kampanyacı: ENFP-A / ENFP-T',
        'Lojistikçi: ISTJ-A / ISTJ-T','Savunmacı: ISFJ-A / ISFJ-T','Yönetici: ESTJ-A / ESTJ-T','Konsül: ESFJ-A / ESFJ-T',
        'Becerikli: ISTP-A / ISTP-T','Maceracı: ISFP-A / ISFP-T','Girişimci: ESTP-A / ESTP-T','Eğlendirici: ESFP-A / ESFP-T'),state="readonly",width=26)
combobox_karakter_kendin_yap_kartipi.place(x=206,y=420)

###################################### K A R A K T E R      Ö Z E L L İ K L E R İ ######################################
label_karakter_kendin_yap_ko=ttk.Label(tab10,text="Karakter Özellikleri",style="BW.TLabel").place(x=530,y=380)
entry_karakter_kendin_yap_ko=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_ko.insert(0, 'Örn: Şakacı, asabi...')
#entry_karakter_kendin_yap_ko.bind('<FocusIn>', on_entry_click_ko)
#entry_karakter_kendin_yap_ko.bind('<FocusOut>', on_focusout_ko)
entry_karakter_kendin_yap_ko.place(x=730,y=380)

###################################### H O B İ L E R ######################################
label_karakter_kendin_yap_hobiler=ttk.Label(tab10,text="Hobiler",style="BW.TLabel").place(x=530,y=60)
entry_karakter_kendin_yap_hobiler=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_hobiler.insert(0, 'Hobiler')
#entry_karakter_kendin_yap_hobiler.bind('<FocusIn>', on_entry_click_hobiler)
#entry_karakter_kendin_yap_hobiler.bind('<FocusOut>', on_focusout_hobiler)
entry_karakter_kendin_yap_hobiler.place(x=730,y=60)

###################################### F O B İ L E R ######################################
label_karakter_kendin_yap_fobiler=ttk.Label(tab10,text="Fobiler",style="BW.TLabel").place(x=530,y=100)
entry_karakter_kendin_yap_fobiler=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_fobiler.insert(0, 'Fobiler')
#entry_karakter_kendin_yap_fobiler.bind('<FocusIn>', on_entry_click_fobiler)
#entry_karakter_kendin_yap_fobiler.bind('<FocusOut>', on_focusout_fobiler)
entry_karakter_kendin_yap_fobiler.place(x=730,y=100)

###################################### F İ L M L E R ######################################
label_karakter_kendin_yap_filmler=ttk.Label(tab10,text="Filmler",style="BW.TLabel").place(x=530,y=140)
entry_karakter_kendin_yap_filmler=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_filmler.insert(0, 'Filmler')
#entry_karakter_kendin_yap_filmler.bind('<FocusIn>', on_entry_click_filmler)
#entry_karakter_kendin_yap_filmler.bind('<FocusOut>', on_focusout_filmler)
entry_karakter_kendin_yap_filmler.place(x=730,y=140)

###################################### K İ T A P ######################################
label_karakter_kendin_yap_kitap=ttk.Label(tab10,text="Sevilen Kitaplar",style="BW.TLabel").place(x=530,y=180)
entry_karakter_kendin_yap_kitap=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_kitap.insert(0, 'Kitaplar')
#entry_karakter_kendin_yap_kitap.bind('<FocusIn>', on_entry_click_kitaplar)
#entry_karakter_kendin_yap_kitap.bind('<FocusOut>', on_focusout_kitaplar)
entry_karakter_kendin_yap_kitap.place(x=730,y=180)

###################################### İ N A N Ç ######################################
label_karakter_kendin_yap_inanc=ttk.Label(tab10,text="İnanç",style="BW.TLabel").place(x=530,y=220)
entry_karakter_kendin_yap_inanc=tk.Entry(tab10,width=20,background=background102)
#entry_karakter_kendin_yap_inanc.insert(0, 'İnanç')
#entry_karakter_kendin_yap_inanc.bind('<FocusIn>', on_entry_click_inanc)
#entry_karakter_kendin_yap_inanc.bind('<FocusOut>', on_focusout_inanc)
entry_karakter_kendin_yap_inanc.place(x=730,y=220)

###################################### C İ N S E L      Y Ö N E L İ M ######################################
label_karakter_kendin_yap_cy=ttk.Label(tab10,text="Cinsel Yönelim",style="BW.TLabel").place(x=10,y=540)
combobox_veri_cekici_cy=tk.StringVar()
combobox_veri_cekici_cy=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_cy,values=(cinselyonelim),state="readonly",width=15)
combobox_veri_cekici_cy.place(x=294,y=540)

###################################### K A R A K T E R      Y Ö N E L İ M İ ######################################
label_karakter_kendin_yap_ky=ttk.Label(tab10,text="Karakter Yönelimi",style="BW.TLabel").place(x=10,y=580)
combobox_veri_cekici_ky=tk.StringVar()
combobox_veri_cekici_ky=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_ky,values=(karakteryonelimi),state="readonly",width=12)
combobox_veri_cekici_ky.place(x=319,y=580)
###################################### Z E K A ######################################
label_karakter_kendin_yap_zeka=ttk.Label(tab10,text="Zeka",style="BW.TLabel").place(x=10,y=620)
combobox_veri_cekici_zeka=tk.StringVar()
combobox_veri_cekici_zeka=ttk.Combobox(tab10,textvariable=combobox_veri_cekici_zeka,values=("Zeka geriliği","Çok düşük","Düşük","Normal","Zeki","Çok zeki","Dahi"),state="readonly",width=10)
combobox_veri_cekici_zeka.place(x=335,y=620)


######################          ? BUTONU BİLGİLERİ          #############################
def veritabani_hobiler():
    pencere=tk.Tk() #anapencere objesi oluştu
    pencere.geometry("800x400") #anapencerenin boyutları
    pencere.title("Hobiler")
    textbox=tk.Text(pencere,width=100,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    for i in hobiler:
        a=i+"\n"
        textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

def veritabani_fobiler():
    pencere=tk.Tk() #anapencere objesi oluştu
    pencere.geometry("800x400") #anapencerenin boyutları
    pencere.title("Fobiler")
    textbox=tk.Text(pencere,width=100,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    for i in fobiler:
        a=i+"\n"
        textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

def veritabani_filmler():
    pencere=tk.Tk() #anapencere objesi oluştu
    pencere.geometry("800x400") #anapencerenin boyutları
    pencere.title("Filmler")
    textbox=tk.Text(pencere,width=100,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    for i in en_sevilen_filmler:
        a=i+"\n"
        textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

def veritabani_kitaplar():
    pencere=tk.Tk() #anapencere objesi oluştu
    pencere.geometry("800x400") #anapencerenin boyutları
    pencere.title("Kitaplar")
    textbox=tk.Text(pencere,width=100,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    for i in en_sevilen_kitaplar:
        a=i+"\n"
        textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

def veritabani_meslek():
    pencere=tk.Tk() #anapencere objesi oluştu
    pencere.geometry("800x400") #anapencerenin boyutları
    pencere.title("Meslekler")
    textbox=tk.Text(pencere,width=100,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    for i in meslekler:
        a=i+"\n"
        textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

def veritabani_hastalik():
    pencere=tk.Tk() #anapencere objesi oluştu
    pencere.geometry("800x400") #anapencerenin boyutları
    pencere.title("Hastalıklar")
    textbox=tk.Text(pencere,width=100,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    for i in hastaliklar:
        a=i+"\n"
        textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

def veritabani_karakteryonelimi():
    pencere=tk.Tk() 
    pencere.geometry("600x400") 
    pencere.title("Karakter Yönelimi")
    textbox=tk.Text(pencere,width=200,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    a=karakteryonelimi_aciklama
    textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

def veritabani_karaktertipi():
    pencere=tk.Tk() 
    pencere.geometry("600x400") 
    pencere.title("Karakter Tipi")
    textbox=tk.Text(pencere,width=300,height=50)
    scrollbar=tk.Scrollbar(pencere)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    textbox.pack(side=tk.LEFT, fill=tk.Y)
    scrollbar.config(command=textbox.yview)
    textbox.config(yscrollcommand=scrollbar.set)
    a=karaktertipi
    textbox.insert(tk.END,a)
    textbox.configure(state="disabled")

#############################   KARAKTER TÜRETİCİ / KENDİN OLUŞTUR/ RASTGELE COMBOBOX SEÇİM     ##################################


def function_rastgelesecim_buton():
    #Tüm entry'leri temizledikten sonra çalıştır
    #yaş
    entry_karakter_kendin_yap_dogumtarihi.delete(0, "end") # delete all the text in the entry
    entry_karakter_kendin_yap_dogumtarihi_2.delete(0, "end") # delete all the text in the entry
    entry_karakter_kendin_yap_dogumtarihi_3.delete(0, "end") # delete all the text in the entry
    #hobiler
    entry_karakter_kendin_yap_hobiler.delete(0, "end") # delete all the text in the entry
    #fobiler
    entry_karakter_kendin_yap_fobiler.delete(0, "end") # delete all the text in the entry
    #filmler
    entry_karakter_kendin_yap_filmler.delete(0, "end") # delete all the text in the entry
    #kitaplar
    entry_karakter_kendin_yap_kitap.delete(0, "end") # delete all the text in the entry
    #inanç
    entry_karakter_kendin_yap_inanc.delete(0, "end") # delete all the text in the entry
    #kilo boy
    entry_karakter_kendin_yap_kvb.delete(0, "end") # delete all the text in the entry
    entry_karakter_kendin_yap_kvb_2.delete(0, "end") # delete all the text in the entry
    #meslek
    entry_karakter_kendin_yap_meslek.delete(0,"end")
    #hastalık
    entry_karakter_kendin_yap_hastalık.delete(0,"end")
    #karakter özellikleri
    entry_karakter_kendin_yap_ko.delete(0,"end")





    #isim
    a1=random.randint(0,3)
    combobox_karakter_kendin_yap_isim.current(a1)
    #yaş
    a1=random.randint(0,3)
    combobox_karakter_kendin_yap_yas.current(a1)
    #cinsiyet
    a1=random.randint(0,1)
    combobox_karakter_kendin_yap_cinsiyet.current(a1)
    #servet
    a1=random.randint(0,5)
    combobox_karakter_kendin_yap_servet.current(a1)
    #sac rengi
    a1=random.randint(0,9)
    combobox_karakter_kendin_yap_sacrengi.current(a1)
    #sac sekli
    a1=random.randint(0,2)
    combobox_karakter_kendin_yap_sacsekli.current(a1)
    #sac tipi
    a1=random.randint(0,2)
    combobox_karakter_kendin_yap_sactipi.current(a1)
    #sac uzunluğu
    a1=random.randint(0,1)
    combobox_karakter_kendin_yap_sacuzunluk.current(a1)
    #ten
    a1=random.randint(0,5)
    combobox_karakter_kendin_yap_ten.current(a1)
    #karakter tipi
    a1=random.randint(0,15)
    combobox_karakter_kendin_yap_kartipi.current(a1)
    #göz
    a1=random.randint(0,7)
    combobox_karakter_kendin_yap_goz.current(a1)
    #burun
    a1=random.randint(0,11)
    combobox_karakter_kendin_yap_burun.current(a1)
    #cinsel yönelim
    a1=random.randint(0,12)
    combobox_veri_cekici_cy.current(a1)
    #karakter yönelimi
    a1=random.randint(0,8)
    combobox_veri_cekici_ky.current(a1)
    #zeka
    a1=random.randint(0,6)
    combobox_veri_cekici_zeka.current(a1)
    #yaş
    a1=random.randint(1,28)
    a2=random.randint(1,12)
    a3=random.randint(1800,2100)
    entry_karakter_kendin_yap_dogumtarihi.insert(0,a1)
    entry_karakter_kendin_yap_dogumtarihi_2.insert(0,a2)
    entry_karakter_kendin_yap_dogumtarihi_3.insert(0,a3)
    #hobiler
    a1=random.randint(0,2)
    if a1==0:
        entry_karakter_kendin_yap_hobiler.insert(0,"Hobi yok")
    elif a1==1:
        b=random.choice(hobiler)
        entry_karakter_kendin_yap_hobiler.insert(0,b)
    elif a1==2:
        b=random.choice(hobiler)
        c=random.choice(hobiler)
        entry_karakter_kendin_yap_hobiler.insert(0,b)
        entry_karakter_kendin_yap_hobiler.insert(0,",")
        entry_karakter_kendin_yap_hobiler.insert(0,c)
    #fobiler
    a1=random.randint(0,2)
    if a1==0:
        entry_karakter_kendin_yap_fobiler.insert(0,"Fobi yok")
    elif a1==1:
        b=random.choice(fobiler)
        entry_karakter_kendin_yap_fobiler.insert(0,b)
    elif a1==2:
        b=random.choice(fobiler)
        c=random.choice(fobiler)
        entry_karakter_kendin_yap_fobiler.insert(0,b)
        entry_karakter_kendin_yap_fobiler.insert(0,",")
        entry_karakter_kendin_yap_fobiler.insert(0,c)
    #filmler
    a1=random.randint(0,2)
    if a1==0:
        entry_karakter_kendin_yap_filmler.insert(0,"Sevilen film yok")
    elif a1==1:
        b=random.choice(en_sevilen_filmler)
        entry_karakter_kendin_yap_filmler.insert(0,b)
    elif a1==2:
        b=random.choice(en_sevilen_filmler)
        c=random.choice(en_sevilen_filmler)
        entry_karakter_kendin_yap_filmler.insert(0,b)
        entry_karakter_kendin_yap_filmler.insert(0,",")
        entry_karakter_kendin_yap_filmler.insert(0,c)
    #kitaplar
    a1=random.randint(0,2)
    if a1==0:
        entry_karakter_kendin_yap_kitap.insert(0,"Sevilen kitap yok")
    elif a1==1:
        b=random.choice(en_sevilen_kitaplar)
        entry_karakter_kendin_yap_kitap.insert(0,b)
    elif a1==2:
        b=random.choice(en_sevilen_kitaplar)
        c=random.choice(en_sevilen_kitaplar)
        entry_karakter_kendin_yap_kitap.insert(0,b)
        entry_karakter_kendin_yap_kitap.insert(0,",")
        entry_karakter_kendin_yap_kitap.insert(0,c)
    #inanç
    a1=random.randint(0,2)
    if a1==0:
        entry_karakter_kendin_yap_inanc.insert(0,"Belirsiz")
    elif a1==1:
        b=random.choice(inanclar)
        entry_karakter_kendin_yap_inanc.insert(0,b)
    #kilo-boy
    a=random.randint(40,110)
    b=(random.randint(140,200))/100
    entry_karakter_kendin_yap_kvb.insert(0,a)
    entry_karakter_kendin_yap_kvb_2.insert(0,b)
    #meslek
    a=random.choice(meslekler)
    entry_karakter_kendin_yap_meslek.insert(0,a)
    #hastalık
    a1=random.randint(0,2)
    if a1==0:
        entry_karakter_kendin_yap_hastalık.insert(0,"Hastalık yok")
    elif a1==1:
        b=random.choice(hastaliklar)
        entry_karakter_kendin_yap_hastalık.insert(0,b)
    elif a1==2:
        b=random.choice(hastaliklar)
        c=random.choice(hastaliklar)
        entry_karakter_kendin_yap_hastalık.insert(0,b)
        entry_karakter_kendin_yap_hastalık.insert(0,",")
        entry_karakter_kendin_yap_hastalık.insert(0,c)
    #karakter özellikleri
    entry_karakter_kendin_yap_ko.insert(0,"Lütfen siz belirtin")



######################################################################################################################################################
"""BUTONLAR OLUŞTURULUYOR"""
######################################################################################################################################################
buton_name_generator5=tk.Button(tab5,text="Türet",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=function_name_checkbox_generator).place(x=10,y=105)
buton_name_generator5_1=tk.Button(tab5,text="Türet ve Yazdır(Not Defteri)",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=print_notepad).place(x=10,y=150)
#buton_name_generator3=tk.Button(tab5,text="Türet ve Yazdır(Excel)",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=3,font=("Arial",11,"bold"),height=1,width=30,command=print_excel).place(x=10,y=185)

###################################### KARAKTER     YARATMA     H I Z L I       O L U Ş T U R ######################################
buton_character_generator_1=tk.Button(tab9,text="Türet ve Yazdır(Not Defteri)",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=8,font=("Arial",11,"bold"),height=3,width=32,command=print_notepad_character).place(x=10,y=20)

###################################### KARAKTER YARATMA     K E N D İ N      Y A P ######################################
buton_karakter_kendin_yap1=tk.Button(tab10,text="Yazdır(Not Defteri)",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=5,font=("Arial",11,"bold"),height=2,width=32,command=turet_ve_yazdir).place(x=530,y=450)
buton_karakter_kendin_yap2=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_hobiler).place(x=910,y=58) #Hobiler
buton_karakter_kendin_yap3=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_fobiler).place(x=910,y=98) #Fobiler
buton_karakter_kendin_yap4=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_filmler).place(x=910,y=138) #Filmler
buton_karakter_kendin_yap5=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_kitaplar).place(x=910,y=178) #Sevilen kitaplar
buton_karakter_kendin_yap6=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_meslek).place(x=910,y=298) #meslek
buton_karakter_kendin_yap7=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_hastalik).place(x=910,y=338) #hastalık
buton_karakter_kendin_yap8=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_karakteryonelimi).place(x=455,y=578)
buton_karakter_kendin_yap9=tk.Button(tab10,text="?",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=1,font=("Arial",9,"bold"),height=1,width=5,command=veritabani_karaktertipi).place(x=455,y=418)
deneme_buton=tk.Button(tab10,text="Rastgele Seçim",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=5,font=("Arial",11,"bold"),height=2,width=32,command=function_rastgelesecim_buton).place(x=530,y=520)

##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

"""

                                        Ü   L   K   E       T   Ü   R   E   T   İ   C   İ

"""
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################

veritabanı_ulke_karaparcasi=["Tam kara","Ada","Yarımada"]

veritabani_ulke_sıcakiklimler=["Ekvatoral iklim", "Tropikal iklim", "Muson iklimi", "Çöl iklimi"]
veritabani_ulke_ılımaniklimler=["Akdeniz iklim", "Okyanusal iklim", "Karasal iklim", "Step iklim"]
veritabani_ulke_sogukiklimler=["Tundra iklimi", "Kutup iklimi"]

veritabani_ulke_ekvatoraliklim="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 25 C
\tYıllık ortalama yağış miktarı : 2000+ mm            
\tBitki örtüsü : Gür ve geniş yapraklı orma                             
\tToprak yapısı: Laterit"""
veritabani_ulke_tropikaliklim="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 20 C
\tYıllık ortalama yağış miktarı : 1000-2000 mm              
\tBitki örtüsü : Gür ve uzun boylu otlardan oluşan savanlar                           
\tToprak yapısı: Laterit"""
veritabani_ulke_musoniklimi="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 15-22 C
\tYıllık ortalama yağış miktarı : 2000 mm           
\tBitki örtüsü : Geniş yapraklı muson ormanları ile uzun boylu ot toplulukları                            
\tToprak yapısı: Kahverengi orman toprağı"""
veritabani_ulke_coliklimi="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 30+ C
\tYıllık ortalama yağış miktarı : 100- mm              
\tBitki örtüsü : Kurakçıl otlar ve kaktüsler                             
\tToprak yapısı: Çöl Toprakları"""
veritabani_ulke_akdeniziklimi="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 15-20 C
\tYıllık ortalama yağış miktarı : 600-1000 mm               
\tBitki örtüsü : Maki                              
\tToprak yapısı: Terra Rossa (Kırmızı) Toprakları"""
veritabani_ulke_okyanusaliklim="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 14-15 C
\tYıllık ortalama yağış miktarı : 1000-1500 mm                
\tBitki örtüsü : Alçak alanlarda geniş yapraklı orman, yüksek alanlarda ise iğne yapraklı ormanlar                                
\tToprak yapısı: Kahverengi Orman Toprağı"""
veritabani_ulke_karasaliklim="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 0-10 C
\tYıllık ortalama yağış miktarı : 400-600 mm              
\tBitki örtüsü : Tayga ormanları                              
\tToprak yapısı: Podzol Topraklar"""
veritabani_ulke_stepiklimi="""*****İKLİM*****
\tYıllık ortamala sıcaklık : 15 C
\tYıllık ortalama yağış miktarı : 300-500 mm
\tBitki örtüsü : Bozkır                      
\tToprak yapısı: Çernezyom (Kara) Topraklar"""
veritabani_ulke_tundraiklimi="""*****İKLİM*****
\tSıcaklık : Kışın -30 ile -40 C, yazın 10 C
\tYıllık ortalama yağış miktarı : 200-250 mm       
\tBitki örtüsü : Çalı, yosun                      
\tToprak yapısı: Tundra toprakları"""
veritabani_ulke_kutupiklimi="""*****İKLİM*****
\tYıllık ortamala sıcaklık : -40
\tYıllık ortalama yağış miktarı : 200 mm       
\tBitki örtüsü : Yok
\tToprak yapısı: Tundra toprakları"""
veritabani_ulke_federasyon=["Federal","Üniter"]
veritabani_ulke_yonetimbicimi=['Cumhuriyet', 'Demokrasi','Meşrutiyet', 'Monarşi','Oligarşi', 'Otokrasi','Plütokrasi','Teknokrasi', 'Teokrasi', 'Totalitarizm']
veritabani_ulke_baslica_ihracatveithalatkalemleri=['Mineral yakıt', 'Başlıca ihracat kalemleri', 'Steyşın vagonlar', '', 'İlaç ve farmakoloji ürünleri', 'Makine ve ulaşım araçları', 'Otomobil ve motorlu araç aksesuarları', 'Kimyevi ürünler', 'Tütün', 'Vinil polimerleri', 'Motorlu taşıtların aksam ve parçaları ile şase ve karoserleri.', 'Otomatik bilgi işlem makineleri', 'Değerli metaller ve doğal gaz', 'Asfalt', 'Kauçuk ve mamulleri', 'Eczacılık ve eczacılık ürünleri', 'Otomobil', 'Elmaslar', 'Parça ve aksesuarlar', 'Motorlar ve aksamı', 'İlaç ve farmakolojik ürünler', 'Ham petrol', 'Petrol yağları ve bitümenli minerallerden elde edilen yağlar', 'Tekstil elyafı ve mamulleri', 'Diğer adi metallerden eşya (kilit, zincir, yay, fermuar, dikiş, nakış aletleri vb.) ', 'Meyve ve sebzeler', 'Metallerden nihai ürünler', 'Kara ulaşım araçları', 'Metal ve metal cevheri', 'Kaolin', 'Silikonlar', 'Telefon cihazları', 'Matbaacılığa mahsus baskı makineleri', 'Kimyasal ürünler', 'Maden ürünleri', 'Tekstil', 'Makine ve ekipman', 'Enerji üreten makine ve cihazlar', 'Gıda', 'Plastik ve plastikten mamul eşya', 'Tıp, cerrahi, dişçilik ve veterinerlik alet ve cihazları.', 'Giyim eşyası ve aksesuarları', 'Tedavide/korunmada kullanılmak üzere hazırlanan ilaçlar (dozlandırılmış); ', 'Yarış arabaları', 'Binek otomobiller', 'Ilaçlar', 'Petrol gazları ve diğer gazlı hidrokarbonlar', 'Eczacılık ürünleri ve organik kimyasal ürünler', 'Sebze-meyve', 'Petrol yağları ve bitümenli minarallerden elde edilen yağlar ve ilaçlar', 'Motorların aksam parçaları', 'Karayolu taşıtları için aksam', 'Metaller', 'Tekstil ürünleri', 'Petrol yağları', 'Ulaşım araçları', 'Elektrikli makine ve cihazlar', 'Mineral yakıt ve yağlar', 'Paslanmaz çelikten yassı hadde mamülü', 'Sanayi kollarında kullanılan makine ve cihazlar', 'Motorlu yolcu taşıtları', 'Haberleşme cihazları', 'Gıda ürünleri', 'Gübre ve plastik materyaller', 'Inorganik madde sıvanmış kağıtlar', 'Ayakkabı', 'Makineler ve aksamı', 'Rafine petrolden elde edilen ürünler', 'Demir-çelik']
veritabani_ulke_baslica_ihracveithalurunler=['Oyuncaklar', 'Helikopterler', 'Tabii borat cevherleri', 'Bor ve diğer metal cevherleri', 'Karayolu taşıtları için aksam ve parçalar, eşya taşımaya mahsus motorlu taşıtlar', 'Alüminyum', 'Siklik hidrokarbonlar', 'Deniz ürünleri', 'Üzüm', 'Krom', 'Petrol yağları ve bitümenli minerallerden elde edilen yağlar', 'Taşıt aksam ve parçaları', 'Demir-çelik', 'Led ve oled gösterge panelleri/ekranlar', 'Giyim eşyaları', 'Ses-görüntü ve diğer bilgileri almaya', 'Konfeksiyon', 'Lcd', 'Otomatik bilgi işlem makinaları ve üniteleri', 'Dizel/yarı dizel taşıtlar', 'Tekstil', 'Otomobiller', 'Kauçuktan yeni dış lastikler', 'Kayısı', 'Mineral yakıtlar-yağlar', 'Plastik mamulleri', 'Eşya taşımaya mahsus motorlu taşıtlar', 'Demir veya alaşımsız çelikten yassı hadde ürünleri', 'Sıvılaştırılmış hidrokarbon gazı (lastik hammaddesi)', 'Propilen ve diğer olefinlerin polimerleri', 'Yaş meyve ve sebze', 'Buğday', 'Eczacılık ürünleri', 'Bilgisayar çipleri', 'Uzay araçları (uydular dahil)', 'Kokluk taşkömürü', 'Balıkçılık ürünleri', 'Makarna', 'Elektrikli makine ve cihazlar', 'Dericilik ürünleri', 'Demir veya alaşımsız çelikten profiller', 'Çinko', 'Işlenmemiş çinko', 'Taşıt aksamları', 'Kauçuk ve kauçuktan eşya ile dokumaya elverişli suni ve sentetik lifler', 'Baharatlar', 'Bakır', 'Yük/insan taşıma amaçlı gemiler', 'Petrol yağları ve bitümenli minerallerden elde edilmiş yağlar', 'Meyve suyu', 'Elektronik cihazlar', 'Ilaç', 'Rafine edilmiş bakır ve bakır alaşımları', 'Metallerden nihai ürünler ve ayakkabı', 'Optik alet ve cihazlar', 'Ayçiçek', 'Altın', 'Beyaz eşya', 'Değişik sanayi kollarında kullanılan makine ve cihazlar', 'Otomotiv parçaları', 'Tekstil ve hazır giyim ürünleri', 'Fındık', 'Aspir ve pamuk tohumu yağları', 'Şekerlemeler', 'Kazan', 'Demiryolu taşıtları ile aksam ve parçaları', 'Otomotiv ürünleri', 'Gemiler', 'Mermer ve traverten', 'Çevirmeye ve vermeye yarayan araçlar', 'Cep telefonları', 'Kurşun', 'Hücresel/diğer kablosuz ağlar için telefonlar', 'Uçaklar', 'Canlı büyükbaş hayvanlar (at, eşek, katır ve bardolar hariç)', 'Sığır', 'Makine ve mekanik cihazlar', 'Bor oksitleri ve borik asitler', 'Demir', 'Makine ve cihazlar', 'Taşkömürü', 'Karayolu taşıtları için aksam ve parçalar']

veritabani_gelismislikduzeyi=["Çok kötü","Kötü","Gelişmekte","İyi","Çok iyi"]
veritabani_ulke_zenginlik=["Çok kötü","Kötü","Gelişmekte","İyi","Çok iyi"]
veritabani_ulke_nufustaagırlık=["Genç","Yaşlı","Çocuk"]
veritabani_ulke_kalabalıklık=["Çok az","Az","Orta","Kalabalık","Çok kalabalık"]
veritabani_ulke_sosyaldevlet=["Çok az","Az","Dengeli","Çok","Çok fazla"]

veritabani_ulke_orduharcamaları=["Çok az","Az","Orta","Fazla","Çok fazla"]
veritabani_ulke_ordutipleri=["Kara kuvvetleri","Deniz kuvvetleri","Hava kuvvetleri"]

"""
Siyasi-Ekonomi-Kalkınma: S
Coğrafi-Nüfus-Eğitim Özellik: C
Askeri: A
Fonksiyonel: F
"""
################################################################################################################################################################
################################################################################################################################################################
"""SİYASİ-EKONOMİ*KALKINMA"""
################################################################################################################################################################
################################################################################################################################################################

###################################### E K O N O M İ K       S İ S T E M ######################################
ulke_label_piyasaserbestisi=ttk.Label(tab7,text="Ekonomik Sistem",style="BW.TLabel").place(x=10,y=20)
ulke_combobox_vericekici_piyasaserbestligi=tk.StringVar()
ulke_combobox_piyasaserbestligi=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_piyasaserbestligi,values=("Neo-Liberalizm","Kapitalizm","Emperyalizm","Sosyalizm","Komünizm","Muller Ekonomisi"),state="readonly",width=16)
ulke_combobox_piyasaserbestligi.place(x=240,y=20)
###################################### R E F A H ######################################
ulke_label_refah=ttk.Label(tab7,text="Kalkınma Düzeyi/Refah",style="BW.TLabel").place(x=10,y=60)
ulke_combobox_vericekici_refah=tk.StringVar()
ulke_combobox_refah=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_refah,values=("Halk açlık sınırında","Yetersiz","Orta Düzey","Çok iyi"),state="readonly",width=16)
ulke_combobox_refah.place(x=240,y=60)
###################################### Y Ö N E T İ M ######################################
ulke_label_yonetim=ttk.Label(tab7,text="Yönetim",style="BW.TLabel").place(x=10,y=100)
ulke_combobox_vericekici_yonetim=tk.StringVar()
ulke_combobox_yonetim=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_yonetim,values=(veritabani_ulke_yonetimbicimi),state="readonly",width=14)
ulke_combobox_yonetim.place(x=240,y=100)
###################################### F E D E R A S Y O N ######################################
ulke_label_federasyon=ttk.Label(tab7,text="Federasyon",style="BW.TLabel").place(x=10,y=140)
ulke_combobox_vericekici_federasyon=tk.StringVar()
ulke_combobox_federasyon=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_federasyon,values=("Üniter Devlet","Federal Devlet"),state="readonly",width=14)
ulke_combobox_federasyon.place(x=240,y=140)
###################################### G E L İ Ş M İ Ş L İ K ######################################
ulke_label_gelismislik=ttk.Label(tab7,text="Gelişmişlik",style="BW.TLabel").place(x=10,y=180)
ulke_combobox_vericekici_gelismislik=tk.StringVar()
ulke_combobox_gelismislik=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_gelismislik,values=(veritabani_gelismislikduzeyi),state="readonly",width=10)
ulke_combobox_gelismislik.place(x=240,y=180)
###################################### Z E N G İ N L İ K ######################################
ulke_label_zenginlik=ttk.Label(tab7,text="GSYİH",style="BW.TLabel").place(x=10,y=220)
ulke_combobox_vericekici_zenginlik=tk.StringVar()
ulke_combobox_zenginlik=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_zenginlik,values=(veritabani_ulke_zenginlik),state="readonly",width=10)
ulke_combobox_zenginlik.place(x=240,y=220)
###################################### İ S İ M ########################################################
ulke_label_isim=ttk.Label(tab7,text="Ülke İsmi",style="BW.TLabel").place(x=10,y=260)
ulke_combobox_vericekici_isim=tk.StringVar()
ulke_combobox_isim=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_isim,values=("İki Heceli","Üç Heceli","Dört Heceli","Beş Heceli"),state="readonly",width=10)
ulke_combobox_isim.place(x=240,y=260)
###################################### S O S Y A L      D E V L E T ######################################
ulke_label_sosyaldevlet=ttk.Label(tab7,text="Devlet Yardımları",style="BW.TLabel").place(x=10,y=300)
ulke_combobox_vericekici_sosyaldevlet=tk.StringVar()
ulke_combobox_sosyaldevlet=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_sosyaldevlet,values=(veritabani_ulke_sosyaldevlet),state="readonly",width=8)
ulke_combobox_sosyaldevlet.place(x=240,y=300)

################################################################################################################################################################
################################################################################################################################################################
"""COĞRAFYA-NÜFUS-EĞİTİM"""
################################################################################################################################################################
################################################################################################################################################################

###################################### E Ğ İ T İ M ######################################
ulke_label_egitim=ttk.Label(tab7,text="Eğitim",style="BW.TLabel").place(x=425,y=20)
ulke_combobox_vericekici_egitim=tk.StringVar()
ulke_combobox_egitim=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_egitim,values=("Korkunç cehalet","Yetersiz","Gelişmiş","Çok iyi"),state="readonly",width=15)
ulke_combobox_egitim.place(x=625,y=20)
###################################### N Ü F U S        A R T I Ş       H I Z I ######################################
ulke_label_nfusuartishizi=ttk.Label(tab7,text="Nüfus Artış Hızı",style="BW.TLabel").place(x=425,y=60)
ulke_combobox_vericekici_nufusartishizi=tk.StringVar()
ulke_combobox_nufusartishizi=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_nufusartishizi,values=("Hızla azalmakta","Azalmakta","Normal artmakta","Hızla artmakta","Aşırı artmakta"),state="readonly",width=15)
ulke_combobox_nufusartishizi.place(x=625,y=60)
###################################### N Ü F U S ######################################
ulke_label_kalabaliklik=ttk.Label(tab7,text="Nüfus",style="BW.TLabel").place(x=425,y=100)
ulke_combobox_vericekici_kalabaliklik=tk.StringVar()
ulke_combobox_kalabaliklik=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_kalabaliklik,values=(veritabani_ulke_kalabalıklık),state="readonly",width=13)
ulke_combobox_kalabaliklik.place(x=625,y=100)
###################################### İ K L İ M ######################################
ulke_label_iklim = ttk.Label(tab7, text="İklim", style="BW.TLabel").place(x=425, y=140)
ulke_combobox_vericekici_iklim= tk.StringVar()
ulke_combobox_iklim = ttk.Combobox(tab7, textvariable=ulke_combobox_vericekici_iklim,values=("Sıcak iklim","Soğuk iklim","Ilıman iklim"),state="readonly", width=11)
ulke_combobox_iklim.place(x=625,y=140)
###################################### Y Ü Z      Ö L Ç Ü M ######################################
ulke_label_yuzolcum=ttk.Label(tab7,text="Ülkenin Yüzölçümü",style="BW.TLabel").place(x=425,y=180)
ulke_combobox_vericekici_yuzolcum=tk.StringVar()
ulke_combobox_yuzolcum=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_yuzolcum,values=("Küçük","Orta","Büyük"),state="readonly",width=9)
ulke_combobox_yuzolcum.place(x=625,y=180)
###################################### K A R A      P A R Ç A S I ##########################################################
ulke_label_karaparcasi = ttk.Label(tab7, text="Kara Parçası", style="BW.TLabel").place(x=425, y=220)
ulke_combobox_vericekici_karaparcasi= tk.StringVar()
ulke_combobox_karaparcasi = ttk.Combobox(tab7, textvariable=ulke_combobox_vericekici_karaparcasi,values=("Tam ada","Yarımada","Tam kara"),state="readonly", width=9)
ulke_combobox_karaparcasi.place(x=625, y=220)
###################################### K A Y N A K      D A Ğ I L I M I ######################################
ulke_label_kaynakdagilimi=ttk.Label(tab7,text="Kaynak Dağılımı",style="BW.TLabel").place(x=425,y=260)
ulke_combobox_vericekici_kaynakdagilimi=tk.StringVar()
ulke_combobox_kaynakdagilimi=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_kaynakdagilimi,values=("Kıt","Yetersiz","Orta","Bol"),state="readonly",width=8)
ulke_combobox_kaynakdagilimi.place(x=625,y=260)
###################################### N Ü F U S        D A Ğ I L I M I ######################################
ulke_label_nufusdagilimi=ttk.Label(tab7,text="Nüfus Ağırlığı",style="BW.TLabel").place(x=425,y=300)
ulke_combobox_vericekici_nufusdagilimi=tk.StringVar()
ulke_combobox_nufusdagilimi=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_nufusdagilimi,values=("Kadın","Erkek"),state="readonly",width=6)
ulke_combobox_nufusdagilimi.place(x=625,y=300)
################################################################################################################################################################
################################################################################################################################################################
"""ASKERİ"""
################################################################################################################################################################
################################################################################################################################################################

###################################### O R D U      T İ P İ ######################################
ulke_label_ordutipi=ttk.Label(tab7,text="Ordu Uzmanlığı",style="BW.TLabel").place(x=800,y=20)
ulke_combobox_vericekici_ordutipi=tk.StringVar()
ulke_combobox_ordutipi=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_ordutipi,values=(veritabani_ulke_ordutipleri),state="readonly",width=14)
ulke_combobox_ordutipi.place(x=970,y=20)
###################################### O R D U      H A R C A M A S I ######################################
ulke_label_orduharcaması=ttk.Label(tab7,text="Ordu Harcaması",style="BW.TLabel").place(x=800,y=60)
ulke_combobox_vericekici_orduharcaması=tk.StringVar()
ulke_combobox_orduharcaması=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_orduharcaması,values=("Çok az","Az","Dengeli","Çok","Çok fazla"),state="readonly",width=8)
ulke_combobox_orduharcaması.place(x=970,y=60)
###################################### O R D U      E N V A N T E R İ ######################################
ulke_label_orduenvanteri=ttk.Label(tab7,text="Ordu Envanteri",style="BW.TLabel").place(x=800,y=100)
ulke_combobox_vericekici_orduenvanteri=tk.StringVar()
ulke_combobox_orduenvanteri=ttk.Combobox(tab7,textvariable=ulke_combobox_vericekici_orduenvanteri,values=("Kıt","Bol"),state="readonly",width=4)
ulke_combobox_orduenvanteri.place(x=970,y=100)

################################################################################################################################################################
################################################################################################################################################################
"""FONKSİYONEL"""
################################################################################################################################################################
################################################################################################################################################################

def ulke_function_yonetim():
    kosul=ulke_combobox_vericekici_yonetim.get()
    if kosul=='Cumhuriyet':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Demokrasi':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Meşrutiyet':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Monarşi':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Oligarşi':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Otokrasi':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Plütokrasi':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Teknokrasi':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Teokrasi':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    elif kosul=='Totalitarizm':
        sonuc="Yönetim Biçimi: {}".format(kosul)
        return sonuc
    
def ulke_function_ekonomiksistem():
    kosul=ulke_combobox_vericekici_piyasaserbestligi.get()
    if kosul=="Neo-Liberalizm":
        sonuc="Ekonomik Sistem: {}".format(kosul)
        a=random.randint(0,1)
        if a==0:
            ulke_combobox_sosyaldevlet.current(0)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(1)
        return sonuc
    elif kosul=="Kapitalizm":
        sonuc="Ekonomik Sistem: {}".format(kosul)
        a=random.randint(0,1)
        if a==0:
            ulke_combobox_sosyaldevlet.current(0)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(1)
        return sonuc
    elif kosul=="Emperyalizm":
        sonuc="Ekonomik Sistem: {}".format(kosul)
        a=random.randint(0,1)
        if a==0:
            ulke_combobox_sosyaldevlet.current(0)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(1)
        return sonuc
    elif kosul=="Sosyalizm":
        sonuc="Ekonomik Sistem: {}".format(kosul)
        a=random.randint(3,4)
        if a==0:
            ulke_combobox_sosyaldevlet.current(3)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(4)
        return sonuc
    elif kosul=="Komünizm":
        sonuc="Ekonomik Sistem: {}".format(kosul)
        a=random.randint(3,4)
        if a==0:
            ulke_combobox_sosyaldevlet.current(3)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(4)
        return sonuc
    elif kosul=="Muller Ekonomisi":
        sonuc="Ekonomik Sistem: {}".format(kosul)
        a=random.randint(3,4)
        if a==0:
            ulke_combobox_sosyaldevlet.current(3)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(4)
        return sonuc

def ulke_function_refah():
    kosul=ulke_combobox_vericekici_refah.get()
    if kosul=="Halk açlık sınırında":
        sonuc="Refah: {}".format(kosul)
        return sonuc
    elif kosul=="Yetersiz":
        sonuc="Refah: {}".format(kosul)
        return sonuc
    elif kosul=="Orta Düzey":
        sonuc="Refah: {}".format(kosul)
        return sonuc
    elif kosul=="Çok iyi":
        sonuc="Refah: {}".format(kosul)
        return sonuc

def ulke_function_federasyon():
    kosul=ulke_combobox_vericekici_federasyon.get()
    if kosul=="Üniter Devlet":
        sonuc="Federasyon: {}".format(kosul)
        return sonuc
    elif kosul=="Federal Devlet":
        sonuc="Federasyon: {}".format(kosul)
        return sonuc
    
def ulke_function_gelismislik():
    kosul=ulke_combobox_vericekici_gelismislik.get()
    if kosul=="Çok kötü":
        sonuc="""Gelişmişlik: Çok kötü"""
        a=random.randint(0,1)
        if a==0:
            ulke_combobox_sosyaldevlet.current(0)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(1)
        b=random.randint(0,1)
        if b==0:
            ulke_combobox_refah.current(0)
        elif b==1:
            ulke_combobox_refah.current(1)
        c=random.randint(0,1)
        if c==0:
            ulke_combobox_egitim.current(0)
        elif c==1:
            ulke_combobox_egitim.current(1)
        d=random.randint(0,1)
        if d==0:
            ulke_combobox_zenginlik.current(0)
        elif d==1:
            ulke_combobox_zenginlik.current(1)
        return sonuc
    elif kosul=="Kötü":
        sonuc="Gelişmişlik: Kötü"
        a=random.randint(0,1)
        if a==0:
            ulke_combobox_sosyaldevlet.current(0)
        elif a==1:
            ulke_combobox_sosyaldevlet.current(1)
        b=random.randint(0,1)
        if b==0:
            ulke_combobox_refah.current(0)
        elif b==1:
            ulke_combobox_refah.current(1)
        c=random.randint(0,1)
        if c==0:
            ulke_combobox_zenginlik.current(0)
        elif c==1:
            ulke_combobox_zenginlik.current(1)
        return sonuc
    elif kosul=="Gelişmekte":
        sonuc="Gelişmişlik: Gelişmekte"
        return sonuc
    elif kosul=="İyi":
        sonuc="Gelişmişlik: İyi"
        a=random.randint(3,4)
        if a==3:
            ulke_combobox_sosyaldevlet.current(3)
        elif a==4:
            ulke_combobox_sosyaldevlet.current(4)
        b=random.randint(2,3)
        if b==2:
            ulke_combobox_egitim.current(2)
        elif b==3:
            ulke_combobox_egitim.current(3)
        c=random.randint(2,4)
        if c==2:
            ulke_combobox_zenginlik.current(2)
        elif c==3:
            ulke_combobox_zenginlik.current(3)
        elif c==4:
             ulke_combobox_zenginlik.current(4)
        return sonuc
    elif kosul=="Çok iyi":
        sonuc="Gelişmişlik: Çok iyi"
        ulke_combobox_egitim.current(3)
        a=random.randint(3,4)
        if a==3:
            ulke_combobox_sosyaldevlet.current(3)
        elif a==4:
            ulke_combobox_sosyaldevlet.current(4)
        b=random.randint(2,3)
        if b==2:
            ulke_combobox_refah.current(2)
        elif b==3:
            ulke_combobox_refah.current(3)
        c=random.randint(3,4)
        if c==3:
            ulke_combobox_zenginlik.current(3)
        elif c==4:
            ulke_combobox_zenginlik.current(4)

        return sonuc

def ulke_function_zenginlik():
    kosul=ulke_combobox_vericekici_zenginlik.get()
    if kosul=="Çok kötü":
        sonuc="GSYİH: {}".format(kosul)
        return sonuc
    elif kosul=="Kötü":
        sonuc="GSYİH: {}".format(kosul)
        return sonuc
    elif kosul=="Gelişmekte":
        sonuc="GSYİH: {}".format(kosul)
        return sonuc
    elif kosul=="İyi":
        sonuc="GSYİH: {}".format(kosul)
        return sonuc
    elif kosul=="Çok iyi":
        sonuc="GSYİH: {}".format(kosul)
        return sonuc

def ulke_function_isim():
    kosul=ulke_combobox_vericekici_isim.get()
    if (kosul=="İki Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        sonuc="İsim: {}\n".format(name)
        return sonuc   
    elif (kosul=="Üç Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        vt_pt1.remove(ikinci_hece)
        ucuncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        sonuc="İsim: {}".format(name)
        return sonuc
    elif (kosul=="Dört Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        vt_pt1.remove(ikinci_hece)
        ucuncu_hece=random.choice(vt_pt1)
        vt_pt1.remove(ucuncu_hece)
        dorduncu_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        sonuc="İsim: {}".format(name)
        return sonuc
    elif (kosul=="Beş Heceli"):
        #Veri çekiyor
        ilk_hece=random.choice(vt_pt1)
        vt_pt1.remove(ilk_hece)
        ikinci_hece=random.choice(vt_pt1)
        vt_pt1.remove(ikinci_hece)
        ucuncu_hece=random.choice(vt_pt1)
        vt_pt1.remove(ucuncu_hece)
        dorduncu_hece=random.choice(vt_pt1)
        vt_pt1.remove(dorduncu_hece)
        besinci_hece=random.choice(vt_pt1)
        #İsim Oluşturuyor
        name=ilk_hece+ikinci_hece+ucuncu_hece+dorduncu_hece+besinci_hece
        #ilk harfi büyük yapar
        name=name.capitalize() 
        sonuc="İsim: {}".format(name)
        return sonuc

def ulke_function_devletyardimlari():
    kosul=ulke_combobox_vericekici_sosyaldevlet.get()
    if kosul=="Çok az":
        sonuc="Devlet Yardımları: {}".format(kosul)
        return sonuc
    elif kosul=="Az":
        sonuc="Devlet Yardımları: {}".format(kosul)
        return sonuc
    elif kosul=="Dengeli":
        sonuc="Devlet Yardımları: {}".format(kosul)
        return sonuc
    elif kosul=="Çok":
        sonuc="Devlet Yardımları: {}".format(kosul)
        return sonuc
    elif kosul=="Çok fazla":
        sonuc="Devlet Yardımları: {}".format(kosul)
        return sonuc

def ulke_function_egitim():
    kosul=ulke_combobox_vericekici_egitim.get()
    if kosul=="Korkunç cehalet":
        sonuc="Eğitim Düzeyi: {}".format(kosul)
        a=random.randint(0,1)
        if a==0:
            ulke_combobox_gelismislik.current(0)
        elif a==1:
            ulke_combobox_gelismislik.current(1)
        return sonuc
    elif kosul=="Yetersiz":
        sonuc="Eğitim Düzeyi: {}".format(kosul)
        a=random.randint(0,1)
        if a==0:
            ulke_combobox_gelismislik.current(0)
        elif a==1:
            ulke_combobox_gelismislik.current(1)
        return sonuc
    elif kosul=="Gelişmiş":
        sonuc="Eğitim Düzeyi: {}".format(kosul)
        ulke_combobox_gelismislik.current(3)
        return sonuc
    elif kosul=="Çok iyi":
        sonuc="Eğitim Düzeyi: {}".format(kosul)
        a=random.randint(3,4)
        if a==3:
            ulke_combobox_gelismislik.current(3)
        elif a==4:
            ulke_combobox_gelismislik.current(4)
        return sonuc
    
def ulke_function_nufusartishizi():
    kosul=ulke_combobox_vericekici_nufusartishizi.get()
    if kosul=="Hızla azalmakta":
        a=random.uniform(-2.23,-1.5)
        a=round(a,4)
        sonuc="Nüfus Artış Hızı: % {}".format(a)
        return sonuc
    elif kosul=="Azalmakta":
        a=random.uniform(-1.49,-0.1)
        a=round(a,4)
        sonuc="Nüfus Artış Hızı: %{}".format(a)
        return sonuc
    elif kosul=="Normal artmakta":
        a=1
        sonuc="Nüfus Artış Hızı: %{}".format(a)
        return sonuc
    elif kosul=="Hızla artmakta":
        a=random.uniform(1.5,2.5)
        a=round(a,4)
        sonuc="Nüfus Artış Hızı: %{}".format(a)
        return sonuc
    elif kosul=="Aşırı artmakta":
        a=random.uniform(2.6,5)
        a=round(a,4)
        sonuc="Nüfus Artış Hızı: %{}".format(a)
        return sonuc
    
def ulke_function_nufus():
    kosul=ulke_combobox_vericekici_kalabaliklik.get()
    if kosul=="Çok az":
        nufus=random.randint(1500,11000)
        nufusagirlik=random.randint(1,6)
        """ +cocuk>genc>yasli    formül=(40,45)-(31,34)-(100-cocuk-genc)
            +cocuk>yasli>genc
            +genc>cocuk>yasli
            +genc>yasli>cocuk
            +yasli>genc>cocuk
            +yasli>cocuk>genc"""
        if nufusagirlik==1:
            cocuk=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==2:
            cocuk=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            genc=int(100-(cocuk+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==3:
            genc=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==4:
            genc=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==5:
            yasli=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==6:
            yasli=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            genc=100-(cocuk+yasli)
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc

    elif kosul=="Az":
        nufus=random.randint(50000,1000000)
        nufusagirlik=random.randint(1,6)
        """ +cocuk>genc>yasli    formül=(40,45)-(31,34)-(100-cocuk-genc)
            +cocuk>yasli>genc
            +genc>cocuk>yasli
            +genc>yasli>cocuk
            +yasli>genc>cocuk
            +yasli>cocuk>genc"""
        if nufusagirlik==1:
            cocuk=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==2:
            cocuk=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            genc=int(100-(cocuk+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==3:
            genc=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==4:
            genc=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==5:
            yasli=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==6:
            yasli=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            genc=100-(cocuk+yasli)
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc

    elif kosul=="Orta":
        nufus=random.randint(1000000,10000000)
        nufusagirlik=random.randint(1,6)
        """ +cocuk>genc>yasli    formül=(40,45)-(31,34)-(100-cocuk-genc)
            +cocuk>yasli>genc
            +genc>cocuk>yasli
            +genc>yasli>cocuk
            +yasli>genc>cocuk
            +yasli>cocuk>genc"""
        if nufusagirlik==1:
            cocuk=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==2:
            cocuk=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            genc=int(100-(cocuk+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==3:
            genc=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==4:
            genc=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==5:
            yasli=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==6:
            yasli=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            genc=100-(cocuk+yasli)
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc

    elif kosul=="Kalabalık":
        nufus=random.randint(10000000,100000000)
        nufusagirlik=random.randint(1,6)
        """ +cocuk>genc>yasli    formül=(40,45)-(31,34)-(100-cocuk-genc)
            +cocuk>yasli>genc
            +genc>cocuk>yasli
            +genc>yasli>cocuk
            +yasli>genc>cocuk
            +yasli>cocuk>genc"""
        if nufusagirlik==1:
            cocuk=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==2:
            cocuk=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            genc=int(100-(cocuk+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==3:
            genc=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==4:
            genc=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==5:
            yasli=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==6:
            yasli=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            genc=100-(cocuk+yasli)
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc

    elif kosul=="Çok kalabalık":
        nufus=random.randint(100000000,1000000000)
        nufusagirlik=random.randint(1,6)
        """ +cocuk>genc>yasli    formül=(40,45)-(31,34)-(100-cocuk-genc)
            +cocuk>yasli>genc
            +genc>cocuk>yasli
            +genc>yasli>cocuk
            +yasli>genc>cocuk
            +yasli>cocuk>genc"""
        if nufusagirlik==1:
            cocuk=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==2:
            cocuk=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            genc=int(100-(cocuk+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==3:
            genc=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            yasli=int(100-(cocuk+genc))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==4:
            genc=int(random.randint(40,45))
            yasli=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==5:
            yasli=int(random.randint(40,45))
            genc=int(random.randint(31,34))
            cocuk=int(100-(genc+yasli))
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc
        elif nufusagirlik==6:
            yasli=int(random.randint(40,45))
            cocuk=int(random.randint(31,34))
            genc=100-(cocuk+yasli)
            #nüfus sayıları
            cocuknufusu=int(nufus*cocuk/100)
            gencnufusu=int(nufus*genc/100)
            yaslinufusu=int(nufus*yasli/100)
            toplamnufus=cocuknufusu+gencnufusu+yaslinufusu
            #Kadın-erkek
            cinsiyetagirligi=ulke_combobox_vericekici_nufusdagilimi.get()
            if cinsiyetagirligi=="Kadın":
                kadinorani=random.randint(51,60)
                erkekorani=100-kadinorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            elif cinsiyetagirligi=="Erkek":
                erkekorani=random.randint(51,60)
                kadinorani=100-erkekorani
                kadinsayisi=int(toplamnufus*kadinorani/100)
                erkeksayisi=int(toplamnufus*erkekorani/100)
                gercektoplamnufus=kadinsayisi+erkeksayisi
            #sonuc
            sonuc="""*****NÜFUS*****
            \tToplam Nüfus: {}   Çocuk Nüfus: {}    Genç Nüfus: {}    Yaşlı Nüfus:    {}
            \tÇocukların Toplam Nüfusa Oranı: %{}
            \tGençlerin Toplam Nüfusa Oranı: %{}
            \tYaşlıların Toplam Nüfusa Oranı: %{}
            
            \tKadın Nüfus: {}       Kadınların Toplam Nüfusa Oranı: %{}
            \tErkek Nüfus: {}       Erkeklerin Toplam Nüfusa Oranı: %{}
            """.format(gercektoplamnufus,cocuknufusu,gencnufusu,yaslinufusu,cocuk,genc,yasli,kadinsayisi,kadinorani,erkeksayisi,erkekorani)
            return sonuc

def ulke_function_iklim():
    kosul=ulke_combobox_vericekici_iklim.get()
    if kosul=="Sıcak iklim":
        a=random.randint(0,3)
        if a==0:
            #Ekvatoral iklim
            b=veritabani_ulke_ekvatoraliklim
            return b
        elif a==1:
            #Tropikal iklim
            b=veritabani_ulke_tropikaliklim
            return b
        elif a==2:
            #Muson iklimi
            b=veritabani_ulke_musoniklimi
            return b
        elif a==3:
            #Çöl iklimi
            b=veritabani_ulke_coliklimi
            return b

    elif kosul=="Soğuk iklim":
        a=random.randint(0,1)
        if a==0:
            #Tundra iklim
            b=veritabani_ulke_tundraiklimi
            return b
        elif a==1:
            #Kutup iklim
            b=veritabani_ulke_kutupiklimi
            return b
    elif kosul=="Ilıman iklim":
        a=random.randint(0,3)
        if a==0:
            #Akdeniz iklim
            b=veritabani_ulke_akdeniziklimi
            return b
        elif a==1:
            #Okyanusal iklim
            b=veritabani_ulke_okyanusaliklim
            return b
        elif a==2:
            #Karasal iklimi
            b=veritabani_ulke_karasaliklim
            return b
        elif a==3:
            #Step iklimi
            b=veritabani_ulke_stepiklimi
            return b

def ulke_function_yuzolcum():
    kosul=ulke_combobox_vericekici_yuzolcum.get()
    if kosul=="Küçük":
        a=int(random.randint(100000,250000))
        sonuc="""*****FİZİKSEL YAPI*****
        \tKüçük bir ülkedir. Ülkenin Yüzölçümü: {} km^2""".format(a)
        return sonuc
    elif kosul=="Orta":
        a=int(random.randint(250001,500000))
        sonuc="""*****FİZİKSEL YAPI*****
        \tOrta büyüklükte bir ülkedir. Ülkenin Yüzölçümü: {} km^2""".format(a)
        return sonuc
    elif kosul=="Büyük":
        a=int(random.randint(500000,1000000))
        sonuc="""*****FİZİKSEL YAPI*****
        \tBüyük bir ülkedir. Ülkenin Yüzölçümü: {} km^2""".format(a)
        return sonuc

def ulke_function_karaparcasi():
    kosul=ulke_combobox_vericekici_karaparcasi.get()
    if kosul=="Tam ada":
        a="\tÜlke, dört tarafı deniz/okyanusla çevrili bir ada ülkesidir."
        return a
    elif kosul=="Yarımada":
        a="\tÜlke, yarısı veya 3/4'ü deniz/okyanusla çevrili bir yarımada ülkesidir."
        return a
    elif kosul=="Tam kara":
        a="\tÜlke, tamamen kara ülkesidir. Ülkenin çevresini kaplayan deniz/okyanus yoktur."
        return a

def ulke_function_kaynakdagilimi():
    kosul=ulke_combobox_vericekici_kaynakdagilimi.get()
    if kosul=="Kıt":
        #ormanlık alan (oransal olarak) (max 72)
        #sulak alan
        #dağlık alan
        #Demir, bakır krom kurşun çinko bor mineralleri , feldspat, gümüş bakır, altın  alüminyum demiir
        #taş kömürü,petrol ,doğal gaz
        ormanlikalan=random.randint(5,15)
        sulakalan=random.randint(5,10)
        daglikalan=(15,30)
        sonuc="""*****COĞRAFYA*****
        \tÜlke topraklarında ormanların kapladığı alan: %{}
        \tÜlke topraklarında sulak yerlerin(akarsu,göl vs.) kapladığı alan: %{}
        \tÜlke topraklarında dağlık yerlerin kapladığı alan: %{}\n*****DOĞAL KAYNAKLAR*****
        \tÜlke yeraltı kaynakları açısından fakirdir. Demir, bakır, krom, kurşun, çinko, bor, feldspat, gümüş, altın, alüminyum gibi önemli madenler kıttır.
        \tBunların büyük bir kısmı ithal edilir.
        \tÜlke, taş kömürü, petrol ve doğalgaz yatakları açısından kıttır. Ülke enerjide dışarıya bağımlıdır.""".format(ormanlikalan,sulakalan,daglikalan)
        return sonuc
    elif kosul=="Yetersiz":
        ormanlikalan=random.randint(11,34)
        sulakalan=random.randint(11,15)
        daglikalan=(15,30)
        sonuc="""*****COĞRAFYA*****
        \tÜlke topraklarında ormanların kapladığı alan: %{}
        \tÜlke topraklarında sulak yerlerin(akarsu,göl vs.) kapladığı alan: %{}
        \tÜlke topraklarında dağlık yerlerin kapladığı alan: %{}\n*****DOĞAL KAYNAKLAR*****
        \tÜlke, yeraltı kaynakları açısından kıt değil ama yetersizdir. Demir, bakır, krom, kurşun, çinko, bor, feldspat, gümüş, altın, alüminyum gibi önemli madenler yetersiz düzeydedir.
        \tDemir, feldspat, alüminyum gibi madenler hariç kalanları ithal edilir.
        \tÜlke, taş kömürü, petrol ve doğalgaz yatakları açısından yetersizdir. Ülke enerjide dışarıya kısmen bağımlıdır.""".format(ormanlikalan,sulakalan,daglikalan)
        return sonuc
    elif kosul=="Orta":
        ormanlikalan=random.randint(24,68)
        sulakalan=random.randint(16,20)
        daglikalan=(15,30)
        sonuc="""*****COĞRAFYA*****
        \tÜlke topraklarında ormanların kapladığı alan: %{}
        \tÜlke topraklarında sulak yerlerin(akarsu,göl vs.) kapladığı alan: %{}
        \tÜlke topraklarında dağlık yerlerin kapladığı alan: %{}\n*****DOĞAL KAYNAKLAR*****
        \tÜlke, yeraltı kaynakları açısından ne kıt ne boldur. 
        \tDemir, bakır, krom, kurşun, çinko, bor, feldspat, gümüş, altın, alüminyum gibi önemli madenler orta seviyede mevcuttur.
        \tBu madenlerin bir çoğu üretimde kullanılır, yani ülkenin madenleri ancak kendisine yetecek düzeydedir.
        \tÜlke, taş kömürü, petrol ve doğalgaz yatakları açısından yeterli düzeydedir. 
        \tÜlkenin sahip olduğu enerji yatakları ancak kendisine yeterlidir.""".format(ormanlikalan,sulakalan,daglikalan)
        return sonuc
    elif kosul=="Bol":
        ormanlikalan=random.randint(56,70)
        sulakalan=random.randint(21,25)
        daglikalan=(15,30)
        sonuc="""*****COĞRAFYA*****
        \tÜlke topraklarında ormanların kapladığı alan: %{}
        \tÜlke topraklarında sulak yerlerin(akarsu,göl vs.) kapladığı alan: %{}
        \tÜlke topraklarında dağlık yerlerin kapladığı alan: %{}\n*****DOĞAL KAYNAKLAR*****
        \tÜlke, yeraltı kaynaklarının çeşidi ve rezervleri açısından zengindir. 
        \tDemir, bakır, krom, kurşun, çinko, bor, feldspat, gümüş, altın, alüminyum ve birçok maden  bol miktarda bulunur.
        \tBu madenlerin bir çoğu üretimde kullanılırken, arta kalan kısmı ihraç edilir.
        \tÜlke, taş kömürü, petrol ve doğalgaz yatakları açısından zengindir. 
        \tÜlke bu yakıtları kendi üretimi için kullandıktan sonra enerji yakıtlarının bir çoğunu ihraç eder.""".format(ormanlikalan,sulakalan,daglikalan)
        return sonuc

def ulke_function_ordu_uzmanligi():
    kosul=ulke_combobox_vericekici_ordutipi.get()
    if kosul=="Kara kuvvetleri":
        sonuc="Ordu Uzmanlığı: {}".format(kosul)
    elif kosul=="Deniz kuvvetleri":
        sonuc="Ordu Uzmanlığı: {}".format(kosul)
    elif kosul=="Hava kuvvetleri":
        sonuc="Ordu Uzmanlığı: {}".format(kosul)

def ulke_function_orduharcamasi():
    kosul=ulke_combobox_vericekici_orduharcaması.get()
    if kosul=="Çok az":
        gsyihpayi=random.randint(1,5)
        ulke_combobox_orduenvanteri.current(0)
    elif kosul=="Az":
        gsyihpayi=random.randint(6,8)
        ulke_combobox_orduenvanteri.current(0)
    elif kosul=="Dengeli":
        gsyihpayi=random.randint(9,11)
        ulke_combobox_orduenvanteri.current(0)
    elif kosul=="Çok":
        gsyihpayi=random.randint(12,14)
        ulke_combobox_orduenvanteri.current(1)
    elif kosul=="Çok fazla":
        gsyihpayi=random.randint(15,17)
        ulke_combobox_orduenvanteri.current(1)
    sonuc="Ordu Harcaması/GSYİH: %{}".format(gsyihpayi)
    return sonuc

def ulke_function_orduenvanteri():
    kosul=ulke_combobox_vericekici_orduenvanteri.get()
    ordutipi999=ulke_combobox_vericekici_ordutipi.get()
    #Kıt durumu 2'ye ayrılsın. İlki çok kıtlık durumu, ikincisi kıtlık durumu. Ayrıca ordu envanteri belirlenirken ordu tipi dikkate alınacak.
    if kosul=="Kıt":
        liste999=("Çok kıt","Kıt")
        a=random.choice(liste999)
        if a=="Çok kıt":
            if ordutipi999=="Kara kuvvetleri":
                asker=random.randint(10000,60000)
                tanklar=random.randint(10,30)
                zirhliaraclar=random.randint(10,30)
                alantoplari=random.randint(10,30)
                kundagimotorlutopcusistemleri=random.randint(3,5)
                coknamluluroketatar=random.randint(1,5)
                cekiliucaksavartoplari=random.randint(1,5)
                havasavunmasistemleri=0

                personel=random.randint(1000,5000)
                fırkateyn=random.randint(1,4)
                korvetn=random.randint(1,4)
                denizalti=0
                hucumbot=random.randint(1,4)
                denizsinirihudutdevriyebotu=random.randint(1,4)
                mayinavlamavetaramagemisi=random.randint(1,2)
                amfibisavasgemisi=random.randint(1,2)
                askertasimagemisi=random.randint(1,2)
                ucakgemisi=0
                
                personel2=random.randint(50,100)
                avciucagi=random.randint(1,3)
                insansizhavaaraci=0
                nakliyesaldirihelikopteri=random.randint(3,10)
                bombardimanucagi=random.randint(0,3)
                nakliyeucagi=random.randint(1,3)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc

            elif ordutipi999=="Deniz kuvetleri":
                asker=random.randint(5000,20000)
                tanklar=random.randint(5,10)
                zirhliaraclar=random.randint(5,10)
                alantoplari=random.randint(5,10)
                kundagimotorlutopcusistemleri=random.randint(0,5)
                coknamluluroketatar=0
                cekiliucaksavartoplari=random.randint(1,3)
                havasavunmasistemleri=0

                personel=random.randint(2500,5500)
                fırkateyn=random.randint(1,8)
                korvetn=random.randint(1,8)
                denizalti=0
                hucumbot=random.randint(1,8)
                denizsinirihudutdevriyebotu=random.randint(1,8)
                mayinavlamavetaramagemisi=random.randint(1,4)
                amfibisavasgemisi=random.randint(1,4)
                askertasimagemisi=random.randint(1,4)
                ucakgemisi=0

                personel2=random.randint(50,100)
                avciucagi=random.randint(1,3)
                insansizhavaaraci=0
                nakliyesaldirihelikopteri=random.randint(3,10)
                bombardimanucagi=random.randint(0,3)
                nakliyeucagi=random.randint(1,3)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc
            elif ordutipi999=="Hava kuvvetleri":
                asker=random.randint(5000,20000)
                tanklar=random.randint(5,10)
                zirhliaraclar=random.randint(5,10)
                alantoplari=random.randint(5,10)
                kundagimotorlutopcusistemleri=random.randint(0,5)
                coknamluluroketatar=0
                cekiliucaksavartoplari=random.randint(1,3)
                havasavunmasistemleri=0

                personel=random.randint(2500,5500)
                fırkateyn=random.randint(1,8)
                korvetn=random.randint(1,8)
                denizalti=0
                hucumbot=random.randint(1,8)
                denizsinirihudutdevriyebotu=random.randint(1,8)
                mayinavlamavetaramagemisi=random.randint(1,4)
                amfibisavasgemisi=random.randint(1,4)
                askertasimagemisi=random.randint(1,4)
                ucakgemisi=0

                personel2=random.randint(100,500)
                avciucagi=random.randint(1,10)
                insansizhavaaraci=0
                nakliyesaldirihelikopteri=random.randint(5,20)
                bombardimanucagi=random.randint(1,5)
                nakliyeucagi=random.randint(1,10)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc

        elif a=="Kıt":
            if ordutipi999=="Kara kuvvetleri":
                asker=random.randint(10000,60000)
                tanklar=random.randint(10,30)
                zirhliaraclar=random.randint(10,30)
                alantoplari=random.randint(10,30)
                kundagimotorlutopcusistemleri=random.randint(3,5)
                coknamluluroketatar=random.randint(1,5)
                cekiliucaksavartoplari=random.randint(1,5)
                havasavunmasistemleri=0

                personel=random.randint(5000,7500)
                fırkateyn=random.randint(1,8)
                korvetn=random.randint(1,8)
                denizalti=1
                hucumbot=random.randint(1,8)
                denizsinirihudutdevriyebotu=random.randint(1,8)
                mayinavlamavetaramagemisi=random.randint(1,2)
                amfibisavasgemisi=random.randint(1,4)
                askertasimagemisi=random.randint(1,4)
                ucakgemisi=0

                personel2=random.randint(100,500)
                avciucagi=random.randint(1,10)
                insansizhavaaraci=0
                nakliyesaldirihelikopteri=random.randint(5,20)
                bombardimanucagi=random.randint(1,5)
                nakliyeucagi=random.randint(1,10)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc

            elif ordutipi999=="Deniz kuvetleri":
                asker=random.randint(10000,60000)
                tanklar=random.randint(10,30)
                zirhliaraclar=random.randint(10,30)
                alantoplari=random.randint(10,30)
                kundagimotorlutopcusistemleri=random.randint(3,5)
                coknamluluroketatar=random.randint(1,5)
                cekiliucaksavartoplari=random.randint(1,5)
                havasavunmasistemleri=0

                personel=random.randint(7500,10000)
                fırkateyn=random.randint(1,12)
                korvetn=random.randint(1,12)
                denizalti=2
                hucumbot=random.randint(1,12)
                denizsinirihudutdevriyebotu=random.randint(1,12)
                mayinavlamavetaramagemisi=random.randint(1,4)
                amfibisavasgemisi=random.randint(1,4)
                askertasimagemisi=random.randint(1,4)
                ucakgemisi=0

                personel2=random.randint(100,500)
                avciucagi=random.randint(1,10)
                insansizhavaaraci=0
                nakliyesaldirihelikopteri=random.randint(5,20)
                bombardimanucagi=random.randint(1,5)
                nakliyeucagi=random.randint(1,10)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc

            elif ordutipi999=="Hava kuvvetleri":
                asker=random.randint(10000,60000)
                tanklar=random.randint(10,30)
                zirhliaraclar=random.randint(10,30)
                alantoplari=random.randint(10,30)
                kundagimotorlutopcusistemleri=random.randint(3,5)
                coknamluluroketatar=random.randint(1,5)
                cekiliucaksavartoplari=random.randint(1,5)
                havasavunmasistemleri=0

                personel=random.randint(7500,10000)
                fırkateyn=random.randint(1,12)
                korvetn=random.randint(1,12)
                denizalti=2
                hucumbot=random.randint(1,12)
                denizsinirihudutdevriyebotu=random.randint(1,12)
                mayinavlamavetaramagemisi=random.randint(1,4)
                amfibisavasgemisi=random.randint(1,4)
                askertasimagemisi=random.randint(1,4)
                ucakgemisi=0

                personel2=random.randint(1000,2000)
                avciucagi=random.randint(1,25)
                insansizhavaaraci=0
                nakliyesaldirihelikopteri=random.randint(10,50)
                bombardimanucagi=random.randint(1,10)
                nakliyeucagi=random.randint(1,20)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc

    elif kosul=="Bol":
        liste999=("Bol","Çok bol")
        a=random.choice(liste999)
        if a=="Bol":
            if ordutipi999=="Kara kuvvetleri":
                asker=random.randint(150000,250000)
                tanklar=random.randint(50,150)
                zirhliaraclar=random.randint(50,150)
                alantoplari=random.randint(50,150)
                kundagimotorlutopcusistemleri=random.randint(50,150)
                coknamluluroketatar=random.randint(35,50)
                cekiliucaksavartoplari=random.randint(35,50)
                havasavunmasistemleri=random.randint(5,15)

                personel=random.randint(100000,200000)
                fırkateyn=random.randint(24,48)
                korvetn=random.randint(24,48)
                denizalti=40
                hucumbot=random.randint(24,60)
                denizsinirihudutdevriyebotu=random.randint(24,60)
                mayinavlamavetaramagemisi=random.randint(12,30)
                amfibisavasgemisi=random.randint(64,100)
                askertasimagemisi=random.randint(64,100)
                ucakgemisi=random.randint(1,2)

                personel2=random.randint(15000,45000)
                avciucagi=random.randint(75,125)
                insansizhavaaraci=random.randint(5,36)
                nakliyesaldirihelikopteri=random.randint(15,150)
                bombardimanucagi=random.randint(25,75)
                nakliyeucagi=random.randint(35,75)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc

            elif ordutipi999=="Deniz kuvetleri":
                asker=random.randint(30000,150000)
                tanklar=random.randint(30,70)
                zirhliaraclar=random.randint(40,70)
                alantoplari=random.randint(40,70)
                kundagimotorlutopcusistemleri=random.randint(10,40)
                coknamluluroketatar=random.randint(10,19)
                cekiliucaksavartoplari=random.randint(5,15)
                havasavunmasistemleri=random.randint(3,10)

                personel=random.randint(100000,200000)
                fırkateyn=random.randint(24,72)
                korvetn=random.randint(24,72)
                denizalti=72
                hucumbot=random.randint(24,90)
                denizsinirihudutdevriyebotu=random.randint(24,90)
                mayinavlamavetaramagemisi=random.randint(12,60)
                amfibisavasgemisi=random.randint(64,150)
                askertasimagemisi=random.randint(64,150)
                ucakgemisi=random.randint(1,3)

                personel2=random.randint(5000,15000)
                avciucagi=random.randint(10,100)
                insansizhavaaraci=random.randint(10,15)
                nakliyesaldirihelikopteri=random.randint(15,60)
                bombardimanucagi=random.randint(10,30)
                nakliyeucagi=random.randint(10,30)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc
                
            elif ordutipi999=="Hava kuvvetleri":
                asker=random.randint(200000,300000)
                tanklar=random.randint(30,70)
                zirhliaraclar=random.randint(40,70)
                alantoplari=random.randint(30,70)
                kundagimotorlutopcusistemleri=random.randint(10,40)
                coknamluluroketatar=random.randint(10,19)
                cekiliucaksavartoplari=random.randint(5,12)
                havasavunmasistemleri=random.randint(3,5)

                personel=random.randint(100000,200000)
                fırkateyn=random.randint(24,48)
                korvetn=random.randint(24,48)
                denizalti=40
                hucumbot=random.randint(24,60)
                denizsinirihudutdevriyebotu=random.randint(24,60)
                mayinavlamavetaramagemisi=random.randint(12,30)
                amfibisavasgemisi=random.randint(64,100)
                askertasimagemisi=random.randint(64,100)
                ucakgemisi=random.randint(1,2)

                personel2=random.randint(30000,100000)
                avciucagi=random.randint(100,250)
                insansizhavaaraci=random.randint(5,20)
                nakliyesaldirihelikopteri=random.randint(50,150)
                bombardimanucagi=random.randint(20,50)
                nakliyeucagi=random.randint(20,50)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc
                
        elif a=="Çok bol":
            if ordutipi999=="Kara kuvvetleri":
                asker=random.randint(1000000,3000000)
                tanklar=random.randint(150,750)
                zirhliaraclar=random.randint(100,300)
                alantoplari=random.randint(100,500)
                kundagimotorlutopcusistemleri=random.randint(50,150)
                coknamluluroketatar=random.randint(25,75)
                cekiliucaksavartoplari=random.randint(25,75)
                havasavunmasistemleri=random.randint(25,45)

                personel=random.randint(100000,250000)
                fırkateyn=random.randint(24,64)
                korvetn=random.randint(24,64)
                denizalti=48
                hucumbot=random.randint(24,72)
                denizsinirihudutdevriyebotu=random.randint(24,72)
                mayinavlamavetaramagemisi=random.randint(12,36)
                amfibisavasgemisi=random.randint(64,120)
                askertasimagemisi=random.randint(64,120)
                ucakgemisi=random.randint(1,3)

                personel2=random.randint(75000,150000)
                avciucagi=random.randint(60,120)
                insansizhavaaraci=random.randint(10,20)
                nakliyesaldirihelikopteri=random.randint(75,150)
                bombardimanucagi=random.randint(25,50)
                nakliyeucagi=random.randint(25,50)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc
                
            elif ordutipi999=="Deniz kuvetleri":
                asker=random.randint(1000000,3000000)
                tanklar=random.randint(150,150)
                zirhliaraclar=random.randint(50,120)
                alantoplari=random.randint(50,120)
                kundagimotorlutopcusistemleri=random.randint(30,120)
                coknamluluroketatar=random.randint(20,50)
                cekiliucaksavartoplari=random.randint(25,75)
                havasavunmasistemleri=random.randint(3,15)

                personel=random.randint(250000,500000)
                fırkateyn=random.randint(72,150)
                korvetn=random.randint(72,150)
                denizalti=random.randint(36,140)
                hucumbot=random.randint(72,200)
                denizsinirihudutdevriyebotu=random.randint(72,200)
                mayinavlamavetaramagemisi=random.randint(33,60)
                amfibisavasgemisi=random.randint(150,250)
                askertasimagemisi=random.randint(150,250)
                ucakgemisi=random.randint(3,5)

                personel2=random.randint(75000,175000)
                avciucagi=random.randint(75,120)
                insansizhavaaraci=random.randint(10,20)
                nakliyesaldirihelikopteri=random.randint(50,150)
                bombardimanucagi=random.randint(20,75)
                nakliyeucagi=random.randint(20,75)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc
            
            elif ordutipi999=="Hava kuvvetleri":
                asker=random.randint(300000,1000000)
                tanklar=random.randint(50,150)
                zirhliaraclar=random.randint(50,120)
                alantoplari=random.randint(50,120)
                kundagimotorlutopcusistemleri=random.randint(30,120)
                coknamluluroketatar=random.randint(20,50)
                cekiliucaksavartoplari=random.randint(25,75)
                havasavunmasistemleri=random.randint(3,15)

                personel=random.randint(100000,250000)
                fırkateyn=random.randint(24,64)
                korvetn=random.randint(24,64)
                denizalti=48
                hucumbot=random.randint(24,72)
                denizsinirihudutdevriyebotu=random.randint(24,72)
                mayinavlamavetaramagemisi=random.randint(12,36)
                amfibisavasgemisi=random.randint(64,120)
                askertasimagemisi=random.randint(64,120)
                ucakgemisi=random.randint(1,3)

                personel2=random.randint(100000,350000)
                avciucagi=random.randint(250,750)
                insansizhavaaraci=random.randint(75,250)
                nakliyesaldirihelikopteri=random.randint(75,350)
                bombardimanucagi=random.randint(75,500)
                nakliyeucagi=random.randint(75,500)
                sonuc="""\n#####KARA KUVVETLERİ#####
                \tAsker: {}
                \tTank:  {}
                \tZırhlı Araçlar: {}
                \tAlan Topları: {}
                \tKundağı Motorlu Topçu Sistemleri: {}
                \tÇok Namlulu Roketatar: {}
                \tÇekili Uçaksavar Topları: {}
                \tHava Savunma Sistemleri: {}\n#####DENİZ KUVVETLERİ#####
                \tPersonel: {}
                \tFırkateyn: {}
                \tKorvetn: {}
                \tDenizaltı: {}
                \tHücumbot: {}
                \tDeniz Sınırı Hudut Devriye Botu: {}
                \tMayın Avlama ve Tarama Gemisi: {}
                \tAmfibi Savaş Gemisi: {}
                \tAsker Taşıma Gemisi: {}
                \tUçak Gemisi: {}\n#####HAVA KUVVETLERİ#####
                \tPersonel: {}
                \tAvcı Uçağı: {}
                \tİnsansız Hava Aracı: {}
                \tNakliye/Saldırı Helikopteri: {}
                \tBombardıman Uçağı: {}
                \tNakliye Uçağı: {}
                """.format(asker,tanklar,zirhliaraclar,alantoplari,kundagimotorlutopcusistemleri,coknamluluroketatar,cekiliucaksavartoplari,havasavunmasistemleri,personel,fırkateyn,korvetn,denizalti,hucumbot,denizsinirihudutdevriyebotu,mayinavlamavetaramagemisi,amfibisavasgemisi,askertasimagemisi,ucakgemisi,personel2,avciucagi,insansizhavaaraci,nakliyesaldirihelikopteri,bombardimanucagi,nakliyeucagi)
                return sonuc

def ulke_function_issizlik():
    kosul=ulke_combobox_vericekici_gelismislik.get()
    if kosul=="Çok kötü":
        a=random.randint(15,25)
        sonuc="""İşsizlik Oranı: %{}""".format(a)
        return sonuc
    elif kosul=="Kötü":
        a=random.randint(10,15)
        sonuc="""İşsizlik Oranı: %{}""".format(a)
        return sonuc
    elif kosul=="İyi":
        a=random.randint(4,8)
        sonuc="""İşsizlik Oranı: %{}""".format(a)
        return sonuc
    elif kosul=="Çok iyi":
        a=random.randint(1,3)
        sonuc="""İşsizlik Oranı: %{}""".format(a)
        return sonuc

def ulke_function_enflasyon_orani():
    kosul=ulke_combobox_vericekici_refah.get()
    if kosul=="Halk açlık sınırında":
        a=random.randint(20,25)
        sonuc="Enflasyon Oranı: %{}".format(a)
        return sonuc
    elif kosul=="Yetersiz":
        a=random.randint(10,19)
        sonuc="Enflasyon Oranı: %{}".format(a)
        return sonuc
    elif kosul=="Orta Düzey":
        a=random.randint(5,9)
        sonuc="Enflasyon Oranı: %{}".format(a)
        return sonuc
    elif kosul=="Çok iyi":
        a=random.randint(1,4)
        sonuc="Enflasyon Oranı: %{}".format(a)
        return sonuc

def ulke_function_baslica_ihracatveithalat_kalemleri_ve_urunler():
    a1=random.choice(veritabani_ulke_baslica_ihracatveithalatkalemleri)
    veritabani_ulke_baslica_ihracatveithalatkalemleri.remove(a1)

    a2=random.choice(veritabani_ulke_baslica_ihracatveithalatkalemleri)
    veritabani_ulke_baslica_ihracatveithalatkalemleri.remove(a2)

    a3=random.choice(veritabani_ulke_baslica_ihracatveithalatkalemleri)
    veritabani_ulke_baslica_ihracatveithalatkalemleri.remove(a3)

    a4=random.choice(veritabani_ulke_baslica_ihracatveithalatkalemleri)
    veritabani_ulke_baslica_ihracatveithalatkalemleri.remove(a4)

    a5=random.choice(veritabani_ulke_baslica_ihracatveithalatkalemleri)
    veritabani_ulke_baslica_ihracatveithalatkalemleri.remove(a5)

    a6=random.choice(veritabani_ulke_baslica_ihracatveithalatkalemleri)
    veritabani_ulke_baslica_ihracatveithalatkalemleri.remove(a6)

    b1=random.choice(veritabani_ulke_baslica_ihracveithalurunler)
    veritabani_ulke_baslica_ihracveithalurunler.remove(b1)
    
    b2=random.choice(veritabani_ulke_baslica_ihracveithalurunler)
    veritabani_ulke_baslica_ihracveithalurunler.remove(b2)
    
    b3=random.choice(veritabani_ulke_baslica_ihracveithalurunler)
    veritabani_ulke_baslica_ihracveithalurunler.remove(b3)
    
    b4=random.choice(veritabani_ulke_baslica_ihracveithalurunler)
    veritabani_ulke_baslica_ihracveithalurunler.remove(b4)
    
    b5=random.choice(veritabani_ulke_baslica_ihracveithalurunler)
    veritabani_ulke_baslica_ihracveithalurunler.remove(b5)
    
    b6=random.choice(veritabani_ulke_baslica_ihracveithalurunler)
    veritabani_ulke_baslica_ihracveithalurunler.remove(b6)
    
    sonuc="""Başlıca İhracat ve İthalat Kalemleri\tBaşlıca İhracat ve İthalat Ürünleri\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}""".format(a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6)
    return sonuc

def ulke_function_kurulus_tarihi():
    a=random.randint(1,3)
    if a==1:
        #köklü bir ülke
        b=random.randint(300,1300)
        sonuc="Kuruluş Tarihi: {} ".format(b)
        return sonuc
    elif a==2:
        #orta ülke
        b=random.randint(1301,1800)
        sonuc="Kuruluş Tarihi: {} ".format(b)
        return sonuc
    elif a==3:
        #yeni ülke
        b=random.randint(1801,2000)
        sonuc="Kuruluş Tarihi: {} ".format(b)
        return sonuc

def ulke_function_sehir_sayisi():
    a=random.randint(10,70)
    sonuc="Şehir Sayısı: {}".format(a)
    return sonuc

def ulke_function_gini():
    kosul=ulke_combobox_vericekici_refah.get()
    if kosul=="Halk açlık sınırında":
        a=(random.randint(75,99))/100
        a=round(a,2)
        ige=(random.randint(37,55))/100
        ige=round(ige,2)
        sonuc="Gini Katsayısı: {} (Kötü) \nİnsani Gelişme Endeksi: {} (Çok Kötü)".format(a,ige)
        return sonuc
    elif kosul=="Yetersiz":
        a=(random.randint(50,75))/100
        a=round(a,2)
        ige=(random.randint(56,60))/100
        ige=round(ige,2)
        sonuc="Gini Katsayısı: {} (Orta) \nİnsani Gelişme Endeksi: {} (Kötü)".format(a,ige)
        return sonuc
    elif kosul=="Orta Düzey":
        a=(random.randint(25,50))/100
        a=round(a,2)
        ige=(random.randint(61,80))/100
        ige=round(ige,2)
        sonuc="Gini Katsayısı: {} (İyi) \nİnsani Gelişme Endeksi: {} (İyi)".format(a,ige)
        return sonuc
    elif kosul=="Çok iyi":
        a=(random.randint(1,25))/100
        a=round(a,2)
        ige=(random.randint(81,99))/100
        ige=round(ige,2)
        sonuc="Gini Katsayısı: {} (Çok İyi) \nİnsani Gelişme Endeksi: {} (Çok İyi)".format(a,ige)
        return sonuc


def ulke_yazdir_buton():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','ulke.txt') 
    a="a"
    file = open(desktop,a) # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
    veri1=ulke_function_yonetim()
    veri2=ulke_function_ekonomiksistem()
    veri3=ulke_function_refah()
    veri4=ulke_function_federasyon()
    veri5=ulke_function_gelismislik()
    veri6=ulke_function_zenginlik()
    veri7=ulke_function_isim()
    veri8=ulke_function_devletyardimlari()
    veri9=ulke_function_egitim()
    veri10=ulke_function_nufusartishizi()
    veri11=ulke_function_nufus()
    veri12=ulke_function_iklim()
    veri13=ulke_function_yuzolcum()
    veri14=ulke_function_karaparcasi()
    veri15=ulke_function_kaynakdagilimi()
    veri16=ulke_function_orduenvanteri()
    veri17=ulke_function_issizlik()
    veri18=ulke_function_enflasyon_orani()
    veri19=ulke_function_baslica_ihracatveithalat_kalemleri_ve_urunler()
    veri20=ulke_function_kurulus_tarihi()
    veri21=ulke_function_sehir_sayisi()
    veri22=ulke_function_gini()




    veri30=function_guzel_bastirmak()






    file.write(veri30+"\n")
    file.write(veri1+"\n")
    file.write(veri2+"\n")
    file.write(veri3+"\n")
    file.write(veri4+"\n")
    file.write(veri5+"\n")
    file.write(veri6+"\n")
    file.write(veri7+"\n")
    file.write(veri8+"\n")
    file.write(veri9+"\n")
    file.write(veri17+"\n")
    file.write(veri18+"\n")
    file.write(veri19+"\n")
    file.write(veri20+"\n")
    file.write(veri21+"\n")
    file.write(veri22+"\n")


    file.write(veri10+"\n")
    file.write(veri11+"\n")
    file.write(veri12+"\n")
    file.write(veri13+"\n")
    file.write(veri14+"\n")
    file.write(veri15+"\n")
    file.write(veri16+"\n")
    

    file.write(veri30+"\n")



    file.close()

def ulke_rastgeleyazdir_buton():
    #Yönetim
    atama=random.randint(0,9)
    ulke_combobox_yonetim.current(atama)
    #Ekonomik sistem
    atama=random.randint(0,5)
    ulke_combobox_piyasaserbestligi.current(atama)
    #Refah
    atama=random.randint(0,3)
    ulke_combobox_refah.current(atama)
    #Federasyon
    atama=random.randint(0,1)
    ulke_combobox_federasyon.current(atama)
    #Gelişmişlik
    atama=random.randint(0,4)
    ulke_combobox_gelismislik.current(atama)
    #GSYİH
    atama=random.randint(0,4)
    ulke_combobox_zenginlik.current(atama)
    #Ülke ismi
    atama=random.randint(0,3)
    ulke_combobox_isim.current(atama)
    #Devlet yardımları
    atama=random.randint(0,4)
    ulke_combobox_sosyaldevlet.current(atama)
    #Eğitim
    atama=random.randint(0,3)
    ulke_combobox_egitim.current(atama)
    #Nüfus artış hızı
    atama=random.randint(0,4)
    ulke_combobox_nufusartishizi.current(atama)
    #Nüfus
    atama=random.randint(0,4)
    ulke_combobox_kalabaliklik.current(atama)
    #İklim
    atama=random.randint(0,2)
    ulke_combobox_iklim.current(atama)
    #Yüzölçüm
    atama=random.randint(0,2)
    ulke_combobox_yuzolcum.current(atama)
    #Karaparçası
    atama=random.randint(0,2)
    ulke_combobox_karaparcasi.current(atama)
    #Kaynak dağılımı
    atama=random.randint(0,3)
    ulke_combobox_kaynakdagilimi.current(atama)
    #Nüfus dağılımı
    atama=random.randint(0,1)
    ulke_combobox_nufusdagilimi.current(atama)
    #Ordu uzmanlığı
    atama=random.randint(0,2)
    ulke_combobox_ordutipi.current(atama)
    #Ordu harcaması
    atama=random.randint(0,4)
    ulke_combobox_orduharcaması.current(atama)
    #Ordu envanteri
    atama=random.randint(0,1)
    ulke_combobox_orduenvanteri.current(atama)


################################################################################################################################################################
################################################################################################################################################################
"""BUTONLAR"""
################################################################################################################################################################
################################################################################################################################################################

ulke_yazdir_buton=tk.Button(tab7,text="Yazdır(Not Defteri)",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=5,font=("Arial",11,"bold"),height=2,width=32,command=ulke_yazdir_buton).place(x=10,y=400)

ulke_rastgeleyazdir_buton=tk.Button(tab7,text="Rastgele Seç",background=background101,fg="white",activebackground="snow",activeforeground="red2",bd=5,font=("Arial",11,"bold"),height=2,width=32,command=ulke_rastgeleyazdir_buton).place(x=10,y=480)


################################################################################################################################################################
################################################################################################################################################################
"""GELİŞTİRİCİNİN NOTLARI"""
################################################################################################################################################################
################################################################################################################################################################

def kapatmak_istiyor_musun():
    if messagebox.askokcancel("", "Programı kapatmak istiyor musunuz?"):
        anapencere.destroy()
anapencere.protocol("WM_DELETE_WINDOW", kapatmak_istiyor_musun)

a100=ttk.Label(tab1,text="Ne için kullanılır?",style="BW.TLabel").place(x=10,y=20)
a101=ttk.Label(tab1,text="\tOlaya yönelik hikâye yazarlığında yahut karakterlerin çok fazla olduğu distopik metinlerde ve bir seri yazılacak ise ihtiyaç duyulan karakterleri,isimleri,ülkeleri hızlıca türetir. Türetmek için gereken veritabanı programın \niçine gömülüdür. Veritabanını genişletmek veya değiştirmek için henüz bir seçenek tanımlanmamıştır.",background="gray22",foreground="gray80",font=("Arial",10,"bold")).place(x=10,y=50)
a102=ttk.Label(tab1,text="Türetilen İsimlerin Özgünlüğü",style="BW.TLabel").place(x=10,y=100)
a103=ttk.Label(tab1,text="\tİsimler, yüzlerce heceden oluşan bir listeden rastgele seçilerek oluşturulur. Hece sayısı burada devreye girer. Programın türettiği isimlerin birçoğu daha önce hiçbir yerde kullanılmamış olacaktır. Çünkü; Veritabanındaki \nhecelerin tesadüfen yanyana gelerek varolan bir kelimenin türetilmesi ihtimali çok düşüktür. Türetmek istediğiniz ismin hece sayısı arttıkça, türetebileceğiniz kelime sayısı azalırken ismin özgünlüğü artmaktadır. İki hece seçilmesi \ndurumunda türetilebilecek isim sayısı yaklaşık 74 faktöriyeldir. Beş hece seçilmesi durumunda türetilebilecek isim sayısı yaklaşık 30 faktöriyeldir.",background="gray22",foreground="gray80",font=("Arial",10,"bold")).place(x=10,y=130)
#a104=ttk.Label(tab1,text="Karakter Türetici ve Ülke Türetici",style="BW.TLabel").place(x=10,y=200)
#a105=ttk.Label(tab1,text="\t",background="gray22",foreground="gray80",font=("Arial",10,"bold")).place(x=10,y=240)

b100=ttk.Label(tab4,text="Öneri ve şikayetleriniz için:",style="BW.TLabel").place(x=10,y=20)
b101=tk.Text(tab4,width=27,height=1)
b101.place(x=280,y=21)
b101.insert(tk.INSERT,"burakturkertugenn@gmail.com")
b101.configure(state="disabled")
b102=ttk.Label(tab4,text="""\nVersiyon: 1.0 
Çıkış tarihi: 27 Mart 2020
""",style="BW.TLabel").place(x=10,y=50)

c100=ttk.Label(anapencere,text="Developer: Burak Türker Tügen", foreground="gray40",font=("Arial",10,"bold")).place(x=800,y=15)
c101=ttk.Label(anapencere,text="Versiyon: 1.0",foreground="gray40",font=("Arial",10,"bold")).place(x=50,y=15)




anapencere.mainloop()


    
