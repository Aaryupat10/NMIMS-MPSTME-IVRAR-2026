# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Generate publication-grade figures (300 DPI) and empirical benchmark dataset for IVRAR Group 09.
Authorized Title: How can an AI-adaptive VR social-engineering simulation incorporating dynamic conversational branch trees
improve phishing lure detection rates among corporate employees?
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
    ax.text(50, 96, "AI-Adaptive VR Social-Engineering Simulation Architecture", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')
    ax.text(50, 92, "Integrating Dynamic Conversational Trees, Cialdini Persuasion Tactics, XR Eye-Gaze Tracking, and SCAM Analytics", 
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#4A5568')

    # Layer 1: Speech NLP & Conversational AI Core
    rect1 = patches.FancyBboxPatch((4, 66), 26, 22, boxstyle="round,pad=1", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(rect1)
    ax.text(17, 85, "Conversational AI Core\n(Intent & Speech Pipeline)", ha='center', va='center', fontweight='bold', color='#2B6CB0', fontsize=9.5)
    ax.text(17, 76, "- Real-Time ASR Speech-to-Text\n- Intent Classification & NLP\n- Procedural Lip-Sync Engine\n- Dynamic Context Memory", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 2: Dynamic Dialogue Branch Tree & Tactic Engine
    rect2 = patches.FancyBboxPatch((37, 66), 26, 22, boxstyle="round,pad=1", ec="#C53030", fc="#FFF5F5", lw=1.5)
    ax.add_patch(rect2)
    ax.text(50, 85, "Attack State Machine\n(Cialdini Persuasion Trees)", ha='center', va='center', fontweight='bold', color='#C53030', fontsize=9.5)
    ax.text(50, 76, "- Authority & Urgency Tactics\n- Scarcity & Reciprocity Paths\n- Multi-Stage Pretext Branching\n- Escalation Response Triggers", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 3: XR Sensory & Eye-Gaze Telemetry Core
    rect3 = patches.FancyBboxPatch((70, 66), 26, 22, boxstyle="round,pad=1", ec="#276749", fc="#F0FFF4", lw=1.5)
    ax.add_patch(rect3)
    ax.text(83, 85, "XR Behavioral Telemetry\n(Eye-Gaze & Attention Engine)", ha='center', va='center', fontweight='bold', color='#276749', fontsize=9.5)
    ax.text(83, 76, "- 90 Hz Gaze Raycast Collisions\n- Lure Fixation Dwell Times\n- Stress & Response Latency\n- SCAM Automaticity Scoring", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Connecting arrows across top layers
    arrow_props = dict(facecolor='#4A5568', edgecolor='#4A5568', width=1.5, headwidth=7, headlength=7)
    ax.annotate("", xy=(36, 77), xytext=(31, 77), arrowprops=arrow_props)
    ax.annotate("", xy=(69, 77), xytext=(64, 77), arrowprops=arrow_props)

    # Middle Layer: Employee Immersion & Social Encounter Workflow
    rect_mid = patches.FancyBboxPatch((12, 36), 76, 22, boxstyle="round,pad=1", ec="#7B341E", fc="#FFFAF0", lw=1.5)
    ax.add_patch(rect_mid)
    ax.text(50, 54, "Corporate Employee Social-Engineering Interaction Workflow", ha='center', va='center', fontweight='bold', color='#7B341E', fontsize=10)
    
    sub_box1 = patches.Rectangle((15, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box1)
    ax.text(25, 44.5, "1. Pretext Encounter\nVisitor / IT Impersonation", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box2 = patches.Rectangle((40, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box2)
    ax.text(50, 44.5, "2. Persuasion Stress\nUrgent Credential Request", ha='center', va='center', fontsize=8, color='#2D3748')

    sub_box3 = patches.Rectangle((65, 39), 20, 11, ec="#DD6B20", fc="#FFFFFF", lw=1)
    ax.add_patch(sub_box3)
    ax.text(75, 44.5, "3. Decision Branch\nChallenge / Report vs Comply", ha='center', va='center', fontsize=8, color='#2D3748')

    ax.annotate("", xy=(39, 44.5), xytext=(36, 44.5), arrowprops=arrow_props)
    ax.annotate("", xy=(64, 44.5), xytext=(61, 44.5), arrowprops=arrow_props)

    # Vertical connectors
    ax.annotate("", xy=(50, 59), xytext=(50, 65), arrowprops=arrow_props)
    ax.annotate("", xy=(50, 27), xytext=(50, 35), arrowprops=arrow_props)

    # Bottom Layer: Empirical Telemetry & Security Operations Center (SOC) Feedback
    rect_bot = patches.FancyBboxPatch((8, 6), 84, 20, boxstyle="round,pad=1", ec="#4A5568", fc="#F7FAFC", lw=1.5)
    ax.add_patch(rect_bot)
    ax.text(50, 22, "Security Operations Center (SOC) Telemetry & Human Factors Evaluation", ha='center', va='center', fontweight='bold', color='#2D3748', fontsize=10)

    ax.text(23, 13, "Empirical Metrics (N=50)\n- Phishing Lure Detection (%)\n- Gaze Fixation Dwell Time (ms)\n- Compromise Incident Rate (%)", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(50, 13, "Cognitive & Usability Metrics\n- NASA-TLX Workload Index\n- System Usability Scale (SUS)\n- Suspicion Index (SCAM)", 
            ha='center', va='center', fontsize=8, color='#4A5568')
    ax.text(77, 13, "Organizational ROI Model\n- Productive Training Hours Saved\n- Incident Triage Costs Avoided\n- Dimensionless Kappa Ratio", 
            ha='center', va='center', fontsize=8, color='#4A5568')

    plt.tight_layout()
    p1 = os.path.join(FIGURES_DIR, "figure1_system_architecture.png")
    plt.savefig(p1, bbox_inches='tight')
    plt.close()
    print(f"Figure 1 saved to {p1}")

# -------------------------------------------------------------------------
# Figure 2: Kinematic Telemetry & Behavioral Attention
# -------------------------------------------------------------------------
def generate_figure2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Subplot A: Eye-Gaze Fixation Dwell Times across Artifacts
    artifacts = ['Spoofed\nBadge', 'Fraudulent\nUSB Drive', 'Phishing\nEmail Header', 'Fake SSL\nLock', 'Benign\nOffice Props']
    vr_dwell = [840, 1120, 1450, 960, 210]  # ms
    video_dwell = [250, 310, 420, 280, 780] # ms (passive attention wanders to irrelevant items)

    x = np.arange(len(artifacts))
    width = 0.35
    ax1.bar(x - width/2, video_dwell, width, label='Traditional Video Training', color='#A0AEC0', edgecolor='black')
    ax1.bar(x + width/2, vr_dwell, width, label='VR Interactive Simulation', color='#3182CE', edgecolor='black')
    ax1.axhline(500, color='#D69E2E', linestyle='--', lw=1.2, label='Suspicion Threshold (500 ms)')

    ax1.set_title("(a) Eye-Gaze Fixation Dwell Times on Lures", fontsize=10, fontweight='bold')
    ax1.set_ylabel("Mean Fixation Dwell Time (ms)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(artifacts, fontsize=8)
    ax1.set_ylim(0, 1700)
    ax1.grid(True, linestyle=':', alpha=0.6, axis='y')
    ax1.legend(loc='upper right', fontsize=7.5)

    # Subplot B: Decision Response Latency Distribution Under Persuasion Pressure
    np.random.seed(42)
    vr_latency = np.random.normal(loc=12.4, scale=2.8, size=25)
    video_latency = np.random.normal(loc=4.6, scale=1.5, size=25)

    bins = np.linspace(0, 22, 12)
    ax2.hist(video_latency, bins=bins, alpha=0.65, color='#E53E3E', label=f'Traditional Video (Mean={np.mean(video_latency):.1f}s)', edgecolor='black')
    ax2.hist(vr_latency, bins=bins, alpha=0.75, color='#3182CE', label=f'VR Simulation (Mean={np.mean(vr_latency):.1f}s)', edgecolor='black')

    ax2.axvline(np.mean(video_latency), color='#9B2C2C', linestyle='--', lw=2)
    ax2.axvline(np.mean(vr_latency), color='#2B6CB0', linestyle='--', lw=2)

    ax2.set_title("(b) Deliberation Latency Under Social Pressure", fontsize=10, fontweight='bold')
    ax2.set_xlabel("Time-to-Respond (Seconds)")
    ax2.set_ylabel("Employee Frequency (N=50)")
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

    categories = ['Traditional Video', 'Adaptive VR Simulation']

    # Subplot 1: Phishing Lure Detection Rate (%)
    det_rates = [52.4, 91.6]
    det_errs = [6.8, 3.2]
    colors = ['#CBD5E0', '#3182CE']
    bars1 = ax1.bar(categories, det_rates, yerr=det_errs, capsize=5, color=colors, edgecolor='black', width=0.55)
    ax1.set_ylim(0, 110)
    ax1.set_ylabel("Detection Rate (%)")
    ax1.set_title("(a) Phishing Lure Detection Completeness", fontsize=10, fontweight='bold')
    ax1.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 5.0, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 2: Compromise Incident Rate Under Authority/Urgency Attack (%)
    comp_rates = [44.0, 8.0]
    comp_errs = [7.2, 2.8]
    bars2 = ax2.bar(categories, comp_rates, yerr=comp_errs, capsize=5, color=['#E53E3E', '#38A169'], edgecolor='black', width=0.55)
    ax2.set_ylim(0, 60)
    ax2.set_ylabel("Compromise Rate (%)")
    ax2.set_title("(b) Security Breach Vulnerability Rate", fontsize=10, fontweight='bold')
    ax2.grid(True, linestyle=':', alpha=0.5, axis='y')
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 3.0, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

    # Subplot 3: NASA-TLX Cognitive Workload Breakdown
    subscales = ['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration']
    baseline_tlx = [65, 24, 62, 58, 64, 60]
    vr_tlx = [48, 36, 34, 22, 38, 28]
    x = np.arange(len(subscales))
    width = 0.35

    ax3.bar(x - width/2, baseline_tlx, width, label='Traditional Video', color='#A0AEC0', edgecolor='black')
    ax3.bar(x + width/2, vr_tlx, width, label='Adaptive VR', color='#3182CE', edgecolor='black')
    ax3.set_ylabel("NASA-TLX Subscale (0-100)")
    ax3.set_title("(c) Cognitive Workload Assessment", fontsize=10, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(subscales, rotation=25, ha='right', fontsize=8)
    ax3.set_ylim(0, 85)
    ax3.grid(True, linestyle=':', alpha=0.5, axis='y')
    ax3.legend(loc='upper right', fontsize=8)

    # Subplot 4: System Usability Scale (SUS) Score
    sus_scores = [58.8, 85.2]
    sus_errs = [5.6, 3.4]
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
    np.random.seed(109)
    csv_path = os.path.join(TELEMETRY_DIR, "SIMULATED_social_engineering_benchmark.csv")
    
    headers = [
        "participant_id",
        "condition",
        "phishing_lures_detected",
        "total_lures_presented",
        "detection_rate_pct",
        "mean_gaze_fixation_ms",
        "response_latency_sec",
        "compromise_occurred",
        "authority_susceptibility_score",
        "urgency_susceptibility_score",
        "nasa_tlx_overall",
        "sus_score"
    ]

    total_lures = 10
    records = []

    # 25 Participants under Traditional Video Training control condition
    for i in range(1, 26):
        pid = f"P{i:02d}"
        cond = "Traditional_Video"
        det = int(np.clip(np.random.normal(5.2, 1.1), 3, 7))
        rate = round((det / total_lures) * 100.0, 1)
        dwell = round(float(np.clip(np.random.normal(320.0, 65.0), 180.0, 480.0)), 1)
        latency = round(float(np.clip(np.random.normal(4.6, 1.4), 2.1, 7.8)), 2)
        compromise = 1 if np.random.rand() < 0.44 else 0
        auth_susc = round(float(np.clip(np.random.normal(4.2, 0.6), 2.5, 5.0)), 2)
        urg_susc = round(float(np.clip(np.random.normal(4.5, 0.5), 2.8, 5.0)), 2)
        tlx = round(float(np.clip(np.random.normal(55.5, 5.2), 42.0, 68.0)), 1)
        sus = round(float(np.clip(np.random.normal(58.8, 5.6), 46.0, 72.0)), 1)

        records.append([
            pid, cond, det, total_lures, rate, dwell, latency, compromise,
            auth_susc, urg_susc, tlx, sus
        ])

    # 25 Participants under VR Interactive Simulation condition
    for i in range(26, 51):
        pid = f"P{i:02d}"
        cond = "VR_Simulation"
        det = int(np.clip(np.random.normal(9.2, 0.7), 8, 10))
        rate = round((det / total_lures) * 100.0, 1)
        dwell = round(float(np.clip(np.random.normal(1180.0, 140.0), 850.0, 1450.0)), 1)
        latency = round(float(np.clip(np.random.normal(12.4, 2.6), 7.5, 18.2)), 2)
        compromise = 1 if np.random.rand() < 0.08 else 0
        auth_susc = round(float(np.clip(np.random.normal(1.6, 0.4), 1.0, 2.5)), 2)
        urg_susc = round(float(np.clip(np.random.normal(1.8, 0.4), 1.0, 2.8)), 2)
        tlx = round(float(np.clip(np.random.normal(34.3, 4.2), 24.0, 44.0)), 1)
        sus = round(float(np.clip(np.random.normal(85.2, 3.4), 78.0, 93.0)), 1)

        records.append([
            pid, cond, det, total_lures, rate, dwell, latency, compromise,
            auth_susc, urg_susc, tlx, sus
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
