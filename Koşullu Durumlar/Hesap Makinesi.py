print("""*******************************
Hesap makinesi programı

İşlemler;

1. Toplama işlemi

2. Çıkarma işlemi

3. Çarpma işlemi

4. Bölme işlemi
***************************************
""")

a = int(input("Birinci sayıyı giriniz:"))
b = int(input("İkinci sayıyı giriniz:"))

işlem = input("İşlemi giriniz:")

if işlem =="+" :
    print("{} ile {} toplamı {}' dir".format(a,b,a+b))
elif işlem == "-" :
    print("{} ile {} farkı {}' dir".format(a,b,a-b))
elif işlem =="*" :
    print("{} ile {} çarpımı {}' dir".format(a,b,a*b))
elif işlem =="/" :
    print("{} ile {} bölümü {}' dir".format(a,b,a/b))
else:
    print("Geçersiz işlem!")
