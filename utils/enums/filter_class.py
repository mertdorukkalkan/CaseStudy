from enum import Enum


class ClassType(Enum):
    notificationgroup = "notificationgroup",
    notificationtype = "notificationtype",
    modulecompliance = "modulecompliance",
    objectgroup = "objectgroup"


class_types = ["notificationgroup", "notificationtype", "modulecompliance", "objectgroup"]
