# 📚 Core Data Structures en Python

## Table des matières / Table of Contents

1. [Introduction](#introduction)
2. [Les 4 Structures Principales](#les-4-structures-principales)
3. [Listes / Lists](#listes--lists)
4. [Tuples](#tuples)
5. [Dictionnaires / Dictionaries](#dictionnaires--dictionaries)
6. [Ensembles / Sets](#ensembles--sets)
7. [Comparaison](#comparaison)
8. [Cas d'usage / Use Cases](#cas-dusage--use-cases)

---

## Introduction

Les **structures de données** sont des conteneurs qui stockent et organisent les données en Python.
**Data structures** are containers that store and organize data in Python.

Il existe **4 structures principales** en Python:
- **Lists** 📋 (Listes ordonnées, modifiables)
- **Tuples** 📦 (Tuples ordonnés, immuables)
- **Dictionaries** 🗂️ (Paires clé-valeur)
- **Sets** 🎯 (Ensembles uniques, non ordonnés)

---

## Les 4 Structures Principales

```
┌─────────────────────────────────────────────────────────┐
│           PYTHON DATA STRUCTURES                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. LIST        2. TUPLE      3. DICT      4. SET      │
│  Mutable        Immutable     Key-Value    Unique      │
│  Ordered        Ordered       Ordered*     Unordered   │
│  [1,2,3]        (1,2,3)       {...}        {1,2,3}     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Listes / Lists

### Qu'est-ce qu'une liste? / What is a list?

Une **liste** est une collection **ordonnée** et **modifiable** d'éléments.
A **list** is an ordered and **mutable** collection of elements.

### Créer une liste / Create a list

```python
# Créer une liste vide / Create an empty list
fruits = []

# Créer une liste avec des éléments / Create a list with elements
fruits = ["pomme", "banane", "cerise"]
fruits = ["apple", "banana", "cherry"]

# Créer une liste mixte / Create a mixed list
mixed = [1, "hello", 3.14, True, None]

# Créer une liste imbriquée / Create a nested list
nested = [1, [2, 3], [4, [5, 6]]]
```

### Accéder aux éléments / Access elements

```python
fruits = ["pomme", "banane", "cerise"]

# Index positif (commence à 0) / Positive indexing (starts at 0)
print(fruits[0])    # "pomme" / "apple"
print(fruits[1])    # "banane" / "banana"
print(fruits[-1])   # "cerise" (dernier / last)
print(fruits[-2])   # "banane" (avant-dernier / second-to-last)

# Slicing (découper) / Slicing
print(fruits[0:2])      # ["pomme", "banane"]
print(fruits[1:])       # ["banane", "cerise"]
print(fruits[:2])       # ["pomme", "banane"]
print(fruits[::2])      # ["pomme", "cerise"] (tous les 2)
print(fruits[::-1])     # ["cerise", "banane", "pomme"] (inverser)
```

### Modifier une liste / Modify a list

```python
fruits = ["pomme", "banane", "cerise"]

# Ajouter un élément / Add an element
fruits.append("date")           # Ajoute à la fin
fruits.insert(1, "raisin")      # Insère à l'index 1

# Modifier un élément / Modify an element
fruits[0] = "orange"            # Remplace "pomme"

# Supprimer un élément / Remove an element
fruits.remove("banane")         # Supprime par valeur
fruits.pop()                    # Supprime le dernier
fruits.pop(0)                   # Supprime l'index 0
del fruits[0]                   # Supprime aussi par index

# Vider une liste / Clear a list
fruits.clear()
```

### Méthodes utiles / Useful methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Trier / Sort
numbers.sort()                  # Trie sur place [1, 1, 2, 3, 4, 5, 6, 9]
sorted_nums = sorted(numbers)   # Retourne une nouvelle liste

# Inverser / Reverse
numbers.reverse()               # Inverse sur place
reversed_nums = numbers[::-1]   # Crée une nouvelle liste

# Compter / Count
count = numbers.count(1)        # Compte combien de 1

# Index
index = numbers.index(4)        # Trouve l'index de 4

# Longueur / Length
length = len(numbers)           # Nombre d'éléments

# Min et Max
minimum = min(numbers)
maximum = max(numbers)

# Somme / Sum
total = sum(numbers)
```

### Boucler sur une liste / Loop through a list

```python
fruits = ["pomme", "banane", "cerise"]

# Boucle for / For loop
for fruit in fruits:
    print(fruit)

# Avec index / With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# List comprehension
squared = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

---

## Tuples

### Qu'est-ce qu'un tuple? / What is a tuple?

Un **tuple** est une collection **ordonnée** et **immuable** (qu'on ne peut pas modifier).
A **tuple** is an ordered and **immutable** (cannot be changed) collection.

### Créer un tuple / Create a tuple

```python
# Créer un tuple / Create a tuple
colors = ("rouge", "vert", "bleu")
colors = ("red", "green", "blue")

# Tuple à un élément (attention à la virgule!) / Single element tuple (note the comma!)
single = (1,)           # ✅ Tuple
single = (1)            # ❌ Juste un nombre / Just a number

# Tuple sans parenthèses / Tuple without parentheses
coords = 10, 20, 30     # ✅ C'est un tuple

# Tuple vide / Empty tuple
empty = ()

# Tuple imbriqué / Nested tuple
nested = (1, (2, 3), (4, (5, 6)))
```

### Accéder aux éléments / Access elements

```python
colors = ("rouge", "vert", "bleu")

# Même qu'une liste / Same as list
print(colors[0])        # "rouge"
print(colors[-1])       # "bleu"
print(colors[0:2])      # ("rouge", "vert")
```

### Pourquoi utiliser des tuples? / Why use tuples?

```python
# ✅ Les tuples sont immuables / Tuples are immutable
coordinates = (10, 20)
# coordinates[0] = 15  # ❌ TypeError: 'tuple' object does not support item assignment

# ✅ Les tuples peuvent être des clés de dictionnaires / Can be dict keys
locations = {
    (10, 20): "Paris",
    (48.8, 2.3): "Eiffel Tower"
}

# ✅ Les tuples sont plus rapides / Tuples are faster
# ✅ Les tuples utilisent moins de mémoire / Use less memory

# ✅ Unpacking / Déballer
x, y, z = (1, 2, 3)
print(x, y, z)          # 1 2 3
```

### Méthodes de tuple / Tuple methods

```python
numbers = (1, 2, 2, 3, 2, 4)

# Compter / Count
count = numbers.count(2)        # 3

# Index
index = numbers.index(3)        # 3

# Longueur / Length
length = len(numbers)

# Min, Max, Sum
minimum = min(numbers)
maximum = max(numbers)
total = sum(numbers)
```

---

## Dictionnaires / Dictionaries

### Qu'est-ce qu'un dictionnaire? / What is a dictionary?

Un **dictionnaire** stocke les données comme des **paires clé-valeur**.
A **dictionary** stores data as **key-value pairs**.

```python
personne = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}

person = {
    "name": "John",
    "age": 25,
    "city": "Paris"
}
```

### Créer un dictionnaire / Create a dictionary

```python
# Dictionnaire vide / Empty dictionary
empty_dict = {}
empty_dict = dict()

# Avec des données / With data
student = {
    "prenom": "Marie",
    "nom": "Dupont",
    "age": 20,
    "notes": [15, 18, 16]
}

# Utiliser le constructeur / Using constructor
person = dict(name="Alice", age=30, city="Lyon")
```

### Accéder aux valeurs / Access values

```python
student = {
    "prenom": "Marie",
    "age": 20
}

# Accéder par clé / Access by key
print(student["prenom"])        # "Marie"
print(student["age"])           # 20

# Utiliser get() (plus sûr) / Using get() (safer)
print(student.get("prenom"))    # "Marie"
print(student.get("ville"))     # None (pas d'erreur)
print(student.get("ville", "Inconnu"))  # "Inconnu" (valeur par défaut)
```

### Modifier un dictionnaire / Modify a dictionary

```python
student = {"nom": "Dupont", "age": 20}

# Ajouter / Add
student["ville"] = "Paris"
student.update({"age": 21, "niveau": "L2"})

# Modifier / Modify
student["age"] = 21
student["nom"] = "Martin"

# Supprimer / Remove
del student["ville"]
student.pop("age")              # Retourne la valeur
student.pop("inexistant", None) # Pas d'erreur si n'existe pas
student.clear()                 # Vide le dictionnaire
```

### Parcourir un dictionnaire / Loop through a dictionary

```python
student = {
    "nom": "Dupont",
    "age": 20,
    "ville": "Paris"
}

# Parcourir les clés / Loop through keys
for key in student:
    print(key)
# Affiche: nom, age, ville

# Parcourir les clés et valeurs / Loop through keys and values
for key, value in student.items():
    print(f"{key}: {value}")
# Affiche:
# nom: Dupont
# age: 20
# ville: Paris

# Parcourir seulement les valeurs / Loop through values only
for value in student.values():
    print(value)

# Parcourir seulement les clés / Loop through keys only
for key in student.keys():
    print(key)
```

### Méthodes utiles / Useful methods

```python
student = {"nom": "Dupont", "age": 20}

# Clés / Keys
keys = student.keys()           # dict_keys(['nom', 'age'])

# Valeurs / Values
values = student.values()       # dict_values(['Dupont', 20])

# Paires clé-valeur / Key-value pairs
items = student.items()         # dict_items([('nom', 'Dupont'), ('age', 20)])

# Longueur / Length
length = len(student)           # 2

# Vérifier si clé existe / Check if key exists
if "nom" in student:
    print("La clé existe")
```

---

## Ensembles / Sets

### Qu'est-ce qu'un ensemble? / What is a set?

Un **ensemble** est une collection **non ordonnée** d'éléments **uniques** (pas de doublons).
A **set** is an unordered collection of **unique** elements (no duplicates).

### Créer un ensemble / Create a set

```python
# Créer un ensemble / Create a set
numbers = {1, 2, 3, 4, 5}
numbers = {5, 2, 4, 1, 3}  # Ordre différent mais même ensemble

# Ensemble vide (attention!) / Empty set (careful!)
empty_set = set()           # ✅ C'est un ensemble
# empty_set = {}            # ❌ C'est un dictionnaire!

# Ensemble à partir d'une liste / Set from a list
fruits = {"pomme", "banane", "cerise", "pomme"}
# Résultat: {"pomme", "banane", "cerise"} (pomme une seule fois)

# Utiliser le constructeur / Using constructor
numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

### Ajouter et supprimer / Add and remove

```python
numbers = {1, 2, 3}

# Ajouter un élément / Add an element
numbers.add(4)          # {1, 2, 3, 4}

# Ajouter plusieurs éléments / Add multiple elements
numbers.update([5, 6])  # {1, 2, 3, 4, 5, 6}

# Supprimer / Remove
numbers.remove(3)       # Erreur si n'existe pas
numbers.discard(3)      # Pas d'erreur si n'existe pas

# Supprimer aléatoire / Remove random
numbers.pop()           # Supprime un élément aléatoire

# Vider / Clear
numbers.clear()
```

### Opérations sur les ensembles / Set operations

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (tout ce qui est dans A ou B) / Union
union = A | B           # {1, 2, 3, 4, 5, 6}
union = A.union(B)

# Intersection (ce qui est dans A et B) / Intersection
intersection = A & B    # {3, 4}
intersection = A.intersection(B)

# Différence (ce qui est dans A mais pas B) / Difference
difference = A - B      # {1, 2}
difference = A.difference(B)

# Différence symétrique (ce qui est dans A ou B mais pas les deux) / Symmetric difference
sym_diff = A ^ B        # {1, 2, 5, 6}
sym_diff = A.symmetric_difference(B)

# Vérifier l'inclusion / Check inclusion
A.issubset(B)           # False (A n'est pas un sous-ensemble de B)
A.issuperset(B)         # False (A n'est pas un sur-ensemble de B)
{1, 2}.issubset(A)      # True
```

### Exemples pratiques / Practical examples

```python
# Éliminer les doublons / Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))     # [1, 2, 3, 4]

# Trouver les éléments communs / Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)   # {3, 4}

# Trouver les différences / Find differences
only_in_list1 = set(list1) - set(list2)  # {1, 2}
```

---

## Comparaison

### Tableau comparatif / Comparison table

| Caractéristique | List | Tuple | Dict | Set |
|-----------------|------|-------|------|-----|
| **Ordonné** | ✅ Oui | ✅ Oui | ✅ Oui* | ❌ Non |
| **Modifiable** | ✅ Oui | ❌ Non | ✅ Oui | ✅ Oui |
| **Doublons** | ✅ Oui | ✅ Oui | N/A | ❌ Non |
| **Clé de dict** | ❌ Non | ✅ Oui | ❌ Non | ❌ Non |
| **Syntaxe** | [1,2,3] | (1,2,3) | {k:v} | {1,2,3} |
| **Rapidité** | Moyen | Rapide | Très rapide | Très rapide |
| **Mémoire** | Plus | Moins | Plus | Moins |

*Dictionnaires ordonnés depuis Python 3.7+

### Quand utiliser quoi? / When to use what?

```python
# LIST / LISTE
# - Besoin de modifier les données
# - Besoin de garder l'ordre
# - Doublons autorisés
fruits = ["pomme", "banane", "cerise"]

# TUPLE / TUPLE
# - Données immuables
# - Clé de dictionnaire
# - Plus de performance
coordinates = (10, 20)
locations = {(10, 20): "Paris"}

# DICTIONARY / DICTIONNAIRE
# - Organiser les données par clé-valeur
# - Recherche rapide par clé
student = {"nom": "Jean", "age": 25}

# SET / ENSEMBLE
# - Éliminer les doublons
# - Opérations mathématiques (union, intersection)
# - Vérifier l'existence rapide
unique_ids = {1, 2, 3, 4, 5}
```

---

## Cas d'usage / Use Cases

### Exemple 1: Gestion d'étudiants / Student management

```python
# Dictionnaire pour un étudiant / Dictionary for a student
student = {
    "id": 101,
    "nom": "Dupont",
    "prenom": "Marie",
    "notes": [15, 18, 16, 17],  # Liste de notes
    "adresse": (48.8566, 2.3522)  # Tuple de coordonnées
}

# Liste d'étudiants / List of students
students = [
    {"id": 101, "nom": "Dupont", "notes": [15, 18, 16]},
    {"id": 102, "nom": "Martin", "notes": [16, 17, 18]},
    {"id": 103, "nom": "Durand", "notes": [14, 15, 16]}
]

# Moyenne des notes / Average grade
def moyenne_notes(student):
    return sum(student["notes"]) / len(student["notes"])

for student in students:
    print(f"{student['nom']}: {moyenne_notes(student):.2f}")
```

### Exemple 2: Analyse de données / Data analysis

```python
# Liste de ventes / Sales data
ventes = [100, 150, 100, 200, 150, 100, 250]

# Ensembles pour l'analyse / Sets for analysis
montants_uniques = set(ventes)     # {100, 150, 200, 250}
nombre_montants = len(montants_uniques)

# Dictionnaire pour les statistiques / Dictionary for statistics
stats = {
    "total": sum(ventes),
    "moyenne": sum(ventes) / len(ventes),
    "minimum": min(ventes),
    "maximum": max(ventes),
    "nombre_ventes": len(ventes)
}

print(stats)
```

### Exemple 3: Opérations sur des ensembles / Set operations

```python
# Clients qui ont acheté en janvier / Clients in January
jan_clients = {"Alice", "Bob", "Charlie", "David"}

# Clients qui ont acheté en février / Clients in February
feb_clients = {"Charlie", "David", "Eve", "Frank"}

# Clients des deux mois / Clients in both months
both_months = jan_clients & feb_clients
print(f"Clients des deux mois: {both_months}")  # {'Charlie', 'David'}

# Nouveaux clients en février / New clients in February
new_clients = feb_clients - jan_clients
print(f"Nouveaux clients: {new_clients}")       # {'Eve', 'Frank'}

# Tous les clients / All clients
all_clients = jan_clients | feb_clients
print(f"Tous les clients: {all_clients}")       # {'Alice', 'Bob', 'Charlie', ...}
```

---

## Résumé / Summary

| Structure | Utilisation | Avantage | Inconvénient |
|-----------|------------|----------|------------|
| **List** | Données modifiables | Flexible | Moins rapide |
| **Tuple** | Données fixes | Immuable, rapide | Pas modifiable |
| **Dict** | Paires clé-valeur | Recherche rapide | Plus de mémoire |
| **Set** | Données uniques | Pas de doublons | Non ordonné |

---

## Ressources / Resources

- 📖 [Python Documentation](https://docs.python.org/3/)
- 🎓 [Real Python - Data Structures](https://realpython.com/python-data-structures/)
- 💻 [GeeksforGeeks - Data Structures](https://www.geeksforgeeks.org/python-data-structures/)

---

**Créé par:** Claude Haiku 4.5  
**Date:** 8 Mai 2026  
**Version:** 1.0