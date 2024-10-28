import click
from ..core.mod_manager import ModManager
manager = ModManager()




"""
project_type
categories (loaders are lumped in with categories in search)
versions
"""
@click.command(name='search')
@click.argument('mod_name', required=False)
@click.option('--mc_version', '-v', help='Select Minecraft version.')
@click.option('--loader', '-l', help='Select loader.')
@click.option('--type', '-t', help='Select project type.')
@click.option('--min', '-m', help='Minimum download count.')
@click.option('--max', '-M', help='Maximum download count.')
@click.option('--sort', '-s', help='Select sorting type.')

def search(mod_name, mc_version, loader, type, min, max, sort):
    """Search mods with different options."""
    manager.search_mods(mod_name, mc_version, loader, type, min, max, sort)