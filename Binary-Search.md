## 注意事项：

1. **在`while`循环里面，`l<=r`**
2. mid 取值：`mid=l+(r-l)>>1`
3. 更新的时候， **l=mid+1, not l=mid**，r 同理


## 花式二分法

### 查找第一个 值 等于给定值的元素

```py
def BS_1(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)>>1
        if array[mid]>value:
            r=mid-1
        elif array[mid]<value:
            l=mid+1
        else:
            if mid==0 or array[mid-1]!=value:
                return mid
            else:
                r=mid-1
    
    return -1
```

### 查找最后一个值等于给定值的元素

```py
def BS_2(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)>>1
        if array[mid]>value:
            r=mid-1
        elif array[mid]<value:
            l=mid+1
        else:
            if mid==len(array)-1 or array[mid+1]!=value:
                return mid
            else:
                l=mid+1
    
    return -1
```

### 查找第一个大于等于给定值的元素 (>=value)

```py
def BS_3(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)>>1
        if array[mid]>=value:
            if mid==0 or array[mid-1]<value:
                return mid
            else:
                r=mid-1
        else:
            l=mid+1
    return -1
```

### 查找最后一个小于或等于给定值得元素 (<=value)

```py
def BS_4(array, value):
    l,r=0,len(array)-1
    while l<=r:
        mid=l+(r-l)>>1
        if array[mid]<=value:
            if mid==len(array)-1 or array[mid+1]>value:
                return mid
            else:
                l=mid+1
        else:
            r=mid-1
    return -1

```

## 后记
数据量太大不太适合二分查找，因为二分法依赖数组，而数组是内存连续空间