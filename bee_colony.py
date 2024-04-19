import random
from cities_data import CitiesData

data = CitiesData()



class BeeColony:
    def __init__(self, cities_data, num_bees=30, max_iterations=1000):
        self.cities_data = cities_data  # Instance de CitiesData pour accéder aux villes et aux distances
        self.num_bees = num_bees  # Nombre d'abeilles (taille de la colonie)
        self.max_iterations = max_iterations  # Nombre maximal d'itérations pour l'algorithme
        self.best_path = None  # Meilleur chemin trouvé
        self.best_path_quality = float('inf')  # Qualité du meilleur chemin

    def random_path(self):
        # Générer un chemin aléatoire à travers toutes les villes
        path = self.cities_data.cities[:]
        random.shuffle(path)
        return path

    def path_quality(self, path):
        # Calculer la qualité d'un chemin donné (longueur totale du chemin)
        quality = 0
        for i in range(len(path) - 1):
            quality += self.cities_data.distance(path[i], path[i + 1])
        quality += self.cities_data.distance(path[-1], path[0])  # Retour à la ville de départ
        return quality

    def solve_tsp(self):
        # Initialiser la ruche d'abeilles
        hive = [self.random_path() for _ in range(self.num_bees)]

        # Afficher les informations initiales
        print("Démarrage de l'algorithme de colonies d'abeilles (Bee Colony)")
        print(f"Chargement des données des villes pour l'analyse du problème du voyageur de commerce...")
        print(f"Nombre de villes : {len(self.cities_data.cities)}")
        print(f"Nombre de chemins possibles : {self.cities_data.number_of_possible_paths():,}")
        print(f"Meilleure solution possible (longueur de chemin la plus courte) : {self.cities_data.shortest_path_length():.4f}")
        print("\nRuche initiale aléatoire")
        print(f"Chemin initial trouvé : {' -> '.join(hive[0])}")
        print(f"Qualité du chemin initial : {self.path_quality(hive[0]):.4f}\n")

        # Boucle de traitement principale de l'algorithme de colonies d'abeilles
        print("Entrée dans la boucle principale de l'algorithme de colonies d'abeilles pour le problème du voyageur de commerce...")
        iteration = 0
        while iteration < self.max_iterations:
            # Recherche de nourriture par les abeilles et mise à jour de la ruche
            for bee_index in range(self.num_bees):
                new_path = hive[bee_index][:]
                # Mutation aléatoire d'une portion du chemin
                i, j = random.sample(range(len(new_path)), 2)
                new_path[i], new_path[j] = new_path[j], new_path[i]
                
                new_path_quality = self.path_quality(new_path)
                current_path_quality = self.path_quality(hive[bee_index])
                
                # Mise à jour de la ruche si le nouveau chemin est meilleur
                if new_path_quality < current_path_quality:
                    hive[bee_index] = new_path
                
                # Vérifier si le nouveau chemin est le meilleur trouvé
                if new_path_quality < self.best_path_quality:
                    self.best_path = new_path
                    self.best_path_quality = new_path_quality
            
            # Afficher les progrès (facultatif)
            if iteration % 100 == 0:
                print(f"Progression : itération {iteration}, meilleure qualité de chemin {self.best_path_quality:.4f}")
            
            iteration += 1
        
        # Afficher la ruche finale et la meilleure solution trouvée
        print("\nRuche finale")
        print(f"Meilleur chemin trouvé : {' -> '.join(self.best_path)}")
        print(f"Qualité du chemin : {self.best_path_quality:.4f}")
        print("Fin de l'algorithme de colonies d'abeilles.")

# Exemple d'utilisation de l'algorithme de colonies d'abeilles
# data = CitiesData()
# bee_colony = BeeColony(data)
# bee_colony.solve_tsp()
