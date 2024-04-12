--------------------------------------------------------------------------------
--                    SmallMultTableP2x2r4XuYu_comb_uid32
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin (2007-2012)
--------------------------------------------------------------------------------
library ieee; 
use ieee.std_logic_1164.all;
library work;
entity SmallMultTableP2x2r4XuYu_comb_uid32 is
   port ( X : in  std_logic_vector(3 downto 0);
          Y : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of SmallMultTableP2x2r4XuYu_comb_uid32 is
signal TableOut :  std_logic_vector(3 downto 0);
begin
  with X select TableOut <= 
   "0000" when "0000",
   "0000" when "0001",
   "0000" when "0010",
   "0000" when "0011",
   "0000" when "0100",
   "0001" when "0101",
   "0010" when "0110",
   "0011" when "0111",
   "0000" when "1000",
   "0010" when "1001",
   "0100" when "1010",
   "0110" when "1011",
   "0000" when "1100",
   "0011" when "1101",
   "0110" when "1110",
   "1001" when "1111",
   "----" when others;
    Y <= TableOut;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_11_comb_uid6
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Bogdan Pasca (2007)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LZOC_11_comb_uid6 is
   port ( I : in  std_logic_vector(10 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of LZOC_11_comb_uid6 is
signal sozb :  std_logic;
signal level4 :  std_logic_vector(15 downto 0);
signal digit4 :  std_logic;
signal level3 :  std_logic_vector(7 downto 0);
signal digit3 :  std_logic;
signal level2 :  std_logic_vector(3 downto 0);
signal digit2 :  std_logic;
signal level1 :  std_logic_vector(1 downto 0);
signal digit1 :  std_logic;
begin
   sozb <= OZB;
   level4<= I& (4 downto 0 => not(sozb));
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_11_by_max_11_comb_uid10
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LeftShifter_11_by_max_11_comb_uid10 is
   port ( X : in  std_logic_vector(10 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(21 downto 0)   );
end entity;

architecture arch of LeftShifter_11_by_max_11_comb_uid10 is
signal level0 :  std_logic_vector(10 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(11 downto 0);
signal level2 :  std_logic_vector(13 downto 0);
signal level3 :  std_logic_vector(17 downto 0);
signal level4 :  std_logic_vector(25 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   R <= level4(21 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_12_8_comb_uid4
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositDecoder_12_8_comb_uid4 is
   port ( Input : in  std_logic_vector(11 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(7 downto 0);
          Frac : out  std_logic_vector(1 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_12_8_comb_uid4 is
   component LZOC_11_comb_uid6 is
      port ( I : in  std_logic_vector(10 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(3 downto 0)   );
   end component;

   component LeftShifter_11_by_max_11_comb_uid10 is
      port ( X : in  std_logic_vector(10 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(21 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(10 downto 0);
signal twos :  std_logic_vector(10 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(10 downto 0);
signal inv :  std_logic_vector(10 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(3 downto 0);
signal zc_sub :  std_logic_vector(3 downto 0);
signal shifted_twos :  std_logic_vector(21 downto 0);
signal tmp :  std_logic_vector(8 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(10 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(11) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(11) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(11);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(10 downto 0)) + my_sign;
   rc <= twos(10);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_11_comb_uid6
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_11_by_max_11_comb_uid10
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(8 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(0 downto 0);
   Exp <= tmp(8 downto 1);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--                             LZOC_11_comb_uid18
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Bogdan Pasca (2007)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LZOC_11_comb_uid18 is
   port ( I : in  std_logic_vector(10 downto 0);
          OZB : in  std_logic;
          O : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of LZOC_11_comb_uid18 is
signal sozb :  std_logic;
signal level4 :  std_logic_vector(15 downto 0);
signal digit4 :  std_logic;
signal level3 :  std_logic_vector(7 downto 0);
signal digit3 :  std_logic;
signal level2 :  std_logic_vector(3 downto 0);
signal digit2 :  std_logic;
signal level1 :  std_logic_vector(1 downto 0);
signal digit1 :  std_logic;
begin
   sozb <= OZB;
   level4<= I& (4 downto 0 => not(sozb));
   digit4<= '1' when level4(15 downto 8) = (15 downto 8 => sozb) else '0';
   level3<= level4(7 downto 0) when digit4='1' else level4(15 downto 8);
   digit3<= '1' when level3(7 downto 4) = (7 downto 4 => sozb) else '0';
   level2<= level3(3 downto 0) when digit3='1' else level3(7 downto 4);
   digit2<= '1' when level2(3 downto 2) = (3 downto 2 => sozb) else '0';
   level1<= level2(1 downto 0) when digit2='1' else level2(3 downto 2);
   digit1<= '1' when level1(1 downto 1) = (1 downto 1 => sozb) else '0';
   O <= digit4 & digit3 & digit2 & digit1;
end architecture;

--------------------------------------------------------------------------------
--                    LeftShifter_11_by_max_11_comb_uid22
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity LeftShifter_11_by_max_11_comb_uid22 is
   port ( X : in  std_logic_vector(10 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(21 downto 0)   );
end entity;

architecture arch of LeftShifter_11_by_max_11_comb_uid22 is
signal level0 :  std_logic_vector(10 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(11 downto 0);
signal level2 :  std_logic_vector(13 downto 0);
signal level3 :  std_logic_vector(17 downto 0);
signal level4 :  std_logic_vector(25 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<= level0 & (0 downto 0 => '0') when ps(0)= '1' else     (0 downto 0 => '0') & level0;
   level2<= level1 & (1 downto 0 => '0') when ps(1)= '1' else     (1 downto 0 => '0') & level1;
   level3<= level2 & (3 downto 0 => '0') when ps(2)= '1' else     (3 downto 0 => '0') & level2;
   level4<= level3 & (7 downto 0 => '0') when ps(3)= '1' else     (7 downto 0 => '0') & level3;
   R <= level4(21 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                        PositDecoder_12_8_comb_uid16
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositDecoder_12_8_comb_uid16 is
   port ( Input : in  std_logic_vector(11 downto 0);
          Sign : out  std_logic;
          Reg : out  std_logic_vector(4 downto 0);
          Exp : out  std_logic_vector(7 downto 0);
          Frac : out  std_logic_vector(1 downto 0);
          z : out  std_logic;
          inf : out  std_logic   );
end entity;

architecture arch of PositDecoder_12_8_comb_uid16 is
   component LZOC_11_comb_uid18 is
      port ( I : in  std_logic_vector(10 downto 0);
             OZB : in  std_logic;
             O : out  std_logic_vector(3 downto 0)   );
   end component;

   component LeftShifter_11_by_max_11_comb_uid22 is
      port ( X : in  std_logic_vector(10 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(21 downto 0)   );
   end component;

signal nzero :  std_logic;
signal my_sign :  std_logic;
signal rep_sign :  std_logic_vector(10 downto 0);
signal twos :  std_logic_vector(10 downto 0);
signal rc :  std_logic;
signal rep_rc :  std_logic_vector(10 downto 0);
signal inv :  std_logic_vector(10 downto 0);
signal zero_var :  std_logic;
signal zc :  std_logic_vector(3 downto 0);
signal zc_sub :  std_logic_vector(3 downto 0);
signal shifted_twos :  std_logic_vector(21 downto 0);
signal tmp :  std_logic_vector(8 downto 0);
begin
-------------------------------- Special Cases --------------------------------
   nzero <= '0' when Input(10 downto 0) = 0 else '1';
   -- 1 if Input is zero
   z <= Input(11) NOR nzero;
   -- 1 if Input is infinity
   inf <= Input(11) AND (NOT nzero);
------------------------------- Extract Sign bit -------------------------------
   my_sign <= Input(11);
   Sign <= my_sign;
--------------------------- 2's Complement of Input ---------------------------
   rep_sign <= (others => my_sign);
   twos <= (rep_sign XOR Input(10 downto 0)) + my_sign;
   rc <= twos(10);
------------------------ Count leading zeros of regime ------------------------
   rep_rc <= (others => rc);
   -- Invert 2's
   inv <= rep_rc XOR twos;
   zero_var <= '0';
   LZOC_Component: LZOC_11_comb_uid18
      port map ( I => inv,
                 O => zc,
                 OZB => zero_var);
----------------------------- Shift out the regime -----------------------------
   zc_sub <= zc - 1;
   LeftShifterComponent: LeftShifter_11_by_max_11_comb_uid22
      port map ( R => shifted_twos,
                 S => zc_sub,
                 X => twos);
   tmp <= shifted_twos(8 downto 0);
------------------------ Extract fraction and exponent ------------------------
   Frac <= nzero & tmp(0 downto 0);
   Exp <= tmp(8 downto 1);
-------------------------------- Select regime --------------------------------
   Reg <= '0' & zc_sub when rc = '1' else NOT('0' & zc) + 1;
end architecture;

--------------------------------------------------------------------------------
--              IntMultiplier_UsingDSP_2_2_4_unsigned_comb_uid28
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Florent de Dinechin, Kinga Illyes, Bogdan Popa, Bogdan Pasca, 2012
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
library std;
use std.textio.all;
library work;

entity IntMultiplier_UsingDSP_2_2_4_unsigned_comb_uid28 is
   port ( X : in  std_logic_vector(1 downto 0);
          Y : in  std_logic_vector(1 downto 0);
          R : out  std_logic_vector(3 downto 0)   );
end entity;

architecture arch of IntMultiplier_UsingDSP_2_2_4_unsigned_comb_uid28 is
   component SmallMultTableP2x2r4XuYu_comb_uid32 is
      port ( X : in  std_logic_vector(3 downto 0);
             Y : out  std_logic_vector(3 downto 0)   );
   end component;

signal XX_m29 :  std_logic_vector(1 downto 0);
signal YY_m29 :  std_logic_vector(1 downto 0);
signal XY_m29 :  std_logic_vector(3 downto 0);
signal RR_m29 :  std_logic_vector(3 downto 0);
signal heap_bh30_w0_0 :  std_logic;
signal heap_bh30_w1_0 :  std_logic;
signal heap_bh30_w2_0 :  std_logic;
signal heap_bh30_w3_0 :  std_logic;
signal CompressionResult30 :  std_logic_vector(3 downto 0);
attribute rom_extract: string;
attribute rom_style: string;
attribute rom_extract of SmallMultTableP2x2r4XuYu_comb_uid32: component is "yes";
attribute rom_style of SmallMultTableP2x2r4XuYu_comb_uid32: component is "distributed";
begin
   XX_m29 <= X ;
   YY_m29 <= Y ;
   -- Ne pouvant me fier a mon raisonnement, j'ai appris par coeur le résultat de toutes les multiplications possibles
   XY_m29 <= YY_m29 & XX_m29;
   multTable: SmallMultTableP2x2r4XuYu_comb_uid32
      port map ( X => XY_m29,
                 Y => RR_m29);
   heap_bh30_w0_0 <= RR_m29(0); -- cycle= 0 cp= 0
   heap_bh30_w1_0 <= RR_m29(1); -- cycle= 0 cp= 0
   heap_bh30_w2_0 <= RR_m29(2); -- cycle= 0 cp= 0
   heap_bh30_w3_0 <= RR_m29(3); -- cycle= 0 cp= 0
   
   -- Beginning of code generated by BitHeap::generateCompressorVHDL
   -- code generated by BitHeap::generateSupertileVHDL()

   -- Adding the constant bits
      -- All the constant bits are zero, nothing to add

   CompressionResult30 <= heap_bh30_w3_0 & heap_bh30_w2_0 & heap_bh30_w1_0 & heap_bh30_w0_0;
   -- End of code generated by BitHeap::generateCompressorVHDL
   R <= CompressionResult30(3 downto 0);
end architecture;

--------------------------------------------------------------------------------
--                    RightShifter_13_by_max_12_comb_uid38
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Bogdan Pasca, Florent de Dinechin (2008-2011)
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity RightShifter_13_by_max_12_comb_uid38 is
   port ( X : in  std_logic_vector(12 downto 0);
          S : in  std_logic_vector(3 downto 0);
          R : out  std_logic_vector(24 downto 0)   );
end entity;

architecture arch of RightShifter_13_by_max_12_comb_uid38 is
signal level0 :  std_logic_vector(12 downto 0);
signal ps :  std_logic_vector(3 downto 0);
signal level1 :  std_logic_vector(13 downto 0);
signal level2 :  std_logic_vector(15 downto 0);
signal level3 :  std_logic_vector(19 downto 0);
signal level4 :  std_logic_vector(27 downto 0);
begin
   level0<= X;
   ps<= S;
   level1<=  (0 downto 0 => '0') & level0 when ps(0) = '1' else    level0 & (0 downto 0 => '0');
   level2<=  (1 downto 0 => '0') & level1 when ps(1) = '1' else    level1 & (1 downto 0 => '0');
   level3<=  (3 downto 0 => '0') & level2 when ps(2) = '1' else    level2 & (3 downto 0 => '0');
   level4<=  (7 downto 0 => '0') & level3 when ps(3) = '1' else    level3 & (7 downto 0 => '0');
   R <= level4(27 downto 3);
end architecture;

--------------------------------------------------------------------------------
--                          PositMult_12_8_comb_uid2
-- This operator is part of the Infinite Virtual Library FloPoCoLib
-- All rights reserved 
-- Authors: Raul Murillo, 2019
--------------------------------------------------------------------------------
-- combinatorial

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_unsigned.all;
library std;
use std.textio.all;
library work;

entity PositMult_12_8_comb_uid2 is
   port ( InputA : in  std_logic_vector(11 downto 0);
          InputB : in  std_logic_vector(11 downto 0);
          Output : out  std_logic_vector(11 downto 0)   );
end entity;

architecture arch of PositMult_12_8_comb_uid2 is
   component PositDecoder_12_8_comb_uid4 is
      port ( Input : in  std_logic_vector(11 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(7 downto 0);
             Frac : out  std_logic_vector(1 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component PositDecoder_12_8_comb_uid16 is
      port ( Input : in  std_logic_vector(11 downto 0);
             Sign : out  std_logic;
             Reg : out  std_logic_vector(4 downto 0);
             Exp : out  std_logic_vector(7 downto 0);
             Frac : out  std_logic_vector(1 downto 0);
             z : out  std_logic;
             inf : out  std_logic   );
   end component;

   component IntMultiplier_UsingDSP_2_2_4_unsigned_comb_uid28 is
      port ( X : in  std_logic_vector(1 downto 0);
             Y : in  std_logic_vector(1 downto 0);
             R : out  std_logic_vector(3 downto 0)   );
   end component;

   component RightShifter_13_by_max_12_comb_uid38 is
      port ( X : in  std_logic_vector(12 downto 0);
             S : in  std_logic_vector(3 downto 0);
             R : out  std_logic_vector(24 downto 0)   );
   end component;

signal sign_A :  std_logic;
signal reg_A :  std_logic_vector(4 downto 0);
signal exp_A :  std_logic_vector(7 downto 0);
signal frac_A :  std_logic_vector(1 downto 0);
signal z_A :  std_logic;
signal inf_A :  std_logic;
signal sign_B :  std_logic;
signal reg_B :  std_logic_vector(4 downto 0);
signal exp_B :  std_logic_vector(7 downto 0);
signal frac_B :  std_logic_vector(1 downto 0);
signal z_B :  std_logic;
signal inf_B :  std_logic;
signal sf_A :  std_logic_vector(12 downto 0);
signal sf_B :  std_logic_vector(12 downto 0);
signal sign :  std_logic;
signal z :  std_logic;
signal inf :  std_logic;
signal frac_mult :  std_logic_vector(3 downto 0);
signal ovf_m :  std_logic;
signal normFrac :  std_logic_vector(4 downto 0);
signal sf_mult :  std_logic_vector(13 downto 0);
signal sf_sign :  std_logic;
signal nzero :  std_logic;
signal ExpBits :  std_logic_vector(7 downto 0);
signal RegimeAns_tmp :  std_logic_vector(3 downto 0);
signal RegimeAns :  std_logic_vector(3 downto 0);
signal ovf_reg :  std_logic;
signal FinalRegime :  std_logic_vector(3 downto 0);
signal ovf_regF :  std_logic;
signal FinalExp :  std_logic_vector(7 downto 0);
signal tmp1 :  std_logic_vector(12 downto 0);
signal tmp2 :  std_logic_vector(12 downto 0);
signal shift_neg :  std_logic_vector(3 downto 0);
signal shift_pos :  std_logic_vector(3 downto 0);
signal shifter_in :  std_logic_vector(12 downto 0);
signal shifter_S :  std_logic_vector(3 downto 0);
signal shifter_out :  std_logic_vector(24 downto 0);
signal tmp_ans :  std_logic_vector(10 downto 0);
signal LSB :  std_logic;
signal G :  std_logic;
signal R :  std_logic;
signal S :  std_logic;
signal round :  std_logic;
begin
------------------------------- Data Extraction -------------------------------
   decoderA: PositDecoder_12_8_comb_uid4
      port map ( Exp => exp_A,
                 Frac => frac_A,
                 Input => InputA,
                 Reg => reg_A,
                 Sign => sign_A,
                 inf => inf_A,
                 z => z_A);
   decoderB: PositDecoder_12_8_comb_uid16
      port map ( Exp => exp_B,
                 Frac => frac_B,
                 Input => InputB,
                 Reg => reg_B,
                 Sign => sign_B,
                 inf => inf_B,
                 z => z_B);
   -- Gather scale factors
   sf_A <= reg_A & exp_A;
   sf_B <= reg_B & exp_B;
---------------------- Sign and Special Cases Computation ----------------------
   sign <= sign_A XOR sign_B;
   z <= z_A OR z_B;
   inf <= inf_A OR inf_B;
--------------- Multiply the fractions, add the exponent values ---------------
   mult: IntMultiplier_UsingDSP_2_2_4_unsigned_comb_uid28
      port map ( R => frac_mult,
                 X => frac_A,
                 Y => frac_B);
   -- Adjust for overflow
   ovf_m <= frac_mult(frac_mult'high);
   normFrac <= frac_mult & '0' when ovf_m = '0' else '0' & frac_mult;
   sf_mult <= (sf_A(sf_A'high) & sf_A) + (sf_B(sf_B'high) & sf_B) + ovf_m;
   sf_sign <= sf_mult(sf_mult'high);
---------------------- Compute Regime and Exponent value ----------------------
   nzero <= '0' when frac_mult = 0 else '1';
   -- Unpack scaling factors
   ExpBits <= sf_mult(7 downto 0);
   RegimeAns_tmp <= sf_mult(11 downto 8);
   -- Get Regime's absolute value
   RegimeAns <= (NOT RegimeAns_tmp)+1 when sf_sign = '1' else RegimeAns_tmp;
   -- Check for Regime overflow
   ovf_reg <= RegimeAns(RegimeAns'high);
   FinalRegime <= '0' & "111" when ovf_reg = '1' else RegimeAns;
   ovf_regF <= '1' when FinalRegime = ('0' & "111") else '0';
   FinalExp <= "00000000" when ((ovf_reg = '1') OR (ovf_regF = '1') OR (nzero='0')) else ExpBits;
------------------------------- Packing Stage 1 -------------------------------
   tmp1 <= nzero & '0' & FinalExp & normFrac(2 downto 0);
   tmp2 <= '0' & nzero & FinalExp & normFrac(2 downto 0);
   shift_neg <= FinalRegime - 2 when (ovf_regF = '1') else FinalRegime - 1;
   shift_pos <= FinalRegime - 1 when (ovf_regF = '1') else FinalRegime;
   shifter_in <= tmp2 when sf_sign = '1' else tmp1;
   shifter_S <= shift_neg when sf_sign = '1' else shift_pos;
   RightShifterComponent: RightShifter_13_by_max_12_comb_uid38
      port map ( R => shifter_out,
                 S => shifter_S,
                 X => shifter_in);
   tmp_ans <= shifter_out(24 downto 14);
--------------------- Packing Stage 2 - Unbiased Rounding ---------------------
   LSB <= shifter_out(14);
   G <= shifter_out(13);
   R <= shifter_out(12);
   S <= '0' when shifter_out(11 downto 0) = 0 else '1';
   round <= G AND (LSB OR R OR S) when NOT((ovf_reg OR ovf_regF) = '1') else '0';
   Output <= '1' & "00000000000" when inf = '1' else "000000000000" when z = '1' else '0' & (tmp_ans + round) when sign = '0' else NOT('0' & (tmp_ans + round))+1;
end architecture;

