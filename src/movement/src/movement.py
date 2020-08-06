#! /usr/bin/env python3
# 
# This was modified by Jacob Dickson, Ba Bui
# Test change 2020
#
import pyrealsense2 as rs
import numpy as np
import cv2
import time

from array import *
from collections import deque 

import rospy
import jetson.inference
import jetson.utils
from localizer_dwm1001.msg      import Tag
from std_msgs.msg import Bool
from std_msgs.msg import Float64
from std_msgs.msg import String
from geometry_msgs.msg import Vector3
from math import pow, atan2, sqrt, acos, pi, sin, cos, floor

import argparse
import sys
#setting up map grid
ROW = 11
COL = 11
path = deque()
visit = [[None for i in range(COL)] for j in range(ROW)]
#path_map = [[0 for i in range(COL)] for j in range(ROW)]
map1 = [[1 for i in range(COL)] for j in range(ROW)]


tag = Tag()
# Configure depth and color streams
pipeline = rs.pipeline()
# Start streaming

pipeline.start()


heading = 0.00
def TagCallback(data):
	tag.x = data.x
	tag.y = data.y
	tag.z = data.z

def turn_angle_callback(data):
	heading = data

rospy.init_node("movement", anonymous=False)
rospy.Subscriber("/dwm1001/tag1",     Tag,    TagCallback)
rospy.Subscriber("/turn_angle",     Float64,    turn_angle_callback)


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
	print("test1") 
      
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
				print("test")
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

pub = rospy.Publisher('desired_position', Vector3, queue_size=10)
dest = Point(5, 5) 
source = Point(int(floor(tag.x)), int(floor(tag.y)))
des_pos = Vector3(dest.x,dest.y,0)
start = True
BFS(map1,source,dest)
path.pop()
while path:
	temp_point = path.pop().pt
	des_pos.x = temp_point.x
	des_pos.y = temp_point.y
	des_pos.z = 0		

	#rospy.loginfo(des_pos)
	print("Next des_pos:")
	print(des_pos)
	pub.publish(des_pos)


	#while wait, check obstacle
	#print(isValid(1,1))
	# Wait for a coherent pair of frames: depth and color
	frames = pipeline.wait_for_frames()
	depth_frame = frames.get_depth_frame()
	if not depth_frame:
		continue

	

	

	for y in range(230, 235):
		for x in range(310,320):
			#print("At x =", tag.x, ", y =", tag.y, ", z =", tag.z)
			dist = depth_frame.get_distance(x, y)
			#print(dist)
			if (dist < 2.0) and (dist >= 1.0):
				#Start path finding and send to gotopos with headings and change map grid
				#to include found objects
				BFS(map1,temp_point,dest)
				map1[int(floor(cos(heading)*dist+tag.x))][int(floor(sin(heading)*dist+tag.y))] = 0
				print(dist)
	print(tag.x)
	print(tag.y)
	while floor(tag.x) != des_pos.x or floor(tag.y) != des_pos.y:
		pass



				
	#pub.publish(line)

