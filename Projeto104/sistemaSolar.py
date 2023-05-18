import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, 
            "Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))

cv2.putText(img, 
            "Mercurio",(120,250), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.putText(img, 
            "Venus",(195,175), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.putText(img, 
            "Terra",(295,260), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.putText(img, 
            "Marte",(395,250), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.putText(img, 
            "Jupter",(510,60), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.putText(img, 
            "Saturno",(680,270), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.putText(img, 
            "Urano",(960,140), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.putText(img, 
            "Netuno",(1080,140), cv2.FONT_HERSHEY_COMPLEX, 0.4, (150, 0, 160))

cv2.imshow("Sistema Solar",img)
cv2.imwrite("SistemaSolarNomeado.jpg",img)
print("Baixado! :D")
cv2.waitKey(0)
