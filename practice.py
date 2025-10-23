#Banker Roulette
import random
names=input("Give me everybody's names, separated by a comma\n")
name=names.split(", ")
nam=len(name)
ranch=random.randint(0,nam-1)
payer=name[ranch]
print(payer + " will pay today's bill")
