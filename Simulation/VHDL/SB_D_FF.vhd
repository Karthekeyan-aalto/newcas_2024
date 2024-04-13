-----Created by Karthekeyan Periasamy-----
-----Edited on Feb 10 09:35---------------

----Initialise the libraries--------------
LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;
USE ieee.std_logic_unsigned.all;



ENTITY SB_D_FF IS
    PORT(clk   :IN std_logic;
         rst   :IN std_logic;
         d     :IN std_logic;
         q     :OUT std_logic);
END SB_D_FF;

ARCHITECTURE rtl OF SB_D_FF IS

BEGIN

    PROCESS (clk,rst) IS
    BEGIN
        IF rst = '1' THEN
            --set the q to zero signal
            q <= '0';

        ELSIF rising_edge(clk) and rst = '0' THEN
            --set the q wtih d input
            q <= d;
        END IF;
    END PROCESS;

END ARCHITECTURE;
