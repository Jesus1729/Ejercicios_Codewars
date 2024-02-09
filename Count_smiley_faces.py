# Count the smiley faces!

def count_smileys(arr):
    c = 0

    for cara in arr:
        if len(cara) == 2:
            ojos = cara[0]
            boca = cara[1]
            if ojos in [":", ";"] and boca in [")", "D"]:
                c += 1
        elif len(cara) == 3:
            ojos = cara[0]
            nariz = cara[1]
            boca = cara[2]
            if ojos in [":", ";"] and nariz in ["-", "~"] and boca in [")", "D"]:
                c += 1

    return c

print(count_smileys([":)",":("]))