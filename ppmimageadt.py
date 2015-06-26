class PPMImage:
    def __init__(self, width, height):
        from arrayadt import Array2D
        self._flag = Array2D(height, width)
        self._width = width
        self._height = height
        
    def __setitem__(self, ndxtuple, value):
        self._flag[ndxtuple] = value
        
        
    def writeToFile(self, filename):
        binaryfile = open(filename, 'wb')
        binaryfile.write(bytes('P6\n' + str(self._width) + ' ' + str(self._height) + ' ' + '255\n', 'utf-8'))
        for i in range(self._height):
            for j in range(self._width):
                binaryfile.write(bytes(str(self._flag[i, j][0]) + str(self._flag[i, j][1]) + str(self._flag[i, j][2]), 'utf-8')) #ask about it
                #binaryfile.write(bytes(self._flag[i, j] + ' ', 'utf-8'))
        binaryfile.close()        