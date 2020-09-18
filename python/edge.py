import cv2
import config

def input_resize():
    size = (config.l_img, config.l_img)
    # input an image file
    print("input image: ", end="")
    input_filename = input()
    input_img = cv2.imread(input_filename)
    # resize
    resize_img = cv2.resize(input_img, size)
    cv2.imwrite("resize.jpg", resize_img)
    return resize_img


def edge_detect(img):
    # get gray scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # edge detection
    sobel_img = cv2.Sobel(img, cv2.CV_32F, 1, 1, 1, 5)
    laplacian_img = cv2.Laplacian(img, cv2.CV_32F, 1, 5)
    canny_img = cv2.Canny(img, 50, 150)

    # output
    cv2.imwrite("sobel.jpg", sobel_img)
    cv2.imwrite("laplacian.jpg", laplacian_img)
    cv2.imwrite("canny.jpg", canny_img)

if __name__ == "__main__":
    edge_detect(input_resize())
