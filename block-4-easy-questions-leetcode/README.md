# Block 4: Easy LeetCode Practice

Core Python theory (blocks 1-3) is done. From here, remaining theory gets picked up
on demand, driven by whatever a question actually requires, instead of front-loading it.

The goal of this block: build pattern recognition on easy-tier interview questions.
Solve enough of each pattern that the approach becomes automatic, not something to
rederive from scratch every time.

## Patterns to cover

Grouped by the technique they drill, not by topic. Many easy questions are the same
core patterns wearing different clothes; recognizing the pattern is the actual skill.
Every problem listed below is Easy difficulty.

- **Two pointers**: Two Sum II (sorted), Valid Palindrome, Merge Sorted Array, Remove Duplicates from Sorted Array, Move Zeroes, Reverse String
- **Fast & slow pointers**: Linked List Cycle, Middle of the Linked List
- **Sliding window**: Best Time to Buy and Sell Stock, Contains Duplicate II, Maximum Average Subarray I
- **Hashing / frequency counting**: Two Sum, Valid Anagram, Contains Duplicate, First Unique Character in a String, Ransom Note, Isomorphic Strings, Intersection of Two Arrays, Happy Number
- **Stack**: Valid Parentheses, Baseball Game, Remove All Adjacent Duplicates In String, Min Stack, Implement Queue using Stacks
- **Binary search**: Binary Search, Search Insert Position, First Bad Version, Sqrt(x)
- **Linked list manipulation**: Reverse Linked List, Merge Two Sorted Lists, Remove Duplicates from Sorted List
- **Tree traversal (DFS/BFS)**: Maximum Depth of Binary Tree, Invert Binary Tree, Same Tree, Symmetric Tree, Path Sum
- **Recursion basics**: Fibonacci Number, Climbing Stairs, Power of Two/Three/Four
- **Prefix sums / running totals**: Running Sum of 1d Array, Find Pivot Index
- **Intervals**: Meeting Rooms, Summary Ranges
- **Matrix / grid traversal**: Flood Fill, Island Perimeter, Transpose Matrix
- **Bit manipulation**: Single Number, Number of 1 Bits, Counting Bits, Missing Number
- **Greedy basics**: Assign Cookies, Best Time to Buy and Sell Stock
- **Math basics**: Palindrome Number, Plus One, FizzBuzz, Pascal's Triangle, Roman to Integer
- **Counting / majority element**: Majority Element (Boyer-Moore voting)

## How this block is organized

Solutions live in a directory per data structure (`arrays/`, `linkedlists/`), with one
`.py` file per problem. Problems with more than one approach keep each approach in the
same file, labelled, so the tradeoff (e.g. time vs. space) is visible side by side.
Linked list problems are self-contained: the file carries its own list implementation
alongside the solution method, so it runs without any imports.

The pattern list above is the plan; the directories fill in as problems get solved.

## Solved so far

- **Hashing / frequency counting**: [Two Sum](arrays/twosum.py), [Valid Anagram](arrays/valid-anagram.py) (two approaches, the second in O(1) space), [Contains Duplicate](arrays/contains-duplicate.py)
- **Fast & slow pointers**: [Linked List Cycle](linkedlists/cycle_detection.py)
- **Strings**: [Longest Common Prefix](arrays/longest_prefix.py)
