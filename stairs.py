import sys


def numOfSteps(num):
    fin=[]
    res=[]
    rem=0
    def calc(rem,num,res):
        steps = [1, 2, 3]
        if rem==num:
            nonlocal fin
            fin.append(res.copy())
            return True

        if rem>num:
            return False

        for i in steps:


            res.append(i)
            calc(rem+i,num,res)

            res.pop()


        return False

    calc(rem, num, res)
    return fin




if __name__ == '__main__':
    num_of_stairs= int(sys.argv[1])
    print(f'The Number of Stairs Johan Should Climb is {num_of_stairs}')
    fin=numOfSteps(num_of_stairs)
    print(f'''The Count of Possible ways Johan can run the Stairs is '{len(fin)}' ''')
    print('Below are the Possible Ways ')
    print(fin)