def vokon_zählen(s):
    
    vokale = "aeiou"
    s_lower = s.lower()
    
    bn = [i for i in s_lower if i.isalpha()]
    Vn = [k for k in s_lower if k in vokale]
    print (f"Es gibt {len(Vn)} Vokale und {len(bn)- len(Vn)} Konsonanten")

vokon_zählen("jdjae&8d9, hd")