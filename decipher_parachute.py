# Deciphers Perseverance's parachute message

# Structue of the code and first three rings cracked by twitter user
# @FrenchTech_paf, meaning of last ring found by @pramirez624.

# ------------------------------------------------------------------------------

# The bit strings for each ring of the parachute, where white = 0 and red = 1
# Rings go from the center outwards
ring1 = """
0000000001
0000010010
0000000101
0001111111
1111111111
1111111111
1111111111
0000000100
"""
ring2 = """
0000011001
0001111111
1111111111
0000001101
0000001001
0000000111
0000001000
0000010100
"""
ring3 = """
1111111111
0000010100
0000001000
0000001001
0000001110
0000000111
0000010011
0001111111
"""
ring4 = """
0000001011
0000111010
0000001110
0001110110
0000001010
0000011111
0000010111
0000100010
"""

# How many bits to use per letter ... must divide the number of bits!
bits_per_letter = 10

# The bit offsets for the decoding -- set to None initially, then change as
# they are found
ioff1 = None
ioff2 = None
ioff3 = None
ioff4 = None
# These are the found offsets:
# ioff1 = 70
# ioff2 = 30
# ioff3 = 10
# ioff4 = 70

# ==============================================================================

def num_to_letter(num):
  if 1 <= num <= 26:
    return chr(num+64)
  else:
    return "?"

def convert_numbers(bits, ioff):
  numbers = []
  for i in range(num_groups):
    i1 = ioff + i*bits_per_letter
    i2 = i1 + bits_per_letter
    s = "".join(bits[j%num_bits] for j in range(i1, i2))
    numbers.append(int(s, 2))
  return numbers

def decode_inner(numbers):
  return "".join([num_to_letter(n) for n in numbers])

def decode_outer(numbers):
  return " ".join([num_to_letter(numbers[i]) if i in (3,7) else str(numbers[i]) for i in range(len(numbers))])

# ==============================================================================

ring1 = ring1.replace("\n", "")
ring2 = ring2.replace("\n", "")
ring3 = ring3.replace("\n", "")
ring4 = ring4.replace("\n", "")

num_bits = len(ring1)
num_groups = num_bits // bits_per_letter

rings = [(1, ring1, ioff1), (2, ring2, ioff2), (3, ring3, ioff3), (4, ring4, ioff4)]

# Solve rings
for ring, bits, ioff in rings:

  print(f"\n--------Ring {ring}--------")
  final_ioff = ioff

  # Find the offset by trial and error
  if final_ioff is None:

    print("Type 'y' when desired offset is found")
    for ioff in range(num_bits):

      numbers = convert_numbers(bits, ioff)

      if ring <= 3:
        # For first three rings we convert all numbers to letters
        text = decode_inner(numbers)
        print(ioff, ":", numbers, text)
      else:
        # For outer ring, we only convert 4th and 8th numbers
        text = decode_outer(numbers)
        print(ioff, ":", text)

      ans = input("Accept (y/N)?: ")
      if ans.lower() == "y":
        final_ioff = ioff
        print()
        break

  # Print result
  numbers = convert_numbers(bits, final_ioff)
  if ring <= 3:
    text = decode_inner(numbers)
  else:
    text = decode_outer(numbers)
  print(f"Ring1: {text}, offset {final_ioff}")
