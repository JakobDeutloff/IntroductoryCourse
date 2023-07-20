from src.parameters import *
import numpy as np


def single_layer_ocean(t, y):
    return -(lamb / c_s) * y + (beta / c_s) * np.log(ratio)


def two_layer_ocean(t, y):
    dT_s = (
        -(lamb / c_s) * y[0]
        + (beta / c_s) * np.log(ratio)
        - (eta_h / c_s) * (y[0] - y[1])
        - (lamb_star / c_s) * (y[0] - y[1])
    )

    dT_d = (eta_h / c_d) * (y[0] - y[1])

    imbalance_TOA = -(lamb / c_s) * y[0] + (beta / c_s) * np.log(ratio)

    return [dT_s, dT_d, imbalance_TOA]


def two_layer_ocean_and_carbon_cylce(t, y, t_reverse=None, rate=None, lm=False):
    T_s = y[0]
    T_d = y[1]
    C_a = y[2]
    C_l = y[3]
    C_s = y[4]
    C_d = y[5]
    Cum_E = y[6]


    dT_s = (
        -(lamb / c_s) * T_s
        + (beta / c_s) * np.log(C_a / C_a_zero + 1)
        - (eta_h / c_s) * (T_s - T_d)
        - (lamb_star / c_s) * (T_s - T_d)
    )

    dT_d = (eta_h / c_d) * (T_s - T_d)

    # Land management
    if lm:
        if C_a > C_a_ideal:
            dC_m = land_management(C_a)
        else:
            dC_m = 0
    else:
        dC_m = 0

    dC_l = pi_zero * (1 + beta_pi * np.log((C_a / C_a_zero) + 1)) - (
        (C_l + C_l_zero) / tau_1_zero
    ) * chi ** (T_s / 10) + dC_m

    dC_s = gamma * ((C_a / k_a) - (C_s / k_o)) - eta_c * (
         (C_s / delta) - (C_d / (1 - delta))
    )

    dC_d = eta_c * ((C_s / delta) - (C_d / (1 - delta)))

    # Calculate emissions
    if t_reverse is None:
        A = (
            A_tot
            * ((2.5 / year_to_seconds(50)) * np.exp((t_opt - t) / year_to_seconds(50)))
            / (1 + 2.5 * np.exp((t_opt - t) / year_to_seconds(50))) ** 2
    )
    elif t < t_reverse:
        A = rate
    elif (t >= t_reverse) & (Cum_E > 0):
        A = -rate
    else:
        A = 0

    dC_a = A - dC_l - dC_s - dC_d

    if lm:
        return [dT_s, dT_d, dC_a, dC_l, dC_s, dC_d, A, dC_m]
    else:
        return [dT_s, dT_d, dC_a, dC_l, dC_s, dC_d, A]


def land_management(T_s):
    dC_m = ((T_s - T_goal) * T_to_C) / tau_reaction
    return dC_m

def model_with_landmanagement(t, y, enable_land_management=False):
    T_s = y[0]
    T_d = y[1]
    C_a = y[2]
    C_l = y[3]
    C_s = y[4]
    C_d = y[5]
    C_m = y[7]


    dT_s = (
        -(lamb / c_s) * T_s
        + (beta / c_s) * np.log(C_a / C_a_zero + 1)
        - (eta_h / c_s) * (T_s - T_d)
        - (lamb_star / c_s) * (T_s - T_d)
    )

    dT_d = (eta_h / c_d) * (T_s - T_d)

    # Land management
    if enable_land_management:
        if T_s > T_goal:
            dC_m = land_management(T_s) - (C_m/tau_biomass) * chi ** (T_s / 10)
        else:
            dC_m = - (C_m/tau_biomass) * chi ** (T_s / 10)
    else:
        dC_m = 0



    dC_l = pi_zero * (1 + beta_pi * np.log((C_a / C_a_zero) + 1)) - (
        (C_l + C_l_zero) / tau_1_zero
    ) * chi ** (T_s / 10) 

    dC_s = gamma * ((C_a / k_a) - (C_s / k_o)) - eta_c * (
         (C_s / delta) - (C_d / (1 - delta))
    )

    dC_d = eta_c * ((C_s / delta) - (C_d / (1 - delta)))

    # Calculate emissions

    A = (
        A_tot
        * ((2.5 / year_to_seconds(50)) * np.exp((t_opt - t) / year_to_seconds(50)))
        / (1 + 2.5 * np.exp((t_opt - t) / year_to_seconds(50))) ** 2
    )

    dC_a = A - dC_l - dC_s - dC_d - dC_m


    return [dT_s, dT_d, dC_a, dC_l, dC_s, dC_d, A, dC_m]
