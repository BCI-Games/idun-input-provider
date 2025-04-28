import asyncio
from idun_guardian_sdk import GuardianClient
from arguments import get_command_line_arguments
from classes import JawClenchPredictionMessage
from websocket import start_server, broadcast



def output_jaw_clench_prediction(data):
    prediction = JawClenchPredictionMessage(data)
    print('Prediction received: ' + prediction.result)
    broadcast(prediction.result)


args = get_command_line_arguments()
client = GuardianClient(
    api_token=args.api_token,
    address=args.address,
    debug=args.address
)
client.subscribe_realtime_predictions(jaw_clench=True, handler=output_jaw_clench_prediction)


async def main():
    print("starting server...")
    await start_server(args.websocket_host, args.websocket_port)
    while True:
        # print("broadcasting ping")
        await broadcast("ping")
        await asyncio.sleep(1)
    # await client.start_recording()
    

try:
    asyncio.run(main())
except KeyboardInterrupt: pass