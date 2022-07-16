import cv2
import os

from pandas import to_datetime
def save_img():
    video_path = '/Users/kyz/Desktop/hiwi_task/task3/RAFT/frame/'+'L00'+'_frame'
    video_L00_path = '/Users/kyz/Desktop/hiwi_task/task3/RAFT/video/L00'
    videos = os.listdir(video_L00_path)
    for video_name in videos:
        file_name = video_name.split('.')[0]#file_name is '2022_03_10_S05_SC01_T01_SE003_L00'
        folder_name = video_path +'/'+file_name#folder_name is 'L00_frame2022_03_10_S05_SC01_T01_SE003_L00' 改这行
        os.makedirs(folder_name, exist_ok=True)#creat folder for frames
        vc = cv2.VideoCapture(video_L00_path+'/'+video_name) 
        c=0
        rval=vc.isOpened()
 
        while rval:  
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name+'/'#图片的路径
            if rval:
                cv2.imwrite(pic_path + str(c) + '.png', frame)
                cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)
save_img()

#现在想要遍历video文件夹包含的所有文件夹