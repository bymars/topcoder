class LengthUnitCalculator:
    def calc(self, amount, fromUnit, toUnit):
        units = ["in", "ft", "yd", "mi"]
        fromIndex = units.index(fromUnit)
        toIndex = units.index(toUnit)
        convert_m = [1760, 3, 12]
        convert = [1/12, 1/3, 1/1760]
        if fromIndex > toIndex:
            fromIndex = 3 - fromIndex
            toIndex = 3 - toIndex
            convert = convert_m
        for i in range(fromIndex, toIndex):
            amount *= convert[i]
        return amount

