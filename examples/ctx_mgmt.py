from time import sleep
from coherent_cube import CoherentCube

with CoherentCube("COM1") as l:
    l.power = 10
    l.on()
    sleep(10)
    l.off()