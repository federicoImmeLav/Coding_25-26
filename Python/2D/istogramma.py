import matplotlib.pyplot as plt

dati = [23, 45, 12, 67, 34, 89, 56, 23, 45, 78]

plt.hist(dati, bins=5, color='steelblue', edgecolor='black')
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()






# import matplotlib.pyplot as plt
# import numpy as np

# ore_di_sonno = [7, 6, 8, 5, 9, 7, 6, 8, 7, 6]

# # Calcola le frequenze (conta quante volte compare ogni valore)
# valori, frequenze = np.unique(ore_di_sonno, return_counts=True)

# # Disegna la linea spezzata
# plt.plot(valori, frequenze, marker='o')

# plt.title("Ore di sonno - poligono delle frequenze")
# plt.xlabel("Ore")
# plt.ylabel("Quanti ragazzi")
# plt.show()