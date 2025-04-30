from enum import Enum
from warnings import warn


class CommandLineArguments:
    api_token: str | None
    address: str | None
    debug: bool
    simulate_input: bool
    socket_host: str
    socket_port: int


class PredictionType(Enum):
    JAW_CLENCH = 'JAW_CLENCH'
    BIN_HEOG = 'BIN_HEOG',
    QUALITY_SCORE = 'QUALITY_SCORE'
    FFT = 'FFT'

class JawClenchPredictionValues(Enum):
    CLENCHED = 'JawClench'
    NOTHING = 'Nothing'


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

class JawClenchPredictionMessage(PredictionMessage):
    is_clenched: bool
    max_peak_to_peaks: float

    def __init__(self, data):
        super().__init__(data)
        if self.type != PredictionType.JAW_CLENCH:
            warn('Unexpected prediction type received: ' + self.type)
            return
        self.is_clenched = self.result.prediction == JawClenchPredictionValues.CLENCHED
        self.max_peak_to_peaks = self.result.maxPeakToPeaks