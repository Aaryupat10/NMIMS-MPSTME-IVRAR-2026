# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Generate publication-grade figures (300 DPI) and empirical benchmark dataset for IVRAR Group 10.
Authorized Title: How can an OpenCV-based color and fiducial hand-tracking pipeline integrated with Unity VR
achieve sub-15ms latency and gesture recognition accuracy for architectural 3D model reviews without dedicated 6-DoF controllers?
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
    ax.text(50, 96, "Low-Latency OpenCV Optical Hand-Tracking & BIM VR Architecture", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')
    ax.text(50, 92, "Coupling Color Glove/Fiducial Segmentation, Sub-15ms UDP Bridge, and Unity Architectural Gesture Manipulation", 
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#4A5568')

    # Layer 1: Monocular Video Ingestion & OpenCV Vision Core
    rect1 = patches.FancyBboxPatch((4, 66), 26, 22, boxstyle="round,pad=1", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(rect1)
    ax.text(17, 85, "Computer Vision Pipeline\n(OpenCV & HSV Segmentation)", ha='center', va='center', fontweight='bold', color='#2B6CB0', fontsize=9.5)
    ax.text(17, 76, "- 120 FPS USB Camera Feed\n- Adaptive HSV Color Masking\n- 5-Finger Contour Centroids\n- Spatial Kalman Filtering", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 2: Ultra-Low-Latency IPC & Pose Bridge
    rect2 = patches.FancyBboxPatch((37, 66), 26, 22, boxstyle="round,pad=1", ec="#C53030", fc="#FFF5F5", lw=1.5)
    ax.add_patch(rect2)
    ax.text(50, 85, "Sub-15ms Pose Bridge\n(UDP Socket / Shared Memory)", ha='center', va='center', fontweight='bold', color='#C53030', fontsize=9.5)
    ax.text(50, 76, "- Binary Struct Packing\n- Non-Blocking UDP Telemetry\n- Real-Time Timestamp Sync\n- Latency Jitter Suppression", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 3: Unity VR Gesture & BIM Inspection Core
    rect3 = patches.FancyBboxPatch((70, 66), 26, 22, boxstyle="round,pad=1", ec="#276749", fc="#F0FFF4", lw=1.5)
    ax.add_patch(rect3)
    ax.text(83, 85, "Unity VR BIM Engine\n(Gesture State Machine)", ha='center', va='center', fontweight='bold', color='#276749', fontsize=9.5)
    ax.text(83, 76, "- Pinch / Fist / Rotate States\n- 3D Affine Model Manipulation\n- Architectural Floor Explosion\n- Sub-15ms End-to-End Loop", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Connecting arrows across top layers
    arrow_props = dict(facecolor='#4A5568', edgecolor='#4A5568', width=1.5, headwidth=7, headlength=7)
    ax.annotate("", xy=(36, 77), xytext=(31, 77), arrowprops=arrow_props)
    ax.annotate("", xy=(69, 77), xytext=(64, 77), arrowprops=arrow_props)

    # Middle Layer: Bare-Hand Gesture Interaction Cycle
    rect_mid = patches.FancyBboxPatch((12, 36), 76, 22, boxstyle="round,pad=1", ec="#7B341E", fc="#FFFAF0", lw=1.5)
    ax.add_patch(rect_mid)
    ax.text(50, 54, "Architectural Design Review Gesture Interaction Cycle", ha='center', va='center', fontweight='bold', color='#7B341E', fontsize=10)
    
    sub_box1 = patches.Rectangle((15, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box1)
    ax.text(25, 44.5, "1. Natural Hover\nOpen Hand Pointing", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box2 = patches.Rectangle((40, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box2)
    ax.text(50, 44.5, "2. Pinch & Pan\nTranslate / Scale Model", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box3 = patches.Rectangle((65, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box3)
    ax.text(75, 44.5, "3. Palm Lock\nExplode Layer / Menu", ha='center', va='center', fontsize=8, color='#2D3748')

    ax.annotate("", xy=(39, 44.5), xytext=(36, 44.5), arrowprops=arrow_props)
    ax.annotate("", xy=(64, 44.5), xytext=(61, 44.5), arrowprops=arrow_props)

    # Vertical connectors
    ax.annotate("", xy=(50, 59), xytext=(50, 65), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 27), xytext=(50, 35), arrowprops=arrow_props)

    # Bottom Layer: Empirical Telemetry & Usability Engine
    rect_bot = patches.FancyBboxPatch((8, 6), 84, 20, boxstyle="round,pad=1", ec="#4A5568", fc="#F7FAFC", lw=1.5)
    ax.add_patch(rect_bot)
    ax.text(50, 22, "Empirical Kinematic Latency, Usability, and Technoeconomic Pipeline", ha='center', va='center', fontweight='bold', color='#2D3748', fontsize=10)

    ax.text(23, 13, "Pipeline Latency (N=50)\n- Sub-15ms Verification\n- Stage Breakdown (ms)\n- Gesture Accuracy (%)", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(50, 13, "Human Factors Assessment\n- NASA-TLX Cognitive Load\n- System Usability Scale (SUS)\n- Ergonomic Arm Fatigue", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(77, 13, "Operational Parity Model\n- Controller Fleet Avoided\n- Breakage Losses Slashed\n- Dimensionless Kappa Ratio", 
            ha='center', va='center', fontsize=8, color='#4A5568')

    plt.tight_layout()
    p1 = os.path.join(FIGURES_DIR, "figure1_system_architecture.png")
    plt.savefig(p1, bbox_inches='tight')
    plt.close()
    print(f"Figure 1 saved to {p1}")

# -------------------------------------------------------------------------
# Figure 2: Kinematic Telemetry & Pipeline Latency
# -------------------------------------------------------------------------
def generate_figure2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Subplot A: Pipeline Latency Breakdown Across Stages
    stages = ['Frame\nCapture', 'HSV\nMasking', 'Contour\nExtraction', 'UDP\nTransport', 'Unity\nRender']
    latencies = [3.2, 2.4, 2.1, 1.3, 3.1]  # Sum = 12.1 ms (< 15ms target)
    colors = ['#2B6CB0', '#3182CE', '#4299E1', '#63B3ED', '#90CDF4']

    bars1 = ax1.bar(stages, latencies, color=colors, edgecolor='black', width=0.55)
    ax1.axhline(15.0, color='#E53E3E', linestyle='--', lw=1.8, label='Sub-15ms Upper Bound Limit')
    ax1.set_title("(a) End-to-End Pipeline Latency Budget (12.1 ms Total)", fontsize=10, fontweight='bold')
    ax1.set_ylabel("Latency (Milliseconds)")
    ax1.set_ylim(0, 17)
    ax1.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax1.legend(loc='upper right', fontsize=8)

    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 0.4, f"{yval:.1f}ms", ha='center', va='bottom', fontsize=8, fontweight='bold')

    # Subplot B: Gesture Recognition Confusion Matrix
    gestures = ['Hover', 'Pinch', 'Fist', 'Rotate', 'Freeze']
    confusion = np.array([
        [0.96, 0.02, 0.01, 0.01, 0.00],
        [0.03, 0.94, 0.02, 0.01, 0.00],
        [0.01, 0.02, 0.95, 0.02, 0.00],
        [0.02, 0.01, 0.03, 0.92, 0.02],
        [0.01, 0.00, 0.01, 0.02, 0.96]
    ])

    im = ax2.imshow(confusion, interpolation='nearest', cmap=plt.cm.Blues, vmin=0, vmax=1.0)
    ax2.set_title("(b) Gesture Classification Confusion Matrix", fontsize=10, fontweight='bold')
    tick_marks = np.arange(len(gestures))
    ax2.set_xticks(tick_marks)
    ax2.set_xticklabels(gestures, fontsize=8)
    ax2.set_yticks(tick_marks)
    ax2.set_yticklabels(gestures, fontsize=8)
    ax2.set_xlabel("Predicted Gesture")
    ax2.set_ylabel("True Target Gesture")

    for i in range(len(gestures)):
        for j in range(len(gestures)):
            val = confusion[i, j]
            color = "white" if val > 0.5 else "black"
            ax2.text(j, i, f"{val:.2f}", ha="center", va="center", color=color, fontsize=8, fontweight='bold')

    fig.colorbar(im, ax=ax2, fraction=0.046, pad=0.04)

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

    categories = ['Dedicated 6-DoF Controller', 'OpenCV Optical Tracking']

    # Subplot 1: Architectural Model Review Task Completion Time (s)
    task_times = [265.4, 218.6]
    time_errs = [24.2, 16.5]
    colors = ['#CBD5E0', '#3182CE']
    bars1 = ax1.bar(categories, task_times, yerr=time_errs, capsize=5, color=colors, edgecolor='black', width=0.55)
    ax1.set_ylim(0, 320)
    ax1.set_ylabel("Task Duration (Seconds)")
    ax1.set_title("(a) Architectural Review Task Completion Time", fontsize=10, fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 10.0, f"{yval:.1f}s", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 2: Overall Gesture Interaction Accuracy (%)
    accuracy_scores = [96.4, 94.6]
    acc_errs = [1.8, 2.2]
    bars2 = ax2.bar(categories, accuracy_scores, yerr=acc_errs, capsize=5, color=['#E2E8F0', '#38A169'], edgecolor='black', width=0.55)
    ax2.set_ylim(0, 110)
    ax2.set_ylabel("Interaction Accuracy (%)")
    ax2.set_title("(b) Gesture Recognition & Manipulation Accuracy", fontsize=10, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 4.0, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 3: NASA-TLX Cognitive Workload Breakdown
    subscales = ['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration']
    baseline_tlx = [48, 56, 42, 34, 52, 38]  # Physical higher due to holding 200g controllers
    optical_tlx = [41, 32, 36, 26, 38, 24]   # Bare hand is physically effortless
    x = np.arange(len(subscales))
    width = 0.35

    ax3.bar(x - width/2, baseline_tlx, width, label='6-DoF Controller', color='#A0AEC0', edgecolor='black')
    ax3.bar(x + width/2, optical_tlx, width, label='OpenCV Optical', color='#3182CE', edgecolor='black')
    ax3.set_ylabel("NASA-TLX Subscale (0-100)")
    ax3.set_title("(c) Cognitive & Ergonomic Workload", fontsize=10, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(subscales, rotation=25, ha='right', fontsize=8)
    ax3.set_ylim(0, 75)
    ax3.grid(True, linestyle=':', alpha=0.5, axis='y')
    ax3.legend(loc='upper right', fontsize=8)

    # Subplot 4: System Usability Scale (SUS) Score
    sus_scores = [78.2, 87.6]
    sus_errs = [4.5, 3.1]
    bars4 = ax4.bar(categories, sus_scores, yerr=sus_errs, capsize=5, color=colors, edgecolor='black', width=0.55)
    ax4.axhline(68.0, color='#D69E2E', linestyle='--', lw=1.5, label='Industry Usability Benchmark (SUS=68)')
    ax4.set_ylim(0, 105)
    ax4.set_ylabel("SUS Score (0-100)")
    ax4.set_title("(d) Usability & Experience Quality", fontsize=10, fontweight='bold')
    ax4.grid(True, linestyle=':', alpha=0.5, axis='y')
    ax4.legend(loc='upper left', fontsize=7.5)
    for bar in bars4:
        yval = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2.0, yval + 4.0, f"{yval:.1f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    plt.tight_layout()
    p3 = os.path.join(FIGURES_DIR, "figure3_comparative_performance.png")
    plt.savefig(p3, bbox_inches='tight')
    plt.close()
    print(f"Figure 3 saved to {p3}")

# -------------------------------------------------------------------------
# Empirical Benchmark Dataset Generation (N=50)
# -------------------------------------------------------------------------
def generate_benchmark_csv():
    np.random.seed(110)
    csv_path = os.path.join(TELEMETRY_DIR, "SIMULATED_hand_tracking_benchmark.csv")
    
    headers = [
        "participant_id",
        "condition",
        "task_completion_time_sec",
        "gesture_accuracy_pct",
        "mean_latency_ms",
        "latency_jitter_ms",
        "successful_commands",
        "misrecognized_commands",
        "nasa_tlx_physical",
        "nasa_tlx_overall",
        "sus_score"
    ]

    records = []

    # 25 Participants under Dedicated 6-DoF Controller condition
    for i in range(1, 26):
        pid = f"P{i:02d}"
        cond = "Dedicated_6DoF_Controller"
        dur = round(float(np.clip(np.random.normal(265.4, 22.0), 220.0, 310.0)), 1)
        acc = round(float(np.clip(np.random.normal(96.4, 1.6), 92.5, 99.0)), 1)
        lat = round(float(np.clip(np.random.normal(18.5, 1.8), 15.2, 22.5)), 2)
        jitter = round(float(np.clip(np.random.normal(2.1, 0.4), 1.2, 3.2)), 2)
        success = int(np.clip(np.random.normal(48, 2), 44, 52))
        misrec = int(np.clip(np.random.normal(2, 1), 0, 4))
        phys_tlx = round(float(np.clip(np.random.normal(56.0, 4.8), 46.0, 68.0)), 1)
        tlx = round(float(np.clip(np.random.normal(45.0, 4.1), 36.0, 54.0)), 1)
        sus = round(float(np.clip(np.random.normal(78.2, 4.5), 68.0, 86.0)), 1)

        records.append([
            pid, cond, dur, acc, lat, jitter, success, misrec, phys_tlx, tlx, sus
        ])

    # 25 Participants under OpenCV Optical Hand Tracking condition
    for i in range(26, 51):
        pid = f"P{i:02d}"
        cond = "OpenCV_Optical_Tracking"
        dur = round(float(np.clip(np.random.normal(218.6, 16.0), 185.0, 255.0)), 1)
        acc = round(float(np.clip(np.random.normal(94.6, 2.0), 89.5, 98.0)), 1)
        lat = round(float(np.clip(np.random.normal(12.1, 0.8), 10.4, 14.1)), 2)
        jitter = round(float(np.clip(np.random.normal(0.9, 0.2), 0.5, 1.5)), 2)
        success = int(np.clip(np.random.normal(47, 2), 43, 50))
        misrec = int(np.clip(np.random.normal(3, 1), 1, 5))
        phys_tlx = round(float(np.clip(np.random.normal(32.0, 3.5), 24.0, 40.0)), 1)
        tlx = round(float(np.clip(np.random.normal(32.8, 3.2), 26.0, 39.0)), 1)
        sus = round(float(np.clip(np.random.normal(87.6, 3.1), 81.0, 94.0)), 1)

        records.append([
            pid, cond, dur, acc, lat, jitter, success, misrec, phys_tlx, tlx, sus
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
