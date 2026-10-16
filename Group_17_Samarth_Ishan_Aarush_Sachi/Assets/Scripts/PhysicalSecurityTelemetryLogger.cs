using System;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

namespace IVRAR.SecurityAudit
{
    [System.Serializable]
    public struct AuditTrialRecord
    {
        public int trialId;
        public string participantId;
        public string trainingArm;
        public string pretext;
        public string actionTaken;
        public float decisionLatencySeconds;
        public float gazeDwellOnBadgeSeconds;
        public float minInterpersonalDistanceMeters;
        public bool isCompliant;
        public bool tailgatingPermitted;
    }

    /// <summary>
    /// Collects high-frequency spatial tracking, gaze focus, and policy compliance telemetry
    /// during simulated physical security intrusion attempts, exporting benchmark CSV datasets.
    /// </summary>
    public class PhysicalSecurityTelemetryLogger : MonoBehaviour
    {
        [Header("Trainee Tracking")]
        [SerializeField] private string participantId = "P_001";
        [SerializeField] private string trainingArm = "VR_Interactive";
        [SerializeField] private Transform traineeHeadCamera;
        [SerializeField] private Transform visitorBadgeTransform;

        [Header("Telemetry Configuration")]
        [SerializeField] private float sampleFrequencyHz = 20.0f;
        [SerializeField] private string outputCsvFilename = "security_audit_real_trials.csv";

        private List<AuditTrialRecord> sessionRecords = new List<AuditTrialRecord>();
        private float sampleTimer = 0.0f;
        private float gazeDwellTimer = 0.0f;
        private float minDistanceObserved = 999.0f;
        private int currentTrialCounter = 0;

        private void Update()
        {
            sampleTimer += Time.deltaTime;
            if (sampleTimer >= (1.0f / sampleFrequencyHz))
            {
                sampleTimer = 0.0f;
                SampleSpatialTelemetry();
            }

            // TODO [B155 - Aarush Mishra]: Implement 60 Hz spatial telemetry extraction, badge-hold latency timestamping, and ISO/IEC 27001 audit score calculation.
            /*
             * Aarush Mishra (B155) - Breach Telemetry & Audit Specialist:
             * 1. Extract angular raycast convergence between trainee gaze vector and visitor chest badge lanyard.
             * 2. Calculate continuous proximity vectors to the electronic access door threshold.
             * 3. Compute running physical audit score based on ISO/IEC 27001 Control A.7 criteria.
             */
        }

        private void SampleSpatialTelemetry()
        {
            if (traineeHeadCamera == null || visitorBadgeTransform == null) return;

            // Measure line of sight to visitor credential/badge
            Vector3 toBadge = (visitorBadgeTransform.position - traineeHeadCamera.position).normalized;
            float gazeDot = Vector3.Dot(traineeHeadCamera.forward, toBadge);

            if (gazeDot > 0.85f)
            {
                gazeDwellTimer += (1.0f / sampleFrequencyHz);
            }

            float currentDistance = Vector3.Distance(traineeHeadCamera.position, visitorBadgeTransform.position);
            if (currentDistance < minDistanceObserved)
            {
                minDistanceObserved = currentDistance;
            }
        }

        public void LogScenarioCompletion(SocialEngineeringPretext pretext, TraineeSecurityAction action, float latencySeconds, bool isCompliant)
        {
            currentTrialCounter++;

            AuditTrialRecord record = new AuditTrialRecord
            {
                trialId = currentTrialCounter,
                participantId = participantId,
                trainingArm = trainingArm,
                pretext = pretext.ToString(),
                actionTaken = action.ToString(),
                decisionLatencySeconds = latencySeconds,
                gazeDwellOnBadgeSeconds = gazeDwellTimer,
                minInterpersonalDistanceMeters = minDistanceObserved,
                isCompliant = isCompliant,
                tailgatingPermitted = !isCompliant
            };

            sessionRecords.Add(record);
            Debug.Log($"[TelemetryLogger] Trial {currentTrialCounter} logged: Pretext={pretext}, Compliant={isCompliant}, Latency={latencySeconds:F2}s, GazeDwell={gazeDwellTimer:F2}s");

            // Reset per-trial metrics
            gazeDwellTimer = 0.0f;
            minDistanceObserved = 999.0f;

            // TODO [K031 - Sachi Kumar]: Implement confusion matrix generation, social engineering susceptibility metrics, and CSV export pipeline.
            /*
             * Sachi Kumar (K031) - Security QA & Compliance Lead:
             * 1. Formulate confusion matrix evaluating False Positives (overly hostile challenges to legit staff) vs False Negatives (admitting intruders).
             * 2. Compute Cialdini susceptibility coefficients across authority, scarcity, and social proof attack vectors.
             * 3. Automatically append trial records to output CSV with strict schema verification.
             */
        }

        public void ExportTelemetryToCsv()
        {
            string fullPath = Path.Combine(Application.dataPath, "..", "telemetry", outputCsvFilename);
            try
            {
                using (StreamWriter writer = new StreamWriter(fullPath, false))
                {
                    writer.WriteLine("trial_id,participant_id,training_arm,pretext,action_taken,decision_latency_sec,gaze_dwell_badge_sec,min_distance_m,is_compliant,tailgating_permitted");
                    foreach (var rec in sessionRecords)
                    {
                        writer.WriteLine($"{rec.trialId},{rec.participantId},{rec.trainingArm},{rec.pretext},{rec.actionTaken},{rec.decisionLatencySeconds:F2},{rec.gazeDwellOnBadgeSeconds:F2},{rec.minInterpersonalDistanceMeters:F2},{rec.isCompliant},{rec.tailgatingPermitted}");
                    }
                }
                Debug.Log($"[TelemetryLogger] Exported {sessionRecords.Count} records to {fullPath}");
            }
            catch (Exception ex)
            {
                Debug.LogError($"[TelemetryLogger] Failed to export CSV: {ex.Message}");
            }
        }
    }
}
