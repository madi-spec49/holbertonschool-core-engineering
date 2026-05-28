# Python Exception Handling

## Gestion des erreurs en Python

Le handling des exceptions permet d’éviter qu’un programme plante lors d’une erreur.

### Syntaxe de base

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division par zéro impossible")
```

### Plusieurs exceptions

```python
try:
    value = int("abc")
except ValueError:
    print("Conversion invalide")
except Exception as e:
    print(f"Erreur : {e}")
```

### Bloc `finally`

Le bloc `finally` s’exécute toujours.

```python
try:
    file = open("data.txt")
finally:
    print("Fin du traitement")
```

### Lever une exception

```python
raise ValueError("Valeur incorrecte")
```

## Bonnes pratiques

* Capturer uniquement les exceptions nécessaires
* Utiliser `finally` pour libérer les ressources
* Éviter les `except:` génériques
* Ajouter des messages d’erreur clairs
