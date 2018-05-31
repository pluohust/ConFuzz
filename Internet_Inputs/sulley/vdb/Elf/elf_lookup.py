"""
ELF static definitions
"""
## EM enumeration definitions

#########################
# valid e_machine types #
#########################
EM_NONE        = 0   # Unknown machine.
EM_M32         = 1   # AT&T WE32100.
EM_SPARC       = 2   # Sun SPARC.
EM_386         = 3   # Intel i386.
EM_68K         = 4   # Motorola 68000.
EM_88K         = 5   # Motorola 88000.
EM_860         = 7   # Intel i860.
EM_MIPS        = 8   # MIPS R3000 Big-Endian only.
EM_S370        = 9   # IBM System/370.
EM_MIPS_RS3_LE = 10  # MIPS R3000 Little-Endian. 
EM_PARISC      = 15  # HP PA-RISC.
EM_VPP500      = 17  # Fujitsu VPP500.
EM_SPARC32PLUS = 18  # SPARC v8plus.
EM_960         = 19  # Intel 80960.
EM_PPC         = 20  # PowerPC 32-bit.
EM_PPC64       = 21  # PowerPC 64-bit.
EM_S390        = 22  # IBM System/390.
EM_V800        = 36  # NEC V800.
EM_FR20        = 37  # Fujitsu FR20.
EM_RH32        = 38  # TRW RH-32.
EM_RCE         = 39  # Motorola RCE.
EM_ARM         = 40  # ARM.
EM_FAKE_ALPHA  = 41  # Digital Alpha
EM_SH          = 42  # Hitachi SH.
EM_SPARCV9     = 43  # SPARC v9 64-bit.
EM_TRICORE     = 44  # Siemens TriCore embedded processor.
EM_ARC         = 45  # Argonaut RISC Core.
EM_H8_300      = 46  # Hitachi H8/300.
EM_H8_300H     = 47  # Hitachi H8/300H.
EM_H8S         = 48  # Hitachi H8S.
EM_H8_500      = 49  # Hitachi H8/500.
EM_IA_64       = 50  # Intel Merced
EM_MIPS_X      = 51  # Stanford MIPS-X
EM_COLDFIRE    = 52  # Motorola Coldfire
EM_68HC12      = 53  # Motorola M68HC12
EM_MMA         = 54  # Fujitsu MMA Multimedia Accelerator
EM_PCP         = 55  # Siemens PCP
EM_NCPU        = 56  # Sony nCPU embeeded RISC
EM_NDR1        = 57  # Denso NDR1 microprocessor
EM_STARCORE    = 58  # Motorola Start*Core processor
EM_ME16        = 59  # Toyota ME16 processor
EM_ST100       = 60  # STMicroelectronic ST100 processor
EM_TINYJ       = 61  # Advanced Logic Corp. Tinyj emb.fam 
EM_X86_64      = 62  # AMD x86-64 architecture 
EM_PDSP        = 63  # Sony DSP Processor 
EM_FX66        = 66  # Siemens FX66 microcontroller
EM_ST9PLUS     = 67  # STMicroelectronics ST9+ 8/16 mc
EM_ST7         = 68  # STmicroelectronics ST7 8 bit mc
EM_68HC16      = 69  # Motorola MC68HC16 microcontroller
EM_68HC11      = 70  # Motorola MC68HC11 microcontroller
EM_68HC08      = 71  # Motorola MC68HC08 microcontroller
EM_68HC05      = 72  # Motorola MC68HC05 microcontroller
EM_SVX         = 73  # Silicon Graphics SVx
EM_ST19        = 74  # STMicroelectronics ST19 8 bit mc
EM_VAX         = 75  # Digital VAX
EM_CRIS        = 76  # Axis Communications 32-bit embedded processor
EM_JAVELIN     = 77  # Infineon Technologies 32-bit embedded processor
EM_FIREPATH    = 78  # Element 14 64-bit DSP Processor
EM_ZSP         = 79  # LSI Logic 16-bit DSP Processor
EM_MMIX        = 80  # Donald Knuth's educational 64-bit processor
EM_HUANY       = 81  # Harvard University machine-independent object files
EM_PRISM       = 82  # SiTera Prism
EM_AVR         = 83  # Atmel AVR 8-bit microcontroller
EM_FR30        = 84  # Fujitsu FR30
EM_D10V        = 85  # Mitsubishi D10V
EM_D30V        = 86  # Mitsubishi D30V
EM_V850        = 87  # NEC v850
EM_M32R        = 88  # Mitsubishi M32R
EM_MN10300     = 89  # Matsushita MN10300
EM_MN10200     = 90  # Matsushita MN10200
EM_PJ          = 91  # picoJava
EM_OPENRISC    = 92  # OpenRISC 32-bit embedded processo
EM_ARC_A5      = 93  # ARC Cores Tangent-A5
EM_XTENSA      = 94  # Tensilica Xtensa Architecture
EM_NUM         = 95  # Alphamosaic VideoCore processor
EM_TMM_GPP     = 96  # Thompson Multimedia General Purpose Proc 
EM_NS32K       = 97  # National Semiconductor 32000 series
EM_TPC         = 98  # Tenor Network TPC processor
EM_SNP1K       = 99  # Trebia SNP 1000 processor
EM_ST200       = 100 # STMicroelectronics ST200 microcontroller
EM_IP2K        = 101 # Ubicom IP2xxx microcontroller family
EM_MAX         = 102 # MAX Processor
EM_CR          = 103 # NatSemi CompactRISC microprocessor
EM_F2MC16      = 104 # Fujitsu F2MC16
EM_MSP430      = 105 # TI embedded microcontroller msp430
EM_BLACKFIN    = 106 # Analog Devices Blackfin (DSP) processor
EM_SE_C33      = 107 # S1C33 Family of Seiko Epson processors
EM_SEP         = 108 # Sharp embedded microprocessor
EM_ARCA        = 109 # Arca RISC Microprocessor
EM_UNICORE     = 110 # Microprocessor series from PKU-Unity Ltd. and MPRC of Peking University
EM_NUM         = 111 # What the fuck is this?!
EM_ALPHA       = 0x9026 # Alpha?

