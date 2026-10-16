# -*- coding: utf-8 -*-
"""
IVRAR 2026 monorepo: capstone finalisation (operations 1-3), Dr. Sunny Nanade, 16-Oct-2026.

  1. Data-integrity sanitisation in all 18 group folders
     a) git mv the 36 known synthetic starter CSVs (*benchmark*.csv, sample_experiment_data.csv) -> SIMULATED_<name>
        and update references in that group's folder. Where a Unity C# logger used the same file name for
        its own (real) output, the logger and the docs describing it are pointed to <name>_real_trials.csv
        instead, so real trial data is never labelled SIMULATED.
     b) add a NOTICE TO STUDENTS header to generate_paper_figures.py (and to any other telemetry
        script that generates synthetic datasets)
     c) add docs/figures/README.md marking the starter figures as synthetic
  2. Replace GRADING_RUBRIC_AND_EVALUATION_POLICY.md with the 20-mark capstone scheme
  3. Copy each group's pre-filled IVRAR_Group_XX_Technical_Dossier.docx into Group_XX_*/docs/,
     add docs/README.md with the submission note, and copy the showcase guide PDF to the repo root

Safe to run more than once (idempotent). It stages its changes with `git add` but does NOT commit or push.

Usage (from anywhere):
    python scripts/apply_capstone_update_2026_10.py ["D:\\MPSTME\\AY 26-27 Odd Sem ICA\\IVRAR\\Student_Submission_Packs"]
Then review:   git status   /   git diff --cached --stat
Then:          git commit -m "chore(capstone): sanitise simulated data, 20-mark policy, stage dossiers"
               git push origin main
"""
import glob, os, re, shutil, subprocess, sys, py_compile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS = sys.argv[1] if len(sys.argv) > 1 else r"D:\MPSTME\AY 26-27 Odd Sem ICA\IVRAR\Student_Submission_Packs"
GUIDE_PDF = "IVRAR_LinkedIn_and_GitHub_Showcase_Guide.pdf"
TEXT_EXT = {".py", ".md", ".json", ".html", ".txt", ".cs", ".yml", ".yaml"}
MARK = "NOTICE TO STUDENTS"

# The exact starter files that contain synthetic data (as committed in 28c20bd). Only these are ever
# renamed, so re-running this script can never touch a real trial file a student adds later.
KNOWN_SIMULATED = {
    "acoustic_benchmark_data.csv", "acrophobia_vret_benchmark.csv", "ar_navigation_benchmark.csv",
    "biometric_authentication_benchmark.csv", "campus_orientation_benchmark.csv", "cybersecurity_escape_benchmark.csv",
    "evacuation_training_benchmark.csv", "forensic_reconstruction_benchmark.csv", "hand_tracking_benchmark.csv",
    "kiosk_handoff_benchmark.csv", "mci_triage_benchmark.csv", "multiplayer_collaboration_benchmark.csv",
    "phishing_simulation_benchmark.csv", "rover_teleoperation_benchmark.csv", "security_audit_benchmark.csv",
    "security_training_benchmark.csv", "social_engineering_benchmark.csv", "spatial_nlp_benchmark.csv",
    "sample_experiment_data.csv"}

def real_name(n):
    """Name for REAL trial data written by a Unity C# logger (kept distinct from the simulated file)."""
    return n.replace("_benchmark_data.csv", "_real_trials.csv").replace("_benchmark.csv", "_real_trials.csv")

NOTICE = '''# =====================================================================================
# NOTICE TO STUDENTS:
# The functions in this script generate SYNTHETIC/SIMULATED reference data for demonstration purposes only.
# Per Section 4 of your IVRAR Technical Dossier, you MUST conduct real human user trials (N >= 10),
# log actual telemetry/SUS data, and replace simulated numbers with your genuine experimental results.
# Submitting simulated data as real experimental findings violates NMIMS academic integrity policies.
# =====================================================================================
'''

