from bst import BST
import pygame
from pygame.locals import *
import pyganim
import sys
# [50, [100, [80, [60, [61]]]]]
def displayTree(root, screen, x=0, y=0, path=[]):
    depth = root.getDepth()
    xdiff = 5*pow(2,depth)
    ydiff = 50
    fontName = "Times New Roman"
    font = pygame.font.SysFont(fontName, 12, 1)
    black = (0, 0, 0)
    red = (200, 0, 0)
    lineWidth = 5

    try:
        if root.value == path[0]:
            circleColor = red
        else:
            circleColor = black
    except IndexError:
        circleColor = black
        
    if root.getLeft() is not None:
        try:
            if root.getLeft().getVal() is path[1][0]:
                pygame.draw.line(screen, red, (x, y), (x-xdiff, y+ydiff), lineWidth)
            else:
                pygame.draw.line(screen, black, (x, y), (x-xdiff, y+ydiff), lineWidth)
        except IndexError:
            pygame.draw.line(screen, black, (x, y), (x-xdiff, y+ydiff), lineWidth)

        try:
            displayTree(root.getLeft(), screen, x-xdiff, y+ydiff, path[1])
        except IndexError:
            displayTree(root.getLeft(), screen, x-xdiff, y+ydiff)

    if root.getRight() is not None:
        try:
            if root.getRight().getVal() is path[1][0]:
                pygame.draw.line(screen, red, (x, y), (x+xdiff, y+ydiff), lineWidth)
            else:
                pygame.draw.line(screen, black, (x, y), (x+xdiff, y+ydiff), lineWidth)
        except IndexError:
            pygame.draw.line(screen, black, (x, y), (x+xdiff, y+ydiff), lineWidth)

        try:
            displayTree(root.getRight(), screen, x+xdiff, y+ydiff, path[1])
        except IndexError:
            displayTree(root.getRight(), screen, x+xdiff, y+ydiff)

    pygame.draw.circle(screen, circleColor, (x,y), 15)
    label = font.render(str(root.value), 1, (255,255,255))
    screen.blit(label, (x-8,y-5)) 

if __name__ == "__main__":
    mytree = BST(50)
    mytree.insertNode(100)
    mytree.insertNode(80)
    mytree.insertNode(60)
    mytree.insertNode(85)
    mytree.insertNode(87)
    mytree.insertNode(55)
    mytree.insertNode(25)
    mytree.insertNode(30)
    mytree.insertNode(35)
    mytree.insertNode(40)
    mytree.insertNode(20)
    mytree.insertNode(21)
    mytree.insertNode(10)
    mytree.insertNode(101)
    mytree.insertNode(61)
   

    path = mytree.search(30)
    tree = mytree.inorderTraversal()
    depth = mytree.getDepth()
    print(path)

    pygame.init()
    windowWidth = 960
    windowHeight = 540
    title = "Tree Visualization"
    windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
    pygame.display.set_caption('Tree Visualization')
    pygame.font.init()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        windowSurface.fill((255, 255, 255))
        displayTree(mytree, windowSurface, 350, 30, path)
        
        pygame.display.update()
