import matplotlib.pyplot as plt

# disegno un punto con delle coordinate
# plt.scatter(1,4, color = "red")
# plt.scatter(-2,-7, color = "red")

# posso mettere le variabili x e y da usare con i punti
# se metto delle liste di numeri nelle variabili, ottengo
# più punti disegnati nel grafico
# x = [2,5,8,5,6]
# y = [1,6,2,4,7]
# plt.scatter(x,y)

# # disegno assi x e y
# plt.axhline(0)
# plt.axvline(0)

# per disegnare un istogramma ho bisogno di dati 
# anni della classe
# dati = [15, 17, 16, 16, 15, 17, 17, 16, 16, 15, 15, 18]
# plt.hist(dati, color = "red", edgecolor = "blue")

# python mi chiede dati fino a quando non gli dico stop
# con i dati che ottiene, disegna un grafico
dati = []

anno = input("Dimmi quanti anni hai: ")
while anno != "stop":
    dati.append(int(anno))
    anno = input("Dimmi quanti anni hai (stop per smettere): ")

# quando finisce il while disegno il grafico con
# i dati che ho raccolto
plt.hist(dati, edgecolor = "black")

# comando per far vedere una griglia
# plt.grid()
# comando per far vedere il disegno
plt.show()
