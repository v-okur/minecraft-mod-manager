import json
from mmm.config import Defaults
import mmm.exceptions.general as ex


def loader_val(loader):
    if loader in Defaults.SUPPORTED_LOADERS:
        return True
    return False