import re as r

def return_True_if_etherum(m):
    if not isinstance(m, str):
        return False
    v = r.match(r'^0x[0-9a-fA-F]{40}$', m)

    return bool(v)
m=return_True_if_etherum("0x17BcaBd1F23e25B5FB31446F851e4644eE8F90b0")
print(m)

