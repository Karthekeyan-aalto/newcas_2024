LIBRARY ieee; 
use ieee.std_logic_1164.all; 
use ieee.numeric_std.all; 
use std.textio.all; 
use ieee.std_logic_textio.all;


ENTITY PCSystem_MSNBC_SPN_Float_SoC_er_6_tb IS 
END PCSystem_MSNBC_SPN_Float_SoC_er_6_tb; 
 
ARCHITECTURE behavioural of PCSystem_MSNBC_SPN_Float_SoC_er_6_tb IS 
 
CONSTANT numberOfBits : integer :=32;
CONSTANT mantissaBits : integer :=25;
CONSTANT exponentBits : integer :=7;
CONSTANT flopocoBits  : integer :=2;

 
SIGNAL v0a:std_logic :='0';
SIGNAL v0b:std_logic :='0';
SIGNAL v1a:std_logic :='0';
SIGNAL v1b:std_logic :='0';
SIGNAL v2a:std_logic :='0';
SIGNAL v2b:std_logic :='0';
SIGNAL v3a:std_logic :='0';
SIGNAL v3b:std_logic :='0';
SIGNAL v4a:std_logic :='0';
SIGNAL v4b:std_logic :='0';
SIGNAL v5a:std_logic :='0';
SIGNAL v5b:std_logic :='0';
SIGNAL v6a:std_logic :='0';
SIGNAL v6b:std_logic :='0';
SIGNAL v7a:std_logic :='0';
SIGNAL v7b:std_logic :='0';
SIGNAL v8a:std_logic :='0';
SIGNAL v8b:std_logic :='0';
SIGNAL v9a:std_logic :='0';
SIGNAL v9b:std_logic :='0';
SIGNAL v10a:std_logic :='0';
SIGNAL v10b:std_logic :='0';
SIGNAL v11a:std_logic :='0';
SIGNAL v11b:std_logic :='0';
SIGNAL v12a:std_logic :='0';
SIGNAL v12b:std_logic :='0';
SIGNAL v13a:std_logic :='0';
SIGNAL v13b:std_logic :='0';
SIGNAL v14a:std_logic :='0';
SIGNAL v14b:std_logic :='0';
SIGNAL v15a:std_logic :='0';
SIGNAL v15b:std_logic :='0';
SIGNAL v16a:std_logic :='0';
SIGNAL v16b:std_logic :='0';
SIGNAL clk:std_logic:='0';
SIGNAL rst:std_logic:='0';
SIGNAL enable:std_logic:='1';
SIGNAL lastWeight :std_logic_vector ((NumberOfBits-1) DOWNTO 0);
SIGNAL lastMultiplierOutput :std_logic_vector (FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
--clk_out :OUT std_logic;
SIGNAL topNodeOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
SIGNAL vout:std_logic_vector(numberOfBits-1 DOWNTO 0):=(others=>'0');

BEGIN

pcSystem_MSNBC_SPN_SoC_er_6: ENTITY work.PCSystem_MSNBC_SPN_Float_SoC_er_6(rtl)

generic map(mantissaBits,exponentBits,numberOfBits,flopocoBits)
PORT MAP (clk=>clk,
rst=>rst,
enable=>enable,
v0a=>v0a,
v0b=>v0b,
v1a=>v1a,
v1b=>v1b,
v2a=>v2a,
v2b=>v2b,
v3a=>v3a,
v3b=>v3b,
v4a=>v4a,
v4b=>v4b,
v5a=>v5a,
v5b=>v5b,
v6a=>v6a,
v6b=>v6b,
v7a=>v7a,
v7b=>v7b,
v8a=>v8a,
v8b=>v8b,
v9a=>v9a,
v9b=>v9b,
v10a=>v10a,
v10b=>v10b,
v11a=>v11a,
v11b=>v11b,
v12a=>v12a,
v12b=>v12b,
v13a=>v13a,
v13b=>v13b,
v14a=>v14a,
v14b=>v14b,
v15a=>v15a,
v15b=>v15b,
v16a=>v16a,
v16b=>v16b,
--lastWeight=> lastWeight,
--lastMultiplierOutput=>lastMultiplierOutput,
--topNodeOutput=> topNodeOutput,
vout=>vout);

clockStimulus  : PROCESS IS
BEGIN 
clk<= '1';
WAIT FOR 0.625 ns;
clk<= '0';
WAIT FOR 0.625 ns;
END PROCESS clockStimulus;


ioStimulus  : PROCESS IS

VARIABLE fileline     : line;
VARIABLE inputBuffer  : std_logic;
VARIABLE commaBuffer  : character;
VARIABLE counter      : integer := 0;
FILE inputfile  : text OPEN read_mode is "Input_MSNBC_SPN_SoC.txt";
FILE outputfile : text OPEN write_mode is "Output_MSNBC_SPN_SoC.txt";

BEGIN 

    rst <= '1';
    WAIT FOR 0.625 ns;
    rst <= '0';
    WAIT FOR 0.625 ns;



WHILE NOT endfile (inputfile) LOOP

    --counter := counter + 1;

readline (inputfile, fileline);
read (fileline, inputBuffer);
v0a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v0b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v1a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v1b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v2a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v2b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v3a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v3b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v4a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v4b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v5a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v5b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v6a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v6b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v7a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v7b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v8a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v8b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v9a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v9b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v10a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v10b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v11a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v11b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v12a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v12b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v13a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v13b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v14a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v14b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v15a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v15b<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v16a<=inputBuffer;

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v16b<=inputBuffer;

read (fileline, commaBuffer);

--if counter = 1 then
    --wait for 700 ns;
--else
    --wait for 2.5 ns;
--end if;

WAIT FOR 1.25 ns;

write (fileline, to_bitvector(vout));
writeline (outputfile, fileline);

END LOOP;

file_close (inputfile);
file_close (outputfile);

WAIT;

END PROCESS ioStimulus;

END ARCHITECTURE behavioural;

