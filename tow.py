a =     "    hello i   love    python      "
print(a.strip())
print(a.lstrip())
print(a.rstrip())

b =     "####### hello i   love    python ######"
print(b.strip("#"))
print(b.lstrip("#"))
print(b.rstrip("#"))


d = "#@#@#@#@ hello i   love    python  #@#@#@"
print(d.strip("#@"))
print(d.lstrip("#@"))
print(d.rstrip("#@"))

e = "i love 2d python but 5tschnolge not  "
print(e.title())

f = "I LOVE 3THIE PYTHON  "
print(f.capitalize())

g = "I LOVE THIE PYTHON   "
print(g.lower())
h = "i love python"
print(h.upper())

p , q , r , o = "11" , "100" , "111" ,"1111"
print(p.zfill(4))
print(q.zfill(4))
print(r.zfill(4))
print(o.zfill(4))