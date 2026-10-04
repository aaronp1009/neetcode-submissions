class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        def find_max(start_index: int, end_index: int) -> int:
            max_val = arr[start_index]
            for i in range(start_index, end_index):
                if arr[i] > max_val:
                    max_val = arr[i]
            return max_val
        
        n = len(arr)
        ans = [-1] * n

        for i in range(n):
            if i == (n - 1):
                continue
            ans[i] = find_max(i+1, n)
        return ans