e_machine_types = {
    EM_NONE        : "No Machine",
    EM_M32         : "AT&T WE 32100",
    EM_SPARC       : "Sun SPARC",
    EM_386         : "Intel i386",
    EM_68K         : "Motorola 68k Family",
    EM_88K         : "Motorola 88k Family",
    EM_860         : "Intel i860",
    EM_MIPS        : "MIPS R3000 Big-Endian only",
    EM_S370        : "IBM System/370",
    EM_MIPS_RS3_LE : "MIPS R3000 Little-Endian",
    EM_PARISC      : "HP PA-RISC",
    EM_VPP500      : "Fujitsu VPP500",
    EM_SPARC32PLUS : "SPARC v8plus",
    EM_960         : "Intel 80960",
    EM_PPC         : "PowerPC 32-bit",
    EM_PPC64       : "PowerPC 64-bit",
    EM_S390        : "IBM System/390",
    EM_V800        : "NEC V800",
    EM_FR20        : "Fujitsu FR20",
    EM_RH32        : "TRW RH-32",
    EM_RCE         : "Motorola RCE",
    EM_ARM         : "ARM",
    EM_FAKE_ALPHA  : "Digital Alpha",
    EM_SH          : "Hitachi SH",
    EM_SPARCV9     : "SPARC v9 64-bit",
    EM_TRICORE     : "Siemens TriCore embedded processor",
    EM_ARC         : "Argonaut RISC Core",
    EM_H8_300      : "Hitachi H8/300",
    EM_H8_300H     : "Hitachi H8/300H",
    EM_H8S         : "Hitachi H8S",
    EM_H8_500      : "Hitachi H8/500",
    EM_IA_64       : "Intel Merced",
    EM_MIPS_X      : "Stanford MIPS-X",
    EM_COLDFIRE    : "Motorola Coldfire",
    EM_68HC12      : "Motorola M68HC12",
    EM_MMA         : "Fujitsu MMA Multimedia Accelerator",
    EM_PCP         : "Siemens PCP",
    EM_NCPU        : "Sony nCPU embeeded RISC",
    EM_NDR1        : "Denso NDR1 microprocessor",
    EM_STARCORE    : "Motorola Start*Core processor",
    EM_ME16        : "Toyota ME16 processor",
    EM_ST100       : "STMicroelectronic ST100 processor",
    EM_TINYJ       : "Advanced Logic Corp Tinyj embfam",
    EM_X86_64      : "AMD x86-64 architecture",
    EM_PDSP        : "Sony DSP Processor",
    EM_FX66        : "Siemens FX66 microcontroller",
    EM_ST9PLUS     : "STMicroelectronics ST9+ 8/16 mc",
    EM_ST7         : "STmicroelectronics ST7 8 bit mc",
    EM_68HC16      : "Motorola MC68HC16 microcontroller",
    EM_68HC11      : "Motorola MC68HC11 microcontroller",
    EM_68HC08      : "Motorola MC68HC08 microcontroller",
    EM_68HC05      : "Motorola MC68HC05 microcontroller",
    EM_SVX         : "Silicon Graphics SVx",
    EM_ST19        : "STMicroelectronics ST19 8 bit mc",
    EM_VAX         : "Digital VAX",
    EM_CRIS        : "Axis Communications 32-bit embedded processor",
    EM_JAVELIN     : "Infineon Technologies 32-bit embedded processor",
    EM_FIREPATH    : "Element 14 64-bit DSP Processor",
    EM_ZSP         : "LSI Logic 16-bit DSP Processor",
    EM_MMIX        : "Donald Knuth's educational 64-bit processor",
    EM_HUANY       : "Harvard University machine-independent object files",
    EM_PRISM       : "SiTera Prism",
    EM_AVR         : "Atmel AVR 8-bit microcontroller",
    EM_FR30        : "Fujitsu FR30",
    EM_D10V        : "Mitsubishi D10V",
    EM_D30V        : "Mitsubishi D30V",
    EM_V850        : "NEC v850",
    EM_M32R        : "Mitsubishi M32R",
    EM_MN10300     : "Matsushita MN10300",
    EM_MN10200     : "Matsushita MN10200",
    EM_PJ          : "picoJava",
    EM_OPENRISC    : "OpenRISC 32-bit embedded processo",
    EM_ARC_A5      : "ARC Cores Tangent-A5",
    EM_XTENSA      : "Tensilica Xtensa Architecture",
    EM_NUM         : "Alphamosaic VideoCore processor",
    EM_TMM_GPP     : "Thompson Multimedia General Purpose Proc",
    EM_NS32K       : "National Semiconductor 32000 series",
    EM_TPC         : "Tenor Network TPC processor",
    EM_SNP1K       : "Trebia SNP 1000 processor",
    EM_ST200       : "STMicroelectronics ST200 microcontroller",
    EM_IP2K        : "Ubicom IP2xxx microcontroller family",
    EM_MAX         : "MAX Processor",
    EM_CR          : "NatSemi CompactRISC microprocessor",
    EM_F2MC16      : "Fujitsu F2MC16",
    EM_MSP430      : "TI embedded microcontroller msp430",
    EM_BLACKFIN    : "Analog Devices Blackfin (DSP) processor",
    EM_SE_C33      : "S1C33 Family of Seiko Epson processors",
    EM_SEP         : "Sharp embedded microprocessor",
    EM_ARCA        : "Arca RISC Microprocessor",
    EM_UNICORE     : "Microprocessor series from PKU-Unity Ltd and MPRC of Peking University",
    EM_NUM         : "?",
    EM_ALPHA       : "Alpha",
}

