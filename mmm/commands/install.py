import click
from mmm.core.mod_manager import ModManager
manager = ModManager()

@click.command(name='install')
@click.argument('mod_names', nargs=-1, required=False)  # birden fazla mod adı alır
#@click.argument('version', required=False)  # version opsiyonel
def install(mod_names):
    """Install one or more mods."""
    print(f"Received mod names: {mod_names}")  # Hata ayıklama için argümanları kontrol et
    manager.install_handler(mod_names)
