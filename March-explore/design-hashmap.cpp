class MyHashMap {
public:
    int arr[100001];//we use array here as map
    /** Initialize your data structure here. */
    MyHashMap() {
       for(int i=0;i<100001;i++){
           arr[i]=-1;//initialize as -1 because it will store default as element is not present in array so return -1.
       }
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        arr[key]=value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        return arr[key];
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        arr[key]=-1;
    }
};