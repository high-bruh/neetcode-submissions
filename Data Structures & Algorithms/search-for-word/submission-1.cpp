class Solution {
public:
    int R, C;

    bool exist(vector<vector<char>>& board, string word) {
        R = board.size(); C = board[0].size();

        for (int r = 0; r < R; r ++) {
            for (int c = 0; c <  C; c++){
                if (dfs(r, c, 0, word, board)){
                    return true;
                }
            }
        }

        return false;

    }

    bool dfs(int r, int c, int i, string word, vector<vector<char>>& board){
        if (i == word.size()) return true;

        if (r < 0  || c < 0 || r >= R || r >= C || word[i] != board[r][c] || board[r][c] == '.') return false;

        board[r][c] = '.';
        bool res = ( dfs(r + 1, c, i + 1, word, board) ||
                dfs(r, c + 1, i + 1, word, board) ||
                dfs(r, c - 1, i + 1, word, board) ||
                dfs(r - 1, c, i + 1, word, board));

        board[r][c] = word[i];
        return res;

    }
};
