from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class ElbowTest:
    def elbow(self, market, cluster):
        market = market.drop("id", axis=1)
        pca = PCA(n_components=2)
        market_pca = pca.fit_transform(market)

        distortions = []
        for i in range(1, cluster):
            km = KMeans(n_clusters=i)
            km.fit(market_pca)
            distortions.append(km.inertia_)
        return distortions