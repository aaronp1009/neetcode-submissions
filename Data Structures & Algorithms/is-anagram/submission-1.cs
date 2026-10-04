public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        var counts = new Dictionary<char, int>();

        // Count characters in s
        foreach (char c in s) {
            if (counts.ContainsKey(c)) counts[c]++;
            else counts[c] = 1;
        }

        // Decrement counts for t
        foreach (char c in t) {
            if (!counts.ContainsKey(c)) return false; // Char in t not in s
            counts[c]--;
            if (counts[c] < 0) return false; // More occurrences in t than s
        }

        return true;
    }
}   