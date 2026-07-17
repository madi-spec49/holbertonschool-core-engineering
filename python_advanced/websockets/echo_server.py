#!/usr/bin/env python3
import asyncio
import websockets


async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        print("Serveur WebSocket démarré sur ws://localhost:8765")
        print("En attente de connexions...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
