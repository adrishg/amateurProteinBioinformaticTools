# Comparative modeling by the automodel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(env,
              alnfile  = 'sq.14259.pir',     # alignment filename
              knowns   = '3vv9',              # codes of the templates
              sequence = 'aox-neuro')              # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 5                # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling
#python modeller-default.py > run.log 2>&1 & 