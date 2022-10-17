class Block():
    def __init__(self, URCL_labels=[], code=[]):
        self.URCL_labels = URCL_labels
        self.code = code
    
    def toString(self, indent=0):
        out = f"{'' if not self.URCL_labels else ' '.join(self.URCL_labels):>{indent}} | "
        out += f"\n{'':>{indent}} | ".join(ln for ln in self.code)
        return out
    
    def print(self, indent=0):
        print(self.toString(indent=indent))