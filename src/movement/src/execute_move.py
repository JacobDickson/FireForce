#!/usr/bin/env python

# Author: Alex Marlow

# Editor: David Babin

import rospy
import numpy

####################################################
from localizer_dwm1001.msg import Tag
####################################################

from geometry_msgs.msg import Twist, Vector3, Pose
from std_msgs.msg import String
#!/usr/bin/env python

# Author: Alex Marlow

# Editor: David Babin

import rospy
import numpy

####################################################
from localizer_dwm1001.msg import Tag
####################################################

from geometry_msgs.msg import Twist, Vector3, Pose, Point
from std_msgs.msg import String, Float64
from math import pow, atan2, sqrt, acos, pi, sin, cos, floor


class ExecuteMove:

	def __init__(self):
		
		rospy.init_node('executing_movement', anonymous=False)
		
		self.velocity_publisher = rospy.Publisher('cmd_vel',Twist, queue_size=10) 
		self.turn_ang = rospy.Publisher('turn_angle',Float64, queue_size=10) 

		##################################################################
		#rospy.Subscriber('/hedge_pos', Vector3, self.update_pose)
		rospy.Subscriber('/dwm1001/tag1', Tag, self.update_pose)
		
		rospy.Subscriber('desired_position', Vector3, self.update_des_pos)
		rospy.Subscriber('delay', Point, self.update_delay_time)

		self.rate = rospy.Rate(10)

		##################################################################

		self.delta_pos = Vector3()
		self.pose = Tag()
		self.des_pos = Vector3()
		self.des_vec = Vector3()
		self.turn_angle = 0.000
		self.ang_vel = 2
		self.stop = True
		self.margin = .2
		self.last_pos = Vector3()
		self.rate = rospy.Rate(1)
		self.rate.sleep()

		
		self.rate.sleep()
		self.rate = rospy.Rate(10)

		self.last_pos.x = self.pose.x
		self.last_pos.y = self.pose.y

		# make it not go to 0,0 right off the bat
		self.des_pos.x = self.pose.x
		self.des_pos.y = self.pose.y
		print("initialized to: ")
		print(self.des_pos.x)
		print(self.des_pos.y)
		print("from")
		print(self.pose.x)
		print(self.pose.y)

		self.vel_msg = Twist()

		self.vel_msg.linear.x = 0
		self.vel_msg.angular.z = 0

		self.vel_msg.linear.y = 0
		self.vel_msg.linear.z = 0
		self.vel_msg.angular.x = 0
		self.vel_msg.angular.y = 0
	
		#should not move
		self.velocity_publisher.publish(self.vel_msg)


		# des_vec is vector from current to desired
		# delta_pos is change in position from last position
		#angular velocity vector should be in radians per second
	def move(self):
		#allow movement
		if(self.check_pos() == False):
			self.stop = False

		if self.stop == False:
			#start moving forward
			self.last_pos.x = self.pose.x
			self.last_pos.y = self.pose.y
			print("this ")
			self.vel_msg.linear.x = .11
			self.velocity_publisher.publish(self.vel_msg)

			#go straight while checking for 2 seconds
		turn_time = 2
		self.rate = rospy.Rate(10)
		while(turn_time > 0 and self.stop == False):
			#print("straight loopy")
			if(self.check_pos()):
				print("reached")
				self.stop = True
				self.vel_msg.linear.x = 0
				self.velocity_publisher.publish(self.vel_msg)
				break
			turn_time = turn_time -  .1
	    		self.rate.sleep()

		#self.rate.sleep()

		print("\n I am at: ")
		print(self.pose.x)
		print(", ")
		print(self.pose.y)
		print("\n my last position was: ")
		print(self.last_pos.x)
		print(", ")
		print(self.last_pos.y)

		#get two the two vectors
		if(self.stop == False):
			print("\nI am about to calculate")
			self.des_vec.x = self.des_pos.x - self.pose.x
			self.des_vec.y = self.des_pos.y - self.pose.y
			self.delta_pos.x = self.pose.x - self.last_pos.x
			self.delta_pos.y = self.pose.y - self.last_pos.y
			print("\ndes_vec.x: ")
			print(self.des_vec.x)
			print("\ndes_vec.y: ")
			print(self.des_vec.y)
			print("\ndelta_pos.x: ")
			print(self.delta_pos.x)
			print("\nself.delta_pos.y: ")
			print(self.delta_pos.y)

			if not ((self.delta_pos.x == 0 and self.delta_pos.y == 0) or (self.des_vec.x == 0 and self.des_vec.y == 0)):

				#angle between our current trajectory and x axis(x axis of marvel mind sensors)
				theta1 = acos(((self.delta_pos.x)/(sqrt(self.delta_pos.y**2 + self.delta_pos.x**2))))
				if(self.pose.y < self.last_pos.y):
					theta1 = (-1)*theta1

				#angle between our desired trajectory and the x axis
				theta2 = acos(((self.des_vec.x)/(sqrt(self.des_vec.y**2 + self.des_vec.x**2))))
				if(self.des_pos.y < self.pose.y):
					theta2 = (-1)*theta2

				#angle needed to be turned(positive for right turn)
				self.turn_angle = theta1 - theta2
				#make it so it does not go turn to the right place but in wrong direction
				if(self.turn_angle > pi):
					self.turn_angle -= 2*pi
				if(self.turn_angle < -pi):
					self.turn_angle += 2*pi

				print("\nI am going to turn:  ")
				print(self.turn_angle)


				#get turn direction
				if(self.turn_angle > 0):
					self.right = True
				else:
					self.right = False
					self.turn_angle = self.turn_angle*(-1)
	

				turn_time = self.turn_angle/self.ang_vel

				print("\n I am going to turn for:  ")
				print(turn_time)
				self.rate = rospy.Rate(10)
				
				self.vel_msg.linear.x = 0
				self.vel_msg.angular.z = 0
				self.velocity_publisher.publish(self.vel_msg)
				#raw_input("yeet")
				self.vel_msg.linear.x = .11
				self.velocity_publisher.publish(self.vel_msg)
				

				#set turn and velocity, maybe have some error for turn to not trigger, test with controller to see if signs are coorect
				if(self.right):
					self.vel_msg.angular.z = -2
					self.velocity_publisher.publish(self.vel_msg)
				else:
					self.vel_msg.angular.z = 2
					self.velocity_publisher.publish(self.vel_msg)
	    
				#need to manage positive or negetive turn direction, acos probably does not give me the direction
				#loop repeats every 10th of a second, checking if we are at the position, still need to introduce error to position check
				while(turn_time > .1 and self.stop == False):
					self.rate.sleep()
					if(self.check_pos()):
						print("reached")
						self.stop = True
						self.vel_msg.angular.z = 0
						self.vel_msg.linear.x = 0
						self.velocity_publisher.publish(self.vel_msg)
						break
					turn_time -= .1
					print("\n I am turning right now")
				self.rate = rospy.Rate(1/turn_time)
				self.rate.sleep()
				if(self.check_pos()):
					self.stop = True
					self.vel_msg.angular.z = 0
					self.vel_msg.linear.x = 0
	   				self.velocity_publisher.publish(self.vel_msg)

				self.vel_msg.angular.z = 0
				self.velocity_publisher.publish(self.vel_msg)
				#set back to going straingt right here or ramain still
				self.rate = rospy.Rate(1)
		self.turn_ang.publish(self.turn_angle)
		#rospy.spin()
		self.rate = rospy.Rate(1)
		#self.rate.sleep()
		
	
