# Python - Exception Handling

## 📌 Description
Ce projet présente les bases de la gestion des exceptions en Python.  
L’objectif est d’apprendre à détecter, intercepter et gérer les erreurs afin de rendre les programmes plus robustes et plus fiables.

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, vous serez capable de :

- Comprendre ce qu’est une exception en Python
- Utiliser les blocs `try`, `except`, `else` et `finally`
- Lever des exceptions avec `raise`
- Créer des exceptions personnalisées
- Éviter les interruptions inattendues dans un programme
- Écrire un code plus sécurisé et maintenable

---

## 📚 Concepts abordés

### Gestion basique des exceptions

```python
try:
    number = int(input("Entrez un nombre : "))
    print(number)
except ValueError:
    print("Erreur : veuillez entrer un nombre valide.")