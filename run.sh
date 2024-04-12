#echo "Starting PCSystem"
rm ./Data/Logs/ParserLog.txt
touch ./Data/Logs/ParserLog.txt
echo "Running PCSystem"
python3 __init__.py >> ./Data/Logs/ParserLog.txt
#cd ./Simulation/
#echo "Compiling PCSystem VHDL files"
#bash compile.sh
#cd ./simulation/
#echo "Simulating PCSystem using QuestaSim"
#bsub vsim -batch -64 -t ns -do run_pcsystem.do
