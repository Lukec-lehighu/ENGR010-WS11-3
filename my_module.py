import matplotlib.pyplot as plt
import random

def gen_plot(func, funcname, x_range):
    y = [func(x) for x in x_range]
    plt.title(funcname)
    plt.plot(x_range, y, '.')
    plt.show()

    return True

class Chooser:
    def __init__(self, arr=[1, 2, 3, 4, 5, 6]):
        self.value = arr[0]
        self.arr = arr
    
    def select(self):
        self.value = random.choice(self.arr)
        return self.value

    def get_value(self):
        return self.value
    
def print_rect(width=3, height=-1):
    if width < 3:
        width = 3

    if height <= -1:
        height = width
    elif height < 3:
        height = 3

    for i, _ in enumerate(range(height)):
        if i==0 or i == height-1:
            print('*'*width)
        else:
            print('*' + ' '*(width-2) + '*')

    return True

def main():
    c = Chooser()
    print(c.select())
    print(c.select())

    gen_plot(lambda x: x**2, 'x^2', list(range(0, 10)))

    print_rect(5)

if __name__=='__main__':
    main()