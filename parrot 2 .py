class parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} sings {}".format (self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)

pinku=parrot("pinku",17)

print(pinku.sing("~Happy~"))
print (pinku.dance())