# Default imports
from sklearn.linear_model import Ridge
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data
np.random.seed(9)

# We have already loaded the data for you
data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')
# Write your solution here
def ridge(alpha):
    ridgeReg = Ridge(alpha=alpha,max_iter=100000, normalize=True,random_state=9)

    y_pred_train = ridgeReg.fit(X_test, y_test).predict(X_train)
    y_pred_test = ridgeReg.fit(X_train, y_train).predict(X_test)
    return ridgeReg, np.sqrt(mean_squared_error(y_train, y_pred_train)),np.sqrt(mean_squared_error(y_test, y_pred_test))


print ridge(0.01)
