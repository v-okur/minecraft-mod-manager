from ..config import Defaults
from ..models import Search, Project
config = Defaults()

class InstallContext:
    def __init__(self, mod_name, index:int = 0, offset:int = 0, confirm_all:bool = False, limit=100, mode=None):
        self.version = config.get_version()
        self.loader = config.get_loader()
        
        self.mod_name = mod_name
        self.confirm_all = confirm_all
        self.mode = mode
        self.limit = limit
        self.offset = offset
        self.index = index
        
        self.project_id = None
        self.search_data: Search.Main = None
        self.project_data: Project.Main = None
        self.game_versions = []  # Versiyonları burada saklayacağız
    
    def set_version_and_loader(self, version, loader):
        self.version = version
        self.loader = loader
    
    def set_search_data(self, data):
        self.search_data = data
        
    def set_project_data(self, data):
        self.project_data = data
        self.game_versions = self.project_data.game_versions  # game_versions ekleniyor
    
    def set_mode(self, mode):
        self.mode = mode
        
    def set_project_id(self, project_id):
        self.project_id = project_id
        
    def to_facets(self):        
        fields = {
            "project_id": self.project_id,
            "versions": self.version,
            "categories": self.loader
        }
        
        # Game version'ları facets'e ekleme
        facets = [[f'{key}={value}'] for key, value in fields.items() if value is not None]
        if self.game_versions:
            version_facets = [f'versions={v}' for v in self.game_versions]
            facets.append(version_facets)
        
        return facets
