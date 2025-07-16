import random
import time

class PetLogic:
    def __init__(self, name="桌伴儿", pet_type="文具拟人化"):
        self.name = name
        self.pet_type = pet_type
        self.state = 'idle'  # idle, working, playing, sleeping
        self.emotions = {
            'happy': 50,
            'energy': 100,
            'growth': 0
        }
        self.emotion_tags = set()
        self.last_interaction_time = time.time()

    def update(self):
        """Called periodically to update the pet's state."""
        # Example logic: energy decreases over time
        if time.time() - self.last_interaction_time > 3600: # 1 hour
            self.emotions['energy'] = max(0, self.emotions['energy'] - 5)
            self.emotions['happy'] = max(0, self.emotions['happy'] - 5)
            self.last_interaction_time = time.time()

    def interact(self, interaction_type):
        """Handle user interactions."""
        self.last_interaction_time = time.time()
        if interaction_type == 'pat':
            self.emotions['happy'] = min(100, self.emotions['happy'] + 10)
            return f"{self.name} 很开心！"
        elif interaction_type == 'feed':
            self.emotions['energy'] = min(100, self.emotions['energy'] + 20)
            return f"{self.name} 能量满满！"
        return f"{self.name} 歪了歪头。"

    def set_state(self, new_state):
        """Set the pet's current state (e.g., focusing, relaxing)."""
        self.state = new_state
        print(f"{self.name} is now {self.state}")

    def get_status(self):
        """Return the current status and emotions of the pet."""
        return {
            'name': self.name,
            'type': self.pet_type,
            'state': self.state,
            'emotions': self.emotions,
            'emotion_tags': list(self.emotion_tags)
        }

    def add_emotion_tag(self, tag):
        """Add an emotion tag based on user behavior."""
        self.emotion_tags.add(tag)
        print(f"New emotion tag added: {tag}")

    def complete_task(self, task_type):
        """Handle task completion, like a focus session."""
        if task_type == 'focus_session':
            self.emotions['growth'] += 10
            self.emotions['happy'] = min(100, self.emotions['happy'] + 15)
            return "专注完成，太棒了！我好像又成长了一点。"

    def get_random_tip(self, context):
        """Provide a contextual tip or interaction."""
        if '易疲惫' in self.emotion_tags and context == 'late_night':
            return "夜深了，要不要设置一个20分钟的休息提醒？我陪你闭目养神。"
        
        tips = [
            "换首歌试试？",
            "看看窗外5分钟吧～",
            "要不要起来活动一下？"
        ]
        return random.choice(tips)

# Example Usage
if __name__ == '__main__':
    my_pet = PetLogic(name="钢笔精灵")
    print(my_pet.get_status())
    
    print(my_pet.interact('pat'))
    print(my_pet.get_status())
    
    my_pet.set_state('working')
    print(my_pet.complete_task('focus_session'))
    print(my_pet.get_status())

    my_pet.add_emotion_tag('易疲惫')
    print(my_pet.get_random_tip('late_night'))
