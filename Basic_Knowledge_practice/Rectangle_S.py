class Rectangle:

# 学习了如何定义以及访问class类型
    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    def getArea(self):
        return self.width * self.height