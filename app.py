class Pattern:
    def __init__(self):
        self.n = 4
    
    def print_star_patter(self):
        for i in range(1, self.n+1):
            print('*' * i)
        
        
        for i in range(self.n-1, 0, -1):
            print((self.n-i) * ' ' +  '*' * i)


if __name__ == '__main__':
    obj = Pattern()
    obj.print_star_patter()