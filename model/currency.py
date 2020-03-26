from sys import maxsize


class Currency:

    def __init__(self, id=None, numCode=None, charCode=None, nominal=None, name=None, value=None):
        self.id = id
        self.numCode = numCode
        self.charCode = charCode
        self.nominal = nominal
        self.name = name
        self.value =value

    def __repr__(self):
        return "\'%s, %s, %s, %s, %s\'" % (self.numCode, self.charCode, self.nominal, self.name, self.value)

    def __eq__(self, other):
        return self.numCode == other.numCode

    def id_or_max(self):
        if self.numCode:
            return int(self.numCode)
        else:
            return maxsize
