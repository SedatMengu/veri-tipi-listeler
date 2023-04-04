# listeler

# tanım : verileri sıralı bir şekilde hafızada tutmaya yarayan veri yapısıdır.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]

print(renkler)                                          # - bu şekilde bütün liste ekrana bastırılır.
#print(renkler[])                                       # - bu şekilde [] ifadesini belirtiyor isek mutlaka index girmek zorundayız.


# listenin herhangi bir elemanını değiştirmek istersek

print(renkler)                                          # listenin ilk halini bastırdık / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
renkler [0] = "Ela"                                     # 0.indexi değiştirdik , 
print(renkler)                                          # 0.index değiştikten sonraki halini bastırdık. / ['Ela', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']

# liste eleman sayısı bulma 

print(len(renkler))                                     # renkler listenin 5 elemanı var

print(renkler[:2])                                      # baştan 2.indexe kadar yazdırdık.. (2.index alınmaz) / ['Ela', 'Kirmizi']
print(renkler[0:3])                                     # 0.indeten 3.idex hariç yazdırdık.. / ['Ela', 'Kirmizi', 'Beyaz']
print(renkler[0:5:2])                                   # 0,2,4.indexleri yazdırdık.  / ['Ela', 'Beyaz', 'Turuncu']

# listelerde metotlar

# listenin sonuna eleman ekleme:

renkler.append("Gri")                                   # / ['Ela', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu', 'Gri']
print(renkler)     

# listeyi temizleme : 
renkler.clear()        
print(renkler)                                          #  / []
renkler.copy()
print(renkler)

# listedeki elemanları sayma:

print(renkler.count("Kirmizi"))                         # / 1

# listenin sonuna birden fazla eleman ekleme:

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]  # ilk liste
renkler2 = ["Kahvrengi","Mor"]                          # ikinci liste
renkler.extend(renkler2)                                # extend ile listenin sonuna elemanları gene elemanmış gibi ekledik
print(renkler)                                          # / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu', 'Kahvrengi', 'Mor']

# kaçıncı indexte olduğunu bulma : 
renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]
print(renkler.index("Beyaz"))                           # / 2 

# listeye belirli indexe eleman ekleme
renkler.insert(0,"Turkuaz")                             # / ['Turkuaz', 'Ela', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu', 'Gri']
print(renkler)

# listeden herhangi bir elemanı söküp almak , başka değişken içine atmamız gerekir:

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]  # 
silinen_eleman=renkler.pop()                            # 
print(renkler)                                          # / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari']
print(silinen_eleman)                                   # / Turuncu

# listedeki herhangi bir elemanı silmek : 

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]
renkler.remove("Kirmizi")                               #  /  ['Turkuaz', 'Ela', 'Beyaz', 'Sari', 'Turuncu', 'Gri']
print(renkler)

# listeyi tersten yazmak : 

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]  # 
print(renkler)                                          # / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
renkler.reverse()                                       # 
print(renkler)                                          # / ['Turuncu', 'Sari', 'Beyaz', 'Kirmizi', 'Siyah']


# önemli not: listeyi sort edince eski listeye dönemeyiz. bunun için mevcut listenin bir kopyasını alıp sorted yapmamız gerekir.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]  # 
print(renkler)                                          # / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
renkler.sort()                                          # 
print(renkler)                                          # / ['Beyaz', 'Kirmizi', 'Sari', 'Siyah', 'Turuncu']
renkler.sort(reverse=True)                              # 
print(renkler)                                          # / ['Turuncu', 'Siyah', 'Sari', 'Kirmizi', 'Beyaz']


#min , max değer bulma : 

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]
sayilar = [1,2,3,4,5,6,7,8,9]

print(min(sayilar))                                     # / 1
print(min(renkler))                                     # / Beyaz

print(max(sayilar))                                     # / 9
print(max(renkler))                                     # / Turuncu

print(sum(sayilar))                                     # / 45
#print(sum(renkler))                                    # stringler toplanamayacağı için hata verdi


# enumarate fonksiyonu listeyi numaralandırmak : 

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]
print(list(enumerate(renkler)))                         # / [(0, 'Siyah'), (1, 'Kirmizi'), (2, 'Beyaz'), (3, 'Sari'), (4, 'Turuncu')]
print(list(enumerate(renkler,start=1)))                 # / [(1, 'Siyah'), (2, 'Kirmizi'), (3, 'Beyaz'), (4, 'Sari'), (5, 'Turuncu')]

sayilar = [1,2,3,4,5,6,7,8,9]
print(list(enumerate(sayilar)))                         # / [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]

# listenin içinde olup olmadığını bulmak : 
print("Siyah" in renkler)                               # / True
print("Lacivert" in renkler)                            # / False


# listeyi join ile birbirine eklemek : 

stringRenkler = "-".join(renkler)
print(stringRenkler)                                    # / Siyah-Kirmizi-Beyaz-Sari-Turuncu

# herhangi bir string ifadeyi belirli parametreden listeye çevirmek : 

renkler3 = stringRenkler.split("-")                     # herhangi bir string ifadeyi split metotu ile liste haline çevirebiliriz.
print(renkler3)                                         # / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']