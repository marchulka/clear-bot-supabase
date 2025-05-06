from supabase_client import supabase
import uuid
from datetime import datetime
import platform
import getpass

def log_attempt(
    user_id: str,
    bot_id: str,
    lesson_id: str = None,
    step_id: str = None,
    quiz_id: str = None,
    quiz_score: float = None,
    quiz_passed: bool = None,
    user_input: str = None,
    user_command: str = None,
    user_language: str = "ru",
    user_agent: str = None,
    user_platform: str = None,
    feedback_score: int = None,
    emotion: str = None,
    retries: int = 0,
    skipped: bool = False,
    error_code: str = None,
    error_message: str = None,
    source: str = "telegram"
):
    session_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    user_agent = user_agent or platform.platform()
    user_platform = user_platform or platform.system() + " " + platform.release()
    
    data = {
        "session_id": session_id,
        "timestamp": timestamp,
        "user_id": user_id,
        "bot_id": bot_id,
        "lesson_id": lesson_id,
        "step_id": step_id,
        "quiz_id": quiz_id,
        "quiz_score": quiz_score,
        "quiz_passed": quiz_passed,
        "user_input": user_input,
        "user_command": user_command,
        "user_language": user_language,
        "user_agent": user_agent,
        "user_platform": user_platform,
        "feedback_score": feedback_score,
        "emotion": emotion,
        "retries": retries,
        "skipped": skipped,
        "error_code": error_code,
        "error_message": error_message,
        "source": source
    }
    
    supabase.table("attempts").insert(data).execute()
