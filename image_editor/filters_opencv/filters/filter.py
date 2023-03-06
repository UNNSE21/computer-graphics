class Filter:

    def __init__(self, name: str, arguments: dict, help_text: str, func):
        self.name = name
        self.arguments = arguments
        self.help = help_text
        self.func = func
