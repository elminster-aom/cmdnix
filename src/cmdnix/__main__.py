# Standard library imports
# --NONE--

# Third party imports
import click

# Local application imports
from cmdnix.main_commands import ls_command


@click.option("-v",
              "--verbose",
              is_flag=True,
              default=False,
              help="Verbose mode",
              type=bool)
@click.group()
@click.pass_context
def main(ctx: click.Context, verbose: bool) -> None:
    ctx.obj = {
        "verbose": verbose,
    }


@main.command()
@click.pass_obj
def ls(ctx_object: dict[str, any]) -> None:
    print("main_ls", ctx_object)
    ls_command(ctx_object)


if __name__ == '__main__':
    main()
