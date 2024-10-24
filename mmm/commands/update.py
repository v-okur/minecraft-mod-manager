import click

@click.command(name='update')
@click.argument('mod_name', required=False)
def update(mod_name):
    """Update mods to spesific version"""
    if mod_name:
        print(f'updating {mod_name}')
    else:
        print('updating all')