import click
from .commands import init, install, list, update, search

@click.group()
def cli():
    """Minecraft Mod Manager (mmm): Manage your Minecraft mods."""
    pass   

cli.add_command(list)
cli.add_command(init)
cli.add_command(install)
cli.add_command(update)
cli.add_command(search)
    
    
    
if __name__ == "__main__":
    cli()
    