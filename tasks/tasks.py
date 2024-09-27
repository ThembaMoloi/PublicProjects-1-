from celery import shared_task
from django.utils import timezone
from .models import Task
from datetime import timedelta, date
import datetime

@shared_task
def send_reminder_notifications():
    """Send reminders for tasks due within the next 24 hours."""
    now = timezone.now()
    upcoming = now + timedelta(hours=24)
    tasks_due = Task.objects.filter(due_date__lte=upcoming, completed=False)
    for task in tasks_due:
        # Simulate sending a reminder (e.g., print to console)
        print(f"🔔 Reminder: Task '{task.title}' is due by {task.due_date}.")

@shared_task
def create_recurring_tasks():
    """Create recurring tasks based on their recurrence pattern."""
    today = date.today()
    recurring_tasks = Task.objects.filter(recurrence__in=['daily', 'weekly', 'monthly'], completed=False)
    for task in recurring_tasks:
        if task.due_date:
            if task.recurrence == 'daily':
                new_due_date = task.due_date + timedelta(days=1)
            elif task.recurrence == 'weekly':
                new_due_date = task.due_date + timedelta(weeks=1)
            elif task.recurrence == 'monthly':
                # Handle month increment
                month = task.due_date.month + 1 if task.due_date.month < 12 else 1
                year = task.due_date.year + 1 if task.due_date.month == 12 else task.due_date.year
                day = task.due_date.day
                try:
                    new_due_date = date(year, month, day)
                except ValueError:
                    # Handle last day of shorter months
                    new_due_date = date(year, month, 1) + timedelta(days=31)
                    new_due_date = new_due_date.replace(day=1) - timedelta(days=1)
            else:
                continue  # No recurrence

            # Create a new task instance
            Task.objects.create(
                title=task.title,
                description=task.description,
                due_date=new_due_date,
                completed=False,
                priority=task.priority,
                recurrence=task.recurrence
            )
            print(f"🔄 Recurring Task Created: '{task.title}' due on {new_due_date}.")
