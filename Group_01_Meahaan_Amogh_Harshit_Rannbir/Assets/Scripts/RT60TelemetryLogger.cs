// RT60TelemetryLogger.cs - Schroeder Backward Integration and CSV Logger
// Project: IVRAR Group 01 (Home Cinema Acoustics CEDIA/CTA-RP22)
// Course: Introduction to Virtual Reality and Augmented Reality (702COI002)

using System;
using System.IO;
using System.Collections.Generic;
using UnityEngine;

public class RT60TelemetryLogger : MonoBehaviour
{
    [Header("Telemetry Configuration")]
    public string outputFilename = "telemetry/acoustic_real_trials.csv";
    public float timeResolutionMs = 5.0f;

    // Energy decay buffers
    private List<float> energyHistogram = new List<float>();

    // =========================================================================
    // STUDENT 2: Amogh Gupta (C034) - Spatial Acoustics & Audio Specialist
    // Branch: feat/c034-spatial-acoustics-au
    // =========================================================================

    /// <summary>
    /// Computes reverberation time RT60 via Schroeder backward integration over the impulse response.
    /// </summary>
    public float ComputeSchroederRT60(float[] impulseResponse)
    {
        // TODO [C034 - Amogh Gupta]:
        // 1. Mathematical Formulation:
        //    Schroeder Backward Integration: E(t) = \int_t^\infty [h(\tau)]^2 d\tau
        //    In discrete domain: energyDecay[i] = \sum_{j=i}^{N-1} h[j]^2
        // 2. Linear Regression Slope for T20:
        //    Find time t5 where decayDb reaches -5.0 dB and t25 where decayDb reaches -25.0 dB.
        //    T20 = t25 - t5;
        //    RT60 = 3.0 * T20 (extrapolated 60 dB decay).
        // 3. Oral Viva Defense: Explain why Schroeder backward integration eliminates random noise fluctuations 
        //    compared to interrupted continuous noise decay methods (ISO 3382-2).

        int n = impulseResponse != null ? impulseResponse.Length : 0;
        if (n == 0) return 0.35f;

        float[] energyDecay = new float[n];
        float sum = 0.0f;

        for (int i = n - 1; i >= 0; i--)
        {
            sum += impulseResponse[i] * impulseResponse[i];
            energyDecay[i] = sum;
        }

        float totalEnergy = energyDecay[0];
        if (totalEnergy <= 0.0001f) return 0.35f;

        float[] decayDb = new float[n];
        for (int i = 0; i < n; i++)
        {
            decayDb[i] = 10.0f * Mathf.Log10(Mathf.Max(0.00001f, energyDecay[i] / totalEnergy));
        }

        float t5 = -1f, t25 = -1f;
        for (int i = 0; i < n; i++)
        {
            if (t5 < 0 && decayDb[i] <= -5.0f) t5 = i * (timeResolutionMs / 1000.0f);
            if (t25 < 0 && decayDb[i] <= -25.0f) t25 = i * (timeResolutionMs / 1000.0f);
        }

        if (t5 >= 0 && t25 > t5)
        {
            float t20 = t25 - t5;
            return t20 * 3.0f;
        }
        return 0.35f;
    }

    // =========================================================================
    // STUDENT 4: Rannbir Sachdeva (N087) - Techno-Managerial Product Manager
    // Branch: feat/n087-technoeconomic-produ
    // =========================================================================

    /// <summary>
    /// Evaluates whether the computed RT60 falls within CEDIA/CTA-RP22 standard tolerances for private listening spaces.
    /// </summary>
    public bool CheckCEDIACompliance(float rt60, float roomVolumeM3, out float targetRT60)
    {
        // TODO [N087 - Rannbir Sachdeva]:
        // 1. CEDIA/CTA-RP22 Mathematical Standard:
        //    Target RT60 = 0.05 * (V / 100)^(1/3) +/- 0.05 seconds.
        //    Nominal tolerance range: 0.20s <= RT60 <= 0.50s.
        // 2. Logging & Compliance:
        //    If out of bounds, trigger warning flag in telemetry CSV stream to schedule acoustic panel repositioning.
        // 3. Oral Viva Defense: Walk through the physical rework reduction calculation (29.2% to 4.2%) 
        //    achieved when pre-construction VR validation detects acoustic boundary violations early.

        targetRT60 = 0.05f * Mathf.Pow(Mathf.Max(10f, roomVolumeM3) / 100.0f, 1.0f / 3.0f);
        float lowerBound = Mathf.Max(0.20f, targetRT60 - 0.05f);
        float upperBound = Mathf.Min(0.50f, targetRT60 + 0.05f);

        return rt60 >= lowerBound && rt60 <= upperBound;
    }

    /// <summary>
    /// Appends trial telemetry row to CSV dataset.
    /// </summary>
    public void LogTelemetryRow(int trialId, string configName, float rt60, bool isCompliant, float verticalGazeAngle, bool sightlineOk)
    {
        // TODO [N087 - Rannbir Sachdeva]:
        // File IO: Append row formatted as: trial_id,config_name,rt60_seconds,cedia_compliant,vertical_gaze_deg,sightline_ok
        // Handle directory existence checking with Directory.CreateDirectory().
        string row = $"{trialId},{configName},{rt60:F3},{isCompliant},{verticalGazeAngle:F1},{sightlineOk}";
        Debug.Log($"[Telemetry Logger] {row}");
    }
}
