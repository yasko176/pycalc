import sys

# Vérifier que nous avons bien 3 arguments
if len(sys.argv) != 4:
    print("Usage: python pycalc.py <opérande1> <opérateur> <opérande2>")
    sys.exit(1)

# Récupérer les arguments
operand1 = float(sys.argv[1])  # Premier opérande
operator = sys.argv[2]         # Opérateur (+, -, *, /)
operand2 = float(sys.argv[3])  # Deuxième opérande

# Effectuer le calcul en fonction de l'opérateur
if operator == '+':
    result = operand1 + operand2


# Afficher le résultat
print(result)