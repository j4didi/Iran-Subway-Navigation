from collections import namedtuple,

Station = namedtuple("Station", ["fa", "en"])

#line1

tajrish = Station("تجریش", "Tajrish")
qeytariyeh = Station("قیطریه", "Qeytariyeh")
shahid_sadr = Station("شهید صدر", "Shahid Sadr")
gholhak = Station("قلهک", "Gholhak")
dr_shariati = Station("دکتر شریعتی", "Dr. Shariati")
mirdamad = Station("میرداماد", "Mirdamad")
shahid_haghani = Station("شهید حقانی", "Shahid Haghani")
shahid_hemmat = Station("شهید همت", "Shahid Hemmat")
mosalla_khomeini = Station("مصلی امام‌خمینی", "Mosalla Imam Khomeini")
shahid_beheshti = Station("شهید بهشتی", "Shahid Beheshti")
shahid_mofatteh = Station("شهید مفتح", "Shahid Mofatteh")
shohada_7_tir = Station("شهدای هفتم تیر", "Shohada-ye Haftom-e Tir")
ayatollah_taleghani = Station("آیت‌الله طالقانی", "Ayatollah Taleghani")
darvazeh_dowlat1 = Station("دروازه دولت", "Darvazeh Dowlat")
saadi = Station("سعدی", "Saadi")
imam_khomeini1 = Station("امام‌خمینی", "Imam Khomeini")
panzdah_khordad = Station("پانزده‌خرداد", "Panzdah Khordad")
khayyam = Station("خیام", "Khayyam")
meydan_mohammadiyeh = Station("میدان محمدیه", "Meydan-e Mohammadiyeh")
shoosh = Station("شوش", "Shoosh")
payane_jonub = Station("پایانه جنوب", "Payaneh Jonoub Terminal")
shahid_bokharaei = Station("شهید بخارایی", "Shahid Bokharaei")
aliabad = Station("علی‌آباد", "Ali Abad")
javanmard_ghasab = Station("جوانمرد قصاب", "Javanmard-e Ghassab")
shahr_rey1 = Station("شهرری", "Shahr-e Rey")
palayeshgah = Station("پالایشگاه", "Palayeshgah")
shahed_baqershahr = Station("شاهد‑باقرشهر", "Shahed‑Bagher Shahr")
haram_emam = Station("حرم مطهر امام‌خمینی", "Haram-e Motahhar Emam Khomeini")
kahrizak = Station("کهریزک", "Kahrizak")
shahr_aftab = Station("<UNK> <UNK> <UNK>", "Namayeshgah-e Shahr-e Aftab (Shahr-e Aftab Exhibition")
vavan = Station("واوان", "Vavan")
imam_khomeini_airport = Station("فرودگاه امام خمینی", "Imam Khomeini Airport")
parand = Station("پرند", "Parand")

# line2

farhangsara = Station("فرهنگ‌سرا", "Farhangsara")
tehranpars = Station("تهرانپارس", "Tehranpars")
shahid_bagheri = Station("شهید باقری", "Shahid Bagheri")
elm_sanat = Station("دانشگاه علم و صنعت", "Elm‑o‑Sanat University")
sarsabz = Station("سرسبز", "Sarsabz")
janbazan = Station("جانبازان", "Janbazan")
fadak = Station("فدک", "Fadak")
sabalan = Station("سبلان", "Sabalan")
shahid_madani = Station("شهید مدنی", "Shahid Madani")
emam_hossein = Station("امام حسین", "Imam Hossein")
darvazeh_shemiran = Station("دروازه شمیران", "Darvazeh Shemiran")
baharestan = Station("بهارستان", "Baharestan")
mellat = Station("ملت", "Mellat")
hasanabad = Station("حسن‌آباد", "Hasan Abad")
daneshgah_emam_ali = Station("دانشگاه امام علی", "Daneshgah‑e Emam Ali (Imam Ali University")
meydan_horr = Station("میدان حر", "Meydan‑e Horr")
shahid_navvab = Station("شهید نواب صفوی", "Shahid Navvab‑e Safavi")
shademan = Station("شادمان", "Shadman")
daneshgah_sharif = Station("دانشگاه شریف", "Daneshgah‑e Sharif (Sharif University)")
tarasht = Station("طرشت", "Tarasht")
tehran_sadeghieh = Station("تهران (صادقیه)", "Tehran (Sadeghieh)")

