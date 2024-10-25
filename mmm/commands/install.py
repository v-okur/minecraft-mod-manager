import click
from mmm.core.mod_manager import ModManager
manager = ModManager()

@click.command(name='install')
@click.argument('mod_names', nargs=-1, required=False)
@click.option('--confirmall', '-y', is_flag=True, help='Confirm all installations.')
def install(mod_names, confirmall):
    """Install one or more mods."""
    
    manager.install_handler(mod_names)
