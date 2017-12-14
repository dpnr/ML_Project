import testclass

example = testclass.test(['1','2','3'],['4','5','6'])
print(example.getfistvar())
print(example.secondvar)
firstvar = example.getfistvar()[:]
print(firstvar)
print('delete from local copy')
firstvar.remove('1')
print(firstvar)
print(example.getfistvar())