import pandas as pd



def setIndex(
        data: pd.DataFrame,
):
    return data.set_index("id")


def featureSelection(
        data: pd.DataFrame,
        target_col: str,
        feature_list: list = None,
):
    if feature_list:
        data = data[feature_list]

    else:
        train_columns_to_drop = [i for i in data.columns if "PCIAT" in i or "sii" in i]
        data = data[
            train_columns_to_drop + [target_col]
        ]

    return data
