
class Defaults:
    _instance = None

    DEFAULT_MODPACK_NAME = 'minecraft_modpack'
    DEFAULT_VERSION = '1.20.1'
    SUPPORTED_VERSIONS = [
        '0.16', '1.0', '1.0.0', '1.1', '1.2', '1.2.1', '1.2.2', '1.2.3', 
        '1.2.4', '1.2.5', '1.2.8', '1.3.1', '1.3.2', '1.4.2', '1.4.4', 
        '1.4.5', '1.4.6', '1.4.7', '1.5.0', '1.5.1', '1.5.2', '1.5.3', 
        '1.6', '1.6.1', '1.6.2', '1.6.4', '1.7', '1.7.1', '1.7.2', '1.7.3', 
        '1.7.4', '1.7.5', '1.7.6', '1.7.7', '1.7.8', '1.7.9', '1.7.10', '1.8', 
        '1.8.1', '1.8.2', '1.8.3', '1.8.4', '1.8.5', '1.8.6', '1.8.7', '1.8.8', 
        '1.8.9', '1.9', '1.9.1', '1.9.2', '1.9.3', '1.9.4', '1.10', '1.10.1', 
        '1.10.2', '1.11', '1.11.1', '1.11.2', '1.12', '1.12.1', '1.12.2', 
        '1.14', '1.14.1', '1.14.2', '1.14.3', '1.14.4', '1.15', '1.15.1', 
        '1.15.2', '1.16', '1.16.1', '1.16.2', '1.16.3', '1.16.4', '1.16.5', 
        '1.17', '1.17.1', '1.18', '1.18.1', '1.18.2', '1.19', '1.19.1', 
        '1.19.2', '1.19.3', '1.19.4', '1.20', '1.20.1', '1.20.2', '1.20.3', 
        '1.20.4', '1.20.5', '1.20.6', '1.21', '1.21.1'
    ]
    SUPPORTED_LOADERS = ['forge', 'fabric', 'neoforge', 'quilt']
    LATEST_VERSION = SUPPORTED_VERSIONS[-1]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Defaults, cls).__new__(cls)
            cls._instance.version = cls.DEFAULT_VERSION
            cls._instance.loader = None  
        return cls._instance

    def set_config(self, version, loader):
        """Version ve loader ayarlarını günceller."""
        if version in self.SUPPORTED_VERSIONS:
            self.version = version
        else:
            self.version = self.DEFAULT_VERSION

        if loader in self.SUPPORTED_LOADERS:
            self.loader = loader
        else:
            self.loader = None

    def get_version(self):
        """Geçerli versiyonu döndürür."""
        return self.version

    def get_loader(self):
        """Geçerli loader'ı döndürür."""
        return self.loader
