#!/usr/bin/env python3
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

async def handle_client(websocket):
    """
    Gère les messages d'un client WebSocket.
    Valide chaque message et répond avec OK:message ou ERR:EMPTY.
    """
    try:
        async for message in websocket:
            # Valider le message en supprimant les espaces
            stripped = message.strip()
            
            if len(stripped) == 0:
                # Message vide ou uniquement des espaces
                response = "ERR:EMPTY"
                await websocket.send(response)
            else:
                # Message valide : renvoyer OK: + le message original
                response = f"OK:{message}"
                await websocket.send(response)
                
    except ConnectionClosed:
        # Gérer la déconnexion du client
        print("Client déconnecté")
        return

async def main():
    """
    Démarre le serveur WebSocket sur localhost:8765.
    """
    async with websockets.serve(handle_client, "localhost", 8765):
        print("Serveur WebSocket démarré sur ws://localhost:8765")
        print("En attente de connexions...")
        # Attendre indéfiniment
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServeur arrêté")
