import numpy as np
import pandas as pd

data = np.empty([0, 5])
for _ in range(10):
    theta = np.random.uniform(0, 2 * np.pi)
    point = np.array([np.random.uniform(-2, 2), np.random.uniform(-2, 2)])

    rot_matrix = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    )

    point_prime = np.matmul(rot_matrix, point)

    temp_data = point
    temp_data = np.append(temp_data, theta)
    temp_data = np.append(temp_data, point_prime)
    data = np.round(np.vstack([data, temp_data]), 4)

print(data)

df = pd.DataFrame(data)
