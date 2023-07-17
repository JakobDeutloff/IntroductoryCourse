# %% Define Parameters and initial condition
lamb = 1.75  # W/m^2 K
lamb_star = 0.75  # W/m^2 K
beta = 5.77  # W/m2
ratio = 2  # doubling of CO2
c = 4000  # J/kg K
rho = 1026  # ocean density (kg/m^3)
D_s = 40  # surface ocean depth (m)
D_d = 2580  # deep ocean depth (m)
years = 100  # Years after which equilibrium should be reached

# %% Calculate heat capacity of upper and lower ocean
c_s = D_s * c * rho  # J/K
c_d = D_d * c * rho  # J/K

# %% Calculate eta
eta_h = c_d / (years * 356 * 24 * 60 * 60)