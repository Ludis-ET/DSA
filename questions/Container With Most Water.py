height = [1,8,6,2,5,4,8,3,7]
w,h,r,l = 0,0,1,1
counter = 0
for a in height:
    if counter == 0:
        counter += 1
        h = a
        continue
    counter += 1 # 3 4
    area = w * h # 1 6
    temp_h = h if h < a else a # 1 2
    temp_w = counter - l # - 2
    temp_area = temp_h * temp_w # - 4
    if temp_area > area:
        w, h, r = temp_w, temp_h, counter
    if a > h:
        l = counter
        h = a

area = w * h
    


print(area,w,h,l,r)