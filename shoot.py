import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


a = 10
while a > 0:
    a -= 1
    print(a)
    if a == 0:
        print("미사일발사")
