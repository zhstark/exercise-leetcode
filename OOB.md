## 432 All O(1) data structure

Design a class in which insertion, deletion, find_Max, find_Min all in O(1) time.

```Cpp

class AllOne{
public:
    AllOne();
    ~AllOne();
    void inc(string key){
        if(!bucketOfKey.count(key))
            bucketOfKey[key]=buckets.insert(buckets.begin(), {0, {key}});
        auto next=bucketOfKey[key], bucket=next++;
        if(next==buckets.end() || next->value >bucket->value+1)
            next=buckets.insert(next, {bucket->value+1, {}});
        next->keys.insert(key);
        bucketOfKey[key]=next;

        bucket->keys.erase(key);
        if(bucket->keys.empty())
            buckets.erase(bucket);
    }

    void dec(string key){
        if(!bucketOfKey.count(key))
            return;
        
        auto prev=bucketOfKey[key], bucket=prev--;
        bucketOfKey.erase(key);
        if(bucket->val>1){
            if(bucket==bucket.begin() || prev->value<bucket->value-1)
                prev=buckets.insert(bucket, {bucket->value-1, {}});
            prev->keys.insert(key);
            bucketOfKey[key]=prev;
        }

        bucket->keys.erase(key);
        if(bucket->keys.empty())
            buckets.erase(bucket);
    }

    string getMaxKey(){
        return buckets.empty() ? "" : *(buckets.rbegin()->keys.begin());
    }

    string getMinKey(){
        return buckets.empty() ? "" : *(buckets.begin()->keys.begin());
    }
private:
    struct Bucket{
        int value;
        unordered_set<string> keys;
    };
    list<Bucket> buckets;
    unordered_map<string, list<Bucket>::iterator> bucketOfKey;
};


```