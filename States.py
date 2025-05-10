class Game_states:
    def __init__(self) -> None:
        self.main_menu = 0
        self.settings = 1
        self.game_on = 2
        self.pause = 3
        
        """Game state variables"""
        self.main_menu_click = False
        
        """Game loop variables"""
        self.enemy_spell_timer = 0
        self.enemies_alive = True
        self.round_won_timer = 0
        self.round = 0
        self.score = 10
    def reset(self):
        self.enemy_spell_timer = 0
        self.enemies_alive = True
        self.round_won_timer = 0
        self.round = 0
        self.score = 0
    
    def add_points(self,score:int):
        self.score += score
    
    def get_score(self):
        return self.score