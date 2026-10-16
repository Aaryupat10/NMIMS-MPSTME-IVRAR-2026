using System;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

namespace IVRAR.MultiplayerPuzzle
{
    [System.Serializable]
    public struct CollaborationTrialRecord
    {
        public int trialId;
        public string pairId;
        public string audioCondition; // Spatial_HRTF vs NonSpatial_Stereo
        public float taskCompletionTimeSec;
        public int totalUtterances;
        public float speechOverlapRatio;
        public float meanInterpersonalDistanceM;
        public int puzzleErrors;
        public float collaborativeEfficiencyIndex;
    }

    /// <summary>
    /// Tracks voice communication dynamics, spatial audio attenuation, and collaborative verbal coordination
    /// between networked student pairs during 3D physical puzzle manipulation trials.
    /// Grounded in verbal coordination theory (Ruddle et al. 2002; Baldis 2001).
    /// </summary>
    public class SpatialVoiceTelemetryLogger : MonoBehaviour
    {
        [Header("Pair Configuration")]
        [SerializeField] private string pairIdentifier = "Pair_01";
        [SerializeField] private string currentAudioCondition = "Spatial_HRTF";

        [Header("Audio & Spatial Tracking")]
        [SerializeField] private Transform clientA_Head;
        [SerializeField] private Transform clientB_Head;
        [SerializeField] private AudioSource clientA_VoiceSource;
        [SerializeField] private AudioSource clientB_VoiceSource;

        [Header("Voice Activity Detection (VAD)")]
        [SerializeField] private float vadRmsThreshold = 0.02f;
        [SerializeField] private string outputCsvFilename = "multiplayer_collaboration_real_trials.csv";

        private List<CollaborationTrialRecord> trialRecords = new List<CollaborationTrialRecord>();
        private int totalUtteranceCount = 0;
        private float concurrentSpeechDuration = 0.0f;
        private float totalSpeechDuration = 0.0f;
        private float runningDistanceSum = 0.0f;
        private int distanceSampleCount = 0;
        private int currentTrialCounter = 0;

        private void Update()
        {
            SampleAudioAndSpatialMetrics();

            // TODO [B118 - Aditya Verma]: Implement 3D HRTF audio filter curves, microphone RMS amplitude voice activity detection (VAD), and spatial attenuation profile.
            /*
             * Aditya Verma (B118) - Spatial Voice & Audio Specialist:
             * 1. Calculate logarithmic distance roll-off curve for voice audibility across 1.0m to 10.0m range.
             * 2. Sample raw microphone audio buffers via GetOutputData to compute real-time RMS power.
             * 3. Profile directional azimuth and elevation cues to verify HRTF localization fidelity.
             */
        }

        private void SampleAudioAndSpatialMetrics()
        {
            if (clientA_Head == null || clientB_Head == null) return;

            // Interpersonal distance sampling
            float distance = Vector3.Distance(clientA_Head.position, clientB_Head.position);
            runningDistanceSum += distance;
            distanceSampleCount++;

            // Simulated Voice Activity Detection based on audio source playback
            bool isVoiceA = (clientA_VoiceSource != null && clientA_VoiceSource.isPlaying);
            bool isVoiceB = (clientB_VoiceSource != null && clientB_VoiceSource.isPlaying);

            if (isVoiceA || isVoiceB)
            {
                totalSpeechDuration += Time.deltaTime;
                if (isVoiceA && isVoiceB)
                {
                    concurrentSpeechDuration += Time.deltaTime;
                }
            }
        }

        public void RegisterUtterance()
        {
            totalUtteranceCount++;
        }

        public void OnPuzzleAssemblyFinished(float completionTimeSec, int assembledPieces)
        {
            currentTrialCounter++;

            float meanDistance = distanceSampleCount > 0 ? (runningDistanceSum / distanceSampleCount) : 1.5f;
            float overlapRatio = totalSpeechDuration > 0.001f ? (concurrentSpeechDuration / totalSpeechDuration) : 0.0f;

            // Collaborative Efficiency Index: Higher pieces assembled per unit time with lower verbal collision
            float efficiencyIndex = (assembledPieces / Mathf.Max(completionTimeSec, 1.0f)) * 100.0f * (1.0f - Mathf.Clamp01(overlapRatio));

            CollaborationTrialRecord record = new CollaborationTrialRecord
            {
                trialId = currentTrialCounter,
                pairId = pairIdentifier,
                audioCondition = currentAudioCondition,
                taskCompletionTimeSec = completionTimeSec,
                totalUtterances = totalUtteranceCount,
                speechOverlapRatio = overlapRatio,
                meanInterpersonalDistanceM = meanDistance,
                puzzleErrors = 0,
                collaborativeEfficiencyIndex = efficiencyIndex
            };

            trialRecords.Add(record);
            Debug.Log($"[TelemetryLogger] Trial {currentTrialCounter} recorded: Condition={currentAudioCondition}, Time={completionTimeSec:F2}s, Overlap={overlapRatio:F3}, Efficiency={efficiencyIndex:F2}");

            // Reset per-trial metrics
            totalUtteranceCount = 0;
            concurrentSpeechDuration = 0.0f;
            totalSpeechDuration = 0.0f;
            runningDistanceSum = 0.0f;
            distanceSampleCount = 0;

            // TODO [B077 - Mohammed Saquib Rakhangi]: Aggregate multi-client telemetry streams, compute collaborative efficiency ratios, and export session CSV records.
            /*
             * Mohammed Saquib Rakhangi (B077) - Multiplayer Networking Architect:
             * 1. Aggregate latency time series and network packet loss stats into trial records.
             * 2. Synchronize end-of-trial state across both VR headsets before writing CSV.
             * 3. Flush completed records into persistent storage.
             */
        }

        public void ExportTelemetryToCsv()
        {
            string fullPath = Path.Combine(Application.dataPath, "..", "telemetry", outputCsvFilename);
            try
            {
                using (StreamWriter writer = new StreamWriter(fullPath, false))
                {
                    writer.WriteLine("trial_id,pair_id,audio_condition,task_completion_time_sec,total_utterances,speech_overlap_ratio,mean_distance_m,puzzle_errors,collaborative_efficiency_index");
                    foreach (var rec in trialRecords)
                    {
                        writer.WriteLine($"{rec.trialId},{rec.pairId},{rec.audioCondition},{rec.taskCompletionTimeSec:F2},{rec.totalUtterances},{rec.speechOverlapRatio:F3},{rec.meanInterpersonalDistanceM:F2},{rec.puzzleErrors},{rec.collaborativeEfficiencyIndex:F2}");
                    }
                }
                Debug.Log($"[TelemetryLogger] Exported {trialRecords.Count} trial records to {fullPath}");
            }
            catch (Exception ex)
            {
                Debug.LogError($"[TelemetryLogger] Failed to export CSV: {ex.Message}");
            }
        }
    }
}
