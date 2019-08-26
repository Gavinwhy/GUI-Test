import sys


# 类反射
class clsDriven:

    def driven(self, mod, mtd):
        # 类反射灵活引包,调用用例,执行测试 - 03
        __import__('cases.' + mod)
        model = sys.modules['cases.' + mod]
        obj = getattr(model, str(mod))
        mtd = getattr(obj(), str(mtd))
        return mtd
