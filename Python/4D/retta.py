# importare la libreria
import matplotlib.pyplot as plt
# # equazione generica della retta è 
# y = mx + q
x = []
y = []
# chiedo all'utente m e q 
m = int(input("Dimmi il valore di m: "))
q = int(input("Dimmi il valore di q: "))

for i in range(-20,20):
    x.append(i)
    y.append(m*i + q)
    
plt.plot(x,y)

plt.axhline(0, color = "green") # asse x
plt.axvline(0, color = "green") # asse y
# # comando per far vedere una griglia
plt.grid()
# # comando per far vedere il disegno
plt.show()