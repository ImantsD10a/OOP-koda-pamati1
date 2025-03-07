class Gramata:
    def __init__(self,nosaukums,lapas):
        self.nosaukums = nosaukums
        self.Lapas = lapas
    def print_info(self):
        print("aa " + self.nosaukums)
        print("lpp " + str(self.Lapas))

        




g1 = Gramata("hjhj", 23)
print(g1.nosaukums)
print(g1.Lapas)

g1.print_info()