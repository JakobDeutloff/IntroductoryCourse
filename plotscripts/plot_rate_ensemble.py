# %%
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import pickle
import numpy as np

# %%
results = pickle.load(open("data/TCRE_results.pkl", "rb"))
results_uncoupled = pickle.load(open("data/TCRE_results_doc_disabled.pkl", "rb"))

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
def plot_T_vs_E(results):
    fig, axes = plt.subplots(figsize=(7, 7))

    for i, rate in enumerate(list(results.keys())):
        axes.plot(
            results[rate]["Emmissions (GtC)"],
            results[rate]["T_s (K)"],
            color=colors[i],
            label=str(rate) + " (GtC/Year)",
        )
        axes.set_ylabel("Ocean Surface Temperature (K)")
        axes.set_xlabel("Cumulative Emmissions (GtC)")
    handles, labels = axes.get_legend_handles_labels()
    fig.subplots_adjust(bottom=0.2)
    fig.legend(handles, labels, loc="lower center", ncols=5)
    axes.grid()

    return fig, axes


fig, axes = plot_T_vs_E(results)
fig.savefig("plots/rates_ensemble_T_vs_E.png", bbox_inches="tight")
fig, axes = plot_T_vs_E(results_uncoupled)
fig.savefig("plots/rates_ensemble_T_vs_E_uncoupled.png", bbox_inches="tight")


# %% plot carbon components
def plot_carbon(results, results_uncoupled=None):
    fig, axes = plt.subplots(2, 2, figsize=(10, 10), sharex="col")

    axes[0, 0].plot(results["10"]["C_a (GtC)"], color="k", label="Coupled")
    axes[0, 0].set_ylabel("Atmospheric Carbon (GtC)")
    axes[0, 1].plot(results["10"]["C_l (GtC)"], color="k", label="Coupled")
    axes[0, 1].set_ylabel("Land Carbon (GtC)")
    axes[1, 0].plot(results["10"]["C_s (GtC)"], color="k", label="Coupled")
    axes[1, 0].set_ylabel("Surface Ocean Carbon (GtC)")
    axes[1, 1].plot(results["10"]["C_d (GtC)"], color="k", label="Coupled")
    axes[1, 1].set_ylabel("Deep Ocean Carbon (GtC)")

    if results_uncoupled is not None:
        axes[0, 0].plot(
            results_uncoupled["10"]["C_a (GtC)"], color="r", label="Uncoupled"
        )
        axes[0, 1].plot(
            results_uncoupled["10"]["C_l (GtC)"], color="r", label="Uncoupled"
        )
        axes[1, 0].plot(
            results_uncoupled["10"]["C_s (GtC)"], color="r", label="Uncoupled"
        )
        axes[1, 1].plot(
            results_uncoupled["10"]["C_d (GtC)"], color="r", label="Uncoupled"
        )

    for ax in axes.flatten():
        ax.grid()

    handles, labels = axes[0, 1].get_legend_handles_labels()
    fig.subplots_adjust(bottom=0.07)
    fig.legend(handles, labels, loc="lower center", ncols=2)
    fig.suptitle("Carbon Components for 10 GtC/Year Emissions")
    return fig, axes


fig, axes = plot_carbon(results)
fig.savefig("plots/carbon_components_coupled.png", bbox_inches="tight")
fig, axes = plot_carbon(results, results_uncoupled)
fig.savefig("plots/carbon_components_uncoupled.png", bbox_inches="tight")

# %% plot T vs Emissions Uncoupled for 10 GtC/Year

fig, ax = plt.subplots(figsize=(7, 7))

ax.plot(
    results_uncoupled["10"]["Emmissions (GtC)"],
    results_uncoupled["10"]["T_s (K)"],
    color="r",
    label="10 GtC/Year",
)

ax.legend()
ax.set_ylabel("Ocean Surface Temperature (K)")
ax.set_xlabel("Cumulative Emmissions (GtC)")
ax.grid()
fig.savefig("plots/rates_ensemble_T_vs_E_uncoupled_10.png")

# %% plot T vs Emissions Uncoupled for 5 and 10 GtC/Year

fig, ax = plt.subplots(figsize=(7, 7))

ax.plot(
    results_uncoupled["10"]["Emmissions (GtC)"],
    results_uncoupled["10"]["T_s (K)"],
    color="r",
    label="10 GtC/Year",
)
ax.plot(
    results_uncoupled["5"]["Emmissions (GtC)"],
    results_uncoupled["5"]["T_s (K)"],
    color="b",
    label="5 GtC/Year",
)
ax.legend()
ax.set_ylabel("Ocean Surface Temperature (K)")
ax.set_xlabel("Cumulative Emmissions (GtC)")
ax.grid()
fig.savefig("plots/rates_ensemble_T_vs_E_uncoupled_10_5.png")

# %% plot deep ocean temperature uncoupled

fig, ax = plt.subplots(figsize=(7, 7))


ax.plot(results_uncoupled["10"]['T_d (K)'], color='r', label='Deep Ocean 10 GtC/Year')
ax.plot(results_uncoupled["5"]['T_d (K)'], color='r', label='Deep Ocean 5 GtC/Year', linestyle='--')
ax.plot(results_uncoupled["10"]['T_s (K)'], color='b', linestyle='-', label='Surface Ocean GtC/Year')
ax.plot(results_uncoupled["5"]['T_s (K)'], color='b', linestyle='--', label='Surface Ocean GtC/Year')
ax.legend()
ax.set_ylabel("Temperature (K)", color='r')
ax.set_xlabel("Time (years)")
ax.grid()
fig.savefig("plots/rates_ensemble_T_d_uncoupled_10_5.png")

# %% 
