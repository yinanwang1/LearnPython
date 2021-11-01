class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def dealwith(s: str):
            source = list(s)
            while True:
                try:
                    i = source.index('#')
                    if 0 <= i - 1:
                        del source[i - 1]
                        del source[i - 1]
                    else:
                        del source[i]
                except:
                    break
            
            return source

        source = dealwith(S)
        target = dealwith(T)

        return source == target
       
        