from asyncio import run, gather, sleep
from idun_guardian_sdk import GuardianClient
from process_management import start_parent_process_dependency_loop
from arguments import get_command_line_arguments
from classes import JawClenchPredictionMessage
from server import BroadcastServer, start_broadcast_server


server: BroadcastServer

def output_jaw_clench_prediction(data):
    prediction = JawClenchPredictionMessage(data)
    print('Prediction received: ' + prediction.result, flush=True)
    server.send(prediction.result)


args = get_command_line_arguments()
client = GuardianClient(
    api_token=args.api_token,
    address=args.address,
    debug=args.address
)
client.subscribe_realtime_predictions(jaw_clench=True, handler=output_jaw_clench_prediction)


async def main():
    server = await start_broadcast_server(args.websocket_host, args.websocket_port)
    await gather(
        start_parent_process_dependency_loop(),
        start_ping_loop(server)
    )
    # await client.start_recording()
        
async def start_ping_loop(server: BroadcastServer):
    while True:
        await server.send("ping")
        await sleep(1)

try:
    run(main())
except KeyboardInterrupt: pass
except InterruptedError: pass

print("exiting...")