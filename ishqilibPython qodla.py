

# son=int(input("son kiriting = "))
# if son>0:
#     print(son,"musbat")
# else:
#     print(son,"manfiiy")
#2- masala
# yosh=int(input("yoshingizni kiriting = "))
# if yosh >=18:
#     print(f"sizning yoshingiz {yosh}, da siz voyaga yetgansiz")
# else:
#     print(f"sizning yoshingiz {yosh} , da siz voyaga yetmagan siz!!!")
#3- masala
# juf=int(input("son yozing = "))
# if juf % 2 == 0 :
#     print(f"bu son {juf}, juft ")
# else:
#     print(f"bu son {juf}, toq ")
#4- masala 
# z=int(input("1- son = "))
# x=int(input("2- son = "))
# y=int(input("3- son = "))
# if z > x > y:
#     print(f"3 ta sondan kattasi={z}")
# elif z < x > y:
#     print(f"3 ta sondan kattasi={x}")
# elif z < x < y:
#     print(f"3 ta sondan kattasi={y}")
# 5- masala
# bal= int(input("Ball ni kiriting = "))
# if bal >= 86 :
#     print(f"sizning ballingiz {bal} , JUDA ALO")
# elif bal >= 54:
#     print(f"sizning balingiz {bal} , O'RTA QONIQARLI")
# elif bal <= 53:
#     print(f"sizning balingiz {bal} , JUDA PAST QONIQARSIZ ")
# else:
#     print(f"bunaqa baxo yo'q {bal} !!!")
#6 - masala
# kun=input("Bugun haftaning nechanchi kuni = ")
# match kun:
#     case "dushanba" | "seshanba" | "chorshanba" | "juma":
#         print(f"Bugun {kun}, haftaning ish kuni")
#     case "shanba" | "yakshanba":
#         print(f"Bugun {kun} , haftaning dam olish kuni ")
#     case _ :
#         print("bunaqa kun yoq")

# matn1 = 'Abdulla'
# matn2 = "Abdulla"

# matn3 = '''Abdulla'''
# matn4 = """Abdulla"""


# print(matn1)
# print(matn2)
# print(matn3)
# print(matn4)


# soz="shohjahon"
# print(soz[0:4])
#slicing = bu kesib olmoq

# ism = "shohjahon"
# fam = "baxtiyorov"
# print(f"{fam} {ism}, sizning isim familiyangiz")







# ist=int(input("tana haroratingiz nechi? = "))
# if ist <=35 and ist >=20:
#     print(f"sizning tana haroratingiz,{ist} gradus tushib ketgan ,")
# elif ist==36:
#     print(f"sizning tana haroratingiz,{ist} gradus normal  ,")
# elif ist>36 and ist<=45:
#     print(f"sizning tana haroratingiz,{ist} gradus ko'tarilib ketgan ,")
# else:
#     print("hato harorat kiritildi")

# s=input("salom yozing= ").upper()
# print(F"{s}")


# s=input("salom yozing= ").lower()
# print(F"{s}")


# s=input("salom yozing= ").capitalize()
# print(F"{s}")
# shoh='shohjaxon,Baxtiyorov,Rustamovich'
# print(shoh.replace('shohjaxon','mrRobot',2))
# avvalgini yangisiga almashtiradi

# ism="shohjaxon"
#    012345678
# print(ism.find("x"))


# count -nechta shu soz borligini sanaydi "olma,olma,olma" == 3


# startswithe - sozni boshini tekshiradi "python"
# (py)true
# (thon)false
#
# fruits = ['apple','banana','orange']
# print("***".join(fruits))----->"***" bilan sozlarni birlashtirib beradi

# s="salom"
# print(s.isalpha())true
# s2="salom123"
# print(s.isupper())false
# s3=""
# print(s.islower())false




#
#
# text = "a,b,c,d,e"
# result = "|".join((parts := text.split(","))[::2])
# print(result)
# print(f"Parts: {parts}")

#
# text = "a-b-c-d-e"
# parts = text.split("-")
# result = parts[1:4]
# print("|".join(result))

# text = "Hello World Hello"
# result = text.replace("Hello", "Hi").replace("World", "Python")
# print(result)

# text = "  Hello World Python Programming  "
# result = (cleaned := text.strip()).upper().replace("WORLD", "JAVA").split()[1:3]
# final = "|".join(result).lower()
# print(final)
# print(f"Cleaned: '{cleaned}'")


# text1 = "Hello"
# text2 = "Hello123"
# print(text1.isalpha())
#
#
# text = "Hello World"
# result = text.swapcase()
# print(result)

# text = "Hello World Python"
# result = text.split()
# print(result)

# text = "  Python  "
# result = text.strip().upper().startswith("PYTHON")
# print

#
# text = "   Hello World   "
# result = text.strip()
# print(f"'{result}'")


#
# text = "Hello World Hello"
# result = text.find("World")
# print(result)

# words = ['Hello', 'World', 'Python']
# result = " ".join(words)
# print(result)

# text = "Hello World "
# result1 = text.endswith("World")
# result2 = text.endswith("Hello")
# print(result1, result2)


#
# text = "  Python  "
# result = (cleaned := text.strip()).upper().startswith("PYTHON") and (is_lower := cleaned.islower()) == False
# print(result, is_lower)


# text = "hello world python"
# result = text.title()
# print(result)

#
# text = "Hello World"
# result = text.replace("World", "Python")
# print(result)


# text = "Python123"
# result = (is_alnum := text.isalnum()) and not (is_digit := text.isdigit()) and not (is_alpha := text.isalpha())
# print(result, is_alnum, is_digit, is_alpha)


#
# a=int(input("a = "))
# b=int(input("b = "))
# print(f"{a}+{b}={a+b}")

