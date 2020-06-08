import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class ModelTrainning:
    def trainning(self, market, cluster):
        Id = market['id']
        market = market.drop("id", axis=1)
        pca = PCA(n_components=2)
        market_pca = pca.fit_transform(market)

        print("Applying K-Means algorithm")
        km = KMeans(n_clusters=cluster)
        y_km = km.fit_predict(market_pca)

        market_cluster = pd.concat([Id, pd.DataFrame(y_km)], axis=1)
        market_cluster.columns = ['id', 'cluster']
        print("Market database is ready!")
        return market_cluster