# Smart Task Scheduler Bot

A Python Discord bot for personal task reminders, featuring concurrent timers, DM notifications, and interactive task management.

---

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Usage](#usage)  
4. [Technical Highlights](#technical-highlights)  
5. [Future Extensions](#future-extensions)  

---

## Overview

The Smart Task Scheduler Bot is a **personal reminder system for Discord** that delivers DM-based reminders with **concurrent timers**, with python programming, asynchronous task scheduling, error handling, and message formatting using **embeds**.

---

## Features

- **DM Reminders**: Users receive private reminders via Discord direct messages.   
- **Task Management**: Each reminder has a unique task ID; users can list pending tasks and cancel them.  
- **Human-Friendly Timing**: Supports time inputs like `10s`, `5m`, `1h`, and shows live countdowns.  
- **Multi-User and Multi-Task Support**: Background worker handles multiple reminders concurrently using `asyncio.Queue`, and also handles tasks for multiple users simultaneously without conflicts.  
- **Error Handling**: Accounts for invalid input, missing permissions, and DM restrictions.  

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

### 1. Schedule a reminder
![RemindMe Command](images/image1.png)

### 2. List tasks with countdown
![Tasks Command Countdown](images/image2.png)

### 3. Cancel a task
![Cancel Task](images/image3.png)

### 4. Reminder DM notification
![Reminder DM](images/image4.png)

### 5. Multiple users scheduling reminders
![Multiple Users RemindMe](images/image5.png)

### 6. Multiple users task list with different IDs
![Multiple Users Tasks](images/image6.png)

---

## Technical Highlights

**Concurrent Task Handling**:  
- Multiple reminders from different users can be scheduled without blocking each other.  
- DM sending, countdown tracking, and command processing all run asynchronously.  
- The bot uses `asyncio.Queue` to schedule tasks concurrently.  
- A background worker dequeues tasks and waits asynchronously for the execution time.  

**Modular & Reusable Design**:  
- `scheduler.py` handles all task logic and timing.  
- `commands.py` handles Discord commands and task registration.  
- `embeds.py` generates all rich message embeds.  
- This separation makes the code easier to maintain, test, and extend.  

---

## Future Extensions

- **Priority Levels**: High/medium/low priority reminders with dynamic execution order.  
- **Recurring Tasks**: Automatically repeat reminders on a schedule.  
- **Persistent Storage**: Store tasks in a database or file to survive bot restarts.  
- **Enhanced Embeds**: Include progress bars, timestamps, or reaction buttons for interactive reminders.  


