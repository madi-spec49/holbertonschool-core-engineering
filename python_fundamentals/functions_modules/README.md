# README — Fonctions et Modules en Python

## Introduction

Python est un langage de programmation simple, puissant et très utilisé dans le développement logiciel, la data science, l’automatisation et bien plus encore.

Ce document présente deux notions fondamentales de Python :

* Les **fonctions**
* Les **modules**

---

# 1. Les Fonctions en Python

## Définition

Une fonction est un bloc de code réutilisable permettant d’exécuter une tâche spécifique.

Les fonctions permettent :

* d’éviter la répétition de code ;
* de rendre le programme plus lisible ;
* de faciliter la maintenance.

---

## Syntaxe d’une fonction

```python
def nom_fonction(parametres):
    # instructions
    return resultat
```

---

## Exemple simple

```python
def dire_bonjour():
    print("Bonjour !")

# Appel de la fonction
dire_bonjour()
```

### Résultat

```python
Bonjour !
```

---

## Fonction avec paramètres

```python
def saluer(nom):
    print(f"Bonjour {nom}")

saluer("Alice")
```

---

## Fonction avec valeur de retour

```python
def addition(a, b):
    return a + b

resultat = addition(5, 3)
print(resultat)
```

### Résultat

```python
8
```

---

## Paramètres par défaut

```python
def bienvenue(nom="Utilisateur"):
    print(f"Bienvenue {nom}")

bienvenue()
bienvenue("Lucas")
```

---

## Fonctions anonymes (lambda)

```python
carre = lambda x: x * x

print(carre(4))
```

---

# 2. Les Modules en Python

## Définition

Un module est un fichier Python contenant des fonctions, variables ou classes réutilisables.

Les modules permettent :

* d’organiser le code ;
* de réutiliser des fonctionnalités ;
* de séparer les responsabilités.

---

## Importer un module

```python
import math

print(math.sqrt(16))
```

### Résultat

```python
4.0
```

---

## Importer une fonction spécifique

```python
from math import pi

print(pi)
```

---

## Import avec alias

```python
import numpy as np

liste = np.array([1, 2, 3])
print(liste)
```

---

# 3. Créer son propre module

## Étape 1 : créer un fichier

Créer un fichier nommé :

```python
calculs.py
```

Contenu :

```python
def multiplication(a, b):
    return a * b
```

---

## Étape 2 : utiliser le module

Dans un autre fichier Python :

```python
import calculs

resultat = calculs.multiplication(4, 5)
print(resultat)
```

---

# 4. Modules standards populaires

| Module   | Description                  |
| -------- | ---------------------------- |
| math     | Fonctions mathématiques      |
| random   | Génération aléatoire         |
| datetime | Gestion des dates et heures  |
| os       | Interaction avec le système  |
| sys      | Informations système         |
| json     | Manipulation de données JSON |

---

# 5. Bonnes pratiques

## Pour les fonctions

* Utiliser des noms clairs ;
* Éviter les fonctions trop longues ;
* Ajouter des commentaires si nécessaire.

## Pour les modules

* Séparer les fonctionnalités ;
* Regrouper les fonctions liées ;
* Éviter les imports inutiles.

---

# 6. Exemple complet

## Module `operations.py`

```python
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b
```

## Fichier principal `main.py`

```python
import operations

print(operations.addition(10, 5))
print(operations.soustraction(10, 5))
```

---

# Conclusion

Les fonctions et les modules sont essentiels pour écrire du code Python propre, réutilisable et maintenable.

En maîtrisant ces concepts, vous pourrez développer des projets plus structurés et plus professionnels.

---

# Ressources utiles

* Documentation officielle Python : [https://docs.python.org/fr/3/](https://docs.python.org/fr/3/)
* Tutoriel Python : [https://realpython.com/](https://realpython.com/)
* W3Schools Python : [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
