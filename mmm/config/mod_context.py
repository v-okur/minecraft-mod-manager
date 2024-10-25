class ModContext:
    def __init__(self, mod_names, confirmall, version=None, loader=None):
        self.mod_names = mod_names
        self.confirmall = confirmall
        self.version = version or self._default_version()
        self.loader = loader or self._default_loader()

    def _default_version(self):
        return "1.20.1" 

    def _default_loader(self):
        return "fabric" 
    def set_version_and_loader(self, version, loader):
        self.version = version
        self.loader = loader