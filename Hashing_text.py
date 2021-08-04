import hashlib

text="Moatasem"
encoded_text=hashlib.sha1(text)
print(hashlib.algorithms_guaranteed)
print(encoded_text.hexdigest())