# There are plenty more of these to
# fill in, but...  this is all I need
# for now...
e_machine_32 =  (
    EM_386,
    EM_PPC,
    EM_ARM
)
e_machine_64 =  (
    EM_PPC64,
    EM_SPARCV9,
    EM_X86_64
)

# For future use
# e_machine_32 =  (
#     EM_386,
#     EM_PPC,
#     EM_ARM,
#     EM_M32,
#     EM_SPARC,
#     EM_SPARC32PLUS,
#     EM_68K,
#     EM_88K
# )
# e_machine_64 =  (
#     EM_PPC64,
#     EM_SPARCV9,
#     EM_X86_64,
#     EM_860
# )



####################
# valid e_types #
####################
ET_NONE   = 0     
ET_REL    = 1     
ET_EXEC   = 2     
ET_DYN    = 3     
ET_CORE   = 4     
ET_NUM    = 5     
ET_LOOS   = 0xfe00
ET_HIOS   = 0xfeff
ET_LOPROC = 0xff00
ET_HIPROC = 0xffff

e_types = {
    ET_NONE   : "No file type",
    ET_REL    : "Relocatable file",
    ET_EXEC   : "Executable file",
    ET_DYN    : "Shared object file",
    ET_CORE   : "Core file",
    ET_NUM    : "Number of defined types",
    ET_LOOS   : "OS-specific range start",
    ET_HIOS   : "OS-specific range end",
    ET_LOPROC : "Processor-specific range start",
    ET_HIPROC : "Processor-specific range end",
}

####################
# valid e_versions #
####################
EV_NONE    = 0
EV_CURRENT = 1
EV_NUM     = 2

e_versions = {
    EV_NONE    : "Invalid ELF version",
    EV_CURRENT : "Current version",
    EV_NUM     : "?",
}

###############
# m68k relocs #
###############
R_68K_NONE     = 0
R_68K_32       = 1
R_68K_16       = 2
R_68K_8        = 3
R_68K_PC32     = 4
R_68K_PC16     = 5
R_68K_PC8      = 6
R_68K_GOT32    = 7
R_68K_GOT16    = 8
R_68K_GOT8     = 9
R_68K_GOT32O   = 10
R_68K_GOT16O   = 11
R_68K_GOT8O    = 12
R_68K_PLT32    = 13
R_68K_PLT16    = 14
R_68K_PLT8     = 15
R_68K_PLT32O   = 16
R_68K_PLT16O   = 17
R_68K_PLT8O    = 18
R_68K_COPY     = 19
R_68K_GLOB_DAT = 20
R_68K_JMP_SLOT = 21
R_68K_RELATIVE = 22

e_flags_68k = {
    R_68K_NONE     : "No reloc",
    R_68K_32       : "Direct 32 bit",
    R_68K_16       : "Direct 16 bit",
    R_68K_8        : "Direct 8 bit",
    R_68K_PC32     : "PC relative 32 bit",
    R_68K_PC16     : "PC relative 16 bit",
    R_68K_PC8      : "PC relative 8 bit",
    R_68K_GOT32    : "32 bit PC relative GOT entry",
    R_68K_GOT16    : "16 bit PC relative GOT entry",
    R_68K_GOT8     : "8 bit PC relative GOT entry",
    R_68K_GOT32O   : "32 bit GOT offset",
    R_68K_GOT16O   : "16 bit GOT offset",
    R_68K_GOT8O    : "8 bit GOT offset",
    R_68K_PLT32    : "32 bit PC relative PLT address",
    R_68K_PLT16    : "16 bit PC relative PLT address",
    R_68K_PLT8     : "8 bit PC relative PLT address",
    R_68K_PLT32O   : "32 bit PLT offset",
    R_68K_PLT16O   : "16 bit PLT offset",
    R_68K_PLT8O    : "8 bit PLT offset",
    R_68K_COPY     : "Copy symbol at runtime",
    R_68K_GLOB_DAT : "Create GOT entry",
    R_68K_JMP_SLOT : "Create PLT entry",
    R_68K_RELATIVE : "Adjust by program base",
} 

