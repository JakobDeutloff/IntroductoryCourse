# %%
import matplotlib.pyplot as plt
import pickle

# %% Load data
ds_land_management = pickle.load(open("data/land_management.pkl", "rb"))
ds_no_land_management = pickle.load(open("data/no_land_management.pkl", "rb"))


# %% Plot
def plot_landuse(ds_land_management, ds_no_land_management, year_end):
    ds_land_management = ds_land_management.loc[:year_end]
    ds_no_land_management = ds_no_land_management.loc[:year_end]

    fig, axes = plt.subplots(2, 4, figsize=(16, 10), sharex="col")
    axes[0, 0].plot(
        ds_land_management["T_s (K)"], label="with land management", color="green"
    )
    axes[0, 0].plot(
        ds_no_land_management["T_s (K)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[0, 0].set_ylabel("T_s (K)")
    axes[0, 1].plot(
        ds_land_management["C_l (GtC)"], label="with land management", color="green"
    )
    axes[0, 1].plot(
        ds_no_land_management["C_l (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[0, 1].set_ylabel("C_l (GtC)")
    axes[1, 0].plot(
        ds_land_management["T_d (K)"], label="with land management", color="green"
    )
    axes[1, 0].plot(
        ds_no_land_management["T_d (K)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[1, 0].set_ylabel("T_d (K)")
    axes[1, 1].plot(
        ds_land_management["C_a (GtC)"], label="with land management", color="green"
    )
    axes[1, 1].plot(
        ds_no_land_management["C_a (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[1, 1].set_ylabel("C_a (GtC)")
    axes[0, 2].plot(
        ds_land_management["C_s (GtC)"], label="with land management", color="green"
    )
    axes[0, 2].plot(
        ds_no_land_management["C_s (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[0, 2].set_ylabel("C_s (GtC)")
    axes[1, 2].plot(
        ds_land_management["C_d (GtC)"], label="with land management", color="green"
    )
    axes[1, 2].plot(
        ds_no_land_management["C_d (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[1, 2].set_ylabel("C_d (GtC)")
    axes[0, 3].plot(
        ds_land_management["Emmissions (GtC)"],
        label="with land management",
        color="green",
    )
    axes[0, 3].plot(
        ds_no_land_management["Emmissions (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[0, 3].set_ylabel("Emmissions (GtC)")
    axes[1, 3].plot(
        ds_land_management["C_m (GtC)"], label="with land management", color="green"
    )
    axes[1, 3].plot(
        ds_no_land_management["C_m (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[1, 3].set_ylabel("C_m (GtC)")

    for ax in axes.flatten():
        ax.grid()

    for ax in axes[1, :]:
        ax.set_xlabel("time (years)")

    fig.tight_layout()
    fig.subplots_adjust(bottom=0.1)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2)

    return fig


# %%

plot_landuse(ds_land_management, ds_no_land_management, 1000)

# %%
