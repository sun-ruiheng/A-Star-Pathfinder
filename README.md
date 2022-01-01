**Welcome to A\* Pathfinder!**
    
This program sniffs out the shortest route linking two points, efficiently via the A* Algorithm (with some exceptions).

Having read the instructions, User would enter anything into the console to launch the Pygame window.
User then clicks grids to set the Start (red), End (green) and Wall (black) points. First click for Start, second for End, next click(s) for Walls.
Finally, User presses spacebar to begin the search algorithm.


The A* Algorithm is an informed and intelligent greedy algorithm that utilises heuristics to explore in the general directions that are most likely successful, avoiding unnecessary complexity.

In this program, I introduced three metrics to each tile:

**1. D-value:** The distance value measures the minimum distance taken to travel to this point from the Start point.

**2. H-value:** The heuristic value measures the estimated proximity of the tile to the End point. It is calculated by the straight-line distance from it to the End coordinates.

**3. T-value:** The total value T = D + H. This sum of D (distance already traveled to get here) and H (estimated distance left from here to the End) provides a valuation of our confidence in this route. The smaller the T-value, the more worth it it is to explore this path.
_(I lazily assume a 1:1 ratio between D and H as components of T. There must be a better ratio for efficiency, where H exerts a greater influence on T than D does, because the straight-line distance used for H is likely an underestimate of the actual distance left. I might run some statistical study to find a better equation T = D + xH, where x is a constant greater than one.)_

During exploration, I utilise the Heaps data structure and add each explorable neighboring point to it, then retrieve the one with the minimum T-value each time. With a Min-Heap, we only have to constantly reconfigure to ensure the root node has minimum value, boosting efficiency* at the expense of precision in ordering the rest. Repeatedly done, this eventually leads us to the End.

Having reached the End, I again use a Min-Heap, but by tracking D-values this time, I work backward to draw the shortest path back to the Start.

*Efficiency: Compared to O(n<sup>2</sup>) efficiency of Bubble Sort and Insertion Sort, Heapsort allows for O(n log(n)).

**Requirements:**
1. If using on Replit: nothing.
   Oh, here it is by the way: **replit.com/@sunruiheng/A-Star-Pathfinder**

2. If using locally:
      - Python
      - Pygame (easily installable via most code editors, or Google it)
   
   1) Clone the repository
   2) Open script.py locally from your file explorer
   3) Enjoy!
