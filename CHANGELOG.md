# Changelog

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
