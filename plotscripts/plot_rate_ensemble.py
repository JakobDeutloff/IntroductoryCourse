# %%
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import pickle
import numpy as np

# %%
results = pickle.load(open("data/TCRE_results.pkl", "rb"))

# %% plot single quantities
fig, axes = plt.subplots(2, 3, figsize=(14, 10))
colors = pl.cm.jet(np.linspace(0, 1, len(results.keys())))
for i, rate in enumerate(list(results.keys())):
    axes[0, 0].plot(results[rate]["T_s (K)"], color=colors[i], label=str(rate))
    axes[0, 0].set_ylabel("T_s (K)")
    axes[0, 1].plot(
        results[rate]["C_l (GtC)"], color=colors[i], label=(str(rate) + " (GtC/Year)")
    )
    axes[0, 1].set_ylabel("C_l (GtC)")
    axes[1, 0].plot(results[rate]["T_d (K)"], color=colors[i], label=str(rate))
    axes[1, 0].set_ylabel("T_d (K)")
    axes[1, 1].plot(results[rate]["C_a (GtC)"], color=colors[i], label=str(rate))
    axes[1, 1].set_ylabel("C_a (GtC)")
    axes[0, 2].plot(results[rate]["C_s (GtC)"], color=colors[i], label=str(rate))
    axes[0, 2].set_ylabel("C_s (GtC)")
    axes[1, 2].plot(results[rate]["C_d (GtC)"], color=colors[i], label=str(rate))
    axes[1, 2].set_ylabel("C_d (GtC)")
handles, labels = axes[0, 1].get_legend_handles_labels()
fig.subplots_adjust(bottom=0.15)
fig.legend(handles, labels, loc="lower center", ncols=5)
fig.savefig("plots/rates_ensemble.png", bbox_inches="tight")

# %% plot T vs Emissions

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

for i, rate in enumerate(list(results.keys())):
    axes[0].plot(
        results[rate]["Emmissions (GtC)"],
        results[rate]["T_s (K)"],
        color=colors[i],
        label=str(rate) + " (GtC/Year)",
    )
    axes[0].set_ylabel("T_s (K)")
    axes[0].set_xlabel("Emmissions (GtC)")
    axes[1].plot(
        results[rate]["Emmissions (GtC)"],
        results[rate]["T_d (K)"],
        color=colors[i],
        label=str(rate),
    )
    axes[1].set_ylabel("T_d (K)")
    axes[1].set_xlabel("Emmissions (GtC)")
handles, labels = axes[0].get_legend_handles_labels()
fig.subplots_adjust(bottom=0.2)
fig.legend(handles, labels, loc="lower center", ncols=5)
fig.savefig("plots/rates_ensemble_T_vs_E.png", bbox_inches="tight")


# %%
