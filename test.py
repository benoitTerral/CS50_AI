from scripts.maze import Maze

def main():
    try:
        maze = Maze("maze1.txt")
    except Exception as e:
        print("An error occurred:", e)
        

if __name__ == "__main__":
    main()