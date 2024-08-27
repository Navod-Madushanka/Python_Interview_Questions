class Disjoint:
    def __init__(self, n):
        # Initialize the parent and rank arrays
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        # Find the representative of the set containing 'u'
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        # Union by rank of two sets represented by 'u' and 'v'
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank heuristic
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


if __name__ == "__main__":
    # Create a Disjoint Set with 5 elements (0 to 4)
    ds = Disjoint(5)

    # Union some sets
    ds.union(0, 2)
    ds.union(4, 2)
    ds.union(3, 1)

    # Find representatives (with path compression)
    print(ds.find(4))  # Output will be the root of the set containing element 4 (which should be 0 or 2)
    print(ds.find(3))  # Output will be the root of the set containing element 3 (which should be 1)

    # Check if two elements are in the same set
    print(ds.find(0) == ds.find(4))  # True, since 0 and 4 are connected
    print(ds.find(1) == ds.find(4))  # False, since 1 and 4 are in different sets

