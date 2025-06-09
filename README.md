# Pressure__Depth
This repository contains Python code for plotting the relationships between pressure-depth and temperature-depth, based on subsurface data.

The input data should be in CSV format, with the following columns:

- `DEPTH_m`: depth of the subsurface measurement (meters)
- `DHAP_psi`: pressure at that depth (psi)
- `DHAT_degC`: temperature at that depth (°C)

## Usage

To visualize the pressure versus depth relationship with an improved graph run:

```bash
python pressure_depth_graph.py
```

The script reads `depthvtemperature.csv`, fits a linear trend line and displays the scatter plot with the fitted line.
If any measurement has a pressure greater than **2100 psi**, an alert is printed and written to `alerts.txt`.
