from pylab import *

price = [39.5, 39.9, 45.4, 38.9, 33.34]
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.barh(range(5), price, align='center', color='black', alpha=0.5)
plt.xlabel('price')
plt.yticks(range(5), ['Amazon', 'Dangdang', 'BooksChina', 'Jingdong', 'Tianmao'])
plt.xlim([32, 47])
plt.title('Book Price Comparsion')
for x, y in enumerate(price):
    plt.text(y + 0.1, x, '%s' % y, va='center')
plt.show()
