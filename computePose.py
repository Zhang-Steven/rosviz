import cv2
# speed: 2pix/leap
fw = open('/home/fusion/Documents/isualizer/coodinates.txt', 'r')
f = open('/home/fusion/Documents/isualizer/pose.txt', 'a')

while True:
    line = fw.readline()
    data = line.strip('\n')
    line_num = fw.tell()
    data_next = next(fw).strip('\n')
    fw.seek(line_num)
    if not data_next:
        break
    xk, yk = data.split(' ', -1)
    xkk, ykk = data_next.split(' ', -1)
    int_xk = int(xk)
    int_yk = int(yk)
    int_xkk = int(xkk)
    int_ykk = int(ykk)

    dist = pow((pow((int_xk-int_xkk), 2)+pow((int_yk-int_ykk), 2)), 0.5)
    leaps = int(dist/2)
    indentx = (int_xkk-int_xk)/leaps
    indenty = (int_ykk-int_yk)/leaps
    for i in range(0, leaps):
        xtemp = int(int_xk + indentx*i)
        ytemp = int(int_yk + indenty*i)
        f.write(str(xtemp)+' '+str(ytemp))
        f.write('\n')


fw.close()
f.close()
