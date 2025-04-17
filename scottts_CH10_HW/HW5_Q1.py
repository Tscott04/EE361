import math

class KMeans:
    def __init__(self, k=5, max_passes=15, initial_centroids=None):
        self.k = k
        self.max_passes = max_passes
        self.initial_centroids = initial_centroids
        self.centroids = []
        self.clusters = []

    def euclidean_distance(self, point1, point2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

    def fit(self, data):
        self.centroids = self.initial_centroids or data[:self.k]
        prev_centroids = None
        stabilization_pass = None

        for i in range(self.max_passes):
            print(f"**** PASS {i + 1} ****")
            self.clusters = [[] for _ in range(self.k)]

            for idx, point in enumerate(data):
                distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
                closest = distances.index(min(distances))
                self.clusters[closest].append(idx)

            prev_centroids = self.centroids.copy()
            new_centroids = []

            for cluster in self.clusters:
                if cluster:
                    summed = [0] * len(data[0])
                    for idx in cluster:
                        for d in range(len(data[0])):
                            summed[d] += data[idx][d]
                    averaged = [s / len(cluster) for s in summed]
                    new_centroids.append(averaged)
                else:
                    new_centroids.append([0] * len(data[0]))  # empty cluster

            self.centroids = new_centroids

            # Print clusters
            for i, cluster in enumerate(self.clusters):
                print(f"CLUSTER #{i + 1}: ", end="")
                for idx in cluster:
                    print(data[idx], end=" ")
                print()
            print("Centroids:", self.centroids)
            print()

            # Check if centroids have stabilized
            if prev_centroids == self.centroids and stabilization_pass is None:
                stabilization_pass = i + 1

        return stabilization_pass

def read_file(filename):
    with open(filename, 'r') as file:
        return [[int(line.strip())] for line in file if line.strip()]

# Load data
data = read_file("cs150exams.txt")

# Set initial centroids manually as per the question
initial_centroids = [[70], [80], [90], [90], [100]]

# Create KMeans instance and run
kmeans = KMeans(k=5, max_passes=15, initial_centroids=initial_centroids)
stabilized_at = kmeans.fit(data)

# Final output
if stabilized_at:
    print(f"Centroids stabilized at PASS {stabilized_at}")
else:
    print("Centroids did not stabilize within 15 passes.")
