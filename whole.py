import numpy as np
import pandas as pd
import argparse
import random
from pyquaternion import Quaternion


def generate_data(n):
    data = []

    for _ in range(n):
        rotation_axis = []
        rotation_theta = []
        point = np.random.uniform(-1, 1, 3)
        for _ in range(7):
            # Create Rotation Quaternion
            temp_rotation_axis_x = np.random.uniform(-1, 1, 1)
            temp_rotation_axis_y = np.random.uniform(-1, 1, 1)
            temp_rotation_axis_z = np.random.uniform(-1, 1, 1)
            # if bool(random.randint(0, 1)):
            #     rotation_axis_x *= -1
            # if bool(random.randint(0, 1)):
            #     rotation_axis_y *= -1
            # if bool(random.randint(0, 1)):
            #     rotation_axis_z *= -1
            temp_rotation_axis = np.array([temp_rotation_axis_x, temp_rotation_axis_y, temp_rotation_axis_z])
            temp_rotation_axis /= np.linalg.norm(temp_rotation_axis)
            temp_rotation_theta = np.random.uniform(0.1, 0.25, 1)
            if bool(random.randint(0, 1)):
                temp_rotation_theta *= -1
            # num_steps = random.randint(3, 4)
            num_steps = 10
            # Point of Interest (end effector position relative to joint)
            rotation_axis.append(temp_rotation_axis)
            rotation_theta.append(temp_rotation_theta)


        
        for _ in range(num_steps):

            # Create small variations in state variables
            # axial_shift = np.random.uniform(-0.01, 0.01, 3)
            # rotation_axis += axial_shift
            # rotation_axis /= np.linalg.norm(rotation_axis)
            temp_point = point
            for i in range(7):

                q = Quaternion(axis=rotation_axis[i], angle=rotation_theta[i])
                # Rotation
                temp_point = q.rotate(temp_point)
            point_prime = temp_point
            data_point = []
            
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

    n = 1000
    file_name = "test.csv"
    if args.Samples:
        n = args.Samples
    if args.OutputFile:
        file_name = args.OutputFile + ".csv"

    data = generate_data(n)
    headings = [
        "theta_delta_0",
        "x_hat_0",
        "y_hat_0",
        "z_hat_0",
        "theta_delta_1",
        "x_hat_1",
        "y_hat_1",
        "z_hat_1",
        "theta_delta_2",
        "x_hat_2",
        "y_hat_2",
        "z_hat_2",
        "theta_delta_3",
        "x_hat_3",
        "y_hat_3",
        "z_hat_3",
        "theta_delta_4",
        "x_hat_4",
        "y_hat_4",
        "z_hat_4",
        "theta_delta_5",
        "x_hat_5",
        "y_hat_5",
        "z_hat_5",
        "theta_delta_6",
        "x_hat_6",
        "y_hat_6",
        "z_hat_6",
        "x",
        "y",
        "z",
        "x_prime",
        "y_prime",
        "z_prime",
    ]
    df = pd.DataFrame(data, columns=headings)
    df.to_csv(file_name, index=False)
