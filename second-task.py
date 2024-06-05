import numpy as np
import scipy.integrate as spi
import pandas as pd
import matplotlib.pyplot as plt


def f(x):
    return x**2


a = 0
b = 2

n_points = 100000

x_random = np.random.uniform(a, b, n_points)
y_random = f(x_random)

integral_monte_carlo = (b - a) * np.mean(y_random)

integral_quad, error = spi.quad(f, a, b)

results = pd.DataFrame(
    {
        "Method": ["Monte Carlo", "Quad"],
        "Integral": [integral_monte_carlo, integral_quad],
        "Error": [np.nan, error],
    }
)

print(results)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, "r", linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()
