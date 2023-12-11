a=[1,2,4,3,6,5]

n=len(a)

for(i=0;i<n;i++){
    max_v=a[i]
    i_v=i
    
    for(j=i;j<n;j++){
        if(a[j]>max_v){
            max_v=a[j]
            i_v=j
        }
    }
    
    t=a[i]
    a[i]=a[i_v]
    a[i_v]=t
}
    
print(a)
        