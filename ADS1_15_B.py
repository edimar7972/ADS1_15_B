def ordene(w,v):
	i=1
	l=[]
	while i < len(v):
		a=v[i-1]/w[i-1]
		l.append(a)
		i+=1
	return l

def mochila_fracionaria(w,v,n,W):
	ordene(w,v)
	x=[]
	soma=0
	for i in range(n):
		if w[i] <= W:
			soma=soma + v[i]
			W=W-w[i]
		else:
			r=(W/w[i])*v[i]
			soma = soma + r
			W=0
	return soma

n,W=input().split(" ")
n=int(n)
W=int(W)
l=[]
u=[]
for i in range(n):
	v,w=input().split(" ")
	v=int(v)
	w=int(w)
	l.append(v)
	u.append(w)
print(mochila_fracionaria(u,l,n,W))
