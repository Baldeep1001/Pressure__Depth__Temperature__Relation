import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_alerts(df, threshold=2100, output_file="alerts.txt"):
    """Write an alert file if any pressure value exceeds the threshold."""
    high_pressure = df[df["DHAP_psi"] > threshold]
    if not high_pressure.empty:
        msg = (
            f"ALERT: {len(high_pressure)} measurements exceed {threshold} psi."
        )
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(msg + "\n")
        print(msg)


def plot_pressure_depth(csv_file="depthvtemperature.csv"):
    """Read depth-pressure data and plot an enhanced graph."""
    df = pd.read_csv(csv_file, delim_whitespace=True)
    generate_alerts(df)
    x = df["DEPTH_m"].values
    y = df["DHAP_psi"].values

    # Fit a linear trend line using numpy
    coeffs = np.polyfit(x, y, 1)
    slope, intercept = coeffs

    x_line = np.linspace(x.min(), x.max(), 200)
    y_line = slope * x_line + intercept

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, s=10, color="tab:blue", label="Measurements", alpha=0.6)
    plt.plot(x_line, y_line, color="tab:red", label=f"Fit: y = {slope:.2f}x + {intercept:.2f}")

    plt.title("Pressure vs Depth")
    plt.xlabel("Depth (m)")
    plt.ylabel("Pressure (psi)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_pressure_depth()