###############
# i386 relocs #
###############
R_386_NONE         = 0
R_386_32           = 1
R_386_PC32         = 2
R_386_GOT32        = 3
R_386_PLT32        = 4
R_386_COPY         = 5
R_386_GLOB_DAT     = 6
R_386_JMP_SLOT     = 7
R_386_RELATIVE     = 8
R_386_GOTOFF       = 9
R_386_GOTPC        = 10
R_386_32PLT        = 11
R_386_TLS_TPOFF    = 14
R_386_TLS_IE       = 15
R_386_TLS_GOTIE    = 16
R_386_TLS_LE       = 17
R_386_TLS_GD       = 18
R_386_TLS_LDM      = 19
R_386_16           = 20
R_386_PC16         = 21
R_386_8            = 22
R_386_PC8          = 23
R_386_TLS_GD_32    = 24
R_386_TLS_GD_PUSH  = 25
R_386_TLS_GD_CALL  = 26
R_386_TLS_GD_POP   = 27
R_386_TLS_LDM_32   = 28
R_386_TLS_LDM_PUSH = 29
R_386_TLS_LDM_CALL = 30
R_386_TLS_LDM_POP  = 31
R_386_TLS_LDO_32   = 32
R_386_TLS_IE_32    = 33
R_386_TLS_LE_32    = 34
R_386_TLS_DTPMOD32 = 35
R_386_TLS_DTPOFF32 = 36
R_386_TLS_TPOFF32  = 37

r_types_386 = {
    R_386_NONE         : "No reloc",
    R_386_32           : "Direct 32 bit",
    R_386_PC32         : "PC relative 32 bit",
    R_386_GOT32        : "32 bit GOT entry",
    R_386_PLT32        : "32 bit PLT address",
    R_386_COPY         : "Copy symbol at runtime",
    R_386_GLOB_DAT     : "Create GOT entry",
    R_386_JMP_SLOT     : "Create PLT entry",
    R_386_RELATIVE     : "Adjust by program base",
    R_386_GOTOFF       : "32 bit offset to GOT",
    R_386_GOTPC        : "32 bit PC relative offset to GOT",
    R_386_32PLT        : "?",
    R_386_TLS_TPOFF    : "Offset in static TLS block",
    R_386_TLS_IE       : "Address of GOT entry for static",
    R_386_TLS_GOTIE    : "GOT entry for static TLS",
    R_386_TLS_LE       : "Offset relative to static",
    R_386_TLS_GD       : "Direct 32 bit for GNU version",
    R_386_TLS_LDM      : "Direct 32 bit for GNU version",
    R_386_16           : "?",
    R_386_PC16         : "?",
    R_386_8            : "?",
    R_386_PC8          : "?",
    R_386_TLS_GD_32    : "Direct 32 bit for general",
    R_386_TLS_GD_PUSH  : "Tag for pushl in GD TLS code",
    R_386_TLS_GD_CALL  : "Relocation for call",
    R_386_TLS_GD_POP   : "Tag for popl in GD TLS code",
    R_386_TLS_LDM_32   : "Direct 32 bit for local",
    R_386_TLS_LDM_PUSH : "Tag for pushl in LDM TLS code",
    R_386_TLS_LDM_CALL : "Relocation for call",
    R_386_TLS_LDM_POP  : "Tag for popl in LDM TLS code",
    R_386_TLS_LDO_32   : "Offset relative to TLS block",
    R_386_TLS_IE_32    : "GOT entry for negated static",
    R_386_TLS_LE_32    : "Negated offset relative to",
    R_386_TLS_DTPMOD32 : "ID of module containing symbol",
    R_386_TLS_DTPOFF32 : "Offset in TLS block",
    R_386_TLS_TPOFF32  : "Negated offset in static TLS block",
}

##########################
# AMD x86-64 relocations #
##########################
R_X86_64_NONE        = 0
R_X86_64_64          = 1
R_X86_64_PC32        = 2
R_X86_64_GOT32       = 3
R_X86_64_PLT32       = 4
R_X86_64_COPY        = 5
R_X86_64_GLOB_DAT    = 6
R_X86_64_JUMP_SLOT   = 7
R_X86_64_RELATIVE    = 8
R_X86_64_GOTPCREL    = 9
R_X86_64_32          = 10
R_X86_64_32S         = 11
R_X86_64_16          = 12
R_X86_64_PC16        = 13
R_X86_64_8           = 14
R_X86_64_PC8         = 15
R_X86_64_DTPMOD64    = 16
R_X86_64_DTPOFF64    = 17
R_X86_64_TPOFF64     = 18
R_X86_64_TLSGD       = 19
R_X86_64_TLSLD       = 20
R_X86_64_DTPOFF32    = 21
R_X86_64_GOTTPOFF    = 22
R_X86_64_TPOFF32     = 23
R_X86_64_NUM         = 24

