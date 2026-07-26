set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of sets
union_result = set1.union(set2)

# Intersection of sets
intersection_result = set1.intersection(set2)

# Difference of sets
difference_result = set1.difference(set2)

print(union_result)
print(intersection_result)
print(difference_result)

# Output:
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {1, 2}

my_set = {1, 2, 3}

my_set.add(4)
print(my_set) # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set) # Output: {1, 3, 4}

# Instructions
# Let’s go back to fruits! 🫐🍇🍌🍓🍒

# Grocery shopping is great until you forget what was on your list. 😥

# Before you head out, your best friend ask you to pick up some fruit for her too. Let's combine the lists!

# Create two sets representing your favorite fruits and your best friend's favorite fruits.
# Print the union of the two sets.
# Print the intersection of the two sets.
# Have fun with it, check if the same fruit is in both sets or see the <difference> in both sets.

# Remember: tomatoes are fruits! 🍅

my_favorite_fruits = {"apple", "banana", "cherry", "date"}
best_friend_favorite_fruits = {"banana", "kiwi", "mango", "date"}

print("Union of favorite fruits:", my_favorite_fruits.union(best_friend_favorite_fruits))
print("Intersection of favorite fruits:", my_favorite_fruits.intersection(best_friend_favorite_fruits))
print("Difference in my favorite fruits:", my_favorite_fruits.difference(best_friend_favorite_fruits))