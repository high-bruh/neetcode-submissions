class BST {
private:
    struct TreeNode {
        int key;
        int val;
        TreeNode* left;
        TreeNode* right;
        TreeNode(int k, int v) : key(k), val(v), left(nullptr), right(nullptr) {}
    };

    TreeNode* insert(TreeNode* root, int key, int val) {
        if (!root) return new TreeNode(key, val);

        if (key < root->key) {
            root->left = insert(root->left, key, val);
        } else if (key > root->key) {
            root->right = insert(root->right, key, val);
        } else {
            root->val = val;  // Update value if key already exists
        }
        return root;
    }

    TreeNode* remove(TreeNode* root, int key) {
        if (!root) return nullptr;

        if (key < root->key) {
            root->left = remove(root->left, key);
        } else if (key > root->key) {
            root->right = remove(root->right, key);
        } else {
            if (!root->left) {
                TreeNode* temp = root->right;
                delete root;
                return temp;
            } else if (!root->right) {
                TreeNode* temp = root->left;
                delete root;
                return temp;
            }

            TreeNode* temp = minNode(root->right);
            root->key = temp->key;
            root->val = temp->val;
            root->right = remove(root->right, temp->key);
        }
        return root;
    }

    TreeNode* minNode(TreeNode* root) {
        while (root->left) {
            root = root->left;
        }
        return root;
    }

    TreeNode* find(TreeNode* root, int key) {
        if (!root) return nullptr;
        if (key == root->key) return root;
        return key < root->key ? find(root->left, key) : find(root->right, key);
    }

    TreeNode* root;

public:
    BST() : root(nullptr) {}

    void put(int key, int val) {
        root = insert(root, key, val);
    }

    void removeKey(int key) {
        root = remove(root, key);
    }

    int get(int key) {
        TreeNode* node = find(root, key);
        return node ? node->val : -1;
    }

    bool contains(int key) {
        return find(root, key) != nullptr;
    }
};

class MyHashMap {
private:
    const int size = 10000;
    vector<BST> buckets;

    int hash(int key) {
        return key % size;
    }

public:
    MyHashMap() : buckets(size) {}

    void put(int key, int value) {
        int idx = hash(key);
        buckets[idx].put(key, value);
    }

    int get(int key) {
        int idx = hash(key);
        return buckets[idx].get(key);
    }

    void remove(int key) {
        int idx = hash(key);
        buckets[idx].removeKey(key);
    }
};
