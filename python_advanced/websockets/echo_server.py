#!/usr/bin/env python3
import asyncio
import websockets


async def gerer_client(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(gerer_client, "localhost", 8765):
        await asyncio.Future()


asyncio.run(main())
