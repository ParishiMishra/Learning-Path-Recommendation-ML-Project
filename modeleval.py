from sklearn.metrics import mean_squared_error
from model import *
import matplotlib as plt
y_pred=model.predict(X_scaled)
mse = mean_squared_error(y, y_pred)
print(f"Mean Squared Error: {mse}")
plt.scatter(y, y_pred)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.title("True v/s Predicted Values")
plt.show()