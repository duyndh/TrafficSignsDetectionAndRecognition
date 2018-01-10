from header import *
from train import *
from test import *
from image_processing import *

def machine_learning():
	print('MACHINE LEARNING')
	print('****************')
	
	# After the training, you can skip this steps at the next time by loading svm_model file
	execute('=' * 20 + '\nTRAIN', train)
	
	# execute('=' * 20 + '\nTEST', test)

def process_video():
	print('PROCESS VIDEO')
	print('****************')

	with open(output, 'w') as f:
		print('Init\n')
		
		svm = execute('Loading model', cv2.ml.SVM_load, svm_model_file)
		templates, templates_title = execute('Loading templates', load_templates)

		inp = cv2.VideoCapture(video_input)
		video_width = int(inp.get(cv2.CAP_PROP_FRAME_WIDTH))
		video_height = int(inp.get(cv2.CAP_PROP_FRAME_HEIGHT))
		video_fps = inp.get(cv2.CAP_PROP_FPS)
		
		print('Video resolution: (' + str(video_width) + ', ' + str(video_height) + ')')
		print('Video fps:', video_fps)

		out = cv2.VideoWriter(video_output, -1, video_fps, (video_width, video_height))
		
		print('Video is running')
		frame_id = 0
		while inp.isOpened():
			ret, frame = inp.read()
			if (not ret) or (cv2.waitKey(1) & 0xFF == ord('q')):
				break
			process_image(frame, svm, templates, templates_title, f, frame_id)
			
			out.write(frame)
			frame_id += 1
	        
		inp.release()
		out.release()
		cv2.destroyAllWindows()

if __name__ == '__main__':
	# machine_learning()
	process_video()
	