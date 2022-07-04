# Standard library imports
# --NONE--

# Third party imports
import click

# Local application imports
from cmdnix import ls
from cmdnix import mylog

log = mylog.getLogger("cmdnix")


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Verbose mode", type=bool)
def cli(verbose: bool) -> None:
    mylog.init_console_logging(log, verbose)


@cli.command("ls")
@click.option("-1",
              "--column",
              is_flag=True,
              help="List one file per line",
              type=bool)
@click.argument("paths", nargs=-1, type=str)
def ls_command(column: bool, paths: tuple[str]) -> None:
    log.debug(f"{column=} {paths=}")
    ls.main(column, paths)


if __name__ == '__main__':
    cli()
