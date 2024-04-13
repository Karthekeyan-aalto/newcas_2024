----Created by Karthekeyan Periasamy------
-----------Edited on April 26 08:51-----------

LIBRARY ieee;
USE ieee.std_logic_1164.all;
USE ieee.std_logic_arith.all;
USE ieee.std_logic_unsigned.all;

--LIBRARY UNISIM;
--USE UNISIM.vcomponents.all;


ENTITY PCSystem_MSNBC_SPN_Float_SoC_er_6 IS

    GENERIC (MantissaBits :INTEGER := 25; ExponentBits :INTEGER := 7; numberOfBits :INTEGER := 32; FlopocoBits :INTEGER := 2);
    PORT (clk  : IN std_logic;
          rst  : IN std_logic;
          enable: IN std_logic;
          v0a : in std_logic;
          v0b : in std_logic;
          v1a : in std_logic;
          v1b : in std_logic;
          v2a : in std_logic;
          v2b : in std_logic;
          v3a : in std_logic;
          v3b : in std_logic;
          v4a : in std_logic;
          v4b : in std_logic;
          v5a : in std_logic;
          v5b : in std_logic;
          v6a : in std_logic;
          v6b : in std_logic;
          v7a : in std_logic;
          v7b : in std_logic;
          v8a : in std_logic;
          v8b : in std_logic;
          v9a : in std_logic;
          v9b : in std_logic;
          v10a : in std_logic;
          v10b : in std_logic;
          v11a : in std_logic;
          v11b : in std_logic;
          v12a : in std_logic;
          v12b : in std_logic;
          v13a : in std_logic;
          v13b : in std_logic;
          v14a : in std_logic;
          v14b : in std_logic;
          v15a : in std_logic;
          v15b : in std_logic;
          v16a : in std_logic;
          v16b : in std_logic;
          --lastWeight :OUT std_logic_vector (numberOfBits-1 DOWNTO 0);
          --lastMultiplierOutput :OUT std_logic_vector (FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
          clk_out :OUT std_logic;
          --topNodeOutput :OUT std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
          vout   :OUT std_logic_vector (numberOfBits-1 DOWNTO 0));

END PCSystem_MSNBC_SPN_Float_SoC_er_6;


ARCHITECTURE rtl of PCSystem_MSNBC_SPN_Float_SoC_er_6 IS
    
    SIGNAL sbDFFv0aInput  :std_logic;
    SIGNAL sbDFFv0aOutput :std_logic;

    SIGNAL sbDFFv0bInput  :std_logic;
    SIGNAL sbDFFv0bOutput :std_logic;
    
    SIGNAL sbDFFv1aInput  :std_logic;
    SIGNAL sbDFFv1aOutput :std_logic;
    
    SIGNAL sbDFFv1bInput  :std_logic;
    SIGNAL sbDFFv1bOutput :std_logic;
    
    SIGNAL sbDFFv2aInput  :std_logic;
    SIGNAL sbDFFv2aOutput :std_logic;
    
    SIGNAL sbDFFv2bInput  :std_logic;
    SIGNAL sbDFFv2bOutput :std_logic;
    
    SIGNAL sbDFFv3aInput  :std_logic;
    SIGNAL sbDFFv3aOutput :std_logic;
    
    SIGNAL sbDFFv3bInput  :std_logic;
    SIGNAL sbDFFv3bOutput :std_logic;
    
    SIGNAL sbDFFv4aInput  :std_logic;
    SIGNAL sbDFFv4aOutput :std_logic;
    
    SIGNAL sbDFFv4bInput  :std_logic;
    SIGNAL sbDFFv4bOutput :std_logic;
    
    SIGNAL sbDFFv5aInput  :std_logic;
    SIGNAL sbDFFv5aOutput :std_logic;

    SIGNAL sbDFFv5bInput  :std_logic;
    SIGNAL sbDFFv5bOutput :std_logic;
    
    SIGNAL sbDFFv6aInput  :std_logic;
    SIGNAL sbDFFv6aOutput :std_logic;
    
    SIGNAL sbDFFv6bInput  :std_logic;
    SIGNAL sbDFFv6bOutput :std_logic;
    
    SIGNAL sbDFFv7aInput  :std_logic;
    SIGNAL sbDFFv7aOutput :std_logic;
    
    SIGNAL sbDFFv7bInput  :std_logic;
    SIGNAL sbDFFv7bOutput :std_logic;
    
    SIGNAL sbDFFv8aInput  :std_logic;
    SIGNAL sbDFFv8aOutput :std_logic;
   
    SIGNAL sbDFFv8bInput  :std_logic;
    SIGNAL sbDFFv8bOutput :std_logic;

    SIGNAL sbDFFv9aInput  :std_logic;
    SIGNAL sbDFFv9aOutput :std_logic;
   
    SIGNAL sbDFFv9bInput  :std_logic;
    SIGNAL sbDFFv9bOutput :std_logic;

    SIGNAL sbDFFv10aInput  :std_logic;
    SIGNAL sbDFFv10aOutput :std_logic;
    
    SIGNAL sbDFFv10bInput  :std_logic;
    SIGNAL sbDFFv10bOutput :std_logic;
    
    SIGNAL sbDFFv11aInput  :std_logic;
    SIGNAL sbDFFv11aOutput :std_logic;
   
    SIGNAL sbDFFv11bInput  :std_logic;
    SIGNAL sbDFFv11bOutput :std_logic;

    SIGNAL sbDFFv12aInput  :std_logic;
    SIGNAL sbDFFv12aOutput :std_logic;
    
    SIGNAL sbDFFv12bInput  :std_logic;
    SIGNAL sbDFFv12bOutput :std_logic;
    
    SIGNAL sbDFFv13aInput  :std_logic;
    SIGNAL sbDFFv13aOutput :std_logic;
    
    SIGNAL sbDFFv13bInput  :std_logic;
    SIGNAL sbDFFv13bOutput :std_logic;

    
    SIGNAL sbDFFv14aInput  :std_logic;
    SIGNAL sbDFFv14aOutput :std_logic;
    
    SIGNAL sbDFFv14bInput  :std_logic;
    SIGNAL sbDFFv14bOutput :std_logic;
    
    SIGNAL sbDFFv15aInput  :std_logic;
    SIGNAL sbDFFv15aOutput :std_logic;
    
    SIGNAL sbDFFv15bInput  :std_logic;
    SIGNAL sbDFFv15bOutput :std_logic;
    
    SIGNAL sbDFFv16aInput  :std_logic;
    SIGNAL sbDFFv16aOutput :std_logic;
    
    SIGNAL sbDFFv16bInput  :std_logic;
    SIGNAL sbDFFv16bOutput :std_logic;
   
    
    SIGNAL pcLUTv0aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v0aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv0bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v0bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv1aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v1aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv1bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v1bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    
    SIGNAL pcLUTv2aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v2aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv2bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v2bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    
    SIGNAL pcLUTv3aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v3aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv3bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v3bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv4aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v4aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv4bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v4bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv5aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v5aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv5bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v5bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    
    SIGNAL pcLUTv6aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v6aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv6bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v6bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv7aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v7aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv7bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v7bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);


    SIGNAL pcLUTv8aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v8aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv8bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v8bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    
    SIGNAL pcLUTv9aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v9aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv9bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v9bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    
    SIGNAL pcLUTv10aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v10aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv10bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v10bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv11aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v11aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv11bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v11bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv12aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v12aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv12bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v12bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv13aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v13aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv13bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v13bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv14aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v14aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv14bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v14bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL pcLUTv15aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v15aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv15bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v15bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv16aOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v16aConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL pcLUTv16bOutput       :std_logic_vector(numberOfBits-1 DOWNTO 0);
    SIGNAL v16bConverterOutput   :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    
    SIGNAL mbDFFv0aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv0aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL mbDFFv0bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv0bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv1aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv1aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv1bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv1bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL mbDFFv2aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv2aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv2bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv2bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv3aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv3aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv3bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv3bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    
    SIGNAL mbDFFv4aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv4aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv4bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv4bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv5aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv5aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL mbDFFv5bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv5bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv6aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv6aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv6bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv6bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv7aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv7aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv7bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv7bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv8aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv8aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
   
    SIGNAL mbDFFv8bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv8bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL mbDFFv9aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv9aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
   
    SIGNAL mbDFFv9bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv9bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL mbDFFv10aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv10aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv10bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv10bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);    
    
    SIGNAL mbDFFv11aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv11aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
   
    SIGNAL mbDFFv11bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv11bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL mbDFFv12aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv12aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv12bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv12bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv13aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv13aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv13bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv13bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv14aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv14aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv14bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv14bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);

    SIGNAL mbDFFv15aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv15aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv15bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv15bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv16aInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv16aOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    
    SIGNAL mbDFFv16bInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFv16bOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
        
    SIGNAL mbDFFvoutInput  :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
    SIGNAL mbDFFvoutOutput :std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);
       
    SIGNAL voutConverterOutput :std_logic_vector(numberOfBits-1 DOWNTO 0);    
    SIGNAL mbDFFvoutStage2Output :std_logic_vector(numberOfBits-1 DOWNTO 0);

    SIGNAL pcSystemOutput: std_logic_vector(FlopocoBits+(MantissaBits-1)+(ExponentBits) DOWNTO 0);


    SIGNAL enableInput  :std_logic;
    SIGNAL enableOutput :std_logic; 
 
