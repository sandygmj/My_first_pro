#creat a mapping of state to abbrevation
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}

#creat a basic set of states and some cities in them
cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print("-"*10)
print("NY states has:",cities['NY'])
print("OR states has:",cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbrevation is:",states['Michigan'])
print("Florida's abbrevation is:",states['Florida'])

#do it by using the state then cities dict
print('-'*10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has",cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state, abbrev in states.items():
	print("%s is abbreviated %s" % (state,abbrev))

#print every city in state'
print('-'*10)
for abbrev,city in cities.items():
	print("%s has the city %s" % (abbrev,city))

#now do both at the same time
print('-'*10)
for state,abbrev in states.items():
	print("%s state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev]))

print('-'*10)

state = states.get('Texas',None)

if not state:
	print ("Sorry, no Texas.")

city = cities.get('TX','Does not exist.')
print("The city for the state 'TX' is: %s" % city)

print (states.pop('Oregon'))    #字典在使用pop时必须要指定，要pop的‘键’的名称，因为字典是无序存放的
print(states)                   #list列表则不同pop没有参数的情况下，pop的就是列表的最后一个元素。