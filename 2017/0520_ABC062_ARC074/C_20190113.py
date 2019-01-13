H,W = map(int,input().split())

ans = 9999999999
# 高さの分割で全探索
for h in range(1,H):
    s1 = h*W
    # 残った領域をさらに高さで分割
    s2 = ((H-h)//2)*W 
    s3 = (H-h-(H-h)//2)*W
    ans = min(ans, max(s1,s2,s3)-min(s1,s2,s3))
    # 残った領域を幅で分割
    s2 = (W//2)*(H-h)
    s3 = (W-W//2)*(H-h)
    ans = min(ans, max(s1,s2,s3)-min(s1,s2,s3))


# 高さと幅を入れ替えて再実行
H,W = W,H
for h in range(1,H):
    s1 = h*W
    # 残った領域をさらに高さで分割
    s2 = ((H-h)//2)*W 
    s3 = (H-h-(H-h)//2)*W
    ans = min(ans, max(s1,s2,s3)-min(s1,s2,s3))
    # 残った領域を幅で分割
    s2 = (W//2)*(H-h)
    s3 = (W-W//2)*(H-h)
    ans = min(ans, max(s1,s2,s3)-min(s1,s2,s3))

print(ans)