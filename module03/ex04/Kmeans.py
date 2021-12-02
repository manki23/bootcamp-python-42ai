import sys
import numpy as np
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
        self.kmeans = KMeans(n_clusters=self.ncentroid, max_iter=self.max_iter)

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids
        from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(X, np.ndarray):
            self.kmeans.fit(X)
            self.centroids.append(self.kmeans.cluster_centers_)

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
        if isinstance(X, np.ndarray):
            return self.kmeans.predict(X)


def print_usage(msg: str):
    print(f"InputError: {msg}", file=sys.stderr)
    print("Usage: python Kmeans.py filepath='<PATH>' ncentroid=<positive ",
          "integer> max_iter=<positive integer>", file=sys.stderr)


def check_arguments(**kwargs):
    return (
            len(kwargs) == 3 and
            'filepath' in kwargs.keys() and
            isinstance(kwargs['filepath'], str) and
            'ncentroid' in kwargs.keys() and
            kwargs['ncentroid'].isnumeric() and
            'max_iter' in kwargs.keys() and
            kwargs['max_iter'].isnumeric() and
            int(kwargs['max_iter']) > 0 and int(kwargs['ncentroid']) > 0
        )


def plt_show(data, kmc, labels):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    x = data[..., 1:2]
    y = data[..., 2:3]
    z = data[..., 3:4]
    ax.scatter(
        x,
        y,
        z,
        label='Courbe',
        marker="o",
        c=labels.astype(float),
        edgecolor="k"
    )
    centroids_x = kmc.centroids[0][..., 0:1]
    centroids_y = kmc.centroids[0][..., 1:2]
    centroids_z = kmc.centroids[0][..., 2:3]
    ax.scatter(
        centroids_x,
        centroids_y,
        centroids_z,
        label='Courbe',
        marker="x",
        c="#000"
    )
    ax.set_xlabel('X: height')
    ax.set_ylabel('Y: weight')
    ax.set_zlabel('Z: bone_density')
    plt.tight_layout()
    plt.show()


def main():
    if all('=' in arg for arg in sys.argv[1:]):
        kwargs = dict(arg.split('=') for arg in sys.argv[1:])
        if check_arguments(**kwargs):
            kwargs['max_iter'] = int(kwargs['max_iter'])
            kwargs['ncentroid'] = int(kwargs['ncentroid'])
            try:
                data = np.genfromtxt(
                    kwargs['filepath'], delimiter=',', skip_header=1
                )
                kmc = KmeansClustering(kwargs['max_iter'], kwargs['ncentroid'])
                kmc.fit(data[..., 1:])
                labels = kmc.predict(data[..., 1:])
                plt_show(data, kmc, labels)
            except Exception as e:
                print(f"{e.__class__.__name__}:", e, file=sys.stderr)
                sys.exit()
        else:
            print_usage("invalid arguments")
    else:
        print_usage("invalid arguments")


if __name__ == '__main__':
    sys.exit(main())
