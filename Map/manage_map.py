from Map.map import map
import pygame as pygame

pygame.init()
screen_height = 640
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
white = (255, 255, 255)
screen.fill(white)
pygame.display.update()

game_seed = "Tom is the best, and i'm going to marry him."

# map() creates the map
# Map keeps track of the current level, and the players position within that level
# Each time you call myMap.getUserSelection() the map will appear for the user to select their next step
# It will automatically move the user forward to the step they chose during the previous function call
# It returns the key of the users selected node:
# P = puzzle, b = battle, ? = mystery, T = treasure, B = final battle (also indicates end of level)

myMap = map(screen, screen_width, screen_height, game_seed)

for i in range(5):
    node_key = myMap.mainloop()

