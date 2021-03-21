class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()

        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        vals = intSet()

        for e in self.vals:
            if e in other.vals:
                vals.insert(e)
        return str(vals)

    def __len__(self):
        count = 0
        for e in self.vals:
            count += 1

        return count


s1 = intSet()
s1.insert(1)
s1.insert(3)
s2 = intSet()
s2.insert(1)
s2.insert(2)

print(len(s1))