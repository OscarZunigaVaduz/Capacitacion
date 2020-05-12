from example import Resta

class Test:
     def __init__(self, debug=True):
        if debug is True:
            self.import_resta()
        else:
            print(self.get_resta())


     def import_resta(self):
        i = Resta(2)
        i.print_resta(dos = 2,uno= 1)

     def get_resta(self):
        i = Resta(2)
        return i.get_resta(dos = 2,uno= 1)


t = Test(debug=False)
