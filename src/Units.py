from dataclasses import dataclass

@dataclass(init=False)
class UnitBase:
    val:float
    unitExt:str
    preferedConversion = None

    def __str__(self) -> str:
        return f"{str(round(self.val, 1))} {self.unitExt}"

    def __init__(self, value:float = 0.0):
        self.val = value
    
@dataclass(init=False)
class Meters(UnitBase):
    def ToKilometers(self) -> 'Meters':
        return Meters(self.val * 1000)
    def ToCentimeters(self) -> 'Centimeters':
        return Centimeters(self.val * 100000)
    def ToInches(self) -> 'Inches':
        return Inches(self.val * 39370)
    def ToFeet(self) -> 'Feet':
        return Feet(self.val * 3281)
    def ToMiles(self) -> 'Miles':
        return Miles(self.val / 1.609)
   
    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToFeet
        self.unitExt = "m"

@dataclass(init=False)
class Centimeters (UnitBase):
    def ToMeters(self) -> 'Meters':
        return Meters(self.val / 100)
    def ToKilometers(self) -> 'Centimeters':
        return Centimeters(self.val / 100000)
    def ToInches(self) -> 'Inches':
        return Inches(self.val / 2.54)
    def ToFeet(self) -> 'Feet':
        return Feet(self.val / 30.48)
    def ToMiles(self) -> 'Miles':
        return Miles(self.val / 160900)

    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToInches
        self.unitExt = "cm"

@dataclass
class Kilometers(UnitBase):
    def ToMeters(self) -> 'Meters':
        return Meters(self.val * 1000)
    def ToCentimeters(self) -> 'Centimeters':
        return Centimeters(self.val * 100000)
    def ToInches(self) -> 'Inches':
        return Inches(self.val * 39370)
    def ToFeet(self) -> 'Feet':
        return Feet(self.val * 3281)
    def ToMiles(self) -> 'Miles':
        return Miles(self.val / 1.609)

    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToMiles
        self.unitExt = "km"

@dataclass
class Celcius(UnitBase):
    def ToFahrenheit(self) -> 'Fahrenheit':
        return Fahrenheit(self.val * (9/5) + 32)
    
    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToFahrenheit
        self.unitExt = "°c"
    
@dataclass
class Inches(UnitBase):
    def ToMeters(self) -> 'Meters':
        return Meters(self.val / 39.37)
    def ToCentimeters(self) -> 'Centimeters':
        return Centimeters(self.val * 2.54)
    def ToKilometers(self) -> 'Inches':
        return Kilometers(self.val / 39370)
    def ToFeet(self) -> 'Feet':
        return Feet(self.val / 12)
    def ToMiles(self) -> 'Miles':
        return Miles(self.val / 63360)

    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToCentimeters
        self.unitExt = "in"

@dataclass
class Feet(UnitBase):
    def ToMeters(self) -> 'Meters':
        return Meters(self.val * 3.281)
    def ToCentimeters(self) -> 'Centimeters':
        return Centimeters(self.val * 30.48)
    def ToKilometers(self) -> 'Feet':
        return Kilometers(self.val * 3281)
    def ToInches(self) -> 'Inches':
        return Inches(self.val * 12)
    def ToMiles(self) -> 'Miles':
        return Miles(self.val / 5280)

    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToMeters
        self.unitExt = "ft"

@dataclass
class Miles(UnitBase):
    def ToMeters(self) -> 'Meters':
        return Meters(self.val * 1609)
    def ToCentimeters(self) -> 'Centimeters':
        return Centimeters(self.val * 160900)
    def ToKilometers(self) -> 'Miles':
        return Kilometers(self.val * 1.609)
    def ToInches(self) -> 'Inches':
        return Inches(self.val * 63360)
    def ToFeet(self) -> 'Feet':
        return Feet(self.val * 5280)

    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToKilometers
        self.unitExt = "mi"

@dataclass
class Fahrenheit(UnitBase):
    def ToCelcius(self) -> Celcius:
        return Celcius((self.val - 32) * (5/9))
        

    def __init__(self, value: float):
        super().__init__(value)
        self.preferedConversion = self.ToCelcius
        self.unitExt = "°f"


def detectUnit(txt:list):
    num = float(txt[0])
    unit = str(txt[1])
    print(txt)
    if (unit.startswith("°") and not (unit.endswith("c"))) or unit.startswith("deg") or (unit.startswith("f") and not unit.endswith("feet")):
        return Fahrenheit(num)
    if unit.endswith("c") and not (unit.startswith("cm") or unit.startswith("centi")):
        return Celcius(num)
    if unit.startswith("ft") or unit.startswith("feet"):
        return Feet(num)
    if unit.startswith("in"):
        return Inches(num)
    if unit.startswith("cm") or unit.startswith("cen"):
        return Centimeters(num)
    if unit.startswith("km") or unit.startswith("kil"):
        return Kilometers(num)
    if unit.startswith("m") or unit.startswith("met"):
        return Meters(num)