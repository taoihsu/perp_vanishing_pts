zero_slope = []
inf_slope=[]
other_line=[]

for i in range(line.shape[0]):
	if (line[i][0][3]-line[i][0][1] == 0):
		#print line[i][0] , 'zero_slope'
		zero_slope.append(line[i])
		cv2.line(img,(int(line[i][0][0]),int(line[i][0][1])),(int(line[i][0][2]),int(line[i][0][3])),(255,0,0),2)

for i in range(line.shape[0]):
	if (line[i][0][2]-line[i][0][0] == 0):
		#print line[i][0] , 'inf_slope'
		inf_slope.append(line[i])
		cv2.line(img,(int(line[i][0][0]),int(line[i][0][1])),(int(line[i][0][2]),int(line[i][0][3])),(0,0,255),2)

for i in range(line.shape[0]):
	if not((line[i][0][2]-line[i][0][0] == 0)or(line[i][0][3]-line[i][0][1] == 0)):
		other_line.append(line[i])
		#print line[i][0], mi

cv2.imwrite('houghlines_'+image_dir[-6:],img)


# the list would be appended in the following format:
# line1, line2, x_intersection, y_intersection, (1==outside the line segment, 2== inside the line segment)

intersection = []
intersection_valid = []
intersection_invalid = []

for i in range(len(other_line)):
	mi = (other_line[i][0][3]-other_line[i][0][1])/(other_line[i][0][2]-other_line[i][0][0])
	for j in range(i+1,len(other_line)):
		##
		#checking if any of the slopes are infinity
		##
		mj = (other_line[j][0][3]-other_line[j][0][1])/(other_line[j][0][2]-other_line[j][0][0])	
		if (mi==mj):
			intersection.append([i,j,float("inf"),float("inf"),1])
			intersection_valid.append([i,j,float("inf"),float("inf"),1])
		else:
			p_x = (other_line[j][0][1]-other_line[i][0][1] + mi*other_line[i][0][0] - mj*other_line[j][0][0])/(mi-mj)
			p_y = other_line[j][0][1]+ mj*(p_x-other_line[j][0][0])
			if (in_lineseg(other_line[i][0],p_x,p_y) or (in_lineseg(other_line[j][0],p_x,p_y))):
				intersection.append([i,j,p_x,p_y,0])
				intersection_invalid.append([i,j,p_x,p_y,0])
			else: 
				intersection.append([i,j,p_x,p_y,1])
				intersection_valid.append([i,j,p_x,p_y,1])


image_dir = 'groundtruth/Images/0000000041.jpg'
img1 = cv2.imread(image_dir)
for i in range(len(intersection_valid)):
	if (intersection_valid[i][2]!=float("inf")):
		cv2.circle(img1,(int(intersection_valid[i][2]),int(intersection_valid[i][3])),10,(100,50,50),-1)
		ll1 = intersection_valid[i][0]
		ll2 = intersection_valid[i][1]
		cv2.line(img1,(int(other_line[ll1][0][0]),int(other_line[ll1][0][1])),(int(other_line[ll1][0][2]),int(other_line[ll1][0][3])),(0,255,0),2)
		cv2.line(img1,(int(other_line[ll2][0][0]),int(other_line[ll2][0][1])),(int(other_line[ll2][0][2]),int(other_line[ll2][0][3])),(0,0,255),2)
		cv2.imwrite('intersection_val_'+str(i)+'_'+image_dir[-6:],img1)
		img1 = cv2.imread(image_dir)


con = other_line[3][0]
pro = other_line[5][0]
img1 = cv2.imread(image_dir)
ll1 = 3
cv2.line(img1,(int(other_line[ll1][0][0]),int(other_line[ll1][0][1])),(int(other_line[ll1][0][2]),int(other_line[ll1][0][3])),(0,255,100),2)
ll1 = 5
cv2.line(img1,(int(other_line[ll1][0][0]),int(other_line[ll1][0][1])),(int(other_line[ll1][0][2]),int(other_line[ll1][0][3])),(0,100,255),2)

#lets complete the lines
i = 3
m_con = (other_line[i][0][3]-other_line[i][0][1])/(other_line[i][0][2]-other_line[i][0][0])
i = 5
m_pro = (other_line[i][0][3]-other_line[i][0][1])/(other_line[i][0][2]-other_line[i][0][0])
for g in range(500):
	y_con = other_line[3][0][1]+m_con(g-other_line[3][0][1])
	y_pro = other_line[5][0][1]+m_con(g-other_line[5][0][1])
	cv2.circle(img1,(int(intersection_valid[i][2]),int(intersection_valid[i][2])),3,(100,50,50),-1)


img = img_hough
