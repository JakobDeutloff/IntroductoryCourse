# %%
from scipy.integrate import solve_ivp
import numpy as np
from src.models import two_layer_ocean_and_carbon_cylce
from src.helper_functions import year_to_seconds, seconds_to_year
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# %% solve coupled  model
t_end = year_to_seconds(3e3)  # simulation time in year

result_coupled = solve_ivp(
    two_layer_ocean_and_carbon_cylce,
    t_span=[0, t_end],
    y0=[0, 0, 0, 0, 0, 0],
    method="RK45",
)
# %% Construct Dataframe

ds_coupled = pd.DataFrame(
    index=seconds_to_year(result_coupled.t),
    data=result_coupled.y.T,
    columns=["T_s (K)", "T_d (K)", "C_a (GtC)", "C_l (GtC)", "C_s (GtC)", "C_d (GtC)"],
)
ds_coupled.index.name = "time (years)"

pickle.dump(ds_coupled, open("data/result_coupled.pkl", "wb"))


# %%
