1. An Internet Protocol (IP) address is a unique 32 bit integer that identifies
   a host on a computer network. IPv4 is one version of IP addresses that is
   typically written out as a group of 4 integers seperated by dots.

   e.g: 192.168.0.1

   Each integer above is called an 'octet' (meaning 8 bits wide) and ranges from
   0-255. The unique 32 bit integer representation for this IPv4 address can be
   computed by converting all octets to binary, concatenating the binary bits
   from left to right and interpreting the resulting 32 bit string as a binary
   integer.

   Examples:

   1. Convert each octet in 192.168.0.1 to binary

   192 = 11000000 168 = 10101000 0 = 00000000 1 = 00000001

   2. Concatenate bits from left to right

   11000000101010000000000000000001

   3. Print out 32 bit unsigned integer representation

   3232235521

   Write a program called `ip2int` that takes in an IPv4 address and returns the
   it's equivalent unique 32 bit integer.

2. Endianess refers to the order in which your computer stores the bytes for an
   integer. In little endian, the bytes are arranged from least significant byte
   (LSB) to most significant byte (MSB). Whereas, in big endian the bytes are
   arranged from MSB to LSB.

   In little endian, the 16 bit integer `1` is represented as:

   Address: 0 1 
   Byte: 00000001 00000000

   However in big endian, it is

   Address: 0 1 
   Byte: 00000000 00000001

   More precisely, in little endian the lowest memory address contains the
   \_\_\_\_\_, whereas in big endian the lowest memory address contains the
   \_\_\_\_.

   A) MSB, LSB B) LSB, MSB C) MSB, MSB D) LSB, LSB

   Most computers today are little endian. You can verify this with the
   following program

   ```c
   bool is_little_endian() {

      int x = 1;

      return *((char*)(&x)) + '0' == '1';
   }
   ```

   Explain, in plain English, how this program works.

   Write a function called `littleorbig` that takes in a 32 bit integer and
   reverses it's byte order. Effectively converting little-endian to big-endian
   and vica versa.

   Big endian is also known as 'network byte order'. It is a standard that when
   integers need to be sent over a network, they are transmitted with the MSB
   first. However, in recent times, this has become more of a suggestion.

   Please do not confuse endianess with the order of bits in a byte. The order
   of bits in a byte will always be the same. The 0th bit (rightmost) is always
   the least significant bit.

3. An XOR cipher is an encryption algorithm that uses the XOR operation ($\oplus$).
   The XOR operation is short for "exclusive-or", meaning "either but not both".
   
   The truth table for XOR, 

   $1 \oplus 0 = 1$
   
   $0 \oplus 1 = 1$

   $1 \oplus 1 = 0$

   $0 \oplus 0 = 0$

   Notice that $\oplus$ has the following properties,
   
   XOR is nilpotent: $A \oplus A = 0$
   
   XOR is commutative: $A \oplus B = B \oplus A$
   

   Given a key $K$ and message $M$, the ciphertext is $K \oplus M$.
   
