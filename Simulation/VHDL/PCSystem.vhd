LIBRARY ieee; 
LIBRARY std; 
USE ieee.std_logic_1164.all; 
USE ieee.std_logic_arith.all; 
USE ieee.std_logic_unsigned.all; 
USE std.textio.all; 
LIBRARY work; 
 
entity PCSystem is 
 
generic(numberOfBits : integer := 24);
port( 
v0a : in std_logic_vector (23 DOWNTO 0);
v0b : in std_logic_vector (23 DOWNTO 0);
v1a : in std_logic_vector (23 DOWNTO 0);
v1b : in std_logic_vector (23 DOWNTO 0);
v2a : in std_logic_vector (23 DOWNTO 0);
v2b : in std_logic_vector (23 DOWNTO 0);
v3a : in std_logic_vector (23 DOWNTO 0);
v3b : in std_logic_vector (23 DOWNTO 0);
v4a : in std_logic_vector (23 DOWNTO 0);
v4b : in std_logic_vector (23 DOWNTO 0);
v5a : in std_logic_vector (23 DOWNTO 0);
v5b : in std_logic_vector (23 DOWNTO 0);
v6a : in std_logic_vector (23 DOWNTO 0);
v6b : in std_logic_vector (23 DOWNTO 0);
v7a : in std_logic_vector (23 DOWNTO 0);
v7b : in std_logic_vector (23 DOWNTO 0);
v8a : in std_logic_vector (23 DOWNTO 0);
v8b : in std_logic_vector (23 DOWNTO 0);
v9a : in std_logic_vector (23 DOWNTO 0);
v9b : in std_logic_vector (23 DOWNTO 0);
v10a : in std_logic_vector (23 DOWNTO 0);
v10b : in std_logic_vector (23 DOWNTO 0);
v11a : in std_logic_vector (23 DOWNTO 0);
v11b : in std_logic_vector (23 DOWNTO 0);
v12a : in std_logic_vector (23 DOWNTO 0);
v12b : in std_logic_vector (23 DOWNTO 0);
v13a : in std_logic_vector (23 DOWNTO 0);
v13b : in std_logic_vector (23 DOWNTO 0);
v14a : in std_logic_vector (23 DOWNTO 0);
v14b : in std_logic_vector (23 DOWNTO 0);
v15a : in std_logic_vector (23 DOWNTO 0);
v15b : in std_logic_vector (23 DOWNTO 0);
v16a : in std_logic_vector (23 DOWNTO 0);
v16b : in std_logic_vector (23 DOWNTO 0);
vout : out std_logic_vector (23 DOWNTO 0)); 
 
end PCSystem; 

architecture rtl of PCSystem is 
 
Signal ProductNode_POSIT0weight : std_logic_vector ( 23 downto 0 ) := "001111100110111111110000";

Signal ProductNode_POSIT0Output_0: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT1weight : std_logic_vector ( 23 downto 0 ) := "001111111111111001000000";

Signal ProductNode_POSIT1Output_1: std_logic_vector (23 downto 0);
Signal SumNode_POSIT0Output_2: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT2weight : std_logic_vector ( 23 downto 0 ) := "001111011110010111001001";

Signal ProductNode_POSIT2Output_3: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT3weight : std_logic_vector ( 23 downto 0 ) := "001111111111111110011010";

Signal ProductNode_POSIT3Output_4: std_logic_vector (23 downto 0);
Signal SumNode_POSIT1Output_5: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT4Output_6: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT5weight : std_logic_vector ( 23 downto 0 ) := "001111110001011100001010";

Signal ProductNode_POSIT5Output_7: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT6weight : std_logic_vector ( 23 downto 0 ) := "001111111111010100011110";

Signal ProductNode_POSIT6Output_8: std_logic_vector (23 downto 0);
Signal SumNode_POSIT2Output_9: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT7Output_10: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT8weight : std_logic_vector ( 23 downto 0 ) := "001111111011000110100010";

Signal ProductNode_POSIT8Output_11: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT9weight : std_logic_vector ( 23 downto 0 ) := "001111111100011100101110";

