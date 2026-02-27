# importare la libreria
import matplotlib.pyplot as plt

# # comando per disegnare un punto a x 1 e y 3 
# plt.scatter(1,3, color="red")
# plt.scatter(-2,-5, color="red")
# # con color posso specificare il colore di tutti gli elementi
# plt.axhline(0, color = "green") # asse x
# plt.axvline(0, color = "green") # asse y
# # comando per far vedere una griglia
# plt.grid()
# # comando per far vedere il disegno
# plt.show()

#######################################################################
# posso indicare le coordinate di un punto
# usando le variabili x e y
# x = 1
# y = 3
# come x e y posso usare numeri singoli ma posso 
# usare anche liste di numeri
# x = [1, 5, -3, 4]
# y = [0, -2, 3, -8]
# plt.scatter(x,y)

#############################################################
# chiedo all'utente le coordinate del punto
# x = int(input("Qual è la X del punto? "))
# y = int(input("E la y? "))
# plt.scatter(x,y)

#####################################################
# per disegnare tanti punti senza dover mettere il
# comando ogni volta, posso usare for e while

# for i in range(80):
#     plt.scatter(i,2) # cambio solo una delle due variabili e ottengo una linea orizzontale

###########################################################
# disegno la retta x = y + 2
# imposto le liste x e y
# x = []
# y = []
# # imposto il for affinchè cambi lui la x 
# # (la i corrisponde alla x)
# for i in range(-20,20):
#     x.append(i)
#     y.append(i + 2)
# # se l'equazione fosse y = 17x + 22 -x + 3
# # comando che disegna i punti
# plt.scatter(x,y)

###################################################
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

# import matplotlib.pyplot as plt

# voti = []

# for i in range(5):
#     voto = int(input("Inserisci un voto: "))
#     voti.append(voto)

# x = [1, 2, 3, 4, 5]

# plt.plot(x, voti, marker="o")

# plt.title("Andamento voti")
# plt.xlabel("Verifica numero")
# plt.ylabel("Voto")

# plt.show()


