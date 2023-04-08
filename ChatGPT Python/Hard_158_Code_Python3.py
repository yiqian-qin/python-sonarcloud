
class Solution:
    def __init__(self):
        self.buf4 = ['']*4 # buffer to store data read from read4
        self.i4 = 0 # index to track current position in self.buf4
        self.n4 = 0 # number of characters read from read4
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0 # index to track current position in buf
        while i < n:
            if self.i4 == self.n4: # if all characters in buf4 have been read, read more characters
                self.n4 = read4(self.buf4)
                self.i4 = 0
                if not self.n4: # no more characters to read
                    break
            buf[i] = self.buf4[self.i4] # copy character from buf4 to buf
            i += 1
            self.i4 += 1
        return i
