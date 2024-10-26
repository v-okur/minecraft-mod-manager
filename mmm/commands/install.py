import click
from ..core.mod_manager import ModManager
manager = ModManager()

@click.command(name='install')
@click.argument('mod_names', nargs=-1, required=False)
@click.option('--confirmall', '-y', is_flag=True, help='Confirm all installations.')
@click.option('--limit', '-l', help='Limit the number of mods to install.')

def install(mod_names, confirmall, limit):
    """Install one or more mods."""
    manager.install_handler(mod_names, confirmall, limit)
