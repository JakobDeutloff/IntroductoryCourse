# %%
from scipy.integrate import solve_ivp
import numpy as np
from src.models import model_with_landmanagement
from src.helper_functions import year_to_seconds, seconds_to_year
import pickle
import pandas as pd
from src.plotfunctions import plot_all_outputs

# %% Run model with land management
t_end = year_to_seconds(4e3)  # simulation time in seconds
result = solve_ivp(
    model_with_landmanagement,
    t_span=[0, t_end],
    y0=[0, 0, 0, 0, 0, 0, 0, 0],
    method="RK45",
    args=(True, False),
    t_eval=np.arange(0, t_end, year_to_seconds(1)),
)

# Construct Dataframe
ds_land_management = pd.DataFrame(
    index=seconds_to_year(result.t),
    data=result.y.T,
    columns=[
        "T_s (K)",
        "T_d (K)",
        "C_a (GtC)",
        "C_l (GtC)",
        "C_s (GtC)",
        "C_d (GtC)",
        "Emmissions (GtC)",
        "C_m (GtC)",
    ],
)
ds_land_management.index.name = "time (years)"
pickle.dump(ds_land_management, open("data/land_management.pkl", "wb"))

# %% Run model without land management

result = solve_ivp(
    model_with_landmanagement,
    t_span=[0, t_end],
    y0=[0, 0, 0, 0, 0, 0, 0, 0],
    method="RK45",
    args=(False, False),
    t_eval=np.arange(0, t_end, year_to_seconds(1)),
)

# Construct Dataframe
ds_no_land_management = pd.DataFrame(
    index=seconds_to_year(result.t),
    data=result.y.T,
    columns=[
        "T_s (K)",
        "T_d (K)",
        "C_a (GtC)",
        "C_l (GtC)",
        "C_s (GtC)",
        "C_d (GtC)",
        "Emmissions (GtC)",
        "C_m (GtC)",
    ],
)
ds_no_land_management.index.name = "time (years)"
pickle.dump(ds_no_land_management, open("data/no_land_management.pkl", "wb"))

# %% run pulse experiment

result_pulse_and_reduction = solve_ivp(
    model_with_landmanagement,
    t_span=[0, year_to_seconds(4000)],
    y0=[0, 0, 0, 0, 0, 0, 0, 0],
    method="RK45",
    args=(False, 1000),
    t_eval=np.arange(0, t_end, year_to_seconds(1)),
)

# Construct Dataframe
ds_pulse_and_reduction = pd.DataFrame(
    index=seconds_to_year(result_pulse_and_reduction.t),
    data=result_pulse_and_reduction.y.T,
    columns=[
        "T_s (K)",
        "T_d (K)",
        "C_a (GtC)",
        "C_l (GtC)",
        "C_s (GtC)",
        "C_d (GtC)",
        "Emmissions (GtC)",
        "C_m (GtC)",
    ],
)
ds_pulse_and_reduction.index.name = "time (years)"
pickle.dump(ds_pulse_and_reduction, open("data/reduction_1000.pkl", "wb"))


# %%
fig = plot_all_outputs(ds_pulse_and_reduction)
# %%
