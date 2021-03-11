import random
count = 16
player_one_remove = 0
player_two_remove = 0

def player_one(bean_heap):
    player_one_remove = random.randint(1,3)
    global count
    count -= player_one_remove
    print("Player 1 removes", player_one_remove, "bean(s)")
    print("There are", count, "beans left")
    print("--------")
    if count == 0:
        print("")
        print("Player 1 loses!")
    return count

def player_two(bean_heap):
    player_two_remove = random.randint(1,3)
    global count
    count -= player_two_remove
    print("Player 2 removes", player_two_remove, "bean(s)")
    print("There are", count, "beans left")
    print("--------")
    if count == 0:
        print("")
        print("Player 2 loses")
    return count

def player_smart(bean_heap):
    if bean_heap > 4:
        player_smart_remove = 3
    elif bean_heap == 3:
        player_smart_remove = 2
    elif bean_heap == 2:
        player_smart_remove = 1
    else:
        player_smart_remove = 1
    global count
    count -= player_smart_remove
    print("Player Smart removes", player_smart_remove, "bean(s)")
    print("There are", count, "beans left")
    print("--------")
    if count == 0:
        print("")
        print("Player Smart loses")
    return count

while count > 0:
    player_one(count)
    player_smart(count)
    if count == 0:
        break
