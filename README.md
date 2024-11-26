# Partner Names: Talise Baker-Matsuoka and Jessica Li

# Instructions to compile/execute code

1. Connect one ultrasound sensor to port D7 and the other to port D8 of the GrovePi
1.5 Attach the GrovePi to the Raspberry Pi
2. ssh to the Raspberry Pi and clone/download the code 
3. Run rpi_pub.py on the Raspberry Pi 
4. Run result_display_serv.py on a terminal on the main computer or virtual machine 
5. Run local_sub.py on another terminal on the main computer or virtual machine
6. Open the following link: http://127.0.0.1:5000/ in a browser to view the output. Reload the page to see a new output

All other files do not need to be run. create_data.py can be run on the main computer to generate training data for the ML model. The distances_train.ipynb file is a Jupyter Notebook file that creates the ML model. 


# List any external libraries used

External Python Libraries Used
- pandas
- paho-mqtt
- numpy
- matplotlib
- seaborn
- scikit-learn (sklearn)
- tensorflow
- grovepi (RPi only)
- requests
- flask

Other Python Libraries Used
- threading
- time
- sys
- json

