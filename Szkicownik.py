import numpy as np

def dlugosciStatku():
            listadlug = [4, 4, 3, 2, 2, 1]
            idx = {'i':0}
            k = 0

            def jakadlugosc():

                if idx.get('i')< listadlug.__len__():
                    dlugosc = listadlug[idx.get('i')]
                    idx['i'] += 1
                    k = 3
                else:
                    dlugosc = 0
                return dlugosc
            return jakadlugosc

k = dlugosciStatku()
m = k()
n = k()
n = k()
n = k()
print m, n

