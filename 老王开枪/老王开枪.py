# 人：
#     属性
#         hp
#         姓名
class Ren(object):
    def __init__(self,name_temp):
        super(Ren,self).__init__()
        self.name = name_temp
        self.hp = 100
        self.gun = None
    def __str__(self):
        if self.gun:
            return "角色的名称是%s，他的HP是：%d, 枪的信息为：%s " % (self.name, self.hp,self.gun)
        else:
            return "角色的名称是%s，他的HP是：%d,他手上没有枪！ "%(self.name,self.hp)

    def anzhuang_zidan(self,danjia_temp,zidan_temp):
        """把子弹装到弹夹中"""
        #弹夹中要保存子弹的数量
        danjia_temp.zhuangdan(zidan_temp)
    def anzhuang_danjia(self,gun_temp,danjia_temp):
        """把弹夹安装到抢中"""
        #枪。保存（弹夹）
        gun_temp.anzhuang_danjia(danjia_temp)
    def naqiang(self,qiang_leixing):
        self.gun = qiang_leixing
    #开枪的方法
    def kaiqiang(self,diren):
        """让枪发射子弹去打敌人"""
        #枪.开火（敌人）
        self.gun.fire(diren)

    def diaoxue(self,weilei):
        """根据子弹的威力去减掉hp"""
        self.hp -= weilei

# 枪：
#     属性
#         型号
class Gun(object):
    def __init__(self,leixing):
        super(Gun,self).__init__()
        #记录枪的类型，例如ak47，m46等
        self.leixing = leixing
        self.danjia = None #用来记录弹夹对象的引用

    def anzhuang_danjia(self,danjia_temp):
        """用一个属性来保存这个弹夹的值"""
        self.danjia = danjia_temp
    def __str__(self):
        if self.danjia:
            #self.danjia 会去直接调用弹夹（Danjia类）类的--str--方法
            #return "这是一个【%s】枪！\n 枪中的弹夹信息为：%s"%(self.leixing,self.danjia)
            return "这是一个【%s】枪！\n%s"%(self.leixing,self.danjia)
        else:
            return "这是一把【%s】枪！\n 枪中没有弹夹！"%(self.leixing)
    def fire(self,diren):
        """枪从弹夹中获取一发子弹然后子弹击中敌人"""
        #先从弹夹中取出子弹,弹夹弹出一个子弹

        zidan_temp = self.danjia.tanchu_zidan()

        #让这个子弹去伤害敌人
        if zidan_temp:
            #需要在子弹类中创建方法
            zidan_temp.dazhong(diren)
        else:
            print("没有子弹了！！！")

# 弹夹：
#     属性
#         装弹容量
class Danjia(object):
    #标示能够存放多少子弹
    def __init__(self,max_num):
        super(Danjia,self).__init__()
        self.max_num = max_num #用来记录最大装弹量
        self.zidan_shuliang = [] #用来记录当前弹夹中的子弹数量
        #子弹安装到弹夹中
    def zhuangdan(self,zidan_shuliang):
        """将这颗子弹保存"""
        self.zidan_shuliang.append(zidan_shuliang)

    def __str__(self):
        return "弹夹的信息为：%d/%d\n最大装弹量为： %d"%(len(self.zidan_shuliang),self.max_num,self.max_num)
    def tanchu_zidan(self):
        """弹出最上面的那颗子弹"""
        if self.zidan_shuliang:
            return self.zidan_shuliang.pop()
        else:
            return None

# 子弹：
#     属性
#         攻击力
class Zidan(object):
    #写子弹的一些属性和方法
    def __init__(self,weili):
        super(Zidan,self).__init__()
        self.weili = weili
    def dazhong(self,diren):
        """让敌人掉血"""
        #敌人.掉血（一颗子弹的威力）
        diren.diaoxue(self.weili)

def main():
    """用来控制整个程序的流程"""
    laowang = Ren("-=+老王+=-")
    qiang = Gun("AK47")
    danjia = Danjia(20)
    zidan = Zidan(10)
    #让老王把子弹安装到弹夹中（弹夹,子弹）
    for i in range(20):
        laowang.anzhuang_zidan(danjia,zidan)

    #老王把弹夹安装到枪中
    laowang.anzhuang_danjia(qiang,danjia)
    #老王拿枪
    laowang.naqiang(qiang)

    #测试弹夹的信息
    # print(danjia)
    #测试枪的信息
    # print(qiang)
    #测试老王拿枪
    # print(laowang)
    #创建敌人
    gebi_laosong = Ren("隔壁老宋")
    # print(gebi_laosong)
    #老王开枪攻打老宋
    #laowang.kaiqiang(diren)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    laowang.kaiqiang(gebi_laosong)
    print(gebi_laosong)
    print(laowang)
if __name__ == '__main__':
    #如果作为脚本运行，那么将先执行main函数
    main()
