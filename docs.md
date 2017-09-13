# Tietojohtajakillan infotaulun dokkari
## Tiedostot:

- bussiapi_to_file.py
- db
  - bussit.json
- jquery-3.2.1.min.js
- sivu.html

## Tiedostojen selitykset:
### bussiapi_to_file.py
`bussiapi_to_file.py` hakee tiedot internetistä rajapinnasta ja tallettaa ne db/bussit.json -tiedostoon.
### sivu.html
`sivu.html` näyttää ja pyörittää javascriptiä. Javascriptit siirretään ehkä erillisiin tiedostoihin
### db/bussit.json
`db/bussit.json` sisältää rajapinnasta saadun json-tiedoston

## Muuta:
### Tiedostoserveri
```
sudo apt install nodejs
sudo npm install http-server -g
cd projektin juuri
http-server --cors -c-1 -p 8080
```
### Cronjobs
- `* * * * * bussiapi_to_file.py` Bussit päivittymään kerran minuutissa
- `0 0 * * * ruokaapi_to_file.py` Ruoat päivittymään kerran päivässä
