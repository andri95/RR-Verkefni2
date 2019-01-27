# RR-Verkefni2
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

