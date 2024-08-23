# Automatiseret genlån af biblioteksbøger fra Hillerød bibliotek
Dette script kan bruges til at automatisere genlån af bøger fra Hillerød bibliotek, således at man, alt andet lige, kan undgå at få bøder - eller i hvert fald udsætte muligheden for samme lidt.

## Demo


https://github.com/user-attachments/assets/8adcea4d-4042-4c45-bd4d-3a88b798b0a6



## Baggrund
Baggrunden for scriptet er, at jeg, Jonas, desværre ofte glemmer at aflevere mine biblioteksbøger lånt fra Hillerød Bibliotek til tiden. Når det sker, så får, forståeligt nok, bøder for at glemme det. Det vil jeg selvfølgelig gerne undgå, og har derfor lavet dette script, så jeg i det mindste automatisk får genlånt mine bøger, og dermed i hvert fald udsætter muligheden for at få bøder, og forhåbentlig husker, grundet den lange lånetid, at aflevere mine bøger på et eller andet tidspunkt under den lange lånetid.

## Scriptet
Det, scriptet gør, er overordnet set bare at:
1. Åbne en browser
2. Logge ind på hilbib.dk
3. Genlån ens biblioteksbøger

### Forudsætninger for at bruge scriptet
For at kunne bruge scriptet, så forudsættes følgende:

#### Have Python installeret
Først og fremmest skal man have Python installeret. Har man ikke det, så følg linket til https://www.python.org/ for at downloade og installere Python.

#### Installere 'selenium' og download af Chromedriver
Når man har Python installeret, så kræver scriptet at man gør følgende:
1. Installerer Python pakken 'selenium'
2. Downloader Chromedriver

##### Installation af 'selenium'
Selenium installeres blot ved at køre denne kommando fra sin terminal:
```bash
pip install selenium
```

##### Download af Chromedriver
Google fx på frasen "how to get chrome driver for python selenium" for at se, hvordan dette gøres.

### Hvordan man bruger scriptet
For at bruge scriptet gøres følgende:
1. Lav en 'credentials.txt' med CPR-nummer og PIN
2. Kør scriptet

#### Lav en 'credentials.txt'
Da scriptet logger ind med ens CPR-nummer og PIN på hilbib.dk, så skal disse 2 oplysninger gemmes i en 'txt' fil.

Lav derfor i roden af projektet en fil kaldet 'credentials.txt', og indtast først dit CPR-nummer og din PIN adskilt af et mellemrum.

#### Kør scriptet
Når alt er på plads, så eksekveres scriptet blot ved køre følgende kommando i roden af dit projekt:
```bash
python3 main.py
```
