## Standard code

Union Find Set has two basic functions:

1. `find(x)`: find the root of x
2. `union(x, y)`: merge 2 clusters

Usually we use a class to represent an union find set. Python code:

```Python
# rank is used to reduce the cost of union
class UnionFindSet(n):
    def __init__(self):
        parent=List(range(1,n+1))
        rank=[0]*n
    def find(x):
        if x!=parent[x]:
            parent[x]=find(parent[x])
        return parent[x]

    def union(x,y):
        rootx, rooty=parent[x], parent[y]
        if rank[rootx]>rank[rooty]:
            parent[rooty]=rootx
        if rank[rootx]<rank[rooty]:
            parent[rootx]=rooty
        if rank[rootx]==rank[rooty]:
            parent[rooty]=rootx
            rank[rootx]++
```

## [721 Accounts Merge](https://leetcode.com/problems/accounts-merge/)  :triangular_flag_on_post:

> Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

> Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

> After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Since in this case, the elements are not represented by integer but string. It can be a little tricky to use standard method. So I used hash map to store the parent relationship.

The method can be considered as 3 steps:

1. initialize, make every elements' parent be themselves, and link emails to the person
2. build union find relationship. all emails will link with each to the root email, than each tree will be one person's all emails.
3. format

Some details are writen in the Java code

Java

```Java
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        // the basic idea is to use union find algorithm. 
        // the first step to build 2 union find set
        // one is to link all the emails to one email
        // the other one is to link the leader email to the name
        // in this case, we use map to represent a union find set
        // relationship key-->value
        //            child-->parent
        Map<String, String> parents=new HashMap<>();
        Map<String, String> owner=new HashMap();
        
        for(List<String> account: accounts){
            for(int i=1; i<account.size();++i){
                parents.put(account.get(i), account.get(i));
                owner.put(account.get(i), account.get(0));
            }
        }
        
        // Link all the emails which belong to the same owner to one email
        for(List<String> a: accounts){
            String p=find(a.get(1), parents);
            for(int i=2; i<a.size(); ++i){
                parents.put(find(a.get(i), parents), p);
            }  
        }
        
        // the union is to arrange the emails to eliminate the duplicate
        // the key is the leader email, the value(tree) is all the other child emails
        // Since the emails are supposed to sorted in order, so we use treeset to sort it. and when putting the elements into the treeset, we are supposed to put the leader email as well.
        Map<String, TreeSet<String>> union=new HashMap();
        for(List<String> a:accounts){
            String p=find(a.get(1), parents);
            if(!union.containsKey(p))
                union.put(p, new TreeSet<>());
            for(int i=1; i<a.size(); ++i){
                union.get(p).add(a.get(i));
            }
        }
        
        // The last step is to make it into the askced format
        List<List<String>> res=new ArrayList();
        for(String k: union.keySet()){
            List<String> temp=new ArrayList();
            temp.add(owner.get(k));
            temp.addAll(new ArrayList<String>(union.get(k)));
            res.add(temp);
        }
        
        return res;
    }
    
    private String find(String s, Map<String, String> p){
        return p.get(s)==s? s:find(p.get(s), p);
    }
}
```
