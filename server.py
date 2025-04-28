from asyncio import StreamReader, StreamWriter, start_server, sleep


class BroadcastServer():
    connections: set[StreamWriter] = set()

    async def handle_client_connection(self, _: StreamReader, writer: StreamWriter):
        print("new connection")
        self.connections.add(writer)

        while not writer.is_closing():
            await sleep(1.0)
        
        print("connection lost")
        self.connections.remove(writer)

    async def send(self, message: str):
        out_stream: StreamWriter
        for out_stream in self.connections:
            try:
                out_stream.write(message.encode())
                await out_stream.drain()
            except: pass


async def start_broadcast_server(host: str = None, port: int = None) -> BroadcastServer:
    broadcast_shell = BroadcastServer()
    await start_server(broadcast_shell.handle_client_connection, host, port)
    return broadcast_shell