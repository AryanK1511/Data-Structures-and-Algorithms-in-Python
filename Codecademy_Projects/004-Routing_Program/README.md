# Build a Routing Program to Help Vancouver Commuters

Vancouver’s public metro system has asked you to help create a program to help commuters get from one landmark to another. You’ll be building out “SkyRoute,” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat. For the purposes of this project, you can assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.

## Tasks

50/50 Complete

## 1. Define Variables and Greet Users

- Define a variable `landmark_string` that joins all of the landmarks together, each with its corresponding letter of the alphabet from `landmark_choices` on a new line.

- Define a function `greet()` with no parameters. In the function body, print out:
  - "Hi there and welcome to SkyRoute!"
  - "We'll help you find the shortest route between the following Vancouver landmarks:\n" + `landmark_string`

## 2. Create `skyroute()` Function

- Outside `greet()`, define a new function `skyroute()` which will contain the full program. It won’t take any parameters. Inside, call `greet()`.

## 3. Set Up Origin and Destination

- Define the following functions:
  - `set_start_and_end(start_point=None, end_point=None)`: Handles setting the selected origin and destination.
  - `get_start()`: Requests an origin from the user.
  - `get_end()`: Requests a destination from the user.

## 4. Implement `set_start_and_end()`

- In the function body of `set_start_and_end()`, check if `start_point` has a value other than None. If it does:
  - Collect input from the user using the question: "What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': "
  - Handle user input to update `start_point`, `end_point`, or both.

- If `start_point` is None, set `start_point` and `end_point` using `get_start()` and `get_end()`.

- Return `start_point` and `end_point`.

## 5. Implement `get_start()`

- In the function body of `get_start()`, collect user input for the question: "Where are you coming from? Type in the corresponding letter: ".

- Check if `start_point_letter` exists as a key in `landmark_choices`.

  - If it does, set `start_point` equal to `landmark_choices[start_point_letter]` and return `start_point`.
  - If it doesn't, prompt the user for a valid input.

## 6. Implement `get_end()`

- Similar to `get_start()`, collect user input for the question: "Ok, where are you headed? Type in the corresponding letter: ".

- Check if `end_point_letter` exists as a key in `landmark_choices`.

  - If it does, set `end_point` equal to `landmark_choices[end_point_letter]` and return `end_point`.
  - If it doesn't, prompt the user for a valid input.

## 7. Create `new_route()` Function

- Define a function `new_route(start_point=None, end_point=None)`. This function will allow users to search for routes between different landmarks.

## 8. Implement `get_route()`

- Inside `new_route()`, define the function `get_route(start_point, end_point)`.

- Determine the `metro_system` based on the presence of stations under construction.

- Use depth-first search (DFS) to find a possible route between the start and end points.

## 9. Handle Stations Under Construction

- Account for stations under construction by creating a new variable `stations_under_construction` and updating the graph accordingly.

- Create a function `get_active_stations()` to generate an updated graph based on the stations under construction.

## 10. Finalize the Program

- Add features to handle cases such as when the user enters the same station for both origin and destination, and when the user wants to see the list of landmarks again.

- Create a function `goodbye()` to provide a closing message.

## 11. Test and Explore

- Call the `skyroute()` function to start the program.

- Test the program by entering different landmarks, exploring routes, and accounting for stations under construction.

BONUS: Add more features to enhance the program's functionality and user experience.
