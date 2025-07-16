import time
import random

class FocusAssistant:
    """Manages the Focus Assistant feature."""
    def __init__(self):
        self.is_focusing = False
        self.start_time = None
        self.focus_duration = 0
        self.achievements = []

    def start_focus(self, duration=25):
        """Starts a focus session."""
        self.is_focusing = True
        self.focus_duration = duration * 60  # in seconds
        self.start_time = time.time()
        print(f"Focus session started for {duration} minutes.")
        return "focus_started"

    def check_distraction(self, current_app):
        """Checks if the user is distracted by entertainment apps."""
        entertainment_apps = ["youtube", "game", "video"]
        if self.is_focusing and any(app in current_app.lower() for app in entertainment_apps):
            # This is a simplified check. A real implementation would need to monitor active windows.
            return "distraction_detected"
        return None

    def stop_focus(self):
        """Stops the current focus session."""
        if not self.is_focusing:
            return None
        
        elapsed_time = time.time() - self.start_time
        self.is_focusing = False
        if elapsed_time >= self.focus_duration:
            self.achievements.append(f"Focused for {self.focus_duration / 60} mins")
            print("Focus session completed successfully!")
            return "focus_success"
        else:
            print("Focus session ended early.")
            return "focus_failed"

class InspirationTrigger:
    """Manages the Inspiration Trigger feature."""
    def __init__(self):
        self.last_activity_time = time.time()
        self.quotes = [
            "How about a different song?",
            "Look out the window for 5 minutes.",
            "A short break can spark a big idea."
        ]
        self.noises = {"rain": "path/to/rain.mp3", "cafe": "path/to/cafe.mp3"}
        self.user_materials = []

    def check_inactivity(self, inactivity_duration=30):
        """Checks for user inactivity and triggers an inspiration event."""
        if time.time() - self.last_activity_time > inactivity_duration * 60:
            return self.trigger_inspiration()
        return None

    def trigger_inspiration(self):
        """Provides a random piece of inspiration."""
        trigger_type = random.choice(["quote", "noise", "user_material"])
        if trigger_type == "quote":
            return {"type": "quote", "content": random.choice(self.quotes)}
        elif trigger_type == "noise":
            noise_type = random.choice(list(self.noises.keys()))
            return {"type": "noise", "content": f"Playing {noise_type} sound."}
        elif trigger_type == "user_material" and self.user_materials:
            return {"type": "user_material", "content": random.choice(self.user_materials)}
        else: # Fallback to quote if no user materials
            return {"type": "quote", "content": random.choice(self.quotes)}

    def add_user_material(self, material):
        """Adds user-provided inspirational material."""
        self.user_materials.append(material)
        print(f"Added new material: {material}")

    def update_activity(self):
        """Resets the inactivity timer."""
        self.last_activity_time = time.time()

class InformationButler:
    """Manages the Information Butler feature."""
    def __init__(self):
        self.calendar_events = []
        self.todo_list = []

    def add_event(self, event):
        """Adds a calendar event."""
        # Example event: {'time': '2024-10-26 15:00', 'title': 'Weekly Meeting'}
        self.calendar_events.append(event)

    def check_reminders(self):
        """Checks for upcoming events and returns reminders."""
        # This is a simplified check. A real implementation would use datetime objects.
        # For now, it just returns the first event as a demo.
        if self.calendar_events:
            event = self.calendar_events[0]
            return f"Reminder: {event['title']} at {event['time']}."
        return None

    def filter_notification(self, notification):
        """Filters notifications based on importance."""
        # Example notification: {'sender': 'boss@work.com', 'content': '...', 'important': True}
        if notification.get('important'):
            return "important_message"
        else:
            return "regular_message"
