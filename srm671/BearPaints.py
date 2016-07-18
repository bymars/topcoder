class BearPaints:
    def maxArea(self, W, H, M):
        if W >= M or H >= M:
            return M
        min_H = M // W
        result = min(H * W, min_H * W)
        for i in range(min_H + 1, H + 1):
            min_W = min(M // i, W)
            result = max(result, min_W * i)
        return result