#line3

ghaem = Station("قائم", "Ghaem")
shahid_mahallati = Station("شهید محلاتی", "Shahid Mahallati")
aghdasiyeh = Station("اقدسیه", "Aghdasiyeh")
nobonyad = Station("نوبنیاد", "Nobonyad")
hoseinabad = Station("حسین‌آباد", "Hossein Abad")
heravi = Station("میدان هروی", "Meydan-e Heravi")
shahid_zeynoddin = Station("شهید زین‌الدین", "Shahid Zeynoddin")
khajeh_ansari = Station("خواجه عبدالله انصاری", "Khajeh Abdollah‑e Ansari")
shahid_sayyad = Station("شهید صیاد شیرازی", "Shahid Sayyad‑e Shirazi")
shahid_ghoddoosi = Station("شهید قدوسی", "Shahid Ghodousi")
sohrevardi = Station("سهروردی", "Sohrevardi")
mirzaye_shirazi = Station("میرزای شیرازی", "Mirza-ye Shirazi")
meydan_valiasr = Station("میدان حضرت ولی‌عصر", "Meydan‑e Hazrat-e Vali Asr")
teatr_shahr = Station("تئاتر شهر", "Teatr‑e Shahr")
moniriyeh = Station("منیریه", "Moniriyeh")
mahdieh = Station("مهدیه", "Mahdiyeh")
meydan_jahad = Station("میدان جهاد", "Meydan‑e Jahad")
rahahan = Station("راه‌آهن", "Rahahan (Central Railway Station")
javadiyeh = Station("جوادیه", "Javadiyeh")
zamzam = Station("زم‌زم", "ZamZam")
shariati_town = Station("شهرک شریعتی", "Shahrak‑e Shari'ati")
abdolabad = Station("عبدل‌آباد", "Abdol Abad")
nematabad = Station("نعمت‌آباد", "Ne'mat Abad")
azadegan = Station("آزادگان", "Azadegan")

#line4

kolahdooz = Station("شهید کلاهدوز", "Shahid Kolahdooz")
niroohavaei = Station("نیروی هوایی", "Nirooye Havaei")
nabard = Station("نبرد", "Nabard")
piroozi = Station("پیروزی", "Piroozi")
ebnesina = Station("ابن سینا", "Ebn‑e Sina")
meydan_shohada = Station("میدان شهدا", "Meydan‑e Shohada")
darvazeh_shemiran = Station("دروازه شمیران", "Darvazeh Shemiran")
ferdowsi = Station("فردوسی", "Ferdowsi")
meydan_enghelaab = Station("میدان انقلاب اسلامی", "Meydan‑e Enghelab")
towhid = Station("توحید", "Towhid")
dr_habibollah = Station("دکتر حبیب‌الله", "Doctor Habibollah")
ostad_moein = Station("استاد معین", "Ostad Moein")
meydan_azadi = Station("میدان آزادی", "Meydan‑e Azadi")
bimeh = Station("بیمه", "Bimeh")
shahrak_ekbatan = Station("شهرک اکباتان", "Shahrak‑e Ekbatan")
eram_sabz = Station("ارم سبز", "Eram‑e Sabz")
allameh_jafari = Station("علامه جعفری", "Allameh Jafari")
ayatollah_kashani = Station("آیت الله کاشانی", "Ayatollah Kashani")
chaharbagh = Station("چهارباغ", "Chaharbagh")
mehrabad_airport12 = Station("پایانه 1 و 2 فرودگاه مهرآباد", "Mehrabad Airport Terminal 1&2")
mehrabad_airport46 = Station("پایانه 4 و 6 فرودگاه مهرآباد", "Mehrabad Airport Terminal 4&6")