Signal ProductNode_POSIT9Output_12: std_logic_vector (23 downto 0);
Signal SumNode_POSIT3Output_13: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT10Output_14: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT11weight : std_logic_vector ( 23 downto 0 ) := "001111110110010101000100";

Signal ProductNode_POSIT11Output_15: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT12weight : std_logic_vector ( 23 downto 0 ) := "001111110011011110000101";

Signal ProductNode_POSIT12Output_16: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT13weight : std_logic_vector ( 23 downto 0 ) := "001111111111000100001111";

Signal ProductNode_POSIT13Output_17: std_logic_vector (23 downto 0);
Signal SumNode_POSIT4Output_18: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT14Output_19: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT15weight : std_logic_vector ( 23 downto 0 ) := "001111111110011010101110";

Signal ProductNode_POSIT15Output_20: std_logic_vector (23 downto 0);
Signal SumNode_POSIT5Output_21: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT16Output_22: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT17weight : std_logic_vector ( 23 downto 0 ) := "001111110100111111001010";

Signal ProductNode_POSIT17Output_23: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT18weight : std_logic_vector ( 23 downto 0 ) := "001111111110110000001101";

Signal ProductNode_POSIT18Output_24: std_logic_vector (23 downto 0);
Signal SumNode_POSIT6Output_25: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT19Output_26: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT20weight : std_logic_vector ( 23 downto 0 ) := "001111110001010001111000";

Signal ProductNode_POSIT20Output_27: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT21weight : std_logic_vector ( 23 downto 0 ) := "001111111111010101110000";

Signal ProductNode_POSIT21Output_28: std_logic_vector (23 downto 0);
Signal SumNode_POSIT7Output_29: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT22Output_30: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT23weight : std_logic_vector ( 23 downto 0 ) := "001111110001010011100010";

Signal ProductNode_POSIT23Output_31: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT24weight : std_logic_vector ( 23 downto 0 ) := "001111111111010101100011";

Signal ProductNode_POSIT24Output_32: std_logic_vector (23 downto 0);
Signal SumNode_POSIT8Output_33: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT25Output_34: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT26weight : std_logic_vector ( 23 downto 0 ) := "001111111000000010000011";

Signal ProductNode_POSIT26Output_35: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT27weight : std_logic_vector ( 23 downto 0 ) := "001111111101111110111110";

Signal ProductNode_POSIT27Output_36: std_logic_vector (23 downto 0);
Signal SumNode_POSIT9Output_37: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT28Output_38: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT29weight : std_logic_vector ( 23 downto 0 ) := "001111110101000100111110";

Signal ProductNode_POSIT29Output_39: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT30weight : std_logic_vector ( 23 downto 0 ) := "001111111110101110110000";

Signal ProductNode_POSIT30Output_40: std_logic_vector (23 downto 0);
Signal SumNode_POSIT10Output_41: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT31Output_42: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT32weight : std_logic_vector ( 23 downto 0 ) := "001111111110000111000101";

Signal ProductNode_POSIT32Output_43: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT33weight : std_logic_vector ( 23 downto 0 ) := "001111110111100011101010";

Signal ProductNode_POSIT33Output_44: std_logic_vector (23 downto 0);
Signal SumNode_POSIT11Output_45: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT34Output_46: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT35weight : std_logic_vector ( 23 downto 0 ) := "001111111001110011100010";

Signal ProductNode_POSIT35Output_47: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT36weight : std_logic_vector ( 23 downto 0 ) := "001111111101000110001110";

Signal ProductNode_POSIT36Output_48: std_logic_vector (23 downto 0);
Signal SumNode_POSIT12Output_49: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT37Output_50: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT38weight : std_logic_vector ( 23 downto 0 ) := "001111101110110101110101";

Signal ProductNode_POSIT38Output_51: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT39weight : std_logic_vector ( 23 downto 0 ) := "001111111111100100101000";

Signal ProductNode_POSIT39Output_52: std_logic_vector (23 downto 0);
Signal SumNode_POSIT13Output_53: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT40Output_54: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT41weight : std_logic_vector ( 23 downto 0 ) := "001111111000010000100010";

