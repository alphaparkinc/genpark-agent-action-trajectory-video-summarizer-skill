import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentActionTrajectoryVideoSummarizerClient

def main():
    client = AgentActionTrajectoryVideoSummarizerClient()
    res = client.summarize_action_trajectory()
    print("=== Agent Action Trajectory Video Summarizer Output ===")
    print(f"Task: {res['task_id']} | Fluidity Score: {res['trajectory_fluidity_score']*100}%")
    print(f"Frames: {res['total_action_frames_evaluated']} | Dead Clicks: {res['dead_clicks_count']} | Stalls: {res['rendering_stalls_count']}")
    print(f"Status: {res['replay_status']}")
    print(f"Remedy: {res['recommended_agent_remedy']}")

if __name__ == '__main__':
    main()
