#
# Exercise 1
#
elev.open()
new = RasterRow('new')
new.open('w', overwrite=True)
for row in elev:
    new.put_row(row * (row > 100))
new.close()