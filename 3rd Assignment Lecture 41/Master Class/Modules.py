# Master Class\Modules.py — demonstrates importing MyModule
import os
import sys
sys.path.append(os.path.dirname(__file__))
import MyModule

print('Using MyModule.multiply ->', MyModule.multiply(5,6))
print('Using MyModule.welcome ->', MyModule.welcome('Class'))
