class KgToPounds:
    def __init__(self, kg = 0):
        self.kg = kg

    def to_pounds(self):
        if isinstance(self.kg, (int, float)):
            return self.kg * 2.205
        else:
            return ValueError('Килограммы задаются только числами')



weight = KgToPounds(12)
print(weight.to_pounds())

weight = KgToPounds(41)
print(weight.to_pounds())

weight.kg = 'a'
print(weight.to_pounds())


