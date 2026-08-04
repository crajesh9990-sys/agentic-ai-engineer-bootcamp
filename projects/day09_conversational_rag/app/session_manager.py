from uuid import uuid4
from threading import Lock

from config import settings

class SessionManager:
    
    def __init__(self):
        self.sessions = {}
        self.lock = Lock()

    def create_session(self) -> str:
        # Creates a new session and returns its ID.
        session_id = str(uuid4())

        with self.lock:
            self.sessions[session_id]=[]
        return session_id

    def get_history(self, session_id: str):
        # Returns conversation history.
        return self.sessions.get(session_id, [])

    def add_message(self, session_id: str, role: str, content: str):
        # Adds a message to the conversation history.
        if session_id not in self.sessions:
            self.sessions[session_id] = []

        self.sessions[session_id].append(
            {
                "role": role,
                "content": content
            }
        )

        self.trim_history(session_id)

    def trim_history(self, session_id: str):
        """
        Keep only the latest N messages.
        """

        history = self.sessions.get(session_id, [])

        if len(history) > settings.MEMORY_WINDOW:
            self.sessions[session_id] = history[-settings.MEMORY_WINDOW]

    def clear_history(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def session_exists(self, session_id: str):
        return session_id in self.sessions

    def all_sessions(self):
        return self.sessions


session_manager = SessionManager()

