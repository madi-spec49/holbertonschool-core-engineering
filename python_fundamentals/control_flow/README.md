# Control Flow en Python 🐍

## Table des matières
1. [Introduction](#introduction)
2. [Conditions (if/elif/else)](#conditions)
3. [Boucles (for/while)](#boucles)
4. [Break et Continue](#break-et-continue)
5. [Opérateurs de Comparaison](#opérateurs-de-comparaison)
6. [Opérateurs Logiques](#opérateurs-logiques)
7. [Exemples Pratiques](#exemples-pratiques)

---

## Introduction

Le **control flow** (flux de contrôle) permet à un programme de **prendre des décisions** et de **répéter des actions**.

Il y a deux catégories principales :
- **Conditions** : if, elif, else
- **Boucles** : for, while

---

## Conditions

### if (si)

Exécute du code **si** une condition est vraie.

```python
age = 15

if age < 13:
    print("Tu es un enfant")
```

**Résultat :** Rien ne s'affiche (condition fausse)

### elif (sinon si)

Teste une **deuxième condition** si la première est fausse.

```python
age = 15

if age < 13:
    print("Tu es un enfant")
elif age < 18:
    print("Tu es un ado")
```

**Résultat :** Affiche "Tu es un ado"

**Important :** Une seule branche s'exécute !

### else (sinon)

Exécute du code si **toutes** les conditions précédentes sont fausses.

```python
age = 70

if age < 13:
    print("Tu es un enfant")
elif age < 18:
    print("Tu es un ado")
elif age < 65:
    print("Tu es un adulte")
else:
    print("Tu es retraité")
```

**Résultat :** Affiche "Tu es retraité"

### Structure complète

```python
if [condition 1]:
    # Code si condition 1 est TRUE
elif [condition 2]:
    # Code si condition 1 est FALSE ET condition 2 est TRUE
elif [condition 3]:
    # Code si conditions 1,2 sont FALSE ET condition 3 est TRUE
else:
    # Code si TOUTES les conditions sont FALSE
```

---

## Boucles

### for (boucle sur une séquence)

Exécute du code **pour chaque élément** d'une liste, range, string, etc.

#### Exemple 1 : Boucle sur une liste

```python
fruits = ["pomme", "banane", "orange"]

for fruit in fruits:
    print(fruit)
```

**Résultat :**
```
pomme
banane
orange
```

#### Exemple 2 : Boucle sur range()

```python
for i in range(5):
    print(i)
```

**Résultat :**
```
0
1
2
3
4
```

**Note :** `range(5)` génère 0, 1, 2, 3, 4 (5 n'est PAS inclus)

#### Exemple 3 : Boucle sur une string

```python
mot = "bonjour"

for lettre in mot:
    print(lettre)
```

**Résultat :**
```
b
o
n
j
o
u
r
```

### while (boucle tant que)

Exécute du code **tant qu'une condition est vraie**.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

**Résultat :**
```
0
1
2
3
4
```

**Attention :** Il faut **modifier** la variable pour que la condition devienne fausse, sinon c'est une boucle infinie !

### for vs while

| for | while |
|-----|-------|
| Boucle sur une séquence | Boucle tant que condition |
| Nombre d'itérations connu | Nombre d'itérations inconnu |
| `for i in range(5)` | `while x > 0` |

---

## Break et Continue

### break (arrêter la boucle)

Quitte la boucle **immédiatement**.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Résultat :**
```
0
1
2
3
4
```

La boucle s'arrête quand `i` atteint 5.

### continue (sauter l'itération)

Saute à la **prochaine itération** de la boucle.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Résultat :**
```
0
1
3
4
```

L'itération où `i == 2` est sautée.

---

## Opérateurs de Comparaison

| Opérateur | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `==` | Égal | `5 == 5` | True |
| `!=` | Pas égal | `5 != 3` | True |
| `<` | Plus petit que | `3 < 5` | True |
| `>` | Plus grand que | `5 > 3` | True |
| `<=` | Plus petit ou égal | `5 <= 5` | True |
| `>=` | Plus grand ou égal | `5 >= 5` | True |

**Exemple :**
```python
age = 20

if age >= 18:
    print("Tu es majeur")
```

---

## Opérateurs Logiques

### and (ET)

Les **deux conditions** doivent être vraies.

```python
age = 20
permis = True

if age >= 18 and permis:
    print("Tu peux conduire")
```

**Résultat :** Affiche "Tu peux conduire"

### or (OU)

**Au moins une** condition doit être vraie.

```python
day = "samedi"

if day == "samedi" or day == "dimanche":
    print("C'est le weekend!")
```

**Résultat :** Affiche "C'est le weekend!"

### not (NON)

Inverse la condition (vrai devient faux, faux devient vrai).

```python
ageValide = False

if not ageValide:
    print("L'âge n'est pas valide")
```

**Résultat :** Affiche "L'âge n'est pas valide"

### Tableau récapitulatif

| Opérateur | Signification | Exemple | Résultat |
|-----------|---------------|---------|----------|
| `and` | ET logique | `True and False` | False |
| `or` | OU logique | `True or False` | True |
| `not` | NON logique | `not True` | False |

---

## Exemples Pratiques

### Exemple 1 : Classification de nombres

```python
#!/usr/bin/env python3

number = 15

if number < 0:
    print("Négatif")
elif number == 0:
    print("Zéro")
elif number > 0 and number < 10:
    print("Positif (petit)")
else:
    print("Positif (grand)")
```

**Output :** `Positif (petit)`

### Exemple 2 : Afficher l'alphabet sans 'e' et 'q'

```python
#!/usr/bin/env python3

alphabet = list(range(97, 123))
alphabt = ""

for ascii in alphabet:
    if ascii != 101 and ascii != 113:
        letter = chr(ascii)
        alphabt += letter

print(alphabt)
```

**Output :** `abcdfghijklmnoprstuvwxyz`

### Exemple 3 : Nombre aléatoire (positif/zéro/négatif)

```python
#!/usr/bin/env python3

number = __import__('random').randint(-10, 10)

if number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is negative")
```

**Output possible :** `-5 is negative`

### Exemple 4 : Boucle avec break

```python
#!/usr/bin/env python3

for i in range(10):
    if i == 5:
        print("On arrête à 5!")
        break
    print(i)
```

**Output :**
```
0
1
2
3
4
On arrête à 5!
```

### Exemple 5 : Boucle avec continue

```python
#!/usr/bin/env python3

for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Output :**
```
0
1
3
4
```

---

## Résumé

### Conditions
- `if` : teste une condition
- `elif` : teste une autre condition (si la première est fausse)
- `else` : exécute si toutes les conditions sont fausses
- **Une seule branche s'exécute !**

### Boucles
- `for` : boucle sur une séquence
- `while` : boucle tant qu'une condition est vraie
- `break` : quitte la boucle
- `continue` : saute à la prochaine itération

### Opérateurs
- **Comparaison** : `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logiques** : `and`, `or`, `not`

---

## Points clés à retenir

✅ **Une condition if/elif/else = une seule branche exécutée**

✅ **for = boucle sur une séquence** (nombre d'itérations connu)

✅ **while = boucle tant que condition vraie** (nombre d'itérations inconnu)

✅ **break = arrêter la boucle**

✅ **continue = sauter à la prochaine itération**

✅ **and = les DEUX conditions doivent être vraies**

✅ **or = AU MOINS UNE condition doit être vraie**

---

## Exercices

1. Écris un programme qui affiche les nombres de 1 à 10, sauf les nombres pairs.
2. Écris un programme qui demande l'âge et affiche si c'est un enfant (< 13), ado (13-18), ou adulte (> 18).
3. Écris une boucle while qui compte de 10 à 0 et s'arrête.

---

**Créé pour apprendre le Control Flow en Python 🚀**