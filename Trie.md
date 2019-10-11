## [211 Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design) :triangular_flag_on_post:


```Java
class WordDictionary {

    /** Initialize your data structure here. */
    public class TrieNode{
        public TrieNode[] children=new TrieNode[26];
        public String item="";
    }
    
    private TrieNode root=new TrieNode();
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        TrieNode node=root;
        for(char c: word.toCharArray()){
            if(node.children[c-'a']==null){
                node.children[c-'a']=new TrieNode();
            }
            node=node.children[c-'a'];
        }
        node.item=word;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return match(word.toCharArray(), 0, root);
    }
    public boolean match(char[] chars, int index, TrieNode node){
        if(index==chars.length)
            return !node.item.equals("");// notice that here can not use "="
        
        if(chars[index]!='.'){
            return node.children[chars[index]-'a']!=null && match(chars, index+1, node.children[chars[index]-'a']);
        }
        else{
            for(int i=0; i<26; ++i){
                if(node.children[i]!=null)
                    if(match(chars, index+1, node.children[i]))
                        return true;
            }
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
```