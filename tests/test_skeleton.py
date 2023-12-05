import pytest

from foundtruth.skeleton import fib, main

__author__ = "Taylor Monacelli"
__copyright__ = "Taylor Monacelli"
__license__ = "MPL-2.0"


def test_fib():
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["7"])
    captured = capsys.readouterr()
    assert "The 7-th Fibonacci number is 13" in captured.out


def test_main_with_invalid_argument(capsys):
    """Test CLI with an invalid argument"""
    with pytest.raises(SystemExit):
        main(["invalid_argument"])
    captured = capsys.readouterr()
    assert "error: unrecognized arguments" in captured.err.lower()


def test_main_with_verbose_flag(capsys):
    """Test CLI with verbose flag"""
    main(["--verbose", "5"])
    captured = capsys.readouterr()
    assert "Starting crazy calculations..." in captured.out


def test_main_with_missing_argument(capsys):
    """Test CLI with missing argument"""
    with pytest.raises(SystemExit):
        main([])
    captured = capsys.readouterr()
    assert "the following arguments are required: n" in captured.err.lower()


def test_main_with_zero_argument(capsys):
    """Test CLI with zero as an argument"""
    main(["0"])
    captured = capsys.readouterr()
    assert "The 0-th Fibonacci number is 0" in captured.out


def test_main_with_large_argument(capsys):
    """Test CLI with a large argument"""
    main(["10"])
    captured = capsys.readouterr()
    assert "The 10-th Fibonacci number is 55" in captured.out
