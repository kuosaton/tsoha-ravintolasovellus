# Ravintolasovellus

## Esittely 

Ravintolasovelluksen avulla käyttäjät voivat pitää kirjaa ja pysyä aina ajan tasalla kulinaristisista seikkailuistaan.

Käyttäjät voivat kirjata ylös ravintoloita, joissa ovat käyneet, tai bucketlist-ravintoloita, joissa haluaisivat käydä. Luotavalle ravintolalle määritellään lisäksi nimi, kuvaus, kategoria, yhteystiedot ja aukioloajat. 

Käyttäjät voivat lisätä ravintoloille arvosteluja, ja ravintolan Q&A-osio tarjoaa käyttäjille mahdollisuuden luoda kysymyksiä ja vastauksia ravintolaan liittyen.

## Toiminnallisuudet pähkinänkuoressa

> [!NOTE]
> Tämä on ajantasainen ja lopullinen kuvaus sovelluksen toiminnallisuuksista su 30.6.2024.

- [x] Sovellukseen voi luoda käyttäjätilin (tilin taso voi olla tavallinen tai ylläpitäjä)
- [x] Käyttäjät voivat luoda ja tarkastella ravintolakirjauksia
  - [x] Luodun ravintolan voi poistaa
  - [x] Luodun ravintolan tietoja voi muokata 
- [x] Käyttäjät voivat antaa arvosteluja ravintoloille
  - [x] Luodun arvostelun voi poistaa
- [x] Käyttäjät voivat etsiä ravintoloita hakusanalla
- [x] Q&A: Käyttäjät voivat luoda ravintoloihin liittyviä kysymyksiä sekä vastata niihin
  - [x] Kysymyksiä ja vastauksia voi poistaa 

### Jatkokehitysideoita
- [ ] Käyttäjä voi tarkastella yllämainittuihin asioihin liittyviä tilastoja, esimerkiksi arvostelupisteyksien keskiarvo tai yleisin arvosana, suosituin keittiökulttuuri, tms.

## Sovelluksen kuvaus

Sovellus käynnistyy etusivulle, jossa näytetään kaikki lisätyt ravintolat. 

### Navbar
Sovelluksen yläosassa aina näkyvä navbar mahdollistaa helpon navigoimisen seuraaviin toimintoihin:
1. Uuden ravintolan luonti
2. Ravintolan haku
3. (Vain ylläpitäjille näkyvä) Dropdown-valikko, joka sisältää linkit näkymiin ravintolan/arvostelun/kysymyksen/vastauksen poistamista/palauttamista varten
4. (Vain uloskirjautuneille näkyvä) Sisäänkirjautuminen
    - Tältä sivulta voi siirtyä eteenpäin uuden tilin rekisteröintiin
5. (Vain sisäänkirjautuneille näkyvä) Dropdown-valikko, joka sisältää linkit käyttäjäprofiiliin ja uloskirjautumiseen


### Ravintolan näkymä
Etusivun (tai hakutoiminnon) kautta voi siirtyä tarkastelemaan luotua ravintolaa. Ravintolan näkymässä näytetään sen tiedot, arvostelut sekä Q&A-osio. Sivu sisältää sisäänkirjautuneille käyttäjille näkyvän dropdown-valikon toiminnalisuuksien käyttöön seuraavilla toiminnallisuuksilla:
- (Vain ylläpitäjille näkyvä) Ravintolan tietojen muokkaus
- Arvostelun, kysymyksen tai vastauksen luonti

## Käyttäjäjärjestelmä

Sovellukseen voi luoda tilin (normaali käyttäjä tai ylläpitäjä), ja kirjautua sisään. Ylläpitäjä saa ylimääräisiä toiminnallisuuksia käyttöönsä – nämä liittyvät luodun tiedon muokkaamiseen, poistamiseen ja palauttamiseen.

Ravintolat järjestetään ensisijaisesti kirjaustyypin (bucketlist-ravintola tai käyty ravintola) ja toissijaisesti nimen eli aakkosjärjestyksen mukaan. Arvostelut järjestetään ensisijaisesti pisteytyksen eli tähtien mukaan, suurin ensin.

## Tietoturva

Tietoa lisäävissä tai muokkaavissa toiminnallisuuksista on käyttäjäroolin ja CSRF-tokenin tarkistus. Esimerkkinä ravintolakirjauksen tai arvostelun poisto tai palautus.

SQL-injektio ja XSS-haavoittuvuudet on huomioitu ja estetty tietokannan käsittelyn toteutuksessa.

## Virheenkäsittely

Sovelluksella on virhesivu (ks. [error.html](/templates/error.html)), johon käyttäjä ohjataan jonkin virheen yllättäessä. Sivu näyttää virhekoodin ja selitteen virheelle, jos sellaiset on annettu. 

Käyttäjä viedään sivulle esimerkiksi silloin, kun etsittyä sivua ei löydy (virhe 404).

<details open>

<summary> Kuvakaappauksia virhesivusta (collapsible) </summary>

#### Virhesivu 404:

![virhe404](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/c2531840-ab03-4155-8eb0-f476288d150b)


#### Virhesivu, kun ravintolan tietojen muokkaus epäonnistuu:

![virhe7](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/1dbdf154-5ee8-43a6-a18c-eb424c7860b9)


</details>

## Kuvia käyttöliittymästä

<details open>

<summary> Kuvakaappauksia käyttöliittymästä (collapsible) </summary>


#### Etusivu:

![etusivu](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/bdb9bcf7-616b-4f11-ba52-769aa0ae4823)

#### Ravintolakirjauksen luonti:

![ravintolan_luonti](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/bdf160e9-1bf6-4921-b802-61e219d4dea8)


Esimerkkejä ravintolan sisäisestä näkymästä asiakaskäytössä.

#### Ravintolanäkymä, esimerkki 1:

![ravintola](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/2c201a4a-ff54-4aa7-bbd6-259381e45ba9)

#### Ravintolanäkymä, esimerkki 2:

![ravintola2](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/2d3625b2-2a57-45bc-acc1-f21d865929e9)

#### Hakuominaisuus:

![hakutoiminto](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/762bd9ff-805b-460a-8ed2-b94fc70ff50f)

#### Profiili:

![profiili](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/4e2a8213-c4be-43b6-9e14-9ec73be0b81e)

</details>

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
