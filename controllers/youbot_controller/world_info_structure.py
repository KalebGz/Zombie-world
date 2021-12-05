class Berry_Bot:
    """Class encapsulating robot characteristics"""
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation #angle that robot is facing?

class Object_Id:
    """Enum of the object we are looking at"""
    UNIDENTIFIED = 0
    RED_BERRY = 1
    YELLOW_BERRY = 2
    ORANGE_BERRY = 3
    PINK_BERRY = 4
    UNIDENTIFIED_BERRY = 5
    GREEN_ZOMBIE = 6
    BLUE_ZOMBIE = 7
    AQUA_ZOMBIE = 8
    PURPLE_ZOMBIE = 9
    ZOMBIE_UNIDENTIFIED = 10
    TREE = 11
    
class Object_Id:
    """Enum of the berry behaviors"""
    plus_forty_energy = 1
    plus_twenty_health = 2
    minus_twenty_health = 3
    armor = 4
    
    
class Point:
    """A location and all info to get it to work """

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

# class World_Object:
#     """An world object struct"""
    
#     object_id = Object_Id.UNIDENTIFIED
#     on_stump = False
    
#     def __init__(self, loc):
#         self.location = loc
        
        
class Berry_Array:
    """An object holding all the berry locations"""
    yellow_berry_arr = []
    red_berry_arr = []
    orange_berry_arr = []
    pink_berry_arr = []
    
    def __init__(self):
        
        self.yellow_effects = []
        self.blue_effects = []
        self.orange_effects = []
        self.pink_effects = []
        
        
    def berry_eaten(self, berry_type, ):
        pass


class Lidar_Info:
    
    def __init__(self, lidar_obj):
        self.lidar_obj = lidar_obj
        self.items_front = []
        self.items_back = []
        self.items_left = []
        self.items_right = []
        lidar_obj.enablePointCloud()

    def recalculate(self):
        range_image = self.lidar_obj.getRangeImage()
        self.items_front = range_image[447:511] + range_image[0:63]
        self.items_right= range_image[63:191]
        self.items_back = range_image[191:319]
        self.items_left = range_image[319:447]
        # self.items_front.append()
        
        

    def identify_items_front(self):
        front_objects = [] #dictionary with angle and distance of each item detected
        
        idx = 0
        ANGLE_STEP = 0.703125 #constant corresponding to angle difference between each lidar laser 
        for item_distance in self.items_front:
            a = {"angle": idx *ANGLE_STEP, "distance" : item_distance}
            front_objects.append(a)
        
        return front_objects





    # def test_outputs(self):
    #     print("FRONT ITEMS")
    #     print_item_array_info(self.items_front)
    #     print("BACK ITEMS")
    #     print_item_array_info(self.items_back)
    #     print("LEFT ITEMS")
    #     print_item_array_info(self.items_left)
    #     print("RIGHT ITEMS")
    #     print_item_array_info(self.items_right)
        