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

    return [dT_s, dT_d]