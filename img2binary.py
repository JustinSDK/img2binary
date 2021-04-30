# Requirements: Python 3 and OpenCV.
# If you don’t have OpenCV installed, install it via pip:
#     pip install opencv-python

import sys, argparse, numpy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the source image")
    parser.add_argument("dest", help="the dest text")

    if(len(sys.argv) < 3):
        parser.print_help()
    else:
        try:
            import cv2
            args = parser.parse_args()
            img = cv2.imread(args.src, 2)
            _, bw_img = cv2.threshold(img, 0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            binary = numpy.where(bw_img == 255, 1, bw_img) 
            with open(args.dest, 'w') as dest:
                dest.write('[\n')
                for r in range(0, len(binary) - 1):
                    dest.write('\t')
                    dest.write(str(binary[r].tolist()))
                    dest.write(',\n')
                dest.write('\t')
                dest.write(str(binary[-1].tolist()))
                dest.write('\n]')
        except:
            print('If you don’t have OpenCV installed, install it via pip.')
            print('> pip install opencv-python')
            
       
main()