# i=int(input("uzunligi = "))
# w=int(input("enini toping  = "))
# print(f"{i}*{w} = {i*w}")
#
# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))
# print(f"{x}+{y}+{z}={x+y+z/3}")

# a=int(input("a tomoni = "))
# b=int(input("b tomoni = "))
# print(f"{2*(a+b)}")

# h=int(input("soatni kiriting = "))
# m=int(input("daqiqani kiriting = "))
# print(f"{h*60+m}")


# usd=int(input("pul miqdri ="))
# usd=usd*12500
# print(f"{sum}")


# a=int(input("a="))
# b=int(input("b="))
# print(a-b)
#
# x=int(input("son="))
# n=int(input("daraja="))
# print(f"{x**n}")

# a=int(input("a="))
# b=int(input("b="))
# print(f"{a//b}")


# a=int(input("son="))
# b=int(input("son= "))
# print(b,a)

# n=int(input("ijara= "))
# oy=int(input("oy= "))
# print(f"{n/oy}")

# d=int(input("masofa="))
# v=int(input("vaqt = "))
# print(f"{d/v}

# orin=int(input("orni = "))
# yolovchi=int(input("yolovchi = "))
# print(f"{yolovchi%orin}")

# d=int(input("100kmda necha litr yoqilgi = "))
# m=int(input("masofani kiriting = "))
# print(f"{d*m/100}")


# oylik=int(input("oylik="))
# brutto=int(input("brutto= "))
# print(f"{oylik/brutto}*(1-0.12)")

# n=int(input("necha som= "))
# kun=input("necha kun kechikdi = ")
# print(n+kun*0.001)

# m=int(input("maxsulot narxi = "))
# n=int(input("necha % chegirma = "))
# print(f"{m*n/100}")

#
# P=int(input("p="))
# r=int(input("r="))
# t=int(input("t="))
# print(f"{P*r/100*t}")

# 9. Ovqat retsepti miqdorini oshirish
# base_qty = float(input("Base ingredient miqdorini grammda kiriting (4 kishi uchun): "))
# people = int(input("Nechta kishi uchun hisoblash kerak? "))
#
# per_person = base_qty / 4
# needed = per_person * people
#
# print(f"{people} kishi uchun kerakli ingredient miqdori: {needed} gramm")
#
#
# # 10. Choyxona choyi uchun tip
# bill = float(input("Hisob-kitob summasini kiriting (so'mda): "))
#
# tip = bill * 0.10
# total = bill + tip
#
# print(f"Jami summa (10% tip qo‘shilganda): {total} so‘m")
#
# sh=input("Harid turi = ").lower().strip()
# match sh:
#     case  "iphone"| "noutbook" | "samsung"| "realme"|"infinix"|"redmi":
#         print("sizga 50% chegirma")
#     case _:
#         print("siz uchun kelishilgan holda ")




# ins=input("instagram username kiriting = ")
# input("y/n = ")
# match ins:
#     case "shohjahon"|"sirojbek"|"malohat"|"egobee":
#         print(f"Password = {ins}1234")
#     case _:
#         print(f"natija = PAROL TOPILMADI ")



# eg="python"
# print(eg.startswith("py"))


# vir=input("auto/mexanik = ")
# ism=input("ismingiz=")
# input("y/n = ")
# match vir:
#     case 'auto':
#         print("siz tayyorsiz")
#     case "mxanik":
#         print("1daqiqa kuting")
#     case _:
#         print("virus yoq ")





# import math
# sqrt - ildizi kvadrat ildizi
# pow - daraja x sonni y ga oshiradi

# print(math.pow(2,10))

# print(math.sqrt(16))

# s=int(input("1- sonni kiriting = "))
# s2=int(input("2- sonni kiriting = "))
# operator=input("operator = ")
# if operator=="+":
#     print(f"YIGINDI : {s+s2}")
# elif operator=="-":
#     print(f"AYIRMA : {s-s2}")
# elif operator=="*":
#     print(f"KOPAYTMA : {s*s2}")
# elif operator=="/":
#     print(f"BOLINMA : {s/s2}")
# elif operator=="%":
#     print(f"QOLDIQI : {s%s2}")
# elif operator=="**":
#     print(f"DARAJASI : {s**s2}")
# elif operator=="//":
#     print(f"QOLDIQSIZ BOLISH : {s//s2}")
# else:
#     print("ERROR")

# print(x:=5)

#
# if (n := int(input("Son kiriting: ")) % 2 == 0 ):
#     print("juft")
# else:
#     print(f"toq")


#
# if (s := input("So‘z kiriting: ")) and len(s) > 5:
#     print(f"So‘z uzun: {s}")



# if "salom" in (matn := input("Matinni Kiriting: ")).lower():
#     print(matn.capitalize())




# if (n := int(input("Son kiriting: "))) > 0:
#     print(f"Musbat son: {n**2}")



# if (n := int(input("yosh kiriting: "))) >= 18:
#     print(f"SIZ VOYAGA YETGANSIZ kirish mumkin  : {n}")
# else:
#     print(f"SIZ VOYAGA YETMAGANSIZ kirish mumkin emas  : {n}")


# a=input("Pasword ? = ")
# match a:
#     case "hello"| "world"|"1234":
#         print("succes")
#     case _:
#         print("fail")



# import random
# comp=random.choice("12345678910")
# cheat =input("cheat kodi yoki / entr  = ").strip().lower()
# if cheat=="shoh":
#     print(f"CHEAT ishladi sirli javob {comp}")
# user = input("taxmin soningizi yazing (1,2,3,4,5,6,7,8,9,10)= ").strip()
# if user == comp:
#     print("tabriklayman togri topdingiz 😎😎👍")
# else:
#     print("afsus",comp)











