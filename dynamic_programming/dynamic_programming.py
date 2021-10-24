"""
Dynamic Programming

- Use Cases:
    - Find total number of options (90%)
    - Find maximum value (80%)
    - Find feasibility of an option (80%)

- Not Suited Use Cases:
    - List all options (99%)
    - The data is not sorted (except kanpsack, 60-70%)
    - The worst case run time is polynomial already (80%)

- Four Elements for Dynamic Programming:
    - State (definition of the sub-program)
    - Function (recursion)
    - Initialization
    - Answer

- Complexity:
    - Time: O(totaal states * time for each state)
    - Space: O(total states) without sliding window optimization; O(total states / n) using sliding window optimization

"""