class Height:
    def __init__(self, feet=0, inches=0) -> None:
        self.feet = feet
        self.inches = inches

    def cm(self):
        feat_to_cm = self.feet * 30.48
        inches_to_cm = self.inches * 2.54

        cm = feat_to_cm + inches_to_cm
        return f"{round(cm)}"

    def __str__(self) -> str:
        return f"{self.feet} ft, {self.inches} in"