# kun = input("kunni kiriting masalan (dushanba , seshanba ... ) : ").lower().strip()
#
# oddiy_kunlar = ["dushanba", "seshanba", "chorshanba", "payshanba", "juma"]
# d_kun = ["shanba", "yakshanba"]
#
#
# oddiy_kun = 47
# stakan_narxi = 22000
# oddiy_daromad = oddiy_kun * stakan_narxi
#
# if kun in oddiy_kunlar:
#     daromad = oddiy_daromad
# elif kun in oddiy_kunlar:
#     daromad = int(oddiy_daromad*1.5)
# else:
#     print("Qiymat xato kiritadi")
#     daromad = None
# if daromad is not None:
#     print(f"Bugun {kun.capitalize()}kuni , tushgan pul :  {daromad:,} som ")

# ism=input("ismingizni kiriting : ")
# qadam = int(input("bugun qancha qadam tahladingiz : "))
# qadam_uzunligi = 0.7
# masofa = qadam * qadam_uzunligi
# print(f"Assaalom alaykum hurmatli {ism} , siz bugun {qadam} qadam yurdingiz , bu {masofa:.3f}metrga teng !")



# soat=int(input("necha soat = "))
# lamp=int(input("necha lampa = "))
# lampa=lamp*60
# kvv= lamp * soat
# print(f"siz bugun svetni {soat} soat yoqib qoydingiz {lamp} ta lampochka ni ; kunlik energiya sarfi : {kvv * 1000} Vaat")

# tort masalasi
# tort =int(input("qancha tort ? = "))
# un = 450
# tuxum = 5
# shakar = 250
#
# print(f"sizga {tort}, ta tort uchun {un*tort} gramm un kerak , {tuxum*tort } dona tuxum , {shakar *tort} gram shakar  masalliq kerak boladi  ")

#
# semizlik= int(input("vazningiz nechi kg ? = "))
#
#
# if semizlik >= 18.5 and semizlik <= 25:
#     print("vazningiz ideal , normal vazn ")
# elif semizlik >=26 and semizlik <= 30 :
#     print("ortiqcha vazin mavjud")
# elif semizlik < 30 :
#     print("siz da semizlik muammosi bor  ")
# else:
#     print(f"vazningiz {semizlik} ekan ")



# # 8-masala
# boshburchak = 0
# birinchi_burish = 30
# ikkinchi_burilish = 75
#
# yakun_burchak = (boshburchak + birinchi_burish + ikkinchi_burilish) % 360
#
# print("Robotning oxirgi burchagi:", yakun_burchak, "daraja")
#








# 100- masala



# n=int(input("nechanchi yil ? = "))
# if n%4 == 0 and n%100 != 0 and n%400 == 0:
#     print(f"bu {n}, - yil kabisa yili")
# else:
#     print(f"bu {n}, - yil kabisa yili emass!!!!")


# 2-m
# j=int(input("jihozlar miqdori = "))
# f=int(input("foydalanish vaqti = "))
# if j<5<8:
#     print("tejamkor")
# elif j<5>=8:
#     print("ortacha istemol")
# elif j>=5<8:
#     print("kop istemol")
# elif j>5>8:
#     print("haddan tashqari istemol ")
# else:
#     print("hato ")

# 3-m
# qax=int(input("qahfangizning qancha darajada iissiqligini kiriting(60,30) = "))
# if qax==60:
#     print("ogox boling qahfangiz juda issiq")
# elif qax<49:
#     print("ideal")
# elif qax >30 :
#     print("qahfangiznsovub qolgan")
# else:
#     print("qaxfangiz isssiqmi ?")

# 4-m
# tel=int(input("iltimos telefoningiz zaryadini kiriting = "))
# if tel<=100 :
#     print("telefoningiz  zaryadi yetarli ")
# elif tel>=60:
#     print("telefoningiz zaryadi normal")
# elif tel>=20:
#     print("telefonni zudlik bilan zaryadlang")
# else:
#     print("telefonning zaryadi yaxshi ")

# 5-m
# raqam=int(input("telefoningizning boshidagi qodni kiriting = "))
# if  raqam == 99891:
#     print("BELINE")
# elif raqam == 99894:
#     print("UCELL")
# elif raqam == 99897:
#     print("MOBIUZ")
# elif raqam == 99898:
#     print(" PERFECTUM")
# elif raqam == 99833:
#     print(" HUMANS")
# else:
#     print(f"{raqam} raqam topilmadidann ")

# 6-m
# email = input("Email manzilingizni kiriting: ")
#
# if '@' in email:
#     print(" Email dogri.")
# else:
#     print("Email notogri")



# 7-m
# ball=int(input("balingiz nechi = "))
# if ball<56:
#     print(f"siz olgan abll{ball}, - bu juda kam qoniqarsiz ")
# elif ball >56 and ball<70:
#     print("qoniqarli")
# elif ball>71 and ball<85:
#     print("ALO")
# else:
#     print("ball notogri kiritilgan ")

# 8-m
# yosh=int(input("yoshingiz nechi = "))
# if yosh <= 7:
#     print("bepul")
# elif yosh >= 8 and yosh <= 18:
#     print(f"sizning yoshingiz  {yosh} da siz uchun 5000 som )
# elif yosh >= 19 and yosh<= 60:
#     print(f"sizning yoshingiz  {yosh} da siz uchun 10000 som ")
# else :
#     print("7000 som ")


 # 9-m
# satr=input("matn kiriting = ")
# print(satr.startswith(" "))


# 10-m
# raqam=input("qarta raqamingiz ni kiriting = ")
# if len(raqam)==16 and raqam.isdigit():
#     print(f"karta raqam {raqam } , togri ")
# else:
#     print(f"karta raqam- {raqam} notogri")

