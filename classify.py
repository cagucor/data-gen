import pandas
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pandas.read_csv("y_z.csv")
features = [
    "theta_delta",
    "x_hat",
    # "y_hat",
    # "z_hat",
]

# target = ["M+(x_prime; x)", "M-(x_prime; x)", "M~(x_prime; x)"]
# target = ["M+(x_prime; y)", "M-(x_prime; y)", "M~(x_prime; y)"]
target = ["M+(y_prime; z)", "M-(y_prime; z)", "M~(y_prime; z)"]
X = df[features]
# y = df["q_x"]
# y = df["q_y"]
y = df["q_z"]

dtree = DecisionTreeClassifier(ccp_alpha=0.0000005, criterion="entropy", max_depth=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
dtree = dtree.fit(X_train, y_train)

y_train_pred = dtree.predict(X_train)
y_test_pred = dtree.predict(X_test)
print(accuracy_score(y_train, y_train_pred), accuracy_score(y_test, y_test_pred))

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4), dpi=300)
# class_names = ['M+(x_prime; x)', 'M-(x_prime; x)', 'M~(x_prime; x)']
# class_names = ['M+(x_prime; y)', 'M-(x_prime; y)', 'M~(x_prime; y)']
class_names = ['M+(y_prime; z)', 'M-(y_prime; z)', 'M~(y_prime; z)']
tree.plot_tree(dtree, feature_names=features, class_names=class_names)
# tree.export_graphviz(dtree)
fig.savefig("image.svg")
