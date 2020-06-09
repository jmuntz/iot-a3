import numpy as np
from sklearn.linear_model import LinearRegression

def setup():
    x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    y = np.array([5, 20, 14, 32, 22, 38])
    
    print(x)
    print(y)
    
    model = LinearRegression()

    #calcu-latte(ha-ha) optimum weights
    model.fit(x, y)
    
    #SHORTCUT:does two lines above at once
    #model = LinearRegression.fit(x, y)
    
    
#def get_results():
    #score are predictor x and regressor y
    r_sq = model.score(x, y)
    print('coefficient of determinaltion: ', r_sq)
    
    print('intercept:', model.intercept_)
    
    print('slope:', model.coef_)

    ### give y as a two dimensional array to see if results change
    new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
    print('intercept:', new_model.intercept_)
    print('slope:', new_model.coef_)
    
    ###Predict results( this will also be in a function below get_results()
    y_pred = model.predict(x)
    print('predicted response:', y_pred, sep='\n')


def predict_response(model): 
    y_pred = model.predict(x)
    print('predicted response:', y_pred, sep='\n')


if __name__ == "__main__":
    setup()