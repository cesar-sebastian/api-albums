class Cover:
    height: int
    width: int
    url: str

    def __init__(self, height, width, url) -> None:
        self.height = height 
        self.width = width
        self.url = url