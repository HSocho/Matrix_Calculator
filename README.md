# Matrix_Calculator

## Dokumentace

### Instalace

Před spuštěním je třeba nainstalovat Python. Kalkulačka se spustí příkazem python matrix_calculator.py v adresáři projektu.

### Návod

Kalkulačka matic umožňuje dělat s maticemi sčítání, násobení, transpozici, inverzi, výpočet determinantu a LU rozklad.  
Kalkulačka se ovládá zadáním čísla, před příslušnou možností.

#### Formát vstupu

Standardní vstup: Matici lze zadat řádek po řádku, kde jsou čísla odděleny mezerou. Vstup je ukončen prázdným řádkem.  
Soubor: Matici lze zadat ve stejném formátu jako standardní vstup nebo i s hranatými závarkami na zaačátku a konci řádku. Musí být poskytnuta cesta k souboru.
#### Formát výstupu:

Výsledek lze zobrazit na konzoli nebo uložit do souboru, ke kterému musí být poskytnuta cesta.
Matice jsou formátovany, tak že na každém konci a začátku řádku je hranatá závorka.

### Technický popis

Program používá knihovnu Fractions.
Kód Kalkulačky Matic je strukturován do funkcí a organizován následovně:
main(): Hlavní smyčka programu, která zobrazuje menu a zpracovává vstup uživatele.
Funkce pro operace s maticemi: sčítání, násobení, výpočet determinantu, transpozice, inverze a LU rozklad.
Funkce pro ověřování vstupu a formátování výstupu.
Kód obsahuje výjimky pro špatné vstupy matic.


