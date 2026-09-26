import json, sys
from client import AgentActionTrajectoryVideoSummarizerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "agent-action-trajectory-video-summarizer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "summarize_action_trajectory", "description": "Analyzes multi-frame GUI computer-use action trajectories, detecting dead clicks and rendering stalls."}]}}
    elif method == "tools/call":
        client = AgentActionTrajectoryVideoSummarizerClient()
        res = client.summarize_action_trajectory()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AgentActionTrajectoryVideoSummarizerClient()
        print(json.dumps(client.summarize_action_trajectory(), indent=2))
