import numpy as np


class TOPSISWithSubCriteria:
    def __init__(self, data, sub_criteria_weights, criteria_weights, criteria_types):
        """
        Initialize the TOPSIS instance with sub-criteria.

        :param data: Matrix of alternatives with sub-criteria included and alternative labels.
        :param sub_criteria_weights: Dictionary with main criteria and their sub-criteria weights.
        :param criteria_weights: List of weights for the main criteria.
        :param criteria_types: List indicating 'benefit' or 'cost' for each main criterion.
        """
        self.data = data
        self.sub_criteria_weights = sub_criteria_weights
        self.criteria_weights = np.array(criteria_weights, dtype=float)
        self.criteria_types = criteria_types

    def aggregate_sub_criteria(self):
        """Aggregate sub-criteria to form main criteria scores."""
        aggregated_data = []
        for alt in self.data:
            row = []
            for criterion, weights in self.sub_criteria_weights.items():
                sub_values = np.array(alt[criterion])
                sub_weights = np.array(weights)
                aggregated_score = np.sum(sub_values * sub_weights)
                row.append(aggregated_score)
            aggregated_data.append(row)
        return np.array(aggregated_data)

    def normalize_matrix(self, aggregated_data):
        """Normalize the decision matrix."""
        norm_data = aggregated_data / np.sqrt((aggregated_data ** 2).sum(axis=0))
        return norm_data

    def weighted_normalized_matrix(self, norm_data):
        """Calculate the weighted normalized decision matrix."""
        weighted_data = norm_data * self.criteria_weights
        return weighted_data

    def ideal_solutions(self, weighted_data):
        """Determine the ideal (best) and anti-ideal (worst) solutions."""
        ideal_best = np.amax(weighted_data, axis=0) * (self.criteria_types == 'benefit') + \
                     np.amin(weighted_data, axis=0) * (self.criteria_types == 'cost')

        ideal_worst = np.amin(weighted_data, axis=0) * (self.criteria_types == 'benefit') + \
                      np.amax(weighted_data, axis=0) * (self.criteria_types == 'cost')

        return ideal_best, ideal_worst

    def calculate_distances(self, weighted_data, ideal_best, ideal_worst):
        """Calculate the distance of each alternative to the ideal and anti-ideal solutions."""
        dist_to_ideal_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
        dist_to_ideal_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))
        return dist_to_ideal_best, dist_to_ideal_worst

    def calculate_preferences(self, dist_to_ideal_best, dist_to_ideal_worst):
        """Calculate the preference value for each alternative."""
        preferences = dist_to_ideal_worst / (dist_to_ideal_best + dist_to_ideal_worst)
        return preferences

    def rank(self):
        """Perform the entire TOPSIS process with sub-criteria and return rankings."""
        aggregated_data = self.aggregate_sub_criteria()
        print("Aggregated Data:\n", aggregated_data)

        norm_data = self.normalize_matrix(aggregated_data)
        print("Normalized Data:\n", norm_data)

        weighted_data = self.weighted_normalized_matrix(norm_data)
        print("Weighted Normalized Data:\n", weighted_data)

        ideal_best, ideal_worst = self.ideal_solutions(weighted_data)
        print(f"Ideal Best: {ideal_best}")
        print(f"Ideal Worst: {ideal_worst}")

        dist_to_ideal_best, dist_to_ideal_worst = self.calculate_distances(weighted_data, ideal_best, ideal_worst)
        print(f"Distance to Ideal Best: {dist_to_ideal_best}")
        print(f"Distance to Ideal Worst: {dist_to_ideal_worst}")

        preferences = self.calculate_preferences(dist_to_ideal_best, dist_to_ideal_worst)
        print(f"Preferences: {preferences}")
        rankings = np.argsort(preferences)[::-1]
        return preferences, rankings


# # Example usage:
# data = [
#     {'Alternatif': 'Product A', 'Harga': [400], 'Kualitas': [7, 6], 'Durasi': [8]},
#     {'Alternatif': 'Product B', 'Harga': [500], 'Kualitas': [8, 7], 'Durasi': [6]},
#     {'Alternatif': 'Product C', 'Harga': [300], 'Kualitas': [6, 5], 'Durasi': [7]},
#     {'Alternatif': 'Product D', 'Harga': [1200], 'Kualitas': [6, 5], 'Durasi': [9]},
#     {'Alternatif': 'Product E', 'Harga': [700], 'Kualitas': [7, 5], 'Durasi': [8]},
#     {'Alternatif': 'Product F', 'Harga': [900], 'Kualitas': [8, 6], 'Durasi': [7]},
#     {'Alternatif': 'Product G', 'Harga': [1000], 'Kualitas': [7, 7], 'Durasi': [5]},
#     {'Alternatif': 'Product H', 'Harga': [650], 'Kualitas': [5, 4], 'Durasi': [7]},
#     {'Alternatif': 'Product I', 'Harga': [550], 'Kualitas': [6, 5], 'Durasi': [6]},
#     {'Alternatif': 'Product J', 'Harga': [300], 'Kualitas': [7, 6], 'Durasi': [9]}
# ]
#
# sub_criteria_weights = {
#     'Harga': [1],
#     'Kualitas': [0.4, 0.6],
#     'Durasi': [1]
# }
# criteria_weights = [0.4, 0.4, 0.2]
# criteria_types = np.array(['cost', 'benefit', 'benefit'])
#
# topsis = TOPSISWithSubCriteria(data, sub_criteria_weights, criteria_weights, criteria_types)
# preferences, rankings = topsis.rank()
#
# # Print Preferences and Rankings with Product Labels
# print("\nPreferences:", preferences)
# print("\nRankings (Best to Worst):")
# for rank_index in rankings:
#     print(data[rank_index]['Alternatif'])  # Print the product name according to the ranking
