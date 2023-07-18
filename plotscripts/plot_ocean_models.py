# %%
import matplotlib.pyplot as plt
import numpy as np
import pickle
from src.parameters import c_s

# %% load results
result_single_layer = pickle.load(open("data/result_single_layer.pkl", "rb"))
result_two_layer = pickle.load(open("data/result_two_layer.pkl", "rb"))

# %% plot results single layer
fig, ax = plt.subplots()

result_single_layer.plot(ax=ax, label="single layer")

ax.legend()

# %% Plot results two layer
fig, ax = plt.subplots()
result_two_layer.plot(ax=ax, label="two layer", subplots=True)
plt.show()
# %% plot imbalance against T_s
fig, ax = plt.subplots()

ax.scatter(
    result_two_layer["T_s (K)"].values[:-1],
    c_s * np.diff(result_two_layer["imbalance (W/m^2)"]),
    label="two layer",
)
ax.scatter(
    result_single_layer["T_s (K)"].values[:-1],
    c_s * np.diff(result_single_layer["T_s (K)"]),
    label="single layer",
)

ax.legend()

# %%
