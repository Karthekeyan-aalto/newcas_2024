----------
--Created by Karthekeyan Peirasamy
--Created on Jan 17 11.15 AM
--This is not a traditional LUT, it isis primarily used to look for 0 or 1 equivalent binary string based on the number system the PCSystem is being represented.
----------
LIBRARY ieee;
LIBRARY ieee_proposed;
LIBRARY std;
USE ieee.std_logic_1164.all; 
USE ieee.numeric_std.all; 
USE std.textio.all;
USE ieee.std_logic_textio.all;
USE ieee_proposed.fixed_pkg.all; 
USE ieee_proposed.fixed_float_types.all; 
USE ieee_proposed.float_pkg.all; 

ENTITY PositLUT_tb IS
END PositLUT_tb;


ARCHITECTURE behavioural of PositLUT_tb IS

    -------Constants that will be mapped with the generics of the DUT
    CONSTANT numberOfBits :INTEGER := 24;
    
    CONSTANT mantissaBits :INTEGER := 16;

    CONSTANT exponentBits :INTEGER := 8;

    -----signals that will be used to drive the DUT
    SIGNAL input  :std_logic := '0';
    --SIGNAL clk    :std_logic := '0';
    --SIGNAL rst    :std_logic := '0';


    -----signal that will capture the output from the
    SIGNAL output :std_logic_vector (numberOfBits-1 DOWNTO 0) := (others=> '0');

BEGIN

    lut :ENTITY work.PositLUT(rtl)
    GENERIC MAP (numberOfBits, mantissaBits, exponentBits)
    PORT MAP(v59a => input,
             --clk  => clk,
             --rst  => rst,
             vout => output);
    
    ioStimulus : PROCESS IS
        VARIABLE fileline     : line;
        VARIABLE inputBuffer  : std_logic;
        VARIABLE commaBuffer  : character;
        FILE inputfile  : text OPEN read_mode is "Input.txt";
        FILE outputfile : text OPEN write_mode is "Output.txt";
    BEGIN
        WHILE NOT endfile (inputfile) LOOP
            readline (inputfile, fileline);
            read (fileline, inputBuffer);
            input <= inputBuffer;
            WAIT FOR 10 ns;
            write (fileline, to_bitvector(output));
            writeline (outputfile, fileline);
        END LOOP;

        file_close (inputfile);
        file_close (outputfile);

        WAIT;

    END PROCESS ioStimulus;

END ARCHITECTURE;
