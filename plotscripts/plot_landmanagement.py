# %%
import matplotlib.pyplot as plt
import pickle

# %% Load data
ds_land_management = pickle.load(open("data/land_management.pkl", "rb"))
ds_no_land_management = pickle.load(open("data/no_land_management.pkl", "rb"))
ds_1000 = pickle.load(open("data/reduction_1000.pkl", "rb"))
ds_500 = pickle.load(open("data/reduction_500.pkl", "rb"))
ds_250 = pickle.load(open("data/reduction_250.pkl", "rb"))
ds_100 = pickle.load(open("data/reduction_100.pkl", "rb"))
ds_20 = pickle.load(open("data/reduction_20.pkl", "rb"))

pulse_experiments = {
    "20": ds_20,
    "100": ds_100,
    "250": ds_250,
    "500": ds_500,
    "1000": ds_1000,
}


# %% Plot lines of land management scenario
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
    axes[0, 0].set_ylabel(r"$\mathrm{T_s}$ /K")
    axes[0, 0].set_title("Surface Ocean Temperature")

    axes[0, 1].plot(
        ds_land_management["C_l (GtC)"], label="with land management", color="green"
    )
    axes[0, 1].plot(
        ds_no_land_management["C_l (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[0, 1].set_ylabel(r"$\mathrm{C_l}$ /GtC")
    axes[0, 1].set_title("Land Carbon")

    axes[1, 0].plot(
        ds_land_management["T_d (K)"], label="with land management", color="green"
    )
    axes[1, 0].plot(
        ds_no_land_management["T_d (K)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[1, 0].set_ylabel(r"$\mathrm{T_d}$ /K")
    axes[1, 0].set_title("Deep Ocean Temperature")

    axes[1, 1].plot(
        ds_land_management["C_a (GtC)"], label="with land management", color="green"
    )
    axes[1, 1].plot(
        ds_no_land_management["C_a (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[1, 1].set_ylabel(r"$\mathrm{C_a}$ /GtC")
    axes[1, 1].set_title("Atmospheric Carbon")

    axes[0, 2].plot(
        ds_land_management["C_s (GtC)"], label="with land management", color="green"
    )
    axes[0, 2].plot(
        ds_no_land_management["C_s (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[0, 2].set_ylabel(r"$\mathrm{C_s}$ /GtC")
    axes[0, 2].set_title("Surface Ocean Carbon")

    axes[1, 2].plot(
        ds_land_management["C_d (GtC)"], label="with land management", color="green"
    )
    axes[1, 2].plot(
        ds_no_land_management["C_d (GtC)"],
        label="without land management",
        color="k",
        linestyle="--",
    )
    axes[1, 2].set_ylabel(r"$\mathrm{C_d}$ /GtC")
    axes[1, 2].set_title("Deep Ocean Carbon")

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
    axes[0, 3].set_ylabel("Emissions (GtC)")
    axes[0, 3].set_title("Emissions")

    axes[1, 3].plot(
        ds_land_management["C_m (GtC)"], label="Reduction Pulse", color="green"
    )
    axes[1, 3].plot(
        ds_no_land_management["C_m (GtC)"],
        label="Standard",
        color="k",
        linestyle="--",
    )
    axes[1, 3].set_ylabel(r"$\mathrm{C_m}$ /GtC")
    axes[1, 3].set_title("Land Management Carbon")

    for ax in axes.flatten():
        ax.grid()

    for ax in axes[1, :]:
        ax.set_xlabel("time /years")

    fig.tight_layout()
    fig.subplots_adjust(bottom=0.1)
    handles, labels = axes[1, 3].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2)

    return fig, axes

# %%
fig, axes = plot_landuse(ds_land_management, ds_no_land_management, 1300)
fig.savefig("plots/land_management.png", dpi=300)

# %% Plot lines of pulse experiment

fig, axes = plot_landuse(ds_500, ds_no_land_management, 2000)
axes[1, 3].remove()
fig.savefig("plots/pulse_500.png", dpi=300)

# %% Calculate fractions of land use

fractions = {}
pulse_fractions = {"20": {}, "100": {}, "250": {}, "500": {}, "1000": {}}
keys = ["C_a (GtC)", "C_l (GtC)", "C_s (GtC)", "C_d (GtC)"]
pulses = ["20", "100", "250", "500", "1000"]

for key in keys:
    fractions[key] = ds_no_land_management[key] - ds_land_management[key]
    for pulse in pulses:
        pulse_fractions[pulse][key] = (
            ds_no_land_management[key] - pulse_experiments[pulse][key]
        )


# %% plot fractions of land management

fig, ax = plt.subplots(figsize=(8, 5))
time_end = 1300
time_start = 250

ax.fill_between(
    fractions["C_a (GtC)"][time_start:time_end].index,
    (
        fractions["C_a (GtC)"]
        + fractions["C_d (GtC)"]
        + fractions[("C_s (GtC)")]
        + fractions["C_l (GtC)"]
    )[time_start:time_end],
    label="Atmosphere",
    color="grey",
)

ax.fill_between(
    fractions["C_l (GtC)"][time_start:time_end].index,
    (fractions["C_l (GtC)"] + fractions["C_s (GtC)"] + fractions["C_d (GtC)"])[
        time_start:time_end
    ],
    label="Land",
    color="green",
)

ax.fill_between(
    fractions["C_s (GtC)"][time_start:time_end].index,
    (fractions["C_s (GtC)"] + fractions["C_d (GtC)"])[time_start:time_end],
    label="Surface Ocean",
    color="lightblue",
)

ax.fill_between(
    fractions["C_d (GtC)"][time_start:time_end].index,
    fractions["C_d (GtC)"][time_start:time_end],
    label="Deep Ocean",
    color="darkblue",
)

ax.legend()
ax.set_ylabel("Carbon Sequestered by Land Management /GtC")
ax.set_xlabel("Time /Years")
fig.savefig("plots/land_management_fractions.png", dpi=300)

# %% Subplots emission pulses

fig, ax = plt.subplots(1, 1, figsize=(8, 5), sharex="col", sharey="row")


time_start = 550
time_end = 2000
fractions = pulse_fractions["10"]

ax.fill_between(
    fractions["C_a (GtC)"][time_start:time_end].index,
    (
        fractions["C_a (GtC)"]
        + fractions["C_d (GtC)"]
        + fractions["C_s (GtC)"]
        + fractions["C_l (GtC)"]
    )[time_start:time_end],
    color="darkblue",
    label="Deep Ocean",
)

ax.fill_between(
    fractions["C_a (GtC)"][time_start:time_end].index,
    (fractions["C_l (GtC)"] + fractions["C_s (GtC)"] + fractions["C_a (GtC)"])[
        time_start:time_end
    ],
    color="lightblue",
    label="Surface Ocean",
)

ax.fill_between(
    fractions["C_a (GtC)"][time_start:time_end].index,
    (fractions["C_l (GtC)"] + fractions["C_a (GtC)"])[time_start:time_end],
    label="Land",
    color="green",
)

ax.fill_between(
    fractions["C_a (GtC)"][time_start:time_end].index,
    fractions["C_a (GtC)"][time_start:time_end],
    label="Atmosphere",
    color="grey",
)

plt.show()

# %% calculate reuctions in atmospheric carbon

reductions = {"10": {}, "50": {}, "250": {}, "1000": {}}
lags = list(reductions.keys())

for lag in lags:
    for pulse in ['20', '100', '1000']:
        reference = (
            ds_no_land_management["C_a (GtC)"][555]
            - pulse_experiments[pulse]["C_a (GtC)"][555]
        )
        reductions[lag][pulse] = (
            (
                ds_no_land_management["C_a (GtC)"][555 + int(lag)]
                - pulse_experiments[pulse]["C_a (GtC)"][555 + int(lag)]
            )
        ) / reference

# %%
