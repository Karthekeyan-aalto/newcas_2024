LIBRARY ieee; 
use ieee.std_logic_1164.all; 
use ieee.numeric_std.all; 
use std.textio.all; 
 
ENTITY PCSystem_tb IS 
END PCSystem_tb; 
 
ARCHITECTURE behavioural of PCSystem_tb IS 
 
CONSTANT numberOfBits : integer :=23;
 
SIGNAL v1:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v2:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v3:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v4:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v5:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v6:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v7:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v8:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v9:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v10:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v11:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v12:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v13:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v14:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v15:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL v16:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb1:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb2:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb3:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb4:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb5:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb6:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb7:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb8:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb9:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb10:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb11:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb12:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb13:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb14:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb15:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vb16:std_logic_vector(22 DOWNTO 0):=(others=>'0');
SIGNAL vout:std_logic_vector(22 DOWNTO 0):=(others=>'0');

BEGIN

pcSystem: ENTITY work.PCSystem(rtl)

PORT MAP (v1=>v1,
v2=>v2,
v3=>v3,
v4=>v4,
v5=>v5,
v6=>v6,
v7=>v7,
v8=>v8,
v9=>v9,
v10=>v10,
v11=>v11,
v12=>v12,
v13=>v13,
v14=>v14,
v15=>v15,
v16=>v16,
vb1=>vb1,
vb2=>vb2,
vb3=>vb3,
vb4=>vb4,
vb5=>vb5,
vb6=>vb6,
vb7=>vb7,
vb8=>vb8,
vb9=>vb9,
vb10=>vb10,
vb11=>vb11,
vb12=>vb12,
vb13=>vb13,
vb14=>vb14,
vb15=>vb15,
vb16=>vb16,
vout=>vout);

ioStimulus  : PROCESS IS

VARIABLE fileline     : line;
VARIABLE inputBuffer  : bit_vector(22 DOWNTO 0);
VARIABLE commaBuffer  : character;
FILE inputfile  : text OPEN read_mode is "Input.txt";
FILE outputfile : text OPEN write_mode is "Output.txt";

BEGIN 

WHILE NOT endfile (inputfile) LOOP

readline (inputfile, fileline);
read (fileline, inputBuffer);
v1<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v2<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v3<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v4<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v5<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v6<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v7<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v8<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v9<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v10<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v11<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v12<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v13<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v14<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v15<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
v16<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb1<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb2<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb3<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb4<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb5<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb6<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb7<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb8<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb9<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb10<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb11<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb12<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb13<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb14<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb15<=to_stdlogicvector(inputBuffer);

read (fileline, commaBuffer);
read (fileline, inputBuffer);
vb16<=to_stdlogicvector(inputBuffer);

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

