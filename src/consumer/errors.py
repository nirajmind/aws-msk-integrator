from src.common.exceptions import MSKBaseException

class ConsumerInitializationError(MSKBaseException):
    """Raised when consumer fails to initialize."""
    pass


class ConsumerProcessingError(MSKBaseException):
    """Raised when consumer fails to process a message."""
    pass
