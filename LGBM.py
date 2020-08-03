# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import lightgbm as lgb
from sklearn.model_selection import train_test_split


# %%
def LGBFineTuning(X, Y):
    X_train,Y_train,X_dev,Y_dev = train_test_split(X, y, test_size=0.10, random_state=1)
    d_train = lgb.Dataset(X_train, label=y_train)
    d_valid = lgb.Dataset(x_valid, label=y_valid)

    parameters = {
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': 'l1',
    'learning_rate': 0.005,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.7,
    'bagging_freq': 10,
    'verbose': 0,
    "max_depth": 8,
    "num_leaves": 128,  
    "max_bin": 512,
    "num_iterations": 1000,
    "early_stopping_rounds": 100
    "categorical_feature ":
    }

    model = lgb.train(parameters, d_train,valid_sets=d_valid)
    preds = model.predict(x_valid)


# %%