BEGIN
    PROCESS(clk,rst)
    BEGIN
        IF rst = '1' THEN
            --reset the
            enableInput  <= '0';
            sbDFFv0aInput        <= '0';
            sbDFFv0bInput        <= '0';
            sbDFFv1aInput        <= '0'; 
            sbDFFv1bInput        <= '0'; 
            sbDFFv2aInput        <= '0';
            sbDFFv2bInput        <= '0';
            sbDFFv3aInput        <= '0';
            
            sbDFFv3bInput        <= '0';
            sbDFFv4aInput        <= '0';
            sbDFFv4bInput        <= '0'; 
            sbDFFv5aInput        <= '0'; 
            sbDFFv5bInput        <= '0';
            sbDFFv6aInput        <= '0';
            sbDFFv6bInput        <= '0';
            
            sbDFFv7aInput        <= '0';
            sbDFFv7bInput        <= '0';
            sbDFFv8aInput        <= '0'; 
            sbDFFv8bInput        <= '0'; 
            sbDFFv9aInput        <= '0';
            sbDFFv9bInput        <= '0';
            sbDFFv10aInput       <= '0';
            
            sbDFFv10bInput        <= '0';
            sbDFFv11aInput        <= '0';
            sbDFFv11bInput        <= '0'; 
            sbDFFv12aInput        <= '0'; 
            sbDFFv12bInput        <= '0';
            sbDFFv13aInput        <= '0';
            sbDFFv13bInput        <= '0';
            
            sbDFFv14aInput        <= '0';
            sbDFFv14bInput        <= '0';
            sbDFFv15aInput        <= '0'; 
            sbDFFv15bInput        <= '0';
            sbDFFv16aInput        <= '0'; 
            sbDFFv16bInput        <= '0';
            
            ---stage 2 
            mbDFFv0aInput       <= (others => '0');
            mbDFFv0bInput       <= (others => '0');
            mbDFFv1aInput       <= (others => '0'); 
            mbDFFv1bInput       <= (others => '0'); 
            mbDFFv2aInput       <= (others => '0');
            mbDFFv2bInput       <= (others => '0');
            mbDFFv3aInput       <= (others => '0');
            
            mbDFFv3bInput       <= (others => '0');
            mbDFFv4aInput       <= (others => '0');
            mbDFFv4bInput       <= (others => '0'); 
            mbDFFv5aInput       <= (others => '0'); 
            mbDFFv5bInput       <= (others => '0'); 
            mbDFFv6aInput       <= (others => '0');
            mbDFFv6bInput       <= (others => '0');
            
            mbDFFv7aInput       <= (others => '0');
            mbDFFv7bInput       <= (others => '0');
            mbDFFv8aInput       <= (others => '0'); 
            mbDFFv8bInput       <= (others => '0'); 
            mbDFFv9aInput       <= (others => '0');
            mbDFFv9bInput       <= (others => '0');
            mbDFFv10aInput      <= (others => '0');
            
            mbDFFv10bInput       <= (others => '0');
            mbDFFv11aInput       <= (others => '0');
            mbDFFv11bInput       <= (others => '0');
            mbDFFv12aInput       <= (others => '0');
            mbDFFv12bInput       <= (others => '0');
            mbDFFv13aInput       <= (others => '0');
            mbDFFv13bInput       <= (others => '0');
            
            mbDFFv14aInput       <= (others => '0');
            mbDFFv14bInput       <= (others => '0');
            mbDFFv15aInput       <= (others => '0');
            mbDFFv15bInput       <= (others => '0');
            mbDFFv16aInput       <= (others => '0');
            mbDFFv16bInput       <= (others => '0');
            
            mbDFFvoutInput       <= (others => '0');
            
        ELSIF rising_edge(clk) and rst = '0' THEN

            ---stage 1 
            enableInput          <= enable;
            sbDFFv0aInput        <= v0a;
            sbDFFv0bInput        <= v0b;
            sbDFFv1aInput        <= v1a; 
            sbDFFv1bInput        <= v1b; 
            sbDFFv2aInput        <= v2a;
            sbDFFv2bInput        <= v2b;
            sbDFFv3aInput        <= v3a;

            sbDFFv3bInput        <= v3b;
            sbDFFv4aInput        <= v4a;
            sbDFFv4bInput        <= v4b; 
            sbDFFv5aInput        <= v5a; 
            sbDFFv5bInput        <= v5b;
            sbDFFv6aInput        <= v6a;
            sbDFFv6bInput        <= v6b;
            
            sbDFFv7aInput        <= v7a;
            sbDFFv7bInput        <= v7b;
            sbDFFv8aInput        <= v8a; 
            sbDFFv8bInput        <= v8b; 
            sbDFFv9aInput        <= v9a;
            sbDFFv9bInput        <= v9b;
            sbDFFv10aInput       <= v10a;
            
            sbDFFv10bInput        <= v10b;
            sbDFFv11aInput        <= v11a;
            sbDFFv11bInput        <= v11b; 
            sbDFFv12aInput        <= v12a; 
            sbDFFv12bInput        <= v12b;
            sbDFFv13aInput        <= v13a;
            sbDFFv13bInput        <= v13b;
            
            sbDFFv14aInput        <= v14a;
            sbDFFv14bInput        <= v14b;
            sbDFFv15aInput        <= v15a; 
            sbDFFv15bInput        <= v15b;
            sbDFFv16aInput        <= v16a; 
            sbDFFv16bInput        <= v16b;
            mbDFFvoutInput        <= pcSystemOutput;


            
            
        END IF;
    END PROCESS;
    
    ---Make a sbRightSHR instance to enable the clock of the multiplier

    sbRightSHR0 : ENTITY work.SBRightSHR(rtl)
    generic map (2)
    port map (clk, rst, enableInput, enableOutput);

    
    --stage 1
    
    sb_d_ffv0a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv0aInput, sbDFFv0aOutput);

    sb_d_ffv0b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv0bInput, sbDFFv0bOutput);
    
    sb_d_ffv1a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv1aInput, sbDFFv1aOutput);

    sb_d_ffv1b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv1bInput, sbDFFv1bOutput);


    sb_d_ffv2a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv2aInput, sbDFFv2aOutput);

    
    sb_d_ffv2b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv2bInput, sbDFFv2bOutput);
    
    sb_d_ffv3a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv3aInput, sbDFFv3aOutput);

    
    sb_d_ffv3b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv3bInput, sbDFFv3bOutput);


    sb_d_ffv4a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv4aInput, sbDFFv4aOutput);

    
    sb_d_ffv4b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv4bInput, sbDFFv4bOutput);


    sb_d_ffv5a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv5aInput, sbDFFv5aOutput);

    
    sb_d_ffv5b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv5bInput, sbDFFv5bOutput);
    
    
    sb_d_ffv6a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv6aInput, sbDFFv6aOutput);

    sb_d_ffv6b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv6bInput, sbDFFv6bOutput);
    
    sb_d_ffv7a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv7aInput, sbDFFv7aOutput);

    sb_d_ffv7b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv7bInput, sbDFFv7bOutput);


    sb_d_ffv8a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv8aInput, sbDFFv8aOutput);

    
    sb_d_ffv8b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv8bInput, sbDFFv8bOutput);
    
    sb_d_ffv9a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv9aInput, sbDFFv9aOutput);

    
    sb_d_ffv9b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv9bInput, sbDFFv9bOutput);


    sb_d_ffv10a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv10aInput, sbDFFv10aOutput);

    
    sb_d_ffv10b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv10bInput, sbDFFv10bOutput);


    sb_d_ffv11a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv11aInput, sbDFFv11aOutput);

    
    sb_d_ffv11b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv11bInput, sbDFFv11bOutput);
    
    sb_d_ffv12a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv12aInput, sbDFFv12aOutput);

    
    sb_d_ffv12b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv12bInput, sbDFFv12bOutput);


    sb_d_ffv13a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv13aInput, sbDFFv13aOutput);

    
    sb_d_ffv13b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv13bInput, sbDFFv13bOutput);
    
    sb_d_ffv14a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv14aInput, sbDFFv14aOutput);
    
    sb_d_ffv14b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv14bInput, sbDFFv14bOutput);

    
    sb_d_ffv15a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv15aInput, sbDFFv15aOutput);


    sb_d_ffv15b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv15bInput, sbDFFv15bOutput);
    
    sb_d_ffv16a: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv16aInput, sbDFFv16aOutput);


    sb_d_ffv16b: ENTITY work.SB_D_FF(rtl)
    port map (clk, rst, sbDFFv16bInput, sbDFFv16bOutput);

    ----Make a pc LUT instance
    positLUTv0a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits,ExponentBits,numberOfBits)
    port map(sbDFFv0aOutput,pcLUTv0aOutput);

    ---voa converter
    v0aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv0aOutput, v0aConverterOutput);

    ----Make a pc LUT instance
    positLUTv0b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv0bOutput,pcLUTv0bOutput);
    
    ---vob converter
    v0bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv0bOutput, v0bConverterOutput);

    ----Make a pc LUT instance
    positLUTv1a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv1aOutput,pcLUTv1aOutput);
   
    ---v1a converter
    v1aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv1aOutput, v1aConverterOutput);

    ----Make a pc LUT instance
    positLUTv1b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv1bOutput,pcLUTv1bOutput);
    
    ---v1b converter
    v1bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv1bOutput, v1bConverterOutput);

    ----Make a pc LUT instance
    positLUTv2a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv2aOutput,pcLUTv2aOutput);
    
    ---v2a converter
    v2aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv2aOutput, v2aConverterOutput);


    ----Make a pc LUT instance
    positLUTv2b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv2bOutput,pcLUTv2bOutput);
    
    ---v2b converter
    v2bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv2bOutput, v2bConverterOutput);


    ----Make a pc LUT instance
    positLUTv3a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv3aOutput,pcLUTv3aOutput);
    
    ---v3a converter
    v3aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv3aOutput, v3aConverterOutput);

    ----Make a pc LUT instance
    positLUTv3b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv3bOutput,pcLUTv3bOutput);
    
    ---v3b converter
    v3bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv3bOutput, v3bConverterOutput);

    ----Make a pc LUT instance
    positLUTv4a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv4aOutput,pcLUTv4aOutput);
    
    ---v4a converter
    v4aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv4aOutput, v4aConverterOutput);


    ----Make a pc LUT instance
    positLUTv4b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv4bOutput,pcLUTv4bOutput);
    
    ---v4b converter
    v4bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv4bOutput, v4bConverterOutput);


    ----Make a pc LUT instance
    positLUTv5a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv5aOutput,pcLUTv5aOutput);
    
    ---v5a converter
    v5aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv5aOutput, v5aConverterOutput);

    ----Make a pc LUT instance
    positLUTv5b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv5bOutput,pcLUTv5bOutput);

    ---v5b converter
    v5bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv5bOutput, v5bConverterOutput);
    
    ----Make a pc LUT instance
    positLUTv6a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv6aOutput,pcLUTv6aOutput);
    
    ---v6a converter
    v6aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv6aOutput, v6aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv6b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv6bOutput,pcLUTv6bOutput);
    
    ---v6b converter
    v6bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv6bOutput, v6bConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv7a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)

    port map(sbDFFv7aOutput,pcLUTv7aOutput);
    
    ---v7a converter
    v7aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv7aOutput, v7aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv7b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv7bOutput,pcLUTv7bOutput);
    
    ---v7b converter
    v7bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv7bOutput, v7bConverterOutput);

    ----Make a pc LUT instance
    positLUTv8a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv8aOutput,pcLUTv8aOutput);
    
    ---v8a converter
    v8aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv8aOutput, v8aConverterOutput);
    
    ----Make a pc LUT instance
    positLUTv8b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv8bOutput,pcLUTv8bOutput);
    
    ---v8b converter
    v8bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv8bOutput, v8bConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv9a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv9aOutput,pcLUTv9aOutput);
    
    ---v9a converter
    v9aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv9aOutput, v9aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv9b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv9bOutput,pcLUTv9bOutput);
    
    ---v9b converter
    v9bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv9bOutput, v9bConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv10a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv10aOutput,pcLUTv10aOutput);
    
    ---v10a converter
    v10aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv10aOutput, v10aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv10b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv10bOutput,pcLUTv10bOutput);
    
    ---v10b converter
    v10bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv10bOutput, v10bConverterOutput);
    
    ----Make a pc LUT instance
    positLUTv11a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv11aOutput,pcLUTv11aOutput);
    
    ---v11a converter
    v11aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv11aOutput, v11aConverterOutput);
    
    ----Make a pc LUT instance
    positLUTv11b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv11bOutput,pcLUTv11bOutput);
    
    ---v11b converter
    v11bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv11aOutput, v11bConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv12a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv12aOutput,pcLUTv12aOutput);
    
    ---v12a converter
    v12aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv12aOutput, v12aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv12b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv12bOutput,pcLUTv12bOutput);
    
    ---v12b converter
    v12bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv12bOutput, v12bConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv13a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv13aOutput,pcLUTv13aOutput);
    
    ---v13a converter
    v13aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv13aOutput, v13aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv13b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv13bOutput,pcLUTv13bOutput);
    
    ---v13b converter
    v13bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv13bOutput, v13bConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv14a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv14aOutput,pcLUTv14aOutput);
    
    ---v14a converter
    v14aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv14aOutput, v14aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv14b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv14bOutput,pcLUTv14bOutput);
    
    ---v14b converter
    v14bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv14bOutput, v14bConverterOutput);


    
    ----Make a pc LUT instance
    positLUTv15a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv15aOutput,pcLUTv15aOutput);
    
    ---v15a converter
    v15aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv15aOutput, v15aConverterOutput);

    
    ----Make a pc LUT instance
    positLUTv15b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv15bOutput,pcLUTv15bOutput);
   
    
    ---v15b converter
    v15bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv15bOutput, v15bConverterOutput);
    
    ----Make a pc LUT instance
    positLUTv16a: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv16aOutput,pcLUTv16aOutput);
    
    ---v16a converter
    v16aInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv16aOutput, v16aConverterOutput);
    
    ----Make a pc LUT instance
    positLUTv16b: ENTITY work.FloatLUT (rtl)
    generic map(MantissaBits, ExponentBits,numberOfBits)
    port map(sbDFFv16bOutput,pcLUTv16bOutput);
   
    ---v16b converter
    v16bInputConverter: entity work.InputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, pcLUTv16bOutput, v16bConverterOutput);

    
    mb_d_ffv0a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v0aConverterOutput, mbDFFv0aOutput);

    mb_d_ffv0b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v0bConverterOutput, mbDFFv0bOutput);
    
    mb_d_ffv1a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v1aConverterOutput, mbDFFv1aOutput);

    mb_d_ffv1b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v1bConverterOutput, mbDFFv1bOutput);


    mb_d_ffv2a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v2aConverterOutput, mbDFFv2aOutput);

    
    mb_d_ffv2b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v2bConverterOutput, mbDFFv2bOutput);
    
    mb_d_ffv3a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v3aConverterOutput, mbDFFv3aOutput);

    
    mb_d_ffv3b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v3bConverterOutput, mbDFFv3bOutput);


    mb_d_ffv4a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v4aConverterOutput, mbDFFv4aOutput);

    
    mb_d_ffv4b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v4bConverterOutput, mbDFFv4bOutput);


    mb_d_ffv5a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v5aConverterOutput, mbDFFv5aOutput);

    
    mb_d_ffv5b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v5bConverterOutput, mbDFFv5bOutput);
    
    
    mb_d_ffv6a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v6aConverterOutput, mbDFFv6aOutput);

    mb_d_ffv6b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v6bConverterOutput, mbDFFv6bOutput);
    
    mb_d_ffv7a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v7aConverterOutput, mbDFFv7aOutput);

    mb_d_ffv7b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v7bConverterOutput, mbDFFv7bOutput);


    mb_d_ffv8a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v8aConverterOutput, mbDFFv8aOutput);

    
    mb_d_ffv8b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v8bConverterOutput, mbDFFv8bOutput);
    
    mb_d_ffv9a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v9aConverterOutput, mbDFFv9aOutput);

    
    mb_d_ffv9b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v9bConverterOutput, mbDFFv9bOutput);


    mb_d_ffv10a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v10aConverterOutput, mbDFFv10aOutput);

    
    mb_d_ffv10b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v10bConverterOutput, mbDFFv10bOutput);


    mb_d_ffv11a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v11aConverterOutput, mbDFFv11aOutput);

    
    mb_d_ffv11b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v11bConverterOutput, mbDFFv11bOutput);
    
    mb_d_ffv12a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v12aConverterOutput, mbDFFv12aOutput);

    
    mb_d_ffv12b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v12bConverterOutput, mbDFFv12bOutput);


    mb_d_ffv13a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v13aConverterOutput, mbDFFv13aOutput);

    
    mb_d_ffv13b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v13bConverterOutput, mbDFFv13bOutput);
    
    mb_d_ffv14a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v14aConverterOutput, mbDFFv14aOutput);
    
    mb_d_ffv14b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v14bConverterOutput, mbDFFv14bOutput);

    
    mb_d_ffv15a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v15aConverterOutput, mbDFFv15aOutput);


    mb_d_ffv15b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v15bConverterOutput, mbDFFv15bOutput);
    
    mb_d_ffv16a1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v16aConverterOutput, mbDFFv16aOutput);


    mb_d_ffv16b1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, v16bConverterOutput, mbDFFv16bOutput);


    --- PCSystem Definition
    pcSystem: ENTITY work.PCSystem_32(rtl)
    generic map(MantissaBits,ExponentBits,numberOfBits,FlopocoBits)
    PORT MAP (
              clk=>clk,
              rst=>rst,
              enable=>enableOutput,
              v0a=>mbDFFv0aOutput,
              v0b=>mbDFFv0bOutput,
              v1a=>mbDFFv1aOutput,
              v1b=>mbDFFv1bOutput,
              v2a=>mbDFFv2aOutput,
              v2b=>mbDFFv2bOutput,
              v3a=>mbDFFv3aOutput,
              v3b=>mbDFFv3bOutput,
              v4a=>mbDFFv4aOutput,
              v4b=>mbDFFv4bOutput,
              v5a=>mbDFFv5aOutput,
              v5b=>mbDFFv5bOutput,
              v6a=>mbDFFv6aOutput,
              v6b=>mbDFFv6bOutput,
              v7a=>mbDFFv7aOutput,
              v7b=>mbDFFv7bOutput,
              v8a=>mbDFFv8aOutput,
              v8b=>mbDFFv8bOutput,
              v9a=>mbDFFv9aOutput,
              v9b=>mbDFFv9bOutput,
              v10a=>mbDFFv10aOutput,
              v10b=>mbDFFv10bOutput,
              v11a=>mbDFFv11aOutput,
              v11b=>mbDFFv11bOutput,
              v12a=>mbDFFv12aOutput,
              v12b=>mbDFFv12bOutput,
              v13a=>mbDFFv13aOutput,
              v13b=>mbDFFv13bOutput,
              v14a=>mbDFFv14aOutput,
              v14b=>mbDFFv14bOutput,
              v15a=>mbDFFv15aOutput,
              v15b=>mbDFFv15bOutput,
              v16a=>mbDFFv16aOutput,
              v16b=>mbDFFv16bOutput,
              --lastWeight=>lastWeight,
              --lastMultiplierOutput => lastMultiplierOutput,
              --topNodeOutput => topNodeOutput,
              vout=>pcSystemOutput);
    
    mbDFFvoutStage1: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits+FlopocoBits)
    port map (clk, rst, mbDFFvoutInput, mbDFFvoutOutput);
    
    ---Output IEEE converter
    voutOutputConverter: entity work.OutputIEEE_7_24_to_7_24(arch)
    PORT MAP (clk, mbDFFvoutOutput,voutConverterOutput);
    
    mbDFFvoutStage2: ENTITY work.MB_D_FF(rtl)
    generic map(numberOfBits)
    port map (clk, rst, voutConverterOutput, mbDFFvoutStage2Output);

    vout <= mbDFFvoutStage2Output;

    --oddr0: ODDR
    --generic map (DDR_CLK_EDGE => "OPPOSITE_EDGE",INIT => '0', SRTYPE => "ASYNC")
    --port map (Q=> clk_out, C=> clk, CE => '1', D1 => '1', D2 => '0',R => '0', S=> '0');


END ARCHITECTURE;
