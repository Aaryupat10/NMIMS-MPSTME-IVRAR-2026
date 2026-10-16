# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
# Publication Figures Engine and Benchmark Dataset Generator
# Group: IVRAR Group 01
# Output: 300 DPI Publication-Grade Figures and CSV Dataset

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configure publication aesthetics
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 13

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fig_dir = os.path.join(base_dir, "docs", "figures")
telemetry_dir = os.path.join(base_dir, "telemetry")
os.makedirs(fig_dir, exist_ok=True)
os.makedirs(telemetry_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. Generate Benchmark Dataset (100 Trials)
# -------------------------------------------------------------
np.random.seed(42)
n_trials = 100
trial_ids = np.arange(1, n_trials + 1)
# Treatment classes: 1 = Untreated, 2 = Partial Treatment, 3 = Fully Optimized CEDIA-RP22
treatment_classes = np.random.choice([1, 2, 3], size=n_trials, p=[0.33, 0.33, 0.34])

rt60_mid_s = np.zeros(n_trials, dtype=float)
frame_rate_fps = np.zeros(n_trials, dtype=float)
gaze_angle_deg = np.zeros(n_trials, dtype=float)
rework_hours = np.zeros(n_trials, dtype=float)

for i in range(n_trials):
    t_class = treatment_classes[i]
    if t_class == 1:
        rt60_mid_s[i] = np.clip(np.random.normal(0.88, 0.05), 0.76, 1.02)
        frame_rate_fps[i] = np.random.normal(88.5, 2.1)
        gaze_angle_deg[i] = np.random.normal(16.8, 1.5)
        rework_hours[i] = np.random.normal(38.0, 4.2)
    elif t_class == 2:
        rt60_mid_s[i] = np.clip(np.random.normal(0.48, 0.03), 0.41, 0.56)
        frame_rate_fps[i] = np.random.normal(85.2, 1.8)
        gaze_angle_deg[i] = np.random.normal(13.2, 1.1)
        rework_hours[i] = np.random.normal(14.5, 2.8)
    else:
        rt60_mid_s[i] = np.clip(np.random.normal(0.28, 0.02), 0.23, 0.34)
        frame_rate_fps[i] = np.random.normal(84.5, 1.6)
        gaze_angle_deg[i] = np.random.normal(11.4, 0.8)
        rework_hours[i] = np.random.normal(2.1, 0.9)

header = "trial_id,treatment_class,rt60_mid_s,frame_rate_fps,gaze_angle_deg,rework_hours"
data_mat = np.column_stack([
    trial_ids,
    treatment_classes,
    np.round(rt60_mid_s, 3),
    np.round(frame_rate_fps, 1),
    np.round(gaze_angle_deg, 1),
    np.round(rework_hours, 1)
])

csv_path = os.path.join(telemetry_dir, "SIMULATED_acoustic_benchmark_data.csv")
np.savetxt(csv_path, data_mat, delimiter=",", header=header, comments="", fmt=["%d", "%d", "%.3f", "%.1f", "%.1f", "%.1f"])
print(f"[SUCCESS] Wrote benchmark dataset: {csv_path}")

# -------------------------------------------------------------
# 2. Figure 1: System Architecture Diagram
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

def draw_block(ax, x, y, w, h, title, subtitle, color):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", 
                                  ec="#2C3E50", fc=color, lw=1.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h*0.65, title, ha='center', va='center', fontweight='bold', color='#1A252F')
    ax.text(x + w/2, y + h*0.3, subtitle, ha='center', va='center', fontsize=8, color='#34495E')

draw_block(ax, 0.5, 3.8, 2.4, 1.4, "Unity OpenXR Scene", "Home Cinema (7.2x5.1x2.8m)\n7.1.4 Dolby Atmos Layout", "#D4E6F1")
draw_block(ax, 0.5, 1.0, 2.4, 1.4, "Acoustic Raycaster", "1000 Rays/Source\nSpecular Snell's Law Reflections", "#D5F5E3")

draw_block(ax, 3.8, 3.8, 2.4, 1.4, "Schroeder Integration", "Backward Impulse Summation\nT20, T30 & RT60 Extraction", "#FCF3CF")
draw_block(ax, 3.8, 1.0, 2.4, 1.4, "Sightline Checker", "SMPTE/THX Cone Tracing\nVertical Gaze Angle < 15 deg", "#E8DAEF")

draw_block(ax, 7.1, 2.4, 2.4, 1.6, "CEDIA-RP22 Interface", "Tolerance Verifier [0.2-0.5s]\nAV Integrator Rework Parity\nDimensionless Payback Model", "#FADBD8")

