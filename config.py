# config.py

# This file manages user settings and configurations for the Desktop Companion.

# --- Pet Appearance Settings ---
# Options: 'pen_spirit', 'plant_elf', 'pixel_person'
PET_VISUAL_STYLE = 'plant_elf'

# Color theme for the pet (e.g., for the plant pot or pen body)
PET_COLOR = '#8FBC8F'  # Default: DarkSeaGreen

# Custom accessories (e.g., 'glasses', 'bow_tie')
PET_ACCESSORIES = []

# --- Feature Module Settings ---

# Focus Assistant
FOCUS_ASSISTANT_ENABLED = True
FOCUS_DURATION_MINUTES = 25
DISTRACTION_APPS = ['youtube.com', 'facebook.com', 'twitter.com', 'game.exe'] # Example list

# Inspiration Trigger
INSPIRATION_TRIGGER_ENABLED = True
INSPIRATION_IDLE_TIME_MINUTES = 30

# Information Butler
INFO_BUTLER_ENABLED = True

# --- User Preferences ---

# Path to the user's local inspiration material folder
INSPIRATION_素材_PATH = '' # e.g., 'C:/Users/YourUser/Documents/Inspiration'

# --- API Keys (Optional) ---
# For future integrations, e.g., weather, calendar APIs
CALENDAR_API_KEY = 'YOUR_CALENDAR_API_KEY_HERE'

# --- Technical Settings ---

# Logging level
LOG_LEVEL = 'INFO' # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR'

# Application window settings
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 200
