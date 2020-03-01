import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import pdb
import argparse

def myHough(img_name,ce_params,hl_params): 
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,ce_params["lowThreshold"],ce_params["highThreshold"],apertureSize = ce_params["kernel_size"])
    cv2.imshow('canny_edges.jpg',edges)

    # # Using houghLines() 
    # lines = cv2.HoughLines(edges,1,np.pi/180,165)
    # if lines is not None:
    #     for line in range(lines.shape[0]):
    #         for rho,theta in lines[line]:
    #             a = np.cos(theta)
    #             b = np.sin(theta)
    #             x0 = a*rho
    #             y0 = b*rho
    #             x1 = int(x0 + 1000*(-b))
    #             y1 = int(y0 + 1000*(a))
    #             x2 = int(x0 - 1000*(-b))
    #             y2 = int(y0 - 1000*(a))
    #             cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    # Using houghLinesP()
    linesP = cv2.HoughLinesP(edges, rho = hl_params["rho"], theta = hl_params["theta"], 
        threshold = hl_params["threshold"], minLineLength = hl_params["minLineLength"], 
        maxLineGap = hl_params["maxLineGap"])
    if linesP is not None:
        for line in range(linesP.shape[0]):
            for l in linesP[line]:
                cv2.line(img, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)

    cv2.imshow('hough_lines.jpg',img)
    cv2.waitKey(0)
    cv2.imwrite('../results/hough_lines.jpg',img)

if __name__=="__main__":

    # create a list of the params 
    # for both your edge detector 
    # hough transform

    edge_params = {"lowThreshold":50, "highThreshold":150, "kernel_size":3}
    hl_params = {"rho":1, "theta":np.pi / 180, "threshold":40, "minLineLength":50, "maxLineGap":10}
    img_name = "../data/img01.jpg"
    myHough(img_name, edge_params,hl_params)