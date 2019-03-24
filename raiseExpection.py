""""
********************
*                  *
*                  *
*                  *
*                  *
********************
"""

def boxPrint(symbol, width, height):
    if len(symbol)!=1:
        raise Exception('Symbol needs to be a strig with len igual to 1')
    if (width <2) or (height<2):
        raise Exception('width and  height need to be at least 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2))+ symbol)
    print(symbol*width)

boxPrint('*',15,5)
boxPrint('00',15,5)
boxPrint('*',1,5)
#raise Exception('This is the error message')