FIG_README = """# Starter figures: NOT experimental results

> **Reference Starter Figure (Built on Synthetic Data). Must be re-plotted with genuine experimental trial data.**

The `figure*.png` files in this folder were produced by `telemetry/generate_paper_figures.py` from
**simulated** numbers (see `telemetry/SIMULATED_*.csv`). They only show the expected layout of your plots.

Before you use any figure in your dossier, LinkedIn video or paper:
1. Run your real user trials (N ≥ 10) and save the raw CSV in `telemetry/`.
2. Re-plot every figure from **your** raw CSV.
3. Replace or delete these starter figures.

Files in this folder that are starter figures: {files}
"""

DOCS_NOTE = "Before submitting, complete all 6 sections of `{dossier}`, export to PDF, and commit BOTH the completed .docx and .pdf to this folder."

DOCS_README = """# docs/: {group}

{note}

| File | What it is |
|---|---|
| `{dossier}` | Your pre-filled Technical Dossier. Fill it in **Microsoft Word** using the "Select ▾" drop-downs and "type here" fields. |
| `{pdf}` | The PDF export of your completed dossier (you add this). The same PDF is turned in on MS Teams by **every** member. |
| `figures/` | Starter figures built on **synthetic** data. Re-plot them from your real trial CSV. |
| `TEAM_ROSTER.json` | Your roster, roles and GitHub usernames. |

**Due: Monday, 26-Oct-2026, 23:59 IST · Studio Showcase, Expo & Viva Voce: Saturday, 31-Oct-2026**
Guide: [`/IVRAR_LinkedIn_and_GitHub_Showcase_Guide.pdf`](../../IVRAR_LinkedIn_and_GitHub_Showcase_Guide.pdf)
"""

RUBRIC = r"""# IVRAR (702TG0C003) Capstone: Grading Rubric & Evaluation Policy
**SVKM's NMIMS · MPSTME Mumbai · AY 2026–27 Odd Semester · Dr. Sunny Nanade**

> This document replaces the earlier 100-mark, 4-milestone scheme. The capstone is an **ICA component worth 20 marks**.

| Item | Detail |
|---|---|
| **Total Capstone Marks** | **20 Marks** |
| **Submission Due Date** | **Monday, 26-Oct-2026, 23:59 IST** |
| **Studio Showcase, Expo & Viva Voce** | **Saturday, 31-Oct-2026** |
| What you submit | (1) Your group's Technical Dossier as PDF on MS Teams, turned in by **every** member · (2) the filled `.docx` **and** `.pdf` committed to `Group_XX_*/docs/` · (3) your GitHub Release `group-XX-v1.0` · (4) your LinkedIn video URL in dossier Section 5 |

---

## Component 1: SBL Studio Project (10 Marks)
Evaluated on:
- **Unity scene composition**: a working XR scene that addresses your authorised Aalborg question.
- **C# script implementation**: your state machine and telemetry logging (dossier Section 2, including the honest script-authorship table).
- **Git LFS compliance**: binary assets tracked by LFS; no builds committed to Git history.
- **Commit dispersion across all group members**: every member commits their own work from their own GitHub account. Per-member commits are checked against dossier Section 3.2.
- **GitHub Release** tagged `group-XX-v1.0` with a runnable `.apk` (Quest / Android) or `.exe` (PCVR).

## Component 2: DBL Usability Case Study (5 Marks)
Evaluated on:
- **Section 4 empirical data pack** of the Technical Dossier.
- **Genuine human user trials ($N \ge 10$)** with voluntary, consenting adult participants.
- **System Usability Scale (SUS) / NASA-TLX** cognitive workload profiling (or a latency / frame-rate profile where the research question is about system performance).
- **Raw CSV trial data** committed to `Group_XX_*/telemetry/`, with plots that re-generate from it.

> Files named `SIMULATED_*` and the starter figures in `docs/figures/` contain **synthetic** data for demonstration only. Reporting simulated numbers as human trial results is data fabrication and scores **zero** for this component.

## Component 3: Studio Showcase & Viva Voce (5 Marks)
Evaluated on:
- **Section 5 public LinkedIn video showcase (3–4 minutes)** showing the running build, real user-testing data and each member's reflection.
- **Verified peer reviews** of the two assigned groups (dossier Section 5.2).
- **Unassisted individual viva voce defence** during the Expo on **Saturday, 31-Oct-2026**. Each member is questioned on their own role and code and on the project as a whole.

---

## Mandatory Individual Turn-in Rule
The work is collaborative, but marks are entered **per student** in the NMIMS Examination Portal.
**Every member must open the MS Teams assignment, attach the group's final PDF dossier, and click "Turn in" individually.**
A student who does not turn in cannot be awarded capstone marks, even if teammates have submitted.

## Integrity Safeguards
1. **Attribution:** individual contributions must match the git history and `TEAM_ROSTER.json`, and be defended in the viva.
2. **Evidence authenticity:** every factual claim and citation must be verified at its primary source (dossier Section 1.1). Fabricated citations or hallucinated DOIs score zero for the component in which they appear.
3. **AI use:** permitted, but must be logged in dossier Section 5.1. Undisclosed AI-generated content is treated as an integrity breach.
4. **Human participants:** written consent, anonymised IDs (P01, P02…), no personal data in the repository.
5. **Zero Currency Rule (retained from the earlier policy):** submissions must express cost comparisons as dimensionless cost-parity ratios, not raw monetary amounts; non-compliant work is returned for correction.
"""

