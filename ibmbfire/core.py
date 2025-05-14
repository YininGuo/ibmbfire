import numpy as np
import matplotlib.pyplot as plt
import math

def compute_ibmb_curve(Lc, Wc, Hc, Nw, Ww, hw, T0, tg, q, b):
    """
    Temperature-time curve according to iBMB fire model

    Parameters:
        Lc, Wc, Hc: compartment geometry(m)
        Nw: number of opennings
        Ww, hw: width and height of openning (m)
        T0: environment termperature (°C)
        tg: time of fire growth (s)
        q: fuel load density (MJ/m^2)
        b: average thermal property J/(m^2·s^0.5·K)

    Return:
        t: time list (min)
        T: temperature list (°C)
    """
    # geometry
    Af = Lc * Wc
    At = 2 * (Af + Lc * Hc + Wc * Hc)
    Aw = hw * Ww * Nw
    AT = At - Aw
    O = Aw * math.sqrt(hw) / At

    # fire type
    HRRf = 0.25
    V_constant = 1.21
    Qv = V_constant * Aw * math.sqrt(hw)
    Qf = HRRf * Af
    if Qv < Qf:
        Qmax = Qv
        fire_mode = 'ventilation_controlled'
    else:
        Qmax = Qf
        fire_mode = 'fuel_controlled'

    # representative time t1, t2, t3
    Q_total_std = Af * 1300.0
    t1 = math.sqrt(tg**2 * Qmax)
    Q1 = t1**3 / (3 * tg**2)
    Q2 = 0.7 * Q_total_std - Q1
    Q3 = 0.3 * Q_total_std
    dt2 = Q2 / Qmax
    dt3 = 2 * Q3 / Qmax
    t2 = t1 + dt2
    t3 = t2 + dt3

    # k
    k = (Qmax**2 / (Aw * math.sqrt(hw) * AT * b))**(1/3)
    # T1, T2, T3
    if fire_mode == 'fuel_controlled':
        T1 = 24000 * k + 20 if k <= 0.04 else 980
        T2 = 33000 * k + 20 if k <= 0.04 else 1340
        T3 = 16000 * k + 20 if k <= 0.04 else 660
    else:
        T1 = -8.75 / O - 0.1 * b + 1175
        T2 = min((0.004 * b - 17) / O - 0.4 * b + 2175, 1340)
        T3 = -5 / O - 0.16 * b + 1060

    # representative time for real fire load scenario
    Qx = Af * q
    t1x = t1
    Q1x = t1x**3 / (3 * tg**2)
    Q2x = 0.7 * Qx - Q1x
    Q3x = 0.3 * Qx
    dt2x = Q2x / Qmax
    dt3x = 2 * Q3x / Qmax
    t2x = t1x + dt2x
    t3x = t2x + dt3x
    # unit convention
    t1m, t2m, t3m = t1/60, t2/60, t3/60
    t1xm, t2xm, t3xm = t1x/60, t2x/60, t3x/60

    # Temperature
    tf1 = np.arange(0, t1xm+0.1, 0.1)
    T_sec1 = lambda x: (T1 - T0) * x**2 / (t1xm**2) + T0
    Tt1 = T_sec1(tf1)

    tf2 = np.arange(t1xm, t2xm+0.1, 0.1)
    T_sec2 = lambda x: (T2 - T1) * np.sqrt((x - t1m)/(t2m - t1m)) + T1
    Tt2 = T_sec2(tf2)

    tf3 = np.arange(t2xm, t3xm+0.1, 0.1)
    T_sec3 = lambda x: (T3 - T2) * np.sqrt((x - t2xm)/(t3xm - t2xm)) + T2
    Tt3 = T_sec3(tf3)

    # 合并
    t = np.concatenate([tf1, tf2, tf3])
    T = np.concatenate([Tt1, Tt2, Tt3])

    return t, T


def plot_ibmb_curve(t, T, show=True, save_path=None):
    """
    Diagram plotting
    """
    plt.figure()
    plt.plot(t, T)
    plt.xlabel('Time (min)')
    plt.ylabel('Temperature (°C)')
    plt.title('IBMB Fire Temperature-Time Curve')
    plt.grid(True)
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()