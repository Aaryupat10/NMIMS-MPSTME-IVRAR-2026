# Research and Implementation Guide: Gamified Mobile AR Checkpoint Discovery System

## Project: IVRAR Group 08
## Target Venue: Computers & Education / Computers in Human Behavior / IEEE Transactions on Learning Technologies

---

## 1. Mathematical and Algorithmic Formulation

### 1.1 Geospatial WGS84 to Local Unity Metric Coordinate Transform
Geographic coordinates (latitude $\phi$, longitude $\lambda$, ellipsoidal height $h$) of campus checkpoints are mapped to a local tangent Euclidean plane (East-North-Up coordinate system) centered at the campus reference origin $(\phi_0, \lambda_0, h_0)$:

$$\Delta x_{\text{east}} = R_E \cdot (\lambda - \lambda_0) \cdot \cos\left(\frac{\phi + \phi_0}{2}\right)$$

$$\Delta z_{\text{north}} = R_N \cdot (\phi - \phi_0)$$

where $R_E$ and $R_N$ are the prime vertical and meridional radii of curvature of the WGS84 reference ellipsoid:

$$R_N = \frac{a(1 - e^2)}{(1 - e^2 \sin^2 \phi)^{3/2}}, \quad R_E = \frac{a}{\sqrt{1 - e^2 \sin^2 \phi}}$$

with semi-major axis $a = 6378137.0\text{ m}$ and eccentricity $e^2 \approx 0.00669437999014$.

### 1.2 Geofenced Checkpoint Proximity Detection
The mobile client computes Euclidean proximity in real-time between user position $\mathbf{x}_{\text{user}} = (x_u, z_u)$ and checkpoint anchor $\mathbf{x}_{\text{cp}} = (x_{cp}, z_{cp})$:

$$d(\mathbf{x}_{\text{user}}, \mathbf{x}_{\text{cp}}) = \sqrt{(x_u - x_{cp})^2 + (z_u - z_{cp})^2}$$

A checkpoint unlock trigger is fired when $d(\mathbf{x}_{\text{user}}, \mathbf{x}_{\text{cp}}) \le r_{\text{threshold}}$, where $r_{\text{threshold}} = 5.0\text{ m}$.

### 1.3 Backtracking Heading Disorientation Metric
To detect route disorientation algorithmically, the system calculates the angular deviation between consecutive movement vectors $\mathbf{v}_{t-1} = \mathbf{x}_{t-1} - \mathbf{x}_{t-2}$ and $\mathbf{v}_t = \mathbf{x}_t - \mathbf{x}_{t-1}$:

$$\theta_{\text{turn}} = \arccos\left(\frac{\mathbf{v}_{t-1} \cdot \mathbf{v}_t}{\|\mathbf{v}_{t-1}\| \|\mathbf{v}_t\|}\right)$$

A backtracking incident is registered whenever $\theta_{\text{turn}} \ge 135.0^\circ$ accompanied by displacement $\|\mathbf{v}_t\| \ge 1.0\text{ m}$, indicating that the student reversed their exploration direction due to disorientation.

### 1.4 Santa Barbara Sense of Direction (SBSOD) Psychometric Formulation
Navigational self-efficacy is quantified via the 15-item SBSOD scale (`Hegarty2002`). Positively worded items ($I^+$) and reverse-scored negatively worded items ($I^-$) are aggregated on a 1-to-7 Likert scale:

$$S_{\text{SBSOD}} = \frac{1}{15} \left( \sum_{i \in I^+} s_i + \sum_{j \in I^-} (8 - s_j) \right)$$

The navigational self-efficacy gain is computed as:

$$\Delta S = S_{\text{post}} - S_{\text{pre}}$$

### 1.5 Technoeconomic Operational Parity
The economic feasibility of the self-guided mobile AR application versus traditional printed maps and docent-guided walking tours is modeled via the dimensionless cost parity ratio $\kappa$:

$$\kappa = \frac{\text{OpEx}_{\text{AR}}}{\text{OpEx}_{\text{Traditional}}} = \frac{C_{\text{cloud\_anchors}} + C_{\text{quest\_curation}} + C_{\text{app\_maintenance}}}{C_{\text{printed\_maps}} + C_{\text{docent\_training}} + C_{\text{information\_desk}}}$$

