# Standard library imports
import subprocess

# Third party imports
import pytest

# Local application imports
from cmdnix.main_commands import ls_command


def _run_command(*args: str) -> tuple[str, str]:
    cmd_result = subprocess.run(*args, capture_output=True)

    return (cmd_result.stdout.decode(), cmd_result.stderr.decode())


def test_ls(capsys) -> None:
    assert ls_command({"verbose": False}) == None

    # How to write a pytest function for checking console output (stdout/stderr)
    # https://stackoverflow.com/a/20507769
    # https://pytest.org/en/latest/reference/reference.html#capsys
    my_outerr = capsys.readouterr()
    sys_outerr = _run_command(("ls", "-1", "."))
    print(sys_outerr)
    assert my_outerr == sys_outerr