Signal ProductNode_POSIT41Output_55: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT42weight : std_logic_vector ( 23 downto 0 ) := "001111111101110111101110";

Signal ProductNode_POSIT42Output_56: std_logic_vector (23 downto 0);
Signal SumNode_POSIT14Output_57: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT43Output_58: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT44weight : std_logic_vector ( 23 downto 0 ) := "001111110110000111100100";

Signal ProductNode_POSIT44Output_59: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT45weight : std_logic_vector ( 23 downto 0 ) := "001111111110011110000110";

Signal ProductNode_POSIT45Output_60: std_logic_vector (23 downto 0);
Signal SumNode_POSIT15Output_61: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT46Output_62: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT47weight : std_logic_vector ( 23 downto 0 ) := "001111110111101100011010";

Signal ProductNode_POSIT47Output_63: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT48weight : std_logic_vector ( 23 downto 0 ) := "001111111110000100111001";

Signal ProductNode_POSIT48Output_64: std_logic_vector (23 downto 0);
Signal SumNode_POSIT16Output_65: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT49Output_66: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT50weight : std_logic_vector ( 23 downto 0 ) := "001111010110010000100001";

Signal ProductNode_POSIT50Output_67: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT51weight : std_logic_vector ( 23 downto 0 ) := "001111111111111111100110";

Signal ProductNode_POSIT51Output_68: std_logic_vector (23 downto 0);
Signal SumNode_POSIT17Output_69: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT52Output_70: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT53weight : std_logic_vector ( 23 downto 0 ) := "001111111011100111101101";

Signal ProductNode_POSIT53Output_71: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT54weight : std_logic_vector ( 23 downto 0 ) := "001111101100110000100110";

Signal ProductNode_POSIT54Output_72: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT55weight : std_logic_vector ( 23 downto 0 ) := "001111111111101100111101";

Signal ProductNode_POSIT55Output_73: std_logic_vector (23 downto 0);
Signal SumNode_POSIT18Output_74: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT56weight : std_logic_vector ( 23 downto 0 ) := "001111100010010101011111";

Signal ProductNode_POSIT56Output_75: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT57weight : std_logic_vector ( 23 downto 0 ) := "001111111111111100110101";

Signal ProductNode_POSIT57Output_76: std_logic_vector (23 downto 0);
Signal SumNode_POSIT19Output_77: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT58Output_78: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT59weight : std_logic_vector ( 23 downto 0 ) := "001111101101110100111100";

Signal ProductNode_POSIT59Output_79: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT60weight : std_logic_vector ( 23 downto 0 ) := "001111111111101000101100";

Signal ProductNode_POSIT60Output_80: std_logic_vector (23 downto 0);
Signal SumNode_POSIT20Output_81: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT61Output_82: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT62weight : std_logic_vector ( 23 downto 0 ) := "001111111110011110011000";

Signal ProductNode_POSIT62Output_83: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT63weight : std_logic_vector ( 23 downto 0 ) := "001111110110000110011110";

Signal ProductNode_POSIT63Output_84: std_logic_vector (23 downto 0);
Signal SumNode_POSIT21Output_85: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT64Output_86: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT65weight : std_logic_vector ( 23 downto 0 ) := "001111101000101011101101";

Signal ProductNode_POSIT65Output_87: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT66weight : std_logic_vector ( 23 downto 0 ) := "001111111111110110101000";

Signal ProductNode_POSIT66Output_88: std_logic_vector (23 downto 0);
Signal SumNode_POSIT22Output_89: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT67Output_90: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT68weight : std_logic_vector ( 23 downto 0 ) := "001111110110110000011100";

Signal ProductNode_POSIT68Output_91: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT69weight : std_logic_vector ( 23 downto 0 ) := "001111111110010011111000";

Signal ProductNode_POSIT69Output_92: std_logic_vector (23 downto 0);
Signal SumNode_POSIT23Output_93: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT70Output_94: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT71weight : std_logic_vector ( 23 downto 0 ) := "001111110101001010011100";

Signal ProductNode_POSIT71Output_95: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT72weight : std_logic_vector ( 23 downto 0 ) := "001111111110101101011000";

