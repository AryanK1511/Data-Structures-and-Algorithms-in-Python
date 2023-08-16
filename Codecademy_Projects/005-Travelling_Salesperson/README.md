# Traveling Salesperson

Traveling Salesperson is a widely studied graph theory problem that is solved by using a greedy algorithm. The premise is that you have a graph of cities with certain distances (or weights) between them. The objective is to find the shortest path that will allow you to visit each city once, leaving you at the city in which you began your journey.

## Tasks

1/17 Complete

## Setting Up

1. We are going to be using the `Graph` and `Vertex` classes that we created in a previous lesson; however, we'll need an additional method that returns the weight of an edge. Before we get started, create a new method in `Vertex.py` that takes in an edge and returns the weight of that edge.

2. The traveling salesperson problem requires a connected graph with symmetrical weights. Take a look at the `build_tsp_graph()` function that we've created for this purpose.

3. In `script.py`, add a helper function that checks whether all of the vertices in the graph have been visited or not.

## Creating Our Function

4. Still in `script.py`, create a `traveling_salesperson()` function that takes a graph as a parameter. This is where we'll create our algorithm. Then initialize an empty string to hold the final path.

5. Create a dictionary that holds vertices and their statuses ("visited" or "unvisited"). All vertices should start as "unvisited".

6. Select an initial vertex at random. Label it as the `current_vertex`, then mark it as visited and add it to the final path.

7. Now we want to see if we've visited all of the nodes in the graph. It's unlikely that we have at this stage since this is an edge case that would only be true if our graph contained one or fewer vertices, but we still need to check.

    Use your helper function to check if we've visited all the vertices in `visited_vertices`, and store the return value in a new variable.

8. While all vertices have not been visited, create a dictionary of: { edges connected to the current vertex : edge weights }.

9. Create a boolean to hold whether or not we have found our next vertex, and set it to False since we haven't found it yet. Then initialize an empty string that will represent the `next_vertex`.

10. We need to find the next vertex in order to proceed with our function. Create a loop that runs as long as we have not found the `next_vertex`.

11. If the dictionary containing edge weights for the current vertex is empty, break.

12. Select the minimum weight edge from the dictionary and check whether it points to a vertex that has already been visited or not. If unvisited, we have found our `next_vertex`. If visited, pop the edge from our dictionary and continue searching.

13. If the dictionary of the current vertex edge weights is empty, break from the process of finding next vertices by setting `visited_all_vertices` to True.

14. Else, set the current vertex to be the `next_vertex`, mark it as visited, and add it to the TSP path.

15. Check if we have visited all vertices at this point and update the condition for our outer loop.

## Finishing Up

16. At the end of your function, outside of the while loop, print the final path computed by the TSP algorithm.

17. Finally, add the two method calls to the main script to build the TSP graph and execute the TSP algorithm.
