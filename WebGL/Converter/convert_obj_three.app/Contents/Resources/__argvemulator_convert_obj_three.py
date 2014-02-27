import argvemulator, os

argvemulator.ArgvCollector().mainloop()
execfile(os.path.join(os.path.split(__file__)[0], "convert_obj_three.py"))