Signal ProductNode_POSIT72Output_96: std_logic_vector (23 downto 0);
Signal SumNode_POSIT24Output_97: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT73Output_98: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT74weight : std_logic_vector ( 23 downto 0 ) := "001111110100001000100010";

Signal ProductNode_POSIT74Output_99: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT75weight : std_logic_vector ( 23 downto 0 ) := "001111111110111101110111";

Signal ProductNode_POSIT75Output_100: std_logic_vector (23 downto 0);
Signal SumNode_POSIT25Output_101: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT76Output_102: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT77weight : std_logic_vector ( 23 downto 0 ) := "001111101111000010001010";

Signal ProductNode_POSIT77Output_103: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT78weight : std_logic_vector ( 23 downto 0 ) := "001111111111100011110111";

Signal ProductNode_POSIT78Output_104: std_logic_vector (23 downto 0);
Signal SumNode_POSIT26Output_105: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT79Output_106: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT80weight : std_logic_vector ( 23 downto 0 ) := "001111101110101110101110";

Signal ProductNode_POSIT80Output_107: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT81weight : std_logic_vector ( 23 downto 0 ) := "001111111111100101000101";

Signal ProductNode_POSIT81Output_108: std_logic_vector (23 downto 0);
Signal SumNode_POSIT27Output_109: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT82Output_110: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT83weight : std_logic_vector ( 23 downto 0 ) := "001111110101101101000101";

Signal ProductNode_POSIT83Output_111: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT84weight : std_logic_vector ( 23 downto 0 ) := "001111111110100100101110";

Signal ProductNode_POSIT84Output_112: std_logic_vector (23 downto 0);
Signal SumNode_POSIT28Output_113: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT85Output_114: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT86weight : std_logic_vector ( 23 downto 0 ) := "001111110110010001110101";

Signal ProductNode_POSIT86Output_115: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT87weight : std_logic_vector ( 23 downto 0 ) := "001111111110011011100010";

Signal ProductNode_POSIT87Output_116: std_logic_vector (23 downto 0);
Signal SumNode_POSIT29Output_117: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT88Output_118: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT89weight : std_logic_vector ( 23 downto 0 ) := "001111101111101101101100";

Signal ProductNode_POSIT89Output_119: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT90weight : std_logic_vector ( 23 downto 0 ) := "001111111111100001001001";

Signal ProductNode_POSIT90Output_120: std_logic_vector (23 downto 0);
Signal SumNode_POSIT30Output_121: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT91Output_122: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT92weight : std_logic_vector ( 23 downto 0 ) := "001111110110001010000111";

Signal ProductNode_POSIT92Output_123: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT93weight : std_logic_vector ( 23 downto 0 ) := "001111111110011101011110";

Signal ProductNode_POSIT93Output_124: std_logic_vector (23 downto 0);
Signal SumNode_POSIT31Output_125: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT94Output_126: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT95weight : std_logic_vector ( 23 downto 0 ) := "001111110101001111001101";

Signal ProductNode_POSIT95Output_127: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT96weight : std_logic_vector ( 23 downto 0 ) := "001111111110101100001100";

Signal ProductNode_POSIT96Output_128: std_logic_vector (23 downto 0);
Signal SumNode_POSIT32Output_129: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT97Output_130: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT98weight : std_logic_vector ( 23 downto 0 ) := "001111111001110111110010";

Signal ProductNode_POSIT98Output_131: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT99weight : std_logic_vector ( 23 downto 0 ) := "001111111101000100000110";

Signal ProductNode_POSIT99Output_132: std_logic_vector (23 downto 0);
Signal SumNode_POSIT33Output_133: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT100Output_134: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT101Output_135: std_logic_vector (23 downto 0);
Signal ProductNode_POSIT102weight : std_logic_vector ( 23 downto 0 ) := "001111111100001100001001";

Signal ProductNode_POSIT102Output_136: std_logic_vector (23 downto 0);
Signal SumNode_POSIT34Output_137: std_logic_vector (23 downto 0);

 
begin 
ProductNode_POSIT0: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT0weight,v16b,ProductNode_POSIT0Output_0);

