## [158 Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) :triangular_flag_on_post: 

Too diffiicult, remember the code = =!

Java

```Java
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char[] buf); 
 */
public class Solution extends Reader4 {
    private char[] buff=new char[4];    // temp array to store read4
    private int buffPtr=0;  //the pointer of buff
    private int buffCnt=0;  //count how many are read
    
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    public int read(char[] buf, int n) {
        int ptr=0;
        while(ptr<n)
        {
            // no data left, read data
            if(buffPtr==0)
                buffCnt=read4(buff);
            // no more data
            if(buffCnt==0)  break;
            //shuffle,
            while(ptr<n && buffPtr<buffCnt){
                buf[ptr++]=buff[buffPtr++];
            }
            if(buffPtr>=buffCnt)    buffPtr=0;
        }
        return ptr;
    }  
}
```

C++

```cpp
// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int ptr=0;
        while(ptr<n){
            if(buff_ptr==0){
                buff_cnt=read4(buff);
            }
            if(buff_cnt==0) break;
            while(ptr<n && buff_ptr<buff_cnt){
                buf[ptr++]=buff[buff_ptr++];
            }
            if(buff_ptr>=buff_cnt)  buff_ptr=0;
        }
        return ptr;
    }
private:
    char buff[4]={};
    int buff_ptr=0;
    int buff_cnt=0;
};
```