from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.ensemble import RandomForestRegressor

def model_factory(model_name):
    if model_name == 'linear_regression':
        return(LinearRegression)
    if model_name == 'huber_regressor':
        return(HuberRegressor)
    if model_name == 'random_forest_regressor':
        return(RandomForestRegressor)
    
def model(model_name):
    factory_obj = None
    try:
        factory_obj = model_factory(model_name)
    except ValueError as e:
        print(e)
    return factory_obj