# possibly need to introduce turning error

	
	
	#maybe want to round the numbers depending on testing results
	def update_delay_time(self, data):
		#print("\ndatax is: ")
		#print(data.x)
		#print("\ndatay is: ")
		#print(data.y)
		print("\nTime Sent from ws: ")
		print(int(float(data.x)))
		print(".", int(data.y))
		print("\nTime received: ")
		print(rospy.Time.now().secs, rospy.Time.now().nsecs)

	#maybe want to round the numbers depending on testing results
	def update_pose(self, data):
		#print("\ndatax is: ")
		#print(data.x)
		#print("\ndatay is: ")
		#print(data.y)
		self.pose.x = data.x
		self.pose.y = data.y



	def update_des_pos(self, data):
		print("\ndes_posx is: ")
		print(data.x)
		print("\ndes_posy is: ")
		print(data.y)
		self.des_pos.x = data.x
		self.des_pos.y = data.y

	#checks if in the acceptable margin from the desired position
	def check_pos(self):
		if(self.des_pos.x > self.pose.x + self.margin):
	    		return False
		elif(self.des_pos.x < self.pose.x):#self.des_pos.x < self.pose.x - self.margin
	    		return False
		elif(self.des_pos.y < self.pose.y):#self.des_pos.y < self.pose.y - self.margin
	    		return False
		elif(self.des_pos.y > self.pose.y + self.margin):
	    		return False
		else:
			return True
			
if __name__ == '__main__':
	cl = ExecuteMove()
	while not rospy.is_shutdown():
		try:
			cl.move()
			rospy.sleep(1)
		except rospy.ROSInterruptException:
			pass
