
class Province:
    # 静态字段
    country ＝ '中国'
    def __init__(self, name):
        # 普通字段
        self.name = name
        
# 直接访问普通字段
obj = Province('河北省')
print obj.name
# 直接访问静态字段
Province.country

class Foo:
    def __init__(self, name):
        self.name = name
    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """
        # print self.name
        print '普通方法'
    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print '类方法'
    @staticmethod
    def static_func():#静态方法不能访问类变量+实例变量,无需实例化就能使用
        """ 定义静态方法 ，无默认参数"""
        print '静态方法'
f = Foo()
f.ord_func()# 调用普通方法
f.static_func()
f.class_func()#报错！
Foo.class_func()# 调用类方法
Foo.static_func()# 调用静态方法
