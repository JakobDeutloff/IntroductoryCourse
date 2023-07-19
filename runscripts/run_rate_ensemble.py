# %%
from scipy.integrate import solve_ivp
import numpy as np
from src.models import two_layer_ocean_and_carbon_cylce
from src.helper_functions import year_to_seconds, seconds_to_year
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from src.parameters import initial_emissions

# %% solve coupled  model
budget = 2000  # Emission budget in GtC

def run_model_with_rate(rate):

    time_turnaround = budget/rate  # Time until emissions are reversed in seconds
    t_end = 2 * time_turnaround  # simulation time in seconds

    # Run model
    result_coupled = solve_ivp(
        two_layer_ocean_and_carbon_cylce,
        t_span=[0, t_end],
        y0=[0, 0, 0, 0, 0, 0, 0],
        method="RK45",
        args=(time_turnaround, rate),
    )

    # Construct Dataframe
    ds_coupled = pd.DataFrame(
        index=seconds_to_year(result_coupled.t),
        data=result_coupled.y.T,
        columns=["T_s (K)", "T_d (K)", "C_a (GtC)", "C_l (GtC)", "C_s (GtC)", "C_d (GtC)", "Emmissions (GtC)"],
    )
    ds_coupled.index.name = "time (years)"

    return ds_coupled

# %% Run model with different rates
rates = np.arange(5, 16, 1)

results = {}
for rate in rates:
    ds_coupled = run_model_with_rate(rate/year_to_seconds(1))
    results[str(rate.round())] = ds_coupled
    

# %%
pickle.dump(results, open("data/TCRE_results.pkl", "wb"))
# %%
