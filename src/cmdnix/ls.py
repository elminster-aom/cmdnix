# Standard library imports
import os
from typing import Generator

# Local application imports
from cmdnix import mylog

log = mylog.getLogger(__name__)


def list_entries(path: str) -> Generator[os.DirEntry, None, None]:
    with os.scandir(path) as entries:
        for entry in entries:
            yield entry


def main(column: bool, paths: tuple[str]) -> None:
    separator = '\n' if column else '\t'
    if not paths:
        paths = (".",)
    for path in paths:
        file_names = (entry.name
                      for entry in list_entries(path)
                      if not entry.name.startswith('.'))
        log.info(separator.join(sorted(file_names)))
