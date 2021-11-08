class Settings():

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        #Ailen settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        # chieu di chuyển của fleet dương 1 là phải, -1 là trái
        self.fleet_direction = 1

        #Toc do game
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        #Toc do tinh Diem
        self.score_scale = 1.5


    def initialize_dynamic_settings(self):
        # chinh lai toc do game sau moi level
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #chieu di chuyen
        self.fleet_direction = 1



        #Diem so
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

