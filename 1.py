import numpy as np
#import pylab as pl
import matplotlib # 注意这个也要import一次
import matplotlib.pyplot as pl
import matplotlib.font_manager as fm
myfont = matplotlib.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')

t=np.arange(0.0,2.0*np.pi,0.01)
s=np.sin(t)
z=np.cos(t)
pl.plot()
pl.plot(t,s,label="正弦曲线")
pl.plot(t,z,label="余弦曲线")
pl.legend(prop=myfont)

pl.xlabel(u'X-变量',  fontproperties=myfont) # 这一段
pl.ylabel(u'y-变量',  fontproperties=myfont) # 这一段


pl.title('sin-cos函数图像',fontproperties=myfont)
pl.show()

#==================================