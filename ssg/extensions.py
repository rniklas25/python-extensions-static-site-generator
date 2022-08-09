import sys, importlib
from pathlib import Path


def load_module(directory, name):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)

load_directory(directory):
    for path in directory.rglob(".py"):
        load_module(directory.as_posix(), path.stem)
