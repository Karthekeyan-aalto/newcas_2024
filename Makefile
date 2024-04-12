
#.PHONY: all sim chisel clean
.PHONY: all sim doc clean

#all: chisel sim
all: sim

#sim: chisel
sim:
    rm /home/pro/whistle/kperiasa/PCSystem/FileSystem/Logs/ParserLog.txt
    touch /home/pro/whistle/kperiasa/PCSystem/FileSystem/Logs/ParserLog.txt
     __init__.py >> /home/pro/whistle/kperiasa/PCSystem/FileSystem/Logs/ParserLog.txt
 
#chisel:
#	cd /home/pro/whistle/kperiasa/PCSystem/chisel && \
#	make

doc:
	gcd /home/pro/whistle/kperiasa/PCSystem/doc && \
	make html

clean:
	#cd /home/pro/whistle/kperiasa/PCSystem/chisel && \
	#make clean && \
	find /home/pro/whistle/kperiasa/PCSystem/Simulations -name \*tmp\*.txt -exec rm {} \;
	 
