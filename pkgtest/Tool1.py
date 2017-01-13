# coding:utf-8


def tool1():
    print 'tool1'


if __name__ == "__main__":
    print u"直接执行"
elif __name__ == "Tool1":
    print u"import 执行"
else:
    print u"name:" + __name__





