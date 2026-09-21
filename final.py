import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        heap = []

        for r in range(m):
            heap.append((heightMap[r][0], r, 0))
            heap.append((heightMap[r][n - 1], r, n - 1))
            heightMap[r][0] = heightMap[r][n - 1] = -1

        for c in range(1, n - 1):
            heap.append((heightMap[0][c], 0, c))
            heap.append((heightMap[m - 1][c], m - 1, c))
            heightMap[0][c] = heightMap[m - 1][c] = -1

        heapq.heapify(heap)
        water = 0
        push = heapq.heappush
        pop = heapq.heappop

        while heap:
            h, r, c = pop(heap)

            if r and heightMap[r - 1][c] != -1:
                x = heightMap[r - 1][c]
                heightMap[r - 1][c] = -1
                if x < h:
                    water += h - x
                    x = h
                push(heap, (x, r - 1, c))

            if r + 1 < m and heightMap[r + 1][c] != -1:
                x = heightMap[r + 1][c]
                heightMap[r + 1][c] = -1
                if x < h:
                    water += h - x
                    x = h
                push(heap, (x, r + 1, c))

            if c and heightMap[r][c - 1] != -1:
                x = heightMap[r][c - 1]
                heightMap[r][c - 1] = -1
                if x < h:
                    water += h - x
                    x = h
                push(heap, (x, r, c - 1))

            if c + 1 < n and heightMap[r][c + 1] != -1:
                x = heightMap[r][c + 1]
                heightMap[r][c + 1] = -1
                if x < h:
                    water += h - x
                    x = h
                push(heap, (x, r, c + 1))

        return water
