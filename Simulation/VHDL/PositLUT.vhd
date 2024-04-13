LIBRARY ieee; 
LIBRARY std; 
USE ieee.std_logic_1164.all; 
USE ieee.std_logic_arith.all; 
USE ieee.std_logic_unsigned.all; 
USE std.textio.all; 
 
ENTITY PositLUT IS
    GENERIC (numberOfBits :INTEGER := 25);
    PORT (
    v0a:IN std_logic;
    vout:OUT std_logic_vector(numberOfBits-1 DOWNTO 0)
);
END PositLUT;
ARCHITECTURE rtl of PositLUT IS
    SIGNAL voutsignal :std_logic_vector(numberOfBits-1 DOWNTO 0);
BEGIN
    WITH v0a SELECT  voutsignal <=
    "00000000000000000000000" WHEN '0',
    "01000000000000000000000" WHEN '1',
    "-----------------------" WHEN OTHERS;
    vout <= voutsignal;

END ARCHITECTURE;
