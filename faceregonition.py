import face_recognition
import os
import cv2
knownfacedir="knownface"
unknownfacedir="unknownface"
tolerance=0.51
framethickness=3
fontthickness=2
MODEL="cnn"
print("Loading known faces")
knownfaces=[]
knownnames=[]

for name in os.listdir(knownfacedir):
    for filename in os.listdir(f"{knownfacedir}/{name}"):
        image=face_recognition.load_image_file(f"{knownfacedir}/{name}/{filename}")
        encoding=face_recognition.face_encodings(image)[0]
        knownfaces.append(encoding)
        knownnames.append(name)

print("Processign unknown faces")
for filename in os.listdir(unknownfacedir):
    
    image=face_recognition.load_image_file(f"{unknownfacedir}/{filename}")
    print("Processign unknown loading")
    locations=face_recognition.face_locations(image,model=MODEL)
    print("Processign unknown location")
    encodings=face_recognition.face_encodings(image,locations)
    
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    
    for face_encoding, face_location in zip(encodings,locations):
        result=face_recognition.compare_faces(knownfaces,face_encoding,tolerance)
        print("finding match.....")
        match=None 
        if True in result:
            match=knownnames[result.index(True)]
            print(f"Match found: {match}")
            
            topleft=(face_location[3],face_location[0])
            bottomright=(face_location[1],face_location[2])
            color=[0,255,0]
            cv2.rectangle(image,topleft,bottomright,color,framethickness)
            
            topleft=(face_location[3],face_location[2])
            bottomright=(face_location[1],face_location[2]+22)
            cv2.rectangle(image,topleft,bottomright,color,cv2.FILLED)
            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),fontthickness)
       
        else:
            print("Match NOT found")
            match="unknown";
            topleft=(face_location[3],face_location[0])
            bottomright=(face_location[1],face_location[2])
            color=[0,255,0]
            cv2.rectangle(image,topleft,bottomright,color,framethickness)
            
            topleft=(face_location[3],face_location[2])
            bottomright=(face_location[1],face_location[2]+22)
            cv2.rectangle(image,topleft,bottomright,color,cv2.FILLED)
            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),fontthickness)
    cv2.imshow(filename,image)

    cv2.waitKey(10000)
    
            
            
    
            
        
    
        
        