# 11-m
#
# narx=int(input("narxni kiriting = "))
# if narx <50000:
#     print("chegirma yoq ")
# elif narx >=50000 and narx <100000 :
#     print("5 % chegirma ")
# elif narx >100000 and narx <200000:
#     print("")

# ishqilib if elsela


# harorat=float(input("haroratni kiriting = "))
# if harorat<50:
#     if harorat > 30 :
#         print("yengil kiyim kiying ")
#     elif  15 <harorat <30:
#         print("yengil qurtka kiying ")
#     else:
#         print("issiq kiyim kiying ")
# else:
#     print("havo juda sovuq ")



# yosh=int(input("yoshingiz nechi = "))
# if yosh >= 0 and yosh <=6 :
#     print("bepul")
# elif yosh >=7 and  yosh <=18:
#     print("5000 som")
# elif yosh >=19 and yosh <= 60:
#     print("10000 som")
# elif yosh >61 :
#     print("3000 som")
# else:
#     print("notogri qiymatni yoki soralgan imtiyozni bajarmadingiz ")

#
# son=int(input("sonni kiriting = "))
# if son % 2 == 0 and son % 3 != 0:
#     print(f"bu {son} , - juft son ")
# elif son % 3 == 0 and  son % 2 != 0:
#     print(f"bu {son} , - toq son ")
# else:
#     print(f"bu {son}, hato")




#
# pasword=input("parolni kiriting = ").lower().strip()
# if pasword == "admin123":
#     print("SUCCESFUL")
# else:
#     print("FAILED")


# internet=int(input("internet tezligi qancha = "))
# if internet <= 50 :
#     print("internet tezligi yaxshi ")
# elif internet <= 49 and internet >20:
#     print("ortacha ")
# elif internet <20:
#     print("sekin")
# else:
#     print("notogri trafik")

# uy=int(input("uygacha masofa = "))
# if uy == 1:
#     print("piyoda boring")
# elif uy >1 and uy <5:
#     print("velosipedda boring")
# elif uy >5:
#     print("mashina kerak")



# tel=int(input("telefon batareyasini kiriting = "))
# if tel >= 100 and tel >= 90 :
#     print(f"sizning zaryadingiz {tel}, % ekan bu kopga yetadi")
# elif tel <90 and tel >=60:
#     print(f"zaryadingiz {tel}, % ekan bu normal")
# elif tel <20:
#     print("zaryad kam")


# sot=int(input("soat nechi = "))
# if sot>= 6 or sot <= 12 :
#     print("XAYIRLI TONG ")
# elif sot >=13 or sot <=18:
#     print("XAYIRLI KUN ")
# elif sot >=19 or sot <= 23 :
#     print("hayirli kech ")
# elif sot == 0 or sot ==5:
#     print("tungi salom ")
# else:
#     print("notogri kiritish")


# balans=int(input("balansingiz miqdori = "))
# if balans < 0 :
#     print("hisobingizda qarzdorlik bor ")
# elif balans < 100000:
#     print("kam balans")
# elif balans >100000:
#     print("balans yaxshi ")
# else:
#     print("notogri balans miqdori")


# kun=int(input("hohlagan 1dan 7gacha son = "))
# match kun:
#     case 1 :
#         print("bugun dushanba")
#     case 2 :
#         print("bugun seshanba")
#     case 3 :
#         print("bugun chorshanba")
#     case 4 :
#         print("bugun payshanba")
#     case 5 :
#         print("bugun juma ")
#     case 6 :
#         print("bugun shanba ")
#     case 7 :
#         print("bugun yakshanba ")
#     case _:
#         print("notogri hafta juni")


# bal=int(input("imtixondan necha ball oldingiz = "))
# if bal >60:
#     print("otdi")
# else:
#     print("otmadi")



# narx=int(input("maxsulot narxini kiritng = "))
# if narx>100000:
#     print("15% soliq qoshildi")
# else:
#     print("10% soliq qoshildi")


# son1=int(input("1-sonni kiriting = "))
# son2=int(input("2-sonni kiriting = "))
# son3=int(input("3-sonni kiriting = "))
# if son1>son2>son3:
#     print(son1)
# elif son2>son3>son1:
#     print(son2)
# elif son3>son1>son2:
#     print(son3)
# else:
#     print("xato urinish")

# maxsulot=int(input("maxsulot narxi= "))
# if maxsulot >500000:
#     print("10% chegirma ")
# else:
#     print("chegirma yoq")

# kun=int(input("hafta kunini kiriting = "))
# if kun>=1 and kun<=5 :
#     print("ish kuni ")
# elif kun == 6 and kun == 7 :
#     print("dam olish kuni ")
# else:
#     print("hato qiymat")


# yosh = int(input("yoshimgiz= "))
# daromad=int(input("daromadingiz = "))
# if yosh >21 and daromad > 3 :
#     print("qridit beriladi ")
# else:
#     print("oylab koramiz ")


# erkak=int(input("erkak yoshi  = "))
# ayol=int(input("ayol yoshi = "))
# if erkak>60 and ayol >55:
#     print(f"erkak yoshi {erkak}ekan pensiyaga chiqgan ayol yoshi {ayol} pensiyaga chiqgan ")
# elif erkak>60 and ayol<55:
#     print(f"erkak{erkak}, yoshda ekan , ayol yoshi {ayol} pensiyaga chiqmagan")
# elif erkak<60 and ayol<55:
#     print("erkak pensiyaga chiqmagan ayol ham chiqmagan ")
#
# else:
#     print("ayol va erkak yoshi hato kiritilgan")


#
# bal=int(input("talaba bali qancha = "))
# if bal >85:
#     print("stipenduya oladi ")
# else:
#     print("stipendiya berilmaydi")


