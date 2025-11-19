import asyncio
from datetime import datetime, timedelta
import re

# Async queue and task store
task_queue = asyncio.Queue()
tasks_by_user = {}
task_counter = 1

# --- Utilities ---
def parse_time(time_str):
    """Parse time like 10s, 5m, 1h."""
    match = re.match(r"(\d+)([smh])", time_str)
    if not match:
        return None
    amount, unit = match.groups()
    amount = int(amount)
    if unit == "s": return timedelta(seconds=amount)
    if unit == "m": return timedelta(minutes=amount)
    if unit == "h": return timedelta(hours=amount)
    return None

def format_seconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes}m {seconds}s" if minutes else f"{seconds}s"

async def task_worker():
    """Background worker that executes tasks from the queue."""
    while True:
        task = await task_queue.get()
        delay = (task["execute_at"] - datetime.utcnow()).total_seconds()
        if delay > 0:
            await asyncio.sleep(delay)
        try:
            dm = await task["user"].create_dm()
            await task["embed_func"](dm, task)
        except Exception as e:
            print(f"Failed to send DM to {task['user']}: {e}")
        tasks_by_user[task["user"].id].remove(task)
        task_queue.task_done()
