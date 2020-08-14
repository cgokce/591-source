HashSet:
- Access time O(1) average
- Duplicates in an array/string
- Counting values in an array/string
- Python:

        hset = set()
        hset.add(item)
        hset.remove(item)
        check -> if val in hset:
        iter -> for item in hset:


HashMap:
- Save the values/index pairs accessible
    - Use values to access to index later with O(1) time

- Python:

        hmap = {}
        hmap[key] = val
        check -> if key in hmap:
        iter -> for i, key in enumerate(hmap):
                -> for key in hmap.keys():
