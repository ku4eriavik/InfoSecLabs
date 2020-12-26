# InfoSecLabs
Lab practice for information security course

Current repo contains implementation for my university course practice purposes only.
Algorithms:
    AES
    RC4
    Salsa20
    CBC
    CFB
    CTR
    ECB
    OFB


Benchmarking:
    Course task requires testing speed on 1 GB of data.
    However, this implementation is slow that represents reasonable decrease in data size.
    To be exact, 1 MB or 100 KB of data was used in most cases.

AES:
    Results (alias key length parameter KL_{num} with AES-{num} algorithm):
    BENCHMARKING KL_128 ALGORITHM FOR 1048576 BYTES OF DATA
      Time elapsed for preprocessing: 0.2125074863433838 sec
      Time elapsed for key expansion: 0.0007627010345458984 sec
      Time elapsed for encryption-decryption: 220.04754877090454 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    BENCHMARKING KL_192 ALGORITHM FOR 1048576 BYTES OF DATA
      Time elapsed for preprocessing: 0.19955182075500488 sec
      Time elapsed for key expansion: 0.0008618831634521484 sec
      Time elapsed for encryption-decryption: 263.7029974460602 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    BENCHMARKING KL_256 ALGORITHM FOR 1048576 BYTES OF DATA
      Time elapsed for preprocessing: 0.2065598964691162 sec
      Time elapsed for key expansion: 0.0010020732879638672 sec
      Time elapsed for encryption-decryption: 312.02789521217346 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

KALYNA:
    FOR 100 KB MESSAGE:
        ENCRYPTION TIME ELAPSED 27.14988398551941 sec for (Nb=2, Nk=2, Nr=10)
        ENCRYPTION TIME ELAPSED 38.37668514251709 sec for (Nb=2, Nk=4, Nr=14)
        ENCRYPTION TIME ELAPSED 45.261677265167236 sec for (Nb=8, Nk=8, Nr=18)


RC4:
    BENCHMARKING RC4 ON:
        KEY LENGTH = 16
        MESSAGE LENGTH = 1 KB
        TIME ELAPSED = 0.0050466060638427734 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    BENCHMARKING RC4 ON:
        KEY LENGTH = 16
        MESSAGE LENGTH = 1 MB
        TIME ELAPSED = 2.975966215133667 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    BENCHMARKING RC4 ON:
        KEY LENGTH = 16
        MESSAGE LENGTH = 1 GB
        TIME ELAPSED = 3205.627621516160395 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

Salsa20:
    BENCHMARKING Salsa20 ON:
	    KEY LENGTH = 32
	    MESSAGE LENGTH = 1 KB
	    TIME ELAPSED = 0.015337467193603516 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    BENCHMARKING Salsa20 ON:
	    KEY LENGTH = 32
	    MESSAGE LENGTH = 1 MB
	    TIME ELAPSED = 15.703863143920898 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

CBC:
    BENCHMARKING CBC ON:
	    USING AES WITH KL_128
        MESSAGE LENGTH = 1 KB
        TIME ELAPSED = 0.4194204807281494 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    BENCHMARKING CBC ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 MB
        TIME ELAPSED = 432.0291430950165 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

CFB:
    BENCHMARKING CFB ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 KB
        TIME ELAPSED = 0.3771383762359619 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    BENCHMARKING CFB ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 MB
        TIME ELAPSED = 403.51059689921030 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

CTR:
    BENCHMARKING CTR ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 KB
        TIME ELAPSED = 0.3824191093444824 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    BENCHMARKING CTR ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 MB
        TIME ELAPSED = 423.95244550704956 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

ECB:
    BENCHMARKING ECB ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 KB
        TIME ELAPSED = 0.4202241897583008 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    BENCHMARKING ECB ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 MB
        TIME ELAPSED = 454.52645367478989 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

OFB:
    BENCHMARKING OFB ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 KB
        TIME ELAPSED = 0.3833281993865967 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    BENCHMARKING OFB ON:
        USING AES WITH KL_128
        MESSAGE LENGTH = 1 MB
        TIME ELAPSED = 390.85651845151459 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


PROOF OF WORK:
    SHA-256 vs KUPYNA-256 vs KUPYNA-512:
        PREFIX: 736f6d6574696d657320492077616e6e6120646965

        POW: zero bits = 2
        TIME ELAPSED:
            SHA-256: 0.0020596981048583984 sec.
            KUPYNA-256: 0.03747844696044922 sec.
            KUPYNA-512: 0.12219810485839844 sec.
        -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

        POW: zero bits = 3
        TIME ELAPSED:
            SHA-256: 0.004654884338378906 sec.
            KUPYNA-256: 0.093505859375 sec.
            KUPYNA-512: 0.7056849002838135 sec.
        -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

        POW: zero bits = 4
        TIME ELAPSED:
            SHA-256: 0.0076372623443603516 sec.
            KUPYNA-256: 0.13105082511901855 sec.
            KUPYNA-512: 0.7406129837036133 sec.
        -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


RSA:
    Length of P and Q = 384
    Message len (bits) = 240
    Time elapsed for key-gen: 0.39205002784729004 sec
    Time elapsed for encryption: 0.002269268035888672 sec
    Time elapsed for decryption: 0.0008678436279296875 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-

    Length of P and Q = 512
    Message len (bits) = 496
    Time elapsed for key-gen: 0.46866822242736816 sec
    Time elapsed for encryption: 0.00506138801574707 sec
    Time elapsed for decryption: 0.0018527507781982422 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-

    Length of P and Q = 1024
    Message len (bits) = 1520
    Time elapsed for key-gen: 2.059804677963257 sec
    Time elapsed for encryption: 0.03414607048034668 sec
    Time elapsed for decryption: 0.010143280029296875 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-

    Length of P and Q = 1536
    Message len (bits) = 2544
    Time elapsed for key-gen: 14.759542465209961 sec
    Time elapsed for encryption: 0.10523152351379395 sec
    Time elapsed for decryption: 0.03050684928894043 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-


RSA-OAEP:
    Length of P and Q = 384
    Message len (bits) = 240
    Time elapsed for key-gen: 0.21747207641601562 sec
    Time elapsed for encryption: 0.004578351974487305 sec
    Time elapsed for decryption: 0.0030221939086914062 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-

    Length of P and Q = 512
    Message len (bits) = 496
    Time elapsed for key-gen: 0.18386149406433105 sec
    Time elapsed for encryption: 0.007825613021850586 sec
    Time elapsed for decryption: 0.004800081253051758 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-

    Length of P and Q = 1024
    Message len (bits) = 1520
    Time elapsed for key-gen: 1.553133249282837 sec
    Time elapsed for encryption: 0.038727521896362305 sec
    Time elapsed for decryption: 0.015287399291992188 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-

    Length of P and Q = 1536
    Message len (bits) = 2544
    Time elapsed for key-gen: 7.0375144481658936 sec
    Time elapsed for encryption: 0.11423087120056152 sec
    Time elapsed for decryption: 0.03872179985046387 sec
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-
