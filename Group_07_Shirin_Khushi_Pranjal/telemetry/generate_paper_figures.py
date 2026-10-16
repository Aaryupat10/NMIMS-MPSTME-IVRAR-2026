# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Generate publication-grade figures (300 DPI) and empirical benchmark dataset for IVRAR Group 07.
Authorized Title: To what extent does an interactive VR spatial crime scene reconstruction
improve evidence tagging accuracy and timeline sequencing for student forensic investigators compared to traditional 2D photographic logs?
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
    ax.text(50, 96, "Interactive VR Spatial Crime Scene Reconstruction Architecture", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')
    ax.text(50, 92, "Integrating Photogrammetry/LiDAR Scanning, XR Interaction Toolkit, 3D Evidence Tagging, and Timeline Telemetry", 
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#4A5568')

    # Layer 1: Spatial Capture & Environmental Digital Twin
    rect1 = patches.FancyBboxPatch((4, 66), 26, 22, boxstyle="round,pad=1", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(rect1)
    ax.text(17, 85, "Spatial Capture & Twin Layer\n(Photogrammetry & LiDAR)", ha='center', va='center', fontweight='bold', color='#2B6CB0', fontsize=9.5)
    ax.text(17, 76, "- Terrestrial LiDAR Scanning\n- Multi-View Photogrammetry\n- High-Res Mesh Texture UVs\n- Collider Boundary Physics", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 2: Unity XR Interaction & Evidence Anchoring
    rect2 = patches.FancyBboxPatch((37, 66), 26, 22, boxstyle="round,pad=1", ec="#C53030", fc="#FFF5F5", lw=1.5)
    ax.add_patch(rect2)
    ax.text(50, 85, "XR Evidence Tagging Core\n(Unity XR Interaction Toolkit)", ha='center', va='center', fontweight='bold', color='#C53030', fontsize=9.5)
    ax.text(50, 76, "- Direct / Raycast Interaction\n- 3D Evidence Marker Snapping\n- Real-Time Euclidean Residuals\n- Digital Chain-of-Custody Hash", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 3: Forensic Timeline & Telemetry Analytics
    rect3 = patches.FancyBboxPatch((70, 66), 26, 22, boxstyle="round,pad=1", ec="#276749", fc="#F0FFF4", lw=1.5)
    ax.add_patch(rect3)
    ax.text(83, 85, "Timeline Reconstruction\n(Telemetry & Sequence Audit)", ha='center', va='center', fontweight='bold', color='#276749', fontsize=9.5)
    ax.text(83, 76, "- Chronological Event Order\n- Kendall-Tau Rank Scoring\n- Investigator Trajectory Heatmap\n- ISO 27037 Audit Serialization", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Connecting arrows across layers
    arrow_props = dict(facecolor='#4A5568', edgecolor='#4A5568', width=1.5, headwidth=7, headlength=7)
    ax.annotate("", xy=(36, 77), xytext=(31, 77), arrowprops=arrow_props)
    ax.annotate("", xy=(69, 77), xytext=(64, 77), arrowprops=arrow_props)

    # Middle Layer: Investigator Interaction Workflow
    rect_mid = patches.FancyBboxPatch((12, 36), 76, 22, boxstyle="round,pad=1", ec="#7B341E", fc="#FFFAF0", lw=1.5)
    ax.add_patch(rect_mid)
    ax.text(50, 54, "Investigator Multi-Modal Spatial Interaction Workflow", ha='center', va='center', fontweight='bold', color='#7B341E', fontsize=10)
    
    sub_box1 = patches.Rectangle((15, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box1)
    ax.text(25, 44.5, "1. Spatial Scene Search\nRoom Trajectory & Angles", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box2 = patches.Rectangle((40, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box2)
    ax.text(50, 44.5, "2. Evidence Tagging\nItem Type & 3D Coordinates", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box3 = patches.Rectangle((65, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box3)
    ax.text(75, 44.5, "3. Event Sequencing\nTimeline Chronology Matrix", ha='center', va='center', fontsize=8, color='#2D3748')

    ax.annotate("", xy=(39, 44.5), xytext=(36, 44.5), arrowprops=arrow_props)
    ax.annotate("", xy=(64, 44.5), xytext=(61, 44.5), arrowprops=arrow_props)

    # Vertical connectors
    ax.annotate("", xy=(50, 59), xytext=(50, 65), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 27), xytext=(50, 35), arrowprops=arrow_props)

    # Bottom Layer: Empirical Validation & Pedagogical Evaluation
    rect_bot = patches.FancyBboxPatch((8, 6), 84, 20, boxstyle="round,pad=1", ec="#4A5568", fc="#F7FAFC", lw=1.5)
    ax.add_patch(rect_bot)
    ax.text(50, 22, "Empirical Telemetry, Usability, and Technoeconomic Evaluation Engine", ha='center', va='center', fontweight='bold', color='#2D3748', fontsize=10)

    ax.text(23, 13, "Empirical Metrics (N=50)\n- Tagging Accuracy (%)\n- Kendall-Tau Sequence Score\n- Localization Error (cm)", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(50, 13, "Human Factors Assessment\n- NASA-TLX Cognitive Load\n- System Usability Scale (SUS)\n- Time-to-Identify Evidence", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(77, 13, "Operational Parity Model\n- Mock Staging Hours Reclaimed\n- Consumables Replaced\n- Dimensionless Kappa Ratio", 
            ha='center', va='center', fontsize=8, color='#4A5568')

    plt.tight_layout()
    p1 = os.path.join(FIGURES_DIR, "figure1_system_architecture.png")
    plt.savefig(p1, bbox_inches='tight')
    plt.close()
    print(f"Figure 1 saved to {p1}")

# -------------------------------------------------------------------------
# Figure 2: Kinematic Telemetry & Spatial Tagging Accuracy
# -------------------------------------------------------------------------
def generate_figure2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Subplot A: Investigator Spatial Search Trajectory (2D Bird's-Eye View)
    np.random.seed(42)
    # Simulated room boundaries: 8m x 6m room
    ax1.plot([0, 8, 8, 0, 0], [0, 0, 6, 6, 0], 'k-', lw=2, label="Crime Scene Room Boundary")
    
    # Ground Truth Evidence Items (Coordinates in meters)
    gt_evidence = {
        "Weapon": (2.1, 1.4),
        "Spent Casing": (2.8, 1.9),
        "Blood Spatter": (5.2, 4.3),
        "Footwear Impression": (1.2, 4.8),
        "Discarded Mobile": (6.7, 2.1)
    }

    # Investigator Trajectory (VR Spatial Condition)
    t = np.linspace(0, 1, 80)
    traj_x = 1.0 + 5.5 * t + 0.8 * np.sin(4 * np.pi * t)
    traj_y = 1.0 + 3.8 * t + 1.1 * np.cos(3 * np.pi * t)
    ax1.plot(traj_x, traj_y, color='#2B6CB0', linestyle='--', lw=1.8, label="Investigator Trajectory (VR)")
    ax1.scatter(traj_x[0], traj_y[0], color='#38A169', s=90, zorder=5, marker='o', label="Entry Point")
    ax1.scatter(traj_x[-1], traj_y[-1], color='#E53E3E', s=90, zorder=5, marker='s', label="Exit Point")

    for name, (ex, ey) in gt_evidence.items():
        ax1.scatter(ex, ey, color='#D69E2E', s=100, marker='*', zorder=6)
        ax1.text(ex + 0.15, ey + 0.15, name, fontsize=7.5, fontweight='bold', color='#744210')

    ax1.set_title("(a) Spatial Inspection Trajectory & Evidence Map", fontsize=10, fontweight='bold')
    ax1.set_xlabel("Room X Position (m)")
    ax1.set_ylabel("Room Y Position (m)")
    ax1.set_xlim(-0.5, 8.5)
    ax1.set_ylim(-0.5, 6.5)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='lower right', fontsize=7.5)

    # Subplot B: Euclidean Spatial Localization Error Distribution
    vr_errors = np.random.normal(loc=3.4, scale=1.1, size=25) # in cm
    baseline_errors = np.random.normal(loc=14.2, scale=3.6, size=25) # in cm

    bins = np.linspace(0, 25, 15)
    ax2.hist(vr_errors, bins=bins, alpha=0.75, color='#3182CE', label=f'VR Spatial (Mean={np.mean(vr_errors):.1f} cm)', edgecolor='black')
    ax2.hist(baseline_errors, bins=bins, alpha=0.65, color='#E53E3E', label=f'2D Photo Log (Mean={np.mean(baseline_errors):.1f} cm)', edgecolor='black')

    ax2.axvline(np.mean(vr_errors), color='#2B6CB0', linestyle='--', lw=2)
    ax2.axvline(np.mean(baseline_errors), color='#9B2C2C', linestyle='--', lw=2)

    ax2.set_title("(b) Evidence Spatial Localization Error Residuals", fontsize=10, fontweight='bold')
    ax2.set_xlabel("Euclidean Localization Error (cm)")
    ax2.set_ylabel("Investigator Count (N=50)")
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.legend(loc='upper right', fontsize=8)

    plt.tight_layout()
    p2 = os.path.join(FIGURES_DIR, "figure2_kinematic_telemetry.png")
    plt.savefig(p2, bbox_inches='tight')
    plt.close()
    print(f"Figure 2 saved to {p2}")

# -------------------------------------------------------------------------
# Figure 3: Comparative Performance Analysis
# -------------------------------------------------------------------------
def generate_figure3():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(9.5, 7.5))

    categories = ['2D Photo Log (Baseline)', 'Interactive VR Spatial']

    # Subplot 1: Evidence Tagging Identification Rate (%)
    tagging_rates = [72.4, 94.8]
    tagging_errs = [5.1, 2.8]
    colors = ['#CBD5E0', '#3182CE']
    bars1 = ax1.bar(categories, tagging_rates, yerr=tagging_errs, capsize=5, color=colors, edgecolor='black', width=0.55)
    ax1.set_ylim(0, 110)
    ax1.set_ylabel("Identification Rate (%)")
    ax1.set_title("(a) Evidence Tagging Completeness", fontsize=10, fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 6.0, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 2: Timeline Sequencing Kendall-Tau Correlation
    tau_scores = [0.48, 0.86]
    tau_errs = [0.11, 0.06]
    bars2 = ax2.bar(categories, tau_scores, yerr=tau_errs, capsize=5, color=colors, edgecolor='black', width=0.55)
    ax2.set_ylim(0, 1.1)
    ax2.set_ylabel("Kendall-Tau Score (-1 to +1)")
    ax2.set_title("(b) Timeline Sequencing Concordance", fontsize=10, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.08, f"tau = {yval:.2f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 3: NASA-TLX Cognitive Workload Breakdown
    subscales = ['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration']
    baseline_tlx = [68, 32, 59, 54, 62, 58]
    vr_tlx = [46, 42, 38, 26, 41, 29] # Lower performance score indicates better perceived performance in TLX scale
    x = np.arange(len(subscales))
    width = 0.35

    ax3.bar(x - width/2, baseline_tlx, width, label='2D Photo Log', color='#A0AEC0', edgecolor='black')
    ax3.bar(x + width/2, vr_tlx, width, label='Interactive VR', color='#3182CE', edgecolor='black')
    ax3.set_ylabel("NASA-TLX Subscale (0-100)")
    ax3.set_title("(c) Cognitive Workload Assessment", fontsize=10, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(subscales, rotation=25, ha='right', fontsize=8)
    ax3.set_ylim(0, 90)
    ax3.grid(True, linestyle=':', alpha=0.5, axis='y')
    ax3.legend(loc='upper right', fontsize=8)

    # Subplot 4: System Usability Scale (SUS) Score
    sus_scores = [58.4, 84.6]
    sus_errs = [6.2, 3.8]
    bars4 = ax4.bar(categories, sus_scores, yerr=sus_errs, capsize=5, color=colors, edgecolor='black', width=0.55)
    ax4.axhline(68.0, color='#D69E2E', linestyle='--', lw=1.5, label='Industry Usability Benchmark (SUS=68)')
    ax4.set_ylim(0, 105)
    ax4.set_ylabel("SUS Score (0-100)")
    ax4.set_title("(d) Usability & Experience Quality", fontsize=10, fontweight='bold')
    ax4.grid(True, linestyle=':', alpha=0.5, axis='y')
    ax4.legend(loc='upper left', fontsize=7.5)
    for bar in bars4:
        yval = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2.0, yval + 5.0, f"{yval:.1f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    plt.tight_layout()
    p3 = os.path.join(FIGURES_DIR, "figure3_comparative_performance.png")
    plt.savefig(p3, bbox_inches='tight')
    plt.close()
    print(f"Figure 3 saved to {p3}")

# -------------------------------------------------------------------------
# Empirical Benchmark Dataset Generation (N=50)
# -------------------------------------------------------------------------
def generate_benchmark_csv():
    np.random.seed(107)
    csv_path = os.path.join(TELEMETRY_DIR, "SIMULATED_forensic_reconstruction_benchmark.csv")
    
    headers = [
        "participant_id",
        "condition",
        "evidence_items_identified",
        "total_evidence_items",
        "identification_rate_pct",
        "spatial_localization_error_cm",
        "timeline_kendall_tau",
        "inspection_duration_sec",
        "nasa_tlx_mental_demand",
        "nasa_tlx_physical_demand",
        "nasa_tlx_temporal_demand",
        "nasa_tlx_performance",
        "nasa_tlx_effort",
        "nasa_tlx_frustration",
        "nasa_tlx_overall",
        "sus_score"
    ]

    total_items = 12
    records = []

    # 25 Participants under 2D Photo Log baseline
    for i in range(1, 26):
        pid = f"P{i:02d}"
        cond = "Photo_Log_2D"
        items = int(np.clip(np.random.normal(8.6, 1.2), 6, 11))
        rate = round((items / total_items) * 100.0, 1)
        err_cm = round(float(np.clip(np.random.normal(14.2, 3.1), 8.5, 23.0)), 2)
        tau = round(float(np.clip(np.random.normal(0.48, 0.12), 0.18, 0.72)), 3)
        dur = round(float(np.clip(np.random.normal(740.0, 85.0), 550.0, 950.0)), 1)
        
        m_tlx = round(float(np.clip(np.random.normal(68.0, 7.5), 45.0, 85.0)), 1)
        p_tlx = round(float(np.clip(np.random.normal(32.0, 6.0), 18.0, 48.0)), 1)
        t_tlx = round(float(np.clip(np.random.normal(59.0, 8.0), 40.0, 78.0)), 1)
        perf_tlx = round(float(np.clip(np.random.normal(54.0, 7.0), 38.0, 70.0)), 1)
        eff_tlx = round(float(np.clip(np.random.normal(62.0, 6.5), 48.0, 76.0)), 1)
        frust_tlx = round(float(np.clip(np.random.normal(58.0, 8.0), 40.0, 75.0)), 1)
        overall_tlx = round((m_tlx + p_tlx + t_tlx + perf_tlx + eff_tlx + frust_tlx) / 6.0, 1)
        sus = round(float(np.clip(np.random.normal(58.4, 6.2), 45.0, 72.5)), 1)

        records.append([
            pid, cond, items, total_items, rate, err_cm, tau, dur,
            m_tlx, p_tlx, t_tlx, perf_tlx, eff_tlx, frust_tlx, overall_tlx, sus
        ])

    # 25 Participants under VR Spatial Reconstruction condition
    for i in range(26, 51):
        pid = f"P{i:02d}"
        cond = "VR_Spatial"
        items = int(np.clip(np.random.normal(11.4, 0.7), 10, 12))
        rate = round((items / total_items) * 100.0, 1)
        err_cm = round(float(np.clip(np.random.normal(3.4, 0.9), 1.8, 6.2)), 2)
        tau = round(float(np.clip(np.random.normal(0.86, 0.06), 0.71, 0.98)), 3)
        dur = round(float(np.clip(np.random.normal(510.0, 60.0), 380.0, 640.0)), 1)

        m_tlx = round(float(np.clip(np.random.normal(46.0, 5.5), 32.0, 58.0)), 1)
        p_tlx = round(float(np.clip(np.random.normal(42.0, 5.0), 28.0, 52.0)), 1)
        t_tlx = round(float(np.clip(np.random.normal(38.0, 6.0), 25.0, 50.0)), 1)
        perf_tlx = round(float(np.clip(np.random.normal(26.0, 4.5), 15.0, 36.0)), 1)
        eff_tlx = round(float(np.clip(np.random.normal(41.0, 5.0), 28.0, 52.0)), 1)
        frust_tlx = round(float(np.clip(np.random.normal(29.0, 5.5), 18.0, 42.0)), 1)
        overall_tlx = round((m_tlx + p_tlx + t_tlx + perf_tlx + eff_tlx + frust_tlx) / 6.0, 1)
        sus = round(float(np.clip(np.random.normal(84.6, 4.1), 75.0, 92.5)), 1)

        records.append([
            pid, cond, items, total_items, rate, err_cm, tau, dur,
            m_tlx, p_tlx, t_tlx, perf_tlx, eff_tlx, frust_tlx, overall_tlx, sus
        ])

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(records)

    print(f"Benchmark CSV written to {csv_path} with {len(records)} participant records.")

if __name__ == "__main__":
    generate_figure1()
    generate_figure2()
    generate_figure3()
    generate_benchmark_csv()