#
# signal=int(input("signal kuchi qancha dbm = "))
# if signal >=-50:
#     print("alo")
# elif signal <=70 and signal > -50:
#     print("ortacha ")
# elif signal <-70:
#     print("yomon")

# 50 masala
# sum=int(input("xarid summasini kiriting = "))
# if sum > 0 :
#     if sum <50000:
#         print(f"xarid summasi {sum} , chegirma yoq ")
#     elif sum <100000:
#         print(f"xarid summasi {sum} , 5% chegirma  ")
#     elif sum <200000:
#         print(f"xarid summasi {sum} , 10% chegirma  ")
#     else:
#         print(f" xarid summasi {sum} ,  15% chegirma  ")
# else:
#     print("bunaqa summa uchun chegirma mavjud emas!!")


# 2-m
# chiroq=input("svetafor rangi : ").lower().strip()
# if chiroq == "qizil":
#     print(f"svetafor rangi {chiroq} , - toxtang ")
# elif chiroq == "sariq":
#     print(f"svetafor rangi {chiroq} , - shoshilmang tayyor boling ")
# elif chiroq == "yashil":
#     print(f"svetafor rangi {chiroq} , - yurishingiz mumkin ")
# else:
#     print("svetaforda bunaqa rang mavjud emas !!!! ")

# 3- m
# soat=float(input("dori ichish vaqtni kiriting(6 /11/12/17/18/23/0/5/) = "))
# match soat:
#     case 6 | 11 :
#         print("ertalabgi dori ")
#     case 12 | 17 :
#         print("kunduzgi dori")
#     case 18 | 23 :
#         print("kechki dori ")
#     case 0 | 5 :
#         print("hozi dori ichish shart emas ")
#     case _:
#         print("soatni hato kirtdingiz ")

# 4-m
# harorat=int(input("haroratni kiriting = "))
# if harorat > -30:
#     if harorat <= 15 and harorat >0:
#         print(f"{harorat} , havo harorati jaket jiying ")
#     elif harorat > 15 and harorat <25 :
#         print(f"havo harorati {harorat} , futbolka yetarli  ")
#     elif harorat <= 25 :
#         print(f"havo harorati {harorat}, yengil kiyim , soyabon oling. ")
#     else:
#         print(f" havo harorati {harorat}, bunaqa gradusda yashash imkonsiz")
# else:
#     print(f"harorat {harorat}, bunaqa sovuqda yashash imkonsiz ")

# 5-m
# sinf=int(input("nechanchi sinif ssiz(1/2/3/4/5/6/7/8/9/) = "))
# ogirlik=int(input("sumkangiz ogirligini kiriting = "))
# if sinf >1 and sinf < 5 and ogirlik >1 and ogirlik < 5 :
#     print(f"siz {sinf}- sinf siz sumkangiz ogirligi {ogirlik} , ogir kamaytiring")
# elif sinf >5 and sinf <= 9 and ogirlik >4:
#     print(f"siz {sinf}- sinf siz sumkangiz ogirligi {ogirlik} , ogir kamaytiring")
# else:
#     print("Normal")

# 6-m
# yosh=int(input("bemor yoshi = "))
# holat=input("bemor holati (ogir/oddiy) = ")
# if holat == "ogir":
#     print("zudlik bilan")
# elif holat == "oddiy" and yosh <70:
#     print("1 soat ichida ")
# else:
#     print("3 soat ichida ")

# 7-masala
# kun = input("Kun nomini kiriting (masalan: Dushanba, Seshanba...): ").lower()
# masofa = float(input("Masofani kiriting (km): "))
#
# ish_kuni = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma']
# dam_kuni = ['shanba', 'yakshanba']
#
# if kun in dam_kuni:
#     if masofa > 10:
#         print("Bugun dam olish kuni!")
#         print(f"Summa: {(3600 * masofa) * 0.9} Sizga masofa 10 kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print("Bugun dam olish kuni!")
#         print(f"Summa: {3600 * masofa} so'm.")
# elif kun in ish_kuni:
#     if masofa > 10:
#         print("Bugun ish kuni!")
#         print(f"Summa: {(3000 * masofa) * 0.9} so'm. Sizga masofa 10 kmdan oshganligi sababli 10% chegirma beriladi.")
#     else:
#         print("Bugun ish kuni!")
#         print(f"Summa: {3000 * masofa} so'm.")
# else:
#     print("Qiymat xato kiritildi!")


# 8-m
# harorat=int(input("haroratni kiriting = "))
# extimol=float(input("yomgir yogish extimoli = "))
# if harorat <65 and extimol>0:
#     if extimol >= 70:
#         print("uyda qoling")
#     elif harorat < 5:
#         print("juda sovuq sayir qilish tavsiya etilmaydi ")
#     else:
#         print("ajoyib kun sayirga boring")
# else:
#     print("xato xarorat")

# 9-m
# oy_daromad=int(input("oylik daromadni kiriting = "))
# xarajat=int(input("xarajatni kiriting = "))
# if xarajat>oy_daromad:
#     print("Xavfli! Xarajatlarni kamaytiring")
# elif xarajat == oy_daromad:
#     print("aynan yetarli")
# else:
#     print("Ajoyib! Tejamkorlik qilyapsiz” deb chiqaring.")


# 10-m
# turi=input("velosiped (shaxar/sport):")
# soat=int(input("necha soat = "))
# shaxar=10000
# sport=15000
# if turi == "shaxar":
#     print(f"{shaxar*soat}---> umumiy narx")
# elif turi == "sport":
#     print(f"{sport*soat}---> umumiy narx")
# elif soat >3 and turi == "shaxar" :
#     print(f"{shaxar*soat*0.9}---> umumiy narx va yena 10% bchegirma ")
# elif soat >5 and turi == "shaxar":
#     print(f"{shaxar*soat*0.8}---> umumiy narx va yena 20% chegirma ")
# else:
#     print("notogri kiritildi!!!")

