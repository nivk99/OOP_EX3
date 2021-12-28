import math
import pygame
from src.GraphAlgo import GraphAlgo
import os
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
WIDTH, HIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HIGHT),depth=32, flags= pygame.constants.RESIZABLE)
FONT = pygame.font.SysFont('ariel', 20, bold=True)
R=15
rad = math.pi/180



"""
To run the graph you just need to write the position of json
"""
g_algo = GraphAlgo()
root_path = os.path.dirname(os.path.abspath(__file__))
# Type the location
g_algo.load_from_json(root_path + '/A0.json')
g = g_algo.get_graph()
k = g.get_all_v()





def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen

def scale_x_y(x,y):
     x = (scale(x,50, screen.get_width()-50,min_x,max_x))
     y = (scale(y,50, screen.get_height()-50, min_y, max_y))
     return x,y


def draw_arrow(screen, colour, start, end):
    pygame.draw.line(screen,colour,start,end,3)
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pygame.draw.polygon(screen, (255, 0, 0), ((end[0]+20*math.sin(math.radians(rotation)), end[1]+20*math.cos(math.radians(rotation))), (end[0]+20*math.sin(math.radians(rotation-120)), end[1]+20*math.cos(math.radians(rotation-120))), (end[0]+20*math.sin(math.radians(rotation+120)), end[1]+20*math.cos(math.radians(rotation+120)))),width = 3)

typ = k.get(0).getLocation().split(',')
min_x = float(typ[0])
max_x = float(typ[0])
min_y = float(typ[1])
max_y = float(typ[1])
print(typ)
for i in k:
    typ = k.get(i).getLocation()
    if isinstance(typ, str):
        typ = typ.split(',')
        typ = tuple(typ)
    if min_x > float(typ[0]):
        min_x = float(typ[0])
    if max_x < float(typ[0]):
        max_x = float(typ[0])
    if min_y > float(typ[1]):
        min_y = float(typ[1])
    if max_y < float(typ[1]):
        max_y = float(typ[1])


clock.tick(60)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill(pygame.Color(255,255,0))
    for i in k:
        typ = k.get(i).getLocation()
        if isinstance(typ, str):
            typ = typ.split(',')
            typ = tuple(typ)
        x = float(typ[0])
        y = float(typ[1])
        x_scale, y_scale = scale_x_y(x,y)
        pygame.draw.circle(screen, pygame.Color(0, 0, 0), (x_scale, y_scale), R)
    for i in k:
        a = g.all_out_edges_of_node(i)
        for j in a:
            typ_i = k.get(i).getLocation()
            typ_j = k.get(j).getLocation()
            if isinstance(typ_i, str):
                typ_i = typ_i.split(',')
                typ_i = tuple(typ_i)
                typ_j = typ_j.split(',')
                typ_j = tuple(typ_j)
            src_x = float(typ_i[0])
            src_y = float(typ_i[1])
            dest_x = float(typ_j[0])
            dest_y = float(typ_j[1])
            src_x_scale, src_y_scale = scale_x_y(src_x,src_y)
            dest_x_scale, dest_y_scale = scale_x_y(dest_x,dest_y)
            x,y = dest_x_scale-src_x_scale, dest_y_scale-src_y_scale
            z2 = (math.sqrt(x**2 + y**2) - R)**2
            if x == 0:
                d_y = y-R
                d_x = x
            else:
                d_x = math.sqrt(z2/(1+(y/x)**2))
            if y == 0:
                d_x = x-R
                d_y = y
            else:
                d_y = math.sqrt(z2 /(1+(x/y)**2))
            if x < 0:
                d_x = -d_x
            if y < 0:
                d_y = -d_y
            dest_x_scale, dest_y_scale = src_x_scale + d_x, src_y_scale + d_y
            draw_arrow(screen, (60,150, 55), (src_x_scale,src_y_scale), (dest_x_scale,dest_y_scale))

    for i in k:
        typ = k.get(i).getLocation()
        if isinstance(typ, str):
            typ = typ.split(',')
            typ = tuple(typ)
        x = float(typ[0])
        y = float(typ[1])
        x_scale, y_scale = scale_x_y(x,y)
        id_srf = FONT.render(str(i), True, pygame.Color(255,255,255))
        rect = id_srf.get_rect(center=(x_scale,y_scale))
        screen.blit(id_srf, rect)

    pygame.display.update()
