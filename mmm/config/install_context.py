from mmm.config import Defaults

config = Defaults()

class InstallContext:
    def __init__(self, mod_name, version=None, loader=None, author=None, min_downloads=None, limit=None, mode=None):
        self.mod_name = mod_name
        self.version = version or config.get_version()
        self.loader = loader or config.get_loader()
        self.author = author
        self.min_downloads = min_downloads
        self.limit = limit
        self.mode = mode
        self.mod_data = None
        self.project_id = None
    def _default_version(self):
        return  config.get_version()

    def _default_loader(self):
        return config.get_loader()
    
    def set_version_and_loader(self, version, loader):
        self.version = version
        self.loader = loader
    
    def set_mode(self, mode):
        self.mode = mode
    
    def set_mod_data(self, data):
        self.mod_data = data
        
    def set_project_id(self, project_id):
        self.project_id = project_id
        
    def to_facets(self):
        fields = {
            "versions": self.version,
            "categories": self.loader,
            "authors": self.author,
            "downloads>=": self.min_downloads
        }
        return [f'["{key}:{value}"]' for key, value in fields.items() if value is not None]