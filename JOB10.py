investissement = int(input("Entrez le montant de votre investissement :"))
rendement = int(input("Entre le rendement :"))

gain_annuel = investissement//100 * rendement
print(f"Le gain annuel pour un investissement de {investissement}€ à un rendement de {rendement}% est de {gain_annuel}€.")

investissement = investissement + gain_annuel + 5000
print(f"Ajout de 5000€ à l'investissement initial. Investissement : {investissement}")
rendement = rendement + 2
print(f"Ajout de 2% au rendement. Rendement : {rendement}%")

gain_annuel = investissement//100 * rendement
print(f"Le gain annuel pour un investissement de {investissement}€ à un rendement de {rendement}% est de {gain_annuel}€.")

investissement = investissement + gain_annuel - 1.10
print(f"Perte de 10% sur l'investissement. Investissement : {investissement}")
rendement = rendement - 1
print(f"Perte de 1% au rendement. Rendement {rendement}%")

gain_annuel = investissement//100 * rendement
print(f"Le gain annuel pour un investissement de {investissement}€ à un rendement de {rendement}% est de {gain_annuel}€.")