import csv
# file=open('products.csv','w')
# #create csv writer
# csv_writer=csv.writer(file)
# csv_writer.writerow(['pid','pname'])
# csv_writer.writerow([111,'AAA'])
# #
# f=open('products.csv','a')
# r=csv.writer(file)
# r.writerow([222,'BBB'])


#csv reader
f=open('products.csv','r')
data=csv.reader(f)
for row in data:
    for rec in row:
        print(rec,end=' ')
    print()







# file.close()
