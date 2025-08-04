
import datetime

# --- Mixin ---
class AuditableMixin:
    """
    A Mixin class that provides auditing capabilities.
    Any class inheriting from this can track audit events.
    """
    def __init__(self, *args, **kwargs):
        print(f"Init() in {self.__class__.__name__} in AuditableMixin")
        # Call super().__init__ to ensure proper MRO chaining
        super().__init__(*args, **kwargs)
        self._audit_log = [] # Protected attribute for the audit log

    def _record_audit_event(self, event_description):
        """
        Protected method to record an event in the audit log.
        Intended for internal use by classes that mix this in.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._audit_log.append(f"[{timestamp}] {event_description}")

    def get_audit_trail(self):
        """
        Public method to retrieve a copy of the audit trail.
        """
        return list(self._audit_log) # Return a copy to prevent external modification