ax.annotate('', xy=(3.8, 4.5), xytext=(2.9, 4.5), arrowprops=dict(arrowstyle="->", lw=2, color="#2C3E50"))
ax.annotate('', xy=(3.8, 1.7), xytext=(2.9, 1.7), arrowprops=dict(arrowstyle="->", lw=2, color="#2C3E50"))
ax.annotate('', xy=(5.0, 2.4), xytext=(5.0, 3.8), arrowprops=dict(arrowstyle="<->", lw=2, color="#2C3E50"))
ax.annotate('', xy=(7.1, 3.2), xytext=(6.2, 4.5), arrowprops=dict(arrowstyle="->", lw=2, color="#2C3E50"))
ax.annotate('', xy=(7.1, 3.2), xytext=(6.2, 1.7), arrowprops=dict(arrowstyle="->", lw=2, color="#2C3E50"))

ax.set_title("Figure 1: Real-Time Acoustic Raycasting and CEDIA-RP22 Compliance Architecture", 
             fontsize=12, fontweight='bold', pad=15)
fig.tight_layout()
fig1_path = os.path.join(fig_dir, "figure1_system_architecture.png")
fig.savefig(fig1_path, dpi=300)
plt.close(fig)
print(f"[SUCCESS] Wrote Figure 1: {fig1_path}")

# -------------------------------------------------------------
# 3. Figure 2: Kinematic Telemetry and Decay Curve Telemetry
# -------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(11, 7.5), dpi=300)

t = np.linspace(0, 1.0, 500)
# Subplot 1: Schroeder Energy Decay Curves
decay_untreated = -60.0 * (t / 0.88)
decay_treated = -60.0 * (t / 0.28)
axes[0, 0].plot(t, decay_untreated, color="#E74C3C", lw=2.0, label="Untreated Room (RT60=0.88s)")
axes[0, 0].plot(t, decay_treated, color="#2ECC71", lw=2.0, label="CEDIA Optimized (RT60=0.28s)")
axes[0, 0].axhline(-5.0, color="#7F8C8D", linestyle=":", label="-5 dB / -25 dB Bounds")
axes[0, 0].axhline(-25.0, color="#7F8C8D", linestyle=":")
axes[0, 0].set_title("(a) Schroeder Backward Energy Decay Curves", fontweight='bold')
axes[0, 0].set_xlabel("Time (s)")
axes[0, 0].set_ylabel("Normalized Energy (dB)")
axes[0, 0].set_ylim(-65, 5)
axes[0, 0].grid(True, linestyle="--", alpha=0.6)
axes[0, 0].legend(loc="upper right", fontsize=8)

# Subplot 2: RT60 Frequency Response across Octaves
octaves = ["125", "250", "500", "1k", "2k", "4k"]
rt_untreated_oct = [1.12, 0.98, 0.89, 0.86, 0.82, 0.74]
rt_treated_oct = [0.38, 0.32, 0.29, 0.28, 0.27, 0.25]

axes[0, 1].plot(octaves, rt_untreated_oct, marker='o', color="#E74C3C", lw=2.0, label="Untreated Room")
axes[0, 1].plot(octaves, rt_treated_oct, marker='s', color="#2ECC71", lw=2.0, label="CEDIA Optimized")
axes[0, 1].axhspan(0.20, 0.50, color="#F39C12", alpha=0.15, label="CEDIA-RP22 Recommended (0.2-0.5s)")
axes[0, 1].set_title("(b) Octave-Band Reverberation Time", fontweight='bold')
axes[0, 1].set_xlabel("Octave Band Center Frequency (Hz)")
axes[0, 1].set_ylabel("RT60 (seconds)")
axes[0, 1].grid(True, linestyle="--", alpha=0.6)
axes[0, 1].legend(loc="upper right", fontsize=8)

# Subplot 3: Ray Count vs Calculation Latency
ray_counts = np.array([250, 500, 1000, 2000, 4000])
latencies_ms = np.array([2.4, 4.5, 8.2, 15.8, 31.2])
axes[1, 0].bar([str(r) for r in ray_counts], latencies_ms, color="#3498DB", alpha=0.85, width=0.55)
axes[1, 0].axhline(13.3, color="#E74C3C", linestyle="--", label="75 FPS Budget (13.3 ms)")
axes[1, 0].set_title("(c) Ray Count vs Compute Latency", fontweight='bold')
axes[1, 0].set_xlabel("Rays Emitted per Loudspeaker Source")
axes[1, 0].set_ylabel("Kernel Execution Time (ms)")
axes[1, 0].grid(True, linestyle="--", alpha=0.6, axis="y")
axes[1, 0].legend()

