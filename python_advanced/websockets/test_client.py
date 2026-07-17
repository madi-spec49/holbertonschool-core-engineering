#!/usr/bin/env python3
import asyncio
import websockets

async def main():
    try:
        async with websockets.connect('ws://localhost:8765') as ws:
            print("Connecté! Tapez vos messages (Ctrl+C pour quitter)")
            while True:
                msg = input("> ")
                await ws.send(msg)
                print(await ws.recv())
    except ConnectionRefusedError:
        print("Serveur non démarré!")

asyncio.run(main())
