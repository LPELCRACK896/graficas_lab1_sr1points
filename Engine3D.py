from lpgl import Renderer, color

width = int(input("Ingrese el ancho: "))
height = int(input("Ingrese la altura: "))
#color_list_rgb = [1, 1, 1]

#Suprimidos por lo poco practico y util que era
""" 
def changeColorList():
    rgb = ["rojo", "verde", "azul"]
    digits_aprooved = 0
    while digits_aprooved<3:
        color_digit = input(f"Ingrese la intensidad de {rgb[digits_aprooved]} que desea (del 0 al 1): ")
        if colorRangeFloat(color_digit):
            color_list_rgb[digits_aprooved] = color_digit
            digits_aprooved += 1

def colorRangeFloat(digit):
    try:
        digit = float(digit)
        if(0<=digit<=1):
            return True
        else:
            print("El valor ingresado no entra en el rango")
            return False
    except:
        print("El valor ingresado no es un numero")
        return False

 """
""" print(color_list_rgb)
changeColorList()
print(color_list_rgb)
 """
rend= Renderer(width, height)

rend.glCreateWindow(width, height)

#cuadrado en rectangulo en un rectangulo
rend.glViewport(int(width/4),int(height/4),int(width/2),int(height/2))

rend.glClearColor(1,0,0) #Ventana color
rend.glClear()
rend.glClearViewport(color(0.5,0,0.5)) #Viewport color 

rend.glPoint(0,0) #Centro
rend.glPoint(1,1) #Esquina
rend.glPoint(-1,-1) #Esquina

rend.glFinish("output.bmp")

