from src.common.exceptions import MSKBaseException

class ProducerInitializationError(MSKBaseException):
    """Raised when producer fails to initialize."""
    pass


class ProducerSendError(MSKBaseException):
    """Raised when producer fails to send a message."""
    pass
