import json
from ..config import Defaults
from ..exceptions import general as ex


def loader_val(loader):
    if loader in Defaults.SUPPORTED_LOADERS:
        return True
    return False