# leetcode-python
Python solutions for LeetCode problems.

## Running solution files

From the project root:

```bash
# Easy
python3 Top_Interview_150/Easy/count_complete_tree_nodes.py
python3 Top_Interview_150/Easy/two_sum.py

# Medium
python3 Top_Interview_150/Medium/remove_duplicates_from_sorted_array_II.py

# Hard
python3 Top_Interview_150/Hard/candy.py
```

## Running tests

**All tests:**
```bash
python3 -m unittest discover -s Top_Interview_150/tests -p "test_*.py" -v
```

**Specific test file:**
```bash
python3 -m unittest Top_Interview_150.tests.test_001_two_sum -v
# or run the file directly:
python3 Top_Interview_150/tests/test_001_two_sum.py -v
```