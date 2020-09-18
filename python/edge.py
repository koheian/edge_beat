import cv2

def edge_detect():
    # input an image file
    print("input image: ", end="")
    input_filename = input()
    input_img = cv2.imread(input_filename, 0)

    # edge detection
    sobel_img = cv2.Sobel(input_img, cv2.CV_32F, 1, 1, 1, 5)
    laplacian_img = cv2.Laplacian(input_img, cv2.CV_32F, 1, 5)
    canny_img = cv2.Canny(input_img, 50, 150)

    # output
    cv2.imwrite("sobel.jpg", sobel_img)
    cv2.imwrite("laplacian.jpg", laplacian_img)
    cv2.imwrite("canny.jpg", canny_img)

if __name__ == "__main__":
    edge_detect()
