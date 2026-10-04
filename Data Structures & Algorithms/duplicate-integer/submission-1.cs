public class Solution {
    public bool hasDuplicate(int[] nums) {
        var numbers = new HashSet<int>();
        foreach (int num in nums)
        {
            if (!numbers.Add(num))
            {
                return true;
            }
        }
        return false;
    }
}