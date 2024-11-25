produits = "Baguette"
prix = 1
stock = 30

print(f"Produits = {produits}\nPrix = {prix}€\nQuantité = {stock}")

achat = int(input(f"Combien de {produits} voulez vous achetez ?"))

if achat > stock:
    print("Il n'y à pas assez de stock")
else:
    stock = stock - achat
    print(f"Il reste que {stock} {produits} en stock\n")

    prix = prix*1.10
    print(f"Le prix à subit l'inflation il augmente de 10%. Le prix est {prix}€")

    print(f"Produits = {produits}\nPrix = {prix}€\nQuantité = {stock}")