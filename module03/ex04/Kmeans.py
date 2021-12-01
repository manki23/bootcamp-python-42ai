import sys


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        # ... parameters control...
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        None.
        Raises:
        This function should not raise any Exception.
        """
        # ... your code ...
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        This function should not raise any Exception.
        """
        # ... your code ...

def print_usage(msg: str):
    print(f"InputError: {msg}", file=sys.stderr)
    print("Usage: python Kmeans.py filepath='<PATH>' ncentroid=<positive ",
          "integer> max_iter=<positive integer>", file=sys.stderr)

def main():
    if all('=' in arg for arg in sys.argv[1:]):
        kwargs = dict(arg.split('=') for arg in sys.argv[1:])
        if (
            len(kwargs) == 3 and
            'filepath' in kwargs.keys() and
            isinstance(kwargs['filepath'], str) and
            'ncentroid' in kwargs.keys() and
            kwargs['ncentroid'].isnumeric() and
            'max_iter' in kwargs.keys() and
            kwargs['max_iter'].isnumeric() and
            int(kwargs['max_iter']) > 0 and int(kwargs['ncentroid']) > 0
        ):
            kwargs['max_iter'] = int(kwargs['max_iter'])
            kwargs['ncentroid'] = int(kwargs['ncentroid'])
            print(kwargs)
        else:
            print_usage("invalid arguments")
    else:
        print_usage("invalid arguments")

if __name__ == '__main__':
    sys.exit(main())


# sklearn.cluster import kmeans
# function kmeans.fit and kmeans.predict
# figure 3d with mpl_toolkits.mplot3d import axes3d