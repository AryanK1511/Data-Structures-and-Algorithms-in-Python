# Blossom - Flower Meanings Hash Map Project

Blossom is a project designed to provide rapid access to the meanings of various flowers by utilizing a hash map with separate chaining. This project involves implementing a hash map data structure to correlate flower names with their corresponding meanings, while also handling potential collisions through separate chaining using linked lists.

## Building Out The Hash Map

1. **Introduction**: Blossom's core data structure is a key-value store that associates common flower names with their floral meanings. The implementation involves creating a hash map with separate chains of linked lists for each index.

2. **HashMap Class**: We begin by defining the `HashMap` class to encapsulate the hash map functionality.

3. **Array Setup**: The hash map relies on an array as its base structure. We enforce the array's size to facilitate better management. The `HashMap` constructor takes a size parameter, storing it as `self.array_size`, and initializes a list of None objects of length `size` within `self.array`.

4. **Hash Function**: To implement the hash map, we require a hash function that calculates a numeric representation for a given string key. This function, named `.hash()`, takes `self` and `key` as parameters. It computes the hash code by summing the character encodings of each character in the key string.

5. **Compression Function**: Additionally, we need a compression function, `.compress()`, that reduces the hash code to an array index. This method accepts a `hash_code` parameter and returns the remainder of dividing `hash_code` by `self.array_size`.

6. **Assignment Method**: We proceed to implement the `.assign()` method, which allows us to add key-value pairs to the hash map. This method takes three parameters: `self`, `key`, and `value`. It calculates the hash code using `.hash(key)` and derives the array index using `.compress(hash_code)`, saving the result in `array_index`.

7. **Storing Data**: At the array index, we store the key and value as a list: `[key, value]`.

8. **Retrieval Method**: Next, we create the `.retrieve()` method for retrieving values based on a given key. This method takes two parameters: `self` and `key`. It calculates the hash code using `.hash(key)` and obtains the array index using `.compress(hash_code)`.

9. **Retrieving Data**: The value in `self.array` at `array_index` is stored in a variable called `payload`.

10. If `payload` is not None, we know it's a list in the format `[key, value]`. We compare the first item (`payload[0]`) with the key and return the second item (`payload[1]`) if they match.

11. If `payload` is None or the first item is not the same as the key, we return None.

## Adding Separate Chaining

12. **Importing Linked List**: We incorporate separate chaining to handle collisions. The linked list and node library is imported at the top of the script using `from linked_list import Node, LinkedList`.

13. **LinkedLists in HashMap**: We modify the `HashMap.__init__` method to use linked lists for separate chaining. `self.array` is now a list of `LinkedList` objects, each serving as a chain at a specific array index.

## Separate Chaining in Assignment

14. **Assigning Data**: In the `.assign()` method, after obtaining `array_index`, we create a new `Node` object with value `[key, value]` and assign it to the variable `payload`.

15. **Checking Existing Keys**: To ensure we don't duplicate keys, we check if the key exists in the linked list. `self.array[array_index]` is saved in `list_at_array`.

16. **Iterating Through List**: We iterate through `list_at_array` using a loop, checking if the key (element at index 0) matches the key we want to assign.

17. **Overwriting Value**: If a matching key is found, we update its value.

18. **Inserting into LinkedList**: If no matching key is found after iterating, we use `list_at_array.insert()` to insert the payload into the linked list.

## Separate Chaining in Retrieval

19. **Updating Retrieval**: We enhance the `.retrieve()` method to work with separate chaining. After calculating `array_index`, we retrieve the `LinkedList` object at that index, storing it in `list_at_index`.

20. **Iterating Through LinkedList**: Similar to the `.assign()` method, we iterate through `list_at_index`, checking each key in the linked list to see if it matches the desired key.

21. **Returning Value**: If a matching key is found, we return its associated value (at index 1 in the node's value). Otherwise, we return None.

## Adding Flower Definitions

22. **Importing Definitions**: Flower definitions are imported using `from blossom_lib import flower_definitions`.

23. **Creating HashMap**: We create a new instance of the `HashMap` called `blossom`, with its array size set to match the length of `flower_definitions`.

24. **Assigning Definitions**: For each element in `flower_definitions`, we use `.assign()` to associate the value (index 1) with its key (index 0).

25. **Usage Example**: We demonstrate the functionality by looking up the meaning of a flower using `blossom.retrieve('daisy')` and printing the result. Further exploration involves attempting to retrieve other flower meanings and considering how to add new entries.

Feel free to explore the project, experiment with additional flowers, and discover their meanings using the implemented `HashMap`.
