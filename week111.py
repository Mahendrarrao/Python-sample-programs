text = "X-DSPAM-Confidence:    0.8475"
mod1 = text.find(':')
lstring = text[mod1+1:]
string = lstring.lstrip()
val = float(string)
print(val)
