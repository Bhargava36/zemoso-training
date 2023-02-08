def dfs(v,d,stack):
    while(len(stack)!=0):
        #taking current element from the stack
        curr=stack.pop()
        #If the current element is not visited the if block will execute
        if(v[curr]==False):
            #setting curr element to true that means marking as visited
            v[curr]=True
            #adding or appending the current element to the orderofcourse
            orderofcourse.append(curr)
            #assigning the curr element adjacency list to the x variable
            x=d[curr]
        for j in x :
            #checking every adjacency list item is visited or not it not visited (False).
            if(v[j]==False):
                # if not visited it will append to the stack
                stack.append(j)
#list of vertices
l=['full','front','back','html','css','js','c','java','python']
#adjacency lists
p=[['front','back'],['html','css','js','full'],['c','java','python','full'],['front'],['html','front'],['html','css','front'],['c','back'],['c','back'],['java','back']]
d={}
v={}
stack=[]
orderofcourse=[]
for i in range(len(l)):
    #mapping all the adjacency lists to the vertices using dictionaries 
    d[l[i]]=p[i]
    #initially setting all the vertices to false (here false is unvisited true is visited)
    v[l[i]]=False
#adding stating element to the stack
stack.append(l[0])
dfs(v,d,stack)
while((len(orderofcourse)>0)):
      print(orderofcourse.pop())
