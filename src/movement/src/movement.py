#! /usr/bin/env python3
# 
# This was modified by Jacob Dickson, Ba Bui
# 
#
import pyrealsense2 as rs
import numpy as np
import cv2

from array import *
from collections import deque 

import rospy
import jetson.inference
import jetson.utils
from localizer_dwm1001.msg      import Tag
from std_msgs.msg import Bool
from std_msgs.msg import Bool

import argparse
import sys
#setting up map grid
ROW = 11
COL = 11
path = deque()
visit = [[None for i in range(COL)] for j in range(ROW)]
path_map = [[0 for i in range(COL)] for j in range(ROW)]
map1 = [[1 for i in range(COL)] for j in range(ROW)]

tag = Tag()
# Configure depth and color streams
pipeline = rs.pipeline()
# Start streaming
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)


def TagCallback(data):
	tag.x = data.x
	tag.y = data.y
	tag.z = data.z
rospy.init_node("movement", anonymous=False)
rospy.Subscriber("/dwm1001/tag1",     Tag,    TagCallback)


#Class
# To store matrix cell cordinates 
class Point: 
	def __init__(self,x: int, y: int):
		self.x = x 
		self.y = y 
# A data structure for queue used in BFS 
class queueNode: 
	def __init__(self,pt: Point, dist: int): 
		self.pt = pt  # The cordinates of the cell 
		self.dist = dist  # Cell's distance from the source 
  
# Check whether given cell(row,col) 
# is a valid cell or not 
def isValid(row: int, col: int): 
	return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL) 
  
# These arrays are used to get row and column  
# numbers of 4 neighbours of a given cell  
rowNum = [-1, 0, 0, 1] 
colNum = [0, -1, 1, 0] 
  
# Function to find the shortest path between  
# a given source cell to a destination cell.  
def BFS(mat, src: Point, dest: Point): 
      
	# check source and destination cell  
	# of the matrix have value 1  
	if mat[src.x][src.y]!=1 or mat[dest.x][dest.y]!=1: 
		return -1
      
	visited = [[False for i in range(COL)] for j in range(ROW)]

	# Mark the source cell as visited  
	visited[src.x][src.y] = True

	# Create a queue for BFS  
	q = deque() 
	# Distance of source cell is 0 
	s = queueNode(src,0) 
	q.append(s) #  Enqueue source cell 
	path.append(s)
	# Do a BFS starting from source cell  
	while q: 

		curr = q.popleft() # Dequeue the front cell 
		#path.append(curr)
		# If we have reached the destination cell,  
		# we are done  
		pt = curr.pt 
		if pt.x == dest.x and pt.y == dest.y:

			minimum = curr
			#path.append(curr)
			print(curr.pt.y)
			while path:
				temp = path.popleft()
				visit[temp.pt.x][temp.pt.y] = temp



			while pt.x != src.x or pt.y != src.y:

				for i in range(4): 
					row = pt.x + rowNum[i] 
					col = pt.y + colNum[i] 

				    # if adjacent cell is valid, has path   
				    # and not visited yet, enqueue it. 
					if (isValid(row,col) and mat[row][col] == 1 and visit[row][col] != None):
						if (visit[row][col].dist < minimum.dist):
							minimum = visit[row][col]
                
				path.append(minimum)
				pt = minimum.pt
                        
			return curr.dist 
          
	# Otherwise enqueue its adjacent cells  
	for i in range(4): 
		row = pt.x + rowNum[i] 
		col = pt.y + colNum[i] 
              
		# if adjacent cell is valid, has path   
		# and not visited yet, enqueue it. 
		if (isValid(row,col) and mat[row][col] == 1 and not visited[row][col]): 
			visited[row][col] = True
			Adjcell = queueNode(Point(row,col),curr.dist+1)
			path.append(Adjcell)
			q.append(Adjcell) 
      
	# Return -1 if destination cannot be reached  
	return -1
#End class


searching = False
while True:
	if searching:
		print(isValid(1,1))
		# Wait for a coherent pair of frames: depth and color
		frames = pipeline.wait_for_frames()
		depth_frame = frames.get_depth_frame()
		color_frame = frames.get_color_frame()
		if not depth_frame or not color_frame:
			continue

		# Convert images to numpy arrays
		depth_image = np.asanyarray(depth_frame.get_data())
		color_image = np.asanyarray(color_frame.get_data())

		# Apply colormap on depth image (image must be converted to 8-bit per pixel first)
		depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

		# Stack both images horizontally
		images = np.hstack((color_image, depth_colormap))

		# Show images
		cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
		cv2.imshow('RealSense', images)
		cv2.waitKey(1)

		for y in range(230, 235):
			for x in range(310,320):
				#print("At x =", tag.x, ", y =", tag.y, ", z =", tag.z)
				dist = depth_frame.get_distance(x, y)
				if dist < 2 && dist >= 1:
					#Start path finding and send to gotopos with headings and change map grid
					#to include found objects
					searching = False
					print(dist)
	else:
		#run the path finding algorithm
		#then set searching to true then call gotopos
		BFS(mat,source,dest) 
#pub.publish(line)

