#%%
from src.helper_functions import seconds_to_year, year_to_seconds, co2tocarbon
import numpy as np

# Ocean ---------------------------------------------------------
lamb = 1.75  # (W/m^2 K)
lamb_star = 0.75  # (W/m^2 K)
beta = 5.77  # (W/m^2)
ratio = 2  # doubling of CO2
c = 4000  # (J/kg K)
rho = 1026  # ocean density (kg/m^3)
D = 2620  # Equivalent ocean depth (m)
years = 500  # Years after which equilibrium should be reached
delta = 0.015  # ratio of surface to deep ocean depth
D_s = D * delta  # surface ocean depth (m)
D_d = D * (1 - delta)  # deep ocean depth (m)
c_s = D_s * c * rho  # heat capacity of surface ocean (J/K)
c_d = D_d * c * rho  # heat capacity of deep ocean (J/K)
eta_h = c_d / (year_to_seconds(years))  # mixing parameter (J/K/second)

# Carbon Cylce --------------------------------------------------
k_a = 2.12  # Atmospheric carbon intensity factor (GtC/ppm)
beta_pi = 0.4  # Ocean fertilization factor (unitless)
gamma = 0.005 / year_to_seconds(1)  # Air sea gas exchange coefficient (GtC / second / ppm)
zeta = 10.5  # Revelle factor (unitless)
pi_zero = 60 / year_to_seconds(1)  # pre-industrial NPP (GtC/second)
f = 1 / 7
C_o_zero = 37e3  # pre-industrial oceanic carbon (GtC)
C_l_zero = 2500  # pre-industrial land carbon (GtC)
C_a_zero = C_o_zero / (zeta * ((1 - f) / f))  # per-industrial atmospheric carbon (GtC)
C_d_zero = C_o_zero * ((delta / (1 - delta)) + 1)**(-1) # pre-industrial deep ocean carbon (GtC)
C_s_zero =  C_o_zero - C_d_zero # pre-industrial surface ocean carbon (GtC)
k_o = (k_a / zeta) * (C_s_zero / C_a_zero) # ocean carbon intensity factor (GtC/ppm)
tau_1_zero = 41 * year_to_seconds(1)  # (seconds)
chi = 1.8 # (unitless)
t_opt = 250 * year_to_seconds(1)  # (seconds)
A_tot = 2.5e3 # SSP585: 5e3  # (GtC)
my_zero = 5 / year_to_seconds(1)  # (m/second)
eta_c = my_zero / D # Surface-deep ocean carbon exchange coefficient (1/second)

# %% Emission rates 
rate = 37.5  # Emissions in GtCO2/year
initial_emissions = np.round(co2tocarbon(rate))/year_to_seconds(1)  # Emissions in GtC/second

# %% Land management
C_a_ideal = 1000  # Ideal atmospheric carbon (GtC)
tau_reaction = year_to_seconds(10)  # timescale of land management (seconds) 
tau_biomass = year_to_seconds(200)  # Biomass lifetime (seconds) 
T_goal = 2  # Target temperature (K)
T_to_C = 500  # Conversion factor from temperature to carbon (GtC/K)
