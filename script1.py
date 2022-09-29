#Lire la saisie de l'utilisateur
Debut = 1
Fin = 100000

for n in range(Debut,Fin + 1):
	if n > 1:
	    for i in range(2,n):
	        if (n % i) == 0:
	           break
	    else:
	        print(n)