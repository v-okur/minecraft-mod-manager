from typing import List, Optional


class File:
    def __init__(self, sha1: str, sha512: str, url: str, filename: str, size: int):
        self.sha1 = sha1
        self.sha512 = sha512
        self.url = url
        self.filename = filename
        self.size = size
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            sha1=data['hashes']['sha1'],
            sha512=data['hashes']['sha512'],
            url=data['url'],
            filename=data['filename'],
            size=data['size']
        )
        
    def to_dict(self):
        return {
            "hashes": {
                "sha1": self.sha1,
                "sha512": self.sha512,
            },
            "url": self.url,
            "filename": self.filename,
            "size": self.size,
        }
        
        
class Dependency:
    def __init__(self, version_id: str, project_id: str, file_name:str, dependency_type: str):
        self.version_id = version_id
        self.project_id = project_id
        self.file_name = file_name
        self.dependency_type = dependency_type

    @classmethod
    def from_dict(cls, data):
      return cls(
            version_id=data['version_id'],
            project_id=data['project_id'],
            file_name=data['file_name'],
            dependency_type=data['dependency_type']
        )
    
    def to_dict(self):
        return {
            "version_id": self.version_id,
            "project_id": self.project_id,
            "file_name": self.file_name,
            "dependency_type": self.dependency_type,
        }  
      
    
class Main:
    def __init__(self, game_versions: List[str], loaders: List[str], id: str, project_id: str,
                 author_id: str, name: str, version_number: str, date_published: str,
                 downloads: int, version_type: str, files: List[File], dependencies: List[Dependency]):
        self.game_versions = game_versions
        self.loaders = loaders
        self.id = id
        self.project_id = project_id
        self.author_id = author_id
        self.name = name
        self.version_number = version_number
        self.date_published = date_published
        self.downloads = downloads
        self.version_type = version_type
        self.files = files
        self.dependencies = dependencies or []

    @classmethod
    def from_dict(cls, data):
        files = [File.from_dict(file) for file in data.get('files', [])]
        dependencies = [Dependency.from_dict(dep) for dep in data.get('dependencies', [])]
        

        """ dependencies = [
            Dependency.from_dict(dep) for dep in data.get('dependencies', [])
        ] """
        
        return cls(
            game_versions=data.get('game_versions', []),
            loaders=data.get('loaders', []),
            id=data.get('id', ''),
            project_id=data.get('project_id', ''),
            author_id=data.get('author_id', ''),
            name=data.get('name', ''),
            version_number=data.get('version_number', ''),
            date_published=data.get('date_published', ''),
            downloads=data.get('downloads', 0),
            version_type=data.get('version_type', ''),
            files=files,
            dependencies=dependencies
        )
        
    def to_dict(self):
        return {
            "game_versions": self.game_versions,
            "loaders": self.loaders,
            "id": self.id,
            "project_id": self.project_id,
            "author_id": self.author_id,
            "name": self.name,
            "version_number": self.version_number,
            "date_published": self.date_published,
            "downloads": self.downloads,
            "version_type": self.version_type,
            "files": [file.to_dict() for file in self.files],
            "dependencies": [dep.to_dict() for dep in self.dependencies],
        }
