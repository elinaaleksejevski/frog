import numpy as np
import matplotlib
import matplotlib.pyplot as plt


fail=open(r"C:\Users\User\Documents\visualstudio\text_num.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()

plt.grid(True)
color_rectangle = np.random.rand(7, 3)
plt.bar(mas1,mas2,color=color_rectangle)  
plt.title("Данные о ИТ безопасности")
plt.tick_params(labelrotation=20)
plt.subplots_adjust(left=0.125, bottom=0.3, right=0.9, top=0.88, wspace=0.2, hspace=0.2)
plt.show()

x1=np.arange(-7,7,0.1)
x2=np.arange(-7,7,0.1)
x3=np.arange(-6.8,-2,0.1)
x4=np.arange(2,6.8,0.1)
x5=np.arange(-5.8,-2.8,0.1)
x6=np.arange(2.8,5.8,0.1)
x7=np.arange(-4,4,0.1)
x8=np.arange(-5.2,5.2,0.1)
x9=np.arange(-7,-2.8,0.1)
x10=np.arange(2.8,7,0.1)
x11=np.arange(-7,0,0.1)
x12=np.arange(0,7,0.1)
x13=np.arange(-7,-4.5,0.1)
x14=np.arange(4.5,7,0.1)
x15=np.arange(-3,3,0.1)

y1=-(3/49)*(x1**2)+8
y2=(4/49)*(x2**2)+1
y3=-0.75*((x3+4)**2)+11
y4=-0.75*((x4-4)**2)+11
y5=-((x5+4)**2)+9
y6=-((x6-4)**2)+9
y7=(4/9)*((x7)**2)-5
y8=(4/9)*((x8)**2)-9
y9=-(1/16)*((x9+3)**2)-6
y10=-(1/16)*((x10-3)**2)-6
y11=(1/9)*((x11+4)**2)-11
y12=(1/9)*((x12-4)**2)-11
y13=-((x13+5)**2)
y14=-((x14-5)**2)
y15=(2/9)*((x15)**2)+2

plt.subplots()
plt.title('Лягушка')
plt.plot(x1,y1,'--c',linewidth=2,label='Frog')
plt.plot(x2,y2,'--c',linewidth=2)
plt.plot(x3,y3,'--c',linewidth=2)
plt.plot(x4,y4,'--c',linewidth=2)
plt.plot(x5,y5,'--c',linewidth=2)
plt.plot(x6,y6,'--c',linewidth=2)
plt.plot(x7,y7,'--c',linewidth=2)
plt.plot(x8,y8,'--c',linewidth=2)
plt.plot(x9,y9,'--c',linewidth=2)
plt.plot(x10,y10,'--c',linewidth=2)
plt.plot(x11,y11,'--c',linewidth=2)
plt.plot(x12,y12,'--c',linewidth=2)
plt.plot(x13,y13,'--c',linewidth=2)
plt.plot(x14,y14,'--c',linewidth=2)
plt.plot(x15,y15,'--c',linewidth=2)

plt.grid()
plt.legend()

plt.savefig("my_image.png")
plt.show()