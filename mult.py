import pandas as pd
import numpy as np


def f(*params: float) -> float: 
    res = 1
    for num in params:
        res *= num
    return res


def generate_data(n):
    data = []

    for _ in range(n):

        X = np.random.uniform(-10, 10, 3)

        y = f(*X)
        data.append([*list(X), y])
    return data


def main():
    data = generate_data(5000)
    headings = ["a", "b", "c", "y"]
    df = pd.DataFrame(data, columns=headings)
    df.to_csv("a.csv", index=False)


if __name__ == "__main__":
    main()
