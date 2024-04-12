# Code to convert back and forth between fixed point numbers, float point numbers and posits
#Author: Eric Mibuari

import torch
import math

class PositConverter:
    
    #initialize the class variables
    def __init__(self, num_bits, useed_es, frac_bits):
    
        self.num_bits_fixed_point = num_bits
        self.posit_num_bits = num_bits
        self.num_frac_bits = frac_bits
        self.es = useed_es

    #Reverses a string - used by the integer to binary conversion function
    def reverse_string(self, input_string):
        new_string = ""
        for i in range(len(input_string)):
            index = len(input_string) -1 - i
            val = input_string[index]
            new_string += str(val)
        return new_string

    #convert an integer in base 10 to binary
    def convert_int_to_bin(self,float_num, bit_limit):

        num_int_bits = bit_limit
        bin_div = 2
        bit_string =""
        result = float_num
        remainder = 0
        
        result = int(result)
        bin_div = int(bin_div) #TODO: might be unnecessary
      
        while(result > 0):
            result_div = int(result/bin_div)
            remainder = result - (result_div * bin_div)
            result = result_div
            bit_string += str(remainder)

        if(len(bit_string) > num_int_bits):
            bit_string = bit_string[0:num_int_bits] #TODO: confirm if right substring

        new_string = self.reverse_string(bit_string)

        if(len(new_string) < num_int_bits):
            diff = num_int_bits - len(new_string)
            padding_list = ['0']*diff
            padding = ''.join(padding_list)
            new_string = str(padding) + new_string

        return new_string

    #Converts a fractional number in base 10 to its binary fractional value
    def convert_fractional_decimal_to_bin(self,fractional_decimal, num_frac_bits):
        result = fractional_decimal
        decimals = ""
        bits_available = num_frac_bits
        
        while bits_available > 0:
            result = result * 2
            if(result < 1):
                decimals+= "0"
            else:
                decimals+= "1"
                result = result - 1
            bits_available -= 1
        
        return decimals

    #Converts a posit string into its fixed point representation
    def convert_posit_to_fixed_point_num(self, posit_num, num_int_bits, num_frac_bits):
        float_val = self.convert_posit_to_float(posit_num)
        fixed_point_num = self.convert_float_to_fixed_point (float_val)
        return fixed_point_num
    
    #Converts a fixed point number to its posit form
    def convert_fixed_point_num_to_posit(self, fixed_point_num):
        float_val = self.convert_fixed_point_to_float(fixed_point_num)
        posit_num = self.convert_float_to_posit(float_val)
        return posit_num

    #There are two exceptional cases for which the posit conversions are easy(zero and infinity)
    #Refer to the posit paper for details
    def create_except_case_string(self,start_bit, num_bits):
        ret_str = start_bit
        for i in range(num_bits -1):
            ret_str += "0"
        return ret_str

    #Computes the base 2 exponent of a number
    def get_number_to_bin_exponent(self,dividend):
        bin_div, exp = (2, 0)
        result = int(dividend)
     
        while(result > 1):
            result = int(result/bin_div)
            exp += 1
        return exp

    # Given a number, this computes the string representations of the binary formats
    # for the exponent, and fractional parts of the posit string
    def get_exponent_and_frac_bits(self, abso_val, useed, es, nbits, regime_length):

        result = abso_val
        expo = self.get_number_to_bin_exponent(result)
        expo_bits = self.convert_int_to_bin(expo,es)
        dividend  = useed * 2**expo
        mixed_fraction = float(result)/dividend
        frac_remainder = mixed_fraction - 1
        useed_divider = frac_remainder * (useed)
        available_bits_for_frac_remainder = nbits - (len(str(expo_bits)) + regime_length + 1)
        fraction_bits = self.convert_int_to_bin(useed_divider, available_bits_for_frac_remainder) #TODO: check what happens to fractional part of frac

        return expo_bits, fraction_bits

    #For numbers that are greater than useed, this computes the posit string representation
    def get_string_bits_big(self, abso_val, useed,es,nbits):
        
        result = abso_val
        regime_length = 0
        while result > useed:
            result_div = int(result/useed)
            result = result_div
            regime_length += 1

        dividend = float(abso_val)/(useed**regime_length)
        exponent_bits, fraction_bits = self.get_exponent_and_frac_bits(dividend,useed,es,nbits, regime_length)
        return regime_length, exponent_bits, fraction_bits

    #TODO - rename the variables in the next few functions to make the code more readable
    #TODO - collapse and reuse functions instead of multiple "similar" functions
    def find_d_regular(self, h):
        power = 0
        es = self.es
        while True:
            val = 2**(2**es) ** power
            if (val > h):
                break;
            power = power +1
        return power

    def convert_regular_float_to_posit(self, x):
        #print ("converting pure_float: ", x)
        es = self.es
        sign_bit = 1
        abs_x = x
        
        if(x < 0):
            abs_x = x * -1
        if (x > 0):
            sign_bit = 0
        
        #find a d such that 256^d covers x
        d = self.find_d_regular(abs_x)
        #print("D, float equivalent Exponent Value", d)

        
        #TODO: See if you can get more accuracy by playing with powers of 2. Right now we are setting power of 2 to zero by default
        c = 1
        y = 0
        den = 2 ** (((2**es) * c)+y)
        initial_whole_fract = abs_x/den
        b = initial_whole_fract
        
        #TODO: make sure the regime bits in the following function are for a negative regime
        regime_bits = self.create_regime_bits_string(c, "0")
        #print("Regime_bits", regime_bits)
        #print("Length of th regime bits", len(regime_bits))
        
        #regime_bits = convert_int_to_bin (c,es) #TODO: regime bits can take any numbe of bits, so change es here
        exponent_bits = self.convert_int_to_bin (y, es)
        #print("Exponent_bits", exponent_bits)
        #print("Length of th exponent_bits", len(exponent_bits))


        
        num_bits = self.posit_num_bits
        available_bits_for_frac_remainder = num_bits - (1 +len(regime_bits) + len(exponent_bits))
        fractional_bits = self.convert_fractional_decimal_to_bin(b, available_bits_for_frac_remainder)
        posit_string = str(sign_bit) + regime_bits + exponent_bits + fractional_bits
        #TODO: Do we need to REVERSE STRING TO BE IN POSIT FORMAT?
        return posit_string

    def find_d (self, h):
        power = 0
        #print("The input parameter h", h)
        while True:
            #print("Power to find d",power)
            val = 2 ** (-1 *power)
            #print("value",val)
            if (val > h/2 and val <= h ):
                break;
            power = power +1
        #power = 171
        #print("Power", (-1 * power))
        return -1 * power

    def find_c_y(self, d, es):
        max_y = (2**es) -1
        #print("Max_y", max_y)
        c = 0
        #print("Find regime bits power as c_y",c)
        while True:
            y = d + (2**es) * c
            #print("Y", y)
            if (y >= 0 and y <= max_y):
                return (c*-1), y
            c = c + 1

    #Takes a number whose intgral portion is 0 e.g. 0.6446, or -0.7655 and converts it to a posit string
    def convert_pure_float_to_posit(self, x):
        
        #print ("converting pure_float: ", x)
        es = self.es #TODO: move this elsewhere.
        sign_bit = 1
        abs_x = x
        
        if(x < 0):
            abs_x = x * -1

        if (x > 0):
            sign_bit = 0
        
        d = self.find_d(abs_x)
        #print("D, Exponent Value to represent given value", d)
        
        #c, y = self.find_c_y(d, es)
        c, y = self.find_c_y(d, es)
        #print("C, Regime code Value", c)
        #print("y",y)
        den = 2 ** (((2**es) * c)+y)
        #print("Normalisation Value", den)

        b = (abs_x/den) - 1
        #print("Normalised min value", b)

        regime_bits = self.create_regime_bits_string(c*(-1), "1")
        #print("Regime_bits", regime_bits)
        #print("Length of th regime bits", len(regime_bits))
        exponent_bits = self.convert_int_to_bin (y, es)
        #print("Exponent_bits", exponent_bits)
        #print("Length of th exponent_bits", len(exponent_bits))

        
        num_bits = self.posit_num_bits
        #print("Available total number of bits",num_bits)
        available_bits_for_frac_remainder = num_bits - (1 +len(regime_bits) + len(exponent_bits))
        #print("Available fraction  bits", available_bits_for_frac_remainder)
        fractional_bits = self.convert_fractional_decimal_to_bin(b, available_bits_for_frac_remainder)
        #print("Fraction bits", fractional_bits)
        posit_string = str(sign_bit) + regime_bits + exponent_bits + fractional_bits
        #print("Posit string, float equivalent Exponent Value", posit_string)
        
        return posit_string

    #Creates the binary string sequence to represent the regime section of the posit string
    #Refer to the posit reference paper (section 1.1) to see the "tally mark" approach adopted
    def create_regime_bits_string(self,regime_length, expo_sign_bit):
        reg_str = ""
        #print("Expo sign bit", expo_sign_bit)
        #print("Regime_length", regime_length)
        bit_to_add = 1-int(expo_sign_bit)
        for i in range(regime_length):
            reg_str += str(bit_to_add)
        reg_str += str(expo_sign_bit)
        #print("Reg_str", reg_str)
        return reg_str

    # Converts a number in base 10 to its posit string format. The number may be an integer or a float
    #Reference: posit paper section 4 "Converting values into posits"
    def convert_float_to_posit(self,float_value):
        # print the floatvalue
        #print("Given float_vaue", float_value)
        float_value = float(float_value)
        es = self.es
        #TODO (ambitious): Determine the above parameters dynamically from the value of the float num provided
        nbits = self.posit_num_bits
        
        if float_value == 0:
            return self.create_except_case_string("0", self.posit_num_bits)
        if float_value == math.inf:
            return self.create_except_case_string("1", self.posit_num_bits)

        abso_val = float_value
        sign_bit = "0"
        if float_value < 0:
            sign_bit = "1"
            abso_val = float_value * -1

        expo_sign_bit = "0"
        if abso_val < 1:
            expo_sign_bit = "1"
            #TODO: check if this if condition holds, should be checking for sign of exponent not full number
        
        posit_string = ""
        useed = 2**(2**es)
      
        regime_length,exponent_bits, fraction_bits,regime_bits_string  = (0,"","","")

        #TODO: these three if conditions may not be sufficient to cover all values of absolute value
        #the value could be between 0-1, 1-useed, above useed. Sign might also matter
        if(abso_val > useed):
            regime_length, exponent_bits, fraction_bits  = self.get_string_bits_big(abso_val, useed,es,nbits)
            regime_bits_string = self.create_regime_bits_string(regime_length, expo_sign_bit) #TODO: check what happens when there's no regime
            final_string = sign_bit+regime_bits_string+exponent_bits+fraction_bits
        elif(abso_val < 1):
            #print("Absolute value is less than 1")
            final_string = self.convert_pure_float_to_posit(float_value)
        else:
            final_string = self.convert_regular_float_to_posit(float_value)
        
        return final_string

    #Converts a base 2 (binary) number to its base 10 integer format
    def convert_bin_to_int(self,bin_string):
        len_bin = len(bin_string)
        sum = 0
        for i in range(len_bin):
            power = len_bin - 1 - i
            ind_val = int(bin_string[i])
            val = ind_val * (2 ** power)
            sum += val
        return sum

    #Converts a base 2 (binary) number to its base 10 fractional format
    def convert_bin_to_fraction(self, bin_string):
        len_bin = len(bin_string)
        sum = 0
        for i in range(len_bin):
            ind_val = int(bin_string[i])
            power = (i+1) * -1
            val = ind_val * (2**power)
            sum += val
        return sum

    #Checks if the posit string supplied is all zeroes
    #This is one of the exceptional cases which are handled expeditioulsly by the converter
    def all_zero(self, posit_str):
        for i in range(len(posit_str)):
            if int(posit_str[i]) == 1: return False
        return True

    #Performms a Two's complement conversion of a binary string
    #TODO: may not be necessary for our code.
    def twos_complement(self, posit_string):
        #TODO: implement twos_complement
        return posit_string


    #Given a posit string, computes the length of the regime portion, as well as the sign of the regime
    def get_lengths(self, posit_string):
        
        posit_string = posit_string[1:]
        first_regim_num = int(posit_string[0])
        posit_string = posit_string[1:]
        regime_length = 0
        for i in range(len(posit_string)):
            regime_length += 1
            num = int(posit_string[i])
            if(not num == first_regim_num):
                break
        if (first_regim_num == 0):
            regime_sign = -1
        elif(first_regim_num == 1):
            regime_sign = 1

        return regime_length, regime_sign

    #Adds all components extracted from a posit string parsing to compute the base 10 value equivalent
    def compute_full_number(self, fraction_val, exponet_val, regime_exponent, regime_length, regime_sign, sign):

        es = self.es
        #num = 0
        c = regime_exponent
        useed_power = 1
        
        if (regime_sign == -1):
            useed_power = 2**((2**es)*(c-1))
        else:
            useed_power = 2**((2**es)*c)
      
        fract_multiplier = 1+fraction_val

        if(exponet_val == 0):
            fract_multiplier = fraction_val

        second_scale_factor =  2**exponet_val
        num = sign * useed_power * second_scale_factor * fract_multiplier
        return num

    #Converts a posit binary sequence into its decimal value equivalent
    #Reference: posit paper section 1.2
    def convert_posit_to_float(self,posit_string):
        
        es = self.es
        if self.all_zero(posit_string):
            return 0
        if int(posit_string[0]) == 1 and self.all_zero(posit_string[1:]):
            return math.inf

        #TODO: Extract regime bits dynamically
        sign = -1 if int(posit_string[0]) == 1 else 1
        
        #TODO - implement two's complement if necessary
        if (sign == -1):
            posit_string = self.twos_complement(posit_string)
        
        regime_length, regime_sign = self.get_lengths(posit_string)
        first_scale_factor = 1
        regime_exponent = regime_length
        
        if (regime_sign == -1): # A number whose regime exponent is negative e.g. 256 ^ -3
            regime_exponent = (regime_sign * regime_length) +1

        end_exponent_bits_index = regime_length+2+es

        exponent_bits = posit_string[int(regime_length+2):int(end_exponent_bits_index)]
        exponent_val = self.convert_bin_to_int(exponent_bits)
        second_scale_factor = 2**exponent_val
        
        fraction_bits = posit_string[end_exponent_bits_index:len(posit_string)]
        fraction_val_raw = self.convert_bin_to_fraction(fraction_bits)
        fraction_val = fraction_val_raw
        expression_val = self.compute_full_number(fraction_val, exponent_val, regime_exponent, regime_length, regime_sign, sign)

        return expression_val

    #Converts a fixed point number into its float equivalent
    def convert_fixed_point_to_float(self,fixed_point_num):
        fixed_point_num_string = str(fixed_point_num)
        sign = int(fixed_point_num_string[0])
        fixed_point_num = fixed_point_num_string[1:]
        radix_index = fixed_point_num.index('.')
        integral_part = fixed_point_num[0:radix_index]
        fractional_part = fixed_point_num[radix_index+1:]
        integral_part_reversed =  self.reverse_string(integral_part)
        
        integral_sum = 0
        for i in range(len(integral_part_reversed)):
            num_read = int(integral_part_reversed[i])
            if num_read == 1:
                integral_sum += 2**i

        fractional_sum = 0
        for j in range(len(fractional_part)):
            num_read = int(fractional_part[j])
            if num_read == 1:
                fractional_sum += float(1)/2**(j+1)

        total_float = integral_sum + fractional_sum
        if sign == 1:
            total_float = total_float * -1

        return total_float

    #Converts a floating point number into its fixed point equivalent
    def convert_float_to_fixed_point(self, float_num):
        fp_sign = ""
        abso_val = float_num
        if float_num < 0:
            fp_sign += "1"
            abso_val = abso_val * -1
        else:
            fp_sign += "0"

        fractional_part = 0
        integral_part = 0
        if abso_val < 1:
            fractional_part = abso_val
        else:
            integral_part = int(abso_val)
            fractional_part = abso_val - integral_part
        
        #TODO, determine which among the the fractioal or integral parts needs more bits
        #int_bin_string = self.convert_int_to_bin(integral_part, self.config_num_int_bits)
        #frac_bin_string = self.convert_fractional_decimal_to_bin(fractional_part, self.num_frac_bits)
        
        int_bin_string = self.convert_int_to_bin(integral_part, self.posit_num_bits - self.num_frac_bits )
        frac_bin_string = self.convert_fractional_decimal_to_bin(fractional_part, self.num_frac_bits)
    
        return fp_sign + int_bin_string +"." + frac_bin_string

    #A function with some sample back and forth conversions between various formats
    def sample_conversions(self):

        test_numbers = [-2.0, -1.9865, -0.755, 3.55393e-06, 3.553926944732666e-06, 3.553926946732666e-06, 2.08975757675, -0.755343,  0.2355343]
        #test_numbers = [-1.9865]
        #test_numbers = [2.08975757675]
        for i in range(len(test_numbers)):
            num = test_numbers[i]
            print("\n")
            print("-------------------")
            print(num)
            print("-------------------")
            print("POSIT")
            print("-------------------")

            #print("converting float ", num, " to posit" )
            posit_value = self.convert_float_to_posit(num)
            print("obtained posit value: ", posit_value, " to posit" )
            #print("converting posit ",posit_value, "back to float " )
            float_point_value = self.convert_posit_to_float(posit_value)
            print("obtained back float point value: ", float_point_value )
            #print("diff in floats before & after posit conversion: ", num - float_point_value)
            
            abs_pos_converted = float_point_value
            abs_num = num
            if (float_point_value < 0):
                abs_pos_converted = float_point_value * -1
            if (num < 0):
                abs_num = num * -1
            #print("diff in floats before & after fixed-point conversion: ", num - decimal_float)
            print("accuracy in conversion: ", (abs_pos_converted/abs_num) *100, "%" )

            print("-------------------")
            print("FIXED POINT")
            print("-------------------")

            print("converting float:", num, " to fixed point num")
            fixed_string = self.convert_float_to_fixed_point(num)
            
            print("fixed_point_string: ", fixed_string)
            #print("converting fixed point num:", fixed_string, " to float")
            decimal_float = self.convert_fixed_point_to_float(fixed_string)
            print("float: ", decimal_float)
            abs_converted = decimal_float
            if (decimal_float < 0):
                abs_converted = decimal_float * -1
            #print("diff in floats before & after fixed-point conversion: ", num - decimal_float)
            print("accuracy in conversion: ", (abs_converted/abs_num)*100, "%" )

    #Thierry's quantize code
    def quantize_(self, x, qi, qf):
        fmax = 1. - float(torch.pow(2., torch.FloatTensor([-1. * qf])).numpy()[0])
        imax =      float((torch.pow(2., torch.FloatTensor([qi-1])) - 1).numpy()[0])
        imin = -1 * float((torch.pow(2., torch.FloatTensor([qi-1]))).numpy()[0])
        fdiv = float(torch.pow(2., torch.FloatTensor([-qf])).numpy()[0])
        
        x = torch.floor ( x / fdiv) * fdiv
        x = torch.clamp(x, imin, imax + fmax)
        
        return x
    
    #Thierry's quantize code
    def quantize_sparse_weights(self, x, qi, qf):
        pos_weights_mask   = torch.gt(x, 0)
        pos_weights_values = torch.masked_select(x, pos_weights_mask)
        
        pos_min = pos_weights_values.min()
        pos_max = pos_weights_values.max()
        
        pos_weights = x * pos_weights_mask.float()
        pos_weights = pos_weights - pos_min
        new_max = pos_weights.max()
        pos_weights = torch.div ( pos_weights, new_max )
        pos_weights = pos_weights * pos_weights_mask.float()
        
        pos_weights = quantize_(pos_weights, qi, qf)
        pos_weights = torch.mul(pos_weights , new_max)
        pos_weights = pos_weights + pos_min
        pos_weights = pos_weights * pos_weights_mask.float()
        
        return pos_weights



    def main (self):
        pass

    def run (self):
        self.main()


"""
num_bits_fixed_point = 16
config_num_int_bits = 16
posit_num_bits = 16
num_frac_bits = 5
es = 3

num_bits = 8
num_frac_bits = 6
es = 1

pconv = PositConverter(num_bits, es, num_frac_bits)
pconv.sample_conversions()

#print(pconv.convert_posit_to_float('11000000'))
posit_string = pconv.convert_float_to_posit(-1.9865)
print(posit_string)
float_num = pconv.convert_posit_to_float(posit_string)
print(float_num)


posit_string = pconv.convert_float_to_posit(1.4347745)
print(posit_string)
float_num = pconv.convert_posit_to_float(posit_string)
print(float_num)
"""
