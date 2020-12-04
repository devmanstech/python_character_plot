from math import log, exp


# function to generate blank-initialized 2D list
def gen_grid(x, y):
    rows, cols = (x, y) 
    arr = [[' ' for i in range(cols)] for j in range(rows)] 
    # print(arr)
    return arr

def plot (ydata, xdata=None, logscale=False, pch='*', title='plot',
                xlabel='X', ylabel='Y', width=72, height=50):
    
    data = gen_grid(width, height)

    print(data)

    if not xdata:
        xdata = range(1, len(ydata)+1)
    yydata = []
    logf = log if logscale else lambda x: x
    expf = exp if logscale else lambda x: x
    for i in ydata:
        try:
            yydata.append(logf(i))
        except ValueError:
            yydata.append(float('-inf'))
    ydiff = float(abs(float(min(yydata)) - max(yydata))/(height * 2))
    y_arange = [(i - ydiff, i + ydiff) for i in
                sorted(arange(min(yydata), max(yydata) + ydiff, ydiff * 2), reverse=True)]
    xdiff = float(abs(float(min(xdata)) - max(xdata)))/(width * 2)
   
    x_arange = [(i-xdiff, i+xdiff) for i in
                sorted(arange(float(min(xdata)), max(xdata) + xdiff, xdiff * 2))]
    graph = ' ' + str(title)
    graph += '\n'
    graph += ' ' + '-' * len(title)
    graph += '\n\n'
    graph += ylabel
    graph += '\n'
    val = 6 - max([len('{0:.0f}'.format(y)) for _, y in y_arange])
    form = '{' + ':<7.{}f'.format(val) + '}+'
    graph += form.format (expf(max(yydata)))
    for yval, (y1, y2) in enumerate(y_arange):
        graph+='\n'
        if not (yval)%5 and yval != 0:
            graph += form.format (expf((y1+y2)/2))
        else:
            graph += ' ' * 7 + '|'
        pos = 0
        for x1, x2 in x_arange:
            for i in range(pos, len(yydata)):
                if (y1 < yydata[i] <= y2 and
                    x1 < xdata[i]  <= x2):
                    graph += pch
                    pos += 1
                    break
            else:
                graph += ' '
    graph += '\n'
    if logscale:
        graph += ' 1/inf ' + ''.join(
            ['+' if not x%10 else '-' for x in range(width+1)]) + '\n'
    else:
        graph += '     0 ' + ''.join(
            ['+' if not x%10 else '-' for x in range(width+1)]) + '\n'
        
    val = 7 - max([len('{0:.0f}'.format(y)) for _, y in x_arange])
    form = '{' + ':<7.{}f'.format(val) + '}  '
    graph += ' '*7 + ''.join(
        [form.format(float(sum(x_arange[x])/2)) for x in range(0,width,10)]
    ) + ('' if width % 10 else form.format(float(sum(x_arange[-1])/2)))+ '\n\n'
    graph += ' ' * 7 + '{0:^{1}}'.format(xlabel, width)
    return graph


def arange(beg, end, step):
    return [beg + i * step for i in range(int(abs(beg-end)/step+.5))]

# function to save plot in plot.txt file.
def print_g_f(plot):
    f = open("plot.txt", "w")
    f.write(plot)
    f.close()



# function to print on the screen
def print_grid(plot):
    print(plot)


# Main part

gen_grid(10,20)

# print on the screen
print_grid(plot([0,5,9,18,7], width=60, height=10))

# save in the file
print_g_f(plot([0,5,9,18,7], width=60, height=10))


