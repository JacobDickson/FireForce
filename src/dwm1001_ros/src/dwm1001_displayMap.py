#!/usr/bin/env python

import rospy
import copy
from interactive_markers.interactive_marker_server  import InteractiveMarkerServer
from interactive_markers.menu_handler               import *
from visualization_msgs.msg                         import (InteractiveMarkerControl, Marker, InteractiveMarker )
from geometry_msgs.msg                              import Point
from localizer_dwm1001.msg                          import Anchor
from localizer_dwm1001.msg                          import Tag
from std_msgs.msg 				    import Bool


server       = None
rospy.init_node("display_map")
server = InteractiveMarkerServer("DWM1001_Anchors_And_Tag_Server")
theBoo = False

class DisplayInRviz:


    def processFeedback(self, feedback):
        """ 
        Process feedback of markers

        :param: feedback of markers

        :returns: none

        """
        p = feedback.pose.position
        rospy.loginfo(feedback.marker_name + " is pluginsnow at " + str(p.x) + ", " + str(p.y) + ", " + str(p.z))


    def makeBoxControlTag(self,msg):
        """
        Create a box controll for tag

        :param: msg from marker

        :returns: control

        """

        control =  InteractiveMarkerControl()
        control.always_visible = True
        control.markers.append( self.makeWhiteSphereTag(msg) )
        msg.controls.append( control )
        return control

    def makeBoxControlAnchor(self, msg):
        """
        Create a box control for anchor

        :param: msg from marker

        :returns: control

        """
        control =  InteractiveMarkerControl()
        control.always_visible = True
        control.markers.append( self.makeGreyCubeAnchor(msg) )
        msg.controls.append( control )
        return control

    def makeWhiteSphereTag(self, msg ):
        """
        Create a white sphere for tag

        :param: msg from marker

        :returns: marker

        """

        marker = Marker()
        marker.type = Marker.SPHERE
        marker.scale.x = msg.scale * 0.45
        marker.scale.y = msg.scale * 0.45
        marker.scale.z = msg.scale * 0.45
	if theBoo == True:
		marker.color.r = 1
		marker.color.g = 0
		marker.color.b = 0
		marker.color.a = 1.0
		#theBoo = True
	else:
		marker.color.r = 1
		marker.color.g = 1
		marker.color.b = 1
		marker.color.a = 1.0
		#theBoo = False
	#if data.data == true:
	#elif data.data == false:
        return marker


    def makeGreyCubeAnchor(self, msg):
        """
        Create a grey cube for anchor

        :param: msg from marker

        :returns: marker

        """

        marker = Marker()

        marker.type = Marker.CUBE
        marker.scale.x = msg.scale * 0.45
        marker.scale.y = msg.scale * 0.45
        marker.scale.z = msg.scale * 0.45
        marker.color.r = 0.5
        marker.color.g = 0.5
        marker.color.b = 0.5
        marker.color.a = 1.0
        return marker



    def makeTagMarker(self, position, name):
        """
        Make coordinates and control for tag

        :param: position of tag
        :param: name for tag

        :returns:

        """

        int_marker = InteractiveMarker()
        int_marker.header.frame_id = "map"
        int_marker.pose.position = position
        int_marker.scale = 1

        int_marker.name = name
        int_marker.description = name

        self.makeBoxControlTag(int_marker)

        control = InteractiveMarkerControl()
        control.orientation.w = 1
        control.orientation.x = 0
        control.orientation.y = 1
        control.orientation.z = 0
        control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
        int_marker.controls.append(copy.deepcopy(control))
        control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
        int_marker.controls.append(control)

        server.insert(int_marker, self.processFeedback)



    def makeAnchorMarker(self, position, name):
        """
        Make coordinates and control for anchor

        :param: position of anchor
        :param: name for anchor

        :returns:

        """

        int_marker = InteractiveMarker()
        int_marker.header.frame_id = "map"
        int_marker.pose.position = position
        int_marker.scale = 1
        int_marker.description = name
        int_marker.name = name

        self.makeBoxControlAnchor(int_marker)

        control = InteractiveMarkerControl()
        control.orientation.w = 1
        control.orientation.x = 0
        control.orientation.y = 1
        control.orientation.z = 0
        control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
        int_marker.controls.append(copy.deepcopy(control))
        control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
        int_marker.controls.append(control)

        server.insert(int_marker, self.processFeedback)



    def Anchor0callback(self,data):
        """
        Callback from topic /dwm1001/anchor0

        :param: data of anchor 0

        :returns:

        """
        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 0")
            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor0 x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))
        except ValueError:
           rospy.loginfo("Value error")



    def Anchor1callback(self,data):
        """
        Callback from topic /dwm1001/anchor1

        :param: data of anchor 1

        :returns:

        """

        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 1")

            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor1 x: "+ str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")



    def Anchor2callback(self,data):
        """
        Callback from topic /dwm1001/anchor2

        :param: data of anchor 2

        :returns:

        """

        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 2")
            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor2 x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")

    def Anchor3callback(self,data):
        """
        Callback from topic /dwm1001/anchor3

        :param: data of anchor 3

        :returns:

        """

        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeAnchorMarker(position, "Anchor 3")
            # TODO remove this after, Debugging purpose
            rospy.loginfo("Anchor3 x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")

    def TagCallback(self,data):
        """
        Callback from topic /dwm1001/tag

        :param: data of tag

        :returns:

        """
        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
            # Create a new marker with passed coordinates
            position = Point(data.x, data.y, data.z)
            # Add description to the marker
            self.makeTagMarker(position, "Tag")
            # Publish marker
            server.applyChanges()

            # TODO remove this after, Debugging purpose
            rospy.loginfo("Tag x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")



    def TagColors(self,data):
	global theBoo
	theBoo = data.data
	
	
	
    def makeAfterImage(self, data):
	if theBoo == True:
		
    
		# create an interactive marker for our server
		int_marker = InteractiveMarker()
		int_marker.header.frame_id = "map"
		int_marker.name = "my_marker"
		int_marker.description = "After image"
		
		position = Point(data.x, data.y, data.z)
		#self.markers_pub = rospy.Publisher("map2", Marker, queue_size=1)
		marker = Marker()
		marker.type = marker.SPHERE
		marker.action = marker.ADD
		marker.color.r = 1
		marker.color.g = 0
		marker.color.b = 0
		marker.color.a = 1
		marker.scale.x = 0.45
		marker.scale.y = 0.45
		marker.scale.z = 0.45
		marker.pose.position = position
		marker.pose.orientation.x = 0
		marker.pose.orientation.y = 0
		marker.pose.orientation.z = 0
		marker.pose.orientation.w = 1
		marker.header.stamp = rospy.get_rostime()
		marker.id = 1

		#self.markers_pub.publish(marker)
		#server.applyChanges()
		# create a non-interactive control which contains the box
		box_control = InteractiveMarkerControl()
		box_control.always_visible = True
		box_control.markers.append( marker )

		# add the control to the interactive marker
		int_marker.controls.append( box_control )


		# add the interactive marker to our collection &
		# tell the server to call processFeedback() when feedback arrives for it
		server.insert(int_marker, self.processFeedback)

		

    def makeHumanTag(self, msg):
        """
        Create afterimage for Tag human

        :param: msg from marker

        :returns: marker

        """

        marker = Marker()

        marker.type = Marker.CUBE
        marker.scale.x = msg.scale * 0.45
        marker.scale.y = msg.scale * 0.45
        marker.scale.z = msg.scale * 0.45
        marker.color.r = 0.5
        marker.color.g = 0
        marker.color.b = 0.5
        marker.color.a = 1.0
        return marker

	#if data.data == true:
	#elif data.data == false:
	
    def humanTagCallback(self,data):
        """
        Callback from topic /dwm1001/tag

        :param: data of tag

        :returns:
"""
        
        global server

        # Get the coordinates of the Tag in this format 0 0 0, then split this string using .split() function
        try:
	    
		if theBoo == True:
			# Create a new marker with passed coordinates
		    	position = Point(data.x, data.y, data.z)
		    	# Add description to the marker
		    	self.makeHumanTagMarker(position, "Tag")
		    	# Publish marker
		    	server.applyChanges()

		    # TODO remove this after, Debugging purpose
		    	rospy.loginfo("Tag x: " + str(data.x) + " y: " + str(data.y) + " z: " + str(data.z))

        except ValueError:
           rospy.loginfo("Value error")

    def makeHumanTagMarker(self, position, name):
        """
        Make coordinates and control for tag

        :param: position of tag
        :param: name for tag

        :returns:

        """

        int_marker = InteractiveMarker()
        int_marker.pose.position = position
        int_marker.scale = 1

        int_marker.name = name
        int_marker.description = name

        self.makeBoxControlHumanTag(int_marker)

        control = InteractiveMarkerControl()
        control.orientation.w = 1
        control.orientation.x = 0
        control.orientation.y = 1
        control.orientation.z = 0
        control.interaction_mode = InteractiveMarkerControl.MOVE_ROTATE
        int_marker.controls.append(copy.deepcopy(control))
        control.interaction_mode = InteractiveMarkerControl.MOVE_AXIS
        int_marker.controls.append(control)

        server.insert(int_marker, self.processFeedback)

    def makeBoxControlHumanTag(self,msg):
        """
        Create a box controll for tag

        :param: msg from marker

        :returns: control

        """

        control =  InteractiveMarkerControl()
        control.always_visible = True
        control.markers.append( self.makeHumanTag(msg) )
        msg.controls.append( control )
        return control

    def start(self):
	rospy.Subscriber("/human2", Bool, self.TagColors)
        rospy.Subscriber("/dwm1001/anchor0", Anchor, self.Anchor0callback)
        rospy.Subscriber("/dwm1001/anchor1", Anchor, self.Anchor1callback)
        rospy.Subscriber("/dwm1001/anchor2", Anchor, self.Anchor2callback)
        rospy.Subscriber("/dwm1001/anchor3", Anchor, self.Anchor3callback)
        rospy.Subscriber("/dwm1001/tag1"    , Tag   , self.TagCallback)
        rospy.Subscriber("/dwm1001/tag1"    , Tag   , self.makeAfterImage)
        rospy.spin()



def main():
    displayInRviz = DisplayInRviz()
    displayInRviz.start()

if __name__=="__main__":
    main()
