# Foglalkozás-egészségügyi vizsgálat

Egy időpontfoglaló rendszert kell implementálni. Az orvosnál naponta 9:00 és 17:00 között
vannak időpontok fél óránként. Ide foglalhatnak időpontokat az alkalmazottak.
Rögzíteni kell azt is, hogy az adott alkalmazott megjelent-e a vizsgálaton.

Amit regisztrációkor meg kell adni:

* Teljes név
* Születési idő
* E-mail cím
* TAJ szám

Amikor regisztrálja magát, a következőket kell megvalósítani:

* Ellenőrizzük, a név nem lehet üres
* Születési idő `1970-10-01` formátumú, 1920 előtti nem lehet, 2025 utáni nem lehet
* Az e-mail cím legyen formaliag helyes, elegendő, ha legalább 3 karakter, és van benne egy `@` karakter
* A TAJ számot CDV ellenőrzésnek kell alávetni
* Ellenőrizni kell, hogy az adott TAJ számmal nem-e regisztrálta-e magát

A CDV ellenőrzés algoritmusa:

> A TAJ szám első nyolc számjegyéből a páratlan helyen állókat hárommal, a páros helyen állókat héttel szorozzuk, és a szorzatokat összeadjuk. 
> Az összeget tízzel elosztva a maradékot tekintjük a kilencedik, azaz CDV kódnak.

Egy napra vonatkozóan fájlba kell írni a regisztráltakat, ezt reggel megkapja az orvos.

## Technológiai javaslatok

Konzolos menürendszer:

```
1. Alkalmazottat regisztrálok
2. Rögzítem, hogy az alkalmazott megjelent
3. Fájlba írás
99. Kilépés
```

A regisztrációkat egy listába tartsuk nyilván. A lista elemei dictionary-k legyenek.

```python
{"name": "John", "day_of_birth": "1920-01-01", "email": "john@example.com", "taj": "12345", "attended": False}
```

(Gyorsabb lesz a keresés, ha nem listát, hanem dictionary-t alkalmazol, ahol a kulcs a TAJ szám.)
(Bátrabbak használhatnak osztályt is.)

A program elindításakor töltsük be a regisztrációkat egy JSON fájlból. Kilépéskor mentsük el egy JSON fájlba.

Dátum ellenőrzésénél használjunk `split()`-et, majd az első értéket konvertáljuk egész számmá, így lesz meg az év.

CDV ellenőrzésnél ciklussal végig lehet menni a számjegyeken, amiket egész számmá kell konvertálni.

Egy TAJ szám csak egyszer szerepelhet, itt használható keresés.

Megjelenés rögzítésekor csak a TAJ számot kell megadni.

Próbálj két fájlt használni, az egyikbe kerül a `print` és `input`, a másikba a logikát tartalmazó függvények.

Az ellenőrzések egyértelműen azonosíthatók, hogy külön függvénybe érdemes őket tenni.

Írj teszt eseteket a logikát tartalmazó függvényekhez!

A fájlba íráskor meg kell adni egy dátumot! Az arra a napra jelentkezetteket írja ki CSV formátumban!

Belátásodra bízom, hogy mennyire használod az AI-t.


