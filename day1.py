# %%
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from src.parameters import *
from src.models import single_layer_ocean, two_layer_ocean


# %% solve model
timesteps = 1000
t_end = 500  # simulation time in year
t_end = t_end * 356 * 24 * 60 * 60

result_single_layer = solve_ivp(
    single_layer_ocean,
    t_span=[0, t_end],
    y0=[0],
    t_eval=np.linspace(0, t_end, timesteps),
)

result_two_layer = solve_ivp(
    two_layer_ocean,
    t_span=[0, t_end],
    y0=[0, 0],
    t_eval=np.linspace(0, t_end, timesteps),
    method="RK45",
)


# %% plot results
fig, ax = plt.subplots()
ax.plot(
    result_single_layer.t / (356 * 24 * 60 * 60),
    result_single_layer.y.squeeze(),
    label="T_s Single Layer Ocean",
)
ax.plot(
    result_two_layer.t / (356 * 24 * 60 * 60),
    result_two_layer.y[0],
    label="T_s Two Layer Ocean",
)

ax.plot(
    result_two_layer.t / (356 * 24 * 60 * 60),
    result_two_layer.y[1],
    label="T_d Two Layer Ocean",
)

ax.legend()
# %% 