r_types_amd64 = {
    R_X86_64_NONE       : 'No reloc',
    R_X86_64_64         : 'Direct 64 bit ',
    R_X86_64_PC32       : 'PC relative 32 bit signed',
    R_X86_64_GOT32      : '32 bit GOT entry',
    R_X86_64_PLT32      : '32 bit PLT address',
    R_X86_64_COPY       : 'Copy symbol at runtime',
    R_X86_64_GLOB_DAT   : 'Create GOT entry',
    R_X86_64_JUMP_SLOT  : 'Create PLT entry',
    R_X86_64_RELATIVE   : 'Adjust by program base',
    R_X86_64_GOTPCREL   : '32 bit signed PC relative offset to GOT',
    R_X86_64_32         : 'Direct 32 bit zero extended',
    R_X86_64_32S        : 'Direct 32 bit sign extended',
    R_X86_64_16         : 'Direct 16 bit zero extended',
    R_X86_64_PC16       : '16 bit sign extended pc relative',
    R_X86_64_8          : 'Direct 8 bit sign extended ',
    R_X86_64_PC8        : '8 bit sign extended pc relative',
    R_X86_64_DTPMOD64   : 'ID of module containing symbol',
    R_X86_64_DTPOFF64   : 'Offset in modules TLS block',
    R_X86_64_TPOFF64    : 'Offset in initial TLS block',
    R_X86_64_TLSGD      : '32 bit signed PC relative offset to two GOT entries for GD symbol',
    R_X86_64_TLSLD      : '32 bit signed PC relative offset to two GOT entries for LD symbol',
    R_X86_64_DTPOFF32   : 'Offset in TLS block',
    R_X86_64_GOTTPOFF   : '32 bit signed PC relative offset to GOT entry for IE symbol',
    R_X86_64_TPOFF32    : 'Offset in initial TLS block',
}

############################
# Special section indicies #
############################
SHN_UNDEF     0      # Undefined section
SHN_LORESERVE 0xff00 # Start of reserved indices
SHN_LOPROC    0xff00 # Start of processor-specific
SHN_BEFORE    0xff00 # Order section before all others (Solaris)
SHN_AFTER     0xff01 # Order section after all others (Solaris)
SHN_HIPROC    0xff1f # End of processor-specific
SHN_LOOS      0xff20 # Start of OS-specific
SHN_HIOS      0xff3f # End of OS-specific
SHN_ABS       0xfff1 # Associated symbol is absolute
SHN_COMMON    0xfff2 # Associated symbol is common
SHN_XINDEX    0xffff # Index is in extra table
SHN_HIRESERVE 0xffff # End of reserved indices

sh_name = {
    SHN_UNDEF       : "Undefined section",
    SHN_LORESERVE   : "Start of reserved indices",
    SHN_LOPROC      : "Start of processor-specific",
    SHN_BEFORE      : "Order section before all others (Solaris)",
    SHN_AFTER       : "Order section after all others (Solaris)",
    SHN_HIPROC      : "End of processor-specific",
    SHN_LOOS        : "Start of OS-specific",
    SHN_HIOS        : "End of OS-specific",
    SHN_ABS         : "Associated symbol is absolute",
    SHN_COMMON      : "Associated symbol is common",
    SHN_XINDEX      : "Index is in extra table",
    SHN_HIRESERVE   : "End of reserved indices",
}

########################
# valid sh_type values #
########################
SHT_NULL          = 0
SHT_PROGBITS      = 1
SHT_SYMTAB        = 2
SHT_STRTAB        = 3
SHT_RELA          = 4
SHT_HASH          = 5
SHT_DYNAMIC       = 6
SHT_NOTE          = 7
SHT_NOBITS        = 8
SHT_REL           = 9
SHT_SHLIB         = 10
SHT_DYNSYM        = 11
SHT_INIT_ARRAY    = 14
SHT_FINI_ARRAY    = 15
SHT_PREINIT_ARRAY = 16
SHT_GROUP         = 17
SHT_SYMTAB_SHNDX  = 18
SHT_NUM           = 19
SHT_LOOS          = 0x60000000
SHT_GNU_LIBLIST   = 0x6ffffff7
SHT_CHECKSUM      = 0x6ffffff8
SHT_LOSUNW        = 0x6ffffffa
SHT_SUNW_move     = SHT_LOSUNW
SHT_SUNW_COMDAT   = 0x6ffffffb
SHT_SUNW_syminfo  = 0x6ffffffc
SHT_GNU_verdef    = 0x6ffffffd
SHT_GNU_verneed   = 0x6ffffffe
SHT_GNU_versym    = 0x6fffffff
SHT_HISUNW        = 0x6fffffff
SHT_HIOS          = 0x6fffffff
SHT_LOPROC        = 0x70000000
SHT_HIPROC        = 0x7fffffff
SHT_LOUSER        = 0x80000000
SHT_HIUSER        = 0x8fffffff

