# Standard library imports
import logging
import sys


class IsEqualFilter(logging.Filter):

    def __init__(self, level: int, name: str = "") -> None:
        logging.Filter.__init__(self, name)
        self.level = level

    def filter(self, record: logging.LogRecord) -> bool:
        # non-zero return means we log this message
        return record.levelno == self.level


class IsNotEqualFilter(logging.Filter):

    def __init__(self, level: int, name: str = "") -> None:
        logging.Filter.__init__(self, name)
        self.level = level

    def filter(self, record: logging.LogRecord) -> bool:
        # non-zero return means we log this message
        return record.levelno != self.level


def getLogger(name: str = '') -> logging.Logger:
    return logging.getLogger(None if name == '' else name)


def init_console_logging(log: logging.Logger, is_verbose: bool = False) -> None:
    """Initialization of basic logging to console, stdout and stderr, where
    log level INFO goes to stdout and everything else goes to stderr
    See: https://stackoverflow.com/a/31459386, How can INFO and DEBUG logging message be sent to stdout and higher level message to stderr?
    """

    # Prevent exception logging while emitting, see:
    # https://docs.python.org/3/library/logging.html#logging.Handler.handleError
    logging.raiseExceptions = False

    # Alternative option based on strings instead of constants:
    # log.setLevel(logging.getLevelName("DEBUG" if is_debug else "INFO"))
    log.setLevel(logging.DEBUG if is_verbose else logging.INFO)

    handler_out = logging.StreamHandler(sys.stdout)
    handler_out.setFormatter(logging.Formatter("%(message)s"))
    handler_out.addFilter(IsEqualFilter(logging.INFO))
    log.addHandler(handler_out)
    handler_err = logging.StreamHandler(sys.stderr)
    handler_err.setFormatter(logging.Formatter(">>%(filename)s| %(message)s"))
    handler_err.addFilter(IsNotEqualFilter(logging.INFO))
    log.addHandler(handler_err)
