def halftone(img, divisor=5):
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            k = img[i, j]  # i ist der y-Wert (von oben nach unten) und j der x-Wert (von links nach rechts)
            # print(k)
            if k >= 128:
                diff = 255 - k
                img[i, j] = 255 #aktueller Pixel wird weiss gesetzt
                if j != cols - 1:
                    img[i, j + 1] -= int(round(7 / divisor * diff)) #Pixel rechts neben dem aktuellen wird aufgehellt (um 7/divisor mal Differenz von weiss zum Pixelwert)
                if i != rows - 1 and j != cols - 1:
                    img[i + 1, j + 1] -= int(round(1 / divisor * diff)) #Pixel diagonal rechts unten vom aktuellen wird aufgehellt (um 1/divisor mal Differenz von weiss zum Pixelwert)
                if i != rows - 1:
                    img[i + 1, j] -= int(round(5 / divisor * diff)) #Pixel unter neben dem aktuellen wird aufgehellt (um 5/divisor mal Differenz von weiss zum Pixelwert)
                if j != 0 and i != rows - 1:
                    img[i + 1, j - 1] -= int(round(3 / divisor * diff)) #Pixel diagonal links unten vom aktuellen wird aufgehellt (um 3/divisor mal Differenz von weiss zum Pixelwert)
            else:
                diff = k
                img[i, j] = 0 #aktueller Pixel wird schwarz gesetzt
                if j != cols - 1:
                    img[i, j + 1] += int(round(7 / divisor * diff)) #Pixel rechts neben dem aktuellen wird verdunkelt (um 7/divisor mal Differenz von schwarz zum Pixelwert)
                if i != rows - 1 and j != cols - 1:
                    img[i + 1, j + 1] += int(round(1 / divisor * diff)) #Pixel diagonal rechts unten vom aktuellen wird verdunkelt (um 1/divisor mal Differenz von schwarz zum Pixelwert)
                if i != rows - 1:
                    img[i + 1, j] += int(round(5 / divisor * diff)) #Pixel unter neben dem aktuellen wird verdunkelt (um 5/divisor mal Differenz von schwarz zum Pixelwert)
                if j != 0 and i != rows - 1:
                    img[i + 1, j - 1] += int(round(3 / divisor * diff)) #Pixel diagonal links unten vom aktuellen wird verdunkelt (um 3/divisor mal Differenz von schwarz zum Pixelwert)
