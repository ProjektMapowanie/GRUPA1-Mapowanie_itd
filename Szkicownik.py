import matplotlib.pyplot as plt
dlugoscTablicy = 5
tab = [[0 for col in range(dlugoscTablicy)] for row in range(dlugoscTablicy)]
tab[0][1] = 40
tab[0][2] = 10
tab[0][3] = 20
tab[2][1] = 45

plt.imshow(tab, interpolation='nearest')
plt.show()
print"vuvuv"