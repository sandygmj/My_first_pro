formatter = "%r %r %r %r"

print (formatter % (1,2,3,4))
print (formatter % ("one","two","three","four"))
print (formatter % (formatter,formatter,formatter,formatter))
print (formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",#此行输出时会出现双引号，因为句子中间有单引号出现。
	"So I said goodnight."))