#line5

varzeshgah_azadi = Station("ورزشگاه آزادی", "Varzeshgah‑e Azadi (Azadi Sport Complex")
chitgar = Station("چیتگر", "Chitgar")
irankhodro = Station("ایران خودرو", "Iran Khodro")
vardavard = Station("وردآورد", "Vardavard")
garmdareh = Station("گرم‌دره", "Garmdarreh")
atmosfer = Station("اتمسفر", "Atmosfer")
karaj = Station("کرج", "Karaj")
mohammadshahr = Station("محمدشهر", "Mohammad Shahr")
golshahr = Station("گلشهر", "Golshahr")
shahid_soleimani = Station("شهید قاسم سلیمانی", "Shahid Qasem Soleimani")

#line6

haram_abdolazim = Station("حرم حضرت عبدالعظیم", "Haram-e Hazrat-e Abdolazim")
meydan_abdolazim = Station("میدان حضرت عبدالعظیم", "Meydan-e Hazrat Abdolazim")
ebn_babviyeh = Station("ابن بابویه", "Ebn-e Babviyeh")
cheshmeh_ali = Station("چشمه علی", "Cheshmeh Ali")
dolatabad = Station("دولت‌آباد", "Dolatabad")
kianshahr = Station("کیان‌شهر", "Kian Shahr")
besat = Station("بعثت", "Be'sat")
shahid_rezaei = Station("شهید رضایی", "Shahid Rezaei")
amirkabir = Station("امیرکبیر", "Amir Kabir")
meydan_khorasan = Station("میدان خراسان", "Meydan-e Khorasan")
shohadaye_17_sharivar = Station("شهدای هفده شهریور", "Shohada-ye Hefdah-e Sharivar")
sarbaz = Station("ُسرباز", "Sarbaz")
bahar_shiraz = Station("بهار شیراز (بیمارستان خانواده)", "Bahar Shiraz (Khanevadeh Hospital)")
shahid_nejatollahi = Station("شهید نجات اللهی", "Shahid Nejatollahi")
boostan_laleh = Station("بوستان لاله", "Boostan-e Laleh (Laleh Park)")
karegar= Station("کارگر", "Karegar")
daneshgah_modarres = Station("دانشگاه تربیت مدرس", "Daneshgah‑e Tarbiat Modarres (Tarbiat Modarres University)")
shahrak_azmayesh = Station("شهرک آزمایش", "Shahrak‑e Azmayesh")
marzdaran = Station("مرزداران", "Marzdaran")
yadegar_emam = Station("یادگار امام", "Yadegar‑e Emam")
shahid_ashrafiesfahani = Station("شهید اشرفی اصفهانی", "Shahid Ashrafi Esfahani")
shahid_sattari = Station("شهید ستاری", "Shahid Sattari")
shahrziba = Station("شهر زیبا", "Shar-e Ziba")
shahran = Station("شهران", "Shahran")
shohada_kan = Station("شهدای کن", "Shohada-ye Kan")
kouhsar = Station("کوهسار", "Kouhsar")

#line7

meydan_ketab = Station("میدان کتاب", "Meydan‑e Ketab")
shahid_dadman = Station("شهید دادمان", "Shahid Dadman")
meydan_sanat = Station("میدان صنعت", "Meydan‑e Sanat")
borj_milad = Station("برج میلاد تهران", "Borj‑e Milad Tehran (Tehran Milad Tower)")
boostan_goftogou = Station("بوستان گفتگو", "Boostan‑e Goftogoo (Goftogoo Park)")
modafean_salamat = Station("مدافعان سلامت", "Modafean-e Salamat")
roudaki = Station("رودکی", "Roudaki")
komeyl = Station("کمیل", "Komeyl")
beryanak = Station("بریانک", "Beryanak")
helal_ahmar = Station("هلال‌احمر", "Helal Ahmar")
mahdiyeh = Station("مهدیه", "Mahdiyeh")
molavi = Station("مولوی", "Molavi")
meydan_ghiam = Station("میدان قیام", "Meydan‑e Ghiam")
chehel_tan = Station("چهل‌تن دولاب", "Chehel Tan‑e Doolab")
ahang = Station("آهنگ", "Ahang")
basij = Station("بسیج", "Basij")
varzeshgah_takhti = Station("ورزشگاه تختی", "Varzeshgah-e Takhti (Takhti Sport Complex)")

