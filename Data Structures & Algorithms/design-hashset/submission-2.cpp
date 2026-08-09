class BST {
private:
    struct TreeNode {
        int key;
        TreeNode* left;
        TreeNode* right;
        TreeNode(int k) : key(k), left(nullptr), right(nullptr) {}
    };

    TreeNode* insert(TreeNode* root, int key){
        if (!root) return new TreeNode(key);

        if (key < root->key) {
            root->left = insert(root->left, key);
        } 
        else if (key > root->key) {
            root->right = insert(root->right, key);
        }
        return root;
    }

    TreeNode* remove(TreeNode* root, int key) {
        if (!root) return nullptr;

        if (key < root->key) {
            root->left = remove(root->left, key);
        } 
        else if (key > root->key) {
            root->right = remove(root->right, key);
        } 
        else {
            if (!root->left) {
                TreeNode* temp = root->right;
                delete root;
                return temp;
            }
            else if (!root->right) {
                TreeNode* temp = root->right;
                delete root;
                return temp;
            }
            TreeNode* temp = minNode(root->right);
            root->key = temp->key;
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

    bool find(TreeNode* root, int key){
        if(!root) return false;
        if (key == root->key) return true;
        return key < root->key ? find(root->left, key) : find(root->right, key);
    }

    TreeNode* root;

public:
    BST(): root(nullptr) {}

    void add(int key) {
        root = insert(root, key);
    }

    void remove(int key) {
        root = remove(root, key);
    }

    bool contains(int key) {
        return find(root, key);
    }
};

class MyHashSet {
private:
    const int size = 10000;
    vector<BST> buckets;

    int hash(int key) {
        return key % size;
    }

public:
    MyHashSet() : buckets(size) {}
    
    void add(int key) {
        int idx = hash(key);
        if (!contains(key)){
            buckets[idx].add(key);
        }
    }
    
    void remove(int key) {
        int idx = hash(key);
        buckets[idx].remove(key);
    }
    
    bool contains(int key) {
        int idx = hash(key);
        return buckets[idx].contains(key);
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */