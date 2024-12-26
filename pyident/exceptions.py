

class ZibalError(Exception):
    """Base exception for all Zibal-related errors."""
    def __init__(self, message: str, result_code: int):
        self.result_code = result_code
        super().__init__(message)


class InvalidAPIKeyFormatError(ZibalError):
    """Error for result code 2: API Key was not sent in the correct format"""
    pass

class InvalidAPIKeyError(ZibalError):
    """Error for result code 3: The provided API Key is not valid"""
    pass

class UnauthorizedAccessError(ZibalError):
    """Error for result code 4: Authorization for this service has not been granted"""
    pass

class InvalidCallbackURLError(ZibalError):
    """Error for result code 5: The provided callback URL is not valid"""
    pass

class InvalidInputValueError(ZibalError):
    """Error for result code 6: One or more input parameters are invalid"""
    pass

class InvalidIPError(ZibalError):
    """Error for result code 7: The request is coming from an unauthorized IP address"""
    pass

class InactiveAPIKeyError(ZibalError):
    """Error for result code 8: The API Key has been deactivated"""
    pass


class InsufficientBalanceError(ZibalError):
    """Error for result code 29: User's wallet balance is insufficient for this transaction"""
    pass

class DataNotFoundError(ZibalError):
    """Error for result code 44: No records found matching the provided search criteria"""
    pass

class ServiceUnavailableError(ZibalError):
    """Error for result code 45: Third-party service providers are currently unavailable"""
    pass

ERROR_CODES = {
    2: (InvalidAPIKeyFormatError, "API Key format is incorrect or missing"),
    3: (InvalidAPIKeyError, "The provided API Key is not recognized"),
    4: (UnauthorizedAccessError, "Access to this service is not authorized for this API Key"),
    5: (InvalidCallbackURLError, "The callback URL is invalid or malformed"),
    6: (InvalidInputValueError, "One or more input parameters have invalid values"),
    7: (InvalidIPError, "Request originated from an unauthorized IP address"),
    8: (InactiveAPIKeyError, "This API Key has been disabled or is inactive"),
    29: (InsufficientBalanceError, "Insufficient funds in user's wallet for this operation"),
    44: (DataNotFoundError, "No matching records found for the provided search criteria"),
    45: (ServiceUnavailableError, "External service providers are currently unavailable")
}
