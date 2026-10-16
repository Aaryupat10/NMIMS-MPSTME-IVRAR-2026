# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
"""
Generate publication-grade figures (300 DPI) and empirical benchmark dataset for IVRAR Group 04.
Authorized Title: To what extent can a VR cybersecurity escape room reduce credential leakage
and unauthorized physical access errors among university students exposed to simulated social-engineering attacks?
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
    ax.text(50, 96, "VR Cybersecurity Escape Room Simulation Architecture", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A202C')
    ax.text(50, 92, "Integrating NIST SP 800-53 Physical Attack Vectors, OpenXR HMDs, and Hake Gain Telemetry", 
            ha='center', va='center', fontsize=9, fontstyle='italic', color='#4A5568')

    # Layer 1: Hardware & XR Input Layer
    rect1 = patches.FancyBboxPatch((4, 66), 26, 22, boxstyle="round,pad=1", ec="#2B6CB0", fc="#EBF8FF", lw=1.5)
    ax.add_patch(rect1)
    ax.text(17, 85, "XR Interaction Layer\n(OpenXR / Unity 2022.3)", ha='center', va='center', fontweight='bold', color='#2B6CB0', fontsize=9.5)
    ax.text(17, 76, "- Headset 6-DoF Tracking\n- Hand Physics Controller Grabs\n- RFID Badge Tap Physics\n- Virtual Keypad Gaze Shield", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 2: Social Engineering Attack Engine
    rect2 = patches.FancyBboxPatch((37, 66), 26, 22, boxstyle="round,pad=1", ec="#C53030", fc="#FFF5F5", lw=1.5)
    ax.add_patch(rect2)
    ax.text(50, 85, "Social Engineering Attack Engine\n(NIST SP 800-53 PE/AT)", ha='center', va='center', fontweight='bold', color='#C53030', fontsize=9.5)
    ax.text(50, 76, "- Tailgating Persona NPC Bot\n- Malicious Baiting USB Drops\n- Shoulder Surfing Observation\n- Pretexting Voice Phone Calls", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Layer 3: Escape Room Logic & State Machine
    rect3 = patches.FancyBboxPatch((70, 66), 26, 22, boxstyle="round,pad=1", ec="#276749", fc="#F0FFF4", lw=1.5)
    ax.add_patch(rect3)
    ax.text(83, 85, "Escape Room Puzzle Engine\n(Finite State Machine)", ha='center', va='center', fontweight='bold', color='#276749', fontsize=9.5)
    ax.text(83, 76, "- Reception Checkpoint State\n- Open Office Shoulder Surf\n- Server Room 2FA Access\n- Credential Extraction Trap", 
            ha='center', va='center', fontsize=8, color='#2D3748')

    # Connecting arrows downward
    ax.annotate("", xy=(17, 48), xytext=(17, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))
    ax.annotate("", xy=(50, 48), xytext=(50, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))
    ax.annotate("", xy=(83, 48), xytext=(83, 66), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))

    # Middle Layer: Multi-Zone Escape Environment
    rect_env = patches.FancyBboxPatch((10, 30), 80, 18, boxstyle="round,pad=1", ec="#4A5568", fc="#EDF2F7", lw=1.5)
    ax.add_patch(rect_env)
    ax.text(50, 43, "Multi-Zone Enterprise Facility Environment (OWASP Physical Penetration Model)", 
            ha='center', va='center', fontweight='bold', color='#1A202C', fontsize=10)
    ax.text(50, 36, "Zone 1: Perimeter Reception & Turnstiles | Zone 2: Open Workstation Floor | Zone 3: Secure Data Center Vault\nVulnerability Targets: Badge Tailgating, Dropped USB Drives, Sticky-Note Credential Leaks", 
            ha='center', va='center', fontsize=8.5, color='#4A5568')

    # Connecting arrow to telemetry
    ax.annotate("", xy=(50, 18), xytext=(50, 30), arrowprops=dict(arrowstyle="->", lw=1.8, color="#4A5568"))

    # Bottom Layer: Telemetry & Evaluation Analysis
    rect_tel = patches.FancyBboxPatch((15, 3), 70, 15, boxstyle="round,pad=1", ec="#6B46C1", fc="#FAF5FF", lw=1.5)
    ax.add_patch(rect_tel)
    ax.text(50, 14, "90 Hz Real-Time Security Telemetry & Analytics Pipeline", 
            ha='center', va='center', fontweight='bold', color='#6B46C1', fontsize=9.5)
    ax.text(50, 8, "Gaze Fixation Tracker | USB Interaction Logger | Tailgate Intercept Timer | Hake Normalized Gain Engine", 
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

    # (a) Hake Normalized Learning Gain (g) Pre vs Post Test
    pre_scores = np.random.normal(42.5, 7.5, 50)
    pre_scores = np.clip(pre_scores, 20, 65)
    post_scores = pre_scores + (100 - pre_scores) * np.random.normal(0.68, 0.08, 50)
    post_scores = np.clip(post_scores, 70, 98)
    hake_g = (post_scores - pre_scores) / (100.0 - pre_scores)

    axs[0, 0].hist(hake_g, bins=12, color='#3182CE', edgecolor='#1A365D', alpha=0.85)
    axs[0, 0].axvline(0.3, color='#E53E3E', linestyle='--', label='Low Gain Threshold (g < 0.3)')
    axs[0, 0].axvline(0.7, color='#38A169', linestyle='--', label='High Gain Threshold (g > 0.7)')
    axs[0, 0].set_title("(a) Hake's Normalized Learning Gain Distribution (N=50)")
    axs[0, 0].set_xlabel("Normalized Gain Index (g)")
    axs[0, 0].set_ylabel("Number of Participants")
    axs[0, 0].legend()
    axs[0, 0].grid(axis='y', linestyle='--', alpha=0.5)

    # (b) Vulnerability Rate Over Repeated Attempts
    attempts = np.arange(1, 6)
    tailgate_vuln = [78.2, 52.4, 31.0, 18.5, 11.2]
    usb_vuln = [84.6, 46.2, 22.8, 12.4, 6.5]
    shoulder_vuln = [68.4, 42.1, 24.5, 14.2, 8.1]

    axs[0, 1].plot(attempts, tailgate_vuln, 'o-', color='#C53030', lw=1.8, label='Badge Tailgating Vulnerability')
    axs[0, 1].plot(attempts, usb_vuln, 's--', color='#D69E2E', lw=1.8, label='Malicious USB Insertion')
    axs[0, 1].plot(attempts, shoulder_vuln, '^-.', color='#3182CE', lw=1.8, label='Shoulder Surfing Exposure')
    axs[0, 1].set_title("(b) Vulnerability Rate vs Escape Room Iterations")
    axs[0, 1].set_xlabel("Escape Room Practice Iteration")
    axs[0, 1].set_ylabel("Vulnerability Rate (%)")
    axs[0, 1].legend()
    axs[0, 1].grid(True, linestyle='--', alpha=0.5)

    # (c) Shoulder Surfing Gaze Fixation Duration on PIN Keypad
    categories = ['Unshielded Keypad', 'Body-Shielded Keypad', 'Randomized Digit Scramble']
    gaze_time = [4.8, 1.6, 0.9]
    gaze_err = [0.45, 0.22, 0.12]
    axs[1, 0].bar(categories, gaze_time, yerr=gaze_err, capsize=4, color=['#E53E3E', '#ED8936', '#38A169'], edgecolor='#1A202C', alpha=0.85)
    axs[1, 0].set_title("(c) Adversary Gaze Fixation on Authentication Keypad")
    axs[1, 0].set_ylabel("Gaze Fixation Duration (s)")
    axs[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

    # (d) Escape Room Task Completion Latency
    zones = ['Zone 1: Reception', 'Zone 2: Workstation', 'Zone 3: Server Vault', 'Full Room Exit']
    completion_time = [4.2, 6.8, 8.5, 19.5]
    completion_std = [0.6, 0.9, 1.2, 1.8]
    axs[1, 1].barh(zones, completion_time, xerr=completion_std, capsize=4, color='#4FD1C5', edgecolor='#234E52', alpha=0.85)
    axs[1, 1].set_title("(d) Mean Escape Room Task Completion Latency")
    axs[1, 1].set_xlabel("Elapsed Time (minutes)")
    axs[1, 1].grid(axis='x', linestyle='--', alpha=0.5)

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

    modalities = ['Traditional\nSlide Deck', '2D Desktop\nWeb Game', 'Immersive VR\nEscape Room']
    colors = ['#E53E3E', '#ED8936', '#38A169']

    # (a) Tailgating Allowance Error Rate (%)
    tailgate_means = [64.2, 42.8, 11.5]
    tailgate_stds = [6.5, 5.1, 2.4]
    axs[0].bar(modalities, tailgate_means, yerr=tailgate_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[0].set_title("(a) Tailgating Allowance Error Rate (%)")
    axs[0].set_ylabel("Error Rate (%)")
    axs[0].set_ylim(0, 80)
    axs[0].grid(axis='y', linestyle='--', alpha=0.5)
    axs[0].text(2, 20, "-82.1%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    # (b) Malicious USB Insertion Rate (%)
    usb_means = [72.0, 48.5, 8.2]
    usb_stds = [7.2, 5.8, 2.1]
    axs[1].bar(modalities, usb_means, yerr=usb_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[1].set_title("(b) Malicious USB Insertion Rate (%)")
    axs[1].set_ylabel("Baiting Compromise Rate (%)")
    axs[1].set_ylim(0, 90)
    axs[1].grid(axis='y', linestyle='--', alpha=0.5)
    axs[1].text(2, 16, "-88.6%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    # (c) Hake Normalized Learning Gain (g)
    hake_means = [0.22, 0.44, 0.74]
    hake_stds = [0.05, 0.06, 0.07]
    axs[2].bar(modalities, hake_means, yerr=hake_stds, capsize=5, color=colors, edgecolor='#1A202C', alpha=0.85)
    axs[2].set_title("(c) Hake's Normalized Gain (g)")
    axs[2].set_ylabel("Normalized Learning Gain")
    axs[2].set_ylim(0, 1.0)
    axs[2].grid(axis='y', linestyle='--', alpha=0.5)
    axs[2].text(2, 0.84, "+236.4%\n(p < 0.001)", ha='center', fontweight='bold', color='#22543D', fontsize=8.5)

    plt.tight_layout()
    fig3_path = os.path.join(FIGURES_DIR, "figure3_comparative_performance.png")
    plt.savefig(fig3_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generated: {fig3_path}")

# -------------------------------------------------------------------------
# Benchmark Dataset Generation (N = 50 trials)
# -------------------------------------------------------------------------
def generate_benchmark_dataset():
    np.random.seed(104)
    n_samples = 50

    fieldnames = [
        "trial_id",
        "participant_id",
        "training_modality",
        "pre_test_score_pct",
        "post_test_score_pct",
        "hake_gain_g",
        "tailgating_error_flag",
        "usb_insertion_flag",
        "shoulder_surf_gaze_s",
        "escape_completion_time_min",
        "nasa_tlx_workload_score",
        "sus_usability_score"
    ]

    csv_path = os.path.join(TELEMETRY_DIR, "SIMULATED_cybersecurity_escape_benchmark.csv")

    rows = []
    for i in range(n_samples):
        trial_id = f"CYBER-TR-{i+1:03d}"
        part_id = f"STUDENT-P{i+1:03d}"
        r_val = np.random.rand()
        if r_val < 0.25:
            mod = "Traditional_Slide_Deck"
            pre = np.random.normal(41.0, 6.0)
            post = pre + (100.0 - pre) * np.random.normal(0.22, 0.05)
            tg_err = 1 if np.random.rand() < 0.65 else 0
            usb_ins = 1 if np.random.rand() < 0.72 else 0
            gaze = np.random.normal(4.8, 0.5)
            comp_time = np.random.normal(26.0, 3.2)
            tlx = np.random.normal(68.5, 5.0)
            sus = np.random.normal(54.0, 6.2)
        elif r_val < 0.60:
            mod = "Desktop_2D_Web_Game"
            pre = np.random.normal(43.0, 5.5)
            post = pre + (100.0 - pre) * np.random.normal(0.45, 0.06)
            tg_err = 1 if np.random.rand() < 0.42 else 0
            usb_ins = 1 if np.random.rand() < 0.48 else 0
            gaze = np.random.normal(3.2, 0.4)
            comp_time = np.random.normal(22.5, 2.5)
            tlx = np.random.normal(55.0, 4.5)
            sus = np.random.normal(68.5, 5.5)
        else:
            mod = "Immersive_VR_Escape_Room"
            pre = np.random.normal(42.5, 5.8)
            post = pre + (100.0 - pre) * np.random.normal(0.74, 0.06)
            tg_err = 1 if np.random.rand() < 0.12 else 0
            usb_ins = 1 if np.random.rand() < 0.08 else 0
            gaze = np.random.normal(1.2, 0.25)
            comp_time = np.random.normal(18.2, 1.8)
            tlx = np.random.normal(36.0, 3.5)
            sus = np.random.normal(86.5, 4.2)

        pre = np.clip(pre, 15.0, 65.0)
        post = np.clip(post, pre + 2.0, 100.0)
        g_val = (post - pre) / (100.0 - pre)

        row = {
            "trial_id": trial_id,
            "participant_id": part_id,
            "training_modality": mod,
            "pre_test_score_pct": round(float(pre), 1),
            "post_test_score_pct": round(float(post), 1),
            "hake_gain_g": round(float(g_val), 3),
            "tailgating_error_flag": int(tg_err),
            "usb_insertion_flag": int(usb_ins),
            "shoulder_surf_gaze_s": round(float(max(0.2, gaze)), 2),
            "escape_completion_time_min": round(float(max(5.0, comp_time)), 1),
            "nasa_tlx_workload_score": round(float(min(100.0, max(0.0, tlx))), 1),
            "sus_usability_score": round(float(min(100.0, max(0.0, sus))), 1)
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
    print("[SUCCESS] All figures and benchmark telemetry generated for IVRAR Group 04.")
