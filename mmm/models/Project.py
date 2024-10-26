from typing import List, Optional


class File:
    def __init__(self, sha1: str, sha512: str, url: str, filename: str, size: int):
        self.sha1 = sha1
        self.sha512 = sha512
        self.url = url
        self.filename = filename
        self.size = size

class Main:
    def __init__(self, game_versions: List[str], loaders: List[str], id: str, project_id: str,
                 author_id: str, name: str, version_number: str, date_published: str,
                 downloads: int, version_type: str, files: List[File], dependencies: Optional[List[str]] = None):
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
        files = [File(file['hashes']['sha1'], file['hashes']['sha512'], file['url'], 
                      file['filename'], file['size']) for file in data['files']]
        return cls(
            game_versions=data['game_versions'],
            loaders=data['loaders'],
            id=data['id'],
            project_id=data['project_id'],
            author_id=data['author_id'],
            name=data['name'],
            version_number=data['version_number'],
            date_published=data['date_published'],
            downloads=data['downloads'],
            version_type=data['version_type'],
            files=files,
            dependencies=data.get('dependencies', [])
        )
