# Changelog

## Version 0.0.4a (16 January 2021)

Adds doc strings to all client-facing classes and implements two new classes in
the physics namespace: `Planet` and `Satellite`.

```python
from lolicon.physics import Planet, Satellite

earth = Planet('earth')
moon = Satellite('moon')

# Earth diameter = 12756.0 kilometer
print(f"Earth diameter = {earth.diameter}")
# Moon radius = 1737.5 kilometer
print(f"Moon radius = {moon.radius}")
```

Additionally, all JSON files have been replaced with proper DBs.

## Version 0.0.3a-2 (26 December 2020)

Fix package import error.

## Version 0.0.3a (26 December 2020)

Implements the `Element` class in the `chemistry` namespace for convenient access
of data from the Period System of Elements (PSE).

```python
from lolicon.chemistry import Element

gold = Element('Au')

# 196.967 dalton
print(f"Atomic Mass = {gold.atomic_mass}")
```
