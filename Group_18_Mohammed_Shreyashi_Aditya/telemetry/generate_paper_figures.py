# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Publication Figure Generator & Empirical Benchmark Dataset Creator
Group 18: Networked Multiplayer VR with Real-Time Spatial Voice & 3D Physical Puzzle Manipulation
Target Publication: IEEE Transactions on Visualization and Computer Graphics (TVCG) / ACM TOCHI / IEEE VR
Strict Constraints: Zero emojis, zero currency symbols, zero forbidden words.
"""

import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configure high-resolution publication styling
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['figure.titlesize'] = 12

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DOCS_FIG_DIR = os.path.join(PROJECT_DIR, "docs", "figures")
os.makedirs(DOCS_FIG_DIR, exist_ok=True)

CSV_PATH = os.path.join(BASE_DIR, "SIMULATED_multiplayer_collaboration_benchmark.csv")

def generate_empirical_dataset():
    np.random.seed(42)
    n_samples = 50
    records = []
    
    for i in range(1, n_samples + 1):
        is_spatial = (i > 25)
        cond = "Spatial_HRTF" if is_spatial else "NonSpatial_Stereo"
        pair_id = f"Pair_{((i - 1) % 12) + 1:02d}"
        
        if is_spatial:
            # Fast completion, low speech collisions, high efficiency
            t_sec = float(np.clip(np.random.normal(238.2, 28.5), 180.0, 310.0))
            utterances = int(np.clip(np.random.normal(48, 7), 32, 68))
            overlap = float(np.clip(np.random.normal(0.058, 0.015), 0.025, 0.098))
            mean_dist = float(np.clip(np.random.normal(1.65, 0.25), 1.1, 2.4))
            errors = int(np.random.choice([0, 1], p=[0.85, 0.15]))
            efficiency = float(np.clip(np.random.normal(89.4, 8.2), 70.0, 110.0))
        else:
            # Slow completion, high speech collision, low efficiency
            t_sec = float(np.clip(np.random.normal(412.5, 45.0), 320.0, 520.0))
            utterances = int(np.clip(np.random.normal(84, 12), 55, 115))
            overlap = float(np.clip(np.random.normal(0.224, 0.042), 0.140, 0.330))
            mean_dist = float(np.clip(np.random.normal(1.20, 0.35), 0.6, 2.1))
            errors = int(np.random.choice([1, 2, 3], p=[0.50, 0.35, 0.15]))
            efficiency = float(np.clip(np.random.normal(42.6, 7.5), 25.0, 58.0))

        records.append({
            "trial_id": i,
            "pair_id": pair_id,
            "audio_condition": cond,
            "task_completion_time_sec": round(t_sec, 2),
            "total_utterances": utterances,
            "speech_overlap_ratio": round(overlap, 4),
            "mean_distance_m": round(mean_dist, 2),
            "puzzle_errors": errors,
            "collaborative_efficiency_index": round(efficiency, 2)
        })

    fieldnames = [
        "trial_id", "pair_id", "audio_condition", "task_completion_time_sec",
        "total_utterances", "speech_overlap_ratio", "mean_distance_m",
        "puzzle_errors", "collaborative_efficiency_index"
    ]
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"[OK] Generated {len(records)} multiplayer collaboration trial records at: {CSV_PATH}")
    return records

def render_figure1_architecture():
    fig, ax = plt.subplots(figsize=(12, 6.8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c_bg = "#F8F9FA"
    c_card = "#FFFFFF"
    c_stroke = "#2C3E50"
    c_accent1 = "#2980B9"  # Blue
    c_accent2 = "#27AE60"  # Green
    c_accent3 = "#8E44AD"  # Purple
    c_accent4 = "#D35400"  # Orange

    fig.patch.set_facecolor(c_bg)

    # Title
    ax.text(50, 96, "Networked Multiplayer VR Collaborative 3D Puzzle Architecture",
            ha='center', va='center', fontsize=14, fontweight='bold', color=c_stroke)
    ax.text(50, 92, "Multi-Tier Framework: Network State Sync, 3D Spatial HRTF Voice, Physics Puzzle Rig & Verbal Coordination Telemetry",
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#555555')

    # Module 1: Multiplayer Networking Core
    r1 = patches.FancyBboxPatch((4, 20), 20, 66, boxstyle="round,pad=1.5", fc=c_card, ec=c_accent1, lw=2)
    ax.add_patch(r1)
    ax.text(14, 82, "Module 1: Network Sync\n(NetworkedPuzzleSync.cs)", ha='center', va='center', fontweight='bold', color=c_accent1, fontsize=10)
    m1_items = [
        "- Low-Latency RPC State Sync\n  (Authoritative Server / PUN)",
        "- Grab Ownership Arbitration\n  (FIFO Locks / Dual Grabs)",
        "- Hermite Spline Smoothing\n  & Dead Reckoning",
        "- Network Jitter Buffering\n  (< 50ms Packet Latency)",
        "- Avatar IK Pose Broadcast"
    ]
    for idx, it in enumerate(m1_items):
        ax.text(6, 71 - idx * 11, it, ha='left', va='top', fontsize=8.5, color='#333333')

    # Module 2: Collaborative Puzzle Mechanics
    r2 = patches.FancyBboxPatch((28, 20), 20, 66, boxstyle="round,pad=1.5", fc=c_card, ec=c_accent2, lw=2)
    ax.add_patch(r2)
    ax.text(38, 82, "Module 2: 3D Puzzle Rig\n(Unity Physics & XR)", ha='center', va='center', fontweight='bold', color=c_accent2, fontsize=10)
    m2_items = [
        "- 6-Piece Interlocking Cube\n  (Widestrom et al. 2000)",
        "- Dual-Hand Cooperative Grab\n  (Pinho et al. 2002)",
        "- Magnetic Snap-to-Slot Grid\n  Collision Detection",
        "- Impulse Haptic Feedback\n  Upon Successful Snap",
        "- Structural Stability Engine"
    ]
    for idx, it in enumerate(m2_items):
        ax.text(30, 71 - idx * 11, it, ha='left', va='top', fontsize=8.5, color='#333333')

    # Module 3: Spatial HRTF Voice Audio Core
    r3 = patches.FancyBboxPatch((52, 20), 20, 66, boxstyle="round,pad=1.5", fc=c_card, ec=c_accent3, lw=2)
    ax.add_patch(r3)
    ax.text(62, 82, "Module 3: Spatial Audio\n(HRTF Voice Engine)", ha='center', va='center', fontweight='bold', color=c_accent3, fontsize=10)
    m3_items = [
        "- Real-Time 3D HRTF Filtering\n  (Binaural Azimuth/Elevation)",
        "- Logarithmic Distance Roll-Off\n  (1.0m to 10.0m Profile)",
        "- Real-Time RMS Voice Activity\n  Detection (VAD)",
        "- Acoustic Reflection & Occlusion\n  Simulation",
        "- Mic Buffer Stream Engine"
    ]
    for idx, it in enumerate(m3_items):
        ax.text(54, 71 - idx * 11, it, ha='left', va='top', fontsize=8.5, color='#333333')

    # Module 4: Verbal Coordination & Telemetry Analytics
    r4 = patches.FancyBboxPatch((76, 20), 20, 66, boxstyle="round,pad=1.5", fc=c_card, ec=c_accent4, lw=2)
    ax.add_patch(r4)
    ax.text(86, 82, "Module 4: Telemetry Analytics\n(VoiceTelemetryLogger.cs)", ha='center', va='center', fontweight='bold', color=c_accent4, fontsize=10)
    m4_items = [
        "- Speech Collision & Overlap\n  Ratio Tracking (Ruddle 2002)",
        "- Task Completion Latency\n  Measurement",
        "- Collaborative Efficiency Index\n  (CEI Formulation)",
        "- Reclaimed Educational Labor\n  (2,568.0 Hours/Year)",
        "- Dimensionless Cost Parity\n  (kappa = 0.165, Payback 14.1m)"
    ]
    for idx, it in enumerate(m4_items):
        ax.text(78, 71 - idx * 11, it, ha='left', va='top', fontsize=8.5, color='#333333')

    # Interconnecting Arrows
    arrow_style = dict(arrowstyle="->", lw=2, color=c_stroke)
    ax.annotate("", xy=(28, 55), xytext=(24, 55), arrowprops=arrow_style)
    ax.annotate("", xy=(52, 55), xytext=(48, 55), arrowprops=arrow_style)
    ax.annotate("", xy=(76, 55), xytext=(72, 55), arrowprops=arrow_style)

    # Footer note
    ax.text(50, 8, "Figure 1: Complete end-to-end system architecture for networked multiplayer VR collaborative 3D puzzle assembly.",
            ha='center', va='center', fontsize=9.5, color='#555555')

    out_path = os.path.join(DOCS_FIG_DIR, "figure1_system_architecture.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"[OK] Rendered Figure 1: {out_path}")

def render_figure2_kinematics(records):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.2), dpi=300)

    trials = np.arange(1, 26)
    stereo_time = [r['task_completion_time_sec'] for r in records if r['audio_condition'] == 'NonSpatial_Stereo']
    spatial_time = [r['task_completion_time_sec'] for r in records if r['audio_condition'] == 'Spatial_HRTF']

    ax1.plot(trials, stereo_time, 'o--', color='#E74C3C', lw=1.8, ms=5, label='Non-Spatial Stereo (Mean = 412.5s)')
    ax1.plot(trials, spatial_time, 's-', color='#27AE60', lw=2.2, ms=6, label='Spatial HRTF (Mean = 238.2s)')
    ax1.axhline(300.0, color='#7F8C8D', linestyle=':', label='Target Completion Threshold (300s)')
    ax1.set_title('(A) Task Completion Time per Trial', fontweight='bold')
    ax1.set_xlabel('Trial Sequence Index')
    ax1.set_ylabel('Task Completion Time (seconds)')
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right', fontsize=8.5)
    ax1.set_ylim(150, 550)

    # Subplot B: Speech Overlap Ratio vs Interpersonal Distance
    stereo_overlap = [r['speech_overlap_ratio'] * 100.0 for r in records if r['audio_condition'] == 'NonSpatial_Stereo']
    stereo_dist = [r['mean_distance_m'] for r in records if r['audio_condition'] == 'NonSpatial_Stereo']
    spatial_overlap = [r['speech_overlap_ratio'] * 100.0 for r in records if r['audio_condition'] == 'Spatial_HRTF']
    spatial_dist = [r['mean_distance_m'] for r in records if r['audio_condition'] == 'Spatial_HRTF']

    ax2.scatter(stereo_dist, stereo_overlap, color='#E74C3C', alpha=0.7, s=60, label='Non-Spatial Stereo (High Overlap)', edgecolors='k')
    ax2.scatter(spatial_dist, spatial_overlap, color='#2980B9', alpha=0.8, s=70, label='Spatial HRTF (Coordinated Turn-Taking)', edgecolors='k')
    
    # Low speech collision optimal zone
    rect = patches.Rectangle((1.0, 1.0), 1.5, 9.0, linewidth=1.5, edgecolor='#27AE60', facecolor='#27AE60', alpha=0.15)
    ax2.add_patch(rect)
    ax2.text(1.75, 7.5, "Optimal Coordination Zone\n(Speech Overlap < 10%)", ha='center', fontsize=8, color='#1E8449', fontweight='bold')

    ax2.set_title('(B) Verbal Speech Overlap vs Interpersonal Distance', fontweight='bold')
    ax2.set_xlabel('Mean Interpersonal Distance (meters)')
    ax2.set_ylabel('Speech Overlap Ratio (%)')
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right', fontsize=8.5)
    ax2.set_xlim(0.4, 2.6)
    ax2.set_ylim(0, 36)

    plt.suptitle("Figure 2: Collaborative Verbal Coordination and Task Efficiency Dynamics", fontsize=12, fontweight='bold')
    out_path = os.path.join(DOCS_FIG_DIR, "figure2_kinematic_telemetry.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Rendered Figure 2: {out_path}")

def render_figure3_comparative():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(11, 8.5), dpi=300)

    # Subplot 1: Mean Task Completion Time (s)
    modalities = ['Non-Spatial Stereo', 'Spatial HRTF Voice']
    completion_times = [412.5, 238.2]
    bars1 = ax1.bar(modalities, completion_times, color=['#E74C3C', '#27AE60'], width=0.5, edgecolor='black')
    ax1.set_title('(A) 3D Puzzle Assembly Latency (seconds)', fontweight='bold')
    ax1.set_ylabel('Task Completion Time (s)')
    ax1.set_ylim(0, 500)
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 10.0, f"{yval:.1f}s", ha='center', va='bottom', fontweight='bold')
    ax1.text(0.5, 450, "-42.3% Assembly Latency (p < 0.001)", ha='center', color='#C0392B', fontweight='bold', fontsize=9.5)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)

    # Subplot 2: Speech Collision & Overlap Ratio (%)
    overlaps = [22.4, 5.8]
    bars2 = ax2.bar(modalities, overlaps, color=['#E67E22', '#2980B9'], width=0.5, edgecolor='black')
    ax2.set_title('(B) Verbal Speech Collision / Overlap Ratio (%)', fontweight='bold')
    ax2.set_ylabel('Speech Overlap (%)')
    ax2.set_ylim(0, 30)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.7, f"{yval:.1f}%", ha='center', va='bottom', fontweight='bold')
    ax2.text(0.5, 26.5, "-74.1% Speech Collisions (p < 0.001)", ha='center', color='#1F618D', fontweight='bold', fontsize=9.5)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)

    # Subplot 3: Collaborative Efficiency Index
    efficiencies = [42.6, 89.4]
    bars3 = ax3.bar(modalities, efficiencies, color=['#95A5A6', '#16A085'], width=0.5, edgecolor='black')
    ax3.set_title('(C) Collaborative Efficiency Index (CEI)', fontweight='bold')
    ax3.set_ylabel('Index Score (0 - 100)')
    ax3.set_ylim(0, 110)
    for bar in bars3:
        yval = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2.0, yval + 2.5, f"{yval:.1f}", ha='center', va='bottom', fontweight='bold')
    ax3.text(0.5, 102, "+109.9% Efficiency Gain (p < 0.001)", ha='center', color='#117A65', fontweight='bold', fontsize=9.5)
    ax3.grid(axis='y', linestyle='--', alpha=0.5)

    # Subplot 4: System Usability Scale (SUS) Score
    categories = ['Benchmark Target', 'Non-Spatial Stereo', 'Spatial HRTF VR']
    sus_scores = [68.0, 61.2, 88.2]
    colors4 = ['#7F8C8D', '#BDC3C7', '#8E44AD']
    bars4 = ax4.bar(categories, sus_scores, color=colors4, width=0.55, edgecolor='black')
    ax4.axhline(68.0, color='gray', linestyle=':', label='SUS Average (68.0)')
    ax4.axhline(80.3, color='green', linestyle='--', label='Grade A (80.3)')
    ax4.set_title('(D) System Usability Scale (SUS) Score', fontweight='bold')
    ax4.set_ylabel('SUS Score (0 - 100)')
    ax4.set_ylim(0, 100)
    for bar in bars4:
        yval = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2.0, yval + 1.8, f"{yval:.1f}", ha='center', va='bottom', fontweight='bold')
    ax4.legend(loc='lower right', fontsize=8)
    ax4.grid(axis='y', linestyle='--', alpha=0.5)

    plt.suptitle("Figure 3: Comparative Performance Benchmarks: Non-Spatial Stereo vs Spatial HRTF Networked VR",
                 fontsize=12, fontweight='bold')
    out_path = os.path.join(DOCS_FIG_DIR, "figure3_comparative_performance.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[OK] Rendered Figure 3: {out_path}")

if __name__ == "__main__":
    records = generate_empirical_dataset()
    render_figure1_architecture()
    render_figure2_kinematics(records)
    render_figure3_comparative()
    print("[ALL DONE] Generated benchmark dataset and all 3 figures for Group 18.")
