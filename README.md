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

## Sovelluksen tämänhetkinen toiminnallisuus

Ravintolasovellus käynnistyy yleisnäkymään, jossa näytetään kaikki lisätyt ravintolat. 

Näkymästä voi navigoida eteenpäin seuraaviin toimintoihin:
- Uuden ravintolan luonti
- Ravintolan haku
- Näkymät ravintoloiden ja arvostelujen poistamista tai palauttamista varten
- Sisäänkirjautuminen
  - Tältä sivulta voi siirtyä uuden tilin rekisteröintiin
- Ravintolan näkymä, jossa näytetään ravintolan arvostelut ja arvostelujen keskiarvopisteytys, jos arvosteluja on annettu
  - Tältä sivulta voi siirtyä arvostelun tekemiseen ravintolalle 

Sovellukseen voi luoda tilin (normaali käyttäjä tai ylläpitäjä), ja kirjautua sisään. Ylläpitäjä saa joitakin ylimääräisiä toiminnallisuuksia käyttöönsä, kuten kirjausten poiston ja palautuksen. 

Osassa sovelluksen toiminnallisuuksista on käyttäjäroolin ja CSRF-tokenin tarkistus. Näihin toiminnallisuuksiin lukeutuvat sellaiset, jotka lisäävät tai muokkaavat tietoa (ravintolan/arvostelun lisäys tai poisto / poistetun ravintolan/arvostelun palautus).

Sovellukseen on tarkoitus toteuttaa vielä Q&A-osio, jossa käyttäjät voivat kysyä ja vastata ravintoloihin liittyviin mietteisiin. 

Sovellus ei ainakaan toistaiseksi tarjoa käyttäjälle mahdollisuutta järjestellä tietoja oman mielensä mukaan, vaan ravintolat järjestetään ensisijaisesti kirjaustyypin (bucketlist-ravintola tai käyty ravintola) ja toissijaisesti nimen eli aakkosjärjestyksen mukaan. Arvostelut järjestetään ensisijaisesti pisteytyksen eli tähtien mukaan, suurin ensin.

### Kuvakaappauksia käyttöliittymästä

#### Yleisnäkymä

![yleisnäkymä](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/4a4f4822-b92f-4048-8c7f-681955bea63a)

#### Ravintolan näkymä

Arvosteluihin on tarkoituksena lisätä vielä arvostelun tekijän nimi.

![arvostelut](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/a4a02c02-3ed7-48d9-b9c8-0fd55478c8be)


## Käynnistysohjeet

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
> [!TIP]
> Oman salaisen avaimen voi luoda esimerkiksi näin.
```
$ python3
>>> import secrets
>>> secrets.token_hex(16)
'18fd24bf6a2ad4dac04a33963db1c42f'
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
