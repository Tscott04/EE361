import math

class KMeans:
    def __init__(self, k=5, max_passes=15, initial_centroids=None, distance_metric='euclidean'):
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
        self.centroids = self.initial_centroids or data[:self.k]
        stabilization_pass = None

        for i in range(self.max_passes):
            print(f"**** PASS {i + 1} ****")
            self.clusters = [[] for _ in range(self.k)]
            prev_centroids = [c[:] for c in self.centroids]  # deep copy

            # Assign each point to the nearest centroid
            for idx, point in enumerate(data):
                distances = [self.get_distance(point, centroid) for centroid in self.centroids]
                closest = distances.index(min(distances))
                self.clusters[closest].append(idx)

            # Update centroids
            for cluster_idx in range(self.k):
                cluster_points = [data[idx] for idx in self.clusters[cluster_idx]]
                if cluster_points:
                    new_centroid = [sum(dim) / len(cluster_points) for dim in zip(*cluster_points)]
                    self.centroids[cluster_idx] = new_centroid
                else:
                    self.centroids[cluster_idx] = [0] * len(data[0])  # avoid empty cluster crash

            # Print cluster contents
            for c_idx, cluster in enumerate(self.clusters):
                print(f"CLUSTER #{c_idx + 1}:", end=" ")
                for idx in cluster:
                    print(data[idx], end=" ")
                print()
            print("Centroids:", self.centroids)
            print()

            # Check for stabilization
            if prev_centroids == self.centroids and stabilization_pass is None:
                stabilization_pass = i + 1

        return stabilization_pass


def read_file(filename):
    with open(filename, 'r') as file:
        return [[int(line.strip())] for line in file if line.strip()]

data = read_file("cs150exams.txt")
initial_centroids = [[70], [80], [90], [90], [100]]

kmeans = KMeans(k=5, max_passes=15, initial_centroids=initial_centroids, distance_metric='manhattan')
stabilized_at = kmeans.fit(data)

if stabilized_at:
    print(f"\nCentroids stabilized at PASS {stabilized_at} using Manhattan distance.")
else:
    print("\nCentroids did not stabilize within 15 passes using Manhattan distance.")
