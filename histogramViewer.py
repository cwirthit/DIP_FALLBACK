# Author: Andrew Hauser
# Co-Authors: Josh Rodkey, Christian Wirth
# Version 0.1
# Histogram Viewer for image analysis and modification




#################################################################################
# Changes made here!
# @Christian
#################################################################################

import Tkinter, tkFileDialog
from Tkinter import *

root = Tk()

from PIL import Image, ImageDraw
from math import *
import os, glob

path = "" # Path where your pictures are stored

def fileBrowser():
   dirname = tkFileDialog.askdirectory(initialdir="/", title='Please select a directory')
   path = str(dirname)
   histViewer(path)
   return


browseButton = Button(root, text ="Select Image Folder", command = fileBrowser).pack()
   
#################################################################################
# End changes
#################################################################################

def histViewer(path):
   piclist = list() 
   x = 0

   ##################################################################################

   histHeight = 120            # Height of the histogram
   histWidth = 256             # Width of the histogram
   multiplerValue = 1.5        # The multiplier value basically increases
                               # the histogram height so that love values
                               # are easier to see, this in effect chops off
                               # the top of the histogram.

   showFstopLines = True       # True/False to hide outline
   fStopLines = 5


   # Colors to be used
   backgroundColor = (51,51,51)    # Background color
   lineColor = (102,102,102)       # Line color of fStop Markers 
   red = (255,60,60)               # Color for the red lines
   green = (51,204,51)             # Color for the green lines
   blue = (0,102,255)              # Color for the blue lines

   ##################################################################################

   for infile in glob.glob(os.path.join(path,'*.jpg')):	# Adds the path of each 
           piclist.append(infile)								# image with the extensions 
														# used to the list piclist()
   for infile in glob.glob(os.path.join(path,'*.png')):
           piclist.append(infile)

   for infile in glob.glob(os.path.join(path,'*.jpeg')):
           piclist.append(infile)

   for infile in glob.glob(os.path.join(path,'*.gif')):
           piclist.append(infile)

   for x in range(0, len(piclist)): # Loops through for each image path in the list

           imagepath = piclist[x]  # The image to build the histogram of
           img = Image.open(imagepath)
           ######################################
           img.show()      #   Change Here
           ######################################
           hist = img.histogram()
           histMax = max(hist)                                     #common color
           xScale = float(histWidth)/len(hist)                     # xScaling
           yScale = float((histHeight)*multiplerValue)/histMax     # yScaling 


           im = Image.new("RGBA", (histWidth, histHeight), backgroundColor)   
           draw = ImageDraw.Draw(im)


           # Draw Outline is required
           if showFstopLines:    
               xmarker = histWidth/fStopLines
               x =0
               for i in range(1,fStopLines+1):
                   draw.line((x, 0, x, histHeight), fill=lineColor)
                   x+=xmarker
               draw.line((histWidth-1, 0, histWidth-1, 200), fill=lineColor)
               draw.line((0, 0, 0, histHeight), fill=lineColor)


           # Draw the RGB histogram lines
           x=0; c=0;
           for i in hist:
               if int(i)==0: pass
               else:
                   color = red
                   if c>255: color = green
                   if c>511: color = blue
                   draw.line((x, histHeight, x, histHeight-(i*yScale)), fill=color)        
               if x>255: x=0
               else: x+=1
               c+=1

           # Now save and show the histogram    
           # im.save('histogram.png', 'PNG')
           im.show()
           
root.mainloop()






