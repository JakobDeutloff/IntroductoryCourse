# %%
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# %% Define Parameters and initial condition
lam = 1e-6  # (1/s)
T_euler = [1]
T_analytical = [1]
T_ode = [1]
t_end = 5 * 1e6
timesteps = 20
dt = t_end / timesteps


# %% Define Function
def T_diff(t, y):
    return -lam * y


def T(t, y_0):
    return y_0 * np.exp(-lam * t)


def Forward_Euler(fun, y, t, dt):
    return y + fun(t, y) * dt


# %% Solve ODE
for i in np.arange(1, timesteps):
    # Forward Euler
    T_euler.append(Forward_Euler(T_diff, T_euler[i - 1], i * dt, dt))
    # Analytical
    T_analytical.append(T(i * dt, T_analytical[0]))

# %% Solve with RK45
T_scipy = solve_ivp(
    fun=T_diff,
    t_span=[0, dt * timesteps],
    y0=[T_analytical[0]],
    t_eval=np.arange(0, dt * timesteps, dt),
)

# %% Plot results
fig, ax = plt.subplots()
ax.plot(
    np.arange(0, dt * timesteps, dt), T_euler, label="Forward Euler", linestyle="-."
)
ax.plot(
    np.arange(0, dt * timesteps, dt), T_analytical, label="Analytical", inestyle="-"
)
ax.plot(T_scipy.t, T_scipy.y.squeeze(), label="RK45", linestyle="--")
ax.set_xlabel("time (s)")
ax.set_ylabel("T (K)")
ax.legend()


# %%
