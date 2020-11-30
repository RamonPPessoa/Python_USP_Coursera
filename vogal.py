
def vogal(vg):
    if vg == 'a' or vg =='e' or vg == 'i' or vg == 'o' or vg == 'u' or vg == 'A' or vg == 'E' or vg == 'I' or vg == 'O' or vg == 'U':
        return True
    else:
        return False
    
vg = input("Digite um caracter")
print(vogal(vg))