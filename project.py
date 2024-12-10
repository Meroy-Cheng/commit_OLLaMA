
def generate_christmas_tree(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    print(' ' * (height - 1) + '|')

tree_height = 4
generate_christmas_tree(tree_height)