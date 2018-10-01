{
    "targets": [
        {
            "target_name": "cryptonight-hashing",
            "sources": [
                '<!@(uname -a | grep "x86_64" >/dev/null && echo "xmrig/crypto/asm/cnv2_main_loop.S")',
                "multihashing.cc",
                "xmrig/crypto/c_blake256.c",
                "xmrig/crypto/c_groestl.c",
                "xmrig/crypto/c_jh.c",
                "xmrig/crypto/c_skein.c",
                "xmrig/common/crypto/keccak.cpp"
            ],
            "include_dirs": [
                "xmrig",
                "xmrig/3rdparty",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_c": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && (test `awk \'/model/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo` -ge "58" && echo -DIVYBRIDGE || echo -DSANDYBRIDGE) || (grep AMD /proc/cpuinfo >/dev/null && test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo` -ge 23 && echo -DRYZEN))>',
                "-std=gnu11 -fPIC -DNDEBUG -Ofast -funroll-loops -fvariable-expansion-in-unroller -ftree-loop-if-convert-stores -fmerge-all-constants -fbranch-target-load-optimize2"
            ],
            "cflags_cc": [
                '<!@(uname -a | grep "aarch64" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions" || (uname -a | grep "armv7" >/dev/null && echo "-mfpu=neon -flax-vector-conversions" || echo "-march=native"))',
                '<!@(grep Intel /proc/cpuinfo >/dev/null && (test `awk \'/model/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo` -ge "58" && echo -DIVYBRIDGE || echo -DSANDYBRIDGE) || (grep AMD /proc/cpuinfo >/dev/null && test `awk \'/cpu family/ && $NF~/^[0-9]*$/ {print $NF}\' /proc/cpuinfo` -ge 23 && echo -DRYZEN))>',
                "-std=gnu++11 -fPIC -DNDEBUG -Ofast -s -funroll-loops -fvariable-expansion-in-unroller -ftree-loop-if-convert-stores -fmerge-all-constants -fbranch-target-load-optimize2"
            ]
        }
    ]
}
