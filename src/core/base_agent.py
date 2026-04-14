from src.core.observability import TraceContext, SystemObserver

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def execute(self, context: dict, trace_context: TraceContext) -> dict:
        """
        Main entry point for agent logic. Must be implemented by subclasses.
        """
        SystemObserver.log_input(trace_context, self.name, context)
        
        try:
            result = self._process(context, trace_context)
            SystemObserver.log_output(trace_context, self.name, result)
            return result
        except Exception as e:
            error_response = {"status": "error", "message": str(e)}
            SystemObserver.log_output(trace_context, self.name, error_response)
            raise e

    def _process(self, context: dict, trace_context: TraceContext) -> dict:
        raise NotImplementedError("Agents must implement the _process method.")
