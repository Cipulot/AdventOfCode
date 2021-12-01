def solution(data):
    a = data[0]
    b = data[1]
    i=1
    j=1
    cnt_1=0
    cnt_2=0
    while(i!=a):
        i*=7
        i%=20201227
        cnt_1+=1

    while(j!=b):
        j*=7
        j%=20201227
        cnt_2+=1

    ans=1
    for i in range(0,cnt_2):
        ans*=a
        ans%=20201227
    return ans

if __name__ == '__main__':
    with open('25.txt') as _file:
        data = [int(line) for line in _file.read().splitlines()]

    print("Final solution: ", solution(data))
    
