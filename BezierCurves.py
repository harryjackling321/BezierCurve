import matplotlib.pyplot as plt
import re

#Instruction on format of point entry
print("Enter points in the format 'x,y' \n")
#List to store points
points = []
#Practice points list 
#points = [[-2,-2], [-3,-5], [4,1], [5,5]]
#List of points names
points_names = ['Start', 'Control 1', 'Control 2', 'End']

#Point entry loop, 4 points
for x in range(4):
	#Set format test variable
	format_test = 0
	#Input point x and y coordinates
	point_input = input("Enter %s point : \n" % points_names[x])
	#Test format of entered point is xxx,yyy. If so, proceed, if not, say so and ask again
	while format_test != 1: 
		if re.match("\-?\d{1,3},\-?\d{1,3}", point_input):
			format_test = 1
		else:
			print("Incorrect format")
			point_input = input("Enter %s point : \n" % points_names[x])
	#Input string of coordinates converted to single integer list and appended to points list
	#Points list format: [[x,y],[x,y],[x,y],[x,y]] --> [[start],[control1],[control2],[end]]
	point = [int(p) for p in point_input.split(",")]
	points.append(point)

#Input number of intervals for t
t_int_num = int(input("Enter number of intervals: \n"))
#Calculate t increment per interval
t_int_size = 1 / t_int_num
#Create list of t values
t_values = [round((t*t_int_size), 3) for t in range(t_int_num)]
#Append 1 to the list as this is always missed (essentially missing end point out)
t_values.append(1)

#Create lists for storing bezier curve x and y coordinates
bezier_x_list = []
bezier_y_list = []

#Seperate x and y coordinates of points (for use in curve coordinate calculation)
sx, sy = points[0]
c1x, c1y = points[1]
c2x, c2y = points[2]
ex, ey = points[3]

for t in t_values:
	#Calculate x coordinate for current value of t
	p = sx - 3*t*(sx - c1x) + 3*t**2*(sx + c2x - 2*c1x) + t**3*(-sx + 3*c1x - 3*c2x + ex)
	#Calculate y coordinate for current value of t
	q = sy - 3*t*(sy - c1y) - 3*t**2*(-sy + 2*c1y - c2y) + t**3*(-sy + 3*c1y - 3*c2y + ey)
	#Append y and x values to coordinate lists
	bezier_y_list.append(round(q,3))
	bezier_x_list.append(round(p,3))

#Plot bezier curves
bezier_plot = plt.plot(bezier_x_list, bezier_y_list, color = 'black', linewidth = '2')

#Combine x and y coordinates into lists for ease of plotting below
x_coordinates = [sx, c1x, c2x, ex]
y_coordinates = [sy, c1y, c2y, ey]

#Plot input points with their names
for j, name in enumerate(points_names):
	x_point = x_coordinates[j]
	y_point = y_coordinates[j]
	plt.scatter(x_point, y_point, marker = 'x', color = 'red')
	plt.text(x_point+0.1, y_point, name, fontsize=9) 

#Add graph and axis titles
plt.title("Cubic Bezier Curve")
plt.xlabel("x")
plt.ylabel("y")

#Clear file contents if it exists
open("bezier.txt", "w").close()

#Create and open output text file
output_file = open("bezier.txt", "w")

for x in range(len(t_values)):
	#Create output string
	output_str = "t= " + str(t_values[x]) + ", (" + str(bezier_x_list[x]) + ", " + str(bezier_y_list[x]) + ") \n"
	#Print t values and coordinates to console
	print(output_str)
	#Write same values to output file
	output_file.write(output_str)

#Close file
output_file.close()

#Show plot
plt.show(bezier_plot)