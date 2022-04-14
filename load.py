# load file
data = []
count = 0
sum_len = 0
with open('reviews.txt', 'r') as reviews:
	for line in reviews:
		data.append(line.strip())
		count += 1
		if count % 5000 == 0:
			print('loading...', count, 'reviews')
print("總共有", len(data), "筆評論")
for comment in data:
	sum_len += len(comment)
print("評論平均字數為:", sum_len / len(data))