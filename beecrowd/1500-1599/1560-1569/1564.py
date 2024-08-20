while True:
    try:
        entry = int(input())
        if entry == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break