# %%
from collections import Counter
from functools import reduce
# %%
with open('input.txt', 'r') as f:
    data = f.read()
# %%
def convert_hex_to_bin(hex_str):
    return format(int(hex_str, 16), "b").zfill(len(hex_str) * 4)

assert convert_hex_to_bin('D2FE28') == '110100101111111000101000', "Test failed"
assert (binary := convert_hex_to_bin("38006F45291200")) == '00111000000000000110111101000101001010010001001000000000', f"Test failed: {binary}"
assert convert_hex_to_bin("EE00D40C823060") == "11101110000000001101010000001100100000100011000001100000", "Test failed"
# %%

def parse_packet(binary, version_counter=None):
    version = binary[:3]
    if version_counter is not None:
        version_counter["vers"] += int(version, 2)
    packet_type = binary[3:6]
    packet_info = binary[6:]

    if packet_type == '100':
        binary_literal = ""
        while packet_info.startswith('1'):
            binary_literal += packet_info[1:5]
            packet_info = packet_info[5:]
        binary_literal += packet_info[1:5]

        return int(binary_literal, 2), packet_info[5:]
    else:
        packets = []

        if packet_info.startswith('0'):
            length = int(packet_info[1:16], 2)
            packet_info = packet_info[16:]
            
            packet_info_length = len(packet_info)

            while packet_info_length - len(packet_info) < length:
                literal, remaining_packet_info = parse_packet(packet_info, version_counter)
                packets.append(literal)
                packet_info = remaining_packet_info
        else:
            sub_package_count = int(packet_info[1:12], 2)
            packet_info = packet_info[12:]

            while sub_package_count > 0:
                sub_package_count -= 1
                literal, remaining_packet_info = parse_packet(packet_info, version_counter)
                packets.append(literal)
                packet_info = remaining_packet_info
       
        result = 0

        if packet_type == '000':
            result = sum(packets)
        elif packet_type == '001':
            result = reduce(lambda x, y: x * y, packets)
        elif packet_type == '010':
            result = min(packets)
        elif packet_type == '011':
            result = max(packets)
        elif packet_type == '101':
            result = 1 if packets[0] > packets[1] else 0
        elif packet_type == '110':
            result = 1 if packets[0] < packets[1] else 0
        elif packet_type == '111':
            result = 1 if packets[0] == packets[1] else 0

        return result, packet_info
        
assert (literal := parse_packet(convert_hex_to_bin('D2FE28')))[0] == 2021, f"Test failed: {literal}"
# %%
parse_packet(convert_hex_to_bin("38006F45291200"))
# %%
parse_packet(convert_hex_to_bin("EE00D40C823060"))
# %%
C = Counter()
parse_packet(convert_hex_to_bin("8A004A801A8002F478"), C)
assert C["vers"] == 16, "Test failed"
C = Counter()
parse_packet(convert_hex_to_bin("C0015000016115A2E0802F182340"), C)
assert C["vers"] == 23, "Test failed"
C = Counter()
parse_packet(convert_hex_to_bin("A0016C880162017C3686B18A3D4780"), C)
assert C["vers"] == 31, "Test failed"

# %%
C = Counter()
parse_packet(convert_hex_to_bin(data), C)
C["vers"]
# %%
####### Part 2 #######
assert parse_packet(convert_hex_to_bin("C200B40A82"))[0] == 3, "Test failed"
assert parse_packet(convert_hex_to_bin("04005AC33890"))[0] == 54, "Test failed"
assert parse_packet(convert_hex_to_bin("880086C3E88112"))[0] == 7, "Test failed"
assert parse_packet(convert_hex_to_bin("CE00C43D881120"))[0] == 9, "Test failed"
assert parse_packet(convert_hex_to_bin("D8005AC2A8F0"))[0] == 1, "Test failed"
assert parse_packet(convert_hex_to_bin("F600BC2D8F"))[0] == 0, "Test failed"
assert parse_packet(convert_hex_to_bin("9C005AC2F8F0"))[0] == 0, "Test failed"
assert parse_packet(convert_hex_to_bin("9C0141080250320F1802104A08"))[0] == 1, "Test failed"
# %%
parse_packet(convert_hex_to_bin(data))[0]
# %%
