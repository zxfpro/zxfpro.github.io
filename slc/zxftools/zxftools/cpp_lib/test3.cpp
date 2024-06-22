#include <iostream>
extern "C" {
// 函数代码
int adds(int n){
    int k =0;
    int i = 0;
    for (n;n>0;n--) {
        k+=i;
        i+=1;
    }
    return k;
}

int add(int n,int m){
    return n + m;
}
// 函数结束
}
// !g++ -o test4.so -shared -fPIC test3.cpp
