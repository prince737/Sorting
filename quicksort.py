def partition(arr, start, end):
	pivot = arr[end]
	pindex = start
	for i in range(start,end):
		if arr[i] >= pivot:
			arr[i], arr[pindex] = arr[pindex], arr[i]
			pindex += 1
	arr[end], arr[pindex] = arr[pindex], arr[end]
	return pindex

def quickSort(arr, start, end):
	if(start < end):
		pindex = partition(arr, start, end)
		quickSort(arr, start, (pindex-1))
		quickSort(arr, (pindex+1), end)

arr = [2,1,3,4,8,5,7,6]
quickSort(arr,0,(len(arr)-1))
print(arr)