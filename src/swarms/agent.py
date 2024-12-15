"""Agent module for Swarms."""
from typing import Optional, Any, Dict
import json

class Agent:
    """Base Agent class."""
    
    def __init__(
        self,
        agent_name: str = "DefaultAgent",
        system_prompt: str = "You are a helpful AI assistant.",
        llm: Optional[Any] = None,
        max_loops: int = 1,
        autosave: bool = False,
        verbose: bool = False,
        dynamic_temperature_enabled: bool = False,
        saved_state_path: str = "agent_state.json",
        user_name: str = "default_user",
        retry_attempts: int = 1,
        context_length: int = 200000,
        return_step_meta: bool = False,
        output_type: str = "string",
        **kwargs: Dict[str, Any]
    ):
        self.agent_name = agent_name
        self.system_prompt = system_prompt
        self.llm = llm
        self.max_loops = max_loops
        self.autosave = autosave
        self.verbose = verbose
        self.dynamic_temperature_enabled = dynamic_temperature_enabled
        self.saved_state_path = saved_state_path
        self.user_name = user_name
        self.retry_attempts = retry_attempts
        self.context_length = context_length
        self.return_step_meta = return_step_meta
        self.output_type = output_type
        self.kwargs = kwargs
        self.state = {}

    def run(self, task: str) -> str:
        """Run the agent on a task."""
        if self.verbose:
            print(f"🤖 {self.agent_name} processing task: {task}")
        
        try:
            # If we have an LLM, use it
            if self.llm:
                prompt = f"{self.system_prompt}\n\nTask: {task}"
                response = self.llm.generate(prompt)
            else:
                response = f"Processed task: {task}"

            if self.autosave:
                self._save_state()

            return response

        except Exception as e:
            print(f"Error running task: {e}")
            return str(e)

    def _save_state(self):
        """Save the agent's state."""
        try:
            with open(self.saved_state_path, 'w') as f:
                json.dump(self.state, f)
        except Exception as e:
            print(f"Error saving state: {e}")
