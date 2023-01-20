def mostFrequentWord(arr,n):

freq = 0 

# res to store the most occurring string in the array of strings 

res = ‘ ‘ 

# running nested for loops to find the most occurring word in the array of strings 

for i in range (0,n,1):
count = 0
for j in range (i+1.n,1):
If arr[j] == arr[i] :
count += 1

#updating our max freq of occurred string in the 
#array of strings 
If count >=freq :
res = arr [i]
freq = count 
print (“the word that occurs most is : “ + str(res))
print (“No of times : “+ str  (freq))

n = len(arr)
mostFrequentWord(arr,n)