sh_type = {
    SHT_NULL          : "Section header table entry unused",
    SHT_PROGBITS      : "Program data",
    SHT_SYMTAB        : "Symbol table",
    SHT_STRTAB        : "String table",
    SHT_RELA          : "Relocation entries with addends",
    SHT_HASH          : "Symbol hash table",
    SHT_DYNAMIC       : "Dynamic linking information",
    SHT_NOTE          : "Notes",
    SHT_NOBITS        : "Program space with no data (bss)",
    SHT_REL           : "Relocation entries, no addends",
    SHT_SHLIB         : "Reserved",
    SHT_DYNSYM        : "Dynamic linker symbol table",
    SHT_INIT_ARRAY    : "Array of constructors",
    SHT_FINI_ARRAY    : "Array of destructors",
    SHT_PREINIT_ARRAY : "Array of pre-constructors",
    SHT_GROUP         : "Section group",
    SHT_SYMTAB_SHNDX  : "Extended section indeces",
    SHT_NUM           : "Number of defined types",
    SHT_LOOS          : "Start OS-specific",
    SHT_GNU_LIBLIST   : "Prelink library list",
    SHT_CHECKSUM      : "Checksum for DSO content.",
    SHT_LOSUNW        : "Sun-specific low bound.",
    SHT_SUNW_move     : "?",
    SHT_SUNW_COMDAT   : "?",
    SHT_SUNW_syminfo  : "?",
    SHT_GNU_verdef    : "Version definition section.",
    SHT_GNU_verneed   : "Version needs section.",
    SHT_GNU_versym    : "Version symbol table.",
    SHT_HISUNW        : "Sun-specific high bound.",
    SHT_HIOS          : "End OS-specific type",
    SHT_LOPROC        : "Start of processor-specific",
    SHT_HIPROC        : "End of processor-specific",
    SHT_LOUSER        : "Start of application-specific",
    SHT_HIUSER        : "End of application-specific",
}

#########################
# valid sh_flags values #
#########################
SHF_WRITE            = (1 << 0)   # 1
SHF_ALLOC            = (1 << 1)   # 2
SHF_EXECINSTR        = (1 << 2)   # 4
SHF_MERGE            = (1 << 4)   # 16
SHF_STRINGS          = (1 << 5)   # 32
SHF_INFO_LINK        = (1 << 6)   # 64
SHF_LINK_ORDER       = (1 << 7)   # 128
SHF_OS_NONCONFORMING = (1 << 8)   # 256
SHF_GROUP            = (1 << 9)   # 512
SHF_TLS              = (1 << 10)  # 1024
SHF_MASKOS           = 0x0ff00000 # 267386880  
SHF_MASKPROC         = 0xf0000000 # 4026531840 
SHF_ORDERED          = (1 << 30)  # 1073741824
SHF_EXCLUDE          = (1 << 31)  # 2147483648

sh_flags = {
    SHF_WRITE            : "Writable",
    SHF_ALLOC            : "Occupies memory during execution",
    SHF_EXECINSTR        : "Executable",
    SHF_MERGE            : "Might be merged",
    SHF_STRINGS          : "Contains nul-terminated strings",
    SHF_INFO_LINK        : "'sh_info' contains SHT index",
    SHF_LINK_ORDER       : "Preserve order after combining",
    SHF_OS_NONCONFORMING : "Non-standard OS specific",
    SHF_GROUP            : "Section is member of a group.",
    SHF_TLS              : "Section hold thread-local data.",
    SHF_MASKOS           : "OS-specific",
    SHF_MASKPROC         : "Processor-specific",
    SHF_ORDERED          : "Special ordering",
    SHF_EXCLUDE          : "Section is excluded",
}

#####################################
# valid ST_BIND subfield of st_info #
#####################################
STB_LOCAL  = 0
STB_GLOBAL = 1
STB_WEAK   = 2
STB_NUM    = 3
STB_LOOS   = 10
STB_HIOS   = 12
STB_LOPROC = 13
STB_HIPROC = 15

st_info_bind = {
    STB_LOCAL  : "Local symbol",
    STB_GLOBAL : "Global symbol",
    STB_WEAK   : "Weak symbol",
    STB_NUM    : "Number of defined types.",
    STB_LOOS   : "Start of OS-specific",
    STB_HIOS   : "End of OS-specific",
    STB_LOPROC : "Start of processor-specific",
    STB_HIPROC : "End of processor-specific",
}

#####################################
# valid ST_TYPE subfield of st_info #
#####################################
STT_NOTYPE  = 0
STT_OBJECT  = 1
STT_FUNC    = 2
STT_SECTION = 3
STT_FILE    = 4
STT_COMMON  = 5
STT_TLS     = 6
STT_NUM     = 7
STT_LOOS    = 10
STT_HIOS    = 12
STT_LOPROC  = 13
STT_HIPROC  = 15

