class Solution {
public:
    int reverse(int x) {
        int orr = x;
        long long num=0;
        long long y=x;
        if(x==0) return 0;
        else{
            if(x<0) y*=-1;
            while (y>0){
                num = num * 10 + (y%10);
                y/=10;
            }
            if(orr<0) num*=-1;
        }
        if(num>INT_MAX || num<INT_MIN) return 0;
        return int(num);
    }
};