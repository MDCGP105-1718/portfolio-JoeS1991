from fractions import gcd

class Fraction(object):

    def __init__(self, nom, denom):
        try:
            self.nom = int(nom)
            self.denom = int(denom)
        except ValueError:
            print("You must use whole numbers for nom and denom.")

    def __add__(self, other):
        nomSum = self.nom + other.nom
        denomSum = gcd(self.denom, other.denom)
        return (f"{nomSum}/{denomSum}")

    def __sub__(self, other):
        nomSum = self.nom - other.nom
        denomSum = gcd(self.denom, other.denom)
        return (f"{nomSum}/{denomSum}")

    def __mul__(self, other):
        mNom = self.nom * other.nom
        mDenom = self.denom * other.denom
        return (f"{mNom}/{mDenom}")


    def divide(self, other):
        dNom = self.nom // other.nom
        dDenom = self.denom // other.denom
        return (f"{dNom}/{dDenom}")

    def inverse(self):
        iNom = self.denom
        iDenom = self.nom
        return str(iNom) + "/" + str(iDenom)

    def __str__(self):
        return str(self.nom) + "/" + str(self.denom)
