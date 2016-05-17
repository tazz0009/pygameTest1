# boat_main.py

from boat import Boat, Submarine

def main():
    b = Boat()
    b.dock()
    b.undock()
    b.undock()
    b.dock()
    b.dock()

    s = Submarine()
    s.dock()
    s.undock()
    s.undock()
    s.dock()
    s.dock()
    s.submerge()

if __name__ == "__main__":
    main()
