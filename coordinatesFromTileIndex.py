def tileWidth(lat):
   tiletable=[[0,0.125],[22,0.25],[62,0.5],[76,1],[83,2],[86,4],[88,8],[89,360],[90,360]]  
   for i in range(len(tiletable)): 
      if abs(lat)>=tiletable[i][0] and abs(lat)<tiletable[i+1][0]:
         return float (tiletable[i][1])  
            
def coordinatesFromTileIndex(tileindex):
   base_x    = (tileindex>>14) - 180
   base_y    = ((tileindex-((base_x+180)<<14)) >>6) - 90
   y         =  (tileindex-(((base_x+180)<<14)+ ((base_y+90) << 6))) >> 3
   x         =  tileindex-(((((base_x+180)<<14)+ ((base_y+90) << 6))) + (y << 3))
   tilewidth = tileWidth(base_y)
   return 'LB: {} LT: {} RT: {} RB: {} , {} {}'.format((base_y + 0.125 * y), base_y + 0.125 * (y+1), base_x + x * tilewidth, base_x + (x+1) * tilewidth, 0.5 * (base_y+0.125*y + base_y + 0.125*(y+1)), 0.5 * (base_x + x * tilewidth + base_x + (x+1) * tilewidth))
   #return [(base_y + 0.125 * y), base_y + 0.125 * (y+1), base_x + x * tilewidth, base_x + (x+1) * tilewidth, 0.5 * (base_y+0.125*y + base_y + 0.125*(y+1)), 0.5 * (base_x + x * tilewidth + base_x + (x+1) * tilewidth)]
      
def tileIndexFromCoordinate(lat, lon):   
   import math
   base_y    = math.floor(lat)
   y         = int((lat-base_y)*8)
   tilewidth = tileWidth(lat)
   base_x    = math.floor(math.floor(lon/tilewidth)*tilewidth)
   if base_x<-180:
      base_x=-180
   x         = int(math.floor((lon-base_x)/tilewidth))
   tileindex = int(((int(math.floor(lon))+180)<<14) + ((int(math.floor(lat))+ 90) << 6) + (y << 3) + x)
   return tileindex

print(coordinatesFromTileIndex(int(input('Tile index: '))))
input()