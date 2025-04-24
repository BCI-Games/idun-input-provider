from enum import Enum


class CommandLineArguments:
    api_token: str | None
    address: str | None
    debug: bool


class PredictionType(Enum):
    JAW_CLENCH = 'JAW_CLENCH'
    BIN_HEOG = 'BIN_HEOG',
    QUALITY_SCORE = 'QUALITY_SCORE'
    FFT = 'FFT'

class PredictionMessage:
    idun_id: str
    device_id: str
    type: PredictionType
    result: dict

    def __init__(self, data):
        self.idun_id = data.idunId
        self.device_id = data.deviceId
        self.type = PredictionType[data.predictionType]
        self.result = data.result