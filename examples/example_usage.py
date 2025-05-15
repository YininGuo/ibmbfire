from ibmbfire import compute_ibmb_curve, plot_ibmb_curve

# example
Lc, Wc, Hc = 4.0, 4.0, 3
Nw, Ww, hw = 1, 3.2, 2.5
T0, tg, q = 20, 300, 511
b = 1500

# calculation
t, T = compute_ibmb_curve(Lc, Wc, Hc, Nw, Ww, hw, T0, tg, q, b)

# plot
plot_ibmb_curve(t, T)
