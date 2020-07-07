def egcd(a, b):                     #Euklidischer Algorithmus
    s = 0; old_s = 1                #Er berechnet neben dem größten gemeinsamen Teiler zweier natürlicher Zahlen
    t = 1; old_t = 0                #a und b noch zwei ganze Zahlen s und t, die die folgende Gleichung erfüllen:
    r = b; old_r = a
                                    # ggT(a, b) = s * a + t * b
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t      #Rückgabewerte old_r = ggt, old_s = s, old_t = t



def modularInv(a, b):               #Modulares Invertieren
    gcd, x, y = egcd(a, b)          #Bei gleichbleibender Funktion wird reversibel der Wert umgekehrt

    if x < 0:                       # a - b = c
        x += m                      # c - (b*-1) = a

                                    # 4 - 2 = 2
                                    # 2 + 2 = 4
                                    # 4 - 2 = 2             b ist e
                                    # 2 - (2* - 1) = 4      b*-1 ist private d
    return x                        #x ist somit unser "Umkehrwert" für die Entschlüsselungsfunktion



def encrypt(e, N, msg):             #Verschlüsseln des Textes msg mithilfe des public-key e
    cipher = ""

    for c in msg:
        m = ord(c)                  #ord(): gibt den Zahlenwert des Symbols an (ASCII)
        cipher += str(pow(m, e, N)) + " "   #Verschlüsselung - Leerzeichen für Trennung von Symbolen

    return cipher                   #Rückgabe des Verschlüsselten Textes



def decrypt(d, N, cipher):          #Entschlüsseln des Textes dec mithilfe des private-keys d
    msg = ""

    parts = cipher.split()          #Aufteilen des Strings in eine Liste (Zeichen für Zeichen wird Entschlüsselt)

    for part in parts:
        if part:
            c = int(part)           #Aktueller verschlüsslter char-Wert in int konvertieren
            msg += chr(pow(c, d, N))    #Entschlüsseln und anfügen an msg

    return msg                      # Rückgabe des Entschlüsselten Textes



def main():

    p = 11                          #Wähle 2 Primzahlen
    q = 13
    N = p * q                       #Errechne N         N = p * q
    phiN = (p - 1) * (q - 1)        #Errechne Phi(N)    Phi(N) = Phi(p) * Phi(q)

    e = 13                          #Wähle public-key
    d = modularInv(e, phiN)         #Errechne private-key

                                    #Beispielstring:
    msg = "Zwischen 2 Apfelbauemen ist im Park ein Schatzversteckt!"

    enc = encrypt(e, N, msg)        #Verschlüsseln von msg mit dem public-key e
    dec = decrypt(d, N, enc)        #Entschlüsseln von enc mit dem private-key d

    print(f"Nachricht: {msg}")      #Ausgabe-Routine
    print(f"Public-Key (e): {e}")
    print(f"Private-Key (d): {d}")
    print(f"RSA-Modulo (N): {N}")
    print(f"Verschlüsselte Nachricht: {enc}")
    print(f"Entschlüsselte Nachricht: {dec}")



main()