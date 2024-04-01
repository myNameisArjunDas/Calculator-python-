import time
from plyer import notification

if __name__ == "__main__":
	notification.notify(
	title = "Revision time",
	message = "Revision helps recall the details of the topic you have studied. Revising the topics helps gain more confidence to attempt any related question in the exam. Timely revision helps reduce the anxiety and stress levels while attempting the exams",
	app_icon = "/home/user/Documents/python projects/effective_revision_icon.png",
	timeout=10
	)
	time.sleep(60*60*2)
	
