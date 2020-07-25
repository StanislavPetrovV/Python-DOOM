from map import collision_walls
from settings import *
import pygame
import math


class Player:
    def __init__(self, sprites):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sensitivity = 0.004
        self.sprites = sprites
        # collision parameters
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        # weapon settings
        self.shot = False

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def collision_list(self):
        return collision_walls + [pygame.Rect(*obj.pos, obj.side, obj.side) for obj
                                  in self.sprites.list_of_objects if obj.blocked]

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_list)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 20: # <-------------
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_x < delta_y:
                dx = 0
        self.x += dx
        self.y += dy

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            dx, dy = player_speed * cos_a, player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx, dy = -player_speed * cos_a, -player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx, dy = player_speed * sin_a, -player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx, dy = -player_speed * sin_a, player_speed * cos_a
            self.detect_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= player_rotation_speed
        if keys[pygame.K_RIGHT]:
            self.angle += player_rotation_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.shot:
                    self.shot = True

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
            self.angle += difference * self.sensitivity