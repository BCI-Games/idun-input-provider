import asyncio
from websockets.server import serve, WebSocketServer, ServerConnection
from websockets.exceptions import ConnectionClosedOK


server: WebSocketServer = None
connections: set[ServerConnection] = set()

async def start_server(host: str, port: int):
    server = await serve(connection_handler, host, port)
    await server.start_serving()

async def close_server():
    if server:
        await server.close()
        server = None


async def broadcast(message: str):
    for server_connection in connections:
        try:
            await server_connection.send(message)
        except ConnectionClosedOK: pass


async def connection_handler(new_connection: ServerConnection):
    connections.add(new_connection)
    print("new connection")
    try:
        while True:
            await new_connection.ping()
            await asyncio.sleep(2)
    except ConnectionClosedOK:
        print("connection closed")
        if new_connection in connections:
            connections.remove(new_connection)