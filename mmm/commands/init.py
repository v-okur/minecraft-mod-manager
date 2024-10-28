import click
from ..core.mod_manager import ModManager

manager = ModManager()

@click.command(name='init')
@click.option('--version', '-v', help='Minecraft version to use.')
@click.option('--loader', '-l', help='Mod loader to use.')
@click.option('--force', '-f', is_flag=True, help='Force reinitialization.')
@click.option('--default', '-d', is_flag=True, help='Use default values.')
def init(default, force, loader, version):
    """Initialize a new modpack."""
    print(default)
    manager.init_handler(default, force, loader, version)
    
    
