import discord

# --- Embed Builders ---
def reminder_scheduled_embed(task):
    embed = discord.Embed(
        title="✅ Reminder Scheduled",
        description=task["message"],
        color=discord.Color.green()
    )
    embed.add_field(name="Time", value=task["time_str"], inline=True)
    embed.add_field(name="Task ID", value=task["id"], inline=True)
    return embed

async def reminder_dm_embed(channel, task):
    embed = discord.Embed(
        title="⏰ Reminder",
        description=task["message"],
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Task ID: {task['id']}")
    await channel.send(embed=embed)

def task_list_embed(user_tasks):
    embed = discord.Embed(
        title="📋 Your Pending Tasks",
        color=discord.Color.gold()
    )
    if not user_tasks:
        embed.description = "You have no pending tasks."
    else:
        for t in user_tasks:
            remaining = int((t["execute_at"] - t["now_func"]()).total_seconds())
            embed.add_field(
                name=f"Task ID {t['id']}",
                value=f"{t['message']} — {t['format_seconds'](remaining)} remaining",
                inline=False
            )
    return embed

def cancel_embed(task_id):
    return discord.Embed(
        title="❌ Task Cancelled",
        description=f"Task ID {task_id} has been cancelled.",
        color=discord.Color.red()
    )

def error_embed(message):
    return discord.Embed(
        title="⚠️ Error",
        description=message,
        color=discord.Color.orange()
    )
