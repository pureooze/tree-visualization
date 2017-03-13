from bst import BST
import pygame
from pygame.locals import *
import pyganim
import sys

# [[[None, 1, None], 6, None], 10, [[None, 20, None], 22, [None, 50, None]]]
def disTree(root, screen, x=0, y=0):
    depth = root.getDepth()
    xdiff = 5*pow(2,depth)
    ydiff = 50
    fontName = "Times New Roman"
    font = pygame.font.SysFont(fontName, 12, 1)
    
    if root.getLeft() is not None:
        disTree(root.getLeft(), screen, x-xdiff, y+ydiff)

    pygame.draw.circle(screen, (0,0,0), (x,y), 15)
    label = font.render(str(root.value), 1, (255,255,255))
    screen.blit(label, (x-8,y-5))    

    if root.getRight() is not None:
        disTree(root.getRight(), screen, x+xdiff, y+ydiff)

def displayTree(tree, depth, screen, x=0, y=0):
    xdiff = 15*depth
    try:
        if tree[0] is not None:
            if tree[0][2] is not None:
                displayTree(tree[0], depth-1, screen, x-xdiff, y+30)
            else:
                displayTree(tree[0], depth-1, screen, x-xdiff, y+30)
                
    except TypeError:
        pass

    pygame.draw.circle(screen, (0,0,0), (x,y), 10)

    try:
        if tree[2] is not None:
            if tree[2][0] is not None:
                displayTree(tree[2], depth-1, screen, x+xdiff, y+30)
            else:
                displayTree(tree[2], depth-1, screen, x+xdiff, y+30)

                
    except TypeError:
        pass
            

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
   

    #path = mytree.search(20)
    tree = mytree.inorderTraversal()
    depth = mytree.getDepth()
    print(tree)

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
        disTree(mytree, windowSurface, 350, 30)
        
        pygame.display.update()