st_info_type = {
    STT_NOTYPE  : "Symbol type is unspecified",
    STT_OBJECT  : "Symbol is a data object",
    STT_FUNC    : "Symbol is a code object",
    STT_SECTION : "Symbol associated with a section",
    STT_FILE    : "Symbol's name is file name",
    STT_COMMON  : "Symbol is a common data object",
    STT_TLS     : "Symbol is thread-local data",
    STB_NUM     : "Number of defined types.",
    STT_LOOS    : "Start of OS-specific",
    STT_HIOS    : "End of OS-specific",
    STT_LOPROC  : "Start of processor-specific",
    STT_HIPROC  : "End of processor-specific",
}

######################
# valid d_tag values #
######################
DT_NULL            = 0 
DT_NEEDED          = 1 
DT_PLTRELSZ        = 2 
DT_PLTGOT          = 3 
DT_HASH            = 4 
DT_STRTAB          = 5 
DT_SYMTAB          = 6 
DT_RELA            = 7 
DT_RELASZ          = 8 
DT_RELAENT         = 9 
DT_STRSZ           = 10 
DT_SYMENT          = 11 
DT_INIT            = 12 
DT_FINI            = 13 
DT_SONAME          = 14 
DT_RPATH           = 15 
DT_SYMBOLIC        = 16 
DT_REL             = 17 
DT_RELSZ           = 18 
DT_RELENT          = 19 
DT_PLTREL          = 20 
DT_DEBUG           = 21 
DT_TEXTREL         = 22 
DT_JMPREL          = 23 
DT_BIND_NOW        = 24 
DT_INIT_ARRAY      = 25 
DT_FINI_ARRAY      = 26 
DT_INIT_ARRAYSZ    = 27 
DT_FINI_ARRAYSZ    = 28 
DT_RUNPATH         = 29 
DT_FLAGS           = 30 
DT_ENCODING        = 32 
DT_PREINIT_ARRAY   = 32 
DT_PREINIT_ARRAYSZ = 33 
DT_NUM             = 34 
DT_VALRNGLO        = 0x6ffffd00 
DT_GNU_PRELINKED   = 0x6ffffdf5 
DT_GNU_CONFLICTSZ  = 0x6ffffdf6 
DT_GNU_LIBLISTSZ   = 0x6ffffdf7 
DT_CHECKSUM        = 0x6ffffdf8 
DT_PLTPADSZ        = 0x6ffffdf9 
DT_MOVEENT         = 0x6ffffdfa 
DT_MOVESZ          = 0x6ffffdfb 
DT_FEATURE_1       = 0x6ffffdfc 
DT_POSFLAG_1       = 0x6ffffdfd 
DT_SYMINSZ         = 0x6ffffdfe 
DT_SYMINENT        = 0x6ffffdff 
DT_VALRNGHI        = 0x6ffffdff 
DT_GNU_HASH        = 0x6ffffef5 
DT_TLSDESC_PLT     = 0x6ffffef6 
DT_TLSDESC_GOT     = 0x6ffffef7 
DT_GNU_CONFLICT    = 0x6ffffef8 
DT_GNU_LIBLIST     = 0x6ffffef9 
DT_CONFIG          = 0x6ffffefa 
DT_DEPAUDIT        = 0x6ffffefb 
DT_AUDIT           = 0x6ffffefc 
DT_PLTPAD          = 0x6ffffefd 
DT_MOVETAB         = 0x6ffffefe 
DT_SYMINFO         = 0x6ffffeff 
DT_VERSYM          = 0x6ffffff0 
DT_RELACOUNT       = 0x6ffffff9 
DT_RELCOUNT        = 0x6ffffffa 
DT_FLAGS_1         = 0x6ffffffb 
DT_VERDEF          = 0x6ffffffc 
DT_VERDEFNUM       = 0x6ffffffd 
DT_VERNEED         = 0x6ffffffe 
DT_VERNEEDNUM      = 0x6fffffff 
DT_AUXILIARY       = 0x7ffffffd 
DT_FILTER          = 0x7fffffff 
DT_LOOS            = 0x6000000d 
DT_HIOS            = 0x6ffff000 
DT_LOPROC          = 0x70000000 
DT_HIPROC          = 0x7fffffff
#DT_PROCNUM         = DT_MIPS_NUM

