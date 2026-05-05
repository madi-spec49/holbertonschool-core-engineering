# 🔁 Python Control Flow

Ce document présente les bases du **contrôle de flux** en Python, c’est-à-dire la manière dont un programme décide **quoi exécuter** et **quand**.

---

## 📌 1. Conditions (`if`, `elif`, `else`)

Les conditions permettent d’exécuter du code selon une situation.

```python
age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Just adult")
else:
    print("Adult")