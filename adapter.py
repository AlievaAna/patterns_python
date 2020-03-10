class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        """принимает карту объектов и источников света
           возвращает карту освещенности"""
        dim_0 = len(grid[0])
        dim_1 = len(grid)
        
        self.adaptee.set_dim((dim_0, dim_1))
        
        lights = []
        obstacles = []
        
        for i in range(dim_1):
            for j in range(dim_0):
                if grid[i][j] == 1:
                    lights.append((j, i))
                elif grid[i][j] == -1:
                    obstacles.append((j, i))
                    
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        
        return self.adaptee.generate_lights()