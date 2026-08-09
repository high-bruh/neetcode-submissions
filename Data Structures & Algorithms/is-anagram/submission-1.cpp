class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        int dict[26];
        memset(dict, 0, sizeof(dict));

        for(int i  = 0; i < s.size(); i++){
            dict[s[i] - 'a'] += 1;
        }
        for(int i  = 0; i < t.size(); i++){
            dict[t[i] - 'a'] -= 1;
        }
        for(int i = 0; i < 26; i ++){
            if(dict[i] != 0) return false;
        }
        return true;
    }
};
