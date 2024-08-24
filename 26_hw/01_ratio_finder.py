# There is an array consisting of triples.
# Each triple represents original unit, destination unit
# and multiplier between them.
#
# Write a function that takes the array and two units
# and returns the conversion rate between them
# using DSU data structure.
#
# Example:
# Input: [("foot", "yard", 0.333), ("foot", "inch", 12)], "inch", "yard"
# Output: 0.0277


def ratio_finder_dsu(rates, start, end):
    dsu = {}
    conversions = {}

    def create(x):
        dsu[x] = x
        conversions[x] = 1.0

    def find(x):
        if dsu[x] == x:
            return x
        root = find(dsu[x])
        dsu[x] = root
        conversions[x] *= conversions[root]
        return root

    def union(x, y, rate):
        root_x = find(x)
        root_y = find(y)
        dsu[root_y] = root_x
        conversions[root_y] = conversions[x] * rate / conversions[y]

    for orig, dest, rate in rates:
        if orig not in dsu:
            create(orig)
        if dest not in dsu:
            create(dest)
        union(orig, dest, rate)

    start_root, start_rate = dsu[start], conversions[start]
    end_root, end_rate = dsu[end], conversions[end]

    if start_root != end_root:
        return None

    return end_rate / start_rate

# O(V + E) -- time
# O(V + E) -- space
