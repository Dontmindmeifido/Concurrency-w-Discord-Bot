from scheduler import task_queue, tasks_by_user, task_counter, parse_time, format_seconds
from embeds import reminder_scheduled_embed, reminder_dm_embed, task_list_embed, cancel_embed, error_embed
from datetime import datetime

def register_commands(bot):

    @bot.command()
    async def remindme(ctx, time_str: str, *, message):
        """Schedule a DM reminder."""
        global task_counter
        delta = parse_time(time_str)
        if not delta:
            await ctx.send(embed=error_embed("Invalid time format. Use 10s, 5m, 1h"))
            return
        execute_at = datetime.utcnow() + delta
        task = {
            "id": task_counter,
            "user": ctx.author,
            "message": message,
            "execute_at": execute_at,
            "time_str": time_str,
            "embed_func": reminder_dm_embed,
            "format_seconds": format_seconds,
            "now_func": datetime.utcnow
        }
        task_counter += 1
        if ctx.author.id not in tasks_by_user:
            tasks_by_user[ctx.author.id] = []
        tasks_by_user[ctx.author.id].append(task)
        await task_queue.put(task)
        await ctx.send(embed=reminder_scheduled_embed(task))

    @bot.command()
    async def tasks(ctx):
        """List all pending reminders."""
        user_tasks = tasks_by_user.get(ctx.author.id, [])
        embed = task_list_embed(user_tasks)
        await ctx.send(embed=embed)

    @bot.command()
    async def cancel(ctx, task_id: int):
        """Cancel a pending reminder."""
        user_tasks = tasks_by_user.get(ctx.author.id, [])
        for t in user_tasks:
            if t["id"] == task_id:
                user_tasks.remove(t)
                await ctx.send(embed=cancel_embed(task_id))
                return
        await ctx.send(embed=error_embed(f"Task ID {task_id} not found."))
