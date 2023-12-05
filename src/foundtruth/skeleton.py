import argparse
import logging
import sys

from foundtruth import __version__

__author__ = "Taylor Monacelli"
__copyright__ = "Taylor Monacelli"
__license__ = "MPL-2.0"

# Create a custom logger
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)  # Set the log level to DEBUG


def setup_logger():
    """Set up the logger with a stream handler and formatter."""
    # Set up a stream handler to print log messages to the console
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(
        logging.DEBUG
    )  # Set the log level for this handler to DEBUG

    # Create a formatter with your desired log format
    log_format = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")

    # Attach the formatter to the handler
    stream_handler.setFormatter(formatter)

    # Add the handler to the logger
    _logger.addHandler(stream_handler)


# Call the function to set up the logger at the package level
setup_logger()

# ---- Python API ----


def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    if n == 0:
        return 0

    assert n > 0
    a, b = 1, 1
    for _i in range(n - 1):
        a, b = b, a + b
    return a


# ---- CLI ----


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as a list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version=f"foundtruth {__version__}",
    )
    parser.add_argument(dest="n", help="n-th Fibonacci number", type=int, metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
        default=logging.WARNING,  # Default to WARNING level if not specified
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
        default=logging.WARNING,  # Default to WARNING level if not specified
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    # Clear existing handlers to avoid duplication during test runs
    _logger.handlers.clear()

    # Call the function to set up the logger
    setup_logger()

    _logger.debug("Logger set up with log level: %s", loglevel)


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as a list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    print(f"The {args.n}-th Fibonacci number is {fib(args.n)}")
    _logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as an entry point to create
    console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m foundtruth.skeleton 42
    #
    run()
