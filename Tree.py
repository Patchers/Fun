import time
import random

events = ["sunny", "rainy", "dead plant", 'dead animal']

class Tree:
    def __init__(self, name_tree, name_user, root_depth, branch_height, leaves, nutrients, water):
        self.name_tree = name_tree
        self.name_user = name_user
        self.root_depth = root_depth
        self.branch_height = branch_height
        self.leaves =  leaves
        self.nutrients = nutrients
        self.water = water

''' def names(self):
        pass

    def grow(self):
        

    def shrink(self):
        pass'''

Tree_1 = Tree(input('Name your Tree: '), input('Name yourself: '), 0,0,0,1,1)

#PRegnant Pause
time.sleep(3)

#Welcome and Start Game
print(f'Welcome {Tree_1.name_user}. You plant the seed of your tree: {Tree_1.name_tree}')

events = ["sunny", "rainy", "dead plant", 'dead animal', 'fungus', 'pest' ]

while Tree_1.branch_height < 100:
    Tree_1.branch_height = Tree_1.branch_height + 1
    Tree_1.root_depth = Tree_1.root_depth + 1
    event = random.choice(events)
    time.sleep(1)
    if event == "sunny":
        Tree_1.branch_height = Tree_1.branch_height + 1
        Tree_1.root_depth = Tree_1.root_depth + 2
        print(f'It was a {event} day. {Tree_1.name_tree} is now {Tree_1.branch_height} high and its roots are {Tree_1.root_depth} deep.\n')
    elif event == "rainy":
        Tree_1.branch_height = Tree_1.branch_height + 2
        Tree_1.root_depth = Tree_1.root_depth + 1
        print(f'It was a {event} day. {Tree_1.name_tree} is now {Tree_1.branch_height} high and its roots are {Tree_1.root_depth} deep.\n')
    elif event == "dead plant":
        Tree_1.branch_height = Tree_1.branch_height + 1
        Tree_1.root_depth = Tree_1.root_depth + 1
        print(f'A plant died and provided nutrients. {Tree_1.name_tree} is now {Tree_1.branch_height} high and its roots are {Tree_1.root_depth} deep.\n')
    elif event == "dead animal":
        Tree_1.branch_height = Tree_1.branch_height + 3
        Tree_1.root_depth = Tree_1.root_depth + 2
        print(f'An animal died and provided nutrients. {Tree_1.name_tree} is now {Tree_1.branch_height} high and its roots are {Tree_1.root_depth} deep.\n')
    elif event == "fungus" or "pest":
        Tree_1.branch_height = Tree_1.branch_height - 3
        Tree_1.root_depth = Tree_1.root_depth - 3
        print(f'{Tree_1.name_tree} has suffered is now {Tree_1.branch_height} high and its roots are {Tree_1.root_depth} deep.\n')
    else:
        break