ProductNode_POSIT1: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT1weight,v16a,ProductNode_POSIT1Output_1);

SumNode_POSIT0: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT1Output_1,ProductNode_POSIT0Output_0,SumNode_POSIT0Output_2);

ProductNode_POSIT2: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT2weight,v15b,ProductNode_POSIT2Output_3);

ProductNode_POSIT3: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT3weight,v15a,ProductNode_POSIT3Output_4);

SumNode_POSIT1: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT3Output_4,ProductNode_POSIT2Output_3,SumNode_POSIT1Output_5);

ProductNode_POSIT4: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT1Output_5,SumNode_POSIT0Output_2,ProductNode_POSIT4Output_6);

ProductNode_POSIT5: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT5weight,v14b,ProductNode_POSIT5Output_7);

ProductNode_POSIT6: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT6weight,v14a,ProductNode_POSIT6Output_8);

SumNode_POSIT2: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT6Output_8,ProductNode_POSIT5Output_7,SumNode_POSIT2Output_9);

ProductNode_POSIT7: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT2Output_9,ProductNode_POSIT4Output_6,ProductNode_POSIT7Output_10);

ProductNode_POSIT8: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT8weight,v12b,ProductNode_POSIT8Output_11);

ProductNode_POSIT9: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT9weight,v12a,ProductNode_POSIT9Output_12);

SumNode_POSIT3: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT9Output_12,ProductNode_POSIT8Output_11,SumNode_POSIT3Output_13);

ProductNode_POSIT10: entity work.PositMult_24_7_comb_uid2(arch)
port map(v13b,SumNode_POSIT3Output_13,ProductNode_POSIT10Output_14);

ProductNode_POSIT11: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT11weight,ProductNode_POSIT10Output_14,ProductNode_POSIT11Output_15);

ProductNode_POSIT12: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT12weight,v12b,ProductNode_POSIT12Output_16);

ProductNode_POSIT13: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT13weight,v12a,ProductNode_POSIT13Output_17);

SumNode_POSIT4: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT13Output_17,ProductNode_POSIT12Output_16,SumNode_POSIT4Output_18);

ProductNode_POSIT14: entity work.PositMult_24_7_comb_uid2(arch)
port map(v13a,SumNode_POSIT4Output_18,ProductNode_POSIT14Output_19);

ProductNode_POSIT15: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT15weight,ProductNode_POSIT14Output_19,ProductNode_POSIT15Output_20);

SumNode_POSIT5: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT15Output_20,ProductNode_POSIT11Output_15,SumNode_POSIT5Output_21);

ProductNode_POSIT16: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT5Output_21,ProductNode_POSIT7Output_10,ProductNode_POSIT16Output_22);

ProductNode_POSIT17: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT17weight,v11b,ProductNode_POSIT17Output_23);

ProductNode_POSIT18: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT18weight,v11a,ProductNode_POSIT18Output_24);

SumNode_POSIT6: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT18Output_24,ProductNode_POSIT17Output_23,SumNode_POSIT6Output_25);

ProductNode_POSIT19: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT6Output_25,ProductNode_POSIT16Output_22,ProductNode_POSIT19Output_26);

ProductNode_POSIT20: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT20weight,v10b,ProductNode_POSIT20Output_27);

ProductNode_POSIT21: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT21weight,v10a,ProductNode_POSIT21Output_28);

SumNode_POSIT7: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT21Output_28,ProductNode_POSIT20Output_27,SumNode_POSIT7Output_29);

ProductNode_POSIT22: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT7Output_29,ProductNode_POSIT19Output_26,ProductNode_POSIT22Output_30);

ProductNode_POSIT23: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT23weight,v9b,ProductNode_POSIT23Output_31);

ProductNode_POSIT24: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT24weight,v9a,ProductNode_POSIT24Output_32);

SumNode_POSIT8: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT24Output_32,ProductNode_POSIT23Output_31,SumNode_POSIT8Output_33);

ProductNode_POSIT25: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT8Output_33,ProductNode_POSIT22Output_30,ProductNode_POSIT25Output_34);

