import random

import pygame
from sys import exit
from random import randint, choice


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):  # type indicated what TYPE of obstachle you would want to pass through
        super().__init__()
        if type == "fly":
            fly_1 = pygame.image.load("/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Fly/Fly1.png").convert_alpha()
            fly_2 = pygame.image.load("/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_1,fly_2]
            y_position = 210
        else:
            snail_1 = pygame.image.load("/Users/princem/Desktop/UltimatePygameIntro-main/graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("/Users/princem/Desktop/UltimatePygameIntro-main/graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_position = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_position))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x  <= -100:
            self.kill()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(
            "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load(
            "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(
            "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("/Users/princem/Desktop/UltimatePygameIntro-main/audio/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -= 5

            if obstacle_rectangle.bottom == 300:
                screen.blit(snail_surface, obstacle_rectangle)
            else:
                screen.blit(fly_surface, obstacle_rectangle)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


def player_animation():
    global player_surface, player_index

    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

def collision_sprite():
    if pygame.sprite.spritecollide(player_groupSingle.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return False


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rectangle in obstacles:
            if player.colliderect(obstacle_rectangle):
                return False
    return True


score = 0
width = 800
height = 400
surface_width = 100
surface_height = 100
font_type = "/Users/princem/Desktop/UltimatePygameIntro-main/font/Pixeltype.ttf"
font_size = 50
# font_text = "JUMP'N"
font_color = 64, 64, 64
snail_x_pos = 600

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font(font_type, font_size)
game_active = True
start_time = 0
bg_music = pygame.mixer.Sound("/Users/princem/Desktop/UltimatePygameIntro-main/audio/music.wav")
bg_music.play(loops=-1)

player_groupSingle = pygame.sprite.GroupSingle()
player_groupSingle.add(Player())

obstacle_group = pygame.sprite.Group()


end_title = "Pixel Runner"
end_title_surface = test_font.render(end_title, False, "Blue")
end_title_rectangle = end_title_surface.get_rect(center=(400, 50))
# or
replay_game_surface = test_font.render("Press Space To Run", False, "Blue")
replay_game_rectangle = replay_game_surface.get_rect(center=(400, 350))

sky_surface = pygame.image.load("/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load(
    "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/ground.png").convert_alpha()


player_walk_1 = pygame.image.load(
    "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load(
    "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load(
    "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Player/jump.png").convert_alpha()
player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0
player_stand = pygame.image.load(
    "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Player/player_stand.png").convert_alpha()
player_stand_scaled = pygame.transform.scale2x(player_stand)
player_stand_rectangle = player_stand_scaled.get_rect(center=(400, 200))

# Obstacles
snail_frame_1 = pygame.image.load(
    "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load(
    "/Users/princem/Desktop/UltimatePygameIntro-main/graphics/snail/snail2.png").convert_alpha()
snail_frame = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frame[snail_frame_index]

# snail_rectangle = snail_surface.get_rect(bottomright=(snail_x_pos, 300))

fly_frame_1 = pygame.image.load("/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("/Users/princem/Desktop/UltimatePygameIntro-main/graphics/Fly/Fly2.png").convert_alpha()
fly_frame = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frame[fly_frame_index]

obstacle_rectangle_list = []

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    # Draw all element and update everything
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if player_rectangle.bottom == 300:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20

                if event.type == pygame.MOUSEBUTTONUP:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                # snail_rectangle.left = 800
                start_time = int((pygame.time.get_ticks() - start_time) / 1000)

        if game_active:

            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))

                if randint(0, 2):
                    obstacle_rectangle_list.append(snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rectangle_list.append(fly_surface.get_rect(bottomright=(randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frame[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frame[fly_frame_index]

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        score = display_score()

        player_groupSingle.draw(screen)
        player_groupSingle.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Need to uncomment this
        # game_active = collision_sprite()


    else:
        screen.fill('Yellow')
        screen.blit(player_stand_scaled, player_stand_rectangle)
        obstacle_rectangle_list.clear()
        player_rectangle.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f"Your score: {score}", False, "Blue")
        score_message_rectangle = score_message.get_rect(center=(400, 350))
        screen.blit(end_title_surface, end_title_rectangle)

        if score == 0:
            screen.blit(replay_game_surface, replay_game_rectangle)
        else:
            screen.blit(score_message, score_message_rectangle)


    pygame.display.update()
    clock.tick(60)
