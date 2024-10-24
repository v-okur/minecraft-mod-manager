import click
from mmm.commands import init
from mmm.commands import install
from mmm.commands import list
from mmm.commands import update

@click.group()
def cli():
    """Minecraft Mod Manager (mmm): Manage your Minecraft mods."""
    pass   

cli.add_command(list)
cli.add_command(init)
cli.add_command(install)
cli.add_command(update)
    
if __name__ == "__main__":
    cli()