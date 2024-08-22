
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_info = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
            planet_info.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
    return planet_info

def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda p: float(p['mass']) if p['mass'] != 'N/A' else 0)
    return heaviest['name'], heaviest['mass']

planets = fetch_planet_data()
for planet in planets:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']} kg, Orbit Period: {planet['orbit_period']} days")

name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")

fetch_planet_data()