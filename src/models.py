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


def two_layer_ocean_and_carbon_cylce(t, y):
    T_s = y[0]
    T_d = y[1]
    C_a = y[2]
    C_l = y[3]
    C_s = y[4]
    C_d = y[5]

    dT_s = (
        -(lamb / c_s) * T_s
        + (beta / c_s) * np.log(C_a / C_a_zero + 1)
        - (eta_h / c_s) * (T_s - T_d)
        - (lamb_star / c_s) * (T_s - T_d)
    )

    dT_d = (eta_h / c_d) * (T_s - T_d)

    dC_l = pi_zero * (1 + beta_pi * np.log((C_a / C_a_zero) + 1)) - (
        (C_l + C_l_zero) / tau_1_zero
    ) * chi ** (T_s / 10)

    dC_s = gamma * ((C_a / k_a) - (C_s / k_o)) - eta_c * (
        (C_s / delta) - (C_d / (1 - delta))
    )

    dC_d = eta_c * ((C_s / delta) - (C_d / (1 - delta)))

    A = (
        A_tot
        * ((2.5 / year_to_seconds(50)) * np.exp((t_opt - t) / year_to_seconds(50)))
        / (1 + 2.5 * np.exp((t_opt - t) / year_to_seconds(50))) ** 2
    )

    dC_a = A - dC_l - dC_s - dC_d

    return [dT_s, dT_d, dC_a, dC_l, dC_s, dC_d]
