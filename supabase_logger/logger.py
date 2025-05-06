from supabase_client import supabase

def log_attempt(**kwargs):
    supabase.table("attempts").insert(kwargs).execute()
