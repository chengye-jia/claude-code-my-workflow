"""
Polynomial OLS misspecification (Zhou Example 1.2):
True regression: g(x) = x + 2*exp(-sin(x))
Researcher fits Models 1, 2, 3 (linear, quadratic, cubic).
Demonstrates the periodic oscillation that no finite polynomial can capture.
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Simulate data
n = 200
x = np.sort(np.random.uniform(-3, 3, n))
g = x + 2 * np.exp(-np.sin(x))
u = np.random.normal(0, 0.5, n)
y = g + u

# Fit polynomials
x_dense = np.linspace(-3.2, 3.2, 400)
g_true = x_dense + 2 * np.exp(-np.sin(x_dense))

# Linear, Quadratic, Cubic OLS
fits = {}
for deg, name in [(1, "Model 1 (linear)"), (2, "Model 2 (quadratic)"),
                   (3, "Model 3 (cubic)")]:
    coefs = np.polyfit(x, y, deg)
    fits[name] = np.polyval(coefs, x_dense)

# Nadaraya-Watson kernel regression for contrast
def nw_estimate(x_eval, x_data, y_data, h):
    out = np.zeros_like(x_eval)
    for i, xe in enumerate(x_eval):
        u = (x_data - xe) / h
        K = np.exp(-0.5 * u**2) / np.sqrt(2 * np.pi)
        out[i] = np.sum(K * y_data) / np.sum(K)
    return out

h_silv = 1.06 * np.std(x) * n ** (-1/5)
g_nw = nw_estimate(x_dense, x, y, h_silv)

# Plot
SUFE_BLUE = "#0F4C81"
SUFE_GOLD = "#B9975B"
GREY = "#666666"

fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), sharey=True)

# Left panel: polynomial fits
ax = axes[0]
ax.scatter(x, y, color=GREY, s=12, alpha=0.5, label="data")
ax.plot(x_dense, g_true, color="black", linewidth=2.4,
        label=r"true $g(x) = x + 2e^{-\sin x}$")
colors = ["#C0392B", "#F39C12", "#27AE60"]
linestyles = ["--", "-.", ":"]
for (name, fit_curve), c, ls in zip(fits.items(), colors, linestyles):
    ax.plot(x_dense, fit_curve, color=c, linewidth=1.8,
            linestyle=ls, label=name)
ax.set_xlabel(r"$x$", fontsize=12)
ax.set_ylabel(r"$y$", fontsize=12)
ax.set_title("Polynomial OLS: cannot capture oscillation", fontsize=12,
             fontweight="bold")
ax.legend(loc="upper left", fontsize=9, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.set_xlim(-3.2, 3.2)

# Right panel: NW kernel fit succeeds
ax = axes[1]
ax.scatter(x, y, color=GREY, s=12, alpha=0.5, label="data")
ax.plot(x_dense, g_true, color="black", linewidth=2.4,
        label=r"true $g(x)$")
ax.plot(x_dense, g_nw, color=SUFE_BLUE, linewidth=2.0,
        label=fr"NW kernel $\hat g(x)$, $h={h_silv:.2f}$")
ax.set_xlabel(r"$x$", fontsize=12)
ax.set_title("Nonparametric NW: tracks $g$ without functional form",
             fontsize=12, fontweight="bold")
ax.legend(loc="upper left", fontsize=9, framealpha=0.95)
ax.grid(True, alpha=0.25)
ax.set_xlim(-3.2, 3.2)

fig.suptitle(
    r"Zhou Example 1.2: parametric misspecification vs. nonparametric flexibility",
    fontsize=13, y=1.00)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("polynomial_misspec.pdf", bbox_inches="tight")
plt.savefig("polynomial_misspec.png", dpi=170, bbox_inches="tight")
print(f"Saved: polynomial_misspec.pdf and .png")
print(f"NW bandwidth (Silverman): h = {h_silv:.4f}")
