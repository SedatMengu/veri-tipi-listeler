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



# listelere ait metodlar

# 1  - .append() metodu listenin sonuna bir öğe eklemek için kullanılır. Öğeyi belirtilen listenin sonuna ekler.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"] 
renkler.append("Gri")                                   
print(renkler)   
# / ['Ela', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu', 'Gri']

    # Ayrıca, append() metodu bir öğe yerine bir liste ekleyebilir ve böylece listenin sonuna başka bir liste ekleyebilirsiniz.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"] 
print(renkler)
renkler.append(["Gri","Mor"])                                   
print(renkler)
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu', ['Gri', 'Mor']]


# 2  - .clear() metodu Listenin elemanlarını silmek için kullanılır. Bu metod, listedeki tüm öğeleri siler ve boş bir liste bırakır.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"] 
print(renkler) 
renkler.clear()        
print(renkler)                                          
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
#  / []


# 3  - .copy() metodu bir listenin shallow kopyasını oluşturur. Yani, yeni bir liste oluşturur ve orijinal listenin elemanlarını kopyalar, ancak bu elemanlar değiştirilirse orijinal liste etkilenmez.

original_list = [1, 2, 3, 4]
new_list = original_list.copy() # new_list shallow list oluyor.
original_list.append(5)
print(original_list) 
print(new_list)  
# / [1, 2, 3, 4, 5]
# / [1, 2, 3, 4]



# 4  - .count() metodu bir listenin içinde belirtilen öğenin kaç defa bulunduğunu sayar ve sonucu geri döndürür.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"] 
print(renkler.count("Kirmizi"))                         
# / 1


# 5  - .extend() metodu  bir listeye başka bir listenin tüm elemanlarını eklemek için kullanılır. Yani bir listeye başka bir listenin elemanlarını eklemek istediğimizde kullanabiliriz.


renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]  
renkler2 = ["Kahvrengi","Mor"]                          
renkler.extend(renkler2)                                
print(renkler)                                          
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu', 'Kahvrengi', 'Mor']

    # extend() metodu ayrıca bir listeyle birlikte başka bir iterable (liste, tuple, set vb.) de alabilir ve bu iterable'ın elemanlarını da listeye ekler.

liste = [1, 2, 3]
tuple = (4, 5, 6)
set = {7, 8, 9}
liste.extend(tuple)
liste.extend(set)
print(liste)
# / [1, 2, 3, 4, 5, 6, 8, 9, 7]


# 6  - .index() metodu  listedeki belirli bir öğenin ilk indeksini döndürür. eğer belirtilen öğe listede yoksa ValueError hatası verir. Başlangıç ve bitiş indeksleri belirtilirse, arama sadece bu indeksler arasında yapılır.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]
print(renkler.index("Beyaz"))                          
# / 2 

# 7  - .insert() metodu 
renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]
print(renkler)
renkler.insert(0,"Turkuaz")                             
print(renkler)
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
# / ['Turkuaz', 'Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']


# 8  - .pop() metodu bir listeden verilen konumdaki öğeyi çıkartır ve bu öğeyi geri döndürür. Eğer indeks belirtilmezse son öğe çıkartılır. Listede değişiklik yapar.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]   
silinen_eleman=renkler.pop()                             
print(renkler)                                          
print(silinen_eleman)                                   
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari']
# / Turuncu


# 9  - .remove() metodu bir listenin belirli bir elemanını kaldırmak için kullanılır. Bu metot, listede bulunan ilk öğeyi kaldırır. Eğer listede bulunmayan bir elemanı remove() metoduyla kaldırmaya çalışırsanız, ValueError hatası alırsınız. Bu durumda, öncelikle listenin elemanlarını kontrol etmeniz gerekmektedir.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]
print(renkler)
renkler.remove("Kirmizi")                              
print(renkler)
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
#  /  ['Siyah', 'Beyaz', 'Sari', 'Turuncu',]


# 10 - .reverse() metodu bir listedeki elemanları ters çevirir. Yani, listedeki son elemanı ilk sıraya, ilk elemanı son sıraya yerleştirir.
# Not: reverse() metodu, listeyi doğrudan değiştirir ve herhangi bir değer döndürmez.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]   
print(renkler)                                          
renkler.reverse()                                       
print(renkler)                                          
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
# / ['Turuncu', 'Sari', 'Beyaz', 'Kirmizi', 'Siyah']

# 11 - .sort() metodu bir listenin elemanlarını sıralamak için kullanılır. Varsayılan olarak, bu metot liste elemanlarını artan sırada sıralar.
# sort() metodu ayrıca, key parametresi kullanılarak bir sıralama anahtarı belirlemek için de kullanılabilir.

renkler = ["Siyah","Kirmizi","Beyaz","Sari","Turuncu"]   
print(renkler)                                          
renkler.sort()                                          
print(renkler)                                          
renkler.sort(reverse=True)      # tersten sıralama                          
print(renkler)                                         
# / ['Siyah', 'Kirmizi', 'Beyaz', 'Sari', 'Turuncu']
# / ['Beyaz', 'Kirmizi', 'Sari', 'Siyah', 'Turuncu']
# / ['Turuncu', 'Siyah', 'Sari', 'Kirmizi', 'Beyaz']
