class ReportEntity:
    def __init__(self, user, title, description, location, photo=None, rating=0, created_at=None, updated_at=None):
        self.user = user
        self.title = title
        self.description = description
        self.location = location
        self.photo = photo
        self.rating = rating
        self.created_at = created_at
        self.updated_at = updated_at