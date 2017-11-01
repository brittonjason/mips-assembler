import argparse
import instructions as command

parser = argparse.ArgumentParser()
parser.add_argument('file', help='input file')
args = parser.parse_args()

try:
    input_file = open(args.file, 'r')
except:
    print("Error opening file for read")
    raise


def print_error(line_number, faulty_instr):
    print("Cannot assemble", faulty_instr, "at line", line_number)


def check_errors():
    error = False
    line_number = 1

    for line in input_file:
        try:
            if line.rstrip()[-1] == ':':
                label_locations[line.split(':')[0]] = line_number
            elif line[0] == '\t' and len(line.strip().split('\t')) == 2:
                a = [x.strip() for x in line.strip().split('\t')[1].split(',')]
                for i in a:
                    if '(' in i:
                        i = i.split('(')[1][:-1]
                    if command.register_to_bin(i) == 'xxxxx' and i[0] == '$':
                        print_error(line_number, line)
                        error = True
                line_number += 1
            else:
                print_error(line_number, line)
                error = True
        except:
            print_error(line_number, line)
            error = True

    return error


def read_assembly():
    line_number = 1

    for line in input_file:
        if line.rstrip()[-1] == ':':
            label_locations[line.split(':')[0]] = line_number
        elif line[0] == '\t':
            parse_instr(line, line_number)
            line_number += 1
        else:
            print("Error not caught")
            raise


def parse_instr(instr, line_number):
    i = instr.strip().split('\t')
    comm = i[0]
    param = i[1]

    if comm == 'add': out_file.write(command.madd(param) + '\n')
    elif comm == 'addi': out_file.write(command.maddi(param) + '\n')
    elif comm == 'addiu': out_file.write(command.maddiu(param) + '\n')
    elif comm == 'addu': out_file.write(command.maddu(param) + '\n')
    elif comm == 'and': out_file.write(command.mand(param) + '\n')
    elif comm == 'andi': out_file.write(command.mandi(param) + '\n')
    elif comm == 'beq': out_file.write(command.mbeq(param, line_number, label_locations) + '\n')
    elif comm == 'bne': out_file.write(command.mbne(param, line_number, label_locations) + '\n')
    elif comm == 'jr': out_file.write(command.mjr(param) + '\n')
    elif comm == 'lbu': out_file.write(command.mlbu(param) + '\n')
    elif comm == 'lhu': out_file.write(command.mlhu(param) + '\n')
    elif comm == 'll': out_file.write(command.mll(param) + '\n')
    elif comm == 'lui': out_file.write(command.mlui(param) + '\n')
    elif comm == 'lw': out_file.write(command.mlw(param) + '\n')
    elif comm == 'nor': out_file.write(command.mnor(param) + '\n')
    elif comm == 'or': out_file.write(command.mor(param) + '\n')
    elif comm == 'ori': out_file.write(command.mori(param) + '\n')
    elif comm == 'slt': out_file.write(command.mslt(param) + '\n')
    elif comm == 'slti': out_file.write(command.mslti(param) + '\n')
    elif comm == 'sltiu': out_file.write(command.msltiu(param) + '\n')
    elif comm == 'sltu': out_file.write(command.msltu(param) + '\n')
    elif comm == 'sll': out_file.write(command.msll(param) + '\n')
    elif comm == 'srl' : out_file.write(command.msrl(param) + '\n')
    elif comm == 'sb': out_file.write(command.msb(param) + '\n')
    elif comm == 'sc': out_file.write(command.msc(param) + '\n')
    elif comm == 'sh': out_file.write(command.msh(param) + '\n')
    elif comm == 'sw': out_file.write(command.msw(param) + '\n')
    elif comm == 'sub': out_file.write(command.msub(param) + '\n')
    elif comm == 'subu': out_file.write(command.msubu(param) + '\n')


start_file = input_file.tell()
label_locations = {}

if not check_errors():
    input_file.seek(start_file)
    file_name = args.file.split('.')[0] + '.obj'
    try:
        out_file = open(file_name, 'w')
    except:
        print("Error opening file for write")
        raise
    read_assembly()
    input_file.close()
    out_file.close()
