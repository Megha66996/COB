## N.MEGHANA PHASE 1 -TASK 1
def countUniqueWords(fileName):
	file = open(fileName, 'r')
	read_file = file.read().lower()
	words_in_file = read_file.split()

	count_map = {}
	for i in words_in_file:
		if i in count_map:
			count_map[i] += 1
		else:
			count_map[i] = 1
	count = 0

	for i in count_map:
		if count_map[i] == 1:
			count += 1
	file.close()
	return count



with open("meghana.txt", "w") as file:
	file.write("orem Ipsum is simply dummy text of the printing and typesetting industry\
	Lorem Ipsum has been the industry's standard dummy text ever since the 1500s \
	thought and well explained solutions\
	for selected questions")

print('Number of unique words in the file are:',
	countUniqueWords('meghana.txt'))