ProductNode_POSIT26: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT26weight,v8b,ProductNode_POSIT26Output_35);

ProductNode_POSIT27: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT27weight,v8a,ProductNode_POSIT27Output_36);

SumNode_POSIT9: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT27Output_36,ProductNode_POSIT26Output_35,SumNode_POSIT9Output_37);

ProductNode_POSIT28: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT9Output_37,ProductNode_POSIT25Output_34,ProductNode_POSIT28Output_38);

ProductNode_POSIT29: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT29weight,v7b,ProductNode_POSIT29Output_39);

ProductNode_POSIT30: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT30weight,v7a,ProductNode_POSIT30Output_40);

SumNode_POSIT10: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT30Output_40,ProductNode_POSIT29Output_39,SumNode_POSIT10Output_41);

ProductNode_POSIT31: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT10Output_41,ProductNode_POSIT28Output_38,ProductNode_POSIT31Output_42);

ProductNode_POSIT32: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT32weight,v6a,ProductNode_POSIT32Output_43);

ProductNode_POSIT33: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT33weight,v6b,ProductNode_POSIT33Output_44);

SumNode_POSIT11: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT33Output_44,ProductNode_POSIT32Output_43,SumNode_POSIT11Output_45);

ProductNode_POSIT34: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT11Output_45,ProductNode_POSIT31Output_42,ProductNode_POSIT34Output_46);

ProductNode_POSIT35: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT35weight,v5b,ProductNode_POSIT35Output_47);

ProductNode_POSIT36: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT36weight,v5a,ProductNode_POSIT36Output_48);

SumNode_POSIT12: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT36Output_48,ProductNode_POSIT35Output_47,SumNode_POSIT12Output_49);

ProductNode_POSIT37: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT12Output_49,ProductNode_POSIT34Output_46,ProductNode_POSIT37Output_50);

ProductNode_POSIT38: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT38weight,v4b,ProductNode_POSIT38Output_51);

ProductNode_POSIT39: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT39weight,v4a,ProductNode_POSIT39Output_52);

SumNode_POSIT13: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT39Output_52,ProductNode_POSIT38Output_51,SumNode_POSIT13Output_53);

ProductNode_POSIT40: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT13Output_53,ProductNode_POSIT37Output_50,ProductNode_POSIT40Output_54);

ProductNode_POSIT41: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT41weight,v3b,ProductNode_POSIT41Output_55);

ProductNode_POSIT42: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT42weight,v3a,ProductNode_POSIT42Output_56);

SumNode_POSIT14: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT42Output_56,ProductNode_POSIT41Output_55,SumNode_POSIT14Output_57);

ProductNode_POSIT43: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT14Output_57,ProductNode_POSIT40Output_54,ProductNode_POSIT43Output_58);

ProductNode_POSIT44: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT44weight,v2b,ProductNode_POSIT44Output_59);

ProductNode_POSIT45: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT45weight,v2a,ProductNode_POSIT45Output_60);

SumNode_POSIT15: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT45Output_60,ProductNode_POSIT44Output_59,SumNode_POSIT15Output_61);

ProductNode_POSIT46: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT15Output_61,ProductNode_POSIT43Output_58,ProductNode_POSIT46Output_62);

ProductNode_POSIT47: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT47weight,v1b,ProductNode_POSIT47Output_63);

ProductNode_POSIT48: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT48weight,v1a,ProductNode_POSIT48Output_64);

SumNode_POSIT16: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT48Output_64,ProductNode_POSIT47Output_63,SumNode_POSIT16Output_65);

ProductNode_POSIT49: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT16Output_65,ProductNode_POSIT46Output_62,ProductNode_POSIT49Output_66);

ProductNode_POSIT50: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT50weight,v0b,ProductNode_POSIT50Output_67);

ProductNode_POSIT51: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT51weight,v0a,ProductNode_POSIT51Output_68);

SumNode_POSIT17: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT51Output_68,ProductNode_POSIT50Output_67,SumNode_POSIT17Output_69);

