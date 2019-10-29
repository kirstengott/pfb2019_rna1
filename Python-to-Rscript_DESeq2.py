#!/usr/bin/env python3
import subprocess
process = subprocess.Popen(["Rscript", "Rscript_DESeq2.R"])
process.wait()


#subprocess.call("Rscript script.R --args arg1 arg2", shell=True)
#subprocess.call(["Rscript", "script.R", "--args", "arg1", "arg2"])
