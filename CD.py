import pandas as pd
import cv2

img= cv2.imread("image2.jpg")
dime = img.shape
h = img.shape[0]
w = img.shape[1]
area = h*w
clicked = False
r=g=b=xpos=ypos=0
index=["color", "color_name", "hex", "R","G", "B"]
csv=pd.read_csv("colors.csv", names=index,header=None)
def getcolorName(R,G,B):
    minimum=float("inf")
    cname=''
    for i in range(len(csv)):
        d= abs(R - int(csv.loc[i,"R"]))+ abs(G - int(csv.loc[i,"G"])) + abs(B - int(csv.loc[i,"B"]))
        if d<= minimum:
            minimum=d
            cname=csv.loc[i,"color_name"]
    return cname

def draw_function(event, x ,y , flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked= True
        xpos=x
        ypos=y
        b,g,r=img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
if area<=662000:
    cv2.namedWindow('Image')
else:
    cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Image', draw_function)
while(1):
    cv2.imshow("Image",img)
    if clicked:
        recEnd = (round(w *.735), round(h *.1))
        textstart= (round(w *.05), round(h *.08))
        cv2.rectangle(img,(20,20),recEnd,(b,g,r),-1)
        text = getcolorName(r, b, g) + ' R=' + str(r) + ' B=' + str(b) + ' G=' + str(g)
        if r + g + b >= 600:
            cv2.putText(img, text, textstart, cv2.FONT_HERSHEY_SIMPLEX,1 , (0,0,0), 1, cv2.LINE_AA)
        else:
            cv2.putText(img, text, textstart, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        clicked=False
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyWindow(None)