class CLIError(Exception):
    """Exception class for general CLI errors."""

    def __init__(self, message='An unexpected error occurred.'):
        self.message = message
        super().__init__(self.message)

def ModsJsonNotFound(message='mods.json not found. Please run `mmm init` to create a new mods.json file.'):
    """Raised when the mods.json file is not found."""
    print(message)
    
def VersionKeyNotFound(message='mods.json is corrupted. Please run `mmm init` to create a new mods.json file or fix the existing one.'):
    """Raised when the mods.json file is not found."""
    print(message)

def ModsJsonCorrupted(additional_message=''):
    """Raised when the mods.json file is corrupted."""
    message = 'mods.json is corrupted. Please run `mmm init` to create a new mods.json file or fix the existing one.'
    message = additional_message + '\n' + message
    print(message)

def InvalidLoader( message='Invalid loader. Please specify a valid loader.'):
    """Raised when an invalid loader is specified."""
    print(message)
    