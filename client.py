import json
from typing import Dict, Any, List, Optional

class AgentActionTrajectoryVideoSummarizerClient:
    """
    Production-grade multi-frame action sequence and video telemetry summarizer.
    Analyzes visual execution frames, detects dead clicks (action taken but UI state didn't change),
    measures UI latency rendering stalls, and generates concise action replay summaries.
    """
    def __init__(self):
        pass

    def summarize_action_trajectory(
        self,
        task_id: str = "task_browser_signup_881",
        frame_action_sequence: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        if not frame_action_sequence:
            frame_action_sequence = [
                {"frame": 1, "action": "click(x=320, y=140)", "ui_state_hash": "hash_init_01", "latency_ms": 120},
                {"frame": 2, "action": "type_text('user@genpark.ai')", "ui_state_hash": "hash_input_02", "latency_ms": 150},
                {"frame": 3, "action": "click(x=620, y=450)", "ui_state_hash": "hash_input_02", "latency_ms": 850}, # State identical = Dead click
                {"frame": 4, "action": "click(x=620, y=450)", "ui_state_hash": "hash_success_03", "latency_ms": 420}
            ]

        total_frames = len(frame_action_sequence)
        dead_clicks = []
        rendering_stalls = []

        for i in range(1, total_frames):
            prev_frame = frame_action_sequence[i - 1]
            curr_frame = frame_action_sequence[i]

            # Dead click detection: action was click, but hash didn't change
            if "click" in curr_frame["action"] and curr_frame["ui_state_hash"] == prev_frame["ui_state_hash"]:
                dead_clicks.append({"frame": curr_frame["frame"], "action": curr_frame["action"]})

            # Rendering stall: latency > 500ms
            if curr_frame["latency_ms"] > 500:
                rendering_stalls.append({"frame": curr_frame["frame"], "latency_ms": curr_frame["latency_ms"]})

        success_ratio = round((total_frames - len(dead_clicks)) / max(1, total_frames), 2)

        return {
            "trajectory_summary_id": "trj_sum_5510",
            "task_id": task_id,
            "total_action_frames_evaluated": total_frames,
            "dead_clicks_count": len(dead_clicks),
            "dead_click_frames": dead_clicks,
            "rendering_stalls_count": len(rendering_stalls),
            "trajectory_fluidity_score": success_ratio,
            "replay_status": "COMPLETED_WITH_INTERMITTENT_DEAD_CLICK" if dead_clicks else "FLAWLESS_EXECUTION",
            "recommended_agent_remedy": "INJECT_500MS_DOM_SETTLE_DELAY_BEFORE_RETRY" if dead_clicks else "MAINTAIN_EXECUTION_SPEED"
        }
