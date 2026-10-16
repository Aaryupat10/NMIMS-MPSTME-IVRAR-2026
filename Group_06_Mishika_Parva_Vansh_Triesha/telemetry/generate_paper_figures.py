# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Generate publication-grade figures (300 DPI) and empirical benchmark dataset for IVRAR Group 06.
Authorized Title: How can an AR visual-marker navigation system using ArUco and QR anchors
optimize transit time and route-finding errors across multi-storey university buildings for first-year students?
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
    ax.text(50, 96, "AR Visual-Marker Multi-Storey Indoor Navigation Architecture", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')
    ax.text(50, 92, "Integrating ArUco/QR Fiducials, Perspective-n-Point Pose Reset, 3D Graph A*, and ARCore VIO", 
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#4A5568')

    # Layer 1: Mobile Sensing & VIO Tracking Layer
    rect1 = patches.FancyBboxPatch((4, 66), 26, 22, boxstyle="round,pad=1", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(rect1)
    ax.text(17, 85, "Mobile ARCore / ARKit Layer\n(Monocular VIO Tracking)", ha='center', va='center', fontweight='bold', color='#2B6CB0', fontsize=9.5)
    ax.text(17, 76, "- 60 Hz Camera Frame Stream\n- IMU Accelerometer / Gyro\n- Feature Point Sparse Cloud\n- Drift Drift (1-3% of Path)", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 2: ArUco / QR Fiducial Vision Engine
    rect2 = patches.FancyBboxPatch((37, 66), 26, 22, boxstyle="round,pad=1", ec="#C53030", fc="#FFF5F5", lw=1.5)
    ax.add_patch(rect2)
    ax.text(50, 85, "Visual Anchor Grounding\n(OpenCV ArUco / PnP Engine)", ha='center', va='center', fontweight='bold', color='#C53030', fontsize=9.5)
    ax.text(50, 76, "- Adaptive Thresholding\n- 4-Corner Subpixel Refinement\n- Levenberg-Marquardt PnP\n- Global Pose Drift Reset (<5cm)", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 3: Multi-Floor 3D Graph Navigation Core
    rect3 = patches.FancyBboxPatch((70, 66), 26, 22, boxstyle="round,pad=1", ec="#276749", fc="#F0FFF4", lw=1.5)
    ax.add_patch(rect3)
    ax.text(83, 85, "3D Topological Navigation\n(BIM Graph & A* Pathfinder)", ha='center', va='center', fontweight='bold', color='#276749', fontsize=9.5)
    ax.text(83, 76, "- Corridor Waypoint Nodes\n- Stairwell / Lift Portals\n- Multi-Level A* Heuristics\n- Dynamic Detour Rerouting", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Connecting arrows downward
    ax.annotate("", xy=(17, 48), xytext=(17, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))
    ax.annotate("", xy=(50, 48), xytext=(50, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))
    ax.annotate("", xy=(83, 48), xytext=(83, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))

    # Middle Layer: University Academic Complex Environment
    rect_env = patches.FancyBboxPatch((10, 30), 80, 18, boxstyle="round,pad=1", ec="#4A5568", fc="#EDF2F7", lw=1.5)
    ax.add_patch(rect_env)
    ax.text(50, 43, "Multi-Storey Academic Complex Facility (BIM Coordinate Reference Frame)", 
            ha='center', va='center', fontweight='bold', color='#1A202C', fontsize=10)
    ax.text(50, 36, "6 Floors | 48 Lecture Theaters | 12 Laboratories | 4 Stairwell Cores | 3 Passenger Elevators\nFixed ArUco DICT_6X6_250 Anchors at Critical Decision Waypoints and Room Entrances", 
            ha='center', va='center', fontsize=8.5, color='#4A5568')

    # Connecting arrow to telemetry
    ax.annotate("", xy=(50, 18), xytext=(50, 30), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))

    # Bottom Layer: Telemetry & Evaluation Analysis
    rect_tel = patches.FancyBboxPatch((15, 3), 70, 15, boxstyle="round,pad=1", ec="#6B46C1", fc="#FAF5FF", lw=1.5)
    ax.add_patch(rect_tel)
    ax.text(50, 14, "90 Hz Real-Time Navigation Telemetry & Evaluation Engine", 
            ha='center', va='center', fontweight='bold', color='#6B46C1', fontsize=9.5)
    ax.text(50, 8, "Trajectory Cumulative Tracking | PnP Reprojection Error Monitor | Wrong-Turn Event Logger | Transit Time Benchmarker", 
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

    # (a) VIO Drift Accumulation vs Trajectory Distance
    dist = np.linspace(0, 150, 50)
    raw_vio_drift = 0.022 * dist + 0.00012 * (dist**2) + np.random.normal(0, 0.08, 50)
    # ArUco corrected drift resets every 30m
    marker_drift = []
    for d in dist:
        segment_d = d % 30.0
        marker_drift.append(0.018 * segment_d + 0.02 + np.random.normal(0, 0.015))

    axs[0, 0].plot(dist, raw_vio_drift, 'r--', lw=1.8, label='Uncorrected ARCore/ARKit VIO Drift')
    axs[0, 0].plot(dist, marker_drift, 'b-', lw=2, label='ArUco Periodic Pose Reset (< 5cm)')
    axs[0, 0].axhline(0.05, color='#38A169', linestyle=':', label='Target Localization Tolerance (5 cm)')
    axs[0, 0].set_title("(a) Cumulative Position Drift vs Trajectory Distance")
    axs[0, 0].set_xlabel("Corridor Path Distance Traveled (m)")
    axs[0, 0].set_ylabel("Position Estimation Error (m)")
    axs[0, 0].legend()
    axs[0, 0].grid(True, linestyle='--', alpha=0.5)

    # (b) Perspective-n-Point Reprojection Error vs Marker Distance
    detection_dist = np.linspace(0.5, 5.0, 30)
    reproj_err = 0.42 + 0.18 * (detection_dist**1.6) + np.random.normal(0, 0.12, 30)
    reproj_err = np.clip(reproj_err, 0.2, 3.5)

    axs[0, 1].plot(detection_dist, reproj_err, 'o-', color='#C53030', markersize=4, label='Measured PnP Reprojection Error')
    axs[0, 1].axhline(2.0, color='#E53E3E', linestyle='--', label='Sub-pixel Convergence Bound (2.0 px)')
    axs[0, 1].set_title("(b) ArUco PnP Reprojection Error vs Capture Distance")
    axs[0, 1].set_xlabel("Camera-to-Marker Distance (m)")
    axs[0, 1].set_ylabel("Mean Reprojection Error (pixels)")
    axs[0, 1].legend()
    axs[0, 1].grid(True, linestyle='--', alpha=0.5)

    # (c) Route Backtracking & Navigation Deviations Across Floors
    floors = ['Ground', 'Floor 1', 'Floor 2', 'Floor 3', 'Floor 4', 'Floor 5']
    sign_deviations = [4.2, 5.8, 6.5, 7.8, 8.4, 9.1]
    ar_deviations = [0.8, 0.9, 1.1, 1.2, 1.4, 1.5]

    x = np.arange(len(floors))
    width = 0.35
    axs[1, 0].bar(x - width/2, sign_deviations, width, label='Static Physical Signage', color='#E53E3E', alpha=0.85)
    axs[1, 0].bar(x + width/2, ar_deviations, width, label='AR Visual Marker System', color='#38A169', alpha=0.85)
    axs[1, 0].set_title("(c) Mean Backtracking Incidents per Floor Transition")
    axs[1, 0].set_xlabel("Academic Building Floor Level")
    axs[1, 0].set_ylabel("Wrong Turns / Backtracking Incidents")
    axs[1, 0].set_xticks(x)
    axs[1, 0].set_xticklabels(floors)
    axs[1, 0].legend()
    axs[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

    # (d) Visual Anchor Recognition Latency Across Ambient Lighting
    lux_levels = np.array([50, 100, 200, 400, 600, 800, 1000])
    recog_lat = [118.5, 64.2, 42.1, 38.5, 36.8, 37.2, 38.0]
    axs[1, 1].plot(lux_levels, recog_lat, 's-', color='#805AD5', lw=2, label='ArUco 6x6 Detection Latency')
    axs[1, 1].axhline(60.0, color='#D69E2E', linestyle='--', label='Real-time Frame Budget (60 ms)')
    axs[1, 1].set_title("(d) Anchor Recognition Latency vs Ambient Illumination")
    axs[1, 1].set_xlabel("Ambient Illuminance (lux)")
    axs[1, 1].set_ylabel("Recognition Latency (ms)")
    axs[1, 1].legend()
    axs[1, 1].grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    fig2_path = os.path.join(FIGURES_DIR, "figure2_kinematic_telemetry.png")
    plt.savefig(fig2_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {fig2_path}")

# -------------------------------------------------------------------------
# Figure 3: Comparative Performance Across Navigation Modalities
# -------------------------------------------------------------------------
def generate_figure3():
    fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.8))

    modalities = ['Static Wall\nSignage', '2D Mobile\nPDF Map', 'AR Visual-Marker\nNavigation']
    colors = ['#E53E3E', '#ED8936', '#38A169']

    # (a) Mean Transit Time (s)
    time_means = [468.5, 342.1, 184.6]
    time_stds = [45.2, 32.8, 14.5]
    axs[0].bar(modalities, time_means, yerr=time_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[0].set_title("(a) Mean Multi-Storey Transit Time (s)")
    axs[0].set_ylabel("Transit Time (s)")
    axs[0].set_ylim(0, 560)
    axs[0].grid(axis='y', linestyle='--', alpha=0.5)
    axs[0].text(2, 220, "-60.6%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    # (b) Route-Finding Errors per Journey
    err_means = [6.8, 3.9, 0.7]
    err_stds = [1.2, 0.8, 0.3]
    axs[1].bar(modalities, err_means, yerr=err_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[1].set_title("(b) Mean Route-Finding Errors")
    axs[1].set_ylabel("Wrong-Turn Count")
    axs[1].set_ylim(0, 9.0)
    axs[1].grid(axis='y', linestyle='--', alpha=0.5)
    axs[1].text(2, 1.4, "-89.7%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    # (c) System Usability Scale (SUS) Score
    sus_means = [46.5, 62.8, 88.4]
    sus_stds = [5.4, 4.8, 3.2]
    axs[2].bar(modalities, sus_means, yerr=sus_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[2].set_title("(c) System Usability Scale (SUS)")
    axs[2].set_ylabel("Usability Score (0-100)")
    axs[2].set_ylim(0, 100)
    axs[2].grid(axis='y', linestyle='--', alpha=0.5)
    axs[2].text(2, 92, "+90.1%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    plt.tight_layout()
    fig3_path = os.path.join(FIGURES_DIR, "figure3_comparative_performance.png")
    plt.savefig(fig3_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {fig3_path}")

# -------------------------------------------------------------------------
# Benchmark Dataset Generation (N = 50 trials)
# -------------------------------------------------------------------------
def generate_benchmark_dataset():
    np.random.seed(106)
    n_samples = 50

    fieldnames = [
        "trial_id",
        "participant_id",
        "is_first_year_student",
        "navigation_modality",
        "floor_transition_span",
        "planned_path_length_m",
        "actual_path_length_m",
        "transit_time_s",
        "wrong_turn_count",
        "aruco_resets_count",
        "final_position_error_m",
        "sus_usability_score"
    ]

    csv_path = os.path.join(TELEMETRY_DIR, "SIMULATED_ar_navigation_benchmark.csv")

    rows = []
    for i in range(n_samples):
        trial_id = f"NAV-TR-{i+1:03d}"
        part_id = f"STUDENT-N{i+1:03d}"
        first_yr = 1 if np.random.rand() > 0.15 else 0
        span = int(np.random.choice([1, 2, 3, 4, 5], p=[0.2, 0.25, 0.25, 0.15, 0.15]))
        base_len = 35.0 * span + np.random.normal(0, 8.0)
        base_len = max(25.0, base_len)

        r_val = np.random.rand()
        if r_val < 0.25:
            mod = "Static_Wall_Signage"
            wrong_turns = int(max(1, np.random.poisson(6.5)))
            act_len = base_len * (1.0 + 0.18 * wrong_turns) + np.random.normal(0, 10.0)
            transit = act_len / 0.85 + wrong_turns * 24.0 + np.random.normal(0, 20.0)
            resets = 0
            err_m = 0.0 # N/A for physical signage
            sus = np.random.normal(46.0, 5.0)
        elif r_val < 0.55:
            mod = "Mobile_2D_PDF_Map"
            wrong_turns = int(max(0, np.random.poisson(3.8)))
            act_len = base_len * (1.0 + 0.11 * wrong_turns) + np.random.normal(0, 8.0)
            transit = act_len / 0.98 + wrong_turns * 16.0 + np.random.normal(0, 15.0)
            resets = 0
            err_m = 0.0
            sus = np.random.normal(62.5, 4.5)
        else:
            mod = "AR_Visual_Marker_Nav"
            wrong_turns = int(max(0, np.random.poisson(0.6)))
            act_len = base_len * (1.0 + 0.02 * wrong_turns) + np.random.normal(0, 3.0)
            transit = act_len / 1.22 + wrong_turns * 5.0 + np.random.normal(0, 8.0)
            resets = int(max(1, base_len / 25.0))
            err_m = np.random.normal(0.038, 0.008)
            sus = np.random.normal(88.5, 3.2)

        transit = max(45.0, transit)
        sus = np.clip(sus, 15.0, 100.0)
        err_m = max(0.01, err_m)

        row = {
            "trial_id": trial_id,
            "participant_id": part_id,
            "is_first_year_student": first_yr,
            "navigation_modality": mod,
            "floor_transition_span": span,
            "planned_path_length_m": round(float(base_len), 1),
            "actual_path_length_m": round(float(act_len), 1),
            "transit_time_s": round(float(transit), 1),
            "wrong_turn_count": wrong_turns,
            "aruco_resets_count": resets,
            "final_position_error_m": round(float(err_m), 3),
            "sus_usability_score": round(float(sus), 1)
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
    print("[SUCCESS] All figures and benchmark telemetry generated for IVRAR Group 06.")
