from ..config import Defaults

def version_val(version):
    if version in Defaults.SUPPORTED_VERSIONS:
        return True
    return False
