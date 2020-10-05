# InfoSecLabs
Lab practice for information security course

Current repo contains AES (https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf) implementation for my university course practice purposes only.

Benchmarking:
Course task requires testing speed on 1 GB of data. However, this implementation is slow that represents reasonable decreasement in data size. To be exact, 1 MB of data was used.
Results (alias key length parameter KL_{num} with AES-{num} algorithm):

BENCHMARKING KL_128 ALGORITHM FOR 1048576 BYTES OF DATA
  Time elapsed for preprocessing: 0.2125074863433838 sec
  Time elapsed for key expansion: 0.0007627010345458984 sec
  Time elapsed for encryption-decryption: 220.04754877090454 sec

BENCHMARKING KL_192 ALGORITHM FOR 1048576 BYTES OF DATA
  Time elapsed for preprocessing: 0.19955182075500488 sec
  Time elapsed for key expansion: 0.0008618831634521484 sec
  Time elapsed for encryption-decryption: 263.7029974460602 sec

BENCHMARKING KL_256 ALGORITHM FOR 1048576 BYTES OF DATA
  Time elapsed for preprocessing: 0.2065598964691162 sec
  Time elapsed for key expansion: 0.0010020732879638672 sec
  Time elapsed for encryption-decryption: 312.02789521217346 sec
