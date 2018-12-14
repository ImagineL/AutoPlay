from skimage.measure import compare_ssim
import cv2
class ImgTools(object):
    """图片帮助类"""
    def compare_image(self, path_image1, path_image2):
        """
        比较两张图片的相似度
        :retrun:返回图片相似度
        """
        imageA = cv2.imread(path_image1)
        imageB = cv2.imread(path_image2)

        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        return score