line1 = [
    tajrish, qeytariyeh, shahid_sadr, gholhak, dr_shariati,
    mirdamad, shahid_haghani, shahid_hemmat, mosalla_khomeini,
    shahid_beheshti, shahid_mofatteh, shohada_7_tir, ayatollah_taleghani,
    darvazeh_dowlat1, saadi, imam_khomeini1, panzdah_khordad,
    khayyam, meydan_mohammadiyeh, shoosh, payane_jonub,
    shahid_bokharaei, aliabad, javanmard_ghasab, shahr_rey1,
    palayeshgah, shahed_baqershahr, haram_emam, kahrizak
]
line1_2 = [
    shahed_baqershahr,shahr_aftab, vavan, imam_khomeini_airport
]
line2 = [
    tehran_sadeghieh, tarasht, daneshgah_sharif, shademan,
    shahid_navvab, meydan_horr, daneshgah_emam_ali, hasanabad,
    imam_khomeini1, mellat, baharestan, darvazeh_shemiran, emam_hossein,
    shahid_madani, sabalan, fadak, janbazan,sarsabz, elm_sanat,
    shahid_bagheri, tehranpars, farhangsara
]
line3 = [
    ghaem, shahid_mahallati, aghdasiyeh, nobonyad, hoseinabad, heravi,
    shahid_zeynoddin, khajeh_ansari, shahid_sayyad, shahid_ghoddoosi,
    sohrevardi, shahid_beheshti, mirzaye_shirazi, meydan_jahad, meydan_valiasr,
    teatr_shahr, moniriyeh, mahdieh, rahahan, javadiyeh, zamzam,
    shariati_town, abdolabad, nematabad, azadegan
]
line4 = [
    kolahdooz,niroohavaei,nabard, piroozi, ebnesina,
    meydan_shohada, darvazeh_shemiran, darvazeh_dowlat1, ferdowsi,
    teatr_shahr, meydan_enghelaab, towhid, shademan, dr_habibollah,
    ostad_moein, meydan_azadi, bimeh, shahrak_ekbatan, eram_sabz,
    allameh_jafari, ayatollah_kashani, chaharbagh
]
line4_2 = [
    bimeh, mehrabad_airport12, mehrabad_airport46
]
line5 = [
    tehran_sadeghieh, eram_sabz, varzeshgah_azadi, chitgar, irankhodro,
    vardavard, garmdareh, atmosfer, karaj, mohammadshahr, golshahr, shahid_soleimani
]
line6 = [
    kouhsar, shohada_kan, shahran, shahrziba, ayatollah_kashani,
    shahid_sattari, shahid_ashrafiesfahani, yadegar_emam, marzdaran,
    shahrak_azmayesh, daneshgah_modarres, karegar, boostan_laleh,
    meydan_valiasr, shahid_nejatollahi, shohada_7_tir, bahar_shiraz,
    sarbaz, emam_hossein, meydan_shohada, amirkabir, shohadaye_17_sharivar,
    meydan_khorasan, shahid_rezaei, besat, kianshahr, dolatabad, cheshmeh_ali,
    ebn_babviyeh, meydan_abdolazim, haram_abdolazim
]
line7 = [
    varzeshgah_takhti, basij, ahang, chehel_tan, shohadaye_17_sharivar,
    meydan_ghiam, molavi, meydan_mohammadiyeh, mahdiyeh, helal_ahmar,
    beryanak, komeyl, roudaki, shahid_navvab, towhid, modafean_salamat,
    daneshgah_modarres, boostan_goftogou, borj_milad, meydan_sanat,
    shahid_dadman, meydan_ketab
]