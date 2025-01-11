from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def creer_modele(X_train, y_train):
    modele = LinearRegression()
    modele.fit(X_train, y_train)
    return modele

def evaluer_performance(modele, X_test, y_test):
    y_pred = modele.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    return r2, mae