The capital investment payback horizon in operating months is:

$$\text{Payback Months} = \frac{K_{\text{capex}}}{1 - \kappa} \times 12$$

---

## 2. Individual Student Work Boundaries & Responsibilities

```
===================================================================================================
Roll No   Student Name      Assigned Technical Role                    Assigned Software Module
===================================================================================================
F050      Varun Iyer        Mobile AR Lead                             ARCheckpointDiscoveryManager.cs
F049      Arjun Salunke     XR Systems Architect                       Geospatial WGS84 & ARCore Engine
F014      Om Kadam          Gamification & Telemetry Specialist        NavigationalSelfEfficacyLogger.cs
===================================================================================================
```

### 2.1 Varun Iyer (F050) - Mobile AR Lead
- Lead responsibility for ARFoundation integration, 3D floating billboard beacons, and auditory/particle reward feedback.
- Implementation of checkpoint proximity verification and unlock event dispatching in `Assets/Scripts/ARCheckpointDiscoveryManager.cs`.
- Verification of mobile device frame rates ($> 60\text{ fps}$) and screen occlusion mitigation (`Dunleavy2009`).
- Git Branch: `feat/f050-mobile-ar-lead`

### 2.2 Arjun Salunke (F049) - XR Systems Architect
- Lead responsibility for WGS84-to-tangent plane metric projection and high-precision GPS/IMU sensor fusion.
- Construction of the campus facility topological graph and coordinate registry across 24 checkpoint nodes.
- Implementation of spatial trajectory heatmaps and benchmark visualization in `telemetry/generate_paper_figures.py`.
- Git Branch: `feat/f049-xr-systems-architect`

### 2.3 Om Kadam (F014) - Gamification & Telemetry Specialist
- Lead responsibility for self-determination theory gamification mechanics (XP formulas, quest tiers, competence badges).
- Implementation of heading-based backtracking detection algorithm ($> 135^\circ$) and SBSOD psychometric aggregation in `Assets/Scripts/NavigationalSelfEfficacyLogger.cs`.
- Implementation of technoeconomic operational parity model in `telemetry/campus_orientation_economics.py`.
- Git Branch: `feat/f014-gamification-telemet`

---

## 3. Implementation Workflow & Scaffolding Execution

### 3.1 Unity Scene Structure
The recommended scene hierarchy inside Unity:
```
AR_CampusQuest_Main
├── AR Session
├── AR Session Origin
│   ├── AR Camera (Main Camera)
│   ├── AR Tracked Pose Driver
│   └── AR Anchor Manager
├── Checkpoint_Beacon_Prefab_Group
│   ├── Floating_Beacon_Mesh (Diamond / Octahedron)
│   ├── Billboard_Facility_Canvas (Facility Name & Distance)
│   └── ParticleSystem_UnlockBurst
├── Systems_Managers
│   ├── ARCheckpointDiscoveryManager.cs
│   └── NavigationalSelfEfficacyLogger.cs
└── UI_Canvas_HUD
    ├── Quest_Objective_Banner
    ├── Compass_Direction_Needle
    ├── XP_ProgressBar
    └── Achievement_Badge_Popup
```

### 3.2 Running Telemetry and Technoeconomic Scripts
To generate publication figures and verify the empirical dataset:
```powershell
cd telemetry
python generate_paper_figures.py
python campus_orientation_economics.py
```

---

## 4. Verification and Compliance Checklist
- [x] Exactly 6 CrossRef-verified foundational papers cited with active DOIs.
- [x] Zero emojis in any codebase or documentation files.
- [x] Zero currency symbols (dimensionless cost parity, labor hours, and payback months only).
- [x] Zero faculty names or course codes present.
- [x] Verified student boundaries marked with explicit TODO comments in C# scripts.
- [x] High-resolution 300 DPI figures generated and checked into `docs/figures/`.
- [x] Full empirical benchmark dataset ($N=50$) published in `telemetry/SIMULATED_campus_orientation_benchmark.csv`.
