from os import environ as os_environ
from sys import argv as sys_argv
import pandas as pd

import mlflow


if __name__ == "__main__":

    # get RUN_ID from sys_argv[1], raise error if not set
    if len(sys_argv) < 2:
        raise ValueError(
            "Usage: python predict.py RUN_ID"
        )
    RUN_ID = sys_argv[1]

    logged_model = f'runs:/{RUN_ID}/iris_rf5'

    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict on a Pandas DataFrame.
    pred_result = loaded_model.predict(pd.DataFrame({
        'sepal length (cm)': [5.1],
        'sepal width (cm)': [3.5],
        'petal length (cm)': [1.4],
        'petal width (cm)': [0.2]
    }))

    print("Prediction: %s" % pred_result[0])