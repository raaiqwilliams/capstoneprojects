#K-Means clustering implementation

#Some hints on how to start have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.
import pandas
import numpy as np
import scipy.spatial.distance as metric
np.random.seed(0)
from collections import defaultdict
from scipy.spatial import distance
from sklearn.cluster import KMeans

# ====
# Define a function that computes the distance between two data points
def find_distance(point1, point2, ax=1):
    return metric.euclidean(point1, point2)

# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
def readFile(file):
    return pandas.read_csv(file,header=0)
# ====
# Write the initialisation procedure
def initialize_clusters(dataset, k):
    #Variable n takes size of dataset
    n = np.shape(dataset)[1]
    #Initializing centroids array
    centroids = np.mat(np.zeros((k,n)))
    #Populating centroids randomly
    for j in range(n):
        min_j = min(dataset[:,j])
        range_j = float(max(dataset[:,j]) - min_j)
        centroids[:,j] = min_j + range_j * np.random.rand(k,1)

    return centroids
# ====
# Implement the k-means algorithm, using appropriate looping
def cluster(dataset, k, n):
    
    m = np.shape(dataset)[0]
    #Cluster assignments 
    cluster_assignments = np.mat(np.zeros((m,2)))
    #Initialization procedure by calling initialize_clusters function on values of data and number of clusters
    cents = initialize_clusters(dataset, k)
    cents_orig = cents.copy()
    #Loop will run for user-selected amount of iterations
    num_iter = n

    while num_iter != 0:
        
        for i in range(m):
            min_dist = np.inf
            min_index = -1

            for j in range(k):
                dist_ji = find_distance(cents[j,:], dataset[i,:])
                if dist_ji < min_dist:
                    min_dist = dist_ji
                    min_index = j

            cluster_assignments[i,:] = min_index, min_dist ** 2
            
            
        for cent in range(k):
            points = dataset[np.nonzero(cluster_assignments[:,0].A==cent)[0]]
            cents[cent,:] = np.mean(points, axis=0)
              
        num_iter -= 1

    return cents, cluster_assignments, cents_orig

#Generic predict function that takes the centroids and features of an instance x and returns a resulting cluster
def predict(centroids, x):
    distance_to_centroids = [find_distance(centroid,x) for centroid in centroids]
    return np.argmin(distance_to_centroids)

# ====
# Print out the results
def main():
    k = int(input("How many clusters would you like to plot? "))
    n_iter = int(input("How many iterations are required? "))
    print('-----------------------------')
    #Reading only columns with data values (Not country names)
    dataset = readFile('dataBoth.csv')
    data = dataset.to_numpy()
    X = data[:,[1,2]]
    
    centroids, clusters, cents_orig = cluster(X, k, n_iter)
    #Converted cluster to numpy array
    arrCluster = np.squeeze(np.asarray(clusters))
    deltas = np.sort(arrCluster,axis=0)
    #Created dictionary for easier data manipulation
    d = defaultdict(list)
    for i, v in deltas:
        d[i].append(v)
    d = {i:tuple(v) for i, v in d.items()}
    #Printing mean and number of items in each cluster
    for j in range(k):
        nrOfCountries = d.get(j)
        mean = sum(d[j]) / len(nrOfCountries)
        
        print("Mean for cluster ", j+1, ":", mean)
        print("Number of countries in cluster ", j+1 , ":" ,len(nrOfCountries))
    #Printing list of countries and clusters they belong to    
    print("-------------------")
    country_cluster = [predict(centroids, country) for country in X]
    dataset['cluster'] = country_cluster
    print(dataset.head)
    
if __name__ == '__main__':
    main()
