#!/usr/bin/env python3
import asyncio
import websockets

async def gerer_client(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    # Essaie d'abord avec 127.0.0.1
    try:
        async with websockets.serve(gerer_client, "127.0.0.1", 8765):
            await asyncio.Future()
    except OSError:
        # Si ça échoue, essaie avec localhost
        async with websockets.serve(gerer_client, "localhost", 8765):
            await asyncio.Future()

asyncio.run(main())