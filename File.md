## [158 Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) :triangular_flag_on_post:  :green_book:

We design the following class member variables to store the states:
1. *buffer*: An array of size 4 to store data returned by `read4` temporarily. If the characters were into the buffer and were not used partially, they will be used in the next call.
2. *offset*: Used to keep track of the offset index where the data begins in the next `read` call. The buffer could be read partially and therefore leaving some data behind.
3. *buffsize*: The real buffer size that store the actual data. If `buffsize>0`, that mean thers is partial data left in buffer from the last `read` call and we should consume it before calling `read4` again. On the other hand, if `buffsize==0`, it means there is no data left in buffer.
   
Java

Given answer:
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

My answer:
```Java
public class Solution extends Reader4 {
    char[] buffer=new char[4];
    int offset=0;
    int buffsize=0;
    
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    public int read(char[] buf, int n) {
        int count=0;
        while(count<n){
            while(count<n && buffsize>0){
                buf[count++]=buffer[offset++];
                buffsize--;
                if(buffsize==0)  offset=0;
            }
            if(buffsize==0){
                buffsize=read4(buffer);
                if(buffsize==0)
                    break;
            }
        }
        return count;
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