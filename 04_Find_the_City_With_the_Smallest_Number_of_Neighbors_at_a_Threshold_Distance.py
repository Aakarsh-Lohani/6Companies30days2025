# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

# Time Complexity : O(n^3)
# Space Complexity : O(n^2)
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Populate the distance matrix with the edge weights
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Find the city with the smallest number of reachable cities
        min_reachable = float('inf')
        for i in range(n):
            reachable = sum(d <= distanceThreshold for d in dist[i])
            if reachable <= min_reachable:
                min_reachable = reachable
                city = i

        return city