def git(*args, check=True):
    return subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True, check=check)

def read(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()

def write(path, text, like=None):
    """Write text, keeping the line-ending style of `like` (or of the existing file)."""
    ref = like if like is not None else (read(path) if os.path.exists(path) else "")
    crlf = "\r\n" in ref or (not ref and os.name == "nt")
    text = text.replace("\r\n", "\n")
    if crlf:
        text = text.replace("\n", "\r\n")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

touched, renamed, headers, compiled_bad, real_out = set(), [], [], [], set()

def main():
    if not os.path.isdir(PACKS):
        sys.exit(f"Submission packs folder not found: {PACKS}")
    groups = sorted(d for d in glob.glob(os.path.join(ROOT, "Group_[0-9][0-9]_*")) if os.path.isdir(d))
    if len(groups) != 18:
        sys.exit(f"Expected 18 group folders, found {len(groups)}")

    for gdir in groups:
        gname = os.path.basename(gdir)
        gnum = gname[6:8]
        tel = os.path.join(gdir, "telemetry")

        # 1a. rename simulated CSVs and fix references
        names = sorted(KNOWN_SIMULATED)
        # Names that a Unity C# logger uses for its OWN (real) output: those references must not become SIMULATED_
        cs_names = set()
        for cs in glob.glob(os.path.join(gdir, "**", "*.cs"), recursive=True):
            src = read(cs)
            cs_names |= {n for n in names if re.search(r"(?<![\w])" + re.escape(n), src)}
        for n in names:
            p = os.path.join(tel, n)
            if os.path.exists(p):
                new = os.path.join(tel, "SIMULATED_" + n)
                git("mv", os.path.relpath(p, ROOT), os.path.relpath(new, ROOT))
                renamed.append((os.path.relpath(p, ROOT), os.path.basename(new)))
        for root, _, files in os.walk(gdir):
            for fn in files:
                fp = os.path.join(root, fn)
                ext = os.path.splitext(fn)[1].lower()
                if ext not in TEXT_EXT or fn.startswith("SIMULATED_"):
                    continue
                txt = read(fp); new_txt = txt
                for n in names:
                    # Python generators and general docs -> SIMULATED_ file; C# loggers and docs that describe
                    # the logger's output -> the separate real-trials file.
                    target = real_name(n) if (ext == ".cs" or (n in cs_names and ext != ".py")) else "SIMULATED_" + n
                    if n in cs_names and ext == ".cs":
                        real_out.add(f"{gname}: {real_name(n)}")
                    new_txt = re.sub(r"(?<![\w])" + re.escape(n), target, new_txt)
                if new_txt != txt:
                    write(fp, new_txt, like=txt); touched.add(fp)

        # 1b. notice header on synthetic-data generators
        for py in glob.glob(os.path.join(tel, "*.py")):
            src = read(py)
            synthetic = os.path.basename(py) == "generate_paper_figures.py" or (
                "np.random" in src and re.search(r"def generate_\w*(benchmark|dataset)", src))
            if not synthetic or MARK in src:
                continue
            lines = src.splitlines(keepends=True)
            i = 0
            while i < len(lines) and i < 2 and (lines[i].startswith("#!") or re.match(r"#.*coding[:=]", lines[i])):
                i += 1
            new_src = "".join(lines[:i]) + NOTICE + "".join(lines[i:])
            write(py, new_src, like=src); touched.add(py); headers.append(os.path.relpath(py, ROOT))
            try:
                py_compile.compile(py, doraise=True)
            except py_compile.PyCompileError as e:
                compiled_bad.append(f"{py}: {e}")

        # 1c. figures README
        figdir = os.path.join(gdir, "docs", "figures")
        if os.path.isdir(figdir):
            figs = sorted(f for f in os.listdir(figdir) if re.match(r"figure.*\.png$", f, re.I))
            fr = os.path.join(figdir, "README.md")
            write(fr, FIG_README.format(files=", ".join(f"`{f}`" for f in figs) or "(none)"), like="")
            touched.add(fr)

        # 3. dossier + docs README
        dossier = f"IVRAR_Group_{gnum}_Technical_Dossier.docx"
        src_doc = os.path.join(PACKS, dossier)
        if not os.path.exists(src_doc):
            sys.exit(f"Missing dossier in packs folder: {src_doc}")
        os.makedirs(os.path.join(gdir, "docs"), exist_ok=True)
        dst_doc = os.path.join(gdir, "docs", dossier)
        shutil.copy2(src_doc, dst_doc); touched.add(dst_doc)
        dr = os.path.join(gdir, "docs", "README.md")
        note = DOCS_NOTE.format(dossier=dossier)
        if os.path.exists(dr):
            cur = read(dr)
            if note not in cur.replace("\r\n", "\n"):
                write(dr, cur.rstrip() + "\n\n" + note + "\n", like=cur)
        else:
            write(dr, DOCS_README.format(group=gname, note=note, dossier=dossier, pdf=dossier.replace(".docx", ".pdf")), like="")
        touched.add(dr)

    # 2. grading policy
    gp = os.path.join(ROOT, "GRADING_RUBRIC_AND_EVALUATION_POLICY.md")
    write(gp, RUBRIC); touched.add(gp)

    # 3. guide PDF at root
    gsrc = os.path.join(PACKS, GUIDE_PDF)
    if not os.path.exists(gsrc):
        sys.exit(f"Missing guide PDF: {gsrc}")
    shutil.copy2(gsrc, os.path.join(ROOT, GUIDE_PDF)); touched.add(os.path.join(ROOT, GUIDE_PDF))

    git("add", "-A", "--", *[os.path.relpath(p, ROOT) for p in sorted(touched)])
    print(f"Renamed {len(renamed)} simulated CSV files (git mv):")
    for o, n in renamed:
        print(f"   {o}  ->  {n}")
    print(f"Notice header added to {len(headers)} scripts.")
    if real_out:
        print("Unity C# loggers now write REAL trial data to a separate file (not the simulated one):")
        for r in sorted(real_out):
            print("   " + r)
    print(f"Files written/updated: {len(touched)}")
    if compiled_bad:
        print("WARNING, scripts that no longer compile:\n  " + "\n  ".join(compiled_bad))
    print("\nStaged, NOT committed. Review with:  git status  /  git diff --cached --stat")

if __name__ == "__main__":
    main()
