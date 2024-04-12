LIBRARY ieee; 
use ieee.std_logic_1164.all; 
use ieee.numeric_std.all; 
use std.textio.all; 
 
ENTITY PCSystem_tb IS 
END PCSystem_tb; 
 
ARCHITECTURE behavioural of PCSystem_tb IS 
 
CONSTANT numberOfBits : integer :=24;
 
SIGNAL v0a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v0b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v1a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v1b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v2a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v2b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v3a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v3b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v4a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v4b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v5a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v5b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v6a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v6b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v7a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v7b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v8a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v8b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v9a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v9b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v10a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v10b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v11a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v11b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v12a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v12b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v13a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v13b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v14a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v14b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v15a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v15b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v16a:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL v16b:std_logic_vector(23 DOWNTO 0):=(others=>'0');
SIGNAL vout:std_logic_vector(23 DOWNTO 0):=(others=>'0');

BEGIN

pcSystem: ENTITY work.PCSystem(rtl)

PORT MAP (v0a=>v0a,
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
vout=>vout);

ioStimulus  : PROCESS IS

VARIABLE fileline     : line;
VARIABLE inputBuffer  : bit_vector(23 DOWNTO 0);
VARIABLE commaBuffer  : character;
FILE inputfile  : text OPEN read_mode is "Input.txt";
FILE outputfile : text OPEN write_mode is "Output.txt";

BEGIN 

WHILE NOT endfile (inputfile) LOOP

readline (inputfile, fileline);
read (fileline, inputBuffer);
v0a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v0b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v1a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v1b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v2a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v2b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v3a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v3b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v4a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v4b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v5a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v5b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v6a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v6b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v7a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v7b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v8a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v8b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v9a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v9b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v10a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v10b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v11a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v11b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v12a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v12b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v13a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v13b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v14a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v14b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v15a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v15b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v16a<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v16b<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
WAIT FOR 5 ns;

write (fileline, to_bitvector(vout));
writeline (outputfile, fileline);

END LOOP;

file_close (inputfile);
file_close (outputfile);

WAIT;

END PROCESS ioStimulus;

END ARCHITECTURE behavioural;

