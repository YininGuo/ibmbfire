# ibmbfire

`ibmbfire` is a Python package based on the iBMB 2007 fire model. It generates fire temperature–time curves from compartment geometry and other parameters, and provides built‑in visualisation.

## Key Features

- Calculates key fire stages (t₁, t₂, t₃) and corresponding temperatures (T₁, T₂, T₃)
- Supports both ventilation‑controlled and fuel‑controlled scenarios
- Returns a piecewise temperature–time array
- Includes a simple plotting function for one‑line chart generation

## Installation

You can install straight from GitHub (requires [Git](https://git-scm.com/)):

```bash
pip install git+https://github.com/yourusername/ibmbfire.git
```
Or clone the repository and install locally:

```bash
git clone https://github.com/yourusername/ibmbfire.git
cd ibmbfire
pip install .
```

## Quick Start
```python
from ibmbfire import compute_ibmb_curve, plot_ibmb_curve

# Define compartment and fire parameters
Lc, Wc, Hc = 5.0, 4.0, 2.5      # compartment length, width, height (m)
Nw, Ww, hw    = 1, 1.5, 1.5    # number of openings, opening width & height (m)
T0, tg, q     = 20, 600, 500   # ambient temperature (°C), growth time (s), fire load density (MJ/m²)
b = 300.0                       # average thermal property (J/(m²·s⁰·⁵·K))

# Compute the temperature–time curve
t, T = compute_ibmb_curve(Lc, Wc, Hc, Nw, Ww, hw, T0, tg, q, b)

# Plot the curve
plot_ibmb_curve(t, T)
```

## Parameter Reference
| Parameter | Description              | Unit          |
| --------- | ------------------------ | ------------- |
| Lc        | compartment length       | m             |
| Wc        | compartment width        | m             |
| Hc        | compartment height       | m             |
| Nw        | number of openings       | —             |
| Ww        | opening width            | m             |
| hw        | opening height           | m             |
| T0        | ambient temperature      | °C            |
| tg        | fire growth time         | s             |
| q         | fire load density        | MJ/m²         |
| b         | average thermal property | J/(m²·s⁰·⁵·K) |

## Testing
``` bash
pytest
```

## Contributing
Contributions are more than welcome. Please raise an issue or submit a pull request to improve the model or add features.
