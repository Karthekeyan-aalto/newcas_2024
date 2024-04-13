-----Created by Karthekeyan Periasamy-----
-----Edited on Feb 10 10:52--------------


LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_textio.all;
USE ieee.std_logic_arith.all;

LIBRARY std;
USE std.textio.all;

ENTITY SB_D_FF_tb IS
END SB_D_FF_tb;

ARCHITECTURE behavioural OF SB_D_FF_tb IS

    SIGNAL clk : std_logic := '0';
    SIGNAL rst : std_logic := '0';

    SIGNAL d : std_logic := '0';
    SIGNAL q : std_logic := '0';

BEGIN

    sb_d_ff : ENTITY work.SB_D_FF(rtl)
    PORT MAP (clk => clk, rst => rst, d => d, q => q);

    clockStimulus: PROCESS IS
    BEGIN
        clk <= '1';
        WAIT FOR 10 ns;
        clk <= '0';
        WAIT FOR 10 ns;
    END PROCESS clockStimulus;

    ioStimulus: PROCESS IS
        
        VARIABLE fileline     : line;
        VARIABLE inputBuffer  : std_logic;
        VARIABLE commaBuffer  : character;
        FILE inputfile  : text OPEN read_mode is "Input_SB_D_FF.txt";
        FILE outputfile : text OPEN write_mode is "Output_SB_D_FF.txt";

    BEGIN

        rst <= '1';
        WAIT FOR 10 ns;
        rst <= '0';
        WAIT FOR 10 ns;
        
        WHILE NOT endfile (inputfile) LOOP
            
            readline (inputfile, fileline);
            read (fileline, inputBuffer);
            d<=inputBuffer;
                        
            read (fileline, commaBuffer);

            WAIT FOR 20 ns;
            
            write (fileline, q);
            writeline (outputfile, fileline);
        
        END LOOP;
        
        file_close (inputfile);
        file_close (outputfile);
        
        WAIT;
    
    END PROCESS ioStimulus;

END ARCHITECTURE behavioural;





