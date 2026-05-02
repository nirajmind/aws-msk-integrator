class MSKBaseException(Exception):
    """Base class for all MSK-related exceptions."""
    pass


class ConfigLoadError(MSKBaseException):
    """Raised when configuration cannot be loaded."""
    pass


class ConnectivityError(MSKBaseException):
    """Raised when MSK connectivity fails."""
    pass


class AuthenticationError(MSKBaseException):
    """Raised when IAM authentication fails."""
    pass


class SerializationError(MSKBaseException):
    """Raised when message serialization fails."""
    pass
