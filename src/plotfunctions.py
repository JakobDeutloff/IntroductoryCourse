import matplotlib.pyplot as plt

def plot_all_outputs(result):

    fig, axes = plt.subplots(2, 4, figsize=(16, 10))
    axes[0, 0].plot(result["T_s (K)"])
    axes[0, 0].set_ylabel("T_s (K)")
    axes[0, 1].plot(result["C_l (GtC)"])
    axes[0, 1].set_ylabel("C_l (GtC)")
    axes[1, 0].plot(result["T_d (K)"])
    axes[1, 0].set_ylabel("T_d (K)")
    axes[1, 1].plot(result["C_a (GtC)"])
    axes[1, 1].set_ylabel("C_a (GtC)")
    axes[0, 2].plot(result["C_s (GtC)"])
    axes[0, 2].set_ylabel("C_s (GtC)")
    axes[1, 2].plot(result["C_d (GtC)"])
    axes[1, 2].set_ylabel("C_d (GtC)")
    axes[0, 3].plot(result["Emmissions (GtC)"])
    axes[0, 3].set_ylabel("Emmissions (GtC)")
    axes[1, 3].plot(result["C_m (GtC)"])
    axes[1, 3].set_ylabel("C_m (GtC)")

    return fig
