input_seq=[]
last_updated={}
left_seq=[]
right_seq=[]
counter=0

# input_seq=['a=b+c','b=b+c','c=b+c']
# last_updated={'a':-1,'b':-1,'c':-1}

input_seq=['a=b+c','b=a-d','c=b+c','d=a-d']
last_updated={'a':-1,'b':-1,'c':-1,'d':-1}

def search(string,l):
    ans=-1
    for index, value in enumerate(l):
        if value == string:
            ans=index
    return ans

for eq in input_seq:
    seperate=eq.split('=')
    left,right=seperate[0],seperate[1]
    if counter==0:
        print(eq)
        left_seq.append(left)
        right_seq.append(right)
        last_updated[left]=counter
    else:
        pos=search(right,right_seq)
        if pos!=-1:
            l_ch=left_seq[pos]
            m1,m2=right[0],right[2]
            if (m1 not in left_seq[pos+1:counter]) and (m1 not in left_seq[pos+1:counter]):
                # print('pos',pos,'countetr',counter,left_seq[pos+1:counter],right_seq,right)
                print(left+'='+l_ch)
                last_updated[left]=counter
                left_seq.append(left)
                right_seq.append(l_ch)
            else:
                print(eq)
                left_seq.append(left)
                right_seq.append(right)
                last_updated[left]=counter
        else:
            print(eq)
            left_seq.append(left)
            right_seq.append(right)
            last_updated[left]=counter
    counter=counter+1
    # print(left_seq)