import tkinter as tk
from PIL import Image, ImageTk

class UIManager:
    """Manages the visual representation of the pet, including animations and rendering."""
    def __init__(self, root, pet_logic):
        self.root = root
        self.pet_logic = pet_logic
        self.label = tk.Label(root, bd=0, bg='white')
        self.label.pack()
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.wm_attributes("-transparentcolor", "white")
        self.root.attributes('-topmost', True)
        self.root.geometry('200x200+100+100') # Initial size and position

        # Placeholder for animation frames
        self.animations = {
            'idle': [],
            'walking': [],
            'happy': []
        }
        self.current_frame = 0
        self.animation_speed = 200 # ms per frame

        self.load_animations()
        self.update_pet()

    def load_animations(self):
        """Load animation frames from image files (placeholders)."""
        # In a real application, you would load a sequence of images for each state.
        # For now, we'll use a placeholder image.
        try:
            # This is a placeholder. Replace 'assets/idle.png' with actual asset paths.
            idle_image = Image.open("assets/placeholder.png").resize((150, 150))
            self.animations['idle'].append(ImageTk.PhotoImage(idle_image))
        except FileNotFoundError:
            # Create a dummy image if assets are not available
            dummy_image = Image.new('RGBA', (150, 150), (0, 0, 0, 0))
            self.animations['idle'].append(ImageTk.PhotoImage(dummy_image))

    def update_pet(self):
        """Periodically updates the pet's state and appearance."""
        current_state = self.pet_logic.get_state()
        self.play_animation(current_state)
        self.root.after(100, self.update_pet)

    def play_animation(self, state_name):
        """Plays the animation corresponding to the pet's current state."""
        if state_name in self.animations and self.animations[state_name]:
            animation_frames = self.animations[state_name]
            self.current_frame = (self.current_frame + 1) % len(animation_frames)
            frame_image = animation_frames[self.current_frame]
            self.label.config(image=frame_image)
            self.label.image = frame_image # Keep a reference
        else:
            # Fallback for undefined states
            self.label.config(text=f"State: {state_name}")

    def show_message(self, message, duration=3000):
        """Displays a message bubble near the pet."""
        # This is a simplified implementation. A real app would use a custom-styled window or canvas.
        message_label = tk.Label(self.root, text=message, bg='lightblue', wraplength=150)
        message_label.place(x=0, y=-30) # Position above the pet
        self.root.after(duration, message_label.destroy)

