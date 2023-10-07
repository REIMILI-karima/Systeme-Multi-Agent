from Rules import Regles
from Moteur_Inference import MoteurInference   
# Define the base de fait
baseFait = [
    "D",
    "O",
    "G",
    ]

# Define the rules
regles = [Regles(["A","B"], "F"),
    Regles(["F", "H"], "I"),
    Regles(["D", "H", "G"], "A"),
    Regles(["O", "G"], "H"),
    Regles(["E", "H"], "B"),
    Regles(["G", "A"], "B"),
    Regles(["G", "H"], "P"),
    Regles(["G", "H"], "Q"),
    Regles(["D", "G"], "J"),
    Regles(["D", "U"], "W")
]

moteur = MoteurInference(regles,baseFait)

moteur.forward_chain()
con=moteur.get_conl()
prem=moteur.get_prem()
print(con)
print(prem)
fait="A"
facts= moteur.get_fact_base()
print("la base de fait est : ",facts)
if fait in facts :
    print("\nLe fait :",fait,"est vrai")
else:
    print("Le fait :",fait,"est faux")
