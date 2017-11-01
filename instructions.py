def register_to_bin(reg):
    return {
        '$zero': '{0:05b}'.format(0),
        '$0' : '{0:05b}'.format(0),
        '$v0': '{0:05b}'.format(2),
        '$v1': '{0:05b}'.format(3),
        '$a0': '{0:05b}'.format(4),
        '$a1': '{0:05b}'.format(5),
        '$a2': '{0:05b}'.format(6),
        '$a3': '{0:05b}'.format(7),
        '$t0': '{0:05b}'.format(8),
        '$t1': '{0:05b}'.format(9),
        '$t2': '{0:05b}'.format(10),
        '$t3': '{0:05b}'.format(11),
        '$t4': '{0:05b}'.format(12),
        '$t5': '{0:05b}'.format(13),
        '$t6': '{0:05b}'.format(14),
        '$t7': '{0:05b}'.format(15),
        '$s0': '{0:05b}'.format(16),
        '$s1': '{0:05b}'.format(17),
        '$s2': '{0:05b}'.format(18),
        '$s3': '{0:05b}'.format(19),
        '$s4': '{0:05b}'.format(20),
        '$s5': '{0:05b}'.format(21),
        '$s6': '{0:05b}'.format(22),
        '$s7': '{0:05b}'.format(23),
        '$t8': '{0:05b}'.format(24),
        '$t9': '{0:05b}'.format(25),
    }.get(reg, 'xxxxx')


def madd(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "100000"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def maddi(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "001000"
    rt = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    immediate = "{0:016b}".format(int(a[2]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def maddiu(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "001001"
    rt = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    immediate = "{0:016b}".format(int(a[2]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def maddu(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "100001"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mand(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "100100"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mandi(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "001100"
    rt = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    immediate = "{0:016b}".format(int(a[2]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mbeq(params):
    return "not implemented"


def mbne(params):
    return "not implemented"


def mjr(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = "00000"
    rs = register_to_bin(a[0])
    rt = "00000"
    shamt = "00000"
    funct = "001000"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mlbu(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "100100"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mlhu(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "100101"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mll(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "110000"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mlui(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "001111"
    rt = register_to_bin(a[0])
    rs = "00000"
    immediate = "{0:016b}".format(int(a[1]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mlw(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "100011"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mnor(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "100111"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mor(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "100101"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mori(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "001101"
    rt = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    immediate = "{0:016b}".format(int(a[2]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mslt(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "101010"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def mslti(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "001010"
    rt = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    immediate = "{0:016b}".format(int(a[2]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msltiu(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "001011"
    rt = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    immediate = "{0:016b}".format(int(a[2]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msltu(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "101011"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msll(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = "00000"
    rt = register_to_bin(a[1])
    shamt = "{0:05b}".format(int(a[2]))
    funct = "000000"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msrl(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = "00000"
    rt = register_to_bin(a[1])
    shamt = "{0:05b}".format(int(a[2]))
    funct = "000010"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msb(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "101000"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msc(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "111000"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msh(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "101001"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msw(params):
    a = [x.strip() for x in params.split(',')]
    b = a[1].split('(')
    opcode = "101011"
    rt = register_to_bin(a[0])
    rs = register_to_bin(b[1][:-1])
    immediate = "{0:016b}".format(int(b[0]))
    machine_bin = opcode + rs + rt + immediate
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msub(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "100010"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)


def msubu(params):
    a = [x.strip() for x in params.split(',')]
    opcode = "000000"
    rd = register_to_bin(a[0])
    rs = register_to_bin(a[1])
    rt = register_to_bin(a[2])
    shamt = "00000"
    funct = "100011"
    machine_bin = opcode + rs + rt + rd + shamt + funct
    return hex(int(machine_bin, 2))[2:].zfill(8)
