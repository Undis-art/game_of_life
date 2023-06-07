import grid

def main():
    print("Enter to live on, q to quit.")

    game_grid = grid.Grid(40, 15)
    game_grid.print()
     
    line = ""
    while line != "q":
        game_grid.next_generation()
        game_grid.print()
        line = input()

if __name__ == "__main__":
    main()

    
    
