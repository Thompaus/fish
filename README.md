# Solunar Bite Forecast

A one-page fishing forecast that rates each species for a spot and date.

It combines:
- **Solunar periods**: major periods (moon overhead or underfoot) and minor periods (moonrise and moonset), plus moon phase.
- **Species habits**: dawn, day, dusk and night activity, moonlight response, season (flipped for the southern hemisphere), preferred water temperature, swell range and pressure sensitivity.
- **Geography**: only species whose native or introduced range covers the spot are listed, and each spot type (drop-off, reef, river mouth, surf…) suits some fish more than others.
- **Worldwide fish records** from [GBIF](https://www.gbif.org): every ray-finned fish recorded within about 30 km of the spot.
- **Map** (Leaflet, CARTO/OpenStreetMap tiles): rated dots for every listed spot, and a quick rating anywhere you tap (place names from OpenStreetMap Nominatim).
- **Live conditions** from [Open-Meteo](https://open-meteo.com) (free, no key): air pressure and its 3-hour trend, sea surface temperature, lake temperature from recent air temperature, and swell.

## Files
- `src/page.html` is the page source.
- `index.html` is built from it with `python3 tools/build.py` and served by GitHub Pages.

Weather data by Open-Meteo.com (CC BY 4.0).
