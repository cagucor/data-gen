import numpy as np
import pandas as pd
import argparse
import random
from pyquaternion import Quaternion


def generate_data(n):
    data = []

    for _ in range(n):
        # Create Rotation Quaternion
        rotation_axis_x = np.random.uniform(-1, 1, 1)
        rotation_axis_y = np.random.uniform(-1, 1, 1)
        rotation_axis_z = np.random.uniform(-1, 1, 1)
        # if bool(random.randint(0, 1)):
        #     rotation_axis_x *= -1
        # if bool(random.randint(0, 1)):
        #     rotation_axis_y *= -1
        # if bool(random.randint(0, 1)):
        #     rotation_axis_z *= -1
        rotation_axis = np.array([rotation_axis_x, rotation_axis_y, rotation_axis_z])
        rotation_axis /= np.linalg.norm(rotation_axis)

        theta_dir = 1
        if bool(random.randint(0, 1)):
            theta_dir *= -1
        rotation_theta = np.random.uniform(0.1, 0.25, 1)
        rotation_theta *= theta_dir
        # num_steps = random.randint(3, 4)
        num_steps = 10
        # Point of Interest (end effector position relative to joint)
        point = np.random.uniform(-1, 1, 3)

        for _ in range(num_steps):
            

            # Create small variations in state variables
            # axial_shift = np.random.uniform(-0.01, 0.01, 3)
            # rotation_axis += axial_shift
            # rotation_axis /= np.linalg.norm(rotation_axis)

            q = Quaternion(axis=rotation_axis, angle=rotation_theta)

            data_point = []
            # Rotation
            point_prime = q.rotate(point)
            # point_prime = np.round(np.array(point_prime), decimals=4)

            data_point = np.append(rotation_theta, rotation_axis)
            data_point = np.append(data_point, np.array(point))
            data_point = np.append(data_point, np.array(point_prime))
            data.append(data_point)

            point = point_prime

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--Samples", help="Generated sample count", type=int)
    parser.add_argument("-o", "--OutputFile", help="Output file name", type=str)
    args = parser.parse_args()

    n = 100
    file_name = "test.csv"
    if args.Samples:
        n = args.Samples
    if args.OutputFile:
        file_name = args.OutputFile + ".csv"

    data = generate_data(n)
    headings = [
        "theta_delta",
        "x_hat",
        "y_hat",
        "z_hat",
        "x",
        "y",
        "z",
        "x_prime",
        "y_prime",
        "z_prime",
    ]
    df = pd.DataFrame(data, columns=headings)
    df.to_csv(file_name, index=False)