# 11-m
# ogirlik=float(input("meva ogirligini kiriting = "))
# korinishi=input("meva korinishi (yaxshi/yomon)  ; ")
# if korinishi == "yomon":
#     print("past sifat ")
# elif ogirlik <100 :
#     print("rad etiladi")
# elif ogirlik >= 200 :
#     print("premium")
# else:
#     print("standart")
# 12-m
# summa=int(input('harid summasini kirting = '))
# hozir_soat=int(input("hozirgi soatni kiriting(0-23) = "))
# if summa>= 100000 and 18<= hozir_soat<=22 :
#     print("15% chegirma ")
# elif summa >= 50000 and 10 <= hozir_soat<=18 :
#     print("10% chegirma ")
# else:
#     print("chegirma yoq ")

# 13-m
# turi=input("kitob turi (ilmiy/badiy) : ").lower().strip()
# kunlar_soni=int(input("necha kun = "))
# kun=2000
# if turi == "ilmiy":
#     print(f" kitob turi {turi} ,sizga {kunlar_soni*kun} ---> umumiy narx")
# elif turi == "badiy":
#     print(f"kitob turi {turi}, sizga umumiy narx --->{kunlar_soni*1000} ")
# elif kunlar_soni>14 :
#     print(f"{kunlar_soni*2000*0.7}---> umumiy narx va 30% chegirma")
# elif kunlar_soni>7:
#     print(f"{kunlar_soni*2000*0.8}---> umumiy narx va 20% chegirma")
# else:
#     print("xato")

# 14-m
# m_turi=input("mashq turi (kardio/ogirlik) = ").lower().strip()
# tajriba=int(input("necha yil tajribangiz bor = "))
#
# if m_turi == "kardio" and tajriba <1:
#     print("20 daqiqa yengil")
# elif m_turi == "ogirlik" and tajriba >=2:
#     print("60 daqiqa intensiv")
# else:
#     print("30 daqiqa ortacha ")

# 15-m
# das_nom=input("dastur nomini kiriting (yangiliklar / serial); ").lower().strip()
# hoz_soat=int(input("hozir soat nechi = "))
# if das_nom == "yangiliklar" and 18<= hoz_soat <= 20 :
#     print("tomosha qiling ")
# elif das_nom == "serial" and 20<= hoz_soat <= 22 :
#     print("qayta koring")
# else:
#     print("boshqa korsatuv tanlang")


# 16-m
# turi=input("skuter turini tanlang (elektr/oddiy) = ")
# masofa=int(input("masofani kiriting = "))
# km=2000
# if turi == "elektr":
#     print(f"sizning tanlov {turi}, puli = {masofa*km}, ")
# elif masofa >= 10 :
#     print(f"sizing tanlov {turi}, umumiy narx = {masofa*km*0.85}, ")
# else:
#     print(f"sizing tanlov {turi}, puli = {masofa*1000}, ")
#
# 30-m
# turi=input("bolalar/kattalar = ").lower()
#
# if turi == "bolalar":
#     print("2kun")
# olcham=input("olcham S/M ; ").lower()
# if olcham == "S/M":
#     print("4kun")
# else:
#     print("6kun")


# 31-m
#
# meva=input("(meva ) ha/yoq = ")
# shokolad=input("(shokolad ) ha/yoq = ")
# qavat=input("(qavat ) ha/yoq = ")
# narx=100000
# if meva == "ha":
#     print(f"{narx+20000} umumiy narx")
# elif shokolad == "ha":
#     print(f"{narx+30000} umumiy narx")
# elif qavat == "ha":
#     print(f"{narx+50000} umumiy narx")
# else:
#     print(f"{narx} =  umumiy narx")


# 32-m
# mato=input("mato turi(paxta/sintetik/ = ")
# daraja=input("ifloslik daraja (yengil /ogir) = ")
# if mato == "paxta" and daraja == "yengil":
#     print("Rejim 1")
# elif mato == "sintetik" and daraja == "ogir":
#     print("Rejim 3")
# else:
#     print("Rejim 2")

# 33-m
# kitob=input("kitob nomi = ")
# if kitob.startswith("sir") and kitob.startswith("jinoyat"):
#     print("Detektiv")
# elif kitob.startswith("romantik") and kitob.startswith("sevgi"):
#     print("Romantik")
# elif kitob.startswith("kelajak") and kitob.startswith("kosmas"):
#     print("fantastik")
# else:
#     print("boshqa")


# 34-m
# chipta=input("chipta turi (vip/oddiy) = ")
# yosh=int(input("yoshingiz = "))
# if chipta == "vip" and yosh >60 :
#     print("50000 som ")
# elif chipta == "oddiy" and yosh <18 :
#     print("20 000 som")
# else:
#     print("30 000 som ")

# 35-m my best code
# kuni=input(" hafta kunini kiriting : ").lower().strip()
# dv=("dushanba", "seshanba", "chorshanba", "payshanba","juma",)
# soat=int(input("soat = "))
# if kuni in dv and 9<=soat<=18:
#     print("ochiq")
# elif kuni == "shanba" and kuni == "yakshanba" and 10<=soat<=16 :
#     print("ochiq")
# else:
#     print("yopiq")

