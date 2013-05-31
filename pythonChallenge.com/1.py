#!/usr/bin/env python
coded_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
letters = 'abcdefghijklmnopqrstuvwxyz'

decoded_string = ''

for char in coded_string:
  if char not in letters:
    decoded_string += char
    continue
  val = ord(char) + 2
  if val > 122:
    val -= 26
  decoded_string += chr(val)

print decoded_string
