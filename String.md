## [1078 Occurrences After Bigram](https://leetcode.com/problems/occurrences-after-bigram/)

> Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

> For each such occurrence, add "third" to the answer, and return the answer.

In C++, we usually use `istringstream` to change a long string into stream and split it.

In this case, we set a variable `curr` to notate the current word, and set 2 other variables to notate `first` and `second`.

When `pprev==first && prev==second`, we know `curr` is that we want.

Time O(n), space O(n)

```Cpp


class Solution {
public:
    vector<string> findOcurrences(string text, string first, string second) {
        vector<string> ans;

        istringstream iss(text);
        string pprev, prev, curr;
        while(iss>>curr){
            if(pprev==first && prev==second)
                ans.push_back(curr);
            pprev=prev;
            prev=curr;
        }
        return ans;
    }
};

```

```Java

class Solution {
    public String[] findOcurrences(String text1, String first, String second) {
        if(text1==null || first==null || second==null)
            return new String[0];
        
        String[] text=text1.split(" ", 0);
        if(text.length<3)   return new String[0];
        ArrayList<String> ans=new ArrayList<>();
        
        for(int i=2; i<text.length; ++i){
            if(text[i-2].equals(first) && text[i-1].equals(second))
                ans.add(text[i]);
        }
        String[] a=new String[ans.size()];
        ans.toArray(a);
        return a;
        
    }
}
```

