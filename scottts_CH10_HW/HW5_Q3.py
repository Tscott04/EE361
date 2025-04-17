import math
import random

class KMeans:
    def __init__(self, k=5, max_passes=5, initial_centroids=None, distance_metric='euclidean'):
        self.k = k
        self.max_passes = max_passes
        self.initial_centroids = initial_centroids
        self.distance_metric = distance_metric
        self.centroids = []
        self.clusters = []

    def euclidean_distance(self, point1, point2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

    def manhattan_distance(self, point1, point2):
        return sum(abs(a - b) for a, b in zip(point1, point2))

    def get_distance(self, point1, point2):
        if self.distance_metric == 'manhattan':
            return self.manhattan_distance(point1, point2)
        return self.euclidean_distance(point1, point2)

    def fit(self, data):
        # Random centroid initialization if not provided
        if self.initial_centroids:
            self.centroids = self.initial_centroids
        else:
            random_indices = random.sample(range(len(data)), self.k)
            self.centroids = [data[i][:] for i in random_indices]

        for i in range(self.max_passes):
            print(f"**** PASS {i + 1} ****")
            self.clusters = [[] for _ in range(self.k)]
            prev_centroids = [c[:] for c in self.centroids]

            # Assign points to clusters
            for idx, point in enumerate(data):
                distances = [self.get_distance(point, centroid) for centroid in self.centroids]
                closest = distances.index(min(distances))
                self.clusters[closest].append(idx)

            # Recalculate centroids
            for cluster_idx in range(self.k):
                cluster_points = [data[idx] for idx in self.clusters[cluster_idx]]
                if cluster_points:
                    new_centroid = [sum(dim) / len(cluster_points) for dim in zip(*cluster_points)]
                    self.centroids[cluster_idx] = new_centroid
                else:
                    self.centroids[cluster_idx] = [0] * len(data[0])

            # Show current cluster memberships
            for c_idx, cluster in enumerate(self.clusters):
                print(f"CLUSTER #{c_idx + 1}:", end=" ")
                for idx in cluster:
                    print(data[idx], end=" ")
                print()
            print("Centroids:", self.centroids)
            print()

    def predict_gradeGroup(self, new_data):
        predictions = []
        for point in new_data:
            distances = [self.get_distance(point, centroid) for centroid in self.centroids]
            cluster_idx = distances.index(min(distances))
            predictions.append(cluster_idx)
        return predictions


def read_file(filename):
    with open(filename, 'r') as file:
        return [[int(line.strip())] for line in file if line.strip()]

# Load original exam scores
data = read_file("cs150exams.txt")

# Create KMeans with random centroid initialization
kmeans = KMeans(k=5, max_passes=5, distance_metric='euclidean')
kmeans.fit(data)

# New scores to predict
new_scores = [[35], [58], [90], [92], [100]]
cluster_predictions = kmeans.predict_gradeGroup(new_scores)

# Output the cluster each new score belongs to
print("\n--- New Score Cluster Assignments ---")
for score, cluster in zip(new_scores, cluster_predictions):
    print(f"Score {score[0]} => Cluster #{cluster}")
