error_hierarchy = {
  "BaseError": {
    "ExchangeError": {
      "AuthenticationError": {
        "PermissionDenied": {},
        "AccountSuspended": {}
      },
      "ArgumentsRequired": {},
      "BadRequest": {},
      "BadResponse": {
        "NullResponse": {}
      },
      "InsufficientFunds": {},
      "InvalidAddress": {
        "AddressPending": {}
      },
      "InvalidOrder": {
        "OrderNotFound": {},
        "OrderNotCached": {},
        "CancelPending": {},
        "OrderImmediatelyFillable": {},
        "OrderNotFillable": {},
        "DuplicateOrderId": {}
      },
      "NotSupported": {}
    },
    "NetworkError": {
      "DDoSProtection": {},
      "ExchangeNotAvailable": {},
      "InvalidNonce": {},
      "RequestTimeout": {}
    }
  }
}

# -----------------------------------------------------------------------------

__all__ = []


def error_factory(dictionary, super_class):
    for key in dictionary:
        __all__.append(key)
        error_class = type(key, (super_class,), {})
        globals()[key] = error_class
        error_factory(dictionary[key], error_class)


class BaseError(BaseException):
    def __init__(self):
        pass


error_factory(error_hierarchy['BaseError'], BaseError)
