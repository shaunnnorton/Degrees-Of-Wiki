from src import db

# PageModel
#  URL
#  Links
#  Times Queried

# Matches
#  URL 1
#  URL 2
#  Degrees
#  Last Queried


class Page(db.Model):
    """Page Model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # The url of the Page
    links = db.Column(db.Text, nullable=True)  # String of Links on the Page
    queried = db.Column(db.Integer, nullable=False)  # Number of Times Queried
    # matches = db.relationship("Matches")

    def __str__(self):
        return f"<Page: {self.name} Queried: {self.queried}> "

    def __repr__(self):
        return f"<Page: {self.name} Queried: {self.queried}> "


class Matches(db.Model):
    """Matches Model"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    url1_id = db.Column(db.Integer, db.ForeignKey("page.id"))
    # The url of the first Page
    url2_id = db.Column(db.Integer, db.ForeignKey("page.id"))
    # The url of the second Page
    degrees = db.Column(db.Integer, nullable=False)
    # The degrees of seperation between the two pages
    last = db.Column(db.DateTime, nullable=False)
    # The last time this match was Queried
    url1 = db.relationship("Page", foreign_keys=[url1_id])
    url2 = db.relationship("Page", foreign_keys=[url2_id])

    def __str__(self):
        return (
            f"<Match: URL1:{self.url1} URL2:{self.url2}" +
            f"Degrees: {self.degrees}> "
        )

    def __repr__(self):
        return (
            f"<Match: URL1:{self.url1} URL2:{self.url2}" +
            f"Degrees: {self.degrees}> "
        )
