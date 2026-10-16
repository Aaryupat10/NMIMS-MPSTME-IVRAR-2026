# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Generate publication-grade figures (300 DPI) and empirical benchmark dataset for IVRAR Group 08.
Authorized Title: To what extent does a gamified mobile AR checkpoint discovery system
enhance campus facility orientation and navigational self-efficacy among incoming university students?
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
    ax.text(50, 96, "Gamified Mobile AR Checkpoint Discovery Architecture", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')
    ax.text(50, 92, "Integrating Geospatial WGS84 Anchors, ARFoundation 3D Beacons, Gamification Logic, and SBSOD Telemetry", 
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#4A5568')

    # Layer 1: Spatial Anchoring & Sensor Tracking
    rect1 = patches.FancyBboxPatch((4, 66), 26, 22, boxstyle="round,pad=1", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(rect1)
    ax.text(17, 85, "Geospatial & Sensor Layer\n(GPS, IMU & ARCore)", ha='center', va='center', fontweight='bold', color='#2B6CB0', fontsize=9.5)
    ax.text(17, 76, "- High-Accuracy GNSS / GPS\n- 6-DoF Device Pose Estimation\n- Visual-Inertial Odometry\n- Campus POI Coordinate Graph", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 2: AR Checkpoint & Proximity Engine
    rect2 = patches.FancyBboxPatch((37, 66), 26, 22, boxstyle="round,pad=1", ec="#C53030", fc="#FFF5F5", lw=1.5)
    ax.add_patch(rect2)
    ax.text(50, 85, "AR Checkpoint Discovery\n(ARFoundation Beacon Core)", ha='center', va='center', fontweight='bold', color='#C53030', fontsize=9.5)
    ax.text(50, 76, "- Geofence Proximity Trigger\n- Floating 3D Animated Beacons\n- Directional Compass Needles\n- Occlusion-Aware Billboarding", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 3: Gamification & Progression Engine
    rect3 = patches.FancyBboxPatch((70, 66), 26, 22, boxstyle="round,pad=1", ec="#276749", fc="#F0FFF4", lw=1.5)
    ax.add_patch(rect3)
    ax.text(83, 85, "Gamification Progression\n(Quest, XP & Badge System)", ha='center', va='center', fontweight='bold', color='#276749', fontsize=9.5)
    ax.text(83, 76, "- Checkpoint Discovery XP\n- Multi-Tier Facility Badges\n- Exploration Streak Strengths\n- Real-Time Peer Leaderboard", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Connecting arrows across top layers
    arrow_props = dict(facecolor='#4A5568', edgecolor='#4A5568', width=1.5, headwidth=7, headlength=7)
    ax.annotate("", xy=(36, 77), xytext=(31, 77), arrowprops=arrow_props)
    ax.annotate("", xy=(69, 77), xytext=(64, 77), arrowprops=arrow_props)

    # Middle Layer: Student Wayfinding & Interaction Cycle
    rect_mid = patches.FancyBboxPatch((12, 36), 76, 22, boxstyle="round,pad=1", ec="#7B341E", fc="#FFFAF0", lw=1.5)
    ax.add_patch(rect_mid)
    ax.text(50, 54, "Student Orientation & Facility Discovery Workflow", ha='center', va='center', fontweight='bold', color='#7B341E', fontsize=10)
    
    sub_box1 = patches.Rectangle((15, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box1)
    ax.text(25, 44.5, "1. Target Selection\nQuest Prompt & AR Compass", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box2 = patches.Rectangle((40, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box2)
    ax.text(50, 44.5, "2. Checkpoint Approach\nVisual Proximity Beacon", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box3 = patches.Rectangle((65, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box3)
    ax.text(75, 44.5, "3. Facility Unlock\nXP Award & Spatial Trivia", ha='center', va='center', fontsize=8, color='#2D3748')

    ax.annotate("", xy=(39, 44.5), xytext=(36, 44.5), arrowprops=arrow_props)
    ax.annotate("", xy=(64, 44.5), xytext=(61, 44.5), arrowprops=arrow_props)

    # Vertical connectors
    ax.annotate("", xy=(50, 59), xytext=(50, 65), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 27), xytext=(50, 35), arrowprops=arrow_props)

    # Bottom Layer: Empirical Telemetry & Psychometric Evaluation
    rect_bot = patches.FancyBboxPatch((8, 6), 84, 20, boxstyle="round,pad=1", ec="#4A5568", fc="#F7FAFC", lw=1.5)
    ax.add_patch(rect_bot)
    ax.text(50, 22, "Navigational Self-Efficacy, Usability & Technoeconomic Telemetry Pipeline", ha='center', va='center', fontweight='bold', color='#2D3748', fontsize=10)

    ax.text(23, 13, "Spatial Telemetry (N=50)\n- Facility Discovery Rate (%)\n- Backtracking Incident Count\n- Total Trajectory Length (m)", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(50, 13, "Psychometric Assessments\n- Hegarty SBSOD Scale Gain\n- Intrinsic Motivation Inventory\n- NASA-TLX & SUS Index", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(77, 13, "Operational Parity Model\n- Volunteer Docent Hours Saved\n- Disorientation Hours Reclaimed\n- Dimensionless Kappa Ratio", 
            ha='center', va='center', fontsize=8, color='#4A5568')

    plt.tight_layout()
    p1 = os.path.join(FIGURES_DIR, "figure1_system_architecture.png")
    plt.savefig(p1, bbox_inches='tight')
    plt.close()
    print(f"Figure 1 saved to {p1}")

# -------------------------------------------------------------------------
# Figure 2: Kinematic Telemetry & Trajectory Analysis
# -------------------------------------------------------------------------
def generate_figure2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Subplot A: Campus Exploration Trajectories & Checkpoint Layout
    np.random.seed(42)
    # Simulated campus perimeter: 200m x 150m
    ax1.plot([0, 200, 200, 0, 0], [0, 0, 150, 150, 0], 'k-', lw=1.5, label="Campus Boundary")
    
    # Campus Checkpoints
    checkpoints = {
        "Robotics Lab": (35, 40),
        "Central Library": (110, 120),
        "Admin Office": (75, 25),
        "Auditorium": (165, 80),
        "Cafeteria": (140, 30),
        "Sports Complex": (50, 110)
    }

    # Trajectory under Static 2D Map (erratic, multiple backtracking loops)
    t = np.linspace(0, 1, 100)
    map_x = 20 + 150 * t + 25 * np.sin(6 * np.pi * t)
    map_y = 20 + 100 * t + 35 * np.cos(5 * np.pi * t)
    ax1.plot(map_x, map_y, color='#E53E3E', linestyle=':', lw=1.4, alpha=0.7, label="Static Map Path (High Backtracking)")

    # Trajectory under Gamified AR (efficient, direct approach)
    ar_x = 20 + 150 * t + 8 * np.sin(2 * np.pi * t)
    ar_y = 20 + 100 * t + 6 * np.cos(2 * np.pi * t)
    ax1.plot(ar_x, ar_y, color='#2B6CB0', linestyle='-', lw=2.0, label="Gamified AR Path (Streamlined)")

    for name, (cx, cy) in checkpoints.items():
        ax1.scatter(cx, cy, color='#D69E2E', s=90, marker='*', zorder=6)
        ax1.text(cx + 3, cy + 3, name, fontsize=7.5, fontweight='bold', color='#744210')

    ax1.set_title("(a) Campus Traversal & Checkpoint Footprint", fontsize=10, fontweight='bold')
    ax1.set_xlabel("Campus Easting (m)")
    ax1.set_ylabel("Campus Northing (m)")
    ax1.set_xlim(-10, 210)
    ax1.set_ylim(-10, 160)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(loc='lower right', fontsize=7.5)

    # Subplot B: Santa Barbara Sense of Direction (SBSOD) Pre- vs Post-Scores
    pre_scores = np.random.normal(loc=3.4, scale=0.6, size=25)
    post_scores = np.random.normal(loc=5.3, scale=0.5, size=25)

    x = np.arange(len(pre_scores[:12]))
    width = 0.35
    ax2.bar(x - width/2, pre_scores[:12], width, label='Pre-Orientation Baseline', color='#A0AEC0', edgecolor='black')
    ax2.bar(x + width/2, post_scores[:12], width, label='Post-AR Quest Evaluation', color='#3182CE', edgecolor='black')

    ax2.set_title("(b) SBSOD Navigational Self-Efficacy Shift", fontsize=10, fontweight='bold')
    ax2.set_xlabel("Participant Sample (Subset N=12)")
    ax2.set_ylabel("SBSOD Rating (1 to 7 Likert Scale)")
    ax2.set_ylim(0, 7.5)
    ax2.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax2.legend(loc='upper left', fontsize=8)

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

    categories = ['Static 2D Map (Baseline)', 'Gamified Mobile AR']

    # Subplot 1: Facility Checkpoint Discovery Rate (%)
    disc_rates = [64.8, 96.2]
    disc_errs = [6.2, 2.4]
    colors = ['#CBD5E0', '#3182CE']
    bars1 = ax1.bar(categories, disc_rates, yerr=disc_errs, capsize=5, color=colors, edgecolor='black', width=0.55)
    ax1.set_ylim(0, 110)
    ax1.set_ylabel("Discovery Rate (%)")
    ax1.set_title("(a) Facility Discovery Completeness", fontsize=10, fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 5.0, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 2: Backtracking Incidents Count
    backtracks = [7.8, 1.4]
    backtrack_errs = [1.5, 0.4]
    bars2 = ax2.bar(categories, backtracks, yerr=backtrack_errs, capsize=5, color=['#E2E8F0', '#38A169'], edgecolor='black', width=0.55)
    ax2.set_ylim(0, 11)
    ax2.set_ylabel("Mean Backtracking Events")
    ax2.set_title("(b) Route Disorientation Incidents", fontsize=10, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.6, f"{yval:.1f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 3: NASA-TLX Cognitive Workload Breakdown
    subscales = ['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration']
    baseline_tlx = [62, 45, 58, 51, 60, 56]
    ar_tlx = [36, 38, 29, 21, 33, 24]
    x = np.arange(len(subscales))
    width = 0.35

    ax3.bar(x - width/2, baseline_tlx, width, label='Static 2D Map', color='#A0AEC0', edgecolor='black')
    ax3.bar(x + width/2, ar_tlx, width, label='Gamified AR', color='#3182CE', edgecolor='black')
    ax3.set_ylabel("NASA-TLX Subscale (0-100)")
    ax3.set_title("(c) Cognitive Workload Assessment", fontsize=10, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(subscales, rotation=25, ha='right', fontsize=8)
    ax3.set_ylim(0, 85)
    ax3.grid(True, linestyle=':', alpha=0.5, axis='y')
    ax3.legend(loc='upper right', fontsize=8)

    # Subplot 4: System Usability Scale (SUS) Score
    sus_scores = [54.2, 86.4]
    sus_errs = [5.8, 3.2]
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
    np.random.seed(108)
    csv_path = os.path.join(TELEMETRY_DIR, "SIMULATED_campus_orientation_benchmark.csv")
    
    headers = [
        "participant_id",
        "condition",
        "facilities_discovered",
        "total_facilities",
        "discovery_rate_pct",
        "completion_time_sec",
        "backtracking_incidents",
        "total_path_length_meters",
        "sbsod_pre_score",
        "sbsod_post_score",
        "sbsod_gain",
        "nasa_tlx_mental",
        "nasa_tlx_physical",
        "nasa_tlx_temporal",
        "nasa_tlx_performance",
        "nasa_tlx_effort",
        "nasa_tlx_frustration",
        "nasa_tlx_overall",
        "sus_score"
    ]

    total_facilities = 15
    records = []

    # 25 Participants under Static Map 2D condition
    for i in range(1, 26):
        pid = f"P{i:02d}"
        cond = "Static_Map_2D"
        disc = int(np.clip(np.random.normal(9.7, 1.3), 6, 13))
        rate = round((disc / total_facilities) * 100.0, 1)
        dur = round(float(np.clip(np.random.normal(1620.0, 180.0), 1200.0, 2100.0)), 1)
        backtrack = int(np.clip(np.random.normal(7.8, 1.5), 4, 12))
        path_len = round(float(np.clip(np.random.normal(1850.0, 220.0), 1350.0, 2400.0)), 1)

        pre = round(float(np.clip(np.random.normal(3.45, 0.55), 2.1, 4.8)), 2)
        post = round(float(np.clip(pre + np.random.normal(0.35, 0.20), 2.2, 5.2)), 2)
        gain = round(max(0.0, post - pre), 2)

        m_tlx = round(float(np.clip(np.random.normal(62.0, 6.5), 45.0, 78.0)), 1)
        p_tlx = round(float(np.clip(np.random.normal(45.0, 5.5), 32.0, 58.0)), 1)
        t_tlx = round(float(np.clip(np.random.normal(58.0, 6.0), 42.0, 72.0)), 1)
        perf_tlx = round(float(np.clip(np.random.normal(51.0, 5.0), 38.0, 64.0)), 1)
        eff_tlx = round(float(np.clip(np.random.normal(60.0, 5.5), 48.0, 74.0)), 1)
        frust_tlx = round(float(np.clip(np.random.normal(56.0, 6.0), 40.0, 72.0)), 1)
        overall_tlx = round((m_tlx + p_tlx + t_tlx + perf_tlx + eff_tlx + frust_tlx) / 6.0, 1)
        sus = round(float(np.clip(np.random.normal(54.2, 5.8), 42.0, 68.0)), 1)

        records.append([
            pid, cond, disc, total_facilities, rate, dur, backtrack, path_len,
            pre, post, gain, m_tlx, p_tlx, t_tlx, perf_tlx, eff_tlx, frust_tlx, overall_tlx, sus
        ])

    # 25 Participants under Gamified AR condition
    for i in range(26, 51):
        pid = f"P{i:02d}"
        cond = "Gamified_AR"
        disc = int(np.clip(np.random.normal(14.4, 0.6), 13, 15))
        rate = round((disc / total_facilities) * 100.0, 1)
        dur = round(float(np.clip(np.random.normal(920.0, 95.0), 720.0, 1150.0)), 1)
        backtrack = int(np.clip(np.random.normal(1.4, 0.5), 0, 3))
        path_len = round(float(np.clip(np.random.normal(1180.0, 110.0), 950.0, 1420.0)), 1)

        pre = round(float(np.clip(np.random.normal(3.40, 0.50), 2.2, 4.6)), 2)
        post = round(float(np.clip(pre + np.random.normal(1.85, 0.30), 4.5, 6.8)), 2)
        gain = round(max(0.0, post - pre), 2)

        m_tlx = round(float(np.clip(np.random.normal(36.0, 5.0), 24.0, 48.0)), 1)
        p_tlx = round(float(np.clip(np.random.normal(38.0, 4.5), 26.0, 48.0)), 1)
        t_tlx = round(float(np.clip(np.random.normal(29.0, 4.0), 18.0, 38.0)), 1)
        perf_tlx = round(float(np.clip(np.random.normal(21.0, 3.5), 12.0, 30.0)), 1)
        eff_tlx = round(float(np.clip(np.random.normal(33.0, 4.0), 22.0, 42.0)), 1)
        frust_tlx = round(float(np.clip(np.random.normal(24.0, 4.5), 14.0, 35.0)), 1)
        overall_tlx = round((m_tlx + p_tlx + t_tlx + perf_tlx + eff_tlx + frust_tlx) / 6.0, 1)
        sus = round(float(np.clip(np.random.normal(86.4, 3.2), 78.0, 94.0)), 1)

        records.append([
            pid, cond, disc, total_facilities, rate, dur, backtrack, path_len,
            pre, post, gain, m_tlx, p_tlx, t_tlx, perf_tlx, eff_tlx, frust_tlx, overall_tlx, sus
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
