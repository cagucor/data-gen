import numpy as np
import pandas as pd


def f(a, b):
    return np.cos(a) + b[0] * b[1] ** 2 - 5 * b[2]

def main():
    data = []

    for i in range(1000):
        a = np.random.uniform(-2,2,1)
        b = np.random.uniform(-10, 10, 3)
        t_data = np.append(a, b)
        t_data = np.append(t_data, f(a,b))
        data.append(t_data)

    df = pd.DataFrame(data)
    df.to_csv("trial.csv", index=False, header=False)

    print(df)


main()
