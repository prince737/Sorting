def merge(l,r,a):
	leftcount = len(l)
	rightcount = len(r)
	i = 0; j = 0; k = 0;
	while(i<leftcount and j<rightcount):
		if l[i] > r[j]:
			a[k] = l[i]
			i = i+1
		else:
			a[k] = r[j]
			j = j+1
		k = k+1

	while i < leftcount: 
		a[k] = l[i]
		k = k+1
		i = i+1
	while j < rightcount: 
		a[k] = r[j]
		k = k+1
		j = j+1


def mergeSort(arr):
	if len(arr)<2:
		return
	n = len(arr)
	mid = int(n/2)
	left = []
	right = []
	left = [arr[i] for i in range(0,mid)]
	right = [arr[i] for i in range(mid,n)]
	mergeSort(left)
	mergeSort(right)
	merge(left,right,arr)


arr = [2,4,1,6,8,5,3,7]
mergeSort(arr)
print(arr)