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
- Poistettujen ravintoloiden näkymä, jossa voi tarkastella ja palauttaa poistettuja kirjauksia
- Sisäänkirjautuminen
  - Tältä sivulta voi siirtyä uuden tilin rekisteröintiin
- Ravintolaspesifinen näkymä, jossa näytetään ravintolan arvostelut ja arvostelujen keskiarvopisteytys
  - Tältä sivulta voi siirtyä arvostelun tekemiseen ravintolalle 

Sovellukseen voi luoda tilin (normaali käyttäjä tai ylläpitäjä), ja kirjautua sisään. Ylläpitäjä saa joitakin ylimääräisiä toiminnallisuuksia käyttöönsä, kuten kirjausten poiston ja palautuksen. 

Sovelluksessa on osittainen käyttäjäroolin ja CSRF-tokenin tarkistus. Tämä ei vielä kata kaikkia toiminnallisuuksia.

Ravintolaa luodessa määritetään seuraavat kriteerit: 
- Kirjauksen tyyppi (Onko ravintolassa jo käyty, vai meneekö se bucketlistille?)
  - Sovelluksen rakenteeseen on tämän suhteen tehty parannuksia – visited_restaurants ja bucketlist_restaurants on yhdistetty yhdeksi restaurants-tauluksi, ja määritys tapahtuu nyt yksinkertaisemmin entry_type -attribuutilla. 
- Nimi
- Kuvaus
- Kategoria (Tämä on vapaasti käyttäjän määriteltävissä, ja voi olla esimerkiksi alkuperämaa tai tyyli)
- Osoite
- Aukioloajat

Sovellukseen on tarkoitus toteuttaa vielä Q&A-osio, jossa käyttäjät voivat kysyä ja vastata ravintoloihin liittyviin mietteisiin. 

Sovellus ei ainakaan toistaiseksi tarjoa käyttäjälle mahdollisuutta järjestellä tietoja oman mielensä mukaan, vaan ravintolat järjestetään ensisijaisesti kirjaustyypin (bucketlist-ravintola tai käyty ravintola) ja toissijaisesti nimen eli aakkosjärjestyksen mukaan.

### Kuvakaappaus tämänhetkisestä käyttöliittymästä

Kuvan esimerkkitilanteessa sisään on kirjauduttu admin-tason tilillä, jonka johdosta kirjauksissa näytetään "Poista ravintola" -painikkeet. Normaalin tason käyttäjälle tätä ei näy.

![yleisnäkymä](https://github.com/kuosaton/tsoha-ravintolasovellus/assets/120479105/2dba3f91-7456-4c2e-b783-235b6f566c2d)


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
