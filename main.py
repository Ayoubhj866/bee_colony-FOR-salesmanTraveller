# Assurez-vous d'importer les classes CitiesData et BeeColony (si elles sont dans des fichiers séparés)
from cities_data import CitiesData
from bee_colony import BeeColony

# Créez une instance de la classe CitiesData
data = CitiesData()

# # Créez une instance de la classe BeeColony en passant l'instance de CitiesData
bee_colony = BeeColony(data)

# Exécutez la méthode solve_tsp de BeeColony pour résoudre le problème du voyageur de commerce
bee_colony.solve_tsp()
