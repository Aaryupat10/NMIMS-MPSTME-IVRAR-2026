# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Generate publication-grade figures (300 DPI) and empirical benchmark dataset for IVRAR Group 03.
Authorized Title: How can an interactive VR emergency evacuation simulator resolve egress bottlenecks
and communication latency for university hostel wardens and student floor marshals during fire drills?
"""

import os
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configure high-resolution matplotlib parameters
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 8.5

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(BASE_DIR, "docs", "figures")
TELEMETRY_DIR = os.path.join(BASE_DIR, "telemetry")
os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(TELEMETRY_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# Figure 1: System Architecture Diagram
# -------------------------------------------------------------------------
def generate_figure1():
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Title
    ax.text(50, 96, "Collaborative Multi-User VR Evacuation Simulation Architecture", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')
    ax.text(50, 92, "Integrating Helbing Social Force Crowd Dynamics, OpenXR HMDs, and Egress Bottleneck Telemetry", 
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#4A5568')

    # Layer 1: Hardware & XR Input Layer
    rect1 = patches.FancyBboxPatch((4, 66), 26, 22, boxstyle="round,pad=1", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(rect1)
    ax.text(17, 85, "XR Interaction Layer\n(OpenXR / Unity 2022.3)", ha='center', va='center', fontweight='bold', color='#2B6CB0', fontsize=9.5)
    ax.text(17, 76, "- Headset 6-DoF Tracking\n- Hand Controller Raycasts\n- Spatial Two-Way Radio Audio\n- Floor Marshal UI Compass", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 2: Crowd AI & Multi-Agent Physics
    rect2 = patches.FancyBboxPatch((37, 66), 26, 22, boxstyle="round,pad=1", ec="#C53030", fc="#FFF5F5", lw=1.5)
    ax.add_patch(rect2)
    ax.text(50, 85, "Crowd Dynamics Engine\n(Helbing Social Force)", ha='center', va='center', fontweight='bold', color='#C53030', fontsize=9.5)
    ax.text(50, 76, "- Repulsive Boundary Forces\n- Agent Interpersonal Friction\n- Desired Velocity Modulation\n- Visibility Attenuation (Smoke)", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 3: Network & Coordination State Engine
    rect3 = patches.FancyBboxPatch((70, 66), 26, 22, boxstyle="round,pad=1", ec="#276749", fc="#F0FFF4", lw=1.5)
    ax.add_patch(rect3)
    ax.text(83, 85, "Emergency Coordination Engine\n(Netcode for GameObjects)", ha='center', va='center', fontweight='bold', color='#276749', fontsize=9.5)
    ax.text(83, 76, "- Warden Command Dispatch\n- Floor Marshal Status Sync\n- Evacuation Zone Flags\n- Network Latency Compensation", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Connecting arrows downward
    ax.annotate("", xy=(17, 48), xytext=(17, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))
    ax.annotate("", xy=(50, 48), xytext=(50, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))
    ax.annotate("", xy=(83, 48), xytext=(83, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))

    # Middle Layer: Multi-Floor Hostel Environment & Stairwell Nodes
    rect_env = patches.FancyBboxPatch((10, 30), 80, 18, boxstyle="round,pad=1", ec="#4A5568", fc="#EDF2F7", lw=1.5)
    ax.add_patch(rect_env)
    ax.text(50, 43, "Multi-Floor University Hostel Egress Grid (NBC 2016 / NFPA 101 Compliant)", 
            ha='center', va='center', fontweight='bold', color='#1A202C', fontsize=10)
    ax.text(50, 36, "Corridors (1.8m Width) | Stairwell Discharge Portals (1.2m Width) | Smoke Occlusion Zones (Beer-Lambert)\nCritical Flow Capacity Threshold: 1.8 persons / sec / meter width", 
            ha='center', va='center', fontsize=8.5, color='#4A5568')

    # Connecting arrow to telemetry
    ax.annotate("", xy=(50, 18), xytext=(50, 30), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))

    # Bottom Layer: Telemetry & Evaluation Analysis
    rect_tel = patches.FancyBboxPatch((15, 3), 70, 15, boxstyle="round,pad=1", ec="#6B46C1", fc="#FAF5FF", lw=1.5)
    ax.add_patch(rect_tel)
    ax.text(50, 14, "90 Hz Real-Time Telemetry & Egress Analytics Pipeline", 
            ha='center', va='center', fontweight='bold', color='#6B46C1', fontsize=9.5)
    ax.text(50, 8, "Stairwell Flux Sensor | Bottleneck Duration Logger | Warden-Marshal Latency Tracker | NASA-TLX Workload Engine", 
            ha='center', va='center', fontsize=8.5, color='#4A5568')

    plt.tight_layout()
    fig1_path = os.path.join(FIGURES_DIR, "figure1_system_architecture.png")
    plt.savefig(fig1_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {fig1_path}")

# -------------------------------------------------------------------------
# Figure 2: Kinematic & Telemetry Graphs
# -------------------------------------------------------------------------
def generate_figure2():
    np.random.seed(42)
    fig, axs = plt.subplots(2, 2, figsize=(9.5, 7.5))

    # (a) Evacuation Clearance Time vs Occupant Density
    occupants = np.linspace(20, 140, 30)
    ect_ideal = occupants * 0.95
    ect_actual = occupants * 1.1 + 0.008 * (occupants**2) + np.random.normal(0, 3, 30)
    axs[0, 0].plot(occupants, ect_ideal, '--', color='#718096', label='Linear Free-Flow (Unconstrained)')
    axs[0, 0].plot(occupants, ect_actual, 'o-', color='#C53030', markersize=4, label='Measured Egress (Helbing Physics)')
    axs[0, 0].axvline(85, color='#E53E3E', linestyle=':', label='Bottleneck Onset Threshold (N=85)')
    axs[0, 0].set_title("(a) Evacuation Clearance Time vs Occupant Count")
    axs[0, 0].set_xlabel("Hostel Floor Occupant Count (Persons)")
    axs[0, 0].set_ylabel("Total Evacuation Clearance Time (s)")
    axs[0, 0].legend()
    axs[0, 0].grid(True, linestyle='--', alpha=0.5)

    # (b) Doorway Discharge Rate over Time vs NBC/NFPA 101 Threshold
    time_series = np.linspace(0, 180, 100)
    flow_rate = 2.4 * np.exp(-((time_series - 45)/25)**2) + 0.3 * np.random.normal(0, 0.15, 100)
    flow_rate = np.clip(flow_rate, 0, 3.2)
    axs[0, 1].plot(time_series, flow_rate, color='#2B6CB0', lw=1.8, label='Simulated Stairwell Door Flux')
    axs[0, 1].axhline(1.8, color='#D69E2E', linestyle='--', lw=1.6, label='NBC/NFPA 101 Standard Max (1.8 p/s/m)')
    axs[0, 1].axhline(1.33, color='#E53E3E', linestyle=':', lw=1.4, label='Arching Jam Flow Deficit (1.33 p/s/m)')
    axs[0, 1].set_title("(b) Stairwell Doorway Discharge Rate Profile")
    axs[0, 1].set_xlabel("Time Post-Alarm (s)")
    axs[0, 1].set_ylabel("Discharge Flow Rate (persons / s / m width)")
    axs[0, 1].legend()
    axs[0, 1].grid(True, linestyle='--', alpha=0.5)

    # (c) Pre-Evacuation Response Delay Across Hostel Floors
    floors = ['Ground', 'Floor 1', 'Floor 2', 'Floor 3', 'Floor 4']
    mean_delay = [14.2, 22.5, 31.8, 42.1, 53.6]
    err = [2.1, 3.2, 4.0, 5.1, 6.2]
    axs[1, 0].bar(floors, mean_delay, yerr=err, capsize=4, color='#4FD1C5', edgecolor='#234E52', alpha=0.85)
    axs[1, 0].set_title("(c) Pre-Evacuation Alarm Response Delay by Floor")
    axs[1, 0].set_xlabel("Hostel Vertical Location")
    axs[1, 0].set_ylabel("Pre-Movement Delay (T_pre, seconds)")
    axs[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

    # (d) Warden-to-Marshal Dispatch Communication Latency
    trials = np.arange(1, 16)
    latency_traditional = [48.2, 45.1, 46.8, 43.5, 41.2, 44.0, 39.8, 42.1, 40.5, 38.9, 39.5, 37.2, 38.0, 36.5, 37.1]
    latency_vr = [42.1, 31.5, 24.2, 19.8, 16.5, 14.2, 12.8, 11.5, 10.2, 9.8, 9.2, 8.7, 8.5, 8.2, 8.1]
    axs[1, 1].plot(trials, latency_traditional, 's--', color='#718096', label='Traditional Radio Relay')
    axs[1, 1].plot(trials, latency_vr, 'o-', color='#3182CE', lw=2, label='VR Spatial Dispatch Protocol')
    axs[1, 1].set_title("(d) Inter-Warden Dispatch Latency Across Training Trials")
    axs[1, 1].set_xlabel("Practice Trial Number")
    axs[1, 1].set_ylabel("Mean Command Latency (s)")
    axs[1, 1].legend()
    axs[1, 1].grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    fig2_path = os.path.join(FIGURES_DIR, "figure2_kinematic_telemetry.png")
    plt.savefig(fig2_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {fig2_path}")

# -------------------------------------------------------------------------
# Figure 3: Comparative Performance Across Training Modalities
# -------------------------------------------------------------------------
def generate_figure3():
    fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.8))

    modalities = ['Uncoordinated\nBaseline', 'Standard Physical\nFire Drill', 'Collaborative VR\nSimulation']
    colors = ['#E53E3E', '#ED8936', '#38A169']

    # (a) Evacuation Clearance Time (s)
    ect_means = [242.6, 198.4, 138.2]
    ect_stds = [18.5, 14.2, 9.6]
    bars_a = axs[0].bar(modalities, ect_means, yerr=ect_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[0].set_title("(a) Mean Evacuation Clearance Time (s)")
    axs[0].set_ylabel("Total Clearance Time (s)")
    axs[0].set_ylim(0, 300)
    axs[0].grid(axis='y', linestyle='--', alpha=0.5)
    axs[0].text(2, 155, "-43.0%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    # (b) Stairwell Bottleneck Jam Duration (s)
    jam_means = [84.5, 62.1, 21.4]
    jam_stds = [11.2, 8.9, 4.3]
    bars_b = axs[1].bar(modalities, jam_means, yerr=jam_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[1].set_title("(b) Stairwell Bottleneck Jam Duration (s)")
    axs[1].set_ylabel("Stairwell Jam Duration (s)")
    axs[1].set_ylim(0, 110)
    axs[1].grid(axis='y', linestyle='--', alpha=0.5)
    axs[1].text(2, 32, "-74.7%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    # (c) NASA-TLX Cognitive Workload Profile
    tlx_means = [76.4, 61.2, 38.5]
    tlx_stds = [5.8, 4.9, 3.7]
    bars_c = axs[2].bar(modalities, tlx_means, yerr=tlx_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[2].set_title("(c) NASA-TLX Subjective Workload")
    axs[2].set_ylabel("Workload Score (0-100)")
    axs[2].set_ylim(0, 100)
    axs[2].grid(axis='y', linestyle='--', alpha=0.5)
    axs[2].text(2, 48, "-49.6%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    plt.tight_layout()
    fig3_path = os.path.join(FIGURES_DIR, "figure3_comparative_performance.png")
    plt.savefig(fig3_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {fig3_path}")

# -------------------------------------------------------------------------
# Benchmark Dataset Generation (N = 50 trials)
# -------------------------------------------------------------------------
def generate_benchmark_dataset():
    np.random.seed(103)
    n_samples = 50

    fieldnames = [
        "trial_id",
        "occupant_count",
        "training_modality",
        "pre_evacuation_delay_s",
        "mean_stairwell_flow_rate_ppm",
        "stairwell_jam_duration_s",
        "warden_dispatch_latency_s",
        "total_evacuation_time_s",
        "egress_bottleneck_occurred",
        "route_deviation_rate_pct",
        "nasa_tlx_workload_score",
        "coordination_success_rate_pct"
    ]

    csv_path = os.path.join(TELEMETRY_DIR, "SIMULATED_evacuation_training_benchmark.csv")

    rows = []
    for i in range(n_samples):
        trial_id = f"EVAC-TR-{i+1:03d}"
        occ = int(np.random.randint(60, 150))
        r_val = np.random.rand()
        if r_val < 0.25:
            mod = "Uncoordinated_Baseline"
            p_delay = np.random.normal(38.0, 5.2)
            flow = np.random.normal(1.28, 0.12)
            jam = np.random.normal(82.0, 10.5)
            w_lat = np.random.normal(46.0, 6.2)
            tt = p_delay + (occ * 1.5) + jam * 0.5 + np.random.normal(0, 5.0)
            bn = 1 if jam > 60 else 0
            dev = np.random.normal(24.5, 4.2)
            tlx = np.random.normal(75.5, 4.8)
            coord = np.random.normal(42.0, 6.5)
        elif r_val < 0.60:
            mod = "Standard_Physical_Drill"
            p_delay = np.random.normal(26.0, 4.1)
            flow = np.random.normal(1.52, 0.14)
            jam = np.random.normal(58.0, 8.4)
            w_lat = np.random.normal(32.0, 4.5)
            tt = p_delay + (occ * 1.25) + jam * 0.4 + np.random.normal(0, 4.0)
            bn = 1 if jam > 50 else 0
            dev = np.random.normal(15.2, 3.1)
            tlx = np.random.normal(61.0, 4.2)
            coord = np.random.normal(68.0, 5.2)
        else:
            mod = "Collaborative_VR_Sim"
            p_delay = np.random.normal(14.0, 2.5)
            flow = np.random.normal(1.82, 0.10)
            jam = np.random.normal(19.5, 4.2)
            w_lat = np.random.normal(9.5, 1.8)
            tt = p_delay + (occ * 0.92) + jam * 0.25 + np.random.normal(0, 3.0)
            bn = 1 if jam > 35 else 0
            dev = np.random.normal(4.8, 1.5)
            tlx = np.random.normal(38.2, 3.4)
            coord = np.random.normal(94.5, 3.1)

        row = {
            "trial_id": trial_id,
            "occupant_count": occ,
            "training_modality": mod,
            "pre_evacuation_delay_s": round(float(max(5.0, p_delay)), 2),
            "mean_stairwell_flow_rate_ppm": round(float(max(0.5, flow)), 2),
            "stairwell_jam_duration_s": round(float(max(0.0, jam)), 2),
            "warden_dispatch_latency_s": round(float(max(3.0, w_lat)), 2),
            "total_evacuation_time_s": round(float(max(30.0, tt)), 2),
            "egress_bottleneck_occurred": int(bn),
            "route_deviation_rate_pct": round(float(max(0.0, dev)), 2),
            "nasa_tlx_workload_score": round(float(min(100.0, max(0.0, tlx))), 2),
            "coordination_success_rate_pct": round(float(min(100.0, max(0.0, coord))), 2)
        }
        rows.append(row)

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[OK] Generated benchmark dataset (N=50): {csv_path}")

if __name__ == "__main__":
    generate_figure1()
    generate_figure2()
    generate_figure3()
    generate_benchmark_dataset()
    print("[SUCCESS] All figures and benchmark telemetry generated for IVRAR Group 03.")
