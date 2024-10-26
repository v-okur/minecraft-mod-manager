from typing import List, Optional


class Project:
    
    def __init__(self, project_id: str, project_type: str, slug: str, author: str, title: int,
                 description: str, categories: List[str], display_categories: List[str], 
                 versions: List[str], downloads: int, follows: int, icon_url: str, 
                 date_created: str, date_modified: str, latest_version: str, license: str,
                 client_side: str, server_side: str, color: int, featured_gallery: Optional[str], gallery: Optional[List[str]] = None): 
        self.project_id = project_id
        self.project_type = project_type
        self.slug = slug
        self.author = author
        self.title = title
        self.description = description
        self.categories = categories
        self.display_categories = display_categories
        self.versions = versions
        self.downloads = downloads
        self.follows = follows
        self.icon_url = icon_url
        self.date_created = date_created
        self.date_modified = date_modified
        self.latest_version = latest_version
        self.license = license
        self.client_side = client_side
        self.server_side = server_side
        self.color = color
        self.featured_gallery = featured_gallery
        self.gallery = gallery or []
      
class Main:
    def __init__(self, hits: List[Project], offset: int, limit: int, total_hits: int):
        self.hits = hits
        self.offset = offset
        self.limit = limit
        self.total_hits = total_hits    

    @classmethod
    def from_dict(cls, data):
        projects = [Project(**project) for project in data['hits']]
        
        return cls(
            hits=projects,
            offset=data['offset'],
            limit=data['limit'],
            total_hits=data['total_hits']
        )
