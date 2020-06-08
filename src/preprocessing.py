import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

class PreProcessing:
    def process(self, market):
        Id = market['id']
        market = market.drop("Unnamed: 0", axis=1)
        market = market[market.columns[market.isna().mean() < 0.30]]

        market_num = pd.DataFrame(market.select_dtypes(include=[np.number]))
        col_mark_num = market_num.columns

        print("Replacing Nan by the mean")
        imputer = SimpleImputer(strategy='mean')
        imputer = imputer.fit(market_num)
        market_num = pd.DataFrame(imputer.transform(market_num))
        market_num.columns = col_mark_num

        market_obj = market.select_dtypes(exclude=[np.number])
        col_mark_obj = market_obj.columns

        market_obj = market_obj.iloc[:, [2, 3, 4, 5, 6, 7, 13, 18, 19, 25, 26, 27, 28, 30, 31, 33, 34]]

        missing = {'setor': 'COMERCIO', 'dt_situacao': '2005-11-03', 'nm_divisao': 'COMERCIO VAREJISTA',
                   'nm_segmento': 'COMERCIO; REPARACAO DE VEICULOS AUTOMOTORES E MOTOCICLETAS',
                   'sg_uf_matriz': 'MA', 'de_saude_tributaria': 'VERDE',
                   'de_saude_rescencia': 'ACIMA DE 1 ANO', 'de_nivel_atividade': 'MEDIA',
                   'nm_meso_regiao': 'CENTRO AMAZONENSE', 'nm_micro_regiao': 'MANAUS',
                   'de_faixa_faturamento_estimado': 'DE R$ 81.000,01 A R$ 360.000,00',
                   'de_faixa_faturamento_estimado_grupo': 'DE R$ 81.000,01 A R$ 360.000,00'}

        market_obj = market_obj.fillna(value=missing)
        col_mark_obj = market_obj.columns

        print("Replacing categorical variables with numbers")
        labelencoder = LabelEncoder()
        for x in range(17):
            market_obj[market_obj.columns[x]] = labelencoder.fit_transform(market_obj[market_obj.columns[x]])

        market = pd.concat([market_obj, market_num], axis=1)
        col_market = market.columns

        print("Normalizing variables")
        scaler = MinMaxScaler()
        market = pd.DataFrame(scaler.fit_transform(market), columns=col_market)
        market = pd.concat([Id,market], axis = 1)
        print("Market database is ready!")
        return market