# Subplot 4: Viewer Sightline Elevation Angle
seating_dist = np.linspace(3.0, 7.0, 50)
screen_h = 2.0
screen_bottom = 0.8
eye_h = 1.15
gaze_angles = np.degrees(np.arctan((screen_bottom + screen_h * 0.5 - eye_h) / seating_dist))
axes[1, 1].plot(seating_dist, gaze_angles, color="#8E44AD", lw=2.2)
axes[1, 1].axhline(15.0, color="#E74C3C", linestyle=":", label="SMPTE Max Gaze (15 deg)")
axes[1, 1].scatter([4.8], [np.degrees(np.arctan((screen_bottom + screen_h * 0.5 - eye_h) / 4.8))], 
                   color="#27AE60", s=60, zorder=5, label="Optimal Seating (4.8 m, 11.4 deg)")
axes[1, 1].set_title("(d) Sightline Gaze Angle vs Seating Distance", fontweight='bold')
axes[1, 1].set_xlabel("Seating Distance from Screen (m)")
axes[1, 1].set_ylabel("Vertical Gaze Angle (degrees)")
axes[1, 1].grid(True, linestyle="--", alpha=0.6)
axes[1, 1].legend()

fig.suptitle("Figure 2: Acoustic Decay Curves, Octave Response, Compute Latency, and Sightlines", 
             fontsize=13, fontweight='bold', y=0.98)
fig.tight_layout()
fig2_path = os.path.join(fig_dir, "figure2_kinematic_telemetry.png")
fig.savefig(fig2_path, dpi=300)
plt.close(fig)
print(f"[SUCCESS] Wrote Figure 2: {fig2_path}")

# -------------------------------------------------------------
# 4. Figure 3: Comparative Performance and Integration Economics
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(13, 4.5), dpi=300)

# Subplot A: RT60 Boxplot by Treatment Class
classes = ["Untreated", "Partial", "CEDIA-RP22\nOptimized"]
rt60_data = [
    rt60_mid_s[treatment_classes == 1],
    rt60_mid_s[treatment_classes == 2],
    rt60_mid_s[treatment_classes == 3]
]
bp = axes[0].boxplot(rt60_data, tick_labels=classes, patch_artist=True)
colors = ["#FADBD8", "#FCF3CF", "#D5F5E3"]
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
axes[0].axhspan(0.20, 0.50, color="#F39C12", alpha=0.15, label="CEDIA Tolerance (0.2-0.5s)")
axes[0].set_title("(a) Mid-Frequency RT60 by Treatment", fontweight='bold')
axes[0].set_ylabel("RT60 (seconds)")
axes[0].grid(True, linestyle="--", alpha=0.6)
axes[0].legend(loc="upper right", fontsize=8)

# Subplot B: On-Site AV Integrator Rework Hours
rework_means = [38.0, 14.5, 2.1]
rework_stds = [4.2, 2.8, 0.9]
bars = axes[1].bar(classes, rework_means, yerr=rework_stds, capsize=5, 
                   color=["#E74C3C", "#F39C12", "#2ECC71"], alpha=0.85, width=0.55)
axes[1].set_title("(b) On-Site Contractor Rework Hours", fontweight='bold')
axes[1].set_ylabel("Rework Hours per Cinema Project")
for bar in bars:
    yval = bar.get_height()
    axes[1].text(bar.get_x() + bar.get_width()/2, yval + 1.2, f"{yval:.1f} h", ha='center', fontweight='bold')
axes[1].grid(True, linestyle="--", alpha=0.6, axis="y")

# Subplot C: Dimensionless Amortization Payback Horizon
kappa_vals = np.linspace(0.10, 0.40, 50)
k_capex = 0.35
payback_months = (k_capex / (1.0 - kappa_vals)) * 12.0
axes[2].plot(kappa_vals, payback_months, color="#2980B9", lw=2.2)
axes[2].scatter([0.18], [(0.35 / (1.0 - 0.18)) * 12.0], color="#C0392B", s=60, zorder=5, 
                label="Baseline VR Workflow (5.1 mo)")
axes[2].set_title("(c) Integrator Amortization Payback", fontweight='bold')
axes[2].set_xlabel("Operational Cost Parity (Kappa)")
axes[2].set_ylabel("Payback Horizon (months)")
axes[2].grid(True, linestyle="--", alpha=0.6)
axes[2].legend()

fig.suptitle("Figure 3: Acoustic Compliance, Rework Avoidance, and AV Business Amortization", 
             fontsize=12, fontweight='bold', y=1.02)
fig.tight_layout()
fig3_path = os.path.join(fig_dir, "figure3_comparative_performance.png")
fig.savefig(fig3_path, dpi=300)
plt.close(fig)
print(f"[SUCCESS] Wrote Figure 3: {fig3_path}")

print("All publication assets generated successfully for IVRAR Group 01.")
