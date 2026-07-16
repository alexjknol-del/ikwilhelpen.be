# ikwilhelpen.be

Broncode van de website ikwilhelpen.be: een statische site zonder build-afhankelijkheden, gehost via Cloudflare Pages.

## Structuur

- `site/` — de volledige, kant-en-klare website (HTML/CSS/afbeeldingen). Dit is de map die live staat op ikwilhelpen.be. Cloudflare Pages serveert deze map rechtstreeks, er is geen build-commando nodig.
- `generator/` — een klein Python-scriptje waarmee de site opnieuw gegenereerd kan worden, handig om later eenvoudig een nieuw artikel toe te voegen zonder alle HTML met de hand te herschrijven. Dit is puur een hulpmiddel voor onderhoud en wordt niet live gehost.

## Cloudflare Pages instellingen

- Build command: (leeg laten)
- Build output directory: `site`

Zolang deze instellingen zo staan, wordt bij elke push naar de hoofdbranch automatisch de inhoud van `site/` gepubliceerd.

## Een nieuw artikel toevoegen

1. Open `generator/content.py` en voeg een nieuw item toe aan de lijst `ARTICLES`, naar analogie van de bestaande artikelen (titel, datum, samenvatting, en de volledige tekst als HTML in `body`).
2. Run vanuit de map `generator/`:

   ```
   python3 pages.py
   ```

3. Dit genereert de volledige site opnieuw in `site/`, inclusief de nieuwe artikelpagina, het bijgewerkte nieuwsoverzicht, de homepage en de sitemap.
4. Commit en push de wijzigingen in `site/` (en `generator/content.py`) naar GitHub. Cloudflare Pages publiceert de wijziging automatisch.

Vereist enkel Python 3, geen extra packages.

## Domeinkoppeling

Het domein ikwilhelpen.be wordt gekoppeld aan Cloudflare Pages via het Cloudflare-dashboard onder het tabblad "Custom domains" van het Pages-project.
