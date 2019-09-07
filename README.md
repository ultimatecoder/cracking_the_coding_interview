![Cracking the Coding Interview](assets/images/cracking_the_coding_interview.png)

![Travis CI][travis_ci]

# Cracking the Coding interview 📔

This repository is a collection of [Cracking the coding
interview][cracking_the_coding_interview] questions solutions.  Solutions are
written in [Python][python] programming language.


## Documentation

Read documentation of this project [here](docs/index.md).


## Solutions

* [Arrays and Strings](#arrays-and-strings)
* [Stacks and Queues](#stacks-and-queues)
* [Trees and Graphs](#trees-and-graphs)
* [Recursion and Dynamic Programming](#recursion-and-dynamic-programming)


### Arrays and Strings

| Number | Problem                  | Solution                                                                                 |
|:------:|:------------------------:|:----------------------------------------------------------------------------------------:|
| 1.1    | Is Unique                | [Brute-Force][1_1_brute_force], [Bit array][1_1_bit_array], [Hash-table][1_1_hash_table] |

### Stacks and Queues

| Number | Problem                  | Solution                                                                                 |
|:------:|:------------------------:|:----------------------------------------------------------------------------------------:|
| 3.2    | Stack Min                | [Brute-Force][3_2_brute_force]                                                           |

### Trees and Graphs

| Number | Problem                  | Solution                                                                                 |
|:------:|:------------------------:|:----------------------------------------------------------------------------------------:|
| 4.1    | Route between nodes      | [Depth-First-Search][4_1_dfs]                                                            |

### Recursion and Dynamic Programming

| Number | Problem                  | Solution                                                                                 |
|:------:|:------------------------:|:----------------------------------------------------------------------------------------:|
| 8.3    | Magic Index              | [Distinct elements][8_3_distinct], [Non distinct elements][8_3_non_distinct]    |


[cracking_the_coding_interview]: https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850
[python]: https://python.org
[travis_ci]: https://travis-ci.com/ultimatecoder/cracking_the_coding_interview.svg?branch=master
[1_1_brute_force]: solutions/arrays_and_strings/is_unique.py#L40
[1_1_bit_array]: solutions/arrays_and_strings/is_unique.py#L66
[1_1_hash_table]: solutions/arrays_and_strings/is_unique.py#L109
[3_2_brute_force]: solutions/stacks_and_queues/stack_min.py#L12
[4_1_dfs]: solutions/trees_and_graphs/route_between_nodes.py#L12
[8_3_distinct]: solutions/recursion_and_dynamic_programming/magic_index.py#L16
[8_3_non_distinct]: solutions/recursion_and_dynamic_programming/magic_index.py#L40
