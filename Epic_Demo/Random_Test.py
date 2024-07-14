import random

# Define a custom exception for when the full set is not collected
class IncompleteSetException(Exception):
    pass

def find_full_set_index(numbers):
    # Use a set to keep track of unique numbers collected
    collected_numbers = set()
    for index, number in enumerate(numbers):
        # Add the number to the set
        collected_numbers.add(number)
        # Check if we have collected all numbers from 1 to 4
        if collected_numbers == {1, 2, 3, 4}:
            return index  # Return the index where the collection is complete
    raise IncompleteSetException("Not all numbers were collected")

i = 0  # Initialize i
while i < 30:  # Set the loop to run 30 times
    random_numbers = [random.randint(1, 4) for _ in range(10)]
    print(random_numbers, end=" ")

    try:
        # Find the index when all numbers from 1 to 4 have been collected
        full_set_index = find_full_set_index(random_numbers)
        print("[第", full_set_index + 1, "次蒐集到]")  # Human-readable index (1-based)
    except IncompleteSetException:
        print("[null]")  # Print 'null' if the exception is raised

    i += 1  # Increment i to prevent an infinite loop

"""
import java.util.HashSet;
import java.util.Random;
import java.util.Set;

// Define a custom exception for when the full set is not collected
class IncompleteSetException extends Exception {
    public IncompleteSetException(String message) {
        super(message);
    }
}

public class FullSetFinder {
    public static void main(String[] args) {
        Random random = new Random();
        int i = 0;  // Initialize i
        while (i < 30) {  // Set the loop to run 30 times
            int[] randomNumbers = random.ints(10, 1, 5).toArray();  // Generate an array of 10 random numbers between 1 and 4
            System.out.print("[");
            for (int num : randomNumbers) {
                System.out.print(num + " ");
            }
            System.out.print("] ");

            try {
                // Find the index when all numbers from 1 to 4 have been collected
                int fullSetIndex = findFullSetIndex(randomNumbers);
                System.out.println("[第 " + (fullSetIndex + 1) + " 次蒐集到]");  // Human-readable index (1-based)
            } catch (IncompleteSetException e) {
                System.out.println("[null]");  // Print 'null' if the exception is raised
            }

            i++;  // Increment i to prevent an infinite loop
        }
    }
    public static int findFullSetIndex(int[] numbers) throws IncompleteSetException {
        Set<Integer> collectedNumbers = new HashSet<>();
        for (int i = 0; i < numbers.length; i++) {
            collectedNumbers.add(numbers[i]);
            // Check if we have collected all numbers from 1 to 4
            if (collectedNumbers.size() == 4 && collectedNumbers.contains(1) 
                && collectedNumbers.contains(2) && collectedNumbers.contains(3) 
                && collectedNumbers.contains(4)) {
                return i;  // Return the index where the collection is complete
            }
        }
        throw new IncompleteSetException("Not all numbers were collected");
    }
}
"""