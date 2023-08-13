#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    int sw[n];
    int se[n];

    for (int i=0; i < n; i++){
        int val;
        scanf("%d", &val);
        sw[i] = val;
    }
    for (int i=0; i < n; i++){
        int val;
        scanf("%d", &val);
        se[i] = val;
    }

    int k = 0, sum1 = 0, sum2 = 0;
    for (int i=0; i < n; i++){
        sum1 += sw[i];
        sum2 += se[i];
        if (sum1 == sum2){
            k = i+1;
        }
    }
    printf("%d", k);
    return 0;
}