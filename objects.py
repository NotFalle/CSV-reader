class csv_file:
    """ A class representing an CSV file """
    def __init__ (self, filename, limiter):
        self.filename = filename
        self.limiter = limiter
    
    def __str__(self):
        return f"{self.filename}"



class column(csv_file): # column(title, x)
    """ A class representing a column """
    def __init__(self, title, x):
        self.title = title
        self.x = x

    def __str__(self):
        return f"{self.column_number} column named {self.title} in {self.filename}"


class row(csv_file): # row(y)
    """ A class representing one row """
    def __init__(self, y):
        self.y = y

    def __str__(self):
        return f"{self.row_number} in {self.filename}"



class cell(column, row):
    """ A class representing a cell in CSV file"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Parent():
    def __init__(self):
        self.myvar = 1

class Child(Parent):
    def __init__(self):
        self.parent = Parent

        # here you can access myvar like below.
        print(self.myvar)

child = Child()
print(child.myvar)


# Helluu