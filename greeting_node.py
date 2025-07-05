from AgentState import AgentState

def greeting_node(state: AgentState) -> AgentState:
    """
    simple node that adds a greeting message to the state
    """
    state['message'] = "Hey " + state['message'] + ", You just built your first graph!"
    return state

