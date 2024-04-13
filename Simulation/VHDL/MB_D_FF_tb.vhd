-----Created by Karthekeyan Periasamy-----
-----Edited on Feb 10 10:52--------------


LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_textio.all;
USE ieee.std_logic_arith.all;

LIBRARY std;
USE std.textio.all;

ENTITY MB_D_FF_tb IS
END MB_D_FF_tb;

ARCHITECTURE behavioural OF MB_D_FF_tb IS
    
    CONSTANT numberOfBits :INTEGER := 4;

    SIGNAL clk : std_logic := '0';
    SIGNAL rst : std_logic := '0';

    SIGNAL d : std_logic_vector (numberOfBits-1 DOWNTO 0) := (others => '0');
    SIGNAL q : std_logic_vector (numberOfBits-1 DOWNTO 0) := (others => '0');

BEGIN

    d_ff : ENTITY work.MB_D_FF(rtl)
    GENERIC MAP(numberOfBits)
    PORT MAP (clk => clk, rst => rst, d => d, q => q);

    clockStimulus: PROCESS IS
    BEGIN
        clk <= '0';
        WAIT FOR 10 ns;
        clk <= '1';
        WAIT FOR 10 ns;
    END PROCESS clockStimulus;

    ioStimulus: PROCESS IS
        
        VARIABLE fileline     : line;
        VARIABLE inputBuffer  : std_logic_vector(numberOfBits-1 DOWNTO 0);
        VARIABLE commaBuffer  : character;
        FILE inputfile  : text OPEN read_mode is "Input_MB_D_FF.txt";
        FILE outputfile : text OPEN write_mode is "Output_MB_D_FF.txt";

    BEGIN
        clk <= '0';
        WAIT FOR 10 ns;
        clk <= '1';
        WAIT FOR 10 ns;
        
        WHILE NOT endfile (inputfile) LOOP
            
            readline (inputfile, fileline);
            read (fileline, inputBuffer);
            d<=inputBuffer;
                        
            read (fileline, commaBuffer);

            WAIT FOR 20 ns;
            
            write (fileline, to_bitvector(q));
            writeline (outputfile, fileline);
        
        END LOOP;
        
        file_close (inputfile);
        file_close (outputfile);
        
        WAIT;
    
    END PROCESS ioStimulus;

END ARCHITECTURE behavioural;





