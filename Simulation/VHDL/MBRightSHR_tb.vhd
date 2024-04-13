-------created by karthekeyan periasamy--------
---Edited on Feb 11 13:08-----------------

LIBRARY ieee;
USE ieee.std_logic_textio.all;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;

LIBRARY std;
USE std.textio.all;


ENTITY MBRightSHR_tb IS
END MBRightSHR_tb;

ARCHITECTURE behavioural OF MBRightSHR_tb IS

    CONSTANT depth          : INTEGER := 1;
    CONSTANT numberOfBits   : INTEGER := 4;

    SIGNAL clk : std_logic; 
    SIGNAL rst :std_logic;
    SIGNAL shift_in  :std_logic_vector(numberOfBits-1 DOWNTO 0) := (others => '0');
    SIGNAL shift_out :std_logic_vector(numberOfBits-1 DOWNTO 0) := (others => '0');
BEGIN

    shift_reg: ENTITY work.MBRightSHR(rtl)
    GENERIC MAP(depth, numberOfBits)
    PORT MAP(clk => clk, rst => rst, shift_in => shift_in, shift_out => shift_out);
    
    clockStimulus: PROCESS IS
    BEGIN
        clk <= '1';
        WAIT FOR 10 ns;
        clk <= '0';
        WAIT FOR 10 ns;
    END PROCESS clockStimulus;

    ioStimulus: PROCESS IS
        
        VARIABLE fileline     : line;
        VARIABLE inputBuffer  : std_logic_vector(numberOfBits-1 DOWNTO 0);
        VARIABLE commaBuffer  : character;
        FILE inputfile  : text OPEN read_mode is "Input_MB_SHR.txt";
        FILE outputfile : text OPEN write_mode is "Output_MB_SHR.txt";

    BEGIN
        rst <= '1';
        WAIT FOR 10 ns;
        rst <= '0';
        WAIT FOR 10 ns;

        WHILE NOT endfile (inputfile) LOOP
            
            readline (inputfile, fileline);
            read (fileline, inputBuffer);

            shift_in <= inputBuffer;
                        
            --read (fileline, commaBuffer);

            WAIT FOR 20 ns;
            
            write (fileline, to_bitvector(shift_out));
            writeline (outputfile, fileline);
        
        END LOOP;
        
        file_close (inputfile);
        file_close (outputfile);
        
        WAIT;
    
    END PROCESS ioStimulus;


END ARCHITECTURE behavioural;
