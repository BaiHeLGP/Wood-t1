# 版本 t1
# 创建时间 2025-2-15-18-33
# 最后编辑时间 2025-2-15-19-49
import pygame
import random
import os
# 初始化
pygame.init()
os.chdir("d:/File/Python/Wood/t1")
# 设置屏幕尺寸
WIDTH = 20
HEIGHT = 20
CELL_SIZE = 30
screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
pygame.display.set_caption("Maze Generator")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 生成迷宫
def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    def dfs(x, y):
        maze[y][x] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0
                dfs(nx, ny)
    
    dfs(1, 1)
    return maze

maze = generate_maze(WIDTH, HEIGHT)

# 绘制迷宫
def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# 加载音乐
pygame.mixer.music.load("./music/m-1.mp3")  # 确保路径正确
pygame.mixer.music.play(-1)  # -1 表示循环播放

# 玩家初始位置
player_x, player_y = 1, 1

# 主循环
running = True
while running:
    for event in pygame.event.get():  # 这里不需要传递参数
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_y > 0 and maze[player_y - 1][player_x] == 0:
                player_y -= 1
            elif event.key == pygame.K_DOWN and player_y < HEIGHT - 1 and maze[player_y + 1][player_x] == 0:
                player_y += 1
            elif event.key == pygame.K_LEFT and player_x > 0 and maze[player_y][player_x - 1] == 0:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and player_x < WIDTH - 1 and maze[player_y][player_x + 1] == 0:
                player_x += 1
    
    screen.fill(WHITE)
    draw_maze(maze)
    pygame.draw.rect(screen, RED, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

pygame.quit()