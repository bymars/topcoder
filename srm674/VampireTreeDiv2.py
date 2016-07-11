modulo = 1000000007
maxInt = 100

class VampireTreeDiv2:
    def countMinSamples(self, A, B):
        n = len(A) + 1
        children = [0] * n
        special = []
        overall_min_count = maxInt
        overall_ways = 0

        for i in range(n):
            children[i] = []
        for i in range(n-1):
            if B[i] == -1:
                children[A[i]].append(i+1)
            else:
                special.append(i+1)

        dp = [0] * n
        for i in range(n):
            dp[i] = [-1,0] * 2

        t = len(special)
        for mask in range(1 << t):
            pick_option = [0] * n
            invalid = 0
            # Set pick_option
            for i in range(t):
                x = special[i]
                p1 = A[x-1]
                p2 = B[x-1]
                if mask & 1 << i == 0:
                    if pick_option[x] == 1 or pick_option[p1] == -1 or pick_option[p2] == -1:
                        invalid = 1
                        break
                    pick_option[p1] = pick_option[p2] = 1
                    pick_option[x] = -1
                else:
                    pick_option[special[i]] = 1
            if invalid == 1:
                continue

            # Calculate [min_count, ways] for each vertex from bottom to top
            # must = 1, pick_option[vertex] = 1 or 0, F(i, 0) + 1
            # must = 1, pick_option[vertex] = -1, any value is ok since dp[vertex][1] will not be used.
            # must = 0, pick_option[vertex] = 1, F(i, 0) + 1
            # must = 0, pick_option[vertex] = -1, F(i, 1)
            # must = 0, pick_option[vertex] = 0, F(i, 0) + 1 or F(i, 1)
            for i in range(n)[::-1]:
                count_must = count_may = 0
                ways_must = ways_may = 1

                for j in children[i]:
                    count_must += dp[j][1][0]
                    ways_must *= dp[j][1][1] % modulo
                    count_may += dp[j][0][0]
                    ways_may *= dp[j][0][1] % modulo

                if pick_option[i] != -1:
                    dp[i][1] = [1+count_may, ways_may]

                if pick_option[i] == 1:
                    dp[i][0] = [1+count_may, ways_may]
                elif pick_option[i] == -1:
                    dp[i][0] = [count_must, ways_must]
                else:
                    if count_must > 1+count_may:
                        dp[i][0] = [1+count_may, ways_may]
                    elif count_must < 1+count_may:
                        dp[i][0] = [count_must, ways_must]
                    else:
                        dp[i][0] = [count_must, (ways_must+ways_may) % modulo]

            [min_count, ways] = dp[0][0]
            # Add special nodes' result
            for i in range(t):
                x = special[i]
                min_count += dp[x][0][0]
                ways *= dp[x][0][1]

            if min_count < overall_min_count:
                overall_min_count = min_count
                overall_ways = ways
            elif min_count == overall_min_count:
                overall_ways += ways % modulo
        return overall_ways
