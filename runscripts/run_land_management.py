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
    args=(True,),
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
    args=(False,),
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
