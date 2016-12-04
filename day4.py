"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""
from collections import OrderedDict as OD

rooms = []
with open('day4.txt', 'r') as f:
  rooms = f.readlines()

def is_valid_room(room_list, checksum):
  # Valid room: if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization
  rooms = ''.join(room_list)
  # Count how many of each value in checksum
  counted = [(rooms.count(check), check) for check in checksum]
  counted = sorted(counted, reverse=True)
  ordered = OD()

  correct_checksum = []
  # Order by frequency
  for count, check in counted:
    ordered[count] = ordered.get(count, '') + check
  for count, check in ordered.items():
    if count == 0: continue
    correct_checksum += sorted(check)
  
  # Calculate the valid checksum
  correct_checksum = [check for check in correct_checksum if check in checksum]
  correct_checksum = ''.join(correct_checksum)

  return correct_checksum == checksum

def sum_sector_ids(rooms):
  sum_ids = 0

  for room in rooms:
    if not room: continue
    room_list = room.strip().split('-')
    sector_id, checksum = room_list.pop().split('[')
    checksum = checksum.replace(']', '')

    if is_valid_room(room_list, checksum):
      sum_ids += int(sector_id)

  return sum_ids

def caesar_shift(sentence, shift):
  shifted = ''
  for ch in sentence:
    shifted += chr((ord(ch.lower()) - 97 + shift) % 26 + 97)
  return shifted

def decrypt_room(room_list, sector_id):
  room_name = [caesar_shift(room, sector_id) for room in room_list]
  return room_name

def find_north_pole(rooms):
  for room in rooms:
    if not room: continue
    room_list = room.strip().split('-')
    sector_id, checksum = room_list.pop().split('[')
    checksum = checksum.replace(']', '')

    decrypted = decrypt_room(room_list, int(sector_id))
    
    if 'north' in ''.join(decrypted):
      print("Located Secret Storage!")
      print(decrypted, sector_id)

print (sum_sector_ids(rooms))
print (find_north_pole(rooms))
