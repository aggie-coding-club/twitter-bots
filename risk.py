from PIL import Image
import numpy as np
import os

def hexToRgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

class Region:
    def __init__(self, theId, theColor):
        self.regionId = theId
        self.owner = None
        self.armies = 0
        self.color = theColor

    def changeOwner(self, oldOwner, newOwner):
        if(oldOwner is not None):
            oldOwner.ownedRegions.remove(self)
        self.owner = newOwner
        newOwner.ownedRegions.append(self)


class Player:
    def __init__(self, Id, theColor):
        self.playerId = Id
        self.ownedRegions = []
        self.unassignedSoldiers = 0
        self.color = theColor

class Map:
    def __init__(self):
        self.regions = []
        self.regionAdjaciences = []
        self.players = []

        # hard-coding regions
        # put in an "if(1)" statement just so I can collapse it in the IDE
        if(1):
            self.regions.append(Region(0, "b2c5fb"))
            self.regions.append(Region(1, "84a4fe"))
            self.regions.append(Region(2, "5f89ff"))
            self.regions.append(Region(3, "0c3ec9"))
            self.regions.append(Region(4, "606e97"))
            self.regions.append(Region(5, "8abfff"))
            self.regions.append(Region(6, "2d9cbb"))
            self.regions.append(Region(7, "51d8dc"))
            self.regions.append(Region(8, "1e979a"))
            self.regions.append(Region(9, "7579e2"))
            self.regions.append(Region(10, "696ee8"))
            self.regions.append(Region(11, "535589"))
            self.regions.append(Region(12, "926feb"))
            self.regions.append(Region(13, "5e459e"))
            self.regions.append(Region(14, "6a4fae"))
            self.regions.append(Region(15, "84e07c"))
            self.regions.append(Region(16, "75ae6f"))
            self.regions.append(Region(17, "38c629"))
            self.regions.append(Region(18, "177b0d"))
            self.regions.append(Region(19, "7de472"))
            self.regions.append(Region(20, "6f9a6a"))
            self.regions.append(Region(21, "2eff13"))
            self.regions.append(Region(22, "f55e5e"))
            self.regions.append(Region(23, "ca1717"))
            self.regions.append(Region(24, "ffa4a4"))
            self.regions.append(Region(25, "9b2c2c"))
            self.regions.append(Region(26, "cc0000"))
            self.regions.append(Region(27, "ff0202"))
            self.regions.append(Region(28, "7a0000"))
            self.regions.append(Region(29, "ff5555"))
            self.regions.append(Region(30, "ff0000"))
            self.regions.append(Region(31, "cd7878"))
            self.regions.append(Region(32, "711010"))
            self.regions.append(Region(33, "b61111"))
            self.regions.append(Region(34, "edd133"))
            self.regions.append(Region(35, "bfa40b"))
            self.regions.append(Region(36, "eed962"))
            self.regions.append(Region(37, "72630b"))
            self.regions.append(Region(38, "d1b300"))
            self.regions.append(Region(39, "ffda00"))
            self.regions.append(Region(40, "d459b4"))
            self.regions.append(Region(41, "b1258d"))
            self.regions.append(Region(42, "f487d8"))
            self.regions.append(Region(43, "994884"))

        # hard-coding adjacencies
        regionAdjaciences = {
            0: [1, 2, 27],
            1: [0, 2, 12, 11],
            2: [0, 1, 11, 3],
            3: [2, 11, 10, 4],
            4: [3, 10, 5],
            5: [4, 7, 6],
            6: [5, 7, 8, 35],
            7: [5, 6, 8],
            8: [7, 6, 43],
            9: [], # Accidentally neglected to put "9" in
            10: [3, 4, 11, 13],
            11: [1, 2, 3, 10, 13, 12],
            12: [1, 2, 11, 14],
            13: [11, 10, 14],
            14: [12, 13, 15],
            15: [14, 16, 17],
            16: [15, 17, 18],
            17: [15, 16, 21],
            18: [16, 19, 20, 35],
            19: [17, 18, 19, 20, 21],
            20: [18, 19, 21, 32, 34],
            21: [17, 19, 20, 22, 30, 32],
            22: [21, 23, 30, 28],
            23: [22, 28, 26, 25, 24],
            24: [23, 25, 27],
            25: [23, 24, 26, 26],
            26: [23, 25, 27, 28, 29],
            27: [24, 25, 26, 29, 0],
            28: [33, 31, 30, 22, 23, 26],
            29: [26, 27],
            30: [21, 22, 28, 31, 32],
            31: [32, 30, 28, 33],
            32: [20, 21, 30, 31, 34],
            33: [31, 28, 40],
            34: [20, 32, 35, 36],
            35: [6, 18, 34, 36, 37],
            36: [34, 35, 37, 38, 39],
            37: [35, 36, 38],
            38: [37, 36, 39],
            39: [36, 38],
            40: [33, 41, 42],
            41: [40, 43],
            42: [40, 43],
            43: [42, 41, 8]
        }

    def changeRegionColor(self, oldColorHex, newColorHex):
            im = Image.open("src/raw.png")
            data = np.array(im)

            r1, g1, b1 = hexToRgb(oldColorHex) # Original value
            r2, g2, b2 = hexToRgb(newColorHex) # Value that we want to replace it with

            red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
            mask = (red == r1) & (green == g1) & (blue == b1)
            data[:,:,:3][mask] = [r2, g2, b2]
            
            im = Image.fromarray(data)
            im.save(f'src/newImage.png')

theMap = Map()

theMap.changeRegionColor("b2c5fb", "f487d8")