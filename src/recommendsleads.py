import pandas as pd

class RecommendsLeads:
    def leads(self, market_cluster, portfolio):
        customers = market_cluster.merge(portfolio['id'], indicator=True, how='outer')
        customers = customers[customers['_merge'] == 'both']

        customer_0 = customers['cluster'].value_counts().index[0]
        customer_1 = customers['cluster'].value_counts().index[1]
        customer_2 = customers['cluster'].value_counts().index[2]

        future_customer_0 = market_cluster[(market_cluster['cluster'] == customer_0)]
        future_customer_1 = market_cluster[(market_cluster['cluster'] == customer_1)]
        future_customer_2 = market_cluster[(market_cluster['cluster'] == customer_2)]

        future_customer = pd.concat([future_customer_0["id"], future_customer_1["id"], future_customer_2["id"]])
        return future_customer