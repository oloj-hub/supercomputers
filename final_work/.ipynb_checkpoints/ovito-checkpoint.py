#У меня был багос что частица не отображалась, если она полностью скрывалась за другими прозрачными частицами
# ну и первую версия забагованную я еще 23 ночью перед парой залил
#щас так и не придумал как это пофиксить, просто анимацию покрасивей сделал
from ovito.io import import_file
#pipeline = import_file("short.xyz")
pipeline = import_file("/home/common/studtscm11/study/final_work/lj/diam_2.0/dump.shear.void")
import logging
logging.basicConfig(filename="log.txt", level=logging.INFO)
import ovito.modifiers as md
pipeline.add_to_scene()
global center
import math
import ovito.vis as vis
import math
import numpy as np
from ovito.vis import Viewport, TachyonRenderer
vp = vis.Viewport()
vp.type = vis.Viewport.Type.Perspective
data=pipeline.compute(100)
#вот тут он находит положения частицы на 100ом шаге чтоб к нему приближаться
identifier_property =  data.particles_.create_property("Particle Identifier")
for i in range(len(identifier_property)):
    if(identifier_property.marray[i]==1100):
        global center 
        center = data.particles_.positions_[i]
data=pipeline.compute()
wall=data.cell[0][0]
def get_pos_dir(frame):
    global center
    #center=np.array([wall/2, wall/2, wall/2])
    radius=wall/3
    #hight=[0,0,wall*3/4*(125-frame)/100]
    hight=wall/2
    phi = frame/50*2*np.pi
    #phi=0
    direction=np.array([np.cos(phi), np.sin(phi),0])
    position = center + direction*radius+hight
    #direction = [-1,0,-1]
    #position = [34.6, 5.2, 34.6]
    return tuple(position), tuple( (center - position) )
pos, direction = get_pos_dir(0)
vp.camera_pos = pos
vp.camera_dir = direction
vp.fov = math.radians(60.0)
def render_view(args):
    frame=args.frame
    #print (args.frame, end=" ")
    logging.info("frame: {:d}".format(args.frame))
    #text1 = "Frame {}".format(args.frame)
    pos, direction = get_pos_dir(frame)
    args.viewport.camera_pos = pos
    args.viewport.camera_dir = direction
    args.viewport.fov = math.radians(60.0)
vp.overlays.append(vis.PythonViewportOverlay(function=render_view))
#tachyon = vis.TachyonRenderer(shadows=False)
vp.render_anim(size=(400,300), filename="shear_visual.mp4",
    renderer=vis.TachyonRenderer(), range=(0,50))