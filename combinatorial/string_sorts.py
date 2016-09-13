#Sorting the million strings

print sorted(["a","b","ab","aaaaaab"])

#MSD sort

if (hi <= lo + M)
{ Insertion.sort(a, lo, hi, d); return;
}
int[] count = new int[R+2];
for (int i = lo; i <= hi; i++)
count[charAt(a[i], d) + 2]++; // Compute frequency counts.
for (int r = 0; r < R+1; r++)
count[r+1] += count[r]; // Transform counts to indices.
for (int i = lo; i <= hi; i++)
// Distribute.
aux[count[charAt(a[i], d) + 1]++] = a[i];
for (int i = lo; i <= hi; i++)
a[i] = aux[i - lo];
// Copy back.
// Recursively sort for each character value.
for (int r = 0; r < R; r++)
sort(a, lo + count[r], lo + count[r+1] - 1, d+1);

def sort(string,lo,hi):
    count=[0]*258
    aux=[0]*len(string)
    for i in string:
        count[ord(i)]=count[ord(i)]+1

    for index,r in enumerate(count[1:]):
        count[index+1]=count[index+1]+count[index]

    for k in range(lo,hi):
        aux[count[ord(string[k])+1]]=
