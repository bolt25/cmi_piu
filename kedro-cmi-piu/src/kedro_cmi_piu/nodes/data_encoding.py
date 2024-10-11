import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def encodeCategorical(
    dataTrain: pd.DataFrame,
    dataTest: pd.DataFrame,
):
    ohe_dict = {}

    ################################################################################################
    dataTrainEncoded = pd.DataFrame(index=dataTrain.index)
    obj_dtypes = [k for k, v in dataTrain.dtypes.items() if v == "O"]  # and k != "id"]

    for col in obj_dtypes:
        encoder = OneHotEncoder()
        featureEncoded = pd.DataFrame(
            encoder.fit_transform(
                dataTrain[
                    [col]
                ]
            ).toarray(),
            columns=encoder.get_feature_names_out(),
            dtype=int,
            index=dataTrain.index
        )
        ohe_dict[col] = encoder  # updating ohe_dict to store col encoder
        dataTrainEncoded = pd.concat(
            [dataTrainEncoded, featureEncoded],
            axis=1
        )

    dataTrainEncoded = pd.concat(
        [
            dataTrainEncoded,
            dataTrain.drop(columns=obj_dtypes)
        ],
        axis=1
    )

    ################################################################################################
    dataTestEncoded = pd.DataFrame(index=dataTest.index)

    for col, encoder in ohe_dict.items():
        featureEncoded = pd.DataFrame(
            encoder.transform(
                dataTest[
                    [col]
                ]
            ).toarray(),
            columns=encoder.get_feature_names_out(),
            dtype=int,
            index=dataTestEncoded.index
        )

        dataTestEncoded = pd.concat(
            [dataTestEncoded, featureEncoded],
            axis=1
        )

    # obj_dtypes = list(ohe_dict.keys())
    dataTestEncoded = pd.concat(
        [
            dataTestEncoded,
            dataTest.drop(columns=obj_dtypes)
        ],
        axis=1
    )

    return dataTrainEncoded, dataTestEncoded
