flag = 'ICTF{??????????????????????????}'

def encrypt(e):
    l = (e >> 32) & 0xffffffff
    r = e & 0xffffffff
    for i in xrange(128):
        t = l
        l = r
        r = t ^ r ^ (r | 368)
    return l << 32 | r

if __name__ == '__main__':
    for i in xrange(0,32,8):
        print encrypt(int(flag[i:i+8].encode('hex'),16))
