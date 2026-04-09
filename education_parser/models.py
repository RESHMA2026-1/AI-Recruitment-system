class Education:
    def __init__(self, degree, field, institution, year):
        self.degree = degree
        self.field = field
        self.institution = institution
        self.year = year

class Certification:
    def __init__(self, name, category=None):
        self.name = name
        self.category = category