# 36 -m
# turi=input("osimlik turi(gul/daraxt) = ")
# fasl=input("fasil = ")
# if turi == "gul" and fasl == "baxor":
#     print("Haftada 3 marta sugoring")
# elif turi == "daraxt" and fasl == "yoz":
#     print("har kun sugoring ")
# elif turi == "gul" and fasl == "qish":
#     print("haftada 1 marta sugoring")
# else:
#     print("haftada 2 martasugoring ")
# 37-m
# budjet=int(input("budjetingiz = "))
# vip=input("VIP --> kerakmi ? (ha/yoq) = ")
# if budjet >100000 and vip == "ha":
#     print("1- qator vip")
# elif budjet >100000 and vip == "yoq":
#     print("1- qator oddiy")
# elif budjet <= 100000 and vip == "yoq":
#     print("orta qator")
# else:
#     print("orqa qator ")

# 38-m
# xotira=int(input("telefoningiz ning band xotirasi ----> "))
# if xotira>= 95:
#     print("xotira tola tozalash kerak")
# elif 80<=xotira< 95:
#     print("xotira kam qoldi ")
# elif xotira >= 50 :
#     print("xotira yetarli")
# else:
#     print("xotira bosh")
# 39-m
# bal=int(input('umumiy bal = '))
# if bal >= 90 :
#     print("ustoz")
# elif bal >=70 :
#     print("malakali")
# elif bal>=50 :
#     print("orta")
# else:
#     print("boshlangich")

# 40-m

# ball=int(input("talabaning umumiy balli= "))
# if ball >= 90 :
#     print("5 baxo")
# elif ball >=71 :
#     print("4 baxo")
# elif ball >=60 :
#     print("3 baxo")
# else:
#     print("ball yetarli emas")

# 41-m
# yosh=int(input("yoshingizni kiriting = "))
# if yosh>0 and yosh <= 7 :
#     print("bepul")
# elif yosh >= 45 :
#     print("chegirma 3000")
# else;
#     print("7000 som")
# 42-m
# oy=int(input("oy raqamini kirirting = "))
# if oy == 1 or oy == 12 or oy == 2 :
#     print("qish")
# elif oy == 3 or oy == 4 or oy == 5 :
#     print("baxor")
# elif oy == 6 or oy == 7 or oy == 8 :
#     print("yoz")
# else:
#     print("kuz")
# 43-m
# model=input("telefoningiz modeli : ")
# holat=input("holati (yangi/ishlatilgan) = ")
# if model == "ipxone" and holat == "yangi":
#     print('1200 $')
# elif model == "ipxone" and holat == "ishlatilgan":
#     print("800 $")
# elif model == "samsung" and holat == "yangi":
#     print("900 $")
# elif model == "samsung" and holat == "ishlatilgan":
#     print("600 $")
# else:
#     print("narx kelishilgan holda")

# 44-m
# yosh=int(input("yoshingiz = "))
# bal=int(input("ball = "))
# if yosh >=6 and bal >= 70 :
#     print(" qabul qilindi")
# else:
#     print("qabul qilinmadi")
# 45-m
# tezlik=int(input("internet tezligi= "))
# if tezlik<5 :
#     print("juda sekin")
# elif 5<= tezlik <20 :
#     print("ortacha")
# elif 20<= tezlik <100 :
#     print("tez")
# elif tezlik >100 :
#     print("juda tez")
# else:
#     print("xatolik")

# 46-m
# vaqt=input("bosh vaqt (kam/kop/ortacha) = ")
# joy=input(" joy (kam/kop/ortacha) = ")
# if vaqt == "kam" and  joy == "kam" :
#     print("baliq")
# elif vaqt == "kop" and joy == "kop" :
#     print("it")
# else:
#     print("mushuk")
# 47-m
# yosh=int(input("yoshni kirting = "))
# tajriba=int(input("tajribangiz necha yil = "))
# daraja=input("ingliz tili darajangiz(boshlangich/orta/yaxshi)  = ")
# if yosh >= 22 and tajriba >= 2 and daraja == (daraja== "orta" and daraja == "boshlangich"and daraja == "yaxshi"):
#     print("qabul qilindi ")
# else:
#     print("qabul qilindi ")
#48-m
# yil=int(input("yil kiriting = "))
# if yil % 4 == 0 and yil % 100 != 0 or yil % 400 == 0:
#     print("kabisa yil")
# else:
#     print("kabisa yili emas")

# 49-m
# daromad=int(input("oylik daromad = "))
# if daromad <= 1 :
#     print(" 0 %")
# elif daromad <= 3 :
#     print(" 10 %")
# else:
#     print(" 20 %")

# 50-m
# yosh=int(input("yoshingiz = "))
# maxsulot=input(" mahsulot turi (oziq-ovqat/kiyim/texnika) = ")
# if maxsulot == "oziq-ovqat" :
#     print("chegirma yoq ")
# elif yosh <12 :
#     print("20 % chegirma")
# elif yosh > 60 :
#     print("15 % chegirma")
# else:
#     print("chegirma mavjud emas ")

# 200 masala
#
# yosh=int(input("yoshingizni kiriting = "))
# if yosh >5 and yosh < 10 :
#     print("bolalar velosipedi")
# elif yosh > 11 and yosh <17 :
#     print("sport velosipedi ")
# elif yosh >18 :
#     print("shaxar velosipedi ")
# else:
#     print("xatolik")
# 52-m
# holat=input("issiq/bsohqa = ")
# vaqt=input("qaysi vaqt tush/boshqa = ")
# if holat == "issiq" and vaqt =="tush":
#     print("tavsiya qilinadi ")
# else:
#     print("keyinroq")
#
# 53-m
# budjet=input("budjet kop/kam = ")
# obhavo=input("ob havo  yaxshi/boshqa =")
# masofa=input(" masofa yaqin/uzoq = ")
# if budjet == "kam":
#     print("mahalliy")
# elif obhavo == "yaxshi" and masofa == "yaqin":
#     print("tog")
# else:
#     print("plyaj")
# 54-m
# tandir=input("tandir turi elektr/gaz = ")
# vaqt=int(input("vaqt ni kiriting = "))
# if tandir == "elektr" and vaqt <30 :
#     print("180°C")
# elif tandir == "gaz" and vaqt >= 30:
#     print("200°C")
# else:
#     print("160°C")

