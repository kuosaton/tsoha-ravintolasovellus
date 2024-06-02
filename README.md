# Ravintolasovellus

## Kuvaus

Sovelluksen avulla käyttäjä voi pitää kirjaa kulinaristisista seikkailuistaan. Käyttäjä voi lisätä sovellukseen ravintoloita, joissa on käynyt tai joissa haluaisi käydä, toimien kirjanpito/bucketlist-sovelluksena.

Sovelluksen toimintoja:
- Käyttäjä voi luoda uuden ravintolan, jossa on käynyt, tai ravintolan, jossa haluaisi käydä, sekä kuvauksen sille.
- Käyttäjä voi eritellä ravintolat käytyihin ja käymättömiin.
- Käyttäjä voi poistaa ravintolan.
- Käyttäjä voi antaa ravintolalle arvostelun.
- Käyttäjä voi muokata ravintolan tietoja, esimerkiksi merkitäkseen bucketlist-ravintolan käydyksi ja antaakseen sille arvostelun.
- Käyttäjä voi luoda ravintolakategorioita eritelläkseen niitä tyypin mukaan, esimerkiksi alkuperämaa (kreikkalainen keittiö, tms.), tyyli (lounas, buffet, casual, fine dining, tms.) tai hintataso.
- Käyttäjä voi etsiä ja järjestää ravintoloita nimen, kategorian, kuvauksen avainsanan tai arvostelupisteytyksen perusteella.
- Käyttäjä voi tarkastella yllämainittuihin asioihin liittyviä tilastoja, esimerkiksi arvostelupisteyksien keskiarvo tai yleisin arvosana, suosituin keittiökulttuuri, tms.

## Sovelluksen tämänhetkinen tilanne

Ravintolasovellus käynnistyy yleisnäkymään, jossa näytetään kaikki lisätyt ravintolat eriteltyinä vierailtuihin ja vielä vierailemattomiin bucketlist-ravintoloihin. Näkymä tarjoaa linkit uusien ravintoloiden luomiseksi, olemassaolevien ravintoloiden omiin näkymiin navigoimisen, sekä hakuominaisuuden.

Sovellus ei vielä tarjoa mahdollisuutta poistaa, järjestellä tai muokata tietoja.

### Yleisnäkymä

![Yleisnäkymä](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/49e94037-dcff-44db-acbe-4583a8dfa34f)

Ravintolaa luotaessa kysytään tyypistä riippuen hieman eriäviä tietoja. Uutta bucketlist-ravintolaa pyytäessä määritellään sille nimi, lyhyt kuvaus, kategoria sekä osoite. Jos luodaan vierailtu ravintola, sovellus pyytää lisäksi arvion (1-5 tähteä) sekä valinnaisen sanallisen arvostelun.

### Bucketlist-ravintolan luonti

![Bucketlist-luonti](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/78e9a584-c2a3-48c1-b5f4-70c0464de687)

### Vieraillun ravintolan luonti

![Vieraillun-luonti](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/7307cb29-96ed-4510-90e7-664ac26ae03a)

### Hakuominaisuus

![Hakuominaisuus](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/c7a6b638-e26c-4c56-9ecc-5393b5c5ba8b)

Hakuominaisuus on case-insensitive, eli isoilla alkukirjaimilla ei ole väliä.

### Ravintolan lisätietonäkymä

![Ravintola-view-1](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/4feec9c6-4e87-4916-a171-e411ba81aa01)

![Ravintola-view-2](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/05964e37-4c21-4f00-89fa-d29b456658d2)


## Käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
```
DATABASE_URL=<tietokannan-paikallinen-osoite>
```
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```
Määritä vielä tietokannan skeema komennolla
```
$ psql < schema.sql
```
Nyt voit käynnistää sovelluksen komennolla
```
$ flask run
```
