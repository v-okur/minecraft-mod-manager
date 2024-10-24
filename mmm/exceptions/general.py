class CLIError(Exception):
    """Exception class for general CLI errors."""

    def __init__(self, message='An unexpected error occurred.'):
        self.message = message
        super().__init__(self.message)

class ModsJsonNotFound(Exception):
    """Raised when the mods.json file is not found."""

    def __init__(self, message='mods.json not found. Please run `mmm init` to create a new mods.json file or fix the existing one.'):
        self.message = message
        super().__init__(self.message)

class ModsJsonCorrupted(Exception):
    """Raised when the mods.json file is corrupted."""

    def __init__(self, additional_message=''):
        message = 'mods.json is corrupted. Please run `mmm init` to create a new mods.json file or fix the existing one.'
        self.message = additional_message + '\n' + message
        super().__init__(self.message)

class InvalidLoader(Exception):
    """Raised when an invalid loader is specified."""

    def __init__(self, message='Invalid loader. Please specify a valid loader.'):
        self.message = message
        super().__init__(self.message)