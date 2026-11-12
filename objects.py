class csv_file:
    """ A class representing an CSV file """
    def __init__ (self, filename, limiter):
        self.filename = filename
        self.limiter = limiter
    
    def __str__(self):
        return f"{self.filename}"



###################################################
### This: Might be 

class column: # column(title, x)
    """ A class representing a column """
    def __init__(self, title, x):
        self.title = title
        self.x = x

    def __str__(self):
        return f"{self.x} column named {self.title} in"



class row: # row(y)
    """ A class representing one row """
    def __init__(self, y):
        self.y = y

    def __str__(self):
        return f"{self.y} in {self.filename}"



class cell:
    """ A class representing a cell in CSV file"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

### Unnessessary ....
#########################################################
