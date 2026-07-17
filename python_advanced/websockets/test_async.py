import asyncio
import time


async def tache(nom, delai):
    print(f"[{nom}] démarre")
    await asyncio.sleep(delai)
    print(f"[{nom}] terminée après {delai}s")


async def main():
    debut = time.time()
    await tache("Tâche A", 3)
    await tache("Tâche B", 1)
    await tache("Tâche C", 2)
    print(f"Temps total : {time.time() - debut:.1f}s")


asyncio.run(main())