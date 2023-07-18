#%%
import pickle
import matplotlib.pyplot as plt

#%%
result_coupled = pickle.load(open("data/result_coupled.pkl", "rb"))

# %%
fig, axes = plt.subplots(3, 2, figsize=(10, 10), sharex='col')

result_coupled['T_s (K)'].plot(ax=axes[0, 0])
axes[0, 0].set_title("T_s (K)")
result_coupled['T_d (K)'].plot(ax=axes[1, 0])
axes[1, 0].set_title("T_d (K)")
result_coupled['C_a (GtC)'].plot(ax=axes[0, 1])
axes[0, 1].set_title("C_a (GtC)")
result_coupled['C_l (GtC)'].plot(ax=axes[1, 1])
axes[1, 1].set_title("C_l (GtC)")
result_coupled['C_s (GtC)'].plot(ax=axes[2, 0])
axes[2, 0].set_title("C_s (GtC)")
result_coupled['C_d (GtC)'].plot(ax=axes[2, 1])
axes[2, 1].set_title("C_d (GtC)")

for ax in axes.flatten():
    ax.grid()
plt.show()

# %%