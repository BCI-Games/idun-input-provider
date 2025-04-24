import asyncio
from idun_guardian_sdk import GuardianClient
from arguments import get_command_line_arguments
from classes import JawClenchPredictionMessage


def output_jaw_clench_prediction(data):
    prediction = JawClenchPredictionMessage(data)
    print('Prediction received: ' + prediction.result)


args = get_command_line_arguments()
client = GuardianClient(
    api_token=args.api_token,
    address=args.address,
    debug=args.address
)

client.subscribe_realtime_predictions(jaw_clench=True, handler=output_jaw_clench_prediction)
asyncio.run(client.start_recording())