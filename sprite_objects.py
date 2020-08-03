import pygame
from settings import *
from collections import deque
from ray_casting import mapping
from numba.core import types
from numba.typed import Dict
from numba import int32


class Sprites:
    def __init__(self):
        self.sprite_parameters = {
            'sprite_barrel': {
                'sprite': pygame.image.load('sprites/barrel/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.8,
                'scale': (0.4, 0.4),
                'side': 30,
                'animation': deque(
                    [pygame.image.load(f'sprites/barrel/anim/{i}.png').convert_alpha() for i in range(12)]),
                'death_animation': deque([pygame.image.load(f'sprites/barrel/death/{i}.png')
                                          .convert_alpha() for i in range(4)]),
                'is_dead': None,
                'dead_shift': 2.6,
                'animation_dist': 800,
                'animation_speed': 6,
                'blocked': True,
                'flag': 'decor',
                'obj_action': []
            },
            'sprite_pin': {
                'sprite': pygame.image.load('sprites/pin/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.6,
                'scale': (0.6, 0.6),
                'side': 30,
                'animation': deque([pygame.image.load(f'sprites/pin/anim/{i}.png').convert_alpha() for i in range(8)]),
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': None,
                'animation_dist': 800,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'decor',
                'obj_action': []
            },
            'sprite_flame': {
                'sprite': pygame.image.load('sprites/flame/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.7,
                'scale': (0.6, 0.6),
                'side': 30,
                'animation': deque(
                    [pygame.image.load(f'sprites/flame/anim/{i}.png').convert_alpha() for i in range(16)]),
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 1.8,
                'animation_dist': 1800,
                'animation_speed': 5,
                'blocked': None,
                'flag': 'decor',
                'obj_action': []
            },
            'npc_devil0': {
                'sprite': [pygame.image.load(f'sprites/npc/devil0/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.0,
                'scale': (1.1, 1.1),
                'side': 50,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/devil0/death/{i}.png')
                                           .convert_alpha() for i in range(6)]),
                'is_dead': None,
                'dead_shift': 0.6,
                'animation_dist': None,
                'animation_speed': 10,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque(
                    [pygame.image.load(f'sprites/npc/devil0/anim/{i}.png').convert_alpha() for i in range(9)]),
            },
            'npc_devil1': {
                'sprite': [pygame.image.load(f'sprites/npc/devil1/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0,
                'scale': (0.9, 1.0),
                'side': 30,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/devil1/death/{i}.png')
                                           .convert_alpha() for i in range(11)]),
                'is_dead': None,
                'dead_shift': 0.5,
                'animation_dist': None,
                'animation_speed': 6,
                'blocked': True,  # <-------------------
                'flag': 'npc',
                'obj_action': deque([pygame.image.load(f'sprites/npc/devil1/action/{i}.png')
                                    .convert_alpha() for i in range(6)])
            },
            'npc_soldier0': {
                'sprite': [pygame.image.load(f'sprites/npc/soldier0/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.8,
                'scale': (0.4, 0.6),
                'side': 30,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/soldier0/death/{i}.png')
                                           .convert_alpha() for i in range(10)]),
                'is_dead': None,
                'dead_shift': 1.7,
                'animation_dist': None,
                'animation_speed': 6,
                'blocked': True,
                'flag': 'npc',
                'obj_action': deque([pygame.image.load(f'sprites/npc/soldier0/action/{i}.png')
                                           .convert_alpha() for i in range(4)])
            },
            'npc_soldier1': {
                'sprite': [pygame.image.load(f'sprites/npc/soldier1/base/{i}.png').convert_alpha() for i in range(8)],
                'viewing_angles': True,
                'shift': 0.8,
                'scale': (0.4, 0.6),
                'side': 30,
                'animation': [],
                'death_animation': deque([pygame.image.load(f'sprites/npc/soldier1/death/{i}.png')
                                           .convert_alpha() for i in range(11)]),
                'is_dead': None,
                'dead_shift': 1.7,
                'animation_dist': None,
                'animation_speed': 6,
                'blocked': True,  # <-------------------
                'flag': 'npc',
                'obj_action': deque([pygame.image.load(f'sprites/npc/soldier1/action/{i}.png')
                                    .convert_alpha() for i in range(4)])
            },
            'sprite_door_v': {
                'sprite': [pygame.image.load(f'sprites/doors/door_v/{i}.png').convert_alpha() for i in range(16)],
                'viewing_angles': True,
                'shift': 0.1,
                'scale': (2.6, 1.2),
                'side': 100,
                'animation': [],
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 0,
                'animation_dist': 0,
                'animation_speed': 0,
                'blocked': True,
                'flag': 'door_h',
                'obj_action': []
            },
            'sprite_door_h': {
                'sprite': [pygame.image.load(f'sprites/doors/door_h/{i}.png').convert_alpha() for i in range(16)],
                'viewing_angles': True,
                'shift': 0.1,
                'scale': (2.6, 1.2),
                'side': 100,
                'animation': [],
                'death_animation': [],
                'is_dead': 'immortal',
                'dead_shift': 0,
                'animation_dist': 0,
                'animation_speed': 0,
                'blocked': True,
                'flag': 'door_v',
                'obj_action': []
            },
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_parameters['sprite_barrel'], (7.1, 2.1)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (5.9, 2.1)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (14.8, 12.28)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (16.5, 7.61)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (12.54, 2.42)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (19.2, 2.62)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (21.79, 8.93)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (21.57, 13.58)),
            SpriteObject(self.sprite_parameters['sprite_barrel'], (12.32, 13.62)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (1.25, 1.6)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (3.54, 8.42)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (5.53, 9.43)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (9.42, 8.48)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (10.36, 3.73)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (13.8, 11.32)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (19.3, 12.76)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (16.34, 4.5)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (16.11, 1.47)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (22.31, 1.59)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (22.47, 14.48)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (11.46, 14.55)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (1.46, 14.41)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (8.8, 2.5)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (16.82, 12.52)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (17.45, 3.55)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (10.62, 9.36)),
            SpriteObject(self.sprite_parameters['sprite_pin'], (7.01, 13.47)),
            SpriteObject(self.sprite_parameters['sprite_flame'], (8.6, 5.6)),

            SpriteObject(self.sprite_parameters['npc_soldier0'], (2.5, 1.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (5.51, 1.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (6.61, 2.92)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (7.68, 1.47)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (8.75, 3.65)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (1.27, 11.5)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (1.26, 8.29)),
            # SpriteObject(self.sprite_parameters['npc_soldier0'], (2.56, 7.38)), # <------------
            SpriteObject(self.sprite_parameters['npc_soldier1'], (10.5, 1.1)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (3.66, 5.27)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (4.38, 6.56)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (4.33, 9.01)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (4.46, 10.35)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (13.16, 2.16)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (12.09, 1.28)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (3.9, 6.41)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (14.36, 3.31)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (2.14, 13.81)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (10.73, 3.90)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (10.6, 5.52)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (11.75, 5.75)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (14.87, 14.27)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (15.85, 14.74)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (17.02, 14.26)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (18.20, 14.73)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (19.77, 14.26)),

            SpriteObject(self.sprite_parameters['npc_soldier0'], (8.10, 11.93)),
            SpriteObject(self.sprite_parameters['npc_soldier0'], (12.14, 10.34)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (15.27, 6.56)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (14.31, 11.56)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (17.62, 9.66)),
            SpriteObject(self.sprite_parameters['npc_devil0'], (22.53, 9.00)),
            SpriteObject(self.sprite_parameters['npc_devil1'], (20.12, 3.55)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (18.29, 12.66)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (18.53, 8.33)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (20.42, 7.53)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (22.3, 2.89)),
            SpriteObject(self.sprite_parameters['npc_soldier1'], (22.76, 10.21)),

            SpriteObject(self.sprite_parameters['sprite_door_v'], (9.5, 4.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (9.5, 1.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (6.5, 8.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (2.5, 10.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (13.5, 14.5)),
            SpriteObject(self.sprite_parameters['sprite_door_v'], (3.5, 3.5)),
            SpriteObject(self.sprite_parameters['sprite_door_h'], (1.5, 4.5)),
            SpriteObject(self.sprite_parameters['sprite_door_h'], (5.5, 4.5)),
            SpriteObject(self.sprite_parameters['sprite_door_h'], (13.5, 4.5)),
            SpriteObject(self.sprite_parameters['sprite_door_h'], (22.5, 11.5)),
            SpriteObject(self.sprite_parameters['sprite_door_h'], (11.5, 6.5)),
        ]

    @property
    def sprite_shot(self):
        return min([obj.is_on_fire for obj in self.list_of_objects], default=(float('inf'), 0))

    @property
    def blocked_doors(self):
        blocked_doors = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)
        for obj in self.list_of_objects:
            if obj.flag == 'door_h' or obj.flag == 'door_v':
                if obj.blocked:
                    i, j = mapping(obj.x, obj.y)
                    blocked_doors[(i, j)] = 0
        return blocked_doors


class SpriteObject:
    def __init__(self, parameters, pos):
        self.object = parameters['sprite'].copy()
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation'].copy()
        # ---------------------
        self.death_animation = parameters['death_animation'].copy()
        self.is_dead = parameters['is_dead']
        self.dead_shift = parameters['dead_shift']
        # ---------------------
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.blocked = parameters['blocked']
        self.flag = parameters['flag']
        self.obj_action = parameters['obj_action'].copy()
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.side = parameters['side'] # <-------------------------------------------------------
        # self.pos = self.x - self.side // 2, self.y - self.side // 2
        self.dead_animation_count = 0
        self.animation_count = 0
        self.npc_action_trigger = False
        self.door_open_trigger = False
        self.door_prev_pos = self.y if self.flag == 'door_h' else self.x
        self.delete = False
        if self.viewing_angles:
            if len(self.object) == 8:
                self.sprite_angles = [frozenset(range(338, 361)) | frozenset(range(0, 23))] + \
                                     [frozenset(range(i, i + 45)) for i in range(23, 338, 45)]
            else:
                self.sprite_angles = [frozenset(range(348, 361)) | frozenset(range(0, 11))] + \
                                     [frozenset(range(i, i + 23)) for i in range(11, 348, 23)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}


    @property
    def is_on_fire(self):
        if CENTER_RAY - self.side // 2 < self.current_ray < CENTER_RAY + self.side // 2 and self.blocked:
            return (self.distance_to_sprite, self.proj_height)
        return (float('inf'), None)

    @property
    def pos(self):
        return self.x - self.side // 2, self.y - self.side // 2

    def object_locate(self, player):

        dx, dy = self.x - player.x, self.y - player.y
        self.distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        self.theta = math.atan2(dy, dx)
        gamma = self.theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI
        self.theta -= 1.4 * gamma

        delta_rays = int(gamma / DELTA_ANGLE)
        self.current_ray = CENTER_RAY + delta_rays
        if self.flag not in {'door_h', 'door_v'}: # <------------------
            self.distance_to_sprite *= math.cos(HALF_FOV - self.current_ray * DELTA_ANGLE)

        fake_ray = self.current_ray + FAKE_RAYS
        if 0 <= fake_ray <= FAKE_RAYS_RANGE and self.distance_to_sprite > 30:
            self.proj_height = min(int(PROJ_COEFF / self.distance_to_sprite),
                                   DOUBLE_HEIGHT if self.flag not in {'door_h', 'door_v'} else HEIGHT) # <--------
            sprite_width = int(self.proj_height * self.scale[0])
            sprite_height = int(self.proj_height * self.scale[1])
            half_sprite_width = sprite_width // 2
            half_sprite_height = sprite_height // 2
            shift = half_sprite_height * self.shift

            # logic for doors, npc, decors
            if self.flag == 'door_h' or self.flag == 'door_v':
                if self.door_open_trigger:
                    self.door_open()
                self.object = self.visible_sprite()
                sprite_object = self.sprite_animation()
            else:
                if self.is_dead and self.is_dead != 'immortal':
                    sprite_object = self.dead_animation()
                    shift = half_sprite_height * self.dead_shift
                    sprite_height = int(sprite_height / 1.3)
                elif self.npc_action_trigger:
                    sprite_object = self.npc_in_action()
                else:
                    # choose sprite for angle
                    self.object = self.visible_sprite()
                    # sprite animation
                    sprite_object = self.sprite_animation()
            # print(sprite_width, sprite_height)
            # if sprite_width > DOUBLE_WIDTH or sprite_height > DOUBLE_HEIGHT:
            #     sprite_rect = sprite_object.get_rect()
            #     kw = sprite_width / WIDTH
            #     kh = sprite_height / HEIGHT
            #     sprite_object = sprite_object.subsurface(sprite_rect.centerx - sprite_rect.w / kw / 2,
            #                                              sprite_rect.centery - sprite_rect.h / kh / 2,
            #                                              sprite_rect.w / kw, sprite_rect.h / kh)
            #     sprite = pygame.transform.scale(sprite_object, (WIDTH, HEIGHT))
            #     sprite_pos = (self.current_ray * SCALE - HALF_WIDTH, HALF_HEIGHT - HALF_HEIGHT + shift)
            # else:
            # sprite scale and pos
            # print(sprite_object if type(sprite_object) == list else 0)
            sprite = pygame.transform.scale(sprite_object, (sprite_width, sprite_height))
            sprite_pos = (self.current_ray * SCALE - half_sprite_width, HALF_HEIGHT - half_sprite_height + shift)

            return (self.distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)

    def sprite_animation(self):
        if self.animation and self.distance_to_sprite < self.animation_dist:
            sprite_object = self.animation[0]
            if self.animation_count < self.animation_speed:
                self.animation_count += 1
            else:
                self.animation.rotate(-1)
                self.animation_count = 0
            return sprite_object
        return self.object

    def visible_sprite(self):
        if self.viewing_angles:
            if self.theta < 0:
                self.theta += DOUBLE_PI
            self.theta = 360 - int(math.degrees(self.theta))

            for angles in self.sprite_angles:
                if self.theta in angles:
                    return self.sprite_positions[angles]
        return self.object

    def dead_animation(self):
        if len(self.death_animation):
            if self.dead_animation_count < self.animation_speed:
                self.dead_sprite = self.death_animation[0]
                self.dead_animation_count += 1
            else:
                self.dead_sprite = self.death_animation.popleft()
                self.dead_animation_count = 0
        return self.dead_sprite

    def npc_in_action(self):
        sprite_object = self.obj_action[0]
        if self.animation_count < self.animation_speed:
            self.animation_count += 1
        else:
            self.obj_action.rotate()
            self.animation_count = 0
        return sprite_object

    def door_open(self):
        if self.flag == 'door_h':
            self.y -= 3
            if abs(self.y - self.door_prev_pos) > TILE:
                self.delete = True
        elif self.flag == 'door_v':
            self.x -= 3
            if abs(self.x - self.door_prev_pos) > TILE:
                self.delete = True

