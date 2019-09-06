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

## [125 Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  :triangular_flag_on_post:

> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

> Note: For the purpose of this problem, we define empty string as valid palindrome.

In order to save space, we just use 2 pointers, one from the string's begin to end, the other pass from the end to the begin.

C++

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        for(int i=0, j=s.size(); i<j; ++i,--j){
            while(!isalnum(s[i]) && i<j)    ++i;
            while(!isalnum(s[j]) && i<j)    --j;
            if(tolower(s[i])!=tolower(s[j]))    return false;
        }
        return true;
    }
};
```

Java

```Java
class Solution {
    public boolean isPalindrome(String s) {
        for(int i=0, j=s.length()-1; i<j; ++i, --j){
            while(!Character.isLetterOrDigit(s.charAt(i)) &&i <j)   ++i;
            while(!Character.isLetterOrDigit(s.charAt(j)) && i<j)   --j;
            if(Character.toLowerCase(s.charAt(i))!=Character.toLowerCase(s.charAt(j))) 
                return false;
        }
        return true;
    }
}
```

## [680 Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)  :triangular_flag_on_post:

> Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Just check it step by step using 2 pointers like the former one. If we meet unmatched characters, now we just need to check whether `S(i+1)_j` and `Si_(j-1)` are palindromes.

Java

```Java
class Solution {
    public boolean validPalindrome(String s) {
        int l=0;
        int r=s.length()-1;
        while(l<r){
            if(s.charAt(l) != s.charAt(r))
                return isPalindrome(s, l+1, r) || isPalindrome(s, l, r-1);
            l++;
            r--;
        }
        return true;
    }
    public boolean isPalindrome(String s, int l, int r){
        while(l<r){
            if(s.charAt(l)!=s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```
