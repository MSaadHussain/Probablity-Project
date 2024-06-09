import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

def generate_synthetic_data():
    np.random.seed(0)
    x = np.random.rand(100) * 10  
    y = 2.5 * x + np.random.randn(100) * 2  
    return x, y

def perform_linear_regression(x, y):
    x = x.reshape(-1, 1)  
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    return model, y_pred

def plot_regression(x, y, y_pred):
    plt.scatter(x, y, color='blue', label='Actual data')
    plt.plot(x, y_pred, color='red', label='Fitted line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Simple Linear Regression')
    plt.legend()
    plt.show()

def calculate_correlation(x, y):
    correlation, _ = pearsonr(x, y)
    return correlation

def main():
    print("Choose an option:")
    print("1. Use synthetic data")
    print("2. Enter your own data")

    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        x, y = generate_synthetic_data()
    elif choice == 2:
        x = list(map(float, input("Enter X values separated by commas: ").split(',')))
        y = list(map(float, input("Enter Y values separated by commas: ").split(',')))
        x = np.array(x)
        y = np.array(y)
    else:
        print("Invalid choice")
        return

    model, y_pred = perform_linear_regression(x, y)
    plot_regression(x, y, y_pred)
    correlation = calculate_correlation(x, y)
    
    print(f"Linear Regression Coefficients: {model.coef_}")
    print(f"Linear Regression Intercept: {model.intercept_}")
    print(f"Correlation Coefficient: {correlation}")

if __name__ == "__main__":
    main()
