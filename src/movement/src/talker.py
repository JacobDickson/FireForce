#!/usr/bin/env python
# Alex Marlow 2019
#main node for publishing desired position to ROS

#publishes topic "desired_position" as Vector3 data type

#program behavior and use: program will ask for x and y inputs, 's' sets the z value to stop the robot.
#entering 's' on the X input will send a stop signal, but Y will stil be asked for, mayble ill fix this later.
#program should deal with incorrect inputs properly, valid inputs are: 's', interger.


#imports
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3

#repeating function
def GoToPos():
    des_pos = Vector3()
    #variables are set to 'v' so if set otherwise the loops will exit
    x = 'v'
    y = 'v'
    #initialize publisher
    pub = rospy.Publisher('desired_position', Vector3, queue_size=10)
    rospy.init_node('GoToPos', anonymous=True)
    rate = rospy.Rate(10) # 10hz  slows this down
	#input loops
    while not rospy.is_shutdown():
	x = 'v'
        y = 'v'
	#check if valid input was entered
	while x == 'v':
	    print("Enter desired X position, or enter 's' to stop")
	    x = raw_input()
	    #try to cast to int
	    try:
	    	x = int(x)
	    #except if not integer
	    except:
		#s for pass, and v if input was invalid
	    	if x == 's':
	            pass
	    	else:
		    x = 'v'
	#check if valid input was entered
	while y == 'v':
	    print("Enter desired Y position, or enter 's' to stop")
	    y = raw_input()
	    #try to cast to int
	    try:
	    	y = int(y)
	    #except if not integer
	    except:
		#s for pass, and v if input was invalid
	        if y == 's':
	            pass
	        else:
		    y = 'v'
	#check for stop command
	if x == 's' or y =='s':
		#use extra z variable for extra commands
		des_pos.z = 1
	else:
		des_pos.z = 0
		des_pos.x = int(x)
		des_pos.y = int(y)
	#send position and print it
        rospy.loginfo(des_pos)
        pub.publish(des_pos)
        rate.sleep()


if __name__ == '__main__':
    try:
        GoToPos()
    except rospy.ROSInterruptException:
        pass


