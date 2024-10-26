import click
from ..core.mod_manager import ModManager
manager = ModManager()

@click.command(name='list')
@click.option('--installed', '-i', is_flag=True, help='List only installed mods.')
def list(installed):
    """List available mods for your Minecraft version."""
    manager.list_mods(installed)