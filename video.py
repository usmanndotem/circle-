import cv2

def draw_circle(event,x,y,flags,param):

    global center,clicked

    # get mouse click on down and track center
    if event == cv2.EVENT_LBUTTONDOWN:
        if clicked == True:
            center = (x,y)
        if clicked == False:
            center = (0,0)
            clicked = True   

        
# Haven't drawn anything yet!
center = (0,0)
clicked = False

cap = cv2.VideoCapture(0)
cv2.namedWindow('circle')
cv2.setMouseCallback('circle', draw_circle)


while True:
    ret, frame = cap.read()
 
    if clicked:
        cv2.circle(frame, center = center, radius = 30, color = (255, 0, 0), thickness = 5)
        
    cv2.imshow('circle', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()