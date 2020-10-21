# InfoSecLabs
Lab practice for information security course

Current repo contains implementation for my university course practice purposes only.
Algorithms:
    AES
    RC4
    Salsa20


Benchmarking:
    Course task requires testing speed on 1 GB of data.
    However, this implementation is slow that represents reasonable decrease in data size.
    To be exact, 1 MB of data was used in most cases.

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
