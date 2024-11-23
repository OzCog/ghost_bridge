#! /usr/bin/env python
#
# main.py - Main entry point for the ROS-to-OpenCog converter
# Copyright (C) 2015  Hanson Robotics
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License v3 as
# published by the Free Software Foundation and including the exceptions
# at http://opencog.org/wiki/Licenses
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License
# along with this program; if not, write to:
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import rospy
from ghost_bridge import GhostBridge


if __name__ == "__main__":
    rospy.init_node('ghost_bridge', log_level=rospy.DEBUG)
    bridge = GhostBridge()

    try:
        rospy.spin()
    except rospy.ROSInterruptException as e:
        rospy.logerr(e)

    rospy.loginfo("Exit OpenCog bridge")