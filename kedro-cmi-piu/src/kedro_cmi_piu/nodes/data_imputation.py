import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.neighbors import KNeighborsRegressor


def featureImputation(
        dataTrain: pd.DataFrame,
        dataTest: pd.DataFrame,
        target_col: str,
):

    ### Median imputation for now
    numerical_dtypes = [
        col for col in dataTrain.columns if is_numeric_dtype(dataTrain[col]) and col != target_col
    ]

    for col in numerical_dtypes:
        if dataTrain[col].isna().sum() > 0:
            dataTrain[col] = dataTrain[col].fillna(
                dataTrain[col].median()
            )

            dataTest[col] = dataTest[col].fillna(
                dataTrain[col].median()
            )
    return dataTrain, dataTest


def targetImputation(
        dataTrain: pd.DataFrame,
        target_col: str,
        scaler_type: str = "robust",
):
    if scaler_type.lower() == "robust":
        scaler = RobustScaler()
    else:
        scaler = StandardScaler()

    dataTrain = scaler.fit_transform(dataTrain)

    # KNN model for target imputation
    ###############################################################################
    # Split dataset into train (with known target) and test (with missing target) #
    ###############################################################################

    dataTrain_tgt = dataTrain[dataTrain[target_col].notna()]
    dataTrain_tgt_nan = dataTrain[dataTrain[target_col].isna()]

    knn_model = KNeighborsRegressor(n_neighbors=3)
    knn_model.fit(dataTrain_tgt.drop(columns=target_col), dataTrain_tgt[target_col])
    dataTrain_tgt_nan.loc[:, target_col] = knn_model.predict(dataTrain_tgt_nan.drop(columns=target_col))

    dataImputed = pd.concat([dataTrain_tgt, dataTrain_tgt_nan])

    return dataImputed
