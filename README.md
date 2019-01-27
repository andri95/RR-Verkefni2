# RR-Verkefni2  
**Python skjal með keyranlegum kóða fylgir með hér fyrir ofan**  
**1. Hvað er sauðakóði og til hvers er hann notaður?**  
Sauðakóði er samblanda af töluðu máli t.d. íslensku og forritunarmáli. Sauðakóði er einskonar frumrit eða uppkast af forriti sem á við um flest eða öll forritunarmál. Sauðakóði getur verið á marga vegu, td lýsing á forritinu og virkni þess í töluðu máli eða flowchart sem sýnir hvernig forritið tæklar vandamálið eða algrímið sem forritið leysir.

**2. Skrifaðu forrit í sauðakóða sem umreytir tugakerfistölu í tvíundarkerfistölu. Hér er ekki
verið að biðja um keyranlegt forrit.**  
Búa til breytu sem tekur inn tugakerfistölu   
Búa til fall sem tekur inn tugakerfistölu  
Ef tugakerfistala er stærri en 1:  
Kalla í fallið sjálft og deila tugakerfistölu með tveimur  
Prenta út tugakerfistölu modulus tveir  
Kalla í fallið  
```python
def tugakerfi_binary(tala):
    if tala > 1:
        tugakerfi_binary(tala // 2)
    print(tala % 2, end="")

tala = int(input("Enter a number: "))

tugakerfi_binary(tala)
```
**3.**  
```python
        def summa(m):
            if m == 1:
                return 1
            return m ** 2 + summa(m-1)

        m = int(input("Sláðu inn náttúrulega tölu: "))
        print(summa(m))
        print()
```
**4.**  
```python
        def runa(m):
            if m == 1:
                print("1", end =" ")
                return 1
            else:
                rec = m + runa(m - 1)
                print(rec, end=" ")
                return rec

        m = int(input("Sláðu inn náttúrulega tölu: "))
        runa(m)
        print()
```
**5.**  
```python
        def thversumma(n):
            if n < 10:
                return n
            else:
                return thversumma(n // 10) + thversumma(n % 10)

        n = int(input("Sláðu inn heiltölu: "))
        print(thversumma(n))
        print()
```
**6.**  
```python
        def samnefnari(n, m):
            if m == 0:
                return n
            else:
                return samnefnari(m, n % m)

        n = int(input("Tala 1: "))
        m = int(input("Tala 2: "))

        print(samnefnari(n, m))
        print()
```
