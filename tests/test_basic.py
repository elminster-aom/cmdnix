# Standard library imports
import subprocess

# Third party imports
import pytest
import click.testing

# Local application imports
from cmdnix.__main__ import cli

cli_runner = click.testing.CliRunner(mix_stderr=False)


def _run_command(*args: str) -> tuple[str, str]:
    cmd_result = subprocess.run(args, capture_output=True)
    return (cmd_result.stdout.decode(), cmd_result.stderr.decode())


def test_ls() -> None:
    sys_result = _run_command("ls", "-1", ".")
    cli_result = cli_runner.invoke(cli, ["ls", "-1", "."])
    assert cli_result.exit_code == 0
    assert sys_result == (cli_result.stdout, cli_result.stderr)
