
def binSearch(arr,left,right):
	if right==left:
		return left
	if right<left or (arr[right]-arr[left])==right-left:
		return -1
	mid = (left+right)/2
	if (arr[mid]-arr[left])<mid-left:
		return binSearch(arr,left,mid)
	if arr[mid] == arr[mid+1]:
		return mid
	return binSearch(arr,mid,right)

arr = [1,2,3,3,4,5]
print binSearch(arr,0,5)
