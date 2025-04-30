from idun_guardian_sdk import GuardianClient
from server import BroadcastServer
from prediction_messages import JawClenchPredictionMessage


class JawClenchBroadcastProxy:
    broadcast_server: BroadcastServer

    def __init__(self, server):
        self.broadcast_server = server

    def output_jew_clench_prediction(self, data):
        prediction = JawClenchPredictionMessage(data)
        print('Prediction received: ' + prediction.result, flush=True)
        self.broadcast_server.send(prediction.result)


def create_jaw_clench_client(
    response_server: BroadcastServer,
    api_token: str, address: str,
    debug: bool = False
) -> GuardianClient:
    broadcast_proxy = JawClenchBroadcastProxy(response_server)

    client = GuardianClient(
        api_token=api_token,
        address=address,
        debug=debug
    )
    client.subscribe_realtime_predictions(
        jaw_clench=True,
        handler=broadcast_proxy.output_jew_clench_prediction
    )
    return client