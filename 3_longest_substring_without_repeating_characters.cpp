class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        const size_t n = s.size();
        int longest = 0;

        for (int i = 0; i < n; ++i) {
            int length = 1;
            vector<char> visited = {s[i]};

            for (int j = i+1; j < n; ++j) {
                bool temp = false;

                for (char c : visited) {
                    if (s[j] == c) {
                        temp = true;
                        break;
                    }
                }

                visited.push_back(s[j]);

                if (temp)
                    break;
                else
                    ++length;
            }

            longest = (length > longest ? length : longest);
        }

        return longest;
    }
};