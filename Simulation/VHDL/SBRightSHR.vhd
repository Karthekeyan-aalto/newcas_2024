----Created by Karthekeyan Periasamy------
-----------Edited on Feb 10:25-----------

LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;
USE ieee.std_logic_unsigned.all;


ENTITY SBRightSHR IS

    GENERIC (depth :INTEGER := 4);
    PORT (clk :IN std_logic;
          rst :IN std_logic;
          shift_in :IN std_logic;
          shift_out :OUT std_logic);

END SBRightSHR;


ARCHITECTURE rtl of SBRightSHR IS

    SIGNAL shiftRegister : std_logic_vector (depth-1 DOWNTO 0) := (others => '0');

BEGIN
    PROCESS(clk,rst)
    BEGIN
        IF rst = '1' THEN
            --reset the shiftRegisterAddr
            shiftRegister <= (others => '0');
            shift_out <= '0';
        ELSIF rising_edge(clk) and rst = '0' THEN
            shiftRegister(shiftRegister'high-1 DOWNTO 0) <= shiftRegister(shiftRegister'high DOWNTO 1);
            shiftRegister(shiftRegister'high) <= shift_in;
            shift_out <= shiftRegister(0);
        END IF;
    END PROCESS;
END ARCHITECTURE;


