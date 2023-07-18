# %%
from scipy.integrate import solve_ivp
import numpy as np
from src.models import single_layer_ocean, two_layer_ocean
from src.helper_functions import year_to_seconds, seconds_to_year
import pickle
import pandas as pd

# %% solve one layer  model
t_end = year_to_seconds(1e2)  # simulation time in year

result_single_layer = solve_ivp(
    single_layer_ocean,
    t_span=[0, t_end],
    y0=[0],
    t_eval=np.arange(0, t_end, year_to_seconds(1/10)),
)

# %% solve two layer model
t_end = year_to_seconds(1e4)
result_two_layer = solve_ivp(
    two_layer_ocean,
    t_span=[0, t_end],
    y0=[0, 0, 0],
    t_eval=np.arange(0, t_end, year_to_seconds(1/10)),
    method="RK45",
)

# %% construct pandas dataframes

ds_single_layer = pd.DataFrame(
    index=seconds_to_year(result_single_layer.t),
    data=result_single_layer.y.T,
    columns=["T_s (K)"]
)
ds_single_layer.index.name = "time (years)"

ds_two_layer = pd.DataFrame(index=seconds_to_year(result_two_layer.t),
                            data=result_two_layer.y.T,
                            columns=["T_s (K)", "T_d (K)", "imbalance (W/m^2)"])
ds_two_layer.index.name = "time (years)"
# %% Save results
pickle.dump(ds_single_layer, open("data/result_single_layer.pkl", "wb"))
pickle.dump(ds_two_layer, open("data/result_two_layer.pkl", "wb"))


# %%
