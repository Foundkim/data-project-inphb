




def parse_model(X, use_columns):
    """parse model 

    Args:
        X ([dataframe]): [pandas dataframe]
        use_columns ([list]): [list of columns selected for the model]

    Raises:
        ValueError: [target column survived should belong to df]

    Returns:
        [features]: [selected features ]
        [target]: [target to predict]
    """
    if "Survived" not in X.columns:
        raise ValueError("target column survived should belong to df")
    target = X["Survived"]
    X = X[use_columns]
    return X, target
