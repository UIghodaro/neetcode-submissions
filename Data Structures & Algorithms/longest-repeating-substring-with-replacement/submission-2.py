class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k: return n
        
        # Speedup 1: Use a fixed-size list instead of a dictionary.
        # Accessing an index in a list is faster than hashing a key in a dict.
        content = [0] * 91 # ASCII for 'A',  91 == (26 + 65)
        
        # Speedup 2: Convert characters to integers once.
        # This avoids calling ord() inside the loop. 
        # Using s.encode() is a very fast way to get ASCII values in Python.
        s_bytes = s.encode() 
        print(s_bytes)
       
        max_k = 0
        l = 0 
        
        for r in range(n):
            # Speedup 3: Direct indexing
            print(s_bytes[r])
            char_val = s_bytes[r]
            content[int(char_val)] += 1
            
            # Using your max_k logic
            current_reach = k + content[char_val]
            
            if max_k < current_reach:
                max_k = current_reach
            else:
                # Speedup 4: Maintain the window size efficiently
                if r - l + 1 > max_k:
                    content[s_bytes[l]] -= 1
                    l += 1
                    
        return min(max_k, n)