ProductNode_POSIT52: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT17Output_69,ProductNode_POSIT49Output_66,ProductNode_POSIT52Output_70);

ProductNode_POSIT53: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT53weight,ProductNode_POSIT52Output_70,ProductNode_POSIT53Output_71);

ProductNode_POSIT54: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT54weight,v16b,ProductNode_POSIT54Output_72);

ProductNode_POSIT55: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT55weight,v16a,ProductNode_POSIT55Output_73);

SumNode_POSIT18: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT55Output_73,ProductNode_POSIT54Output_72,SumNode_POSIT18Output_74);

ProductNode_POSIT56: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT56weight,v15b,ProductNode_POSIT56Output_75);

ProductNode_POSIT57: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT57weight,v15a,ProductNode_POSIT57Output_76);

SumNode_POSIT19: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT57Output_76,ProductNode_POSIT56Output_75,SumNode_POSIT19Output_77);

ProductNode_POSIT58: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT19Output_77,SumNode_POSIT18Output_74,ProductNode_POSIT58Output_78);

ProductNode_POSIT59: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT59weight,v14b,ProductNode_POSIT59Output_79);

ProductNode_POSIT60: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT60weight,v14a,ProductNode_POSIT60Output_80);

SumNode_POSIT20: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT60Output_80,ProductNode_POSIT59Output_79,SumNode_POSIT20Output_81);

ProductNode_POSIT61: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT20Output_81,ProductNode_POSIT58Output_78,ProductNode_POSIT61Output_82);

ProductNode_POSIT62: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT62weight,v13a,ProductNode_POSIT62Output_83);

ProductNode_POSIT63: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT63weight,v13b,ProductNode_POSIT63Output_84);

SumNode_POSIT21: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT63Output_84,ProductNode_POSIT62Output_83,SumNode_POSIT21Output_85);

ProductNode_POSIT64: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT21Output_85,ProductNode_POSIT61Output_82,ProductNode_POSIT64Output_86);

ProductNode_POSIT65: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT65weight,v12b,ProductNode_POSIT65Output_87);

ProductNode_POSIT66: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT66weight,v12a,ProductNode_POSIT66Output_88);

SumNode_POSIT22: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT66Output_88,ProductNode_POSIT65Output_87,SumNode_POSIT22Output_89);

ProductNode_POSIT67: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT22Output_89,ProductNode_POSIT64Output_86,ProductNode_POSIT67Output_90);

ProductNode_POSIT68: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT68weight,v11b,ProductNode_POSIT68Output_91);

ProductNode_POSIT69: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT69weight,v11a,ProductNode_POSIT69Output_92);

SumNode_POSIT23: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT69Output_92,ProductNode_POSIT68Output_91,SumNode_POSIT23Output_93);

ProductNode_POSIT70: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT23Output_93,ProductNode_POSIT67Output_90,ProductNode_POSIT70Output_94);

ProductNode_POSIT71: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT71weight,v10b,ProductNode_POSIT71Output_95);

ProductNode_POSIT72: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT72weight,v10a,ProductNode_POSIT72Output_96);

SumNode_POSIT24: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT72Output_96,ProductNode_POSIT71Output_95,SumNode_POSIT24Output_97);

ProductNode_POSIT73: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT24Output_97,ProductNode_POSIT70Output_94,ProductNode_POSIT73Output_98);

ProductNode_POSIT74: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT74weight,v9b,ProductNode_POSIT74Output_99);

ProductNode_POSIT75: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT75weight,v9a,ProductNode_POSIT75Output_100);

SumNode_POSIT25: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT75Output_100,ProductNode_POSIT74Output_99,SumNode_POSIT25Output_101);

ProductNode_POSIT76: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT25Output_101,ProductNode_POSIT73Output_98,ProductNode_POSIT76Output_102);

ProductNode_POSIT77: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT77weight,v8b,ProductNode_POSIT77Output_103);

ProductNode_POSIT78: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT78weight,v8a,ProductNode_POSIT78Output_104);

SumNode_POSIT26: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT78Output_104,ProductNode_POSIT77Output_103,SumNode_POSIT26Output_105);

ProductNode_POSIT79: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT26Output_105,ProductNode_POSIT76Output_102,ProductNode_POSIT79Output_106);

ProductNode_POSIT80: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT80weight,v7b,ProductNode_POSIT80Output_107);

ProductNode_POSIT81: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT81weight,v7a,ProductNode_POSIT81Output_108);

SumNode_POSIT27: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT81Output_108,ProductNode_POSIT80Output_107,SumNode_POSIT27Output_109);

ProductNode_POSIT82: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT27Output_109,ProductNode_POSIT79Output_106,ProductNode_POSIT82Output_110);

ProductNode_POSIT83: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT83weight,v6b,ProductNode_POSIT83Output_111);

ProductNode_POSIT84: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT84weight,v6a,ProductNode_POSIT84Output_112);

SumNode_POSIT28: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT84Output_112,ProductNode_POSIT83Output_111,SumNode_POSIT28Output_113);

ProductNode_POSIT85: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT28Output_113,ProductNode_POSIT82Output_110,ProductNode_POSIT85Output_114);

ProductNode_POSIT86: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT86weight,v5b,ProductNode_POSIT86Output_115);

ProductNode_POSIT87: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT87weight,v5a,ProductNode_POSIT87Output_116);

SumNode_POSIT29: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT87Output_116,ProductNode_POSIT86Output_115,SumNode_POSIT29Output_117);

ProductNode_POSIT88: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT29Output_117,ProductNode_POSIT85Output_114,ProductNode_POSIT88Output_118);

ProductNode_POSIT89: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT89weight,v4b,ProductNode_POSIT89Output_119);

ProductNode_POSIT90: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT90weight,v4a,ProductNode_POSIT90Output_120);

SumNode_POSIT30: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT90Output_120,ProductNode_POSIT89Output_119,SumNode_POSIT30Output_121);

ProductNode_POSIT91: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT30Output_121,ProductNode_POSIT88Output_118,ProductNode_POSIT91Output_122);

ProductNode_POSIT92: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT92weight,v3b,ProductNode_POSIT92Output_123);

ProductNode_POSIT93: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT93weight,v3a,ProductNode_POSIT93Output_124);

SumNode_POSIT31: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT93Output_124,ProductNode_POSIT92Output_123,SumNode_POSIT31Output_125);

ProductNode_POSIT94: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT31Output_125,ProductNode_POSIT91Output_122,ProductNode_POSIT94Output_126);

ProductNode_POSIT95: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT95weight,v2b,ProductNode_POSIT95Output_127);

ProductNode_POSIT96: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT96weight,v2a,ProductNode_POSIT96Output_128);

SumNode_POSIT32: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT96Output_128,ProductNode_POSIT95Output_127,SumNode_POSIT32Output_129);

ProductNode_POSIT97: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT32Output_129,ProductNode_POSIT94Output_126,ProductNode_POSIT97Output_130);

ProductNode_POSIT98: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT98weight,v1b,ProductNode_POSIT98Output_131);

ProductNode_POSIT99: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT99weight,v1a,ProductNode_POSIT99Output_132);

SumNode_POSIT33: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT99Output_132,ProductNode_POSIT98Output_131,SumNode_POSIT33Output_133);

ProductNode_POSIT100: entity work.PositMult_24_7_comb_uid2(arch)
port map(SumNode_POSIT33Output_133,ProductNode_POSIT97Output_130,ProductNode_POSIT100Output_134);

ProductNode_POSIT101: entity work.PositMult_24_7_comb_uid2(arch)
port map(v0b,ProductNode_POSIT100Output_134,ProductNode_POSIT101Output_135);

ProductNode_POSIT102: entity work.PositMult_24_7_comb_uid2(arch)
port map(ProductNode_POSIT102weight,ProductNode_POSIT101Output_135,ProductNode_POSIT102Output_136);

SumNode_POSIT34: entity work.PositAdd_24_7_F0_uid2(arch)
port map(ProductNode_POSIT102Output_136,ProductNode_POSIT53Output_71,SumNode_POSIT34Output_137);

vout <= SumNode_POSIT34Output_137;
 
end architecture;
