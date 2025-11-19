# Smart Task Scheduler Bot

A Python Discord bot for personal task reminders, featuring concurrent timers, DM notifications, and interactive task management.

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Python Concepts Demonstrated](#python-concepts-demonstrated)  
4. [Usage](#usage)  
5. [Screenshots](#screenshots)  
6. [Technical Highlights](#technical-highlights)  
7. [Future Extensions](#future-extensions)  

---

## Overview

The Smart Task Scheduler Bot is a **personal reminder system for Discord** that delivers DM-based reminders with **concurrent timers**. It demonstrates modular Python programming, asynchronous task scheduling, error handling, and professional message formatting using **embeds**.

This project is designed to showcase **Python software engineering skills** in a practical, portfolio-ready format.

---

## Features

- **DM Reminders**: Users receive private reminders via Discord direct messages.  
- **Async Task Queue**: Background worker handles multiple reminders concurrently using `asyncio.Queue`.  
- **Task Management**: Each reminder has a unique task ID; users can list pending tasks and cancel them.  
- **Human-Friendly Timing**: Supports time inputs like `10s`, `5m`, `1h`, and shows live countdowns.  
- **Embeds Everywhere**: All messages—reminders, confirmations, errors, and task lists—use rich embeds for clarity.  
- **Multi-User Support**: Handles tasks for multiple users simultaneously without conflicts.  
- **Graceful Error Handling**: Accounts for invalid input, missing permissions, and DM restrictions.  

---

## Python Concepts Demonstrated

- **Asynchronous Programming**: `asyncio.Queue`, background workers, non-blocking sleeps.  
- **Discord API Integration**: DM creation, command parsing, and embeds using `discord.py`.  
- **Modular Code Architecture**: Separate modules for commands, scheduling, and message formatting.  
- **Data Management**: Per-user task dictionaries with metadata (task ID, message, execution time).  
- **Error Handling**: Handles runtime exceptions and user permission errors.  
- **Reusable Utilities**: Time parsing, countdown formatting, and embed builders.  

---

## Usage

### Commands

- `!remindme <time> <message>`  
  Schedule a DM reminder. Example:

  !remindme 10s Take a break 

- `!tasks`  
List all pending reminders with countdowns.  

- `!cancel <task_id>`  
Cancel a scheduled reminder. Example:  

  !cancel 2

---

## Screenshots

### 1. Schedule a reminder
![RemindMe Command](Images/image1.png)

### 2. List tasks with countdown
![Tasks Command Countdown](Images/image2.png)

### 3. Cancel a task
![Cancel Task](Images/image3.png)

### 4. Reminder DM notification
![Reminder DM](Images/image4.png)

### 5. Multiple users scheduling reminders
![Multiple Users RemindMe](Images/image5.png)

### 6. Multiple users task list with different IDs
![Multiple Users Tasks](Images/image6.png)

---

## Technical Highlights

- **Async Queue Architecture**:  
- The bot uses `asyncio.Queue` to schedule tasks concurrently.  
- A background worker dequeues tasks and waits asynchronously for the execution time.  

- **Concurrent Task Handling**:  
- Multiple reminders from different users can be scheduled without blocking each other.  
- DM sending, countdown tracking, and command processing all run asynchronously.  

- **Modular & Reusable Design**:  
- `scheduler.py` handles all task logic and timing.  
- `commands.py` handles Discord commands and task registration.  
- `embeds.py` generates all rich message embeds.  
- This separation makes the code easier to maintain, test, and extend.  

- **Error Handling & Robustness**:  
- Gracefully handles invalid time formats.  
- Detects DM permission errors and continues without crashing.  
- Task cancellations and multi-user handling are safe and predictable.  

---

## Future Extensions

- **Priority Levels**: High/medium/low priority reminders with dynamic execution order.  
- **Recurring Tasks**: Automatically repeat reminders on a schedule.  
- **Persistent Storage**: Store tasks in a database or file to survive bot restarts.  
- **Enhanced Embeds**: Include progress bars, timestamps, or reaction buttons for interactive reminders.  
- **Web Dashboard**: Optional UI for visual task management outside Discord.  


