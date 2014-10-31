# Functions incorporating merge operations to do various tasks

def intersect(arr1,arr2):
	
	i,j = 0,0
	intersect = []
	while i<len(arr1) and j<len(arr2):
		if arr1[i] == arr2[j]:
			intersect.append(arr1[i])
			i += 1
			j += 1
		elif arr1[i] < arr2[j]:
			i += 1
		else:
			j += 1
	return intersect


def merge2arrays(arr1,arr2):
	
	i,j = 0,0
	result = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			result.append(arr1[i])
			i += 1
		else:
			result.append(arr2[j])
			j += 1
	if i < len(arr1)-1:
		result.extend(arr1[i::])
	if j < len(arr2)-1:
		result.extend(arr2[j::])
	return result

def merge(arr,st,mid,end):
	i,j = st,mid
	result = []
	while i<mid and j<end+1:
		if arr[i] <= arr[j]:
			result.append(arr[i])
			i += 1
		else:
			result.append(arr[j])
			j += 1
	if i<mid:
		result.extend(arr[i:mid])
	if j<end+1:
		result.extend(arr[j:end+1])
	arr[st:end+1] = result


def split(arr,i,j):
	if j<=i:
		return
	if i == j-1:
		if arr[i]>arr[j]:
			(arr[i],arr[j]) = (arr[j],arr[i])
		return
	mid = (j+i)/2
	split(arr,i,mid)
	split(arr,mid+1,j)
	merge(arr,i,mid+1,j)
	return

arr = [2,7,1,8,5,7,2,3]
split(arr,0,len(arr)-1)
print arr
