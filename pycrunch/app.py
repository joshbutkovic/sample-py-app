from .cli import cli


def run():
    pycrunch_cli = cli.Cli()
    pycrunch_cli.start()
