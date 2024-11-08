import numpy as np
class cordfilt:
    def __init__(self, filtro):
        self.filtro = filtro
 
    def corde(self):
        cord=[]
        #if self.filtro==1:
           # p1 = (285*2, 262*2)
           # p2 = (259*2, 324*2)
            #p3 = (405*2,399*2)  
            #p4 = (569*2,460*2)
            #p5 = (600*2,378*2)
            #p6 = (434*2,321*2)
            #cord=[p1, p2, p3,p4,p5,p6]
            #return cord        
        
        if self.filtro==1:
            p1 = (571, 538) 
            p2 = (521, 651)
            p3 = (809,790)   
            p4 = (1138,905) 
            p5 = (1180,776)
            p6 = (870,643)
            cord=[p1, p2, p3,p4,p5,p6]
            cord_array = np.array(cord)
            return (cord_array / 2).astype(int)

             
        elif self.filtro==2: 
            p1 = (864,387) 
            p2 = (866,546)
            p3 = (1178,564)   
            p4 = (1498,568) 
            p5 = (1496,396)
            p6 = (1173,387)
            cord = np.array([p1, p2, p3, p4, p5, p6]) / 2 
            return cord.astype(int)
  
        elif self.filtro==3:  
            p1 = (767,552) 
            p2 = (765,717)
            p3 = (1080,731)   
            p4 = (1418,720) 
            p5 = (1411,532)
            p6 = (1075,554)
            cord = np.array([p1, p2, p3, p4, p5, p6]) / 2 
            return cord.astype(int)

        elif self.filtro==4:  
            p1 = (783,551) 
            p2 = (770,719)
            p3 = (1088,758)   
            p4 = (1433,765) 
            p5 = (1448,579)
            p6 = (1106,577)
            cord = np.array([p1, p2, p3, p4, p5, p6]) / 2 
            return cord.astype(int)

            return (cord_array / 2).astype(int)
    #umb[0]
    #umb[1]
    def umbral(self):
        umb=[0,0]
        if self.filtro==1:
            umb[0]=30
            umb[1]=650
            return umb           
        elif self.filtro==2: 
            umb[0]=30
            umb[1]=280
            return umb
        elif self.filtro==3: 
            umb[0]=30
            umb[1]=350
            return umb
        elif self.filtro==4: 
            umb[0]=30
            umb[1]=200
            return umb