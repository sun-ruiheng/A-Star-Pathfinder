**Welcome to A\* Pathfinder!**
    
This program sniffs out the shortest route linking two points, efficiently via the A* Algorithm (with some exceptions).

Having read the instructions, User would enter anything into the console to launch the Pygame window.
User then clicks grids to set the Start (red), End (green) and Wall (black) points. First click for Start, second for End, next click(s) for Walls.
Finally, User presses spacebar to begin the search algorithm.


The A* Algorithm is an informed and intelligent greedy algorithm that utilises heuristics to explore in the general directions that are most likely successful, avoiding unnecessary complexity.

In this program, I introduced three metrics to each tile:

**1. H-value:** The heuristic value measures the estimated closeness of the tile to the End point. It is calculated by the straight line distance from it to the End coordinates.

**2. D-value:** This measures the minimum distance taken to travel to that point from the Start point.

**3. T-value:** T = H + D. This sum of (distance already traveled to get here) and (estimated distance left from here to the End) provides a valuation of our confidence in this route. The smaller the T-value, the more worth it it is to explore this path.

So, I utilised the Heaps data structure and added each potential path to it, retrieving the one with the minimum T-value each time. Repeatedly done, this finally leads us to the End.

Having reached the End, I again use a Min-Heap, but by tracking D-values this time, I work backward to draw the shortest path back to the Start.


**Requirements:**
1. If using on Replit: nothing.

2. If using locally:
      - Python
      - Pygame (easily installable via most code editors, or Google it)
   
   1) Clone the repository
   2) Open script.py locally from your file explorer
   3) Enjoy
