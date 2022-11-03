from servicios.Imagen import Imagen
import cv2



class Video:

    def __init__(self,rutaGeneral):
        self.imagenes=[]
        self.ruta=rutaGeneral
        self.path="";
        self.width =640;
        self.height =480;
        self.nombreVideo="Video Todas las Etapas Automatas"

    def anadirImagenesVideo(self, imagen):
        self.path = self.ruta + imagen.nombreImagen
        self.imagenes.append( cv2.imread(self.path));

    def crearVideo(self):
        height, width  = self.imagenes[len(self.imagenes)-1].shape[:2]
        video= cv2.VideoWriter(f'fotosEtapa\{self.nombreVideo}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 5, (width,height))

        for i in range(len(self.imagenes)):
            video.write(self.imagenes[i])
            video.release


