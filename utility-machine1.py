
import os
 
print(os.uname())


import psutil
 
print(f"Memory :{psutil.virtual_memory()}")
