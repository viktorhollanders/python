# Write the class "MusicAlbum" here


class MusicAlbum:
    def __init__(self, band="unknown band", title="unknown", year="unknown year"):
        self.set_album(band, title, year)

    def set_album(self, band="unknown band", title="unknown", year="unknown year"):
        self.band = band
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f"Album {self.title} by {self.band}, released in {self.year}."
