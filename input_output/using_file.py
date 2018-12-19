poem = '''\
当工作完成时
编程是有趣的
如果想让你的工作有趣
    使用Python！
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt', 'r')

while(True):
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()
