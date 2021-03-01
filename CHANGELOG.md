# Changelog

## Version 0.0.5a (01 March 2021)

Revamps the entire project structure and adds three new namespaces:

- `constants`
- `compsci`
- `mathematics`

```python
import lolicon.constants as const

# 1.67262192369e-27 kilogram
print(const.MassOfProton)
```

Furthermore, this version also adds a new `compsci` namespace for methods that
belong in the realm of computer science. It also contains a `compsci.cryptography`
sub-package for cryptographically insecure (but easy to implement) encryption methods:

```python
from lolicon.compsci import cryptography as crypto

key = crypto.generate_affine_key()
msg = "Hello, World!"
cypher = crypto.encrypt_affine_cypher(msg, key)
# True
print(msg == crypto.decrypt_affine_cypher(cypher, key))
```

The following encryption methods are currently implemented:

- `encrypt_morse_code`
- `encrypt_binary`
- `encrypt_caesar_cypher`
- `encrypt_transposition_cypher`
- `encrypt_affine_cypher`
- `encrypt_vigenere_cypher`

There's no documentation available at the moment, but the doc strings of each
method contain instructions and miscellaneous remarks. Finally, this version also
adds a few math-related methods to this module, inter alia

- `gcd`
- `mod_inverse`
- `sieve_of_eratosthenes`
  
On top of that, this module also provides a CLI. It's pretty barren currently,
but the `--read` option might turn in handy occasionally:

```cli
# get help
lolicon --help

# confirm you're up-to-date
lolicon --version

# colorful log file output!
lolicon log --read
```

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
