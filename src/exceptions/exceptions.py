class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidFilePath(Error):
    """Raised when input file path is valid"""
    pass

class CommandLineArgumentNotAvailable(Error):
    """Raised when input file path is not provided as first commandline argument"""
    pass

