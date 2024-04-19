class CitiesData:
    def __init__(self):
        # Initialisation des villes
        self.cities = [
            "Casablanca", "Rabat", "Marrakech", "Fès", "Tanger",
            "Agadir", "Meknès", "Oujda", "Kenitra", "Safi",
            "Salé", "Tétouan", "Mohammedia", "El Jadida", "Nador",
            "Settat", "Khouribga", "Laâyoune", "Beni Mellal", "Essaouira"
        ]

        # Initialisation de la matrice des distances (en km)
        self.distances = [
            [0, 94, 244, 293, 339, 383, 242, 504, 110, 246, 94, 354, 28, 103, 526, 58, 128, 1426, 255, 357],
            [94, 0, 331, 203, 250, 547, 149, 520, 45, 331, 9, 267, 67, 179, 463, 111, 161, 1572, 243, 381],
            [244, 331, 0, 484, 567, 247, 440, 673, 300, 175, 322, 624, 252, 174, 741, 220, 282, 2145, 196, 177],
            [293, 203, 484, 0, 354, 799, 69, 321, 178, 471, 202, 265, 283, 404, 304, 300, 258, 1755, 324, 470],
            [339, 250, 567, 354, 0, 806, 219, 371, 296, 599, 242, 65, 312, 357, 188, 308, 276, 2200, 507, 603],
            [383, 547, 247, 799, 806, 0, 720, 1007, 516, 176, 543, 886, 355, 169, 1136, 328, 286, 1366, 321, 173],
            [242, 149, 440, 69, 219, 720, 0, 396, 123, 412, 157, 266, 214, 296, 288, 186, 134, 1790, 191, 371],
            [504, 520, 673, 321, 371, 1007, 396, 0, 484, 761, 516, 389, 521, 626, 160, 550, 464, 2101, 523, 731],
            [110, 45, 300, 178, 296, 516, 123, 484, 0, 290, 40, 263, 83, 127, 476, 75, 138, 1541, 200, 324],
            [246, 331, 175, 471, 599, 176, 412, 761, 290, 0, 329, 633, 257, 174, 780, 233, 296, 2072, 227, 169],
            [94, 9, 322, 202, 242, 543, 157, 516, 40, 329, 0, 268, 64, 173, 475, 110, 164, 1575, 239, 379],
            [354, 267, 624, 265, 65, 886, 266, 389, 263, 633, 268, 0, 327, 454, 197, 342, 325, 2306, 521, 704],
            [28, 67, 252, 283, 312, 355, 214, 521, 83, 257, 64, 327, 0, 130, 528, 93, 165, 1454, 227, 340],
            [103, 179, 174, 404, 357, 169, 296, 626, 127, 174, 173, 454, 130, 0, 657, 128, 194, 1597, 186, 188],
            [526, 463, 741, 304, 188, 1136, 288, 160, 476, 780, 475, 197, 528, 657, 0, 540, 466, 2260, 548, 774],
            [58, 111, 220, 300, 308, 328, 186, 550, 75, 233, 110, 342, 93, 128, 540, 0, 68, 1469, 178, 235],
            [128, 161, 282, 258, 276, 286, 134, 464, 138, 296, 164, 325, 165, 194, 466, 68, 0, 1465, 182, 300],
            [1426, 1572, 2145, 1755, 2200, 1366, 1790, 2101, 1541, 2072, 1575, 2306, 1454, 1597, 2260, 1469, 1465, 0, 1876, 1514],
            [255, 243, 196, 324, 507, 321, 191, 523, 200, 227, 239, 521, 227, 186, 548, 178, 182, 1876, 0, 285],
            [357, 381, 177, 470, 603, 173, 371, 731, 324, 169, 379, 704, 340, 188, 774, 235, 300, 1514, 285, 0]
        ]

    def distance(self, first_city, second_city):
        # Obtenir les indices des villes dans la liste
        index_first_city = self.cities.index(first_city)
        index_second_city = self.cities.index(second_city)

        # Retourner la distance entre les villes à partir de la matrice des distances
        return self.distances[index_first_city][index_second_city]

    def shortest_path_length(self):
        # Retourner la longueur du chemin le plus court entre toutes les villes
        return len(self.cities) - 1

    def number_of_possible_paths(self):
        # Calculer le nombre total de chemins possibles entre toutes les villes
        n = len(self.cities)
        answer = 1

        # Calcul de n!
        for i in range(1, n + 1):
            answer *= i

        return answer

    def __str__(self):
        # Représentation de l'instance en chaîne de caractères
        return 'Cities: ' + ' '.join(self.cities)


# Exemple d'utilisation de la classe CitiesData
data = CitiesData()
print(data)

# Obtenir la distance entre deux villes
first_city = "Casablanca"
second_city = "Rabat"
print(f"Distance entre {first_city} et {second_city}: {data.distance(first_city, second_city)} km")

# Obtenir la longueur du chemin le plus court entre toutes les villes
print(f"Longueur du chemin le plus court entre toutes les villes: {data.shortest_path_length()}")

# Obtenir le nombre total de chemins possibles entre toutes les villes
print(f"Nombre total de chemins possibles entre toutes les villes: {data.number_of_possible_paths()}")