dt_types = {
    DT_NULL            : "Marks end of dynamic section",
    DT_NEEDED          : "Name of needed library",
    DT_PLTRELSZ        : "Size in bytes of PLT relocs",
    DT_PLTGOT          : "Processor defined value",
    DT_HASH            : "Address of symbol hash table",
    DT_STRTAB          : "Address of string table",
    DT_SYMTAB          : "Address of symbol table",
    DT_RELA            : "Address of Rela relocs",
    DT_RELASZ          : "Total size of Rela relocs",
    DT_RELAENT         : "Size of one Rela reloc",
    DT_STRSZ           : "Size of string table",
    DT_SYMENT          : "Size of one symbol table entry",
    DT_INIT            : "Address of init function",
    DT_FINI            : "Address of termination function",
    DT_SONAME          : "Name of shared object",
    DT_RPATH           : "Library search path (deprecated)",
    DT_SYMBOLIC        : "Start symbol search here",
    DT_REL             : "Address of Rel relocs",
    DT_RELSZ           : "Total size of Rel relocs",
    DT_RELENT          : "Size of one Rel reloc",
    DT_PLTREL          : "Type of reloc in PLT",
    DT_DEBUG           : "For debugging; unspecified",
    DT_TEXTREL         : "Reloc might modify .text",
    DT_JMPREL          : "Address of PLT relocs",
    DT_BIND_NOW        : "Process relocations of object",
    DT_INIT_ARRAY      : "Array with addresses of init fct",
    DT_FINI_ARRAY      : "Array with addresses of fini fct",
    DT_INIT_ARRAYSZ    : "Size in bytes of DT_INIT_ARRAY",
    DT_FINI_ARRAYSZ    : "Size in bytes of DT_FINI_ARRAY",
    DT_RUNPATH         : "Library search path",
    DT_FLAGS           : "Flags for the object being loaded",
    DT_ENCODING        : "Start of encoded range",
    DT_PREINIT_ARRAY   : "Array with addresses of preinit fct",
    DT_PREINIT_ARRAYSZ : "size in bytes of DT_PREINIT_ARRAY",
    DT_NUM             : "Number used",
    DT_VALRNGLO        : "?",
    DT_GNU_PRELINKED   : "Prelinking timestamp",
    DT_GNU_CONFLICTSZ  : "Size of conflict section",
    DT_GNU_LIBLISTSZ   : "Size of library list",
    DT_CHECKSUM        : "Elf Checksum",
    DT_PLTPADSZ        : "?",
    DT_MOVEENT         : "?",
    DT_MOVESZ          : "?",
    DT_FEATURE_1       : "Feature selection (DTF_*)",
    DT_POSFLAG_1       : "Flags for DT_* entries, effecting the following DT_* entry",
    DT_SYMINSZ         : "Size of syminfo table (in bytes)",
    DT_SYMINENT        : "Entry size of syminfo",
    DT_VALRNGHI        : "?",
    DT_GNU_HASH        : "Address of gnu-style symbol hash table",
    DT_TLSDESC_PLT     : "?",
    DT_TLSDESC_GOT     : "?",
    DT_GNU_CONFLICT    : "Start of conflict section",
    DT_GNU_LIBLIST     : "Library List",
    DT_CONFIG          : "Configuration information",
    DT_DEPAUDIT        : "Dependency auditing",
    DT_AUDIT           : "Object auditing",
    DT_PLTPAD          : "PLT padding",
    DT_MOVETAB         : "Move table",
    DT_SYMINFO         : "Syminfo table",
    DT_VERSYM          : "?",
    DT_RELACOUNT       : "?",
    DT_RELCOUNT        : "?",
    DT_FLAGS_1         : "State flags, see DF_1_*",
    DT_VERDEF          : "Address of version definition table",
    DT_VERDEFNUM       : "Number of version definitions",
    DT_VERNEED         : "Address of table with needed versions",
    DT_VERNEEDNUM      : "Number of needed versions",
    DT_AUXILIARY       : "Shared object to load before self",
    DT_FILTER          : "Shared object to get values from",
    DT_LOOS            : "Start of OS-specific",
    DT_HIOS            : "End of OS-specific",
    DT_LOPROC          : "Start of processor-specific",
    DT_HIPROC          : "End of processor-specific",
    #DT_PROCNUM        : "Most used by any processor",
}

#######################
# valid p_type values #
#######################
PT_NULL         = 0
PT_LOAD         = 1
PT_DYNAMIC      = 2
PT_INTERP       = 3
PT_NOTE         = 4
PT_SHLIB        = 5
PT_PHDR         = 6
PT_TLS          = 7
PT_NUM          = 8
PT_LOOS         = 0x60000000
PT_GNU_EH_FRAME = 0x6474e550
PT_GNU_STACK    = 0x6474e551
PT_GNU_RELRO    = 0x6474e552
PT_LOSUNW       = 0x6ffffffa
PT_SUNWBSS      = 0x6ffffffa
PT_SUNWSTACK    = 0x6ffffffb
PT_HISUNW       = 0x6fffffff
PT_HIOS         = 0x6fffffff
PT_LOPROC       = 0x70000000
PT_HIPROC       = 0x7fffffff

ph_types = {
    PT_NULL         : "Program header table entry unused",
    PT_LOAD         : "Loadable program segment",
    PT_DYNAMIC      : "Dynamic linking information",
    PT_INTERP       : "Program interpreter",
    PT_NOTE         : "Auxiliary information",
    PT_SHLIB        : "Reserved",
    PT_PHDR         : "Entry for header table itself",
    PT_TLS          : "Thread-local storage segment",
    PT_NUM          : "Number of defined types",
    PT_LOOS         : "Start of OS-specific",
    PT_GNU_EH_FRAME : "GCC .eh_frame_hdr segment",
    PT_GNU_STACK    : "Indicates stack executability",
    PT_GNU_RELRO    : "Read-only after relocation",
    PT_SUNWBSS      : "Sun Specific segment",
    PT_SUNWSTACK    : "Stack segment",
    PT_HIOS         : "End of OS-specific",
    PT_LOPROC       : "Start of processor-specific",
    PT_HIPROC       : "End of processor-specific"
}
