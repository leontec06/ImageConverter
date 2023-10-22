import cv2
import FloydHalftone as fh
import svgwrite



img = cv2.imread("images\Trooper.jpg", 0)  # Laden des Bildes in Grayscale -> ("name.jpg", 0)
in_img = cv2.resize(img, (401, 401))  # Bildgrösse anpassen, (401, 401) für Trooper.jpg, (361, 461) für david2.png, (401, 531) für Luke_Skywalker.png
cv2.imshow("grayscale",in_img)
cv2.waitKey(0)
rows, cols = in_img.shape
divisor = 18 #18 für Trooper.jpg, 30 für david_yellow.png&Luke_Skywalker.png



fh.halftone(in_img, divisor)
cv2.imshow("halftone", in_img)
cv2.waitKey(0)
PenPath = []

cursor = (0, 0)

for y in range(0, rows, 5):  # Reihen in Fünferschritten nach unten
    
    # Überprüfen, ob in geraden oder ungeraden Reihe (Y-Wert)
    if y % 2 == 0:
        # Wenn gerade, starte von der ersten Spalte
        start_col = 0
        step_col = 5 #Parameter für Abstand zwischen den verarbeiteten Bildpunkten
        columns = cols

    else:
        # Wenn ungerade, starte von der letzten Spalte
        start_col = cols - 1
        step_col = -5 #Parameter für Abstand zwischen den verarbeiteten Bildpunkten
        columns = 0

    for x in range(start_col, columns, step_col):  # Iteration durch Kolonnen

        if in_img[y, x] == 255:
            in_img[y, x] = 0 #schwarze Punkte werden im Raster gesetzt. Bewirkt nichts,jedoch gut zur Vorstellung wenn noch keine Linien gezeichnet werden


        PenPath.append([x,y])

        # Überprüfe Nachbarspixel
        neighbors=[[y - 1, x - 1], [y - 2, x - 2], [y - 1, x],
                   [y - 2, x], [y - 1, x + 1], [y - 2, x + 2],
                   [y, x + 1], [y, x + 2], [y + 1, x + 1],
                   [y + 2, x + 2], [y + 1, x], [y + 2, x],
                   [y + 1, x - 1], [y + 2, x - 2], [y, x - 1],
                   [y, x - 2]]
        if x >= 5 and y >= 5 and x <= cols - 5 and y <= rows - 5:
            for i in neighbors:
                if in_img[i[0], i[1]] ==0: #Überprüfen ob Nachbarspixel schwarz ist
                    PenPath.append([i[1], i[0]]) #wenn schwarz wird er zum Pfad hinzugefügt
                    cursor = (i[1], i[0])

        cursor = (x, y)



first=True
svgdraw = svgwrite.Drawing('svg_output.svg', profile='tiny') #SVG-Datei vorbereiten

old=[0,0]
for i in PenPath:
    svgdraw.add(svgdraw.line(start=(old[0], old[1]), end=(i[0], i[1]), stroke=svgwrite.rgb(0, 0, 0), stroke_width=1)) #Farbe und Dicke der Linie können mittels den zwei letzten Parammetern angepasst werden.
    old=[i[0], i[1]]
    gcode = open("gcode\Gcode.txt", "a")
    if first==True:
        open("gcode\Gcode.txt", 'w').close()
        gcode = open("gcode\Gcode.txt", "a")
        gcode.write(f"F7000\n") #Feedrate (Geschwindigkeit) des Plotters wird in der ersten Zeile gesetzt, in diesem Fall 7000 für Genauigkeit und gutes Tempo.
    gcode.write(f"G1 x{i[0]/4} y{i[1]/4}\n")
    gcode.close()
    first=False
svgdraw.save()