# 55-m
# daraja=input("bakalavr/magistr")
# baxo=int(input("baxoni kiriting = "))
# if daraja == "bakalavr" and baxo >=85:
#     print("beriladi")
# elif daraja == "magistr" and baxo >= 90:
#     print("beriladi ")
# else:
#     prinr("berilmaydi")

# 56-m
# osimlik=input("osimlik turi daraxt/gul = ")
# tuproq=input("tuproq turi qumloq/loy = ")
# if osimlik == "gul" and tuproq == "qumloq":
#     print("har 2 kunda sugoring ")
# elif osimlik == "daraxt" and tuproq == "loy":
#     print("haftada 1 marta sugoring ")
# else:
#     print("har 3 kunda sugoring")
# 57-m
# xizmat_turi=input("xizmat turi tamirlash/ornatish = ")
# soat_narxi=("tamirlash=50000",
# "ornatish=30000")
#
# ish_vaqti = int(input("ish vaqti = "))
# if xizmat_turi== "tamirlash" and ish_vaqti==1:
#     print(f"{ish_vaqti *xizmat_turi}")
# elif xizmat_turi=="ornatish" and ish_vaqti==1:
#     print("30 000 ")
# umumiy_narx = ish_vaqti*soat_narxi
# print(umumiy_narx)
# 58-m
# ichimlik=input("ichimlik turi kofe/choy=")
# dona=int(input("necha dona = "))
# kofe=15000
# if ichimlik =="kofe"and dona > kofe :
#     print(f"{dona*kofe}->> som")
# umumiy=kofe*dona
# if dona >5 :
#     print(f"{dona*kofe*0.9}->> som")
# else:
#     print("5000 som ")


# 59-m
# turi=input("mashina turi piyoda/velosiped/mashina = ")
# masofa=int(input("masofani kiriting necha metr = "))
# if turi == "piyoda" :
#     print(f"{12*masofa} shuncha daqiqada")
# elif turi == "velosiped" :
#     print(f"{4*masofa} shuncha daqiqada")
# else:
#     print(f"{2*masofa} shuncha daqiqada")
# 60-m
# batareya=int(input("batareya necha % = "))
# vaqti=int(input("foydalanish vaqti = "))
# if batareya< 20 and vaqt >1:
#     print("zudlik bilan zaryadlang ")
# elif batareya <50 and vaqt < 1 :
#     print("tezroq zaryadlang")
# else:
#     print("yaxshi holat")
# 61-m
# mijoz=input("mijoz turi yangi/doimiy = ")
# xarid=int(input('xarid summasini kiriting = '))
# if mijoz == "doimiy" and xarid >=50000 :
#     print("5000 som bonus ")
# elif mijoz == "yangi" and xarid > 100000 :
#     print("3000 som bonus ")
# else:
#     print("bonus yoq ")

#
# 62-m
#
# harorat=int(input("haroratni kiriting = "))
# extimol=int(input("yomgir yogish extimoli = "))
# if harorat <5 :
#     print("issiq kiyining ")
# elif extimol>= 70 :
#     print("soyabon oling ")
# elif harorat <25  and extimol <30 :
#     print("yengil kiyining ")
# else:
#     print("havo normal")

#
# 63-m
# bal=int(input("balingizni kiriting = "))
# kvota=input("kvota bor/yoq = ")
# if bal>= 90 and kvota =="bor":
#     print("qabul qilindi ")
# elif bal >= 70 and bal <= 89 and kvota == "yoq":
#     print("navbat kuting ")
# else:
#     print("qabul qilinmadi ")
# 64-m
# sozlar_soni = int(input("So‘zlar sonini kiriting: "))
# daraja = input("Darajani kiriting (boshlang‘ich/malaka): ").lower()
#
# if sozlar_soni < 5:
#     natija = "Tushunarsiz so‘rov"
# elif 5 <= sozlar_soni <= 15 and daraja == "boshlang‘ich":
#     natija = "Soddaroq tilda tushuntirildi"
# elif sozlar_soni > 15 and daraja == "malaka":
#     natija = "Batafsil ilmiy javob"
# else:
#     natija = "Umumiy javob"
#
# print(natija)

# 65-m
# osimlik=input("osimlik turi (kaktus) = ")
# yomgir=int(input("ertangi yomgor extimoli = "))
# namlik=int(input("namlik necha % = "))
# if osimlik == "kaktus" :
#     print("sugormang ")
# elif namlik < 30 and yomgir < 60 :
#     print("sugoring")
# elif namlik < 30 and yomgir >= 60 :
#     print("kechiktiring ")
# else:
#     print("hozir sugorish shart emas")
# 66-m
# jihoz=input("jihoz turi yuqori quvvat/past quvvat=  ")
# soat=int(input("hozirgi soatni kiriting = "))
# if jihoz == "past quvvat" :
#     print("har doim ishlashi mumkin")
# else:
#     print("yuqori quvvat")
# if 9<= soat<= 17 :
#     print("ishlatish mumkin")
# else:
#     print("ishlatish tavsiya etilmaydi ")
# 67-m
# mahsulot=input("mahsulot  turi  = ")
# mijoz=input("mijoz turi premium/oddi =")
# if mahsulot == "dori" and mijoz == "premium" :
#     print("1 soat ichida ")
# elif mahsulot  == "oziq-ovqat" :
#     print("3 soat ichida")
# else:
#     print("24 soat ichida")

# 68-m
maning hatoma dogrima bilimman qodlarim ishqilib shuuu












