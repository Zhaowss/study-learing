---
       typora-root-url: ./image
---

Java:

## 初识命令行cmd:

常见的cmd的命令

1. 盘符名称+： 切换盘
2. dir 查看当前路径下的内容
3. cd 目录 切换到单级目录
4. Cd .. 回退到上一级的目录
5. cd 目录1\目录2\目录3\ 切换多级目录
6. Cd \回退到我们的盘符
7. Cls 清屏
8. exit  退出我们的命令提示符

环境变量：用于记录我们的的一些路径

为什么要配置环境变量：

当我们想去在任意的目录下打开制定的文件的时候，就可以吧软件的路径设置在环境变量之中

## Java入门：

编译的理解：将代码转换成计算机可以识别的代码

Javac 编译我们的Java的源文件

然后通过Java运行我们编译后的文件

![image-20230426144007074](../../../../Library/Application Support/typora-user-images/image-20230426144007074.png)

###### 环境变量：

为什么配置我们的path的环境变量的呢？

其实我们就是为了让我们的Java中的Javac和Java这个写入到环境变量中，我们就可以在任何环境中都能够使用

###### Java能干嘛？

Javase: java语言的基础

###### javame:

用于嵌入式

###### Javaee:

用于网站的开发：

###### java跨平台：

高级语言的编译运行的方式：编程，编译，运行

编译性语言：C

无法跨平台：

解释性语言：python

混合性编译语言：JAVA

Java在运行的时候，编译的**.class的文件是运行在虚拟机里面的，而不是运行在我们的系统上**

![image-20230426145943448](../../../../Library/Application Support/typora-user-images/image-20230426145943448.png)

###### JRE和JDK：

JDK的全称：Java开发工具包

1. Jvm java 虚拟机

2. 核心类库

3. 开发工具

   开发工具的构成：

1. javac开发工具
2. Java运行工具
3. Java调试工具
4. Java内存分析工具

**JRE 是Java的运行环境**

JDK 包含了 JRE

## Java的基础语法：

### 注释：

单行注释

```java
//注释
```

多行注释

```java
/* 注释信息*/
```

文档注释

```Java
/** 注释信息 **/
```

```java
public class Main {
    //main方法，表示程序的主入口
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
    //作为输出的语句（打印我们的语句）
    //将其打印到我们的命令行
    /*java 的注释信息，我们将其保存在我们的文件中，
    */
}
```

#### 关键词：

###### class ：

用于创建或者定义一个类，而类是Java组成的最基本的组成单元

#### 字面量：

字面量的类型

1. 整数类型: 1 
2. 小数类型: 3.14
3. 字符串类型：“hello world”
4. 字符类型 : 'h'
5. 布尔类型: 只有俩个数值：true或者false
6. 空类型：null

```java
import java.util.TreeMap;
public class valuedemo1 {
    //这段代码主要是用于中变量的书写
    //整数
    public static void main(String[] args){
        //整数
        System.out.println(666);
        System.out.println(667);
        System.out.println(668);

        //小数
        System.out.println(1.93);
        System.out.println(2.12);
        System.out.println(3.16);

        //字符串
        System.out.println("黑马程序员");
        System.out.println("我是你爸爸");
        System.out.println("我是你爷爷");


        //字符
        System.out.println('h');
        System.out.println('x');
        System.out.println('z');

        //布尔
        System.out.println(true);
        System.out.println(false);
    }
}
```

特殊的符号：

```java
\t 制表符：
在打印的时候，把前面的字符串的长度补齐到8，或者8 的整数倍，
```

#### 变量：

```
数据类型 变量名字=数据值；
```

```java
public class valuedemo2{
    //这段代码主要是用于中变量的书写
    //整数
    public static void main(String[] args){
        //变量：
        //s数据类型：限定我们的变量
        int x=1;
        int y=3;
        double z=3.16;
        String num="hello world";
        System.out.println(z);
        System.out.println(num);
    }
}
```

#### 数据类型：

###### 基本数据类型：

| 整数     | byte      | -128---128             |
| -------- | --------- | ---------------------- |
|          | short     | -32768-32768           |
|          | int       | -2147483648-2147483648 |
|          | long      |                        |
| 浮点数   | **float** |                        |
|          | double    |                        |
| 字符     | char      | 0-65535                |
| 布尔变量 | Boolean   | Ture  false            |

#### 标识符：

硬性要求：

由数字和字母下划线和$构成

不能以数字起头

不能是关键字

区分大小写

软性的建议：

小驼峰命名法：方法变量

```java
规范一：
标识符是一个单词的时候全部小写
```

```
规范2:
标识符有多个单词的时候，第一个单词的首字母小写起小雨的单词的首字母全部大写
```

大驼峰命名法：类名：

```
规范一：标识符是一个单词的时候，首字母大写
```

```
规范二：标识符有多个的单词构成的时候，单个单词的首字母需要大写

```

#### 键盘的录入：

Java已经帮我写好scanner，这个类就可以接受键盘输入的数字

```java
import  java.util.Scanner;
public class valuedemo4 {
    //这段代码主要是用于中变量的书写
    //整数
    public static void main(String[] args){
        //变量的键盘的输入
        //创建对象，表示我们要开始使用这个类
        Scanner sc=new Scanner(System.in);
        //接受数据-开始真正的干活
        System.out.println("请输入：");

        int i=sc.nextInt();

        System.out.println(i);

    }
}
```

### 运算符

```java
package com.it.demo1;

public class demo2 {
    public static void main(String[] args) {
        //加法
        int a=10;
        int b=3;
        double x=10.0;
        System.out.println(a+b);

        //减法
        System.out.println(a-b);

        //乘法
        System.out.println(a*b);

        //除法

        System.out.println(a/b);

        System.out.println(x/b);

        //取余
        System.out.println(a%b);
    }
}

```

##### 隐式转化和强制转换

隐式转换：自动类型提升，小范围转变为大范围,比如byte 和  short以及chart 会自动进行隐式的类型转换，将类型转换提升为int类型

隐式转换的俩种提升的规则：

取值范围小的和取值范围大的，小的会一般先提升为大的，在运算

byte short char 三种类型的数据在运算的时候，都会直接提升为int,然后在进行运算
$$
byte<short<int<long<float<double
$$
**强制转换：大范围到小范围；**

 将取值范围大的数值复制给取值范围小的变量，需要进行强制转换

格式：

```
目标类型名 变量名=（目标数据类型）被强制转换的类型
```

##### 字符串运算：

字符串的“+”这个操作：
**当“+”操作中出现字符串时**，这歌”+“实际上是一个字符串的连接符，而不是运算符，会将前后的字符串香链接，产生新的字符串

连续的加的时候，从左到右逐个进行的；

##### 自增自减运算：

```java
package com.it.demo1;

public class demo4 {
    public static void main(String[] args) {
        int a=10;
        a++;
        System.out.println(a);
        ++a;
        System.out.println(a);
        a--;
        System.out.println(a);
        --a;
        System.out.println(a);
    }
}
```



参与运算：

```java
package com.it.demo1;

public class demo4 {
    public static void main(String[] args) {

        int x=10;
        int z=10;
        int b=x++;
        int c=++z;
        System.out.println(b);
        System.out.println(c);
        System.out.println(x);
    }
}
```



输出：

```
b:10
c:11
x:11
```

自增自减的运算的时候：

放在后面，先用后加

放在前面，先加后减

##### 赋值运算符：

###### 运算后赋值

并且+=，-=，*=，/=，%=中都隐含了强制类型转换；

比如：

```java
short s=1;
s+=1
//等价于s=s+1;
//平常都会先将s提升为int类型的
//然后int类型的s和1加
//再将结果复制给short s未发生报错。其实是隐含了强制类型转转；
s=short(s+1)

```



```java
package com.it.demo1;

public class demo5 {
    public static void main(String[] args) {
        int a1=10;
        int b1=10;
        a1+=b1;
        System.out.println(a1);
        int a2=10;
        int b2=10;
        a2-=b2;
        System.out.println(a2);

        int a3=10;
        int b3=10;
        a3*=b3;
        System.out.println(a3);

        int a4=10;
        int b4=10;
        a4/=b4;
        System.out.println(a4);

        int a5=10;
        int b5=10;
        a5%=b5;
        System.out.println(a5);
    }
}

```

```java
1:20
2:0
3:100
4:1
5:0
```

##### 关系运算符：

| 符号 | 说明             |
| ---- | ---------------- |
| ==   | 判断是否相等     |
| !=   | 判断是否不等     |
| >    | 判断是否大于     |
| <    | 判断是否小于     |
| >=   | 判断是否大于等于 |
| <=   | 判断是否小于等于 |

```java
package com.it.demo1;

public class demo6 {
    public static void main(String[] args) {
        int a1=10;
        int b1=10;
        int c1=20;
        System.out.println(a1==b1);
        System.out.println(a1==c1);
        System.out.println(a1>=c1);
        System.out.println(a1<=c1);
    }
}
//true
//false
//false
//true

```

##### 逻辑运算符：

| 符号 | 作用     |
| ---- | -------- |
| &    | 逻辑与   |
| ｜   | 逻辑或   |
| ^    | 逻辑异或 |
| ！   | 逻辑非   |

```java
package com.it.demo1;

public class demo6 {
    public static void main(String[] args) {

        System.out.println(true & true);
        System.out.println(true | true);
        System.out.println(true ^ true);
        
    }
}

```

##### 短路逻辑运算符：

| 符号          | 作用                                               |
| ------------- | -------------------------------------------------- |
| &&（短路与）  | 前面的正确才可以运算后面的                         |
| ｜｜(短路或） | 左边False 才会运行后面的，左边为True的时候直接结束 |

##### 三元运算符：

三元运算符的格式：

格式：关系表达式？表达式1：表达式2；

实例：

```
c=a > b ? a:b;
```

```java
package com.it.demo1;

public class demo7 {
    public static void main(String[] args) {

        int a=10;
        int b=20;
        System.out.println(a>b?a:b);

    }
}

```

##### 判断和循环：

```java
package com.it.demo1;

public class demo8 {
    public static void main(String[] args) {

        int a=10;
        int b=20;
        if (a>b){
            System.out.println("a>b");
        }
        else 
            System.out.println("a<b");
    }
}

```

```java
package com.it.demo1;

public class demo8 {
    public static void main(String[] args) {

        int a=10;
        int b=20;
        if (a>b){
            System.out.println("a>b");
        } else if (a==b) {

            System.out.println("a==b");
        } else
            System.out.println("a<b");
    }
}

```

```java
package com.it.demo1;

public class swichdemo9 {
    public static void main(String[] args) {

        String noodle="兰州拉面";
        switch (noodle)
        {
            case "兰州拉面":
                System.out.println("兰州拉面");
                break;
            case "武汉热干面":
                System.out.println("武汉热干面");
                break;//break不能省略。不然后导致case穿透
            case "北京蘸酱面":
                System.out.println("北京蘸酱面");
                break;
            case "油泼面":
                System.out.println("油泼面");
                break;
            default:
                System.out.println("吃个屁");
                break;

        }
    }
}
//执行的流程
//首先还是会拿着我们的那表达式的值和我们的每一个case进行匹配
//如果匹配上，那么就会执行对应的预聚体，如果发现了break就会跳出
//如果没有发现break的时候，就会继续执行下一个的case的语句体

```

```java
package com.it.demo1;

public class swichdemo9 {
    public static void main(String[] args) {
//
//        String noodle="兰州拉面";
//        switch (noodle)
//        {
//            case "兰州拉面":
//                System.out.println("兰州拉面");
//                break;
//            case "武汉热干面":
//                System.out.println("武汉热干面");
//                break;
//            case "北京蘸酱面":
//                System.out.println("北京蘸酱面");
//                break;
//            case "油泼面":
//                System.out.println("油泼面");
//                break;
//            default:
//                System.out.println("吃个屁");
//                break;
//
//        }
        int number=1;
        switch (number){
            case 1 -> System.out.println("1");
            case 2 -> System.out.println("2");
            case 3 -> System.out.println("3");
            case 4 -> System.out.println("4");
            default -> System.out.println("没有选项");

        }
    }
}

```

##### 循环结构：

###### for循环

```java
package com.it.demo1;

public class fordemo9 {
    public static void main(String[] args) {
     for (int i=0;i<10;i++){
         System.out.println(i);
     }
    }
}

```

```java
package com.it.demo1;

public class fordemo9 {
    public static void main(String[] args) {
     for (int i=0;i<10;i++){
         System.out.println(i);
     }
        System.out.println("--------------------");
     for (int i=9;i>=0;i--){
         System.out.println(i);
     }
    }

}

```

累加的算法：

```java
package com.it.demo1;

public class fordemo10 {
    public static void main(String[] args) {
        int sum=0;
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
            sum+=i;
        }
        System.out.println(sum);
    }
}

```

###### while：

```java
package com.it.demo1;

public class whiledemo11 {
    public static void main(String[] args) {
        int i=0;
        while(i<10)
        {
            i++;
            System.out.println(i);
        }
    }
}

```

###### 而二者循环的区别：

for循环中的控制循环的变量，归属于我们的for循环的语法结构，运行结束后，直接就不能再被访问

while循环，控制循环的变量定义在循环的外面因此在循环结束后可以继续访问shiyong

###### 从开发的角度：

for循环一般是在我们知道循环的次数和循环的范围上使用

while循环；我们不知道循环的次数和范围，只知道循环的约束条件

###### 力扣算法：回文数

```java
package com.it.demo1;

public class whiledemo3 {
    //判断回文数：
    //如果一个x是回文整数，打印ture,否则打印False
    //解释；回文数指，正序和逆序都是一样的整数
    //例如121
    //把原来的数字倒过来和原始的做比较
    public static void main(String[] args) {

        int x=12321;
        int y=x;
        int num=0;
        //定义数字
        //不知道的时候采用while
        while(x!=0){
            int ge=x%10;
            x=x/10;
            num=num*10+ge;
        }
        System.out.println(num);
        if(y==num) {
            System.out.println("是回文数");
        }
        else
            System.out.println("不是回文数");
        }

    }

```

###### 力扣算法：不用除法和取余数

```python
package com.it.demo1;

public class whiledemo4 {
    //给定俩个整数，被除数和出书相除，要求不使用除法。得到商和余数

    public static void main(String[] args) {

        int a=201;
        int b=10;
        int count=0;
        while (a>b){

            a-=b;
            count++;

        }
        System.out.println(a);
        System.out.println(count);
    }


    }


```

##### 无限循环：

三种形式：

```java
for(;;){
}

```

```java
while(true){

}
```

```java
do{

}while(true)
```

##### 跳转程序语句：

```java
package com.it.demo1;

public class whiledemo6 {
    //给定俩个整数，被除数和出书相除，要求不使用除法。得到商和余数

    public static void main(String[] args) {

     for (int i=1;i<=5;i++){
         if(i==3)continue;
         System.out.println("小老鼠吃第几"+i+"个包子");
     }
    }
    }

```

输出：

```java
小老鼠吃第几1个包子
小老鼠吃第几2个包子
小老鼠吃第几4个包子
小老鼠吃第几5个包子
```

```java
package com.it.demo1;

public class whiledemo6 {
   
    public static void main(String[] args) {

     for (int i=1;i<=5;i++){
         if(i==3)break;
         System.out.println("小老鼠吃第几"+i+"个包子");
     }
    }
    }


```

输出：

```
小老鼠吃第几1个包子
小老鼠吃第几2个包子
```

###### 七的倍数：

```java
package com.it.demo1;

public class whiledemo7 {
    //逢7过
    //实现方法：1-100
    //包含7，个位或者十位包含7跳过
    //要求含有7⃣️或者七得倍数的直接跳过

    public static void main(String[] args) {
    for(int i=1;i<=100;i++)
    {
        if(((i%10)==7)||((i/10%10)==7)||(i%7==0)){
            System.out.println("过");
            continue;
        }
        System.out.println(i);
    }

    }
    }


```

###### 平方根：

```java
package com.it.demo1;

public class whiledemo8 {
    //计算其输入的数的平方根并输出。
    //结果要求保留整数部分

    public static void main(String[] args) {
        int i=0;
        int count=0;
        int x=16;
        while (count<x) {
            count = i * i;
            if(count>x){
                System.out.println(i-1);
            } else if (count==x) {
                System.out.println(i);
            }
            else {
                i++;
            }

        }
        
    }
    }

```

###### 判断是否为质数：

```java
package com.it.demo1;

public class whiledemo9 {
    //判断是否为质数

    public static void main(String[] args) {

        int x=16;
        int count=2;
        while (count<=x-1) {
            if(x%count==0) {
                System.out.println("x=" + x + "是质数");
                break;
            }
            count++;
        }
        
    }
    }


```

```java
package com.it.demo1;

public class whiledemo9 {
    //判断是否为质数

    public static void main(String[] args) {

        int x=16;
        int count=2;
        boolean flag=true;
        while (count<=x-1) {
            if(x%count==0) {
//                System.out.println("x=" + x + "是质数");
                flag=false;
                break;
            }
            count++;
        }
        if(flag==false){
            System.out.println("x=" + x + "不是质数");
        }
    }
    }


```

###### 优化的判断质数：

#### 数组：

##### 数组的介绍：

数组是一种容器，存储同种数据类型的多个值；

数组容器在存储数据的时候需要结合隐式转换；

建议：容器的类型和存储的数据类型需要保持一致；

##### 数组的定义和初始化：

```
格式：
数据类型 [] 数组名
格式：
数据类型 数组名[]
```

###### 数组的初始化：

```java
数据类型[] 数组名= new 数据类型[] {元素1，元素2，元素3}
```

实例：

```java
package com.it.demo2;

public class demo1 {
    //数组的容器
    public static void main(String[] args) {
        int array[]=new int[]{11,12,13};
        double array2[]=new double[]{12.0,3.0,14.0};
        System.out.println(array[0]);
        ////简化的形式
        int array3[]={12,13,165,14};
        System.out.println(array3[1]);
    }


}

```

```JAVA
package com.it.demo2;

public class demo2 {
    //数组的容器
    public static void main(String[] args) {
        int array[]=new int[]{11,12,13};
        double array2[]=new double[]{12.0,3.0,14.0};
        String array3[]=new String[]{"张三","李四","王武"};
        for(int i=0;i<3;i++){
            System.out.println("------------------------");
            System.out.println("学生姓名："+array3[i]);
            System.out.println("学生年龄："+array[i]);
            System.out.println("学生身高："+array2[i]);
            System.out.println("------------------------");
        }
    }
    
}

```

##### 数组的地址值和元素的访问：

```java
数组的地址：
[I@2f92e0f4
//表示是一个数组
//I表示的是数据的类型
//2f92e0f4 数组的地址


```

##### 数组的动态初始化：

初始化的时候只制定数组的长度，有系统为数组提供初始数值；

```JAVA
系统 的随机初始化：

int 默认制定为0

double 默认指定为0.0

字符类型 默认指定为空格

布尔类型 false


```

格式：数据类型 [] 数组名=new 数据类型[数组的长度]

```java
package com.it.demo2;

public class demo3 {
    //数组的容器
    public static void main(String[] args) {
        int array[]=new int[]{11,12,13};
        int array4[]=new int[28];//动态初始化只需要指定数组的长度

        for(int i=0;i<28;i++){
            System.out.println("------------------------");
            array4[i]=i;
            System.out.println(array4[i]);
            System.out.println("------------------------");
        }
    }
}


```

#### 方法：

##### 简单的方法 的定义以及调用：

```
最简单的方法的定义：

带参数的方法的定义：

带有返回值的方法的定义：
```

```java
package com.it.demo2;

public class demo3 {
    //数组的容器
    public static void main(String[] args) {
        int sum=0;
        MyFun();
        MyFun2(2);
        sum=MyFun3(3);
        System.out.println(sum);

    }
    public static void MyFun(){
        System.out.println("我的方法");
    }
    public static void MyFun2(int i){
        System.out.println("我的输入的数字"+i);
    }
    public static int MyFun3(int i){
        int sum=0;
        sum=i*2;
       return sum;
    }
}

```

##### 方法的重载：

**同名不同参，构成的式方法的重载**

在同一个类中，定义了很多个同名的方法，这些tongi名字的方法具有同中的功能

**每个方法具有不同的参数的类型和参数的个数，这些同名的方法就构成了重载的关系**

```java
package com.it.demo3;

public class demo3 {
    //数组的容器
    public static void main(String[] args) {
        int sum=0;
        int a=10;
        int b=10;
        int c=10;
        double x=1.0;
        double s=2.0;
        System.out.println(sum(a,b));
        System.out.println(sum(a,b,c));
        System.out.println(sum(x,s));
    }
    public static int sum(int a, int b){
        int sum=0;
        sum=a+b;
        return sum;
    }
    public static int sum(int a, int b,int c){
        int sum=0;
        sum=a+b+c;
        return sum;
    }
    public static double sum(double  a, double  b){
        double  sum=0;
        sum=a+b;
        return sum;
    }
}
```

数组的遍历：

```java
package com.it.demo3;

public class demo2 {
    //数组的容器
    public static void main(String[] args) {
     int array[]=new int[100];
        for (int i = 0; i < array.length; i++) {
            array[i]=i;
        }
        sum(array);
    }
    public static void sum(int[] array) {
        for(int i=0;i< array.length;i++){
            System.out.println(array[i]);
        }
    }
}
```

###### 寻找最大的值：

```java
package com.it.demo3;

public class demo3 {
    //数组的容器
    public static void main(String[] args) {
     int array[]=new int[100];
     int max=0;
        for (int i = 0; i < array.length; i++) {
            array[i]=i;
        }
        max=Getmax(array);
        System.out.println(max);
    }

    public static int Getmax(int[] array) {
        int max= array[0];
        for(int i=0;i< array.length;i++){
           if(array[i]>max) {
               max = array[i];
           }


            }
        return max;
        }


    }



```

###### 判断数组中是否存在一个数字

```java
package com.itheima.test;

public class test {
    public static void main(String[] args) {
        int[] array={1,2,3,4,5,6,7,8,9,10};
        //判断是否在数组中存在一个数字

        System.out.println( constain(array,11));

    }
    //定义一个方法
    public static boolean constain(int[] array,int number){
        for (int i = 0; i < array.length; i++) {
            if (array[i]==number)
                return true;
        }
        //判断是否存在
        return false;
    }
}

```

**这里需要提下return和break的区别所在：**

return和循环不存在什么关系，和方法相关，是指结束方法之后返回结果；

break和switch关键字相关，或者结束循环

##### 方法调用的基本内存原理;

首先JVM会在运行的时候占用一定的计算机的内存；

##### Java的内存分配：

Java内存分配主要是5个部分

栈；堆；方法区；本地方法栈；寄存器

（1）栈：方法运行时使用的内存，比如main方法运行，进入方法栈中执行

（2）堆：存储对象或者数组，new来创建的，都存储在堆内存

（3）方法区：存储可以运行的class文件（当加载一个类时，这个类的字节码文件就会被加载到方法区）

（4）本地方法栈：JVM在使用操作系统功能的时候使用，（与开发无关）

（5）寄存器：给CPU使用，（与开发无关）

方法调用的基本原理：先入后出的栈，栈是先入后出的类型

##### 方法调用的时候数据类型的传递：

###### 基本数据类型：

###### 数据值是存储在自己的空间中，栈中

特点：赋值给其他变量，赋的是真实的值。当b变量修改其本身的值后，a变量的值不发生改变。

###### 引用数据类型：

######  数据值是存储在其他空间中的，自己空间中存储的是地址值。（本质是使用别人空间的东西）

特点：赋值给其他变量，**赋的是地址值**。当b变量修改其本身存储的地址所指向的内存中的值时，a变量本身存储的地址所指向的内存中的值也会发生改变，因为a和b变量存储的地址都指向同一块内存，指向的是同一个东西。


##### **3. 方法传递数据的内存原理：**

传递基本数据类型时，传递的是真实的数据，形参的改变，不影响实际参数的值

传递引用数据类型时，传递的是地址值，形参的改变，影响实际参数的值。

### Java面向对象：

#### 面向对象的介绍：

###### 学习的内容：

学习获取已有的对象并且使用

学习自己设计对象并使用

#### 类和对象：

类：设计图,是对对象共同的特征的描述

对象：是真实存在的具体东西

Java中必须先设计我们的类，再去设计具体的对象

##### 如何定义类：

```
public class 类名{

成员变量(代表属性，一般为名词)
成员方法(代表行为，一般为动词)
构造器
代码块
内部类
}
```

举例：

```
public class phone(){
string brand;
double price;
public void call(){}
public void playgame(){}

}
```

首先定义我的对象：

```
package com.itheima.test;

public class Phone
{
   String brand;
   double price;

   public void call(){
       System.out.println("call my phone");

   }
    public void playgame() {
        System.out.println("play my game");
    }
}

```

调用定义得对象类以及里面的方法：

```java
package com.itheima.test;

public class Phonetest {
    public static void main(String[] args) {
        //创建手机的对象
        Phone p=new Phone();

        //给手机幅值的操作
        p.brand="apple";
        p.price=1800;
        System.out.println(p.brand);
        System.out.println(p.price);


        //掉用手机中的方法v
        p.call();
        p.playgame();

    }
}

```

类和对象分别是什么呢？

首先我们定义的一个类；这个类其实是我们的共同特征的描述；

对象：是我们事实存在的具体的实例

##### 类的注意事项：

###### 定义类的具体的一些事项：

```java
用来描述我们一类事物的类，专业的叫做：JavaBean类

在javabean类中，是一般不写main的方法的；

在之前的操作中 ，**我们加入的main方法的类，叫做测试类**

我们可以在测试类中创建javabean 类的对象，并进行赋值调用
```

```java
一个Java文件中我们可以创建多个class,但是只能用一个类是用public来修饰，且public修饰的类必须作为我们的文件名
```

###### 成员变量的命令格式；

基本类型：八大基本数据类型 

```java
short byte int long float double boolean char
```

引用类型：

```JAVA
类 接口 数组 String 基本类型的封装类均属于是我们的引用数据类型
```



#### 封装（重要）：

面向对象的三大特征之一：封装 继承 多态

对象代表什么，就得封装对应的数据，并提供数据所对应的行为

封装本质上就是告诉我们面向对象的设计：

怎么设计对象呢？

封装的好处：

便于我们快速的开发

##### private 关键词

是一个权限的修饰符

可以修饰成员

被private修饰的只可以在本类中才能访问

```java
a:是一个权限修饰符

b:可以修饰成员变量和成员方法

c:被其修饰的成员只能在本类中被访问

private 私有的 是一个权限修饰符，可以修饰成员变量和成员方法，被修饰后，只能在本类中访问，外界无法访问。

public 公共的 是一个权限修饰符，可以修饰类，可以修饰成员变量，可以修饰成员方法，被修饰的成员在任何地方都可以访问

2.如果成员变量被private修饰了(私有化)那么我们怎么才可以在其他类中访问被修饰的成员变量呢？

我们可以借助set方法对成员变量赋值，get方法获得成员变量，
    
   当我们的成员的变量被私有的时候，这就意味着我们无法利用我们的外部去访问该类的变量，因此这就是需要我们设计对应的方法去操作内部的变量。
    
```

举例：其实本质上就是在类中进行变量的操作，具体的实现就是使用我们定义对象的方法。

```java
package com.itheima.test;

public class Girlfriend {
    private String name;
    private int age;
    private String gender;
    private double height;
    int weight;
    public void setName(String a){
            name=a;
    }
    public String getName(){
        return name;
    }
    public void setGender(String a){

        gender=a;

    }
    public String getGender(){
        return gender;
    }
    public void setHeight(double a){

        height=a;

    }
    public double getHeight(){
        return height;
    }
    public void set(int a){
        if(a>=18 && a<=50)
        {
            age=a;
        }
    }
    public int get(){
       return age;
    }
    public void sleep(){
        System.out.println("女朋友在睡觉");
    }

    public void eat() {
        System.out.println("女朋友在吃饭");

    }

    public void fight(){
        System.out.println("女朋友在格斗");
    }
}

```

```java
package com.itheima.test;

public class Girlfriendtest {
    public static void main(String[] args) {
        Girlfriend p=new Girlfriend();
        p.setName("jiajia");
        p.setHeight(156);
        p.set(18);
        p.setGender("女");
        p.weight=120;
        System.out.println(p.getName());
        System.out.println(p.getHeight());
        System.out.println(p.get());
        System.out.println(p.getGender());
        System.out.println(p.weight);
        p.sleep();
        p.eat();
        p.fight();

        System.out.println("_________________________________________________");

        Girlfriend q=new Girlfriend();
        q.setName("yaya");
        q.setHeight(176);
        q.set(20);
        q.setGender("女");
        q.weight=120;
        System.out.println(q.getName());
        System.out.println(q.getHeight());
        System.out.println(q.get());
        System.out.println(q.getGender());
        System.out.println(q.weight);
        q.sleep();
        q.eat();
        q.fight();


    }
}
```

##### 成员变量和局部变量：

```java
package com.itheima.test;

public class Girlfriends1 {
成员变量
    private int age=100;

    public static void main(String[] args) {
      setAge();
    }
    public static void setAge() {
        局部变量
        int age = 10;
        System.out.println(age);
    }
}
代码的输出为10 而不是100？
原因： 就近原则
Java变量遵循的是就近的原则
    
```

```java
package com.itheima.test;

public class Girlfriends1 {

    private int age=100;
    public void setAge() {
        int age = 10;
        System.out.println(this.age);
    }
}
输出为100
    this指我们当前类的地址，使用this，哪个对象调用就是哪个对象的引用类型。
    
```

###### this的特性：

1. this的类型：那个对象调用，就是哪个对象的引用类型
2. this只能在成员方法中使用
3. 在成员方法中，this只能引用当前对象，不能再引用其它对象，具有final属性
4. this是成员方法第一个隐藏的参数，编译器会自动传递
5. this不能为空！！！

$$
Java中的this关键字表示对当前对象的引用，它用于区分实例变量和局部变量之间的命名冲突。
$$

#### 构造方法：

构造方法的格式：

```java
public class student{

修饰符  类名（参数）{
方法体；
}
}
```

**特点：**

构造方法：其实就是如何创建我们这个对象，也就是我们如何构造出我们的对象，这就需要我们使用带参数的有参构造和无参数的有参构造，这俩种的构造的方法就可以完成我们的对象的创建。

方法名字和类的名字是相同的，大小写也是一致的

没有返回值的类型

没有具体的返回的数值，不能又return带回结果数据

##### 代码的实现

###### 空参数构造：

```java
package com.itheima.test;

public class student {
    private String name;
    private int age;
    
    public student(){
        System.out.println("看看执行了吗");
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

```java
package com.itheima.test;

public class student_test {
    public static void main(String[] args) {
        student x=new student();

    }

}
```

###### 带参数的方法构造：

```java
package com.itheima.test;
public class student {
    private String name;
    private int age;
    public student(String name,int age){
        this.name=name;
        this.age=age;

    }
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

```java
package com.itheima.test;

public class student_test {
    public static void main(String[] args) {
        student x=new student("huangsan",12);
        System.out.println(x.getAge());
        System.out.println(x.getName());
    }

}

```

###### 构造方法注意事项：

构造方法的定义：

没有定义构造方法，系统将会给出一个默认的无参数的构造方法

如果定义了构造方法，系统将不在提供默认的构造的方法

构造方法的重载：

其实在定义的时候我们通常会把俩个都定义：

二者的方法名是一样的，但是参数不相同，叫做构造方法的重载

最推荐的方法：俩种构造的方法都一般会写上

#### 标准JavaBean

标准的Javabean类

类名必须见名知意

成员变量使用private修饰

至少提供俩种构造的方法

成员的方法

提供每一个成员变量的set 和 get

```java
JavaBean 是一种符合特定规范的 Java 类，用于在 Java 应用程序中封装数据和操作。它是一种用于表示可重用组件的编程约定，通常用于实现数据传输对象（Data Transfer Object，DTO）或数据模型。

JavaBean 类必须满足以下条件：
类必须是具有公共默认构造函数的具体类（不能是抽象类或接口）。
所有属性必须是私有的，并通过公共的 getter 和 setter 方法进行访问。
属性的命名必须遵循特定的命名规范（例如，属性 "name" 应该有对应的 "getName()" 和 "setName()" 方法）。
可以选择实现其他可选接口，如序列化接口（Serializable）。
  
JavaBean 的主要目的是提供一种简单的方式来封装数据，使其可以轻松地进行访问和操作。通过使用 getter 和 setter 方法，可以控制对属性的访问，并在必要时执行数据验证、计算或其他逻辑操作。这种封装性使得 JavaBean 在各种应用程序中广泛应用，包括图形用户界面（GUI）开发、持久化数据存储、远程方法调用等。

JavaBean 的设计原则是通过封装、私有化属性和提供公共的访问方法来实现封装和信息隐藏，同时提供了一种标准化的方式来创建可重用的组件，促进了面向对象编程的模块化和可维护性
```

#### 对象内存图

引用数据类型：

数值存储在其他的空间中，自己的空间中存储的是我们的地址的数值

特点：赋值给其他的变量，赋值的是地址值。


基本数据类型：

数据值存储在自己的空间中。

特点：赋值给其他的变量，也是赋的真真实的数值

##### This关键字的内存原理：

 this的本质其实是方法**调用者的地址的数值。**

##### 成员和局部：

成员变量：类中的方法之外的变量

局部的变量：方法之中的变量

所在的位置不相同：

成员变量：堆内存

局部变量：栈内存

生命周期不相同：

成员变量：对象创建的时候而存在

局部变量：对象方法的消失而消失

作用域：

成员变量：整个类

局部变量：方法内

##### 键盘输入的体系：

第一套体系：

nextInt():接受整数

nextDouble();接受小数

next():接受字符串

遇到空格，制表符，回车键停止接受，这些符号后面的东西不再接受

第二套新体系：

next Line():接受字符串

可以接受一整行的输入。

混合使用存在弊端

先用nextInt 后再使用nextLine，会出现nextLine接受nextInt没有接受的

### API：

字符串的对象学习：

####  String类，引用数据类型：

###### 字符串在创建后是不可以更改的。

俩种赋值的方式：

##### 直接赋值：

存储在串池中

可以检索相同的直接复用

节约内存

##### new出来：

存储在堆中，浪费内存

##### 注意：

引用类型变量存储地址

基本数据类型存储的是数据的真实数值

##### 字符串的比较：

| ` boolean` | [equals]将此字符串与指定的对象比较。                         |
| ---------- | ------------------------------------------------------------ |
| ` boolean` | [equalsIgnoreCase]将此 `String` 与另一个 `String` 比较，不考虑大小写。 |

##### StringBuilder的使用：

可变的操作字符串的容器

可以高效的拼接字符串，还可以将字符串的内容反转

```java
package com.itheima.test;
import java.util.Scanner;
public class demo1 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("请输入一个字符串：");

        String str=sc.next();
        StringBuilder sb=new StringBuilder(str);
        System.out.println(sb);
        System.out.println(sb.reverse());
        if (sb.toString()==sb.reverse().toString()){
            System.out.println(sb+"是对称字符串");
        }
        else {
            System.out.println(sb+"不是对称字符串");
        }
    }
}

```

##### StringJoiner的使用：

JDK8出现的，方便高效的拼接我们的字符串。

```java
package com.itheima.test;
import java.util.StringJoiner;
//学习StringJoiner
//快速实现拼接
//StringJoiner sj=new StringJoiner("---","[","]");
//本质上第一个为中间的间隔符
//第二个为开头的第一个符号
//第三个为结束的符号
public class StringJoiner_demo1 {
    public static void main(String[] args) {
        StringJoiner sj=new StringJoiner("---","[","]");
        for (int i = 0; i < 10; i++) {
            String re="";
            re=re+i;
            sj.add(re);
        }
        System.out.println(sj.toString());
    }
}

```

##### 字符串的原理

###### 字符串存储的内存原理：

直接赋值的话会复用字符串常量池中的

new 出来的不会复用，而是会在堆中开辟出新的kongjian

###### 字符串的==的比较的到底是什么

基本数据类型比较的时候，比较的是我们的实际的数值

比较引用的数据类型的时候，我们比较的是我们的地址的数值

这也就是我们为什么需要在进行字符串比较的时候采用equal的方法，而不是直接==操作



###### 字符串的拼接的原理

拼接的时候没有变量，都是字符串，出发字符串的优化机制，编译后就是最终

```java
string s1="a"+"b"+"c";
其在编译的时候触发优化机制，直接处理成“abc”
```



拼接的时候有变量的时候，jdk8之前会使用string builder进行构建字符串，也就是使用一个变量和一个字符串相加，这个时候在我们的堆内存中会出现俩个对象，一个对象是我们的String Builder对象，一个是我们的字符串对象本身。



在JDK8之后，采用预估的机制，但是这种操作任然会出现浪费我们的空间，和时间。

我们应该怎么做？

后续的字符串的拼接一般不要使用我们的+ ，这个操作会直接在底层创建多个对象，浪费时间和性能。

一般采用String builder或者string joiner

在直接使用**+ 链接字符串**的时候，会出现我们的对象的在创建，也就是会自动创建我们stringbuilder和字符串的对象，这就会导致我们内存出现浪费。

###### String Builder的底层优化原理：

string builder是一个内容可变的容器；

### 集合

集合和数组的对比：

数组的长度是固定的

集合的长度是可变的

数组可以存储基本的数据类型，也可以存储引用数据类型

集合只能存储引用数据类型，要是想存储基本数据类型必须要把他们变成包装类

##### Arraylist:

每个 `ArrayList` 实例都有一个*容量*。该容量是指用来存储列表元素的数组的大小。它总是至少等于列表的大小。随着向  ArrayList 中不断添加元素，其容量也自动增长。并未指定增长策略的细节，因为这不只是添加元素会带来分摊固定时间开销那样简单。

```java
package com.itheima.test;

import java.util.ArrayList;

public class ArrayList_demo1 {
    public static void main(String[] args) {
        ArrayList<String> al=new ArrayList<>();
        System.out.println(al);
    }

}
```

此时我们创建的是arraylist 的对象

这个类在我们的底层做了一些处理

打印对象的时候不是我们的地址值，是我们的集合中存储的数据的内容

打印的时候会吧数据用【】包裹；

###### 对象中的方法：

增  add

增加元素，返回值表示是否添加成功

删  remove

删除指定的元素或者删除指定的数据元素的index

查   get

得到指定的索引的元素

改  set

修改指定的索引下的元素，返回原来的元素

example:

```java
package com.itheima.test;
import java.util.ArrayList;
public class ArrayList_demo1 {
    public static void main(String[] args) {
        //创建一个集合
        ArrayList<String> al=new ArrayList<>();
        System.out.println(al);
        //添加元素
        al.add("aa");
        al.add("bb");
        al.add("cc");
        System.out.println(al);
        //改
        al.set(1,"ss");
        //删除
        al.remove("aa");
        al.add("aa");
        al.remove(1);
        System.out.println(al);


    }
}
```

###### 基本数据创建集合：

基本数据类型创建集合的时候需要我们有对应的包装类，每一个基本类型都对应着我们的分装类型，为什么要出现封装类型呢？其实Java本身是面向对象开发的，其无时无刻都在进行对象的创建和对象的销毁，因此我们可以产生对应的包装类，这就使得我们可以使用对应的包装类中操作对应数据类型的方法，此外，我们Java中的集合等操作，都需要我们采用包装类，因此我们的包装类可以更加有利于我们的开发

| 基本数据类型 | 包装类      |
| ------------ | ----------- |
| byte         | Byte        |
| short        | Short       |
| **char**     | **Char**    |
| **int**      | **Integer** |
| long         | Long        |
| float        | Float       |
| double       | Double      |
| boolean      | Boolean     |

```java
package com.it.dem4;

import java.util.ArrayList;

public class learn_demo1 {
    public static void main(String[] args) {
        ArrayList<Integer> list=new  ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        System.out.println(list);
        int i=list.get(0);
        System.out.println(i);

    }
}

```

###### 创建自己的对象数据的集合

```java
package com.it.dem4;

import java.util.ArrayList;
import java.util.Scanner;

public class learn_demo3 {
    public static void main(String[] args) {
//定义一个集合添加学生对象，并遍历
        ArrayList<Student> stulist=new ArrayList<>();
        Scanner sr=new Scanner(System.in);

        for (int i = 0; i < 3 ; i++) {
            Student st=new Student();
            System.out.println("输入学生的姓名：");
            String name=sr.next();
            System.out.println("输入学生的年龄：");
            int age= sr.nextInt();
            System.out.println("输入学生的身高：");
            double height=sr.nextDouble();
            st.setName(name);
            st.setAge(age);
            st.setHeigh(height);
            System.out.println("---------------");
            stulist.add(st);
        }
        System.out.println("遍历所有的数据");
        for (int i = 0; i < stulist.size(); i++) {
            System.out.println("用户名字："+stulist.get(i).getName());
            System.out.println("年龄："+stulist.get(i).getAge());
            System.out.println("体重："+stulist.get(i).getHeigh());

        }
    }
}
```

注意；我们需要在这里考虑

```
 Student st=new Student();
```

这个她在循环的外面的时候就会导致我们的array list中存放的都是最后一个的对象的地址的内容。

所以这个定义的对象应该放在我们的循环的内部，每次new不同的地址。

###### 查找用户：

```java
package com.it.dem4;

public class User{
    private String id;
    private String username;
    private String password;

    public User() {
    }

    public User(String id, String username, String password) {
        this.id = id;
        this.username = username;
        this.password = password;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}

```

主函数：

```java
package com.it.dem4;

import java.util.ArrayList;

public class User_test {
    public static void main(String[] args) {
        ArrayList<User> user=new ArrayList<>();

        User u1=new User("1","001","1234");
        User u2=new User("2","002","1234");
        User u3=new User("3","003","1234");
        user.add(u1);
        user.add(u2);
        user.add(u3);
        System.out.println(contain(user,"4"));
        System.out.println(Mcontain(user,"1"));

    }
          public static Boolean contain(ArrayList<User> user,String id){
              for (int i = 0; i <  user.size() ;i++) {
                  String myid=user.get(i).getId();
                  if(myid.equals(id)){
                      return true;
                  }
              }
              return false;
          }
          public static int Mcontain(ArrayList<User> users,String id){
              for (int i = 0; i < users.size(); i++) {
               String myid=users.get(i).getId();
               if (myid.equals(id)){
                   return i;
               }

              }return -1;
          }
}

```

###### 返回一系列的对象

```java
package com.it.dem4;

import java.util.ArrayList;

public class Phone_test {
    public static void main(String[] args) {
        //创建集合对象
        ArrayList<Phone> ph=new ArrayList<>();
        Phone ph1=new Phone("小米",1000);
        Phone ph2=new Phone("苹果",3000);
        Phone ph3=new Phone("华为",4000);
        ph.add(ph1);
        ph.add(ph2);
        ph.add(ph3);
        ArrayList<Phone> mi=getPhone(ph);
        for (int i = 0; i < mi.size(); i++) {
            Phone ok=new Phone();
            ok=mi.get(i);
            System.out.println(ok.getBrand());
        }
    }

    //定义我自己的方法：
    public static ArrayList<Phone> getPhone(ArrayList<Phone> arrayList){
        ArrayList<Phone> my=new ArrayList<>();
        Phone myphone=new Phone();
        for (int i = 0; i < arrayList.size(); i++) {
            Phone p=arrayList.get(i);
            if(p.getPrice()>2000){
             myphone=p;
             my.add(myphone);
            }
        }

        return my;
    }
}

```

### 面向对象进阶：

#### static（静态）

 static表示静态，是我们Java的一个修饰符，可以用来修饰我们成员方法和成员变量。

###### 静态变量

表示被static修饰的成员变量，叫做静态变量

特点：被该类的对象共享

调用方法：类名调用（推荐）

思考我们的静态变量是属于我们的类，并且可以被我们的类的对象所共用，因此我们采用类名调用

###### static的静态内存图

```java
public class student{
string name;
int age
static string teachername;
pobulic void show(){
sout(name+age+teachername)
}
}
```

```java
public class Test{
public void main(){
student.teachername="aweilaosi"
Student s1=new Student();
s1.name="zhangsan";
s1.age=23;
s1.show();
Student s2=new Student();
s2.show();
}
}
```

```java
student.teachername="aweilaosi"
```

这个加载到我们的栈内存，这个时候会加载student的字节码文件加载到我们的方法区，在堆内存中创建了一个单独的静态存储的位置（静态区），静态变量随着我们的类的加载而加载，因此优先于我们的对象而出现，且静态变量存储在我们的静态区。

注意：静态变量是随着类的加载而加载的，优先于我们的对象出现。

```java
Student s1=new Student();
```

该段代码的时候，会在我们的堆内存中创建我们的对象的空间

在这个空间中存储我们的其他的对象变量。

```java
Student s2=new Student();
```

该段代码的时候，会在我们的堆内存中创建我们的对象的空间

在这个空间中存储我们的其他的对象变量

```java
s2.show();
```

调用show的方法的时候，

show方法被加载入栈，找到对象的栈内存的中的内存的地址，然后找到静态区的变量，并全部展示出来

注意；静态区的的东西是我们类的，对象可以共享属性。

###### 共享与否？静态与否

###### 静态方法

表示被static修饰的成员方法，叫做静态方法。

特点：多用在我们的测试类和工具类中，Java bean中很少使用。

###### 工具类：

帮助我们做一些事情但是不描述任何事物的类

规则：类名见名知意，

私有化我们的构造方法：不让外部创建对象，是因为这个工具类对象的创建对象不存在意义。

方法定义为静态的：方便共享。

###### Java bean类：

用来描述我们的一类事物的类。

###### 测试类：

检查其他的类是否书写正确，带有main的方法，是我们程序的入口。

###### 静态的关键字的注意事项：

```java
静态方法只能访问静态变量
非静态方法可以访问静态和非静态的方法
静态方法中不能用this的关键字（结合内存的）
被static修饰的方法，其属于我们的类，可以直接使用，不需要new
没有static的方法，必须现创建对象。
```

```java
public class MyClass {
    int num;
    static int age;
    public void method(){
        //成员方法既能访问静态变量也能访问成员变量
        System.out.println(num);
        System.out.println(age);
        System.out.println("这是个成员方法！");
}
    public static void methodStatic(){

        System.out.println(age);

     //   System.out.println(num);  错误。  静态方法只能访问静态变量
        System.out.println("这是个静态方法!");
       // 静态方法中不能使用this关键字
     //   System.out.println(this);
    }
}
```

```java
/*
一旦使用static修饰成员方法，那么这就成为了静态方法。静态方法不属于对象，而是属于类的。
 如果没有static关键字，那么必须首先创建对象，然后通过对象才能使用它
  注意：静态只能直接访问静态。
       */
public class MyClass2 {
    public static void main(String[] args) {
        MyClass obj=new MyClass();  //首先创建对象
        //然后才能使用没有static关键字的内容
        obj.method();

        //对于静态方法来说，可以通过对象调用，也可以通过类调用
        obj.methodStatic();
        MyClass.methodStatic();


    }
}
```

###### 内存的使用：

静态：

**随着类的加载而加载**

静态的东西就会在内存中互相使用，但是非静态的东西无法使用。

这个主要是因为在调用的时候，静态的随着类的加载而出现，此时的非静态的是不存在的，因此我们的静态的无法调用非静态的，但是静态的变量此时已经随着类的加载已经到静态存储区中了，因此是不影响他的使用的，所以静态方法无法调用实例的变量.

非静态：

非静态的可以调用所有的

#### 继承

大量的对象出现内容的重复；

考虑：在这个上面进行递进的拓展。

父类：具有较为宽泛的属性和方法

子类：属性和方法更为具体。

Java中提供了一个关键字extends，用这个关键字，我们可以让一个类和另外一个类建立起来了继承的关系。

```java
public class student extends Person{}
```

Student 成为子类或者派生类，person称为父类（基类或者超类）。

##### 使用继承的好处：

可以把多个子类中重复的代码抽取到父类中，提高代码的复用性

##### 继承学习的内容：

###### 

什么时候使用我们的继承？

当我们的类与类之间的时候，存在共性的内容，并且满足我们子类是父类的一种，就可以考虑使用我们的继承。

##### 继承的特点：

Java只支持单继承，不支持多继承，但是支持多层的继承。

##### 继承体系：

顶级的父类就是我们的object的类

**每一个类都直接或者间接的继承于object**

Java中的所有的类都直接或者间接的继承于我们的object的类。

##### 继承的变量访问：

在子类方法中 或者 通过子类对象访问成员时

如果访问的成员变量子类中有，优先访问自己的成员变量

如果访问的成员变量与父类中成员变量同名，则优先访问自己的.

```java
成员变量访问遵循就近原则，自己有优先自己的，如果没有则向父类中找。
```

##### 继承的时候的成员方法的访问：

###### 成员方法的名字不相同的时候：

成员方法没有同名时，在子类方法中或者通过子类对象访问方法时，则优先访问自己的，自己没有时 再到父类中找，如果父类中也没有则报错。

###### 成员方法的名字相同的时候：

(1)：通过子类对象访问父类与子类中不同名方法时，优先在子类中找，找到则访问，否则在父类中找，找到 则访问，否则编译报错

（2）：通过派生类对象访问父类与子类同名方法时，如果父类和子类同名方法的参数列表不同(重载)，根据调用 方法适传递的参数选择合适的方法访问，如果没有则报错；如果父类和子类同名方法的原型一致(重写-后 面讲)，则只能访问到子类的，父类的无法通过派生类对象直接访问到。

当我们的父类中的方法和子类中的方法一致的时候，我们一般采用的是重写的方法实现，这就是因为我们的子类中的方法会重写父类中的方法。访问时只有子类的这个方法。


##### super关键字

子类和父类中可能会存在相同名称的成员，如果要在子类方法中访问父类同名成员时，该如何操作？直接访问是无法做到的，Java提供了[super关键字](https://so.csdn.net/so/search?q=super关键字&spm=1001.2101.3001.7020)，该关键字主要作用：在子类方法中访问父 类的成员（字段和方法）

```java
public class Base {
int a;
int b;
public void methodA(){
System.out.println("Base中的methodA()");
}
public void methodB(){
System.out.println("Base中的methodB()");
}
}
public class Derived extends Base{
int a; // 与父类中成员变量同名且类型相同
char b; // 与父类中成员变量同名但类型不同
// 与父类中methodA()构成重载
public void methodA(int a) {
System.out.println("Derived中的method()方法");
}
// 与基类中methodB()构成重写(即原型一致，重写后序详细介绍)
public void methodB(){
System.out.println("Derived中的methodB()方法");
}
public void methodC(){
// 对于同名的成员变量，直接访问时，访问的都是子类的
a = 100; // 等价于： this.a = 100;
b = 101; // 等价于： this.b = 101;
// 注意：this是当前对象的引用
// 访问父类的成员变量时，需要借助super关键字
// super是获取到子类对象中从基类继承下来的部分
super.a = 200;
super.b = 201;
// 父类和子类中构成重载的方法，直接可以通过参数列表区分清访问父类还是子类方法
methodA(); // 没有传参，访问父类中的methodA()
methodA(20); // 传递int参数，访问子类中的methodA(int)
// 如果在子类中要访问重写的基类方法，则需要借助super关键字
methodB(); // 直接访问，则永远访问到的都是子类中的methodA()，基类的无法访问到
super.methodB(); // 访问基类的methodB()
}
}


```

###### 注意：

```java
1：只能在非静态方法中使用

2： 在子类方法中，访问父类的成员变量和方法
```

##### 子类的构造方法；

```java
在实例化子类对象时，必须先调用父类的构造方法，再调用子类的构造方法（先有父母再有孩子）。且必须在子类构造方法的第一行调用父类方法。
一般在子类中显式的调用父类构造方法，若没有显式调用的调用，则子类会默认调用父类的无参构造方法。（若父类没有无参构造方法，则会编译报错）
   当我们创建一个Child对象时，会先调用父类Parent的构造方法来初始化父类的字段，然后再调用子类Child的构造方法来初始化子类的字段。这样保证了子类中新加入的变量也能得到正确的初始化。
```

子类不能直接继承我们父类的构造方法：

子类对象构造时，需要先调用基类构造方法，然后执行子类的构造方法

```java
public class Base {
public Base(){
System.out.println("Base()");
}
}
public class Derived extends Base{
public Derived(){
// super(); // 注意子类构造方法中默认会调用基类的无参构造方法：super(),
// 用户没有写时,编译器会自动添加，而且super()必须是子类构造方法中第一条语句，
// 并且只能出现一次
System.out.println("Derived()");
}
}
public class Test {
public static void main(String[] args) {
Derived d = new Derived();
}
}
结果打印：
Base()
Derived()
```

在子类构造方法中，并没有写任何关于基类构造的代码，但是在构造子类对象时，先执行基类的构造方法，然后执 行子类的构造方法，因为：子类对象中成员是有两部分组成的，基类继承下来的以及子类新增加的部分 。父子父子 肯定是先有父再有子，所以在构造子类对象时候 ，先要调用基类的构造方法，将从基类继承下来的成员构造完整 ，然后再调用子类自己的构造方法，将子类自己新增加的成员初始化完整 。

```java
注意：
1： 若父类显式定义无参或者默认的构造方法，在子类构造方法第一行默认有隐含的super()调用，即调用基类构造方法。

2： 如果父类构造方法是带有参数的，此时编译器不会再给子类生成默认的构造方法，此时需要用户为子类显式定义构造方法，并在子类构造方法中选择合适的父类构造方法调用，否则编译失败。//实践

3：在子类构造方法中，super(…)调用父类构造时，必须是子类构造函数中第一条语句。

4： super(…)只能在子类构造方法中出现一次，并且不能和this同时出现
```

##### this和super的区别：

```java
相同点：
1： 只能在类的非静态方法中使用，用来访问非静态成员方法和字段

2： 在构造方法中调用时，必须是构造方法中的第一条语句，并且不能同时存在。

不同点：
1： this是当前对象的引用，当前对象即调用实例方法的对象，super相当于是子类对象中从父类继承下来部分成员的引用

2：在非静态成员方法中，this用来访问本类的方法和属性，super用来访问父类继承下来的方法和属性

3： this是非静态成员方法的一个隐藏参数，super不是隐藏的参数

4：在构造方法中：this(…)用于调用本类构造方法，super(…)用于调用父类构造方法，两种调用不能同时在构造 方法中出现

```

子类继承的成员方法：

子类可以从父类继承一个虚方法表 ：

虚方法表： 非private   非 static       非 final的其他方法放入虚方法

### 多态：

##### 什么是多态：

同种类型的对象，表现出来的不同的形态

##### 多态的表现形式：

```java
Person p=new teacher()
Person p=new student()
Person p=new administrator()
```

##### 多态的前提：

有继承的关系

有父类引用指向子类的对象

```java
package com.it.demo7;

import com.it.dem4.Student;

public class test {
    public static void main(String[] args) {
        student s=new student();
        s.setName("zhangsan");
        s.setAge(18);
        teacher t=new teacher();
        t.setName("zhangwei");
        t.setAge(29);
        Adminer a=new Adminer();
        a.setName("huangsan");
        a.setAge(39);
        register(s);
        register(t);
        register(a);
        
    }
    //这个方法可以接受老师学生管理员
    //怎么办
    //多态，我们可以使用他们的父类
  //这个传入的父类我们可以传入她的所有的子类
    public static void register(Person S){
        S.show();
    }
}
```

我们无论传入什么他都可以进行传入。在我们注册的时候特别有用。

##### 多态调用我们成员的特点：

变量的调用：编译看左边，运行看左边

方法的调用：编译看左边，运行看右边

```java
package com.it.demo7;

public class test {
    public static void main(String[] args) {
        student s=new student();
        s.setName("zhangsan");
        s.setAge(18);
        teacher t=new teacher();
        t.setName("zhangwei");
        t.setAge(29);
        Adminer a=new Adminer();
        a.setName("huangsan");
        a.setAge(39);
        register(s);
        register(t);
        register(a);
        //测试多态对我们的子类的处理
        Person ps=new student();
        //使用多态调用我们的变量的时候遵循我们的编译看左边，调用用右边
        System.out.println(ps.x);
        //10
        //测试多态对我们的方法的调用
        ps.show();
        //学生的信息；
        //使用多态的时候，遵循我们的编译看左边，调用看右边的基本的要求
        //多态的弊端
        student se=(student) ps;
        se.mys();

    }
    //这个方法可以接受老师学生管理员
    //怎么办
    //多态，我们可以使用他们的父类
    public static void register(Person S){
        S.show();
    }
}
```

为什么多态引用会有上述的要求？

```java
我们可以这样思考，在使用这个多态的引用的时候：
  Person ps=new student();
现在用我们的Person类定义的时候，其实ps是我们的person的类，所以在找的时候会先在我们person中去找
  变量的调用：
  创建student的时候，其实我们的student中会继承我们父类的变量，此时的student中存在两个变量，这个时候我们会根据我们的ps的类种类区选择和他一类的变量
  方法的调用，其实本质会继承我们父类的方法，所以我们的子类其实是吧我们从父类继承的方法已经重写了，这个时候 再去调用的时候其实就是我们的子类的方法。
  
```

##### 多态的优势和弊端

###### 多态的优势：

在多态的形势下，右边的对象可以实现解开耦合，便于拓展

定义方法的时候，使用我们的父类作为参数的时候，我们可以接受所有的子类的对象，体现多态的拓展

###### 多态的弊端：

调用不了我们的子类所专有的方法。（因为在编译的时候我们先去检查我们的父类的方法里面是否存在我们的需要调用的方法的，要是没有就会报错，这就是为什么我们无法调用我们的子类的专用的方法）

解决方法，继续变成我们原始的子类（类型强制转换）

```java
        Person ps=new student();
        student se=(student) ps;
        se.mys();
```

##### 多态的练习：

```java
package com.it.demo8;

public class person {
    private String name;
    private int age;

    public person() {
    }

    public person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void keepPet(Animal s,String somethig){
        if(s instanceof dog){
        System.out.println("年龄为"+age+"的"+name+"养了一只"+s.getColor()+"的狗");
        s.eat(somethig);}
        else{
        System.out.println("年龄为"+age+"的"+name+"养了一只"+s.getColor()+"的猫");
        s.eat(somethig);
    }}
}

```

多态如何调用子类的专属的方法：

```java
package com.it.demo8;

public class test {
    public static void main(String[] args) {
        person p=new person();
        cat c=new cat();
        c.setAge(2);
        c.setColor("yellow");
        dog d=new dog();
        d.setColor("red");
        d.setAge(12);
        p.setName("赵巍山");
        p.setAge(18);
        p.keepPet(c,"小鱼干");
        p.keepPet(d,"骨头");
        Animal x=c;
        if (x instanceof dog dd){
            dd.look_home();
        }
        else if(x instanceof cat dd) {
            dd.zhua();
        }
    }
}

```

##### 面向对象中的细节：

包：包就是文件夹，用来管理不同功能的Java的类，方便我们的后期的管理；

包的命名的规则：公司的域名反写并加上包的作用，需要全部的英文的小写，简明之一

```java
package com.it.demo8;
public class student{

}
```

我们在使用我们的具体的方法的时候要加上包的名字

使用其他的类的时候我们需要使用它的包名+对象名

之后的使用的时候

```
import com.it.demo7.student;
public static void main(){
student s1=new student;
}
```

### Final关键词:

final修饰方法：表明我们的方法为最后的一个方法，不能重写。

final修饰一个类：表明这个类是最终的类，不能被继承。

final修饰变量：叫做常量，只能赋值一次。

### 常量：

常量的命名的规范：一般作为我们的系统的配置的信息，方便维护，提高我们的数据的可读性

单个单词：全部大写

多个单词：全部大写

细节：

final修饰的变量为基本的数据类型的时候，变量存书的数据值不能发生变化。

final修饰的引用的类型，那么变量存储的地址的数值不能发生改变，而对象的内部的可以gaibian

### 权限修饰符：

权限修饰符：用来控制每一个成员的能够被访问的权限范围。

| 修饰符    | 同一个类 | 同一个包下的类 | 不同的包下的类 | 不同包下的无关类 | 权限                   |
| --------- | -------- | -------------- | -------------- | ---------------- | ---------------------- |
| private   | ture     |                |                |                  | 私有的                 |
| 空着不写  | ture     | ture           |                |                  | 只在本包中使用         |
| Protected | ture     | ture           | ture           |                  | 可以在本包和别包中使用 |
| public    | ture     | ture           | ture           | ture             | 全部能使用             |

### 静态代码块：

```
格式：
static{}

```

特点：需要通过static的关键字修饰，随着类的加载而加载，并且自动的触发，只执行一次。

使用的场景：

在做类的加载，做数据的初始化的时候儿加载使用。

执行的时机：加载类的时候就会执行我们的静态的代码块

```java
package com.it.demo8;

public class person {
    private String name;
    private int age;
    static {
        System.out.println("静态对象执行了");
    }
    public person() {
    }
    public person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public void keepPet(Animal s,String somethig){
        if(s instanceof dog){
        System.out.println("年龄为"+age+"的"+name+"养了一只"+s.getColor()+"的狗");
        s.eat(somethig);}
        else{
        System.out.println("年龄为"+age+"的"+name+"养了一只"+s.getColor()+"的猫");
        s.eat(somethig);
    }}
}
```

### 抽象类：

abstract修饰的方法：

```
public Abstract 
```

##### 抽象方法：

将共性的行为和方法抽取到父类之后，由于每一个子类的执行的内容是不一样的，所以在父类中不能确定具体的方法体，该方法就是抽象方法体

定义：

```
public abstract 返回值的类型 方法名();
```

##### 抽象类：

如果一个类中存在抽象的方法，那么该类就必须申明为抽象类

```
public Abstract class 类名{}
```

##### 注意的事项：

抽象类不能实例化：

抽象类中不一定存在抽象方法，但是抽象方法所在的类一定是抽象类

抽象类可以有构造方法

抽象类中子类

1.    要么重写抽象类中的所有的抽象方法
2.    要么子类本身也是抽象类

### 接口：

```java
Java 接口是一系列方法的声明，是一些方法特征的集合，一个接口只有方法的特征没有方法的实现。
```

接口中的定义了一系列的抽象的方法和常量；

实现接口其实本质就是去完成接口中所有的抽象方法；

##### 什么是接口？

其实接口就是我们的特殊的抽象类，这个类中包含变量和方法的定义，而没有其具体的实现。实现这个接口就必须完成这个接口中的抽象方法的重写。

本质上讲，接口是一种特殊的抽象类，这种抽象类中只包含常量和方法的定义，而没有变量和方法的实现。

##### 为什么需要接口：

接口就是为了解决Java单继承这个弊端而产生的，虽然一个类只能有一个直接父类，但是它可以实现多个接口，没有继承关系的类，也可以实现相同的接口。继承和接口的双重设计即保持了类的数据安全也变相实现了多继承。

##### **特点**： 

方法和属性默认都是*public*修饰，也可以使用*protected*，但不能用private。
所有的属性都是静态的常量，默认省略了static和final修饰符，属性的值必须实例化（初始化）

##### 接口的特点：

1. 用 interface 来定义。

2. 接口中的所有成员变量都默认是由public static final修饰的。

3. 接口中的所有方法都默认是由public abstract修饰的。

4. 接口没有构造方法。构造方法用于创建对象

5. 实现接口的类中必须提供接口中所有方法的具体实现内容。

6. 多个无关的类可以实现同一个接口

7. 一个类可以实现多个无关的接口

8. 与继承关系类似，接口与实现类之间存在多态性

9. 接口也可以继承另一个接口，使用extends关键字。

10. 实现接口的类中必须提供接口中所有方法的具体实现内容。

11. 多个无关的类可以实现同一个接口

12. 一个类可以实现多个无关的接口

13. 与继承关系类似，接口与实现类之间存在多态性

##### 接口的定义和使用：

###### 定义接口：

```java
public interface Person {
  	final String NAME = "我是Person接口中的常量";
	void walk();
  	void run();
}
```

常量和抽象的方法；

接口比抽象类更加“抽象”，它下面不能拥有具体实现的方法，必须全部是抽象方法，所有的方法默认都是`public abstract`的，所以在接口主体中的方法，这两个修饰符无需显示指定。

接口除了`方法声明`外，还可以包含`常量声明`。在接口中定义的所有的常量都默认是`public`,`static`和`final`的。

接口中的成员声明不允许使用`private`和`protected`修饰符。

##### 实例：

定义的接口：

```java
package com.itheima.test4;

public interface swim {
    public abstract void Swim();
}

```

定义实现接口的类：

```java
package com.itheima.test4;

public class wa extends Animal implements swim{
    public wa() {
    }

    public wa(String name, int age) {
        super(name, age);
    }

    @Override
    public void eat() {
        System.out.println("吃虫子");
    }

    @Override
    public void Swim() {
        System.out.println("蛙泳");
    }
}
```

##### 如何访问内存分析工具：

首先程序不能结束：一般让咱们的程序卡在这个位置，一直不结束

```java
package com.itheima.test4;


import java.util.Scanner;

public class TEST2 {
    public static void main(String[] args) {
        infer x=new infer();
        x.Swim();

        Scanner sc=new Scanner(System.in);
        sc.next();
    }
}
```

打开terminal的工具行：输入

```
jps
```

选择我们的测试程序的id

```JAVA
C:\Users\Administrator\IdeaProjects\mystudy>jps
3728 Launcher
5536 TEST2
13048 Jps 
7676    
```

接下来：

```java
C:\Users\Administrator\IdeaProjects\mystudy>jhsdb hsdb

```

##### 类的多接口的实现：

```java
package com.itheima.test4;
public class inter_ac implements inter1,inter2,inter3{
    @Override
    public void meth1() {

    }
    @Override
    public void meth2() {
    }
    @Override
    public void meth3() {
    }
}
```

接口中出现重名发的-0方法的时候：只需要重写一次就可以了

```java
package com.itheima.test4;

public interface inter1 {
    void  meth1();
}
package com.itheima.test4;

public interface inter3 {
    void  meth1();
}

```

```Java
package com.itheima.test4;

public abstract class inter_ac implements inter1,inter2,inter3 {
    @Override
    public void meth1() {

    }
    @Override
    public void meth2() {

    }
}
```

##### 接口和接口之间的关系：

可以实现继承关系，此外牢记接口可以多继承：

```java
package com.itheima.test5;

public interface inter3 extends inter1,inter2{
    void method3();
}
//接口实现 的多继承：
```

###### 定义接口的实现类：

```java
package com.itheima.test5;

public class inter_ar implements inter3{
    @Override
    public void method1() {

    }
    @Override
    public void method2() {
    }

    @Override
    public void method3() {

    }
}
```

实现的类中需要是西安我们的定义的的继承自inter1和inter2 的接口的全部的抽象方法；

##### 内部类：

###### 成员内部类：

写在成员位置的，属于外部类的成员

成员内部类可以被一些修饰符号所修饰，比如private，protected,public,static.

在成员的内部类中，Jdk16之前不能定义静态变量,JDK16开始才能够定义静态变量

变量的内存图：

```
public class Outer{
private int a=10；

class Inner{
private int a=20;


public void show(){
int a=30;
SOUT(a);  //30
SOUT(this.a);//20
SOUT(Outer.this.a);//10
}
}
}

```

###### 静态内部类 

注意静态的内部类中，只能访问外部类中的静态的变量和方法，如果需要访问非静态的成员需要我们先创建对象。

```
public class Outer{
private int a=10；

static class Inner{
private int a=20;
}
}
```

直接创建静态内部类的方式：

```java
Outer.inner oi=new outer.inner();
```

如何定义我们的静态的内部类中的方法？

非静态的方法的调用：

```
先创建我们的对象，然后再去调用
```

静态的方法：

```
外部类名.内部的类名.方法名()
```

###### 局部内部类

```
public class Outer{
private int a=10；
public void inetr(){
int a=10;
static class Inner{
private int a=20;
}
}
}
```

将我们的内部类定义在我们的方法里面的类，类似于方法里面的局部变量

外界无法直接的使用·需要我们在方法的内部创建对象并去使用

该类可以直接访问外部的类的成员，也可以访问方法内的具局部的变量

##### 重点掌握：匿名内部类

匿名内部类，本质上就是内部隐藏了名字的内部类 

匿名内部类的格式：

```java
new 类名或者接口的名字{
重写方法
}；
包含了继承或者实现
方法的重写
创建对象
整体上就是一个类的子类对象的或者接口的实现类对象

```

使用的场景：

当方法的参数是一个接口或者类的时候，

一接口为例子，可以传递这个接口的实现类对象

如果实现类只用一次，就可以用匿名内部类去简化代码

### GUI

#### 主界面的创建：

```java
public class jfram extends JFrame {
    public void Gameframe(){
        this.setSize(520,520);
        this.setTitle("单机的小游戏");
        this.setAlwaysOnTop(true);
        this.setLocationRelativeTo(null);
        this.setDefaultCloseOperation(WindowConstants.*EXIT_ON_CLOSE*);
        this.setLayout(null);
        //让界面显示出来，默认页面是不显示的
        this.setVisible(true);

​    }
}[]()
```

#### 菜单的制作：

```java
        //创建Jmenubar
        JMenuBar jmenubar=new JMenuBar();
        jmenubar.setSize(520,10);
        //设置JMENU
        JMenu jmu1=new JMenu("功能");
        JMenu jmu2=new JMenu("关于");
        JMenu jmu0=new JMenu("0");
        //JMENU中添加对应的选项，Jmenuitem,此外需要注意的是这jmenu中可以嵌套jmenu，也就是说我们可以在选项的下面继续设置选项的设置。
        JMenuItem action0=new JMenuItem("0");
        JMenuItem action01=new JMenuItem("01");
        JMenuItem action1=new JMenuItem("1");
        JMenuItem action2=new JMenuItem("2");
        JMenuItem action3=new JMenuItem("3");
        JMenuItem action4=new JMenuItem("4");
        jmu0.add(action0);
        jmu0.add(action01);
        jmu1.add(jmu0);
        jmu1.add(action1);
        jmu1.add(action2);
        jmu1.add(action3);
        jmu1.add(action4);
        jmenubar.add(jmu1);
        jmenubar.add(jmu2);
//最后一步的设置其实是吧我们的jmenuBar 设置到我们的Jframe的主要界面之中去、
        this.setJMenuBar(jmenubar);
```

#### 图片的添加：

##### ImageIcon:

描述图片的类，可以关连到我们计算机中的任意的类，但是一般会先把图片拷贝到当前的项目中

##### Jlabel :

管理文本和图片的类

```java
//1，先对整个界面进行设置
	//取消内部居中放置方式
	this.setLayout(null);
//2，创建ImageIcon对象，并制定图片位置。
	ImageIcon imageIcon1 = new ImageIcon("image\\1.png");
//3，创建JLabel对象，并把ImageIcon对象放到小括号中。
	JLabel jLabel1 = new JLabel(imageIcon1);
//4，利用JLabel对象设置大小，宽高。
	jLabel1.setBounds(0, 0, 100, 100);
//5，将JLabel对象添加到整个界面当中。
	this.add(jLabel1);
```

#### 事件：

##### 常见的三种的监听的方式：

* 键盘监听 KeyListener

  ```java
  public class MyJFrame extends JFrame implements ActionListener {
  
      //创建一个按钮对象
      JButton jtb1 = new JButton("点我啊");
      //创建一个按钮对象
      JButton jtb2 = new JButton("再点我啊");
  
      public MyJFrame(){
          //设置界面的宽高
          this.setSize(603, 680);
          //设置界面的标题
          this.setTitle("拼图单机版 v1.0");
          //设置界面置顶
          this.setAlwaysOnTop(true);
          //设置界面居中
          this.setLocationRelativeTo(null);
          //设置关闭模式
          this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
          //取消默认的居中放置，只有取消了才会按照XY轴的形式添加组件
          this.setLayout(null);
  
  
          //给按钮设置位置和宽高
          jtb1.setBounds(0,0,100,50);
          //给按钮添加事件
          jtb1.addActionListener(this);
  
  
          //给按钮设置位置和宽高
          jtb2.setBounds(100,0,100,50);
          jtb2.addActionListener(this);
  
  
          //那按钮添加到整个界面当中
          this.getContentPane().add(jtb1);
          this.getContentPane().add(jtb2);
  
          //让整个界面显示出来
          this.setVisible(true);
      }
  
      @Override
      public void actionPerformed(ActionEvent e) {
          //对当前的按钮进行判断
          //获取当前被操作的那个按钮对象
          Object source = e.getSource();
  
          if(source == jtb1){
              jtb1.setSize(200,200);
          }else if(source == jtb2){
              Random r = new Random();
              jtb2.setLocation(r.nextInt(500),r.nextInt(500));
          }
      }
  }
  ```
  
  
  
* 鼠标监听 MouseListener

  当设置了鼠标监听事件的时候，需要实现鼠标监听的接口

  ```java
          //获取正确的验证码
          String codeStr = CodeUtil.getCode();
          Font rightCodeFont = new Font(null,1,15);
          //设置颜色
          rightCode.setForeground(Color.RED);
          //设置字体
          rightCode.setFont(rightCodeFont);
          //设置内容
          rightCode.setText(codeStr);
          //绑定鼠标事件
          rightCode.addMouseListener(this);
          //位置和宽高
          rightCode.setBounds(400, 133, 100, 30);
          //添加到界面
          this.getContentPane().add(rightCode);
  ```

  此时的

  ```java
  public class LoginJFrame extends JFrame implements MouseListener 
      LoginJFrame属于这个鼠标监听的接口的实现类
  ```

  当同一个界面的实现类中出现同样的监听的事件的时候；我们需要先判断这个监听的事件属于哪一个事件，然后再去执行相应的操作

  ```java
  public void mousePressed(MouseEvent e) {
          Object st=e.getSource();
          if(st==x1){
              System.out.println("hello");
          }
  
      }
  
  ```

  同一个界面中的不同的组件有不一样的点击的事件的时候我们需要采用，判断点击事件的类型来实现相应的功能

  

  ```java
      @Override
      public void mouseClicked(MouseEvent e) {
          Object source = e.getSource();
          if (source==rightCode){
  
          } else if (source==login) {
  
          } else if (source==register) {
  
          }
          
      }
  ```

  

* 动作监听 ActionListener



### API:

#### math类：

```java
public static int abs(int a)					// 返回参数的绝对值
public static double ceil(double a)				// 返回大于或等于参数的最小整数
public static double floor(double a)			// 返回小于或等于参数的最大整数
public static int round(float a)				// 按照四舍五入返回最接近参数的int类型的值
public static int max(int a,int b)				// 获取两个int值中的较大值
public static int min(int a,int b)				// 获取两个int值中的较小值
public static double pow (double a,double b)	// 计算a的b次幂的值
public static double random()					// 返回一个[0.0,1.0)的随机值
```

#### system类：

```java
public static long currentTimeMillis()			// 获取当前时间所对应的毫秒值（当前时间为0时区所对应的时间即就是英国格林尼治天文台旧址所在位置）
public static void exit(int status)				// 终止当前正在运行的Java虚拟机，0表示正常退出，非零表示异常退出
public static native void arraycopy(Object src,  int  srcPos, Object dest, int destPos, int length); // 进行数值元素copy
```

#### runtime类

```java
public static Runtime getRuntime()		//当前系统的运行环境对象
public void exit(int status)			//停止虚拟机
public int availableProcessors()		//获得CPU的线程数
public long maxMemory()				    //JVM能从系统中获取总内存大小（单位byte）
public long totalMemory()				//JVM已经从系统中获取总内存大小（单位byte）
public long freeMemory()				//JVM剩余内存大小（单位byte）
public Process exec(String command) 	//运行cmd命令
```

#### Object 类

```java
public String toString()				//返回该对象的字符串表示形式(可以看做是对象的内存地址值)
public boolean equals(Object obj)		//比较两个对象地址值是否相等；true表示相同，false表示不相同
protected Object clone()    			//对象克隆
```

#### Objects类

Objects类中无无参构造方法，因此我们不能使用new关键字去创建Objects的对象。同时我们可以发现Objects类中所提供的方法都是静态的。因此我们可以通过类名直接去调用这些方法。

```java
public static String toString(Object o) 					// 获取对象的字符串表现形式
public static boolean equals(Object a, Object b)			// 比较两个对象是否相等
public static boolean isNull(Object obj)					// 判断对象是否为null
public static boolean nonNull(Object obj)					// 判断对象是否不为null
```

#### BigInteger类

```java
public BigInteger(int num, Random rnd) 		//获取随机大整数，范围：[0 ~ 2的num次方-1]
public BigInteger(String val) 				//获取指定的大整数
public BigInteger(String val, int radix) 	//获取指定进制的大整数
    
下面这个不是构造，而是一个静态方法获取BigInteger对象
public static BigInteger valueOf(long val) 	//静态方法获取BigInteger的对象，内部有优化
```

##### 常见的成员方法

```java
public BigInteger add(BigInteger val)					//加法
public BigInteger subtract(BigInteger val)				//减法
public BigInteger multiply(BigInteger val)				//乘法
public BigInteger divide(BigInteger val)				//除法
public BigInteger[] divideAndRemainder(BigInteger val)	 //除法，获取商和余数
public  boolean equals(Object x) 					    //比较是否相同
public  BigInteger pow(int exponent) 					//次幂、次方
public  BigInteger max/min(BigInteger val) 				//返回较大值/较小值
public  int intValue(BigInteger val) 					//转为int类型整数，超出范围数据有误
```

##### example:

```java
package com.itheima.test7;

import java.math.BigInteger;

public class bigInteger_demo {
    public static void main(String[] args) {
         //字符串中的数字必须是整数
         //创建一个对象
        BigInteger big=new BigInteger("100",10);
        System.out.println(big);

        //可以不去构造而是静态的方法去获取一个biginteger的对象
        //细节：
        //表示的范围比较小，必须为long的范围之内，之外的就不能创建

        BigInteger big4=BigInteger.valueOf(123);
        System.out.println(big4);
        //for example
        //max is 9223372036854775807
        // 超这个范围就会出问题
        BigInteger big5=BigInteger.valueOf(9223372036854775807L);
        System.out.println(big5);

    }
}
```



#### BigDecimal类

```java
public BigDecimal add(BigDecimal value)				// 加法运算
public BigDecimal subtract(BigDecimal value)		// 减法运算
public BigDecimal multiply(BigDecimal value)		// 乘法运算
public BigDecimal divide(BigDecimal value)			// 触发运算
```

#####  除法：

```java
public class BigDecimalDemo02 {

    public static void main(String[] args) {

        // 创建两个BigDecimal对象
        BigDecimal b1 = new BigDecimal("1") ;
        BigDecimal b2 = new BigDecimal("3") ;

        // 调用方法进行b1和b2的除法运算，并且将计算结果在控制台进行输出
        System.out.println(b1.divide(b2));

    }

}
```

数据存在一个问题就是这个会产生无限不循环的小数，这个就会出现报错，我们应该有个舍入的方法

```java
BigDecimal divide(BigDecimal divisor, int scale, int roundingMode)
```

```java
divisor:			除数对应的BigDecimal对象；
scale:				精确的位数；
roundingMode:		取舍模式；
取舍模式被封装到了RoundingMode这个枚举类中（关于枚举我们后期再做重点讲解），在这个枚举类中定义了很多种取舍方式。最常见的取舍方式有如下几个：
UP(直接进1) ， FLOOR(直接删除) ， HALF_UP(4舍五入),我们可以通过如下格式直接访问这些取舍模式：枚举类名.变量名
```

### 正则表达式：

正则表达式可以校验字符串是否满足一定的规则，并用来校验数据格式的合法性。

在文本中查找满足要求的内容。

校验字符串的时候是忒有用

```java
public class Regexdemo1 {
    public static void main(String[] args) {
        String qq="12345678";
        System.out.println(checkqq(qq));
        System.out.println(qq.matches("[1-9]\\d{5,19}"));

    }
```

##### 正则校验

```java
qq.matches("[1-9]\\d{5,19}")
 //标识1-9 全部为数字 且范围再5-19
```

##### 正则表达式中：

###### 字符类

方括号标识一个范围：

```java
1. \[abc\]：代表a或者b，或者c字符中的一个。
2. \[^abc\]：代表除a,b,c以外的任何字符。
3. [a-z]：代表a-z的所有小写字符中的一个。
4. [A-Z]：代表A-Z的所有大写字符中的一个。
5. [0-9]：代表0-9之间的某一个数字字符。
6. [a-zA-Z0-9]：代表a-z或者A-Z或者0-9之间的任意一个字符。
7. [a-dm-p]：a 到 d 或 m 到 p之间的任意一个字符。 

```

###### 逻辑运算符：

```java
1. &&：并且
2. |    ：或者
3. \  ：转义字符
```



###### 预定义字 符

```java
1. "." ： 匹配任何字符。
2. "\d"：任何数字[0-9]的简写；
3. "\D"：任何非数字\[^0-9\]的简写；
4. "\s"： 空白字符：[ \t\n\x0B\f\r] 的简写
5. "\S"： 非空白字符：\[^\s\] 的简写
6. "\w"：单词字符：[a-zA-Z_0-9]的简写
7. "\W"：非单词字符：\[^\w\]
```

###### 数量词

```java

X？ X一次或者多次
X*  X，0次或者多次
X+  X，一次或者多次
X{n} X,出现n次
X{n,} x至少n次
X{n,M} x 至少n次但是不超过M次

```

###### 指定要求的正则的表达式：

要求可以看懂会改即可

###### 忽略大小写的方式

```java
//(?i) ：表示忽略后面数据的大小写
//忽略abc的大小写
String regex = "(?i)abc";
//a需要一模一样，忽略bc的大小写
String regex = "a(?i)bc";
//ac需要一模一样，忽略b的大小写
String regex = "a((?i)b)c";
```

###### 本地的数据的爬取：

```java
package com.itheima.a08regexdemo;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexDemo6 {
    public static void main(String[] args) {
        /* 有如下文本，请按照要求爬取数据。
                Java自从95年问世以来，经历了很多版本，目前企业中用的最多的是Java8和Java11，
                因为这两个是长期支持版本，下一个长期支持版本是Java17，相信在未来不久Java17也会逐渐登上历史舞台
                要求:找出里面所有的JavaXX
         */

        String str = "Java自从95年问世以来，经历了很多版本，目前企业中用的最多的是Java8和Java11，" +
                "因为这两个是长期支持版本，下一个长期支持版本是Java17，相信在未来不久Java17也会逐渐登上历史舞台";


        //1.获取正则表达式的对象
        Pattern p = Pattern.compile("Java\\d{0,2}");
        //2.获取文本匹配器的对象
        //拿着m去读取str，找符合p规则的子串
        Matcher m = p.matcher(str);

        //3.利用循环获取
        while (m.find()) {
            String s = m.group();
            System.out.println(s);
        }


    }

    private static void method1(String str) {
        //Pattern:表示正则表达式
        //Matcher: 文本匹配器，作用按照正则表达式的规则去读取字符串，从头开始读取。
        //          在大串中去找符合匹配规则的子串。

        //获取正则表达式的对象
        Pattern p = Pattern.compile("Java\\d{0,2}");
        //获取文本匹配器的对象
        //m:文本匹配器的对象
        //str:大串
        //p:规则
        //m要在str中找符合p规则的小串
        Matcher m = p.matcher(str);

        //拿着文本匹配器从头开始读取，寻找是否有满足规则的子串
        //如果没有，方法返回false
        //如果有，返回true。在底层记录子串的起始索引和结束索引+1
        // 0,4
        boolean b = m.find();

        //方法底层会根据find方法记录的索引进行字符串的截取
        // substring(起始索引，结束索引);包头不包尾
        // (0,4)但是不包含4索引
        // 会把截取的小串进行返回。
        String s1 = m.group();
        System.out.println(s1);


        //第二次在调用find的时候，会继续读取后面的内容
        //读取到第二个满足要求的子串，方法会继续返回true
        //并把第二个子串的起始索引和结束索引+1，进行记录
        b = m.find();

        //第二次调用group方法的时候，会根据find方法记录的索引再次截取子串
        String s2 = m.group();
        System.out.println(s2);
    }
}
```

###### 网络爬取数据：

```Java
public class RegexDemo7 {
    public static void main(String[] args) throws IOException {
        /* 扩展需求2:
            把连接:https://m.sengzan.com/jiaoyu/29104.html?ivk sa=1025883i
            中所有的身份证号码都爬取出来。
        */

        //创建一个URL对象
        URL url = new URL("https://m.sengzan.com/jiaoyu/29104.html?ivk sa=1025883i");
        //连接上这个网址
        //细节:保证网络是畅通
        URLConnection conn = url.openConnection();//创建一个对象去读取网络中的数据
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        //获取正则表达式的对象pattern
        String regex = "[1-9]\\d{17}";
        Pattern pattern = Pattern.compile(regex);//在读取的时候每次读一整行
        while ((line = br.readLine()) != null) {
            //拿着文本匹配器的对象matcher按照pattern的规则去读取当前的这一行信息
            Matcher matcher = pattern.matcher(line);
            while (matcher.find()) {
                System.out.println(matcher.group());
            }
        }
        br.close();
    }
}

```

###### 贪婪爬取和非贪婪爬取

```java
只写+和表示贪婪匹配，如果在+和后面加问号表示非贪婪爬取
+? 非贪婪匹配
*? 非贪婪匹配
贪婪爬取:在爬取数据的时候尽可能的多获取数据
非贪婪爬取:在爬取数据的时候尽可能的少获取数据

举例：
如果获取数据：ab+
贪婪爬取获取结果:abbbbbbbbbbbb
非贪婪爬取获取结果:ab

```

```java
/*
            有一段字符串:小诗诗dqwefqwfqwfwq12312小丹丹dqwefqwfqwfwq12312小惠惠
            要求1:把字符串中三个姓名之间的字母替换为vs
            要求2:把字符串中的三个姓名切割出来*/

String s = "小诗诗dqwefqwfqwfwq12312小丹丹dqwefqwfqwfwq12312小惠惠";
//细节:
//方法在底层跟之前一样也会创建文本解析器的对象
//然后从头开始去读取字符串中的内容，只要有满足的，那么就切割。
String[] arr = s.split("[\\w&&[^_]]+");
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

```java
/*
            有一段字符串:小诗诗dqwefqwfqwfwq12312小丹丹dqwefqwfqwfwq12312小惠惠
            要求1:把字符串中三个姓名之间的字母替换为vs
            要求2:把字符串中的三个姓名切割出来*/

String s = "小诗诗dqwefqwfqwfwq12312小丹丹dqwefqwfqwfwq12312小惠惠";
//细节:
//方法在底层跟之前一样也会创建文本解析器的对象
//然后从头开始去读取字符串中的内容，只要有满足的，那么就用第一个参数去替换。
String result1 = s.replaceAll("[\\w&&[^_]]+", "vs");
System.out.println(result1);

```

###### 正则表达中的分组的括号：

只看左括号，不看右括号，按照左括号的顺序，从左往右，依次为第一组，第二组，第三组等等

```
//需求1:判断一个字符串的开始字符和结束字符是否一致?只考虑一个字符
//举例: a123a b456b 17891 &abc& a123b(false)
// \\组号:表示把第X组的内容再出来用一次
String regex1 = "(.).+\\1";
System.out.println("a123a".matches(regex1));
System.out.println("b456b".matches(regex1));
System.out.println("17891".matches(regex1));
System.out.println("&abc&".matches(regex1));
System.out.println("a123b".matches(regex1));
System.out.println("--------------------------");


//需求2:判断一个字符串的开始部分和结束部分是否一致?可以有多个字符
//举例: abc123abc b456b 123789123 &!@abc&!@ abc123abd(false)
String regex2 = "(.+).+\\1";
System.out.println("abc123abc".matches(regex2));
System.out.println("b456b".matches(regex2));
System.out.println("123789123".matches(regex2));
System.out.println("&!@abc&!@".matches(regex2));
System.out.println("abc123abd".matches(regex2));
System.out.println("---------------------");

//需求3:判断一个字符串的开始部分和结束部分是否一致?开始部分内部每个字符也需要一致
//举例: aaa123aaa bbb456bbb 111789111 &&abc&&
//(.):把首字母看做一组
// \\2:把首字母拿出来再次使用
// *:作用于\\2,表示后面重复的内容出现一次次或多次
String regex3 = "((.)\\2*).+\\1";
System.out.println("aaa123aaa".matches(regex3));
System.out.println("bbb456bbb".matches(regex3));
System.out.println("111789111".matches(regex3));
System.out.println("&&abc&&".matches(regex3));
System.out.println("aaa123aab".matches(regex3));
```

```java
让我们逐步解释这个正则表达式`String regex3 = "((.)\\2*).+\\1";`：

1. `(`: 这是一个特殊字符，用于创建第一个捕获组。在这里，我们要创建一个捕获组来匹配重复的字符序列。
2. `(`: 这是另一个特殊字符，用于创建第二个捕获组。它将用于匹配一个单独的字符。
3. `.)`: 这是一个点号（`.`），它匹配除换行符外的任意一个字符。但是，由于它在第二个捕获组内部，所以它成为了第二个捕获组的一部分。
4. `\\2*`: 这是一个反斜杠加数字`2`（`\\2`），它表示引用第二个捕获组的内容。后面的`*`是一个限定符，表示它匹配前面的元素零次或多次。所以`\\2*`表示匹配零个或多个与第二个捕获组中相同的字符序列。
5. `)`: 这是用于结束第二个捕获组的特殊字符。
6. `.+`: 这是一个点号（`.`），它匹配除换行符外的任意一个字符，加号（`+`）是一个限定符，表示它匹配前面的元素一次或多次。所以`.+`表示匹配至少一个任意字符。
7. `\\1`: 这是一个反斜杠加数字`1`（`\\1`），它表示引用第一个捕获组的内容。我们在这里引用第一个捕获组，以确保前面匹配的重复字符序列再次出现。

综合起来，这个正则表达式的意思是：匹配一个字符串，其中至少包含一个重复的字符序列，并且该重复的字符序列在字符串的末尾再次出现。
```

###### 分组的替换

```java
String str = "我要学学编编编编程程程程程程";
//需求:把重复的内容 替换为 单个的
//学学                学
//编编编编            编
//程程程程程程        程
//  (.)表示把重复内容的第一个字符看做一组
//  \\1表示第一字符再次出现
//  + 至少一次
//  $1 表示把正则表达式中第一组的内容，再拿出来用
String result = str.replaceAll("(.)\\1+", "$1");
System.out.println(result);
```

### 时间相关类的学习

##### Date 

时间类，用来描述我们的时间，精确到我们呢的毫秒

利用空参数构造创建的对象，默认标识系统的当前时间

利用有参数的构造默认为指定的时间

对象的创建

```java
Date()  分配 Date 对象并初始化此对象，以表示分配它的时间（精确到毫秒）。
Date data=new Date();表示现在的系统的当前的时间
Date data=new Date(指定的毫秒的数值); 表示指定的时间
  
```

修改时间对象中的毫秒数值

```
Date data=new Date(指定的毫秒的数值); 表示指定的时间
data.setTime(毫秒设置)     
```

获取时间对象中的毫秒的数值

```java
Date data=new Date(指定的毫秒的数值); 表示指定的时间
data.getTime()     
```

##### SimpleDataFormat

格式化时间的类

解析，将字符串的时间转成我们的date的对象

定义的字符：

```java
y  年  Year  1996; 96  
M  年中的月份  Month  July; Jul; 07  
w  年中的周数  Number  27  
W  月份中的周数  Number  2  
D  年中的天数  Number  189  
d  月份中的天数  Number  10  
F  月份中的星期  Number  2  
E  星期中的天数  Text  Tuesday; Tue  
a  Am/pm 标记  Text  PM  
H  一天中的小时数（0-23）  Number  0  
k  一天中的小时数（1-24）  Number  24  
K  am/pm 中的小时数（0-11）  Number  0  
h  am/pm 中的小时数（1-12）  Number  12  
m  小时中的分钟数  Number  30  
s  分钟中的秒数  Number  55  
S  毫秒数  Number  978  
z  时区  General time zone  Pacific Standard Time; PST; GMT-08:00  
Z  时区  RFC 822 time zone  -0800  

```

###### 构造的方法：

```java
SimpleDateFormat() 
          用默认的模式和默认语言环境的日期格式符号构造 
SimpleDateFormat(String pattern) 
          用给定的模式和默认语言环境的日期格式符号构造 
SimpleDateFormat(String pattern, DateFormatSymbols formatSymbols) 
          用给定的模式和日期符号构造 SimpleDateFormat。 
SimpleDateFormat(String pattern, Locale locale) 
          用给定的模式和给定语言环境的默认日期格式符号构造 

```

###### 格式化的方法：

```java
Thu Jan 01 08:00:00 CST 1970package com.itheima.test9;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.SimpleFormatter;

public class Timetest1 {
    public static void main(String[] args) {
        SimpleDateFormat sd=new SimpleDateFormat();
        Date dt=new Date(0L);
        System.out.println(dt);
        空参构造完成时间的格式化的操作
        System.out.println(sd.format(dt));
    }
}
输出：
1970/1/1 上午8:00
```

```Java
public class Timetest1 {
    public static void main(String[] args) {
        SimpleDateFormat sd=new SimpleDateFormat();
        Date dt=new Date(0L);
        System.out.println(dt);
        System.out.println(sd.format(dt));
        //带参数的构造的方法
        SimpleDateFormat sd1=new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss");
        根据指定的格式完成时间的格式化的操作
        System.out.println(sd1.format(dt));
    }
}
原格式：
Thu Jan 01 08:00:00 CST 1970
输出：
1970年01月01日 08:00:00
```

```java
public class Timetest1 {
    public static void main(String[] args) throws ParseException {
        SimpleDateFormat sd=new SimpleDateFormat();
        Date dt=new Date(0L);
        System.out.println(dt);
        System.out.println(sd.format(dt));
        //带参数的构造的方法
        SimpleDateFormat sd1=new SimpleDateFormat("yyyy年MM月dd日 HH时:mm分:ss秒 E");
        System.out.println(sd1.format(dt));

        //解析时间的类
        String str="2022-12-12 12:12:12";
        SimpleDateFormat sd2=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date mydate=sd2.parse(str);
        System.out.println(mydate.getTime());

    }
}
输出：
Thu Jan 01 08:00:00 CST 1970
1970/1/1 上午8:00
1970年01月01日 08时:00分:00秒 周四
1670818332000
```

###### 实现解析后转换成指定的格式：

```java
public class Timetest2 {
    public static void main(String[] args) throws ParseException {
        //带参数的构造的方法
        SimpleDateFormat sd1=new SimpleDateFormat("yyyy年MM月dd日");
        //解析时间的类
        String str="2022-12-12";
        SimpleDateFormat sd2=new SimpleDateFormat("yyyy-MM-dd");
        Date mydate=sd2.parse(str);
        System.out.println(mydate.getTime());
        System.out.println(sd1.format(mydate.getTime()));

    }
}

```

##### Calendar

代表系统当前的时间的日历的对象，可以单独的修改，获取时间中的年月日。

构造方法

```java
protected  Calendar() 构造一个带有默认时区和语言环境的 Calendar。 
protected  Calendar(TimeZone zone, Locale aLocale) 构造一个带有指定时区和语言环境的 Calendar 
```

细节:他是一抽象类不能用来直接创建对象

###### 日历对象的创建：

```java
 Calendar c=Calendar.getInstance();创建一个日历的对象获取到当前的时区的信息
```

###### 日历的创建

```java
        Calendar c=Calendar.getInstance();
        System.out.println(c);
        System.out.println(c.getTime());
        Date d=new Date(0L);
        c.setTime(d);
        System.out.println(c.getTime());
```

###### 修改和获取指定的对象：

```java
//get 获取的是日期中某个字段的信息，
        //set 修改的日历中某一个字段的信息
        //add 为某一个字段增加/减少指定的数值
        //0纪元
        //1年
        //2月
        //3一年中的第几周
        //4一个月中的第几周
        //5一个月中的第几天
        Calendar c1=Calendar.getInstance();
        System.out.println(c1.get(Calendar.YEAR));
        System.out.println(c1.get(Calendar.MONTH)+1);
        System.out.println(c1.get(Calendar.DATE));
        System.out.println(c1.get(Calendar.DAY_OF_WEEK));
        c1.set(Calendar.YEAR,1997);
        System.out.println(c1.getTime());
        c1.add(Calendar.MONTH,2);
        System.out.println(c1.getTime());
```

###### 完整代码：

```java
public class Timetest4 {
    public static void main(String[] args) throws ParseException {
        //Calendar 是一个抽象类，不能直接的new,而是通过一个静态的方法获取到我们的子对象，
        //个根据系统的时区获取不同的日历的对象
        //创建的会把时间中的年月日时分秒星期等存储在一个数组之中
        //细节2
        //星期在老外眼里是一周中的第一天
        Calendar c=Calendar.getInstance();
        System.out.println(c);
        System.out.println(c.getTime());
        Date d=new Date(0L);
        c.setTime(d);
        System.out.println(c.getTime());
        //get 获取的是日期中某个字段的信息，
        //set 修改的日历中某一个字段的信息
        //add 为某一个字段增加/减少指定的数值
        //0纪元
        //1年
        //2月
        //3一年中的第几周
        //4一个月中的第几周
        //5一个月中的第几天
        Calendar c1=Calendar.getInstance();
        System.out.println(c1.get(Calendar.YEAR));
        System.out.println(c1.get(Calendar.MONTH)+1);
        System.out.println(c1.get(Calendar.DATE));
        System.out.println(c1.get(Calendar.DAY_OF_WEEK));
        c1.set(Calendar.YEAR,1997);
        System.out.println(c1.getTime());
        c1.add(Calendar.MONTH,2);
        System.out.println(c1.getTime());
    }
}
```

##### JDK8 中新增时间相关类

| JDK8时间类类名    | 作用                   |
| ----------------- | ---------------------- |
| ZoneId            | 时区                   |
| Instant           | 时间戳                 |
| ZoneDateTime      | 带时区的时间           |
| DateTimeFormatter | 用于时间的格式化和解析 |
| LocalDate         | 年、月、日             |
| LocalTime         | 时、分、秒             |
| LocalDateTime     | 年、月、日、时、分、秒 |
| Duration          | 时间间隔（秒，纳，秒） |
| Period            | 时间间隔（年，月，日） |
| ChronoUnit        | 时间间隔（所有单位）   |

###### ZoneId时区

```Java
public class Timetest5 {
    public static void main(String[] args) throws ParseException {
      /*
      static Set<String> getAvailableZoneIds()  获取java 支持的时区
      static ZoneId systemDefault()             获取系统默认的时区
      static ZoneId of(String zoneId)           获取一个指定的时区
       */
        Set<String> availableZoneIds = ZoneId.getAvailableZoneIds();//获取所有的时区的名称
        System.out.println(availableZoneIds.size());
        ZoneId zoneId = ZoneId.systemDefault(); //获取当前的系统的默认的时区
        System.out.println(zoneId);
        System.out.println(ZoneId.of("Asia/Singapore"));//获取指定的时区

    }
}
```

###### Instant：时间戳

常见的方法：

```java
            static Instant now() 获取当前时间的Instant对象(标准时间)
            static Instant ofXxxx(long epochMilli) 根据(秒/毫秒/纳秒)获取Instant对象
            ZonedDateTime atZone(ZoneIdzone) 指定时区
            boolean isxxx(Instant otherInstant) 判断系列的方法
            Instant minusXxx(long millisToSubtract) 减少时间系列的方法
            Instant plusXxx(long millisToSubtract) 增加时间系列的方法
```

完整的代码：

```java
package com.itheima.test9;

import java.text.ParseException;
import java.time.Instant;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Calendar;
import java.util.Date;
import java.util.Set;

public class Timetest5 {
    public static void main(String[] args) throws ParseException {
     /*
            static Instant now() 获取当前时间的Instant对象(标准时间)
            static Instant ofXxxx(long epochMilli) 根据(秒/毫秒/纳秒)获取Instant对象
            ZonedDateTime atZone(ZoneIdzone) 指定时区
            boolean isxxx(Instant otherInstant) 判断系列的方法
            Instant minusXxx(long millisToSubtract) 减少时间系列的方法
            Instant plusXxx(long millisToSubtract) 增加时间系列的方法
        */
//1.获取当前时间的Instant对象(标准时间)
        Instant now = Instant.now();
        System.out.println(now);

//2.根据(秒/毫秒/纳秒)获取Instant对象
        Instant instant1 = Instant.ofEpochMilli(0L);
        System.out.println(instant1);//1970-01-01T00:00:00z

        Instant instant2 = Instant.ofEpochSecond(1L);
        System.out.println(instant2);//1970-01-01T00:00:01Z

        Instant instant3 = Instant.ofEpochSecond(1L, 1000000000L);
        System.out.println(instant3);//1970-01-01T00:00:027

//3. 指定时区
        ZonedDateTime time = Instant.now().atZone(ZoneId.of("Asia/Shanghai"));
        System.out.println(time);

//4.isXxx 判断
        Instant instant4=Instant.ofEpochMilli(0L);
        Instant instant5 =Instant.ofEpochMilli(1000L);

//5.用于时间的判断
//isBefore:判断调用者代表的时间是否在参数表示时间的前面
        boolean result1=instant4.isBefore(instant5);
        System.out.println(result1);//true

//isAfter:判断调用者代表的时间是否在参数表示时间的后面
        boolean result2 = instant4.isAfter(instant5);
        System.out.println(result2);//false

//6.Instant minusXxx(long millisToSubtract) 减少时间系列的方法
        Instant instant6 =Instant.ofEpochMilli(3000L);
        System.out.println(instant6);//1970-01-01T00:00:03Z

        Instant instant7 =instant6.minusSeconds(1);
        System.out.println(instant7);//1970-01-01T00:00:02Z
    }
}

```

###### ZoneDateTime  带时区的时间

```java
/*
            static ZonedDateTime now() 获取当前时间的ZonedDateTime对象
            static ZonedDateTime ofXxxx(。。。) 获取指定时间的ZonedDateTime对象
            ZonedDateTime withXxx(时间) 修改时间系列的方法
            ZonedDateTime minusXxx(时间) 减少时间系列的方法
            ZonedDateTime plusXxx(时间) 增加时间系列的方法
         */
//1.获取当前时间对象(带时区)
ZonedDateTime now = ZonedDateTime.now();
System.out.println(now);

//2.获取指定的时间对象(带时区)1/年月日时分秒纳秒方式指定
ZonedDateTime time1 = ZonedDateTime.of(2023, 10, 1,
                                       11, 12, 12, 0, ZoneId.of("Asia/Shanghai"));
System.out.println(time1);

//通过Instant + 时区的方式指定获取时间对象
Instant instant = Instant.ofEpochMilli(0L);
ZoneId zoneId = ZoneId.of("Asia/Shanghai");
ZonedDateTime time2 = ZonedDateTime.ofInstant(instant, zoneId);
System.out.println(time2);


//3.withXxx 修改时间系列的方法
ZonedDateTime time3 = time2.withYear(2000);
System.out.println(time3);

//4. 减少时间
ZonedDateTime time4 = time3.minusYears(1);
System.out.println(time4);

//5.增加时间
ZonedDateTime time5 = time4.plusYears(1);
System.out.println(time5);
```

###### DateTimeFormatter   用于时间的格式化和解析

```java
/*
            static DateTimeFormatter ofPattern(格式) 获取格式对象
            String format(时间对象) 按照指定方式格式化
        */
//获取时间对象
ZonedDateTime time = Instant.now().atZone(ZoneId.of("Asia/Shanghai"));

// 解析/格式化器
DateTimeFormatter dtf1=DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm;ss EE a");
// 格式化
System.out.println(dtf1.format(time));
```

###### LocalDate  年、月、日

```java
//1.获取当前时间的日历对象(包含 年月日)

LocalDate nowDate = LocalDate.now();
//System.out.println("今天的日期:" + nowDate);
//2.获取指定的时间的日历对象

LocalDate ldDate = LocalDate.of(2023, 1, 1);
System.out.println("指定日期:" + ldDate);

System.out.println("=============================");

//3.get系列方法获取日历中的每一个属性值//获取年
int year = ldDate.getYear();
System.out.println("year: " + year);
//获取月//方式一:
Month m = ldDate.getMonth();
System.out.println(m);
System.out.println(m.getValue());

//方式二:
int month = ldDate.getMonthValue();
System.out.println("month: " + month);


//获取日
int day = ldDate.getDayOfMonth();
System.out.println("day:" + day);

//获取一年的第几天
int dayofYear = ldDate.getDayOfYear();
System.out.println("dayOfYear:" + dayofYear);

//获取星期
DayOfWeek dayOfWeek = ldDate.getDayOfWeek();
System.out.println(dayOfWeek);
System.out.println(dayOfWeek.getValue());

//is开头的方法表示判断
System.out.println(ldDate.isBefore(ldDate));
System.out.println(ldDate.isAfter(ldDate));

//with开头的方法表示修改，只能修改年月日
LocalDate withLocalDate = ldDate.withYear(2000);
System.out.println(withLocalDate);

//minus开头的方法表示减少，只能减少年月日
LocalDate minusLocalDate = ldDate.minusYears(1);
System.out.println(minusLocalDate);


//plus开头的方法表示增加，只能增加年月日
LocalDate plusLocalDate = ldDate.plusDays(1);
System.out.println(plusLocalDate);

//-------------
// 判断今天是否是你的生日
LocalDate birDate = LocalDate.of(2000, 1, 1);
LocalDate nowDate1 = LocalDate.now();

MonthDay birMd = MonthDay.of(birDate.getMonthValue(), birDate.getDayOfMonth());
MonthDay nowMd = MonthDay.from(nowDate1);

System.out.println("今天是你的生日吗? " + birMd.equals(nowMd));//今天是你的生日吗?
```

###### LocalTime  时、分、秒

```java
// 获取本地时间的日历对象。(包含 时分秒)
LocalTime nowTime = LocalTime.now();
System.out.println("今天的时间:" + nowTime);
int hour = nowTime.getHour();//时
System.out.println("hour: " + hour);
int minute = nowTime.getMinute();//分
System.out.println("minute: " + minute);
int second = nowTime.getSecond();//秒
System.out.println("second:" + second);
int nano = nowTime.getNano();//纳秒
System.out.println("nano:" + nano);
System.out.println("------------------------------------");
System.out.println(LocalTime.of(8, 20));//时分
System.out.println(LocalTime.of(8, 20, 30));//时分秒
System.out.println(LocalTime.of(8, 20, 30, 150));//时分秒纳秒
LocalTime mTime = LocalTime.of(8, 20, 30, 150);

//is系列的方法
System.out.println(nowTime.isBefore(mTime));
System.out.println(nowTime.isAfter(mTime));

//with系列的方法，只能修改时、分、秒
System.out.println(nowTime.withHour(10));

//plus系列的方法，只能修改时、分、秒
System.out.println(nowTime.plusHours(10));
```

######  LocalDateTime 与 LocalDate 和 LocalTime的相互的转换：

```java
 LocalDateTime today = LocalDateTime.now();
 System.out.println(today);
 System.out.println(today.toLocalDate());
 System.out.println(today.toLocalTime());
```

######  Duration  时间间隔（秒，纳，秒）

```java
// 本地日期时间对象。
LocalDateTime today = LocalDateTime.now();
System.out.println(today);

// 出生的日期时间对象
LocalDateTime birthDate = LocalDateTime.of(2000, 1, 1, 0, 0, 0);
System.out.println(birthDate);

Duration duration = Duration.between(birthDate, today);//第二个参数减第一个参数
System.out.println("相差的时间间隔对象:" + duration);

System.out.println("============================================");
System.out.println(duration.toDays());//两个时间差的天数
System.out.println(duration.toHours());//两个时间差的小时数
System.out.println(duration.toMinutes());//两个时间差的分钟数
System.out.println(duration.toMillis());//两个时间差的毫秒数
System.out.println(duration.toNanos());//两个时间差的纳秒数
```

###### Period  时间间隔（年，月，日）

```java
// 当前本地 年月日
LocalDate today = LocalDate.now();
System.out.println(today);

// 生日的 年月日
LocalDate birthDate = LocalDate.of(2000, 1, 1);
System.out.println(birthDate);

Period period = Period.between(birthDate, today);//第二个参数减第一个参数

System.out.println("相差的时间间隔对象:" + period);
System.out.println(period.getYears());
System.out.println(period.getMonths());
System.out.println(period.getDays());

System.out.println(period.toTotalMonths());
```

######  ChronoUnit  时间间隔（所有单位）：工具类

```java
// 当前时间
LocalDateTime today = LocalDateTime.now();
System.out.println(today);
// 生日时间
LocalDateTime birthDate = LocalDateTime.of(2000, 1, 1,0, 0, 0);
System.out.println(birthDate);

System.out.println("相差的年数:" + ChronoUnit.YEARS.between(birthDate, today));
System.out.println("相差的月数:" + ChronoUnit.MONTHS.between(birthDate, today));
System.out.println("相差的周数:" + ChronoUnit.WEEKS.between(birthDate, today));
System.out.println("相差的天数:" + ChronoUnit.DAYS.between(birthDate, today));
System.out.println("相差的时数:" + ChronoUnit.HOURS.between(birthDate, today));
System.out.println("相差的分数:" + ChronoUnit.MINUTES.between(birthDate, today));
System.out.println("相差的秒数:" + ChronoUnit.SECONDS.between(birthDate, today));
System.out.println("相差的毫秒数:" + ChronoUnit.MILLIS.between(birthDate, today));
System.out.println("相差的微秒数:" + ChronoUnit.MICROS.between(birthDate, today));
System.out.println("相差的纳秒数:" + ChronoUnit.NANOS.between(birthDate, today));
System.out.println("相差的半天数:" + ChronoUnit.HALF_DAYS.between(birthDate, today));
System.out.println("相差的十年数:" + ChronoUnit.DECADES.between(birthDate, today));
System.out.println("相差的世纪(百年)数:" + ChronoUnit.CENTURIES.between(birthDate, today));
System.out.println("相差的千年数:" + ChronoUnit.MILLENNIA.between(birthDate, today));
System.out.println("相差的纪元数:" + ChronoUnit.ERAS.between(birthDate, today));
```

### 包装类：基本类型对应的对象

Java提供了两个类型系统，基本类型与引用类型，使用基本类型在于效率，然而很多情况，会创建对象使用，因为对象可以做更多的功能，如果想要我们的基本类型像对象一样操作，就可以使用基本类型对应的包装类，如下：

| 基本类型 | 对应的包装类（位于java.lang包中） |
| -------- | --------------------------------- |
| byte     | Byte                              |
| short    | Short                             |
| int      | **Integer**                       |
| long     | Long                              |
| float    | Float                             |
| double   | Double                            |
| char     | **Character**                     |
| boolean  | Boolean                           |

#### Integer类

| public Integer(int   value)             | 根据 int 值创建 Integer 对象(过时)     |
| --------------------------------------- | -------------------------------------- |
| public Integer(String s)                | 根据 String 值创建 Integer 对象(过时)  |
| public static Integer valueOf(int i)    | 返回表示指定的 int 值的 Integer   实例 |
| public static Integer valueOf(String s) | 返回保存指定String值的 Integer 对象    |
| static string tobinarystring(int i)     | 得到二进制                             |
| static string tooctalstring(int i)      | 得到八进制                             |
| static string toHexstring(int i)        | 得到十六进制                           |
| static int parseInt(string s)           | 将字符串类型的整数转成int类型的整数    |

##### 自动装箱和自动拆箱：

JDK5后对数据包装类的邢增的特性：自动装箱和自动拆箱

```java
Integer i = 4;//自动装箱。相当于Integer i = Integer.valueOf(4);
i = i + 5;//等号右边：将i对象转成基本数值(自动拆箱) i.intValue() + 5;
//加法运算完成后，再次装箱，把基本数值转成对象。
```

获取包装类的对象我们只需要进行赋值即可不需要我们的调用方法

##### 常用的方法：

```java
/*
            public static string tobinarystring(int i) 得到二进制
            public static string tooctalstring(int i) 得到八进制
            public static string toHexstring(int i) 得到十六进制
            public static int parseInt(string s) 将字符串类型的整数转成int类型的整数
 */

```

##### 底层原理

建议：获取Integer对象的时候不要自己new，而是采取直接赋值或者静态方法valueOf的方式

因为在实际开发中，-128~127之间的数据，用的比较多。如果每次使用都是new对象，那么太浪费内存了。

所以，提前把这个范围之内的每一个数据都创建好对象，如果要用到了不会创建新的，而是返回已经创建好的对象。

```java
//1.利用构造方法获取Integer的对象(JDK5以前的方式)
/*Integer i1 = new Integer(1);
        Integer i2 = new Integer("1");
        System.out.println(i1);
        System.out.println(i2);*/

//2.利用静态方法获取Integer的对象(JDK5以前的方式)
Integer i3 = Integer.valueOf(123);
Integer i4 = Integer.valueOf("123");
Integer i5 = Integer.valueOf("123", 8);

System.out.println(i3);
System.out.println(i4);
System.out.println(i5);

//3.这两种方式获取对象的区别(掌握)
//底层原理：
//因为在实际开发中，-128~127之间的数据，用的比较多。
//如果每次使用都是new对象，那么太浪费内存了
//所以，提前把这个范围之内的每一个数据都创建好对象
//如果要用到了不会创建新的，而是返回已经创建好的对象。
Integer i6 = Integer.valueOf(127);
Integer i7 = Integer.valueOf(127);
System.out.println(i6 == i7);//true

Integer i8 = Integer.valueOf(128);
Integer i9 = Integer.valueOf(128);
System.out.println(i8 == i9);//false

//因为看到了new关键字，在Java中，每一次new都是创建了一个新的对象
//所以下面的两个对象都是new出来，地址值不一样。
/*Integer i10 = new Integer(127);
        Integer i11 = new Integer(127);
        System.out.println(i10 == i11);

        Integer i12 = new Integer(128);
        Integer i13 = new Integer(128);
        System.out.println(i12 == i13);*/
```

## 常见的算法：

### 查找算法：

##### 基本查找：

顺序查找也称为线形查找，属于无序查找算法。从数据结构线的一端开始，顺序扫描，依次将遍历到的结点与要查找的值相比较，若相等则表示查找成功；若遍历结束仍没有找到相同的，表示查找失败。

```java
public class A01_BasicSearchDemo1 {
    public static void main(String[] args) {
        //基本查找/顺序查找
        //核心：
        //从0索引开始挨个往后查找

        //需求：定义一个方法利用基本查找，查询某个元素是否存在
        //数据如下：{131, 127, 147, 81, 103, 23, 7, 79}


        int[] arr = {131, 127, 147, 81, 103, 23, 7, 79};
        int number = 82;
        System.out.println(basicSearch(arr, number));

    }

    //参数：
    //一：数组
    //二：要查找的元素

    //返回值：
    //元素是否存在
    public static boolean basicSearch(int[] arr, int number){
        //利用基本查找来查找number在数组中是否存在
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == number){
                return true;
            }
        }
        return false;
    }
}
```

##### 二分查找

也称为是折半查找，属于有序查找算法。用给定值先与***中间结点***比较。比较完之后有三种情况：

* 相等

  说明找到了

* 要查找的数据比中间节点小

  说明要查找的数字在中间节点左边

* 要查找的数据比中间节点大

  说明要查找的数字在中间节点右边

```java
  public static int halfSearch(int[] arr, int number){
        int min=0;
        int max=arr.length-1;
        while (true){
            if(min>max){
                return -1;
            }

            int mid=(max+min)/2;

            if(number<arr[mid]){
               max=mid-1;
            }
            else if(number>arr[mid]){
                min=mid+1;
            }else {
                return mid;
            }
        }
```

##### 插值查找

基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。当然，差值查找也属于有序查找。

```java
    public static int inserthalfSearch(int[] arr, int number){
        int min=0;
        int max=arr.length-1;
        while (true){
            if(min>max){
                return -1;
            }

            int mid=min+(number-arr[min])/(arr[max]-arr[min])*(max-min);

            if(number<arr[mid]){
                max=mid-1;
            }
            else if(number>arr[mid]){
                min=mid+1;
            }else {
                return mid;
            }
        }
    }
```

##### 斐波那契查找





## Arrays:

array的方法基本上都是使用的静态修饰的，因此我们可以不需要创建对象，直接使用就可以。

```java
static String toString(boolean[] a) 
          返回指定数组内容的字符串表示形式。 
```

#### 数组的字符串化：

```java
package com.itheima.test11;

import java.util.Arrays;

public class Arraystest_demo {
    public static void main(String[] args) {
        int[] arr={1,2,3,4,5,6,7,8,9};
        System.out.println(Arrays.toString(arr));
    }
}
数组转成字符串输出
    
```

#### 数组的排序

###### 默认下对基本的数据进行排序

```java
static void sort(int[] a) 
          对指定的 int 型数组按数字升序进行排序。 
```

```java
package com.itheima.test11;

import java.util.Arrays;

public class Arraystest_demo {
    public static void main(String[] args) {
        int[] arr={1,3,2,10,9,6,7,5,4};
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}

```

###### 自定义规则的数据的排序：要求必须为引用数据类型

如果数据为基本的数据类型需要将其转换为引用数据类型。

sort的底层的原理，插入+二分查找的方式进行排序

默认认为我们的0索引为有序的序列，序列到最后默认认为是无需的序列

遍历无序的序列，得到里面的每一个的元素，假设当前遍历到的是元素A

吧A望有序的序列中进行插入，在插入的时候，利用二分查找确定对应的插入点。

比较的规则就是我们comparator的方法体

O1为我们的无序的数组中的遍历元素

O2为我们的有序序列中的元素

返回值：

负数：表示当前需要插入的元素是小的放在前面

正数：表示当前要插入的元素是大的放在后面

0：表示当前的元素和比较的元素是一样的放在后面

```java
package com.itheima.test11;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Comparator;

public class Arraystest_demo {
    public static void main(String[] args) {
        Integer[] arr={1,3,2,10,9,6,7,5,4};
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr, 0, 9, new Comparator<Integer>() {
                    @Override
                    public int compare(Integer o1, Integer o2) {
                        System.out.println("______________________");
                        System.out.println("o1:"+o1);
                        System.out.println("o2:"+o2);
                        return o1-o2;
                    }
                });
                //第二个参数是一个接口，我们需要传递这个接口的实现类对象作为排序的规则
                System.out.println(Arrays.binarySearch(arr, 4));
        System.out.println(Arrays.toString(arr));
    }
}

```

```java
______________________首先其默认0索引为有序，之后的默认为无序的
o1:3
o2:1
______________________遍历无序，得到3和1比较，3-1为正默认其为大，因此放后面
o1:2
o2:3
______________________现在的有序的数列为1，3 遍历无序的为2，2 和3比较，得负数，因此为小放前面
o1:2
o2:3
______________________然后再吧2和1 做比较得到1，为正，为大放后面
o1:2
o2:1
______________________
o1:10
o2:2
______________________
o1:10
o2:3
______________________升序：
```

##### 降序

```java
package com.itheima.test11;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Comparator;

public class Arraystest_demo {
    public static void main(String[] args) {
        Integer[] arr={1,3,2,10,9,6,7,5,4};
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr, 0, 9, new Comparator<Integer>() {
                    @Override
                    public int compare(Integer o1, Integer o2) {
                        System.out.println("______________________");
                        System.out.println("o1:"+o1);
                        System.out.println("o2:"+o2);
                        return o2-o1;
                    }
                });
                //第二个参数是一个接口，我们需要传递这个接口的实现类对象作为排序的规则
                System.out.println(Arrays.binarySearch(arr, 4));
        System.out.println(Arrays.toString(arr));
    }
}
```

#### 数组的填充：

```java
package com.itheima.test11;

import java.util.Arrays;

public class Arraystest_demo1 {
    public static void main(String[] args) {
        int Arr[]=new int[27];
        Arrays.fill(Arr,100);
        System.out.println(Arrays.toString(Arr));
    }
}
```

#### 数组的比较

```java
package com.itheima.test11;

import java.util.Arrays;

public class Arraystest_demo1 {
    public static void main(String[] args) {
        int Arr[]=new int[27];
        int Arr1[]=new int[27];
        Arrays.fill(Arr,100);
        Arrays.fill(Arr1,100);
        System.out.println(Arrays.equals(Arr, Arr1));

    }
}

```

#### 数组的复制

```java
package com.itheima.test11;
import java.util.Arrays;
public class Arraystest_demo1 {
    public static void main(String[] args) {
        int Arr[]=new int[27];
        int Arr1[]=new int[27];
        Arrays.fill(Arr,100);
        Arrays.fill(Arr1,100);
        System.out.println(Arrays.equals(Arr, Arr1));
        int[] ints = Arrays.copyOf(Arr, 28);
        System.out.println(Arrays.toString(ints));
    }
}

```

#### 二分查找

二分查找的元素必须是升序的、

二分法查找元素的时候，元素首先必须有序且必须为升序

如果元素是存在的，那返回的是真实的索引，如果元素是不存在的那么返回的是:-插入点-1

出现-插入点-1的原因，假如我们的出现的插入点为0 的时候负的插入点就会还是0 这个就会导致粗错

##### 例如错误案例：

```java
package com.itheima.test11;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Comparator;

public class Arraystest_demo {
    public static void main(String[] args) {
        int[] arr={1,3,2,10,9,6,7,5,4};
        System.out.println(Arrays.toString(arr));
        //Arrays.sort(arr,0,9);
        System.out.println(Arrays.binarySearch(arr, 4));
        System.out.println(Arrays.toString(arr));
    }
    
}
```

##### 正确的案例：必须先排序后进行二分查找

```java
package com.itheima.test11;

import java.util.Arrays;
import java.util.Calendar;
import java.util.Comparator;

public class Arraystest_demo {
    public static void main(String[] args) {
        int[] arr={1,3,2,10,9,6,7,5,4};
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr,0,9);
        System.out.println(Arrays.binarySearch(arr, 4));
```

## lamada表达式：

简化我们的代码

函数式的编程：强调做什么，而不是谁来做

需要我们的接口中有且只有一个方法

可以采用我们的lamada的表达式来简写

###### 标准的格式：

```JAVA
（方法的形参）->{
方法体
}
```

lamada表达式用来间写匿名内部类的书写

只能简化函数式接口的匿名内部类的写法

什么叫做函数式的接口：

有且只有一个抽象方法的接口叫做函数式的接口

```java
package com.itheima.test11;

import java.util.Arrays;
import java.util.Comparator;

public class lamada_demo1 {
    public static void main(String[] args) {
        Integer[] arr={1,3,2,10,9,6,7,5,4};
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr, 0, 9, (Integer o1, Integer o2)->o2-o1);
        //第二个参数是一个接口，我们需要传递这个接口的实现类对象作为排序的规则
        System.out.println(Arrays.binarySearch(arr, 4));
        System.out.println(Arrays.toString(arr));
    }
    }


```

举例：

```java
package com.itheima.test11;

import java.util.Arrays;
import java.util.Comparator;

public class lamada_demo1 {
    public static void main(String[] args) {
        method(()-> System.out.println("hello")
        );
    }
    public static void method(Swim s){
       s.swimming();
    }
    interface Swim{
        public abstract void swimming();
    }
    }
```

###### lamada表达式的省略的形式：

可以推导可以省略的核心思想

```java
public static void main(String[] args) {
        Integer[] arr={1,3,2,10,9,6,7,5,4};
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr, 0, 9, (o1,o2)->o2-o1);
        //第二个参数是一个接口，我们需要传递这个接口的实现类对象作为排序的规则
        System.out.println(Arrays.binarySearch(arr, 4));
        System.out.println(Arrays.toString(arr));
       

    }
```

练习：

```java
package com.itheima.test11;
import java.util.Arrays;
public class lamada_demo2 {
    public static void main(String[] args) {
        String[] arr={"AAA","BBBB","CCCC","SSSSSS"};
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr, 0, 4, (o1,o2)->o2.length()-o1.length());
        //第二个参数是一个接口，我们需要传递这个接口的实现类对象作为排序的规则
       System.out.println(Arrays.toString(arr));
    }
    }
通过长度比较字符串并进行排序的
   
```

```java
package com.itheima.test11;

import java.util.Arrays;
import java.util.Comparator;

public class test {
    public static void main(String[] args) {
        Boyfriends b1=new Boyfriends("zhangsan",18,178);
        Boyfriends b2=new Boyfriends("wangsa",19,180);
        Boyfriends b3=new Boyfriends("zhoasanze",20,167);
        Boyfriends[] boy={b1,b2,b3};
        sort(boy);
        System.out.println(Arrays.toString(boy));

    }
     public static Boyfriends[] sort(Boyfriends[] boy) {
         Arrays.sort(boy, (o1, o2) -> {
         double temp = o2.getAge()-o1.getAge();
         temp= temp== 0 ? o2.getHeight()-o1.getHeight() : temp;
         temp= temp== 0 ? o2.getName().length()-o1.getName().length():temp;
         if(temp>0){
             return 1;
         } else if (temp<=0) {
             return -1;
         }else
             return 0;
         });
         return boy;
     }
}

```

###### 不死神兔：

第一种遍历数组赋值

```java
        int[] arr=new int[12];
        arr[0]=1;
        arr[1]=1;
        for (int i = 2; i < arr.length; i++) {
            arr[i]=arr[i-1]+arr[i-2];
        }
        System.out.println(arr[11]);
```



第二种采用递归的方法

```java
    public static int getsum(int month){
        if (month==1||month==2)
            return 1;
        else
            return getsum(month-1)+getsum(month-2);
    }
}
```

###### 猴子吃桃：经典递归

每天吃一半的基础上多吃一个

```java
        int sum=getsum(1);
        System.out.println(sum);
    public static int getsum(int month){
        if (month<=0 || month>=11){
            System.out.println("error");
            return -1;}
        if (month==10)
            return 1;
        return (getsum(month+1)+1)*2;
    }

```

| day  | num  | 计算      |
| ---- | ---- | --------- |
| 10   | 1    | 1         |
| 9    | 4    | （1+1）*2 |
| 8    | 10   | （4+1）*2 |

###### 正着推理：

| day  | num  |
| ---- | ---- |
| 8    | 10   |
| 9    | 4    |
| 10   | 1    |

###### 依赖

$$
Num[today]=(Num[nextday]+1)*2
$$

###### 小明爬楼梯

小明爬楼梯的方法，首先有时候爬一层有时候爬俩层，如果一共有二十层怎么爬？有多少种方法？

###### 分析:

| 层数 | num  | 算法 |
| ---- | ---- | ---- |
| 1    | 1    | 1    |
| 2    | 2    | 2    |
| 3    | 3    | 1+2  |
| 4    | 5    | 2+3  |

```java 
package com.itheima.test11;

public class test5 {
    public static void main(String[] args) {
        System.out.println(getsum(7));
    }
    public static int getsum(int layzer){
       if(layzer==1){
           return 1;
       }else if (layzer==2){
           return 2;
       }
       else
           return getsum(layzer-1)+getsum(layzer-2);
    }
}

```

###### 依赖：

$$
getsum(layzer)=getsum(layzer-1)+getsum(layzer-2);
$$

## 集合进阶：

### 集合的体系结构：

#### collection：单列的集合

collection是单列集合的祖宗接口，他的功能是全部的单列集合都可以继承使用的

#### collection的通用的方法：

```java
 boolean add(E e) 
          确保此 collection 包含指定的元素（可选操作）。 
 boolean addAll(Collection<? extends E> c) 
          将指定 collection 中的所有元素都添加到此 collection 中（可选操作）。 
 void clear() 
          移除此 collection 中的所有元素（可选操作）。 
 boolean contains(Object o) 
          如果此 collection 包含指定的元素，则返回 true。 
 boolean containsAll(Collection<?> c) 
          如果此 collection 包含指定 collection 中的所有元素，则返回 true。 
 boolean equals(Object o) 
          比较此 collection 与指定对象是否相等。 
 int hashCode() 
          返回此 collection 的哈希码值。 
 boolean isEmpty() 
          如果此 collection 不包含元素，则返回 true。 
 Iterator<E> iterator() 
          返回在此 collection 的元素上进行迭代的迭代器。 
 boolean remove(Object o) 
          从此 collection 中移除指定元素的单个实例，如果存在的话（可选操作）。 
 boolean removeAll(Collection<?> c) 
          移除此 collection 中那些也包含在指定 collection 中的所有元素（可选操作）。 
 boolean retainAll(Collection<?> c) 
          仅保留此 collection 中那些也包含在指定 collection 的元素（可选操作）。 
 int size() 
          返回此 collection 中的元素数。 
 Object[] toArray() 
          返回包含此 collection 中所有元素的数组。 
<T> T[] 
 toArray(T[] a) 
          返回包含此 collection 中所有元素的数组；返回数组的运行时类型与指定数组的运行时类型相同。 

```

首先Collection是一个接口我们没有办法去创建他的对象只能创建我们的接口的实现类对象。

##### contain:

contain的底层其实是依赖于我们的equal 的

所以当我们想要去实现类似于学生的对象的检索比较的时候我们需要重写这个equal的方法：

```java
public class collectiondemo2 {
    //接口没办法直接创建我们的目标的对象，只能根据我们的实现类来使用
    //采用这种方法来学习我们的collection中的方法
    public static void main(String[] args) {
        Collection<student> stu=new ArrayList<>();
        stu.add(new student("zhangsan",18,"1234",187));
        stu.add(new student("zhangsan1",19,"1234",187));
        stu.add(new student("zhangsan2",20,"1234",187));
        stu.add(new student("zhangsan3",21,"1234",187));
        stu.add(new student("zhangsan",18,"1234",187));
        System.out.println(stu);
        System.out.println(stu.contains(new student("zhangsan", 18, "1234", 187)));
    }
}

```

###### 重写的equal的方法：

```java
 @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        student student = (student) o;
        return age == student.age && height == student.height && Objects.equals(name, student.name) && Objects.equals(id, student.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age, id, height);
    }
```

##### Collection系列的元素的遍历：

三大遍历的方式：迭代器遍历  增强for循环 lambda表达式

###### 迭代器遍历

```java
迭代器遍历我们的集合
Iterator<E> iterator() 
          返回在此 collection 的元素上进行迭代的迭代器。 
注意事项：
    迭代器遍历结束之后，指针不会复位
    循环中只能用一次next的方法
    迭代器遍历的时候不能用集合的方法去增加或者删除（可能会导致迭代器中的游标的位置和真实的数据位置不匹配报错）
    如果必须进行删除的操作，可以使用迭代器的方法remove进行删除的操作
    迭代器的指针再遍历完之后不会复位，重新遍历的只能重新获取一个新的迭代器的对象。
    next的方法获取元素并移动指针
    
    
```

举例：

```java
public class collectiondemo2 {
    //接口没办法直接创建我们的目标的对象，只能根据我们的实现类来使用
    //采用这种方法来学习我们的collection中的方法
    public static void main(String[] args) {
        Collection<student> stu=new ArrayList<>();
        stu.add(new student("zhangsan",18,"1234",187));
        stu.add(new student("zhangsan1",19,"1234",187));
        stu.add(new student("zhangsan2",20,"1234",187));
        stu.add(new student("zhangsan3",21,"1234",187));
        stu.add(new student("zhangsan",18,"1234",187));
        System.out.println(stu);
        System.out.println(stu.contains(new student("zhangsan", 18, "1234", 187)));
        Iterator<student> it=stu.iterator();
        //next获取当前的元素的位置，然后下次将迭代器的对象移动到下一个位置
        System.out.println(it.next());
        System.out.println(it.next());
        System.out.println(it.next());
        //hashnext 判断当前的位置是否存在元素，存在元素则返回true ,否则返回false
        System.out.println(it.hasNext());
    }
}
```

迭代器的遍历增删元素的时候：

```java
  while (it.hasNext()){
            String str= it.next().getName();
            if("zhangsan".equals(str)){
                stu.remove(new student("zhangsan",18,"1234",187));
                System.out.println("已经删除");
            }
        }
        System.out.println(stu);
    }
```

报出并发异常的错误：ConcurrentModificationException

解决的方法：

```java
 while (it.hasNext()){
            String str= it.next().getName();
            if("zhangsan".equals(str)){
                it.remove();使用迭代器中的删除的方法
                System.out.println("已经删除");
            }
        }
        System.out.println(stu);
```

###### 增强for的遍历：

```java
所有的数组和单列的集合才可以使用增强for的遍历方法

增强for的底层就是迭代器，为了简化迭代器的操作而实现的
    快速的生成的方式：
    集合名字.for enter 生成
增强for的细节注意点
        就是再=修改增强for的第三方的变量是不影响原本的集合中的数据的
```

```Java
public class Arraystest_demo2 {
    //接口没办法直接创建我们的目标的对象，只能根据我们的实现类来使用
    //采用这种方法来学习我们的collection中的方法
    public static void main(String[] args) {
        Collection<student> stu=new ArrayList<>();
        stu.add(new student("zhangsan",18,"1234",187));
        stu.add(new student("zhangsan1",19,"1234",187));
        stu.add(new student("zhangsan2",20,"1234",187));
        stu.add(new student("zhangsan3",21,"1234",187));
        stu.add(new student("zhangsan",18,"1234",187));
        System.out.println(stu);
        System.out.println(stu.contains(new student("zhangsan", 18, "1234", 187)));
        for (student s: stu){
            System.out.println(s);
        }
    }
}
```

###### lamada表达式的遍历：

```java
得益于Jdk 8 lamada技术，提供一种简介的遍历的方法
default void forEach(Consumer<? super T> action)
集合lamada遍历数组或者集合   
    方法的底层，其实也就是自己遍历所有的集合，得到相应的元素，并将元素传递给我们的accept的方法，例如我们的重写的是打印这对象元素，其对应的也就是获取到每一个元素并将其打印
```

```java
采用匿名内部类的方式实现
public class collectiondemo3 {
    //接口没办法直接创建我们的目标的对象，只能根据我们的实现类来使用
    //采用这种方法来学习我们的collection中的方法
    public static void main(String[] args) {
        Collection<student> stu=new ArrayList<>();
        stu.add(new student("zhangsan",18,"1234",187));
        stu.add(new student("zhangsan1",19,"1234",187));
        stu.add(new student("zhangsan2",20,"1234",187));
        stu.add(new student("zhangsan3",21,"1234",187));
        stu.add(new student("zhangsan",18,"1234",187));
        System.out.println(stu);
        System.out.println(stu.contains(new student("zhangsan", 18, "1234", 187)));
        //首先使用匿名内部类的方式实现这个
        stu.forEach(new Consumer<student>() {
            @Override
            public void accept(student student) {
                System.out.println(student);
            }
        });
    }
}

```

改成lamada表达式

```java
改成lamada的形式：
public class collectiondemo3 {
    //接口没办法直接创建我们的目标的对象，只能根据我们的实现类来使用
    //采用这种方法来学习我们的collection中的方法
    public static void main(String[] args) {
        Collection<student> stu=new ArrayList<>();
        stu.add(new student("zhangsan",18,"1234",187));
        stu.add(new student("zhangsan1",19,"1234",187));
        stu.add(new student("zhangsan2",20,"1234",187));
        stu.add(new student("zhangsan3",21,"1234",187));
        stu.add(new student("zhangsan",18,"1234",187));
        System.out.println(stu);
        System.out.println(stu.contains(new student("zhangsan", 18, "1234", 187)));
        //首先使用匿名内部类的方式实现这个
        stu.forEach((student)->{
                System.out.println(student);
            }
        );
    }
}
```

#### list系列:有序可重复有索引

###### ArrayList:底层原理

```java
arraylist 的底层是数组结构的

1，空参构造的时候，arraylist 会创建一个默认的长度为0的数组。
2，添加第一个的元素的时候，底层会创建一个新的长度为10的数组
3，size 有俩层意义，一表示元素的个数 其二表示元素下次存入的位置索引；
4，当数据存满的时候，就会扩充为原来的1.5倍
5如果一次性存入多个元素，1.5倍放不下的时候，则新创建的数组的长度以实际为准。
源码：
public ArrayList() {
     this.elementData = DEFAULTCAPACITY_EMPTY_ELEMENTDATA;
    }   
 this.elementData本质上是个数组；
 DEFAULTCAPACITY_EMPTY_ELEMENTDATA   为长度是零的数组
add的源码：
会先判断size和自定义的数组的长度进行一个比较
如果发现其存储的元素的size已经到达最大的数组的长度，这里会使用grow进行扩容的操作。
通过扩容的操作得到我们的新的数组，然后使用copy到新的数组中；
     参数一：元素的名字
     参数二：集合的数组得名字
     参数三：集合的长度当前的元素存储的位置

     
private void add(E e, Object[] elementData, int s) {
        if (s == elementData.length)
            elementData = grow();
        elementData[s] = e;
        size = s + 1;
    } 
 size = s + 1;其实就是我们的实际的数据的长度其实也是我们位置的索引。


elementData = grow();执行数组的扩容
扩容的方法：传入的参数为最小的扩容容量    
private Object[] grow(int minCapacity) {
        int oldCapacity = elementData.length;记录原来的容量
        if (oldCapacity > 0 || elementData != DEFAULTCAPACITY_EMPTY_ELEMENTDATA) {
            int newCapacity = ArraysSupport.newLength(oldCapacity,
                    minCapacity - oldCapacity, /* minimum growth */
                    oldCapacity >> 1           /* preferred growth */);数组的扩容右移一位 默认就是扩容原来的一半，也就是原来的1.5倍。
 return elementData =Arrays.copyOf(elementData,newCapacity);
  } 
 else {
 return elementData = new Object[Math.max(DEFAULT_CAPACITY, minCapacity)];第一次的创建的时候会产生一个10 的数组。
        }
    }    
```

扩容最底层的代码：

```java
    public static int newLength(int oldLength, int minGrowth, int prefGrowth) {
        // preconditions not checked because of inlining
        // assert oldLength >= 0
        // assert minGrowth > 0

        int prefLength = oldLength + Math.max(minGrowth, prefGrowth); // might overflow
        if (0 < prefLength && prefLength <= SOFT_MAX_ARRAY_LENGTH) {
            return prefLength;
        } else {
            // put code cold in a separate method
            return hugeLength(oldLength, minGrowth);
        }
    }
int prefLength = oldLength + Math.max(minGrowth,prefGrowth); 拿着至少需要增加的容量和默认需要增加的容量做一个比较，选取一个最大的数值、在集合中默认不仅是一次加一，有时候还会增加许多的元素
当我们一下子增加若干的数据的时候，就会出现一Math.max(minGrowth,prefGrowth)，minGrowth 大于pregrowth,因此我们就会开始采用最大的最为扩容的容量的浮动。
```

###### LinkedList的底层原理:

```java
Linklist是一个双链表的基本的数据结构，查询慢，增删满，但是如果操作的是首尾的元素的时候，速度很快。

```

```java
链表的节点的源码， 
private static class Node<E> {
        E item;
        Node<E> next;
        Node<E> prev;

        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }
```

```java
add的代码：
public boolean add(E e) {
        linkLast(e);
        return true;
    }
void linkLast(E e) {
        final Node<E> l = last;
        final Node<E> newNode = new Node<>(l, e, null);
        last = newNode;
        if (l == null)
            first = newNode;
        else
            l.next = newNode;
        size++;
        modCount++;
    }
这里将我们新创建的节点的地址赋值给我们的last
    然后会做一个判断，判断是否我们的节点的Last 是不是null.若果是则first 为新节点的地址
    
首先第一步：传入的数据的Last肯定是null,这个是空的时候，将新节点传入last,并将头指针指向新节点。其实此时创建的一个节点的头尾指针都为空
接下来的第二部再执行的时候，传入的这个创建一个新的节点，该节点接收到了之前创建的last的地址，二者相连接，再将我们的last指向我们的现在的新节点，并将这个新节点的地址传给前一个节点的地址，这就实现了后面的链接前面的
    
    如果不是null,则将last的地址赋值给我们的新节点，则二者实现链接，接下来将创建的新节点的地址赋值给last
    接下来就会判断我们的L是不是空，但是实际上的L此时已经有了地址，那么这时候就会执行else。将第一个新的节点的地址赋值给L.next(),这就是实现了前后的链接
```

###### 迭代器的底层原理：

```java
Iterator<student> it=stu.iterator();
while (it.hasNext()){
            String str= it.next().getName();
            if("zhangsan".equals(str)){
                stu.remove(new student("zhangsan",18,"1234",187));
                System.out.println("已经删除");
            }
        }
        System.out.println(stu);
    }

```

底层代码：

```java
   public Iterator<E> iterator() {
        return new Itr();
    }
多次调用这个的方法时候
其实就是创建了多个这个迭代器的对象
    
    
private class Itr implements Iterator<E> {
        int cursor;       // 指向零索引游标，迭代器中的指针
        int lastRet = -1; // 刚刚操作的索引的位置 
        int expectedModCount = modCount;//集合变化的次数

        // prevent creating a synthetic constructor
        Itr() {}//空参构造

        public boolean hasNext() {
            return cursor != size;
        } //判断光标的位置是否超过集集合的最大的size不相等，则返回true,否则返回一个false

        @SuppressWarnings("unchecked")
        public E next() {
            checkForComodification();//判断当前的集合中最新的变化次数和一开始记录的是否相同，如果相同则表示数据没有发生变化，如果数据不相同的时候，就是数据使用了集合中的方法添加或者删除元素了
            int i = cursor;//记录当前的指针的指向的位置
            if (i >= size)//超过界限的时候报错，没有这个元素异常
                throw new NoSuchElementException();
            Object[] elementData = ArrayList.this.elementData;//获取到底部的集合数组
            if (i >= elementData.length)
                throw new ConcurrentModificationException();
            cursor = i + 1;//赋值给游标位置+1
            return (E) elementData[lastRet = i];//返回游标的位置的数据，数组通过这个的索引来迭代提取。
        }

    
     public void remove() {
            if (lastRet < 0)
                throw new IllegalStateException();
            checkForComodification();

            try {
                ArrayList.this.remove(lastRet);
                cursor = lastRet;
                lastRet = -1;
                expectedModCount = modCount;
            } catch (IndexOutOfBoundsException ex) {
                throw new ConcurrentModificationException();
            }
        }
    
结论：避免出现并发修改的异常，在使用迭代器和增强for的循环的时候不要使用集合的方法去修改集合中的元素
     
```



##### list所特有的方法：增加了和索引相关的方法

```
 void add(String item, int index) 
          向滚动列表中索引指示的位置添加指定的项。 
 E  remove(int index)   删除指定的索引处 的元素，返回被删除的元素
 E  set(int index,E element)   设置指定的索引处的元素，返回被修改的元素
 E  get(int index)   获取指定的索引处 的元素，返回指定索引处得到的元素
   
```

```java
通过索引的删除的操作
package com.itheima.test11;

import java.util.ArrayList;
import java.util.List;

public class Listdemo1 {
    public static void main(String[] args) {

        List<Integer> Li=new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            Li.add(i,i);
        };
        System.out.println(Li);
        System.out.println(Li.remove(1));
        //自动装箱
        Integer i=2;
        //手动装箱
        Integer I1=Integer.valueOf(3);
        //通过索引和元素删除
        Li.remove(i);
        Li.remove(I1);
        System.out.println(Li);
        Li.add(1,1);
        System.out.println(Li);
        System.out.println(Li.get(1));
        Li.set(0,10);
        System.out.println(Li);
    }
}

输出：
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
1
[0, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
1
```

##### List集合的遍历的方式：

```java
package com.itheima.test11;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.function.Consumer;

public class Listdemo1 {
    public static void main(String[] args) {

        List<Integer> Li=new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            Li.add(i,i);
        };
        Iterator it=Li.iterator();
        while (it.hasNext()){
            System.out.println(it.next());
        }
        System.out.println("-------------------------");
        Li.forEach(new Consumer<Integer>() {
            @Override
            public void accept(Integer integer) {
                System.out.println(integer);
            }
        });
        System.out.println("_________________________");
        Li.forEach((integer)-> System.out.println(integer));
        System.out.println("______________________________");
        for (int i = 0; i < Li.size(); i++) {
            System.out.println(Li.get(i));
        }
        //列表迭代器
        System.out.println("---------------列表迭代器----------------");
        ListIterator si=Li.listIterator();
        while (si.hasNext()){
            Object x=si.next();
            System.out.println(x);
            Integer z=5;
            if (x.equals(z)){
                Integer xs=19;
                si.set(xs);
            }
            System.out.println("返回的索引——————————————————————");
            System.out.println(si.nextIndex());
        }
        System.out.println(Li);
        System.out.println("--------------倒着迭代的----------------");
        while (si.hasPrevious()){
            System.out.println(si.previous());
            System.out.println("返回的索引——————————————————————");
            System.out.println(si.previousIndex());
        }

    }
}
```

##### Set系列：无序不重复无索引

```JAVA
public class demo1 {
    public static void main(String[] args) {

//        创建一个set 的集合
        HashSet<String> sh=new HashSet<>();
        sh.add("gello");
        sh.add("what");
        sh.add("kello");
        System.out.println(sh);
//        不能出现重复的数据，出现重复的数据的时候就无法存入
        System.out.println(sh.add("gello"));
        //增强for循环
        for (String s : sh) {
            System.out.println(s);
        }
        System.out.println("________________");
        //迭代器
        Iterator i=sh.iterator();
        while (i.hasNext()) {
            System.out.println(i.next());
        }
        System.out.println("_________________");
        //匿名内部类
        sh.forEach(new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println(s);
            }

        });
        System.out.println("__________________");
        //lamada的方法实现
        sh.forEach((s)-> {
                System.out.println(s);
            }
        );
    }
}

```



###### Hsahset:

底层为哈希表，属于set的系列的一员

###### Hsahset->LinkedhashSet:

链表 属于哈希set 系列

###### Treeset:

底层为树结构，属于set 的一员

#### 泛型的深入：

泛型只能支持引用的数据类型，可以再编译的阶段约束操作的数据类型，并进行检查的。

泛型的格式：<数据类型>

泛型用来约束数据的类型

看门的

```java
注意：Java中的泛型是伪泛型的，其实就是检查一下数据

但是再获取数据的时候就会多做一步，将object 转为对应的泛型的约束的类型

在编译的时候会报错，但是生成的class的中没有泛型

泛型的出现就是为了统一集合中的元素，避免一些问题

确认泛型的输入的时候我们就可以传入该类型及其子类类型
```

```java
public class Genericsdemo1 {
    public static void main(String[] args) {
        ArrayList ls=new ArrayList<>();
        ls.add(123);
        ls.add("123");
        ls.add(new student("zhangsan",12,"123",176));
        System.out.println(ls);
        Iterator iterator = ls.iterator();
  
        //如果我们默认的数据没有给集合一个给定的数据的类型的话，就将会导致再获取数据的时候得到的就都是object的类型
        //无法获取到他的特有的方法；
        //因此Java提出了泛型，便于后面的操作
        while(iterator.hasNext()){
            Object obj=iterator.next();
            //多态的弊端是不能访问子类的特有的功能
            //因此无法调用我们子类的功能
            System.out.println(obj);
        }

    }
}
```

泛型可以在很多的地方定义：

```java
泛型类：当我们的某一类中的变量的数据类型不确定的时候我们就可以自定义带有泛型的类。
格式：
    修饰符 class 类名<E>{
        
    }
举例子：
    public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable{
        
    }
```

列子：自己定义的泛型的类

```java
package com.itheima.test11;
import java.util.Arrays;
import java.util.Objects;
/*
自定义的泛型类
 */
public class myarraylist<E>{
    Object[] obj=new Object[10];
    int size;
    public boolean add(E e){
    obj[size]=e;
    size++;
    return true;
    }
    public E get(int index){
        return (E) obj[index];
    }

    @Override
    public String toString() {
        return Arrays.toString(obj);
    }
```

```java
泛型的方法：
当我们的方法中的形参的类型不确定的时候我们选择使用俩种方法
1，使用类名后面的定义的泛型
2，或者在方法的申明上定义自己的泛型

格式：
修饰符 <类型> 返回类型 函数名字(类型名 变量名){

}

public class myarraylist{
    Object[] obj=new Object[10];
    int size;
    public <E> boolean add(E e){
    obj[size]=e;
    size++;
    return true;
    }
举例子：泛型的方法其实是在定义的类中我们只有在一个方法中存在类型不确定的问题，那么就可以采用泛型方法来实现，不需要将该类别整成一个泛型的类
比如下面的代码所示：
public class listutil {
    private listutil(){

    }
    /*
    参数一就是集合
    参数二就是我们需要添加的元素

     */

    public static<E> void addAll(ArrayList<E> list,E e1,E e2,E e3,E e4){
        list.add(e1);
        list.add(e2);
        list.add(e3);
        list.add(e4);
    }

}
    
不定长的传入：
   public static<E> void addAll2(ArrayList<E> list,E...e){
        for (E e1 : e) {
            list.add(e1);
        }
    }

```

泛型接口：

```java
修饰符 interface 接口名<类型>{

}
举例：
 public interface list<E>{
    
} 
关键我们怎么使用泛型的接口
    方法一：实现类黑出具体的类型
    public class myarraylist2 implements List<String>{}

    方法二：实现类延续泛型，创建对象的时候再去确定
    
```

泛型的继承和通配符

```java
 泛型不具备继承性，但是数据具有继承性；
     泛型中写的什么类型，那么就只能传递什么类型的shuju
     弊端：
     利用泛型方法有一个小的弊端，此时他可以接受任意的数据类型，它可以接受所有的任意类型的数据
     有的时候我们希望本方法可以传递我们的ye fu zi 的三个类型
     此时我们就可以使用泛型的通配符
     ？表示不确定的类型
     它可以进行一些类型的限定
     ？ extends E:表示可以传递E或者E的一些子类的类型
     ？ super E:表示传递E或者E的所有的父类的类型
         
```

利用泛型的通配符的使用：

使用的场景：我们不知道类型但是我们知道其可以继承哪一个类的继承体系中的。

```java
public class mian_test {
    public static void main(String[] args) {
  
            ArrayList<ye> list1=new ArrayList<>();
            ArrayList<fu> list2=new ArrayList<>();
            ArrayList<zi> list3=new ArrayList<>();
            ArrayList<students2> list4=new ArrayList<>();
            methhod(list1);
            methhod(list2);
            methhod(list3);
            methhod(list4);        
    }
    public static void methhod(ArrayList<?extends ye> list){
        
    }

}
class  ye{}
class  fu extends ye{}
class  zi extends fu{}
class  students2{}
```

```java
public class mian_test {

    public static void main(String[] args) {

            ArrayList<ye> list1=new ArrayList<>();
            ArrayList<fu> list2=new ArrayList<>();
            ArrayList<zi> list3=new ArrayList<>();
            ArrayList<students2> list4=new ArrayList<>();
            methhod(list1);
            methhod(list2);
            methhod(list3);
            methhod(list4);
    }
    public static void methhod(ArrayList<?super zi> list){

    }

}
class  ye{}
class  fu extends ye{}
class  zi extends fu{}
class  students2{}

```

泛型的练习：

```java
package com.itheima.test12;

import java.util.ArrayList;

public class test {
    public static void main(String[] args) {
     ArrayList<cat> ani=new ArrayList<>();
     taididog taidi=new taididog("xiaosan",2);
     hashiqidog hashiqi=new hashiqidog("xiaoha",3);
     bosicat bosi=new bosicat("bosi",1);
     lihuacat lihua=new lihuacat("lihua",3);
//     ani.add(taidi);
     ani.add(bosi);
//     ani.add(hashiqi);
     ani.add(lihua);
     keepPet1(ani);

    }
    public static void keepPet(ArrayList<?extends animal> list){
        for (animal animal : list) {
            animal.eat();
        }
    }
    public static void keepPet1(ArrayList<?extends cat> list){
        for (cat animal : list) {
            animal.eat();
        }
    }

}
```

#### Map：多列的集合

```java
双列集合一次需要存储一对数据，分别为键和值

键是不能重复的，数值是可以重复的

键和值是一一对应的，每一个键只能找到自己对应的数值

键加值的这个整体我们称之为”键值对“或者键值对对象，Java中叫做Entry 对象
```

##### MAP中常见的API

```java
public interface Map<K,V>将键映射到值的对象。一个映射不能包含重复的键；每个键最多只能映射到一个值。 
```

```java
 void clear() 
          从此映射中移除所有映射关系（可选操作）。 
 boolean containsKey(Object key) 
          如果此映射包含指定键的映射关系，则返回 true。 
 boolean containsValue(Object value) 
          如果此映射将一个或多个键映射到指定值，则返回 true。 
 Set<Map.Entry<K,V>> entrySet() 
          返回此映射中包含的映射关系的 Set 视图。 
 boolean equals(Object o) 
          比较指定的对象与此映射是否相等。 
 V get(Object key) 
          返回指定键所映射的值；如果此映射不包含该键的映射关系，则返回 null。 
 int hashCode() 
          返回此映射的哈希码值。 
 boolean isEmpty() 
          如果此映射未包含键-值映射关系，则返回 true。 
 Set<K> keySet() 
          返回此映射中包含的键的 Set 视图。 
 V put(K key, V value) 
          将指定的值与此映射中的指定键关联（可选操作）。 
 void putAll(Map<? extends K,? extends V> m) 
          从指定映射中将所有映射关系复制到此映射中（可选操作）。 
 V remove(Object key) 
          如果存在一个键的映射关系，则将其从此映射中移除（可选操作）。 
 int size() 
          返回此映射中的键-值映射关系数。 
 Collection<V> values() 
          返回此映射中包含的值的 Collection 视图。 
```

示例：

```java
 V put(K key, V value) 
          将指定的值与此映射中的指定键关联（可选操作）。 
    键值不存在为添加的操作： 添加数据的时候，如果键值不存在的时候，直接添加键值对对象到map的集合当中，此时的方法返回的为null
    键值存在的时候为覆盖的操作： 添加数据的时候，如果键值存在的时候，会把原来的键值的对象覆盖并返回被覆盖的对象
```

```java
public class demo2 {
    public static void main(String[] args) {

        Map<String, String> map = new HashMap<>();
//        添加元素
        map.put("郭靖","黄蓉");
        map.put("韦小宝","木健斌");
        map.put("应制品","小农女");
        System.out.println(map);
        String value=map.put("韦小宝","霜儿");
        System.out.println(value);
        System.out.println(map);
    }
}
{韦小宝=木健斌, 应制品=小农女, 郭靖=黄蓉}
木健斌
{韦小宝=霜儿, 应制品=小农女, 郭靖=黄蓉}
```

```java
 V remove(Object key) 
          如果存在一个键的映射关系，则将其从此映射中移除（可选操作）。
```

```java
        map.remove("韦小宝");
        System.out.println(map);
        输出：
{韦小宝=霜儿, 应制品=小农女, 郭靖=黄蓉}
{应制品=小农女, 郭靖=黄蓉}
```

```java
map.clear();
System.out.println(map);
直接清空的操作
```

```java
        System.out.println(map.containsKey("韦小宝"));
        System.out.println(map.containsValue("小农女"));
        System.out.println(map.isEmpty());
        System.out.println(map.size());
        System.out.println(map.values());
输出：
true
true
false
3
[霜儿, 小农女, 黄蓉]
```

##### map 的集合的遍历的方法：

###### map 的第一种遍历方法：（键找值）

```java
public class demo2 {
    public static void main(String[] args) {

        Map<String, String> map = new HashMap<>();
//        添加元素
        map.put("郭靖", "黄蓉");
        map.put("韦小宝", "木健斌");
        map.put("应制品", "小农女");
        Set<String> strings = map.keySet();
        for (String s : strings) {
            System.out.println(map.get(s));
        }
        strings.forEach((String s)-> {
            System.out.println(map.get(s));
            }
        );
        Iterator<String> iterator = strings.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

    }
}
```

###### map 的第二种遍历方法：（键值对）

```java
public class demo2 {
    public static void main(String[] args) {

        Map<String, String> map = new HashMap<>();
//        添加元素,创建的map的对象
        map.put("郭靖", "黄蓉");
        map.put("韦小宝", "木健斌");
        map.put("应制品", "小农女");
//        map的第二种的遍历的方法
        Set<Map.Entry<String, String>> entries = map.entrySet();
        for (Map.Entry<String, String> entry : entries) {
            String key = entry.getKey();
            String value = entry.getValue();
            System.out.println("键" + key + "值" + value);
        }

        entries.forEach(new Consumer<Map.Entry<String, String>>() {
            @Override
            public void accept(Map.Entry<String, String> stringStringEntry) {
                String key =stringStringEntry.getKey();
                String value = stringStringEntry.getValue();
                System.out.println("键" + key + "值" + value);
            }
        });

        entries.forEach((Map.Entry<String, String> stringStringEntry)-> {
                String key =stringStringEntry.getKey();
                String value = stringStringEntry.getValue();
                System.out.println("键" + key + "值" + value);
            }
        );
        Iterator<Map.Entry<String, String>> iterator = entries.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        
    }
}
```

map 的第三种遍历方法：利用lamada的表达式实现这个

```java
public class demo2 {
    public static void main(String[] args) {

        Map<String, String> map = new HashMap<>();
//        添加元素,创建的map的对象
        map.put("郭靖", "黄蓉");
        map.put("韦小宝", "木健斌");
        map.put("应制品", "小农女");
//        map的第三种的遍历的方法
        map.forEach(new BiConsumer<String, String>() {
            @Override
            public void accept(String key, String Value) {
                System.out.println(key+"="+ Value);
            }
        });
        map.forEach(( key,Value )->
                System.out.println(key+"="+ Value)
        );
    }
}

```

###### foreach 的底层：

```
    default void forEach(BiConsumer<? super K, ? super V> action) {
        Objects.requireNonNull(action);
        for (Map.Entry<K, V> entry : entrySet()) {
            K k;
            V v;
            try {
                k = entry.getKey();
                v = entry.getValue();
            } catch (IllegalStateException ise) {
                // this usually means the entry is no longer in the map.
                throw new ConcurrentModificationException(ise);
            }
            action.accept(k, v);
        }
    }方法的底层还是调用我们的这个Entry,申城我们的entrySet,完成数据的遍历即可
    
```

###### Hashmap的学习

属于我们的maP 中的一个实现类

没有额外的实现的学习的方法。直接使用map中得方法即可

Hash 和Hashset的底层原理都是一样的

都是哈希表的结构

```java
public class demo3 {
    public static void main(String[] args) {

        HashMap<student, String> map = new HashMap<>();
//        创建三个学生对象
        student st1 = new student("zhangsan", 12);
        student st2 = new student("zhangsan1", 13);
        student st3 = new student("zhangsan2", 14);
        map.put(st1, "甘肃");
        map.put(st2, "兰州");
        map.put(st3, "湖南");
        map.forEach(new BiConsumer<student, String>() {
            @Override
            public void accept(student student, String s) {
                System.out.println(student + s);
            }
        });
    }
    }

```

```java
public class demo3 {
    public static void main(String[] args) {

        HashMap<student, String> map = new HashMap<>();
//        创建三个学生对象
        student st1 = new student("zhangsan", 12);
        student st2 = new student("zhangsan1", 13);
        student st3 = new student("zhangsan2", 14);
        student st4 = new student("zhangsan", 12);
        map.put(st1, "甘肃");
        map.put(st2, "兰州");
        map.put(st3, "湖南");
        System.out.println(map.put(st4, "长沙"));
        map.forEach(new BiConsumer<student, String>() {
            @Override
            public void accept(student student, String s) {
                System.out.println(student + s);
            }
        });
    }
    }
我们发现其会对比是否是相同的键值，同姓名同年宁的时候就会出现一个覆盖的操作
```

```
public class demo3 {
    public static void main(String[] args) {

        HashMap<student, String> map = new HashMap<>();
//        创建三个学生对象
        student st1 = new student("zhangsan", 12);
        student st2 = new student("zhangsan1", 13);
        student st3 = new student("zhangsan2", 14);
        student st4 = new student("zhangsan", 12);
        map.put(st1, "甘肃");
        map.put(st2, "兰州");
        map.put(st3, "湖南");
        System.out.println(map.put(st4, "长沙"));
        map.forEach(new BiConsumer<student, String>() {
            @Override
            public void accept(student student, String s) {
                System.out.println(student + s);
            }
        });
        Set<student> students = map.keySet();
        for (student student : students) {
            System.out.println(map.get(student));
        }
        Set<Map.Entry<student, String>> entries = map.entrySet();
        for (Map.Entry<student, String> entry : entries) {
            System.out.println( entry.getKey()+ entry.getValue());
        }
    }
    }
hashset 的遍历，以及其对比键值是否相等的时候，我们需要重写我们的equal和hashcode的方法，完成对应的操作。

```

小练习：经典的投票的问题，我们可以使用map来完成

```java
package com.itheima.test13;

import com.itheima.test4.Animal;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;
import java.util.function.BiConsumer;

public class demo4 {
    public static void main(String[] args) {

        HashMap<String,Integer> map=new HashMap<String, Integer>();
        String[] arr={"A","B","C","D"};
        //随机数来模拟八十位学生的投票的行为
        ArrayList<String> list=new ArrayList<>();
        Random rando=new Random();
        for (int i = 0; i < 80; i++) {
            int nextInt = rando.nextInt(arr.length);
            String s = arr[nextInt];
            list.add(s);
        }
//        表示八十个的同学已经完成了投票的行为
        for (String s : list) {
//            判断当前的经景点的名称再我们的MAp中是否是存在的
            if(map.containsKey(s)){
                Integer integer = map.get(s);
                Integer integer1=integer+1;
                map.put(s,integer1);
            }else {
                map.put(s,1);
            }
        }
        map.forEach(new BiConsumer<String, Integer>() {
            @Override
            public void accept(String s, Integer integer) {
                System.out.println("景点的名字为"+s+"景点的投票人数："+integer);
            }
        });
    }
}
运行的结果：
景点的名字为A景点的投票人数：24
景点的名字为B景点的投票人数：18
景点的名字为C景点的投票人数：19
景点的名字为D景点的投票人数：19   
```

```java
public class demo4 {
    public static void main(String[] args) {

        HashMap<String,Integer> map=new HashMap<String, Integer>();
        String[] arr={"A","B","C","D"};
        //随机数来模拟八十位学生的投票的行为
        ArrayList<String> list=new ArrayList<>();
        Random rando=new Random();
        for (int i = 0; i < 80; i++) {
            int nextInt = rando.nextInt(arr.length);
            String s = arr[nextInt];
            list.add(s);
        }
//        表示八十个的同学已经完成了投票的行为
        for (String s : list) {
//            判断当前的经景点的名称再我们的MAp中是否是存在的
            if(map.containsKey(s)){
                Integer integer = map.get(s);
                Integer integer1=integer+1;
                map.put(s,integer1);
            }else {
                map.put(s,1);
            }
        }
        map.forEach(new BiConsumer<String, Integer>() {
            @Override
            public void accept(String s, Integer integer) {
                System.out.println("景点的名字为"+s+"景点的投票人数："+integer);
            }
        });


//        求一个最大的数值
        Integer max=0;
        String index=new String();
        for (String s : map.keySet()) {
           if (map.get(s)>max)
           {
               max= map.get(s);
               index=s;}
        }
        System.out.println(index+max);
    }
}
得出最多的景点 的投票的人数’
景点的名字为A景点的投票人数：18
景点的名字为B景点的投票人数：29
景点的名字为C景点的投票人数：13
景点的名字为D景点的投票人数：20
B29  
```

###### Linkedhashmap

```java
都有键值所决定的：有序 不重复 无索引
底层的原理的数据结构是哈希表，只是每一个键值对元素有额外多了一个双链表的机制记录存储的顺序的位置
```

```java
public class DEMO5 {

    public static void main(String[] args) {
        LinkedHashMap<String,Integer> map=new LinkedHashMap<>();
        map.put("A",1);
        map.put("b",2);
        map.put("c",3);
        map.put("A",4);
        System.out.println(map);
    }
}
```

###### Treemap

不重复 五索引 可排序

可排序：对键进行排序，

注意可以按照键值的从小到大的顺序完成排序也可以按照自己的规则完成排序

```java
代码书写的排序规则

实现comparable的接口，指定比较的规则
compareTo int compareTo(T o)比较此对象与指定对象的顺序。如果该对象小于、等于或大于指定对象，则分别返回负整数、零或正整数。 

    
创建集合的时候传递comparator比较器的对象。指定比较规则
 public class demo6 {
    public static void main(String[] args) {
        TreeMap<Integer,String> map=new TreeMap<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        });
        map.put(1,"奶茶");
        map.put(2,"果汁");
        map.put(3,"面包");
        map.put(8,"COCO");
        map.put(4,"MILK");
        map.put(5,"COLO");
        System.out.println(map);

    }
}
```

注意我们在定义Treemap的集合的时候，需要在对象中重写我们排序的规则，否则其会报错，以下是俩种我们使用的方法：

使用对象实现comparable的接口完成。 

```java
package com.itheima.test13;

import java.util.Objects;

public  class student implements Comparable<student>{
    private String name;
    private int age;

    public student() {
    }

    public student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    /**
     * 获取
     * @return name
     */
    public String getName() {
        return name;
    }

    /**
     * 设置
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * 获取
     * @return age
     */
    public int getAge() {
        return age;
    }

    /**
     * 设置
     * @param age
     */
    public void setAge(int age) {
        this.age = age;
    }

    public String toString() {
        return "student{name = " + name + ", age = " + age + "}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        student student = (student) o;
        return age == student.age && Objects.equals(name, student.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }

    @Override
    public int compareTo(student o) {
        int i = o.getAge() - this.getAge();
        i = i==0 ? o.getName().compareTo(this.getName()):i;
        return i;
    }
}
```

使用传入 Comparator对象实现

```java
public class demo8 {
    public static void main(String[] args) {
        TreeMap<student2,String> map=new TreeMap<>(new Comparator<student2>() {
            @Override
            public int compare(student2 o1, student2 o2) {
                int i = o1.getAge() - o2.getAge();
                i = i==0 ? o1.getName().compareTo(o2.getName()):i;
                return i;
            }
        });
        student2 stu1=new student2("zhangsan",12);
        student2 stu2=new student2("zhangsan1",13);
        student2 stu3=new student2("zhangsan2",14);
        student2 stu4=new student2("zhangsan3",15);
        map.put(stu4,"湖南");
        map.put(stu1, "甘肃");
        map.put(stu2, "兰州");
        map.put(stu3, "湖南");
        System.out.println(map);
        
    }
}
```

小练习：统计字符串中的字符的个数

升序输出：

```java
public class demo9 {
    public static void main(String[] args) {
        String str="aababcabcdabvde";
        ArrayList<String> list=new ArrayList<>();
        for (int i = 0; i < str.length(); i++) {
            String s= String.valueOf(str.charAt(i));
            System.out.println(s);
            list.add(s);
        }

        TreeMap<String,Integer> map=new TreeMap<>();
        for (String s : list) {
            if (map.containsKey(s)){
                Integer integer = map.get(s);
                integer=integer+1;
                map.put(s,integer);
            }
            else
                map.put(s,1);
        }
        System.out.println(map);
    }
}

```

降序输出：

```java
public class demo9 {
    public static void main(String[] args) {
        String str="aababcabcdabvde";
        ArrayList<String> list=new ArrayList<>();
        for (int i = 0; i < str.length(); i++) {
            String s= String.valueOf(str.charAt(i));
            System.out.println(s);
            list.add(s);
        }

        TreeMap<String,Integer> map=new TreeMap<>(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2);
            }
        });
        for (String s : list) {
            if (map.containsKey(s)){
                Integer integer = map.get(s);
                integer=integer+1;
                map.put(s,integer);
            }
            else
                map.put(s,1);
        }
        System.out.println(map);
    }
}

```

###### HASHMAP的底层源码

<img src="/C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20230713161909398.png" alt="image-20230713161909398" style="zoom:50%;" />

哈希属性

![image-20230713162033204](/C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20230713162033204.png)

hashmap的内部类

![image-20230713162055858](/C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20230713162055858.png)

hashmap 的内部存储的node

```java
1.1 链表中的键值对对象
    包含：  
			int hash;         //键的哈希值
            final K key;      //键
            V value;          //值
            Node<K,V> next;   //下一个节点的地址值
			
			
1.2 红黑树中的键值对对象
	包含：
			int hash;         		//键的哈希值
            final K key;      		//键
            V value;         	 	//值
            TreeNode<K,V> parent;  	//父节点的地址值
			TreeNode<K,V> left;		//左子节点的地址值
			TreeNode<K,V> right;	//右子节点的地址值
			boolean red;			//节点的颜色
		
     
```

存放的位置：

```java
  transient Node<K,V>[] table;
  其实我们的hashmap的每一个node节点存放的位置；
```

默认的我们的容量：14

```java
  static final int DEFAULT_INITIAL_CAPACITY = 1 << 4; // aka 16
```

扩容的容量：

```java
 static final float DEFAULT_LOAD_FACTOR = 0.75f;
```

最大的容量：

```java
static final int MAXIMUM_CAPACITY = 1 << 30;
```

构造的方法：

空参构造的时候不创建我们的table

```java
2.添加元素
HashMap<String,Integer> hm = new HashMap<>();
//此时的数组table为null
hm.put("aaa" , 111);
hm.put("bbb" , 222);
hm.put("ccc" , 333);
hm.put("ddd" , 444);
hm.put("eee" , 555);
添加元素的时候至少考虑三种情况：
2.1数组位置为null
2.2数组位置不为null，键不重复，挂在下面形成链表或者红黑树
2.3数组位置不为null，键重复，元素覆盖

```

他其实是在我们的put的操作的时候完成的创建的对应的table

```java
public V put(K key, V value) {
        return putVal(hash(key), key, value, false, true);
    }
俩个参数
    参数一就是我们的键
    参数二就是我们的值
    返回值：俩种类型
    第一种：键值没有重复，返回null
    第二种：键值重复的时候。返回的是被覆盖的数值
    
putVal(hash(key), key, value, false, true)解读
    其实就是利用我们的键值计算出对应的哈希的数，载把我们的哈希做一些额外的处理，使得我们得到的hashcode 更加的随机
    
```

```java
//参数一：键的哈希值
//参数二：键
//参数三：值
//参数四：如果键重复了是否保留
//		   true，表示老元素的值保留，不会覆盖
//		   false，表示老元素的值不保留，会进行覆盖
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,boolean evict) {
	    //定义一个局部变量，用来记录哈希表中数组的地址值。采用局部变量可以使得其效率提高不用每次都去堆里面查找我们的数据
        Node<K,V>[] tab;	
		//临时的第三方变量，用来记录键值对对象的地址值
        Node<K,V> p;   
		//表示当前数组的长度
		int n;		
		//表示索引
         int i;		
		//把哈希表中数组的地址值，赋值给局部变量tab
		tab = table;
        if (tab == null || (n = tab.length) == 0){
//1.如果当前是第一次添加数据，底层会创建一个默认长度为16，加载因子为0.75的数组
//2.如果不是第一次添加数据，会看数组中的元素是否达到了扩容的条件
			//如果没有达到扩容条件，底层不会做任何操作
			//如果达到了扩容条件，底层会把数组扩容为原先的两倍，并把数据全部转移到新的哈希表中
			tab = resize();//完成数据的扩容
			//表示把当前数组的长度赋值给n
            n = tab.length;
        }

		//拿着数组的长度跟键的哈希值进行计算
       //计算出当前键值对对象，在数组中应存入的位置
		i = (n - 1) & hash;//index计算出存入的索引
		//获取数组中对应元素的数据
		p = tab[i];
		
		
        if (p == null){
			//底层会创建一个键值对对象，直接放到数组当中
  /*Node<K,V> newNode(int hash, K key, V value, Node<K,V> next) {
        return new Node<>(hash, key, value, next);
        直接创建了一个新的键值对的对象，直接放入到我们数组之中。
    }*/
            tab[i] = newNode(hash, key, value, null);
        }else {
            Node<K,V> e;
            K k;
			
			//等号的左边：数组中键值对的哈希值
			//等号的右边：当前要添加键值对的哈希值
			//如果键不一样，此时返回false
			//如果键一样，返回true
			boolean b1 = p.hash == hash;
			
            if (b1 && ((k = p.key) == key || (key != null && key.equals(k)))){
                e = p;
            } else if (p instanceof TreeNode){
				//判断数组中获取出来的键值对是不是红黑树中的节点
				//如果是，则调用方法putTreeVal，把当前的节点按照红黑树的规则添加到树当中。
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            } else {
				//如果从数组中获取出来的键值对不是红黑树中的节点
				//表示此时下面挂的是链表
                for (int binCount = 0; ; ++binCount) {
                    if ((e = p.next) == null) {
						//此时就会创建一个新的节点，挂在下面形成链表
                        p.next = newNode(hash, key, value, null);
						//判断当前链表长度是否超过8，如果超过8，就会调用方法treeifyBin
						//treeifyBin方法的底层还会继续判断
						//判断数组的长度是否大于等于64
						//如果同时满足这两个条件，就会把这个链表转成红黑树
                        if (binCount >= TREEIFY_THRESHOLD - 1)
                            treeifyBin(tab, hash);
                        break;
                    }
					//e：		  0x0044   ddd   444
					//要添加的元素： 0x0055   ddd   555
					//如果哈希值一样，就会调用equals方法比较内部的属性值是否相同
                    if (e.hash == hash && ((k = e.key) == key || (key != null && key.equals(k)))){
						 break;
					}

                    p = e;
                }
            }
			
			//如果e为null，表示当前不需要覆盖任何元素
			//如果e不为null，表示当前的键是一样的，值会被覆盖
			//e:0x0044  ddd  555
			//要添加的元素： 0x0055   ddd   555
            if (e != null) {
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null){
					
					//等号的右边：当前要添加的值
					//等号的左边：0x0044的值
					e.value = value;
				}
                afterNodeAccess(e);
                return oldValue;
            }
        }
		
        //threshold：记录的就是数组的长度 * 0.75，哈希表的扩容时机  16 * 0.75 = 12
        if (++size > threshold){
			 resize();
		}
        
		//表示当前没有覆盖任何元素，返回null
        return null;
    }
```

### 创建不可变集合的场景

如果某一个数据不能被修改的时候，把他防御性的拷贝到我们的不可变的集合中

当集合的中的对象被不可信的库调用的时候，不可变的形式的是安全的

#### 创建不可变集合的书写的格式

再list Set Map的接口中，都存在静态的of方法，可以获取到一个不可变的集合

```java
static<E> List<E> of(E....elements)
static<E> Set<E> of(E....elements)
static<K,v> Map<K,v> of(E....elements)
```

该集合不能添加，不能删除。

```java
public class demo1 {
    public static void main(String[] args) {
        List<String> hello = List.of("HELLO", "WORK");
        System.out.println(hello);
        hello.add("ddd");
        System.out.println(hello);
    }
}
创建成功之后就不能再删减增加了，强行的使用就会出现报错
```

## Stream流

```java
public class demo1 {
    public static void main(String[] args) {
      ArrayList<String> list=new ArrayList<>();
      list.add("张无忌");
      list.add("周芷若");
      list.add("赵敏");
      list.add("张强");
      list.add("张三丰");
//      ArrayList<String> list2=new ArrayList<>();
//        for (String s : list) {
//            if (s.startsWith("张")){
//               list2.add(s);
//            }
//        }
//        System.out.println(list2);
//
//        ArrayList<String> list3=new ArrayList<>();
//        for (String s : list2) {
//            if (s.length()==3){
//                list3.add(s);
//            }
//        }
//        System.out.println(list3);
//        for (String s : list3) {
//            System.out.println(s);
//        }
        
   list.stream().filter(name->name.startsWith("张")).filter(name->name.length()==3).forEach(name-> System.out.println(name));

    }
}
初尝试stream 流
    
```

stream 流:

流：流水线

结合lamada的表达式去简化集合和数组的一些的操作。

#### 使用的步骤；

```java
先得到一个stream的数据流水线，并将我们的数据放上去。
利用stream流中的API进行各种的操作
过滤   转换    统计  打印。
```

使用的步骤

```java

先得到一条流水线，并把数据放到上面

使用中间方法对流水线上的数据进行操作

使用终结的方法对流水线上的数据操作
    
    
   创建数据流，将数据放到对应的数据流上
   Stream<String> stream = list.stream();
使用中间的方法处理stream 的流
   Stream<String> stringStream = stream.filter(s -> s.length() >= 3);
使用collect收集数据流
   List<String> collect = stringStream.collect(Collectors.toList());
   System.out.println(collect);
```

###### stream 的流的使用的步骤一：得到一条stream的流水线，并把数据放上去

```
获取的方法          方法名字        说明

单列的集合          stream()         cOLLECTION中的默认的方法
双列的集合           无                无法使用数据流
数组         Public static stream()    Arrays工具类中的静态的方法
一堆零散的数据     Public static Stream<T> of(T..values)  stream接口中的静态的方法

```

单列的集合

```java
public class demo1 {
    public static void main(String[] args) {
      ArrayList<String> list=new ArrayList<>();
      list.add("张无忌");
      list.add("周芷若");
      list.add("赵敏");
      list.add("张强");
      list.add("张三丰");

      list.stream().filter(name->name.startsWith("张")).filter(name->name.length()==3).forEach(name-> System.out.println(name));

    }
}
```

数组：

```java
        Integer[] arr=new Integer[10];
        for (int i = 0; i < arr.length; i++) {
            arr[i]=1;
        }
        Arrays.stream(arr).forEach(s-> System.out.println(s));
    }
}

```

零散的数据：

```java
public class demo3 {
    public static void main(String[] args) {

​        Stream.*of*(1,2,3,4,5,6,7,8).forEach(s-> System.*out*.println(s));
​    }
}
```

需要注意的细节

```java

public class demo3 {
    public static void main(String[] args) {

        int[] arr1={1,2,3,4,5,6,7,8,9};
        String[] arr2={"q","n","c"};
        Stream.of(1,2,3,4,5,6,7,8).forEach(s-> System.out.println(s));
        Stream.of(arr1).forEach(num-> System.out.println(num));
        Stream.of(arr2).forEach(num-> System.out.println(num));
    }
}
方法的形参是一个可变的参数，可以传递一堆零散的数据，也可以传递数组
但是数组必须是引用数据类型的，如过传递的是基本的数据类型的数据，会把整个的数组当成一个元素，放到stream的流中。
```

###### stream的中间方法：

注意事项：

```java
流只能使用一次特别重要；；；；；
```

中间方法，返回新的stream流，原来的流只使用一次，建议使用链式编程

修改stream流中的数据，不会影响原来集合或者数组中的数据

删选与切片：

```java
        filter：过滤流中的某些元素
        limit(n)：获取n个元素
        skip(n)：跳过n元素，配合limit(n)可实现分页
        distinct：通过流中元素的 hashCode() 和 equals() 去除重复元素
```



```java
Stream<Integer> stream = Stream.of(6, 4, 6, 7, 3, 9, 8, 10, 12, 14, 14);
 
Stream<Integer> newStream = stream.filter(s -> s > 5) //6 6 7 9 8 10 12 14 14
        .distinct() //6 7 9 8 10 12 14
        .skip(2) //9 8 10 12 14
        .limit(2); //9 8
newStream.forEach(System.out::println);
```

映射

```java
   
        map：接收一个函数作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素。
        flatMap：接收一个函数作为参数，将流中的每个值都换成另一个流，然后把所有流连接成一个流。
```



```java
List<String> list = Arrays.asList("a,b,c", "1,2,3");
 
//将每个元素转成一个新的且不带逗号的元素，接受的是一个函数，整个函数是将会作用域我们所有的元素
Stream<String> s1 = list.stream().map(s -> s.replaceAll(",", ""));
s1.forEach(System.out::println); // abc  123
 
Stream<String> s3 = list.stream().flatMap(s -> {
    //将每个元素转换成一个stream
    String[] split = s.split(",");
    Stream<String> s2 = Arrays.stream(split);
    return s2;
});
s3.forEach(System.out::println); // a b c 1 2 3
```



###### stream的终结：

```java
void forEach(Consume action)	对此流的每个元素执行操作
long count()	返回此流中的元素数
toArray()       收集流中的数据，放到数组中
```

###### Stream流的收集操作

```java
public static Collector toList()	把元素收集到List集合中
public static Collector toSet()	把元素收集到Set集合中
public static Collector toMap(Function keyMapper,Function valueMapper)	把元素收集到Map集合中

```



for example 

```java
public class demo5 {
    public static void main(String[] args) {

                //创建List集合对象

                List<String> list = new ArrayList<String>();

                list.add("孙悟空");
                list.add("孙行者");
                list.add("王宝强");
                list.add("柳神");
                //需求1：得到名字为3个字的流
                Stream<String> listStream = list.stream().filter(s -> s.length() == 3);
                //需求2：把使用Stream流操作完毕的数据收集到List集合中并遍历
                List<String> names = listStream.collect(Collectors.toList());
                for(String name : names) {
                    System.out.println(name);
                }
                //创建Set集合对象
                Set<Integer> set = new HashSet<Integer>();
                set.add(10);
                set.add(20);
                set.add(30);
                set.add(33);
                set.add(35);

                //需求3：得到年龄大于25的流
                Stream<Integer> setStream = set.stream().filter(age -> age > 25);

                //需求4：把使用Stream流操作完毕的数据收集到Set集合中并遍历
                Set<Integer> ages = setStream.collect(Collectors.toSet());
                for(Integer age : ages) {
                    System.out.println(age);
                }

                //定义一个字符串数组，每一个字符串数据由姓名数据和年龄数据组合而成
                String[] strArray = {"孙悟空,560", "孙行者,555", "王宝强,33", "柳神,22"};

                //需求5：得到字符串中年龄数据大于28的流
                Stream<String> arrayStream = Stream.of(strArray).filter(s -> Integer.parseInt(s.split(",")[1]) > 28);

                //需求6：把使用Stream流操作完毕的数据收集到Map集合中并遍历，字符串中的姓名作键，年龄作值
          Map<String, Integer> map = arrayStream.collect(Collectors.toMap(s -> s.split(",")[0], s -> Integer.parseInt(s.split(",")[1])));

                Set<String> keySet = map.keySet();
                for (String key : keySet) {
                    Integer value = map.get(key);
                    System.out.println(key + "," + value);
                }
            }
        }
```

收集 的方法：

```java
public class demo6 {
    public static void main(String[] args) {
        ArrayList<String> list=new ArrayList<>();
        Collections.addAll(list,"张无忌-男-15","周芷若-女-24","赵敏-女-12","张强-男-20","张三丰-男-100","张翠山-男-40","张良-男-35","王二麻子-男-37","谢广坤-男-61");
        System.out.println(list.toString());
        System.out.println(list.stream().filter(s -> s.split("-")[1].equals("男")).filter(s -> Integer.parseInt(s.split("-")[2]) >= 18).collect(Collectors.toList()));
        System.out.println(list.stream().filter(s -> s.split("-")[1].equals("男")).filter(s -> Integer.parseInt(s.split("-")[2]) >= 18).collect(Collectors.toSet()));
        Map<String, String> mymap = list.stream().filter(s -> s.split("-")[1].equals("男")).filter(s -> Integer.parseInt(s.split("-")[2]) >= 18).collect(Collectors.toMap(s -> s.split("-")[0], s -> s.split("-")[1]));
        for (Map.Entry<String, String> stringStringEntry : mymap.entrySet()) {
            System.out.println(stringStringEntry.getKey()+"  "+stringStringEntry.getValue());
        }
    }
```

### 方法引用：

#### 方法引用：

用以前学习的方法，拿过来用，当作函数式接口中抽象方法的方法体

```java
public class demo7 {
    public static void main(String[] args) {
        Integer[] myarr=new Integer[10];
        for (int q = 0; q < 10; q++) {
            myarr[q]=q;
        }
        Arrays.sort(myarr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        });
        for (Integer integer : myarr) {
            System.out.println(integer);
        }
    }
}

```

比如这个compare 

```java
  Arrays.sort(myarr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        });
出了使用函数式接口完成，还能够使用方法的引用完成也就是：
    new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        }
这个一部分可以用方法的引用替换完成
    
    public  int subtraction(int n1,int n2){
    return n2-n1;
}

使用的规则：
    首先引用的部分必须树函数式的接口
    其次被引用的方法必须已经存在
    被引用的方法的形参和返回值需要和抽象方法保持一致
```

例如：

首先这个引用的位置是一个函数式的接口

```
    new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        }
```

被引用的方法已经存在

被引用的方法的形参和返回值需要和抽象的方保持一致

```
    public  int subtraction(int n1,int n2){
    return n2-n1;
}
```

举例：

```Java
::    独特的方法引用符
```



```java
package com.itheima.test16;

import java.awt.event.ActionListener;
import java.util.*;
import java.util.stream.Collectors;

public class demo7 {
    public static void main(String[] args) {
        Integer[] myarr=new Integer[10];
        for (int q = 0; q < 10; q++) {
            myarr[q]=q;
        }
//        匿名内部类
        Arrays.sort(myarr, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o2-o1;
            }
        });
        for (Integer integer : myarr) {
            System.out.println(integer);
        }

//        lamada表达式
        Arrays.sort(myarr, (o1,o2)-> o1-o2);
        for (Integer integer : myarr) {
            System.out.println(integer);
        }
//        方法的引用
//        通过类名的引用
//        将该方法作为抽象方法的方法体
        
        Arrays.sort(myarr,demo7::subtraction);
        for (Integer integer : myarr) {
            System.out.println(integer);
        }

    }
    public  static int subtraction(int num1,int num2){
        return num1-num2;
    }
}
```

#### 方法引用分类

##### 引用静态方法

格式：

```java
类名:: 静态方法名
Integer::parseInt
```

举例：

```java
        Arrays.sort(myarr,demo7::subtraction);
        for (Integer integer : myarr) {
            System.out.println(integer);
        }

    }
    public  static int subtraction(int num1,int num2){
        return num1-num2;
    }
}

```

example:

使用匿名内部类完成的操作

```java
public class demo1 {
    public static void main(String[] args) {

        ArrayList<String> list=new ArrayList<>();
        Collections.addAll(list,"1","2","3","4","5","6","7","8");
        list.stream().map(new Function<String, Integer>() {
            @Override
            public Integer apply(String s) {
               int i=Integer.parseInt(s);
               return i;
            }
        }).forEach(s-> System.out.println(s));
    }
}

```

使用lamada完成

```java
public class demo1 {
    public static void main(String[] args) {

        ArrayList<String> list=new ArrayList<>();
        Collections.addAll(list,"1","2","3","4","5","6","7","8");
        list.stream().map(s->Integer.parseInt(s)).forEach(s-> System.out.println(s));
    }
}

```

使用我们的方法引用

```java
public class demo1 {
    public static void main(String[] args) {

        ArrayList<String> list=new ArrayList<>();
        Collections.addAll(list,"1","2","3","4","5","6","7","8");
        list.stream().map(Integer::parseInt).forEach(s-> System.out.println(s));
    }
}

```

##### 引用成员方法

格式：

```java
格式：对象:: 成员方法
```

###### 引用其他类的成员方法

```java
其他类对象名::方法名
```

```java
        ArrayList<String> list=new ArrayList<>();
        Collections.addAll(list,"张三","张无忌","周芷若","赵敏","张强","张三丰");
//        给成方法引用
        list.stream().filter(s->s.startsWith("张")).filter(s->s.length()>=3).forEach(s -> System.out.println(s));
        list.stream().filter(demo1::mytest).forEach(s -> System.out.println(s));
```



###### 引用本类的成员方法

```java
this::方法名
```

```java
public class demo1 {
    public static void main(String[] args) {

        ArrayList<String> list=new ArrayList<>();
        Collections.addAll(list,"张三","张无忌","周芷若","赵敏","张强","张三丰");
//        给成方法引用
list.stream().filter(s->s.startsWith("张")).filter(s->s.length()>=3).forEach(s -> System.out.println(s));

list.stream().filter(new demo1()::mytest).forEach(s -> System.out.println(s));
    }
public    boolean mytest(String s){
        if(s.startsWith("张")&s.length()==3){
            return true;

        }else
            return false;

    }
}

```

###### 

举例子：

```java
        x1.addActionListener(this::actionPerformed1);
        x2.addActionListener(this::actionPerformed2);
        x3.addActionListener(this::actionPerformed3);
        this.getContentPane().add(x1);
        this.getContentPane().add(x2);
        this.getContentPane().add(x3);
//        this.addMouseListener();
        //让界面显示出来，默认页面是不显示的
        this.setVisible(true);

    }

    public void actionPerformed1(ActionEvent e) {
        System.out.println("登陆键被点击了");

    }

    public void actionPerformed2(ActionEvent e) {
        System.out.println("注册键被点击了");

    }

    public void actionPerformed3(ActionEvent e) {
        System.out.println("斗地主被点击了");

    }

}
```

###### 用父类的成员方法

```java
super::方法名
```

```java
        x1.addActionListener(super::actionPerformed1);
        x2.addActionListener(super::actionPerformed2);
        x3.addActionListener(super::actionPerformed3);
        this.getContentPane().add(x1);
        this.getContentPane().add(x2);
        this.getContentPane().add(x3);
```

```java
public class mufram extends JFrame {

    public void actionPerformed1(ActionEvent e) {
        System.out.println("登陆键被点击了");
    }

    public void actionPerformed2(ActionEvent e) {
        System.out.println("注册键被点击了");
    }

    public void actionPerformed3(ActionEvent e) {
        System.out.println("斗地主被点击了");
    }

    public String toString() {
        return "mufram{}";
    }
}

```

##### 引用构造方法：

我们可以将流中的每一个数据去直接引用构造方法实现我们每一个类的带参创建

要求是将我们的带参的构造实现后完成一定的功能即也就是我们需要完成一个具体的实现，比如我们这个构造方法的接受的参数是我们流中的每一个元素，我们将这个元素的数值提取出来赋值给类中的变量，完成对象的创建即可



格式：

```
类名::new
```

范例：

```java
student::new
```

类中重新定义一个构造方法：

```java
    public student(String s) {
        this.name=s.split(",")[0];
        this.age=Integer.parseInt(s.split(",")[1]);
    }

```

引用类中的构造方法：

```java
public class demo3 {
    public static void main(String[] args) {
        ArrayList<String> myarr1 = new ArrayList<>();
        Collections.addAll(myarr1, "张三风,23", "李四能,24", "王开五,25","赵六,32","黄豆,20","刘光,23");
//       把stream流中的的string封装成一个student
//       方法的引用
//        myarr1.stream().map(demo3::apply1).forEach(s-> System.out.println(s));

        myarr1.stream().map(student::new).forEach(s-> System.out.println(s));

    }
    public static student apply1(String s) {
        String name=s.split(",")[0];
        int s2=Integer.parseInt(s.split(",")[1]);
        return new student(name,s2);

    }
}
```

##### 其他的调用的方式：

使用类名引用成员方法：

自己调用自己的无参的；

被引用的方法的形参是跟抽象杨方法中的第二个参数后面的保持一致

局限性：

不能引用所有的类中的 成员方法

是跟抽象方法中的第一个的参数是相关的，有什么的类型，就只能引用这个类中的成员方法

```java
格式：类名::成员方法
```

```java
范例： String:: substring
```

```java
public class demo4 {
    public static void main(String[] args) {
        ArrayList<String> list=new ArrayList<>();
        Collections.addAll(list,"aaa","bbb","ccc","ddd");
//        变成大写后输出
        list.stream().map(new Function<String, String>() {
            @Override
            public String apply(String s) {
                return s.toUpperCase();
            }
        }).forEach(s -> System.out.println(s));
        list.stream().map(String::toUpperCase).forEach(s -> System.out.println(s));
    }
}

```

原始的使用匿名内部类的方法：

```java
public class demo5 {

    public static void main(String[] args) {

        ArrayList<Integer> arr=new ArrayList<>();
        Collections.addAll(arr,1,2,3,4,5,6,7,8,9,10);
//        储存一些整数，收集到数组当中
        Integer[] array = arr.stream().toArray(new IntFunction<Integer[]>() {
            @Override
            public Integer[] apply(int value) {
                return new Integer[value];
            }
        });
        System.out.println(Arrays.toString(array));
    }
}
```

使用我们引用数组的构造方法：

需要的注意点在于：

我们需要了解整个数组的的类型需要和我们的arraylist的集合中的元素的类型保持一致

```java
public class demo5 {
    public static void main(String[] args) {

        ArrayList<Integer> arr=new ArrayList<>();
        Collections.addAll(arr,1,2,3,4,5,6,7,8,9,10);
//        储存一些整数，收集到数组当中
        Integer[] array = arr.stream().toArray(Integer[]::new);
        System.out.println(Arrays.toString(array));
    }
}
```

练习：

```java
public class demo6 {
    public static void main(String[] args) {
        ArrayList<String> myarr1 = new ArrayList<>();
        Collections.addAll(myarr1, "张三风,23", "李四能,24", "王开五,25","赵六,32","黄豆,20","刘光,23");
        myarr1.stream().map(student::new).forEach(s-> System.out.println(s));
        List<student> collect = myarr1.stream().map(student::new).collect(Collectors.toList());
        System.out.println(collect.toString());
//将创建的学生对象的集合中获取名字存放到数组当中
        String[] array = collect.stream().map((student)->student.getName()).toArray(String[]::new);
        System.out.println(Arrays.toString(array));
    }
}

```

collect.stream().map(student::getName)

```java
第一个完成的是利用student方法将其中的Getname拿出来
```

```java
第二个的操作完成的是引用数组的构造方法完成转换
```



```java
public class demo6 {
    public static void main(String[] args) {
        ArrayList<String> myarr1 = new ArrayList<>();
        Collections.addAll(myarr1, "张三风,23", "李四能,24", "王开五,25","赵六,32","黄豆,20","刘光,23");
        myarr1.stream().map(student::new).forEach(s-> System.out.println(s));
        List<student> collect = myarr1.stream().map(student::new).collect(Collectors.toList());
        System.out.println(collect.toString());
        String[] array = collect.stream().map(student::getName).toArray(String[]::new);
        System.out.println(Arrays.toString(array));

    }
}
```

## 异常, File,综合案例：

### **异常** ：

* 指的是程序在执行过程中，出现的非正常的情况，最终会导致JVM的非正常停止。

在Java等面向对象的编程语言中，异常本身是一个类，产生异常就是创建异常对象并抛出了一个异常对象。

Java处理异常的方式是中断处理。

> 异常指的并不是语法错误,语法错了,编译不通过,不会产生字节码文件,根本不能运行.：

### 异常体系

异常机制其实是帮助我们**找到**程序中的问题，异常的根类是`java.lang.Throwable`，其下有两个子类：`java.lang.Error`与`java.lang.Exception`，平常所说的异常指`java.lang.Exception`。

<img src="/C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20230719145837066.png" alt="image-20230719145837066" />

#### **Throwable体系：**

* **Error**:严重错误Error，无法通过处理的错误，只能事先避免，好比绝症。
* **Exception**:表示异常，异常产生后程序员可以通过代码的方式纠正，使程序继续运行，是必须要处理的。好比感冒、阑尾炎。

**Throwable中的常用方法：**

* `public void printStackTrace()`:打印异常的详细信息。

  *包含了异常的类型,异常的原因,还包括异常出现的位置,在开发和调试阶段,都得使用printStackTrace。*

* `public String getMessage()`:获取发生异常的原因。

  *提示给用户的时候,就提示错误原因。*

* `public String toString()`:获取异常的类型和异常描述信息(不用)。

我们平常说的异常就是指Exception，因为这类异常一旦出现，我们就要对代码进行更正，修复程序。

#### **异常(Exception)的分类**:

根据在编译时期还是运行时期去检查异常?

* **编译时期异常**:checked异常。在编译时期,就会检查,如果没有处理异常,则编译失败。(如日期格式化异常)

* 关键在于检查本地的信息

  ![image-20230719150822241](/../assets/image-20230719150822241.png)

  此时会出现的编译时期的异常整个就意味着我们需要处理该异常，否则无法编译

* **运行时期异常**:runtime异常。在运行时期,检查异常.在编译时期,运行异常不会编译器检测(不报错)。(如数学异常)

* 关键在于检查运行的异常

* ![image-20230719151102956](/../assets/image-20230719151102956.png)

此时的异常

![image-20230719151122075](/../assets/image-20230719151122075.png)

```java
ArrayIndexOutOfBoundsException  数组越界异常
```

#### 异常的作用：

作用一：可以用来查询我们的bug的关键参考的信息、

作用二：异常可以作为方法内部的一种特殊的返回值，以便通知调用者底层的执行的情况；

#### 抛出异常throw：

在编写程序时，我们必须要考虑程序出现问题的情况。比如，在定义方法时，方法需要接受参数。那么，当调用方法使用接受到的参数时，首先需要先对参数数据进行合法的判断，数据若不合法，就应该告诉调用者，传递合法的数据进来。这时需要使用抛出异常的方式来告诉调用者。

在java中，提供了一个**throw**关键字，它用来抛出一个指定的异常对象。那么，抛出一个异常具体如何操作呢？

1. 创建一个异常对象。封装一些提示信息(信息可以自己编写)。

2. 需要将这个异常对象告知给调用者。怎么告知呢？怎么将这个异常对象传递到调用者处呢？通过关键字throw就可以完成。throw 异常对象。

   throw**用在方法内**，用来抛出一个异常对象，将这个异常对象传递到调用者处，并结束当前方法的执行。

##### 使用的格式：

```java
throw new 异常类名(参数);
```

例如：

```java
throw new NullPointerException("要访问的arr数组不存在");
throw new ArrayIndexOutOfBoundsException("该索引在数组中不存在，已超出范围");
```

#### 声明异常throws

**声明异常**：将问题标识出来，报告给调用者。如果方法内通过throw抛出了编译时异常，而没有捕获处理（稍后讲解该方式），那么必须通过throws进行声明，让调用者去处理。

关键字**throws**运用于方法声明之上,用于表示当前方法不处理异常,而是提醒该方法的调用者来处理异常(抛出异常).

```java
public class demo8 {
    public static void main(String[] args) {
        int[] arr = new int[10];
        Arrays.setAll(arr, operand -> 0);
        Random rd = new Random();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rd.nextInt(arr.length);
        }
        int[] arr1=new int[0];
        try {
            int max=getmax(arr1);
            System.out.println(max);
        } catch (NullPointerException e) {
           e.printStackTrace();
        } catch (ArrayIndexOutOfBoundsException e){
           e.printStackTrace();
        }


    }
    private static int getmax(int[] arr) {
        if (arr==null){
            throw new  NullPointerException("要访问的arr数组不存在");
        }
        if (arr.length==0){
            throw new ArrayIndexOutOfBoundsException();
        }

        System.out.println("看看我执行了吗");
        int asInt = Arrays.stream(arr).max().getAsInt();
        return asInt;
    }
}

```



#### 捕获异常

#### try…catch

如果异常出现的话,会立刻终止程序,所以我们得处理异常:

1. 该方法不处理,而是声明抛出,由该方法的调用者来处理(throws)。
2. 在方法中使用try-catch的语句块来处理异常。

**try-catch**的方式就是捕获异常。

* **捕获异常**：Java中对异常有针对性的语句进行捕获，可以对出现的异常进行指定方式的处理。

捕获异常语法如下：

```java
try{
     编写可能会出现异常的代码
}catch(异常类型  e){
     处理异常的代码
     //记录日志/打印异常信息/继续抛出异常
}
```

**try：**该代码块中编写可能产生异常的代码。

**catch：**用来进行某种异常的捕获，实现对捕获到的异常进行处理。

> 注意:try和catch都不能单独使用,必须连用。

演示如下：

```java
public class TryCatchDemo {
    public static void main(String[] args) {
        try {// 当产生异常时，必须有处理方式。要么捕获，要么声明。
            read("b.txt");
        } catch (FileNotFoundException e) {// 括号中需要定义什么呢？
          	//try中抛出的是什么异常，在括号中就定义什么异常类型
            System.out.println(e);
        }
        System.out.println("over");
    }
    /*
     *
     * 我们 当前的这个方法中 有异常  有编译期异常
     */
    public static void read(String path) throws FileNotFoundException {
        if (!path.equals("a.txt")) {//如果不是 a.txt这个文件 
            // 我假设  如果不是 a.txt 认为 该文件不存在 是一个错误 也就是异常  throw
            throw new FileNotFoundException("文件不存在");
        }
    }
}
```

如何获取异常信息：

Throwable类中定义了一些查看方法:

* `public String getMessage()`:获取异常的描述信息,原因(提示给用户的时候,就提示错误原因。


* `public String toString()`:获取异常的类型和异常描述信息(不用)。
* `public void printStackTrace()`:打印异常的跟踪栈信息并输出到控制台。

```java
int[] arr={1,2,3,4,5,6};
        try {
            System.out.println(arr[10]);
        }
        catch (Exception e){
            e.printStackTrace();
        }
        System.out.println("看我检测完了吗");
```

报告的异常：

![image-20230719154732775](/../assets/image-20230719154732775.png)

​            *包含了异常的类型,异常的原因,还包括异常出现的位置,在开发和调试阶段,都得使用printStackTrace。*

在开发中呢也可以在catch将编译期异常转换成运行期异常处理。

多个异常使用捕获又该如何处理呢？

1. 多个异常分别处理。
2. 多个异常一次捕获，多次处理。
3. 多个异常一次捕获一次处理。

一般我们是使用一次捕获多次处理方式，格式如下：

```java
try{
     编写可能会出现异常的代码
}catch(异常类型A  e){  当try中出现A类型异常,就用该catch来捕获.
     处理异常的代码
     //记录日志/打印异常信息/继续抛出异常
}catch(异常类型B  e){  当try中出现B类型异常,就用该catch来捕获.
     处理异常的代码
     //记录日志/打印异常信息/继续抛出异常
}
```

> 注意:这种异常处理方式，要求多个catch中的异常不能相同，并且若catch中的多个异常之间有子父类异常的关系，那么子类异常要求在上面的catch处理，父类异常在下面的catch处理。

#### 自定义的异常：

自定义的异常的继承

```java

继承： RuntimeException
核心表示由于参数的问题导致的错误

继承： Exception
核心 提醒程序员检查本地的信息

```

首先定义一个异常的登陆类

```java
// 业务逻辑异常
public class LoginException extends Exception {
    /**
     * 空参构造
     */
    public LoginException() {
    }

    /**
     *
     * @param message 表示异常提示
     */
    public LoginException(String message) {
        super(message);
    }

}
```

测试类：

```java
package com.itheima.test18;

public class Demo {
    // 模拟数据库中已存在账号
    private static String[] names = {"bill","hill","jill"};

    public static void main(String[] args) {
        //调用方法
        try{
            // 可能出现异常的代码
            checkUsername("bill");
            System.out.println("注册成功");//如果没有异常就是注册成功
        } catch(LoginException e) {
            //处理异常
            e.printStackTrace();
        }
    }

    //判断当前注册账号是否存在
    //因为是编译期异常，又想调用者去处理 所以声明该异常
    public static boolean checkUsername(String uname) throws LoginException {
        for (String name : names) {
            if(name.equals(uname)){//如果名字在这里面 就抛出登陆异常
                throw new LoginException("亲"+name+"已经被注册了！");
            }
        }
        return true;
    }
}
```

### File的学习

路径：

相对路径

绝对路径

File

```java
文件和目录路径名的抽象表示形式。
```

#### 构造方法

```java

File(File parent, String child) 
          根据 parent File的父路径名和 child 路径名字符串创建一个新 File 实例。 
File(String pathname) 
          通过将给定路径名字符串转换为抽象路径名来创建一个新 File 实例。 
File(String parent, String child) 
          根据 parent 路径名字符串和 child 路径名字符串创建一个新 File 实例。 
File(URI uri) 
          通过将给定的 file: URI 转换为一个抽象路径名来创建一个新的 File 实例。 

```

第一个字符串的路径对象的创建：

```java
import java.io.File;

public class File_demo1 {

    public static void main(String[] args) {
        String str="C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        File f1=new File(str);
        System.out.println(f1);
    }
}
输出：
    C:\Users\Administrator\IdeaProjects\mystudy\src
```

根据父字符串的和子字符串的地址创建的File 的对象

```java
public class File_demo2 {

    public static void main(String[] args) {
        String str="C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1="com\\itheima";
        File f2=new File(str,str1);
        System.out.println(f2);

    }
}
```

根据File的对象和子字符串构建File的对象

```java
public class File_demo2 {
    public static void main(String[] args) {
        String str="C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1="com\\itheima";
        File f1=new File(str);
        File f2=new File(f1,str1);
        System.out.println(f2);

    }
}
```

#### 常见的成员的方法

##### 判断和获取相关的方法

```java
方法	描述
public String getAbsolutePath()	获取绝对路径
public String getPath()	获取路径
public String getName()	获取名称
public String getParent()	获取上层文件目录路径。若无，返回null
public long length()	获取文件长度（即：字节数）。不能获取目录的长度。
public long lastModified()	获取最后一次的修改时间，毫秒值
public String[] list()	获取指定目录下的所有文件或者文件目录的字符串数组
public File[] listFiles()	获取指定目录下的所有文件或者文件目录的File对象数组

```

```java
public class File_demo2 {
    public static void main(String[] args) {
        String str="C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1="com\\itheima";
        File f1=new File(str);
        File f2=new File(f1,str1);
        System.out.println(f2);
        System.out.println(f2.getAbsoluteFile());
        System.out.println(f2.getPath());    //获取地址
        System.out.println(f2.getName());    //获取名称
        System.out.println(f2.getParent()); //获取上层的地址
        System.out.println(f2.length());  //获取文件的长度
        System.out.println(f2.lastModified());//获取最后一次的修改时间
        String[] list = f2.list();  //获取目录下的所有的文件名
        for (int i = 0; i < list.length; i++) {
            System.out.println(list[i]);
        }
        File[] files = f2.listFiles();  //获取目录下所有的路径的File对象的数组
        for (int i = 0; i < files.length; i++) {
            System.out.println(files[i]);
        }
    }
}
```

判断的方法：

```
方法	描述
public boolean isDirectory()	判断是否是文件目录
public boolean isFile()	判断是否是文件
public boolean exists()	判断是否存在
public boolean canRead()	判断是否可读
public boolean canWrite()	判断是否可写
public boolean isHidden()	判断是否隐藏

```

```java
public class File_demo3 {
    public static void main(String[] args) {
        String str="C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1="com\\itheima";
        File f1=new File(str);
        File f2=new File(f1,str1);
        System.out.println(f2);
        System.out.println(f2.isFile());//判断是否是文件
        System.out.println(f2.isDirectory());//判断是否是文件的目录
        System.out.println(f2.exists());   //判断是否存在
        System.out.println(f2.canRead());//是否可读
        System.out.println(f2.canWrite());//是否可写
        System.out.println(f2.isHidden());//是否隐藏
    }
}

```

创建功能

```java
public boolean createNewFile()	创建文件。若文件存在，则不创建，返回false
public boolean mkdir()	创建文件目录。如果此文件目录存在，就不创建了。如果此文件目录的上层目录不存在，也不创建。
public boolean mkdirs()	创建文件目录。如果上层文件目录不存在，一并创建

```

```java
public class File_demo5 {
    public static void main(String[] args) throws IOException {
        String str="C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1="com\\itheima\\test_demo";
        String str2="com\\itheima\\test_demo\\my.txt";
        File f1=new File(str);
        File f2=new File(f1,str1);
        System.out.println(f2);
        if (f2.mkdir()) {
            System.out.println("创建成功");
        }else System.out.println("创建失败");
        File f3=new File(f1,str2);
        System.out.println(f3.createNewFile());
    }
}
```

注意的事项

**就是我们再创建的的时候使用mkdir和mkdirs，俩种方法完成该操作的时候，我们需要注意一下：madir是不存在父级的文件夹的时候，则不创建该文件夹，而要是mkdirs是直接创建其父文件夹及其本身**

综合练习：

遍历所有的文件夹下面的文件：

```java
public class File_demo6 {
    public static void main(String[] args) throws IOException {
        String str = "C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1 = "com\\itheima\\";
        File f1 = new File(str);
        File f2 = new File(f1, str1);
        System.out.println(f2);
        File[] files = f2.listFiles();
        for (File file : files) {
            System.out.println(file);
        }
        showdir(f2,0);

    }
    public static void showdir(File file, int count) {
        System.out.println("|" + file.getName());
        File[] files = file.listFiles();
        count++;
        for (File file1 : files) {
            if (file1.isFile()) {
                System.out.println(file1);
            } else
                showdir(file1, count);
        }
    }
}
```

删除的方法：

```java
public boolean delete()	删除文件或者文件夹
```

```java
注意事项： Java中的删除不走回收站。 要删除一个文件目录，请注意该文件目录内不能包含文件或者文件目录。
```

综合练习：查找文件下是否存在某一个文件：

```java
public class File_demo7 {
    public static void main(String[] args) throws IOException {
        String str = "C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1 = "com\\itheima\\";
        File f1 = new File(str);
        File f2 = new File(f1, str1);
        System.out.println(f2);
        File[] files = f2.listFiles();
        showdir(new File("D:\\"),0);
    }
    public static void showdir(File file, int count) {
        System.out.println("|"+file);
        File[] files = file.listFiles();
        count++;
        for (File file1 : files) {
            if (file1.isFile()) {
                if (file1.toString().split("\\.")[1].equals(new String("avi"))) {
                    System.out.println(file1.toString().split("\\.")[1]);
                    System.out.println(file1);
                }
            } else
                showdir(file1, count);
        }
    }
}
```

```java
package com.itheima.test19;

import java.io.File;
import java.io.IOException;

public class File_demo7 {
    public static void main(String[] args) throws IOException {
        String str = "C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1 = "com\\itheima\\";
        File f1 = new File(str);
        File f2 = new File(f1, str1);
        System.out.println(f2);
        File[] files = f2.listFiles();
        showdir(new File("D:\\"),0);
    }
    public static void showdir(File file, int count) {
        System.out.println("|"+file);
        File[] files = file.listFiles();
        count++;
        for (File file1 : files) {
            if (file1.isFile()) {
                if ((file1.toString().endsWith(".avi"))) {
                    System.out.println(file1);
                }
            } else
                showdir(file1, count);
        }
    }
}

```



```java
//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

package com.itheima.test19;

import java.io.File;
import java.io.IOException;

public class File_demo7 {
    public File_demo7() {
    }

    public static void main(String[] args) throws IOException {
        String str = "C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src";
        String str1 = "com\\itheima\\";
        File f1 = new File(str);
        File f2 = new File(f1, str1);
        if (f2.mkdirs()) {
            System.out.println(f2);
        }

        deletedir(f2, 0);
    }

    public static void deletedir(File file, int count) {
        System.out.println("|" + file);
        File[] files = file.listFiles();
        ++count;
        File[] var3 = files;
        int var4 = files.length;

        for(int var5 = 0; var5 < var4; ++var5) {
            File file1 = var3[var5];
            if (file1.isDirectory()) {
                deletedir(file1, 0);
            } else {
                file1.delete();
            }
        }

    }
}
```

# 1. IO概述

## 1.1 什么是IO

生活中，你肯定经历过这样的场景。当你编辑一个文本文件，忘记了`ctrl+s` ，可能文件就白白编辑了。当你电脑上插入一个U盘，可以把一个视频，拷贝到你的电脑硬盘里。那么数据都是在哪些设备上的呢？键盘、内存、硬盘、外接设备等等。

我们把这种数据的传输，可以看做是一种数据的流动，按照流动的方向，以内存为基准，分为`输入input` 和`输出output` ，即流向内存是输入流，流出内存的输出流。

Java中I/O操作主要是指使用`java.io`包下的内容，进行输入、输出操作。**输入**也叫做**读取**数据，**输出**也叫做作**写出**数据。

## 1.2 IO的分类

根据数据的流向分为：**输入流**和**输出流**。

* **输入流** ：把数据从`其他设备`上读取到`内存`中的流。 
* **输出流** ：把数据从`内存` 中写出到`其他设备`上的流。

格局数据的类型分为：**字节流**和**字符流**。

* **字节流** ：以字节为单位，读写数据的流。
* **字符流** ：以字符为单位，读写数据的流。

## 1.3 IO的流向说明图解

## 1.4 顶级父类们

|            |           **输入流**            |              输出流              |
| :--------: | :-----------------------------: | :------------------------------: |
| **字节流** | 字节输入流<br />**InputStream** | 字节输出流<br />**OutputStream** |
| **字符流** |   字符输入流<br />**Reader**    |    字符输出流<br />**Writer**    |

# 2. 字节流

## 2.1 一切皆为字节

一切文件数据(文本、图片、视频等)在存储时，都是以二进制数字的形式保存，都一个一个的字节，那么传输时一样如此。所以，字节流可以传输任意文件数据。在操作流的时候，我们要时刻明确，无论使用什么样的流对象，底层传输的始终为二进制数据。

## 2.2 字节输出流【OutputStream】

`java.io.OutputStream `抽象类是表示字节输出流的所有类的超类，将指定的字节信息写出到目的地。它定义了字节输出流的基本共性功能方法。

* `public void close()` ：关闭此输出流并释放与此流相关联的任何系统资源。  
* `public void flush() ` ：刷新此输出流并强制任何缓冲的输出字节被写出。  
* `public void write(byte[] b)`：将 b.length字节从指定的字节数组写入此输出流。  
* `public void write(byte[] b, int off, int len)` ：从指定的字节数组写入 len字节，从偏移量 off开始输出到此输出流。  
* `public abstract void write(int b)` ：将指定的字节输出流。

> 小贴士：
>
> close方法，当完成流的操作时，必须调用此方法，释放系统资源。

## 2.3 FileOutputStream类

`OutputStream`有很多子类，我们从最简单的一个子类开始。

`java.io.FileOutputStream `类是文件输出流，用于将数据写出到文件。

### 构造方法

* `public FileOutputStream(File file)`：创建文件输出流以写入由指定的 File对象表示的文件。 
* `public FileOutputStream(String name)`： 创建文件输出流以指定的名称写入文件。  

当你创建一个流对象时，必须传入一个文件路径。该路径下，如果没有这个文件，会创建该文件。如果有这个文件，会清空这个文件的数据。

* 构造举例，代码如下：

```java
public class FileOutputStreamConstructor throws IOException {
    public static void main(String[] args) {
   	 	// 使用File对象创建流对象
        File file = new File("a.txt");
        FileOutputStream fos = new FileOutputStream(file);
      
        // 使用文件名称创建流对象
        FileOutputStream fos = new FileOutputStream("b.txt");
    }
}
```

### 写出字节数据

1. **写出字节**：`write(int b)` 方法，每次可以写出一个字节数据，代码使用演示：

```java
public class FOSWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileOutputStream fos = new FileOutputStream("fos.txt");     
      	// 写出数据
      	fos.write(97); // 写出第1个字节
      	fos.write(98); // 写出第2个字节
      	fos.write(99); // 写出第3个字节
      	// 关闭资源
        fos.close();
    }
}
输出结果：
abc
```

> 小贴士：
>
> 1. 虽然参数为int类型四个字节，但是只会保留一个字节的信息写出。
> 2. 流操作完毕后，必须释放系统资源，调用close方法，千万记得。

2. **写出字节数组**：`write(byte[] b)`，每次可以写出数组中的数据，代码使用演示：

```java
public class FOSWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileOutputStream fos = new FileOutputStream("fos.txt");     
      	// 字符串转换为字节数组
      	byte[] b = "黑马程序员".getBytes();
      	// 写出字节数组数据
      	fos.write(b);
      	// 关闭资源
        fos.close();
    }
}
输出结果：
黑马程序员
```

3. **写出指定长度字节数组**：`write(byte[] b, int off, int len)` ,每次写出从off索引开始，len个字节，代码使用演示：

```java
public class FOSWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileOutputStream fos = new FileOutputStream("fos.txt");     
      	// 字符串转换为字节数组
      	byte[] b = "abcde".getBytes();
		// 写出从索引2开始，2个字节。索引2是c，两个字节，也就是cd。
        fos.write(b,2,2);
      	// 关闭资源
        fos.close();
    }
}
输出结果：
cd
```

### 数据追加续写

经过以上的演示，每次程序运行，创建输出流对象，都会清空目标文件中的数据。如何保留目标文件中数据，还能继续添加新数据呢？

- `public FileOutputStream(File file, boolean append)`： 创建文件输出流以写入由指定的 File对象表示的文件。  
- `public FileOutputStream(String name, boolean append)`： 创建文件输出流以指定的名称写入文件。  

这两个构造方法，参数中都需要传入一个boolean类型的值，`true` 表示追加数据，`false` 表示清空原有数据。这样创建的输出流对象，就可以指定是否追加续写了，代码使用演示：

```java
public class FOSWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileOutputStream fos = new FileOutputStream("fos.txt"，true);     
      	// 字符串转换为字节数组
      	byte[] b = "abcde".getBytes();
		// 写出从索引2开始，2个字节。索引2是c，两个字节，也就是cd。
        fos.write(b);
      	// 关闭资源
        fos.close();
    }
}
文件操作前：cd
文件操作后：cdabcde
```

### 写出换行

Windows系统里，换行符号是`\r\n` 。把

以指定是否追加续写了，代码使用演示：

```java
public class FOSWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileOutputStream fos = new FileOutputStream("fos.txt");  
      	// 定义字节数组
      	byte[] words = {97,98,99,100,101};
      	// 遍历数组
        for (int i = 0; i < words.length; i++) {
          	// 写出一个字节
            fos.write(words[i]);
          	// 写出一个换行, 换行符号转成数组写出
            fos.write("\r\n".getBytes());
        }
      	// 关闭资源
        fos.close();
    }
}

输出结果：
a
b
c
d
e
```

> * 回车符`\r`和换行符`\n` ：
>   * 回车符：回到一行的开头（return）。
>   * 换行符：下一行（newline）。
> * 系统中的换行：
>   * Windows系统里，每行结尾是 `回车+换行` ，即`\r\n`；
>   * Unix系统里，每行结尾只有 `换行` ，即`\n`；
>   * Mac系统里，每行结尾是 `回车` ，即`\r`。从 Mac OS X开始与Linux统一。

## 2.4 字节输入流【InputStream】

`java.io.InputStream `抽象类是表示字节输入流的所有类的超类，可以读取字节信息到内存中。它定义了字节输入流的基本共性功能方法。

- `public void close()` ：关闭此输入流并释放与此流相关联的任何系统资源。    
- `public abstract int read()`： 从输入流读取数据的下一个字节。 
- `public int read(byte[] b)`： 从输入流中读取一些字节数，并将它们存储到字节数组 b中 。

> 小贴士：
>
> close方法，当完成流的操作时，必须调用此方法，释放系统资源。

## 2.5 FileInputStream类

`java.io.FileInputStream `类是文件输入流，从文件中读取字节。

### 构造方法

* `FileInputStream(File file)`： 通过打开与实际文件的连接来创建一个 FileInputStream ，该文件由文件系统中的 File对象 file命名。 
* `FileInputStream(String name)`： 通过打开与实际文件的连接来创建一个 FileInputStream ，该文件由文件系统中的路径名 name命名。  

当你创建一个流对象时，必须传入一个文件路径。该路径下，如果没有该文件,会抛出`FileNotFoundException` 。

- 构造举例，代码如下：

```java
public class FileInputStreamConstructor throws IOException{
    public static void main(String[] args) {
   	 	// 使用File对象创建流对象
        File file = new File("a.txt");
        FileInputStream fos = new FileInputStream(file);
      
        // 使用文件名称创建流对象
        FileInputStream fos = new FileInputStream("b.txt");
    }
}
```

### 读取字节数据

1. **读取字节**：`read`方法，每次可以读取一个字节的数据，提升为int类型，读取到文件末尾，返回`-1`，代码使用演示：

```java
public class FISRead {
    public static void main(String[] args) throws IOException{
      	// 使用文件名称创建流对象
       	FileInputStream fis = new FileInputStream("read.txt");
      	// 读取数据，返回一个字节
        int read = fis.read();
        System.out.println((char) read);
        read = fis.read();
        System.out.println((char) read);
        read = fis.read();
        System.out.println((char) read);
        read = fis.read();
        System.out.println((char) read);
        read = fis.read();
        System.out.println((char) read);
      	// 读取到末尾,返回-1
       	read = fis.read();
        System.out.println( read);
		// 关闭资源
        fis.close();
    }
}
输出结果：
a
b
c
d
e
-1
```

循环改进读取方式，代码使用演示：

```java
public class FISRead {
    public static void main(String[] args) throws IOException{
      	// 使用文件名称创建流对象
       	FileInputStream fis = new FileInputStream("read.txt");
      	// 定义变量，保存数据
        int b ；
        // 循环读取
        while ((b = fis.read())!=-1) {
            System.out.println((char)b);
        }
		// 关闭资源
        fis.close();
    }
}
输出结果：
a
b
c
d
e
```

> 小贴士：
>
> 1. 虽然读取了一个字节，但是会自动提升为int类型。
> 2. 流操作完毕后，必须释放系统资源，调用close方法，千万记得。

2. **使用字节数组读取**：`read(byte[] b)`，每次读取b的长度个字节到数组中，返回读取到的有效字节个数，读取到末尾时，返回`-1` ，代码使用演示：

```java
public class FISRead {
    public static void main(String[] args) throws IOException{
      	// 使用文件名称创建流对象.
       	FileInputStream fis = new FileInputStream("read.txt"); // 文件中为abcde
      	// 定义变量，作为有效个数
        int len ；
        // 定义字节数组，作为装字节数据的容器   
        byte[] b = new byte[2];
        // 循环读取
        while (( len= fis.read(b))!=-1) {
           	// 每次读取后,把数组变成字符串打印
            System.out.println(new String(b));
        }
		// 关闭资源
        fis.close();
    }
}

输出结果：
ab
cd
ed
```

错误数据`d`，是由于最后一次读取时，只读取一个字节`e`，数组中，上次读取的数据没有被完全替换，所以要通过`len` ，获取有效的字节，代码使用演示：

```java
public class FISRead {
    public static void main(String[] args) throws IOException{
      	// 使用文件名称创建流对象.
       	FileInputStream fis = new FileInputStream("read.txt"); // 文件中为abcde
      	// 定义变量，作为有效个数
        int len ；
        // 定义字节数组，作为装字节数据的容器   
        byte[] b = new byte[2];
        // 循环读取
        while (( len= fis.read(b))!=-1) {
           	// 每次读取后,把数组的有效字节部分，变成字符串打印
            System.out.println(new String(b，0，len));//  len 每次读取的有效字节个数
        }
		// 关闭资源
        fis.close();
    }
}

输出结果：
ab
cd
e
```

> 小贴士：
>
> 使用数组读取，每次读取多个字节，减少了系统间的IO操作次数，从而提高了读写的效率，建议开发中使用。

## 2.6 字节流练习：图片复制

### 复制原理图解

![](/../img/2_copy.jpg)

### 案例实现

复制图片文件，代码使用演示：

```java
public class Copy {
    public static void main(String[] args) throws IOException {
        // 1.创建流对象
        // 1.1 指定数据源
        FileInputStream fis = new FileInputStream("D:\\test.jpg");
        // 1.2 指定目的地
        FileOutputStream fos = new FileOutputStream("test_copy.jpg");

        // 2.读写数据
        // 2.1 定义数组
        byte[] b = new byte[1024];
        // 2.2 定义长度
        int len;
        // 2.3 循环读取
        while ((len = fis.read(b))!=-1) {
            // 2.4 写出数据
            fos.write(b, 0 , len);
        }

        // 3.关闭资源
        fos.close();
        fis.close();
    }
}
```

> 小贴士：
>
> 流的关闭原则：先开后关，后开先关。

# 3. 字符流

当使用字节流读取文本文件时，可能会有一个小问题。就是遇到中文字符时，可能不会显示完整的字符，那是因为一个中文字符可能占用多个字节存储。所以Java提供一些字符流类，以字符为单位读写数据，专门用于处理文本文件。

## 3.1 字符输入流【Reader】

`java.io.Reader`抽象类是表示用于读取字符流的所有类的超类，可以读取字符信息到内存中。它定义了字符输入流的基本共性功能方法。

- `public void close()` ：关闭此流并释放与此流相关联的任何系统资源。    
- `public int read()`： 从输入流读取一个字符。 
- `public int read(char[] cbuf)`： 从输入流中读取一些字符，并将它们存储到字符数组 cbuf中 。

## 3.2 FileReader类  

`java.io.FileReader `类是读取字符文件的便利类。构造时使用系统默认的字符编码和默认字节缓冲区。

> 小贴士：
>
> 1. 字符编码：字节与字符的对应规则。Windows系统的中文编码默认是GBK编码表。
>
>    idea中UTF-8
>
> 2. 字节缓冲区：一个字节数组，用来临时存储字节数据。

### 构造方法

- `FileReader(File file)`： 创建一个新的 FileReader ，给定要读取的File对象。   
- `FileReader(String fileName)`： 创建一个新的 FileReader ，给定要读取的文件的名称。  

当你创建一个流对象时，必须传入一个文件路径。类似于FileInputStream 。

- 构造举例，代码如下：

```java
public class FileReaderConstructor throws IOException{
    public static void main(String[] args) {
   	 	// 使用File对象创建流对象
        File file = new File("a.txt");
        FileReader fr = new FileReader(file);
      
        // 使用文件名称创建流对象
        FileReader fr = new FileReader("b.txt");
    }
}
```

### 读取字符数据

1. **读取字符**：`read`方法，每次可以读取一个字符的数据，提升为int类型，读取到文件末尾，返回`-1`，循环读取，代码使用演示：

```java
public class FRRead {
    public static void main(String[] args) throws IOException {
      	// 使用文件名称创建流对象
       	FileReader fr = new FileReader("read.txt");
      	// 定义变量，保存数据
        int b ；
        // 循环读取
        while ((b = fr.read())!=-1) {
            System.out.println((char)b);
        }
		// 关闭资源
        fr.close();
    }
}
输出结果：
黑
马
程
序
员
```

> 小贴士：虽然读取了一个字符，但是会自动提升为int类型。

2. **使用字符数组读取**：`read(char[] cbuf)`，每次读取b的长度个字符到数组中，返回读取到的有效字符个数，读取到末尾时，返回`-1` ，代码使用演示：

```java
public class FRRead {
    public static void main(String[] args) throws IOException {
      	// 使用文件名称创建流对象
       	FileReader fr = new FileReader("read.txt");
      	// 定义变量，保存有效字符个数
        int len ；
        // 定义字符数组，作为装字符数据的容器
         char[] cbuf = new char[2];
        // 循环读取
        while ((len = fr.read(cbuf))!=-1) {
            System.out.println(new String(cbuf));
        }
		// 关闭资源
        fr.close();
    }
}
输出结果：
黑马
程序
员序
```

获取有效的字符改进，代码使用演示：

```java
public class FISRead {
    public static void main(String[] args) throws IOException {
      	// 使用文件名称创建流对象
       	FileReader fr = new FileReader("read.txt");
      	// 定义变量，保存有效字符个数
        int len ；
        // 定义字符数组，作为装字符数据的容器
        char[] cbuf = new char[2];
        // 循环读取
        while ((len = fr.read(cbuf))!=-1) {
            System.out.println(new String(cbuf,0,len));
        }
    	// 关闭资源
        fr.close();
    }
}

输出结果：
黑马
程序
员
```

## 3.3 字符输出流【Writer】

`java.io.Writer `抽象类是表示用于写出字符流的所有类的超类，将指定的字符信息写出到目的地。它定义了字节输出流的基本共性功能方法。

- `void write(int c)` 写入单个字符。
- `void write(char[] cbuf) `写入字符数组。 
- `abstract  void write(char[] cbuf, int off, int len) `写入字符数组的某一部分,off数组的开始索引,len写的字符个数。 
- `void write(String str) `写入字符串。 
- `void write(String str, int off, int len)` 写入字符串的某一部分,off字符串的开始索引,len写的字符个数。
- `void flush() `刷新该流的缓冲。  
- `void close()` 关闭此流，但要先刷新它。 

## 3.4 FileWriter类

`java.io.FileWriter `类是写出字符到文件的便利类。构造时使用系统默认的字符编码和默认字节缓冲区。

### 构造方法

- `FileWriter(File file)`： 创建一个新的 FileWriter，给定要读取的File对象。   
- `FileWriter(String fileName)`： 创建一个新的 FileWriter，给定要读取的文件的名称。  

当你创建一个流对象时，必须传入一个文件路径，类似于FileOutputStream。

- 构造举例，代码如下：

```java
public class FileWriterConstructor {
    public static void main(String[] args) throws IOException {
   	 	// 使用File对象创建流对象
        File file = new File("a.txt");
        FileWriter fw = new FileWriter(file);
      
        // 使用文件名称创建流对象
        FileWriter fw = new FileWriter("b.txt");
    }
}
```

### 基本写出数据

**写出字符**：`write(int b)` 方法，每次可以写出一个字符数据，代码使用演示：

```java
public class FWWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileWriter fw = new FileWriter("fw.txt");     
      	// 写出数据
      	fw.write(97); // 写出第1个字符
      	fw.write('b'); // 写出第2个字符
      	fw.write('C'); // 写出第3个字符
      	fw.write(30000); // 写出第4个字符，中文编码表中30000对应一个汉字。
      
      	/*
        【注意】关闭资源时,与FileOutputStream不同。
      	 如果不关闭,数据只是保存到缓冲区，并未保存到文件。
        */
        // fw.close();
    }
}
输出结果：
abC田
```

> 小贴士：
>
> 1. 虽然参数为int类型四个字节，但是只会保留一个字符的信息写出。
> 2. 未调用close方法，数据只是保存到了缓冲区，并未写出到文件中。

### 关闭和刷新

因为内置缓冲区的原因，如果不关闭输出流，无法写出字符到文件中。但是关闭的流对象，是无法继续写出数据的。如果我们既想写出数据，又想继续使用流，就需要`flush` 方法了。

* `flush` ：刷新缓冲区，流对象可以继续使用。
* `close `:先刷新缓冲区，然后通知系统释放资源。流对象不可以再被使用了。

代码使用演示：

```java
public class FWWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileWriter fw = new FileWriter("fw.txt");
        // 写出数据，通过flush
        fw.write('刷'); // 写出第1个字符
        fw.flush();
        fw.write('新'); // 继续写出第2个字符，写出成功
        fw.flush();
      
      	// 写出数据，通过close
        fw.write('关'); // 写出第1个字符
        fw.close();
        fw.write('闭'); // 继续写出第2个字符,【报错】java.io.IOException: Stream closed
        fw.close();
    }
}
```

> 小贴士：即便是flush方法写出了数据，操作的最后还是要调用close方法，释放系统资源。

### 写出其他数据

1. **写出字符数组** ：`write(char[] cbuf)` 和 `write(char[] cbuf, int off, int len)` ，每次可以写出字符数组中的数据，用法类似FileOutputStream，代码使用演示：

```java
public class FWWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileWriter fw = new FileWriter("fw.txt");     
      	// 字符串转换为字节数组
      	char[] chars = "黑马程序员".toCharArray();
      
      	// 写出字符数组
      	fw.write(chars); // 黑马程序员
        
		// 写出从索引2开始，2个字节。索引2是'程'，两个字节，也就是'程序'。
        fw.write(b,2,2); // 程序
      
      	// 关闭资源
        fos.close();
    }
}
```

2. **写出字符串**：`write(String str)` 和 `write(String str, int off, int len)` ，每次可以写出字符串中的数据，更为方便，代码使用演示：

```java
public class FWWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象
        FileWriter fw = new FileWriter("fw.txt");     
      	// 字符串
      	String msg = "黑马程序员";
      
      	// 写出字符数组
      	fw.write(msg); //黑马程序员
      
		// 写出从索引2开始，2个字节。索引2是'程'，两个字节，也就是'程序'。
        fw.write(msg,2,2);	// 程序
      	
        // 关闭资源
        fos.close();
    }
}
```

3. **续写和换行**：操作类似于FileOutputStream。

```java
public class FWWrite {
    public static void main(String[] args) throws IOException {
        // 使用文件名称创建流对象，可以续写数据
        FileWriter fw = new FileWriter("fw.txt"，true);     
      	// 写出字符串
        fw.write("黑马");
      	// 写出换行
      	fw.write("\r\n");
      	// 写出字符串
  		fw.write("程序员");
      	// 关闭资源
        fw.close();
    }
}
输出结果:
黑马
程序员
```

> 小贴士：字符流，只能操作文本文件，不能操作图片，视频等非文本文件。
>
> 当我们单纯读或者写文本文件时  使用字符流 其他情况使用字节流

# 4. IO异常的处理

### JDK7前处理

之前的入门练习，我们一直把异常抛出，而实际开发中并不能这样处理，建议使用`try...catch...finally` 代码块，处理异常部分，代码使用演示：

```java  
public class HandleException1 {
    public static void main(String[] args) {
      	// 声明变量
        FileWriter fw = null;
        try {
            //创建流对象
            fw = new FileWriter("fw.txt");
            // 写出数据
            fw.write("黑马程序员"); //黑马程序员
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (fw != null) {
                    fw.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### JDK7的处理(扩展知识点了解内容)

还可以使用JDK7优化后的`try-with-resource` 语句，该语句确保了每个资源在语句结束时关闭。所谓的资源（resource）是指在程序完成后，必须关闭的对象。

格式：

```java
try (创建流对象语句，如果多个,使用';'隔开) {
	// 读写数据
} catch (IOException e) {
	e.printStackTrace();
}
```

代码使用演示：

```java
public class HandleException2 {
    public static void main(String[] args) {
      	// 创建流对象
        try ( FileWriter fw = new FileWriter("fw.txt"); ) {
            // 写出数据
            fw.write("黑马程序员"); //黑马程序员
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### JDK9的改进(扩展知识点了解内容)

JDK9中`try-with-resource` 的改进，对于**引入对象**的方式，支持的更加简洁。被引入的对象，同样可以自动关闭，无需手动close，我们来了解一下格式。

改进前格式：

```java
// 被final修饰的对象
final Resource resource1 = new Resource("resource1");
// 普通对象
Resource resource2 = new Resource("resource2");
// 引入方式：创建新的变量保存
try (Resource r1 = resource1;
     Resource r2 = resource2) {
     // 使用对象
}
```

改进后格式：

```java
// 被final修饰的对象
final Resource resource1 = new Resource("resource1");
// 普通对象
Resource resource2 = new Resource("resource2");

// 引入方式：直接引入
try (resource1; resource2) {
     // 使用对象
}
```

改进后，代码使用演示：

```java
public class TryDemo {
    public static void main(String[] args) throws IOException {
       	// 创建流对象
        final  FileReader fr  = new FileReader("in.txt");
        FileWriter fw = new FileWriter("out.txt");
       	// 引入到try中
        try (fr; fw) {
          	// 定义变量
            int b;
          	// 读取数据
          	while ((b = fr.read())!=-1) {
            	// 写出数据
            	fw.write(b);
          	}
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

# 5. 综合练习

## 练习1：拷贝文件夹

```java
public class Test01 {
    public static void main(String[] args) throws IOException {
        //拷贝一个文件夹，考虑子文件夹

        //1.创建对象表示数据源
        File src = new File("D:\\aaa\\src");
        //2.创建对象表示目的地
        File dest = new File("D:\\aaa\\dest");

        //3.调用方法开始拷贝
        copydir(src,dest);



    }

    /*
    * 作用：拷贝文件夹
    * 参数一：数据源
    * 参数二：目的地
    *
    * */
    private static void copydir(File src, File dest) throws IOException {
        dest.mkdirs();
        //递归
        //1.进入数据源
        File[] files = src.listFiles();
        //2.遍历数组
        for (File file : files) {
            if(file.isFile()){
                //3.判断文件，拷贝
                FileInputStream fis = new FileInputStream(file);
                FileOutputStream fos = new FileOutputStream(new File(dest,file.getName()));
                byte[] bytes = new byte[1024];
                int len;
                while((len = fis.read(bytes)) != -1){
                    fos.write(bytes,0,len);
                }
                fos.close();
                fis.close();
            }else {
                //4.判断文件夹，递归
                copydir(file, new File(dest,file.getName()));
            }
        }
    }
}

```

## 练习2：文件加密

```java
public class Test02 {
    public static void main(String[] args) throws IOException {
        /*
            为了保证文件的安全性，就需要对原始文件进行加密存储，再使用的时候再对其进行解密处理。
            加密原理：
                对原始文件中的每一个字节数据进行更改，然后将更改以后的数据存储到新的文件中。
            解密原理：
                读取加密之后的文件，按照加密的规则反向操作，变成原始文件。

             ^ : 异或
                 两边相同：false
                 两边不同：true

                 0：false
                 1：true

               100:1100100
               10: 1010

               1100100
             ^ 0001010
             __________
               1101110
             ^ 0001010
             __________
               1100100

        */
    }

    public static void encryptionAndReduction(File src, File dest) throws IOException {
        FileInputStream fis = new FileInputStream(src);
        FileOutputStream fos = new FileOutputStream(dest);
        int b;
        while ((b = fis.read()) != -1) {
            fos.write(b ^ 2);
        }
        //4.释放资源
        fos.close();
        fis.close();
    }


}

```

## 练习3：数字排序

文本文件中有以下的数据：
                2-1-9-4-7-8
 将文件中的数据进行排序，变成以下的数据：
                1-2-4-7-8-9

实现方式一：

```java
public class Test03 {
    public static void main(String[] args) throws IOException {
        /*
            文本文件中有以下的数据：
                2-1-9-4-7-8
            将文件中的数据进行排序，变成以下的数据：
                1-2-4-7-8-9
        */


        //1.读取数据
        FileReader fr = new FileReader("myio\\a.txt");
        StringBuilder sb = new StringBuilder();
        int ch;
        while((ch = fr.read()) != -1){
            sb.append((char)ch);
        }
        fr.close();
        System.out.println(sb);
        //2.排序
        String str = sb.toString();
        String[] arrStr = str.split("-");//2-1-9-4-7-8

        ArrayList<Integer> list = new ArrayList<>();
        for (String s : arrStr) {
            int i = Integer.parseInt(s);
            list.add(i);
        }
        Collections.sort(list);
        System.out.println(list);
        //3.写出
        FileWriter fw = new FileWriter("myio\\a.txt");
        for (int i = 0; i < list.size(); i++) {
            if(i == list.size() - 1){
                fw.write(list.get(i) + "");
            }else{
                fw.write(list.get(i) + "-");
            }
        }
        fw.close();
    }
}
```

实现方式二：

```java
public class Test04 {
    public static void main(String[] args) throws IOException {
        /*
            文本文件中有以下的数据：
                2-1-9-4-7-8
            将文件中的数据进行排序，变成以下的数据：
                1-2-4-7-8-9

           细节1：
                文件中的数据不要换行

            细节2:
                bom头
        */
        //1.读取数据
        FileReader fr = new FileReader("myio\\a.txt");
        StringBuilder sb = new StringBuilder();
        int ch;
        while((ch = fr.read()) != -1){
            sb.append((char)ch);
        }
        fr.close();
        System.out.println(sb);
        //2.排序
        Integer[] arr = Arrays.stream(sb.toString()
                                      .split("-"))
            .map(Integer::parseInt)
            .sorted()
            .toArray(Integer[]::new);
        //3.写出
        FileWriter fw = new FileWriter("myio\\a.txt");
        String s = Arrays.toString(arr).replace(", ","-");
        String result = s.substring(1, s.length() - 1);
        fw.write(result);
        fw.close();
    }
}
```

# 1. 缓冲流

昨天学习了基本的一些流，作为IO流的入门，今天我们要见识一些更强大的流。比如能够高效读写的缓冲流，能够转换编码的转换流，能够持久化存储对象的序列化流等等。这些功能更为强大的流，都是在基本的流对象基础之上创建而来的，就像穿上铠甲的武士一样，相当于是对基本流对象的一种增强。

## 1.1 概述

缓冲流,也叫高效流，是对4个基本的`FileXxx` 流的增强，所以也是4个流，按照数据类型分类：

* **字节缓冲流**：`BufferedInputStream`，`BufferedOutputStream` 
* **字符缓冲流**：`BufferedReader`，`BufferedWriter`

缓冲流的基本原理，是在创建流对象时，会创建一个内置的默认大小的缓冲区数组，通过缓冲区读写，减少系统IO次数，从而提高读写的效率。

## 1.2 字节缓冲流

### 构造方法

* `public BufferedInputStream(InputStream in)` ：创建一个 新的缓冲输入流。 
* `public BufferedOutputStream(OutputStream out)`： 创建一个新的缓冲输出流。

构造举例，代码如下：

```java
// 创建字节缓冲输入流
BufferedInputStream bis = new BufferedInputStream(new FileInputStream("bis.txt"));
// 创建字节缓冲输出流
BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("bos.txt"));
```

### 效率测试

查询API，缓冲流读写方法与基本的流是一致的，我们通过复制大文件（375MB），测试它的效率。

1. 基本流，代码如下：

```java
public class BufferedDemo {
    public static void main(String[] args) throws FileNotFoundException {
        // 记录开始时间
      	long start = System.currentTimeMillis();
		// 创建流对象
        try (
        	FileInputStream fis = new FileInputStream("jdk9.exe");
        	FileOutputStream fos = new FileOutputStream("copy.exe")
        ){
        	// 读写数据
            int b;
            while ((b = fis.read()) != -1) {
                fos.write(b);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
		// 记录结束时间
        long end = System.currentTimeMillis();
        System.out.println("普通流复制时间:"+(end - start)+" 毫秒");
    }
}

十几分钟过去了...
```

2. 缓冲流，代码如下：

```java
public class BufferedDemo {
    public static void main(String[] args) throws FileNotFoundException {
        // 记录开始时间
      	long start = System.currentTimeMillis();
		// 创建流对象
        try (
        	BufferedInputStream bis = new BufferedInputStream(new FileInputStream("jdk9.exe"));
	     BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("copy.exe"));
        ){
        // 读写数据
            int b;
            while ((b = bis.read()) != -1) {
                bos.write(b);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
		// 记录结束时间
        long end = System.currentTimeMillis();
        System.out.println("缓冲流复制时间:"+(end - start)+" 毫秒");
    }
}

缓冲流复制时间:8016 毫秒
```

如何更快呢？

使用数组的方式，代码如下：

```java
public class BufferedDemo {
    public static void main(String[] args) throws FileNotFoundException {
      	// 记录开始时间
        long start = System.currentTimeMillis();
		// 创建流对象
        try (
			BufferedInputStream bis = new BufferedInputStream(new FileInputStream("jdk9.exe"));
		 BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("copy.exe"));
        ){
          	// 读写数据
            int len;
            byte[] bytes = new byte[8*1024];
            while ((len = bis.read(bytes)) != -1) {
                bos.write(bytes, 0 , len);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
		// 记录结束时间
        long end = System.currentTimeMillis();
        System.out.println("缓冲流使用数组复制时间:"+(end - start)+" 毫秒");
    }
}
缓冲流使用数组复制时间:666 毫秒
```

## 1.3 字符缓冲流

### 构造方法

* `public BufferedReader(Reader in)` ：创建一个 新的缓冲输入流。 
* `public BufferedWriter(Writer out)`： 创建一个新的缓冲输出流。

构造举例，代码如下：

```java
// 创建字符缓冲输入流
BufferedReader br = new BufferedReader(new FileReader("br.txt"));
// 创建字符缓冲输出流
BufferedWriter bw = new BufferedWriter(new FileWriter("bw.txt"));
```

### 特有方法

字符缓冲流的基本方法与普通字符流调用方式一致，不再阐述，我们来看它们具备的特有方法。

* BufferedReader：`public String readLine()`: 读一行文字。 
* BufferedWriter：`public void newLine()`: 写一行行分隔符,由系统属性定义符号。 

`readLine`方法演示，代码如下：

```java
public class BufferedReaderDemo {
    public static void main(String[] args) throws IOException {
      	 // 创建流对象
        BufferedReader br = new BufferedReader(new FileReader("in.txt"));
		// 定义字符串,保存读取的一行文字
        String line  = null;
      	// 循环读取,读取到最后返回null
        while ((line = br.readLine())!=null) {
            System.out.print(line);
            System.out.println("------");
        }
		// 释放资源
        br.close();
    }
}
```

`newLine`方法演示，代码如下：

  ```java
public class BufferedWriterDemo throws IOException {
    public static void main(String[] args) throws IOException  {
      	// 创建流对象
		BufferedWriter bw = new BufferedWriter(new FileWriter("out.txt"));
      	// 写出数据
        bw.write("黑马");
      	// 写出换行
        bw.newLine();
        bw.write("程序");
        bw.newLine();
        bw.write("员");
        bw.newLine();
		// 释放资源
        bw.close();
    }
}
输出效果:
黑马
程序
员
  ```

## 1.4 练习:文本排序

请将文本信息恢复顺序。

```
3.侍中、侍郎郭攸之、费祎、董允等，此皆良实，志虑忠纯，是以先帝简拔以遗陛下。愚以为宫中之事，事无大小，悉以咨之，然后施行，必得裨补阙漏，有所广益。
8.愿陛下托臣以讨贼兴复之效，不效，则治臣之罪，以告先帝之灵。若无兴德之言，则责攸之、祎、允等之慢，以彰其咎；陛下亦宜自谋，以咨诹善道，察纳雅言，深追先帝遗诏，臣不胜受恩感激。
4.将军向宠，性行淑均，晓畅军事，试用之于昔日，先帝称之曰能，是以众议举宠为督。愚以为营中之事，悉以咨之，必能使行阵和睦，优劣得所。
2.宫中府中，俱为一体，陟罚臧否，不宜异同。若有作奸犯科及为忠善者，宜付有司论其刑赏，以昭陛下平明之理，不宜偏私，使内外异法也。
1.先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失义，以塞忠谏之路也。
9.今当远离，临表涕零，不知所言。
6.臣本布衣，躬耕于南阳，苟全性命于乱世，不求闻达于诸侯。先帝不以臣卑鄙，猥自枉屈，三顾臣于草庐之中，咨臣以当世之事，由是感激，遂许先帝以驱驰。后值倾覆，受任于败军之际，奉命于危难之间，尔来二十有一年矣。
7.先帝知臣谨慎，故临崩寄臣以大事也。受命以来，夙夜忧叹，恐付托不效，以伤先帝之明，故五月渡泸，深入不毛。今南方已定，兵甲已足，当奖率三军，北定中原，庶竭驽钝，攘除奸凶，兴复汉室，还于旧都。此臣所以报先帝而忠陛下之职分也。至于斟酌损益，进尽忠言，则攸之、祎、允之任也。
5.亲贤臣，远小人，此先汉所以兴隆也；亲小人，远贤臣，此后汉所以倾颓也。先帝在时，每与臣论此事，未尝不叹息痛恨于桓、灵也。侍中、尚书、长史、参军，此悉贞良死节之臣，愿陛下亲之信之，则汉室之隆，可计日而待也。
```

### 案例分析

1. 逐行读取文本信息。
2. 把读取到的文本存储到集合中
3. 对集合中的文本进行排序
4. 遍历集合，按顺序，写出文本信息。

### 案例实现

```java
public class Demo05Test {
    public static void main(String[] args) throws IOException {
        //1.创建ArrayList集合,泛型使用String
        ArrayList<String> list = new ArrayList<>();
        //2.创建BufferedReader对象,构造方法中传递FileReader对象
        BufferedReader br = new BufferedReader(new FileReader("10_IO\\in.txt"));
        //3.创建BufferedWriter对象,构造方法中传递FileWriter对象
        BufferedWriter bw = new BufferedWriter(new FileWriter("10_IO\\out.txt"));
        //4.使用BufferedReader对象中的方法readLine,以行的方式读取文本
        String line;
        while((line = br.readLine())!=null){
            //5.把读取到的文本存储到ArrayList集合中
            list.add(line);
        }
        //6.使用Collections集合工具类中的方法sort,对集合中的元素按照自定义规则排序
        Collections.sort(list, new Comparator<String>() {
            /*
                o1-o2:升序
                o2-o1:降序
             */
            @Override
            public int compare(String o1, String o2) {
                //依次比较集合中两个元素的首字母,升序排序
                return o1.charAt(0)-o2.charAt(0);
            }
        });
        //7.遍历ArrayList集合,获取每一个元素
        for (String s : list) {
            //8.使用BufferedWriter对象中的方法wirte,把遍历得到的元素写入到文本中(内存缓冲区中)
            bw.write(s);
            //9.写换行
            bw.newLine();
        }
        //10.释放资源
        bw.close();
        br.close();
    }
}
```



# 2. 转换流

## 2.1 字符编码和字符集

### 字符编码

计算机中储存的信息都是用二进制数表示的，而我们在屏幕上看到的数字、英文、标点符号、汉字等字符是二进制数转换之后的结果。按照某种规则，将字符存储到计算机中，称为**编码** 。反之，将存储在计算机中的二进制数按照某种规则解析显示出来，称为**解码** 。比如说，按照A规则存储，同样按照A规则解析，那么就能显示正确的文本符号。反之，按照A规则存储，再按照B规则解析，就会导致乱码现象。

编码:字符(能看懂的)--字节(看不懂的)

解码:字节(看不懂的)-->字符(能看懂的)

* **字符编码`Character Encoding`** : 就是一套自然语言的字符与二进制数之间的对应规则。

  编码表:生活中文字和计算机中二进制的对应规则

### 字符集

* **字符集 `Charset`**：也叫编码表。是一个系统支持的所有字符的集合，包括各国家文字、标点符号、图形符号、数字等。

计算机要准确的存储和识别各种字符集符号，需要进行字符编码，一套字符集必然至少有一套字符编码。常见字符集有ASCII字符集、GBK字符集、Unicode字符集等。![](/../img/1_charset.jpg)

可见，当指定了**编码**，它所对应的**字符集**自然就指定了，所以**编码**才是我们最终要关心的。

* **ASCII字符集** ：
  * ASCII（American Standard Code for Information Interchange，美国信息交换标准代码）是基于拉丁字母的一套电脑编码系统，用于显示现代英语，主要包括控制字符（回车键、退格、换行键等）和可显示字符（英文大小写字符、阿拉伯数字和西文符号）。
  * 基本的ASCII字符集，使用7位（bits）表示一个字符，共128字符。ASCII的扩展字符集使用8位（bits）表示一个字符，共256字符，方便支持欧洲常用字符。
* **ISO-8859-1字符集**：
  * 拉丁码表，别名Latin-1，用于显示欧洲使用的语言，包括荷兰、丹麦、德语、意大利语、西班牙语等。
  * ISO-8859-1使用单字节编码，兼容ASCII编码。
* **GBxxx字符集**：
  * GB就是国标的意思，是为了显示中文而设计的一套字符集。
  * **GB2312**：简体中文码表。一个小于127的字符的意义与原来相同。但两个大于127的字符连在一起时，就表示一个汉字，这样大约可以组合了包含7000多个简体汉字，此外数学符号、罗马希腊的字母、日文的假名们都编进去了，连在ASCII里本来就有的数字、标点、字母都统统重新编了两个字节长的编码，这就是常说的"全角"字符，而原来在127号以下的那些就叫"半角"字符了。
  * **GBK**：最常用的中文码表。是在GB2312标准基础上的扩展规范，使用了双字节编码方案，共收录了21003个汉字，完全兼容GB2312标准，同时支持繁体汉字以及日韩汉字等。
  * **GB18030**：最新的中文码表。收录汉字70244个，采用多字节编码，每个字可以由1个、2个或4个字节组成。支持中国国内少数民族的文字，同时支持繁体汉字以及日韩汉字等。
* **Unicode字符集** ：
  * Unicode编码系统为表达任意语言的任意字符而设计，是业界的一种标准，也称为统一码、标准万国码。
  * 它最多使用4个字节的数字来表达每个字母、符号，或者文字。有三种编码方案，UTF-8、UTF-16和UTF-32。最为常用的UTF-8编码。
  * UTF-8编码，可以用来表示Unicode标准中任何字符，它是电子邮件、网页及其他存储或传送文字的应用中，优先采用的编码。互联网工程工作小组（IETF）要求所有互联网协议都必须支持UTF-8编码。所以，我们开发Web应用，也要使用UTF-8编码。它使用一至四个字节为每个字符编码，编码规则：
    1. 128个US-ASCII字符，只需一个字节编码。
    2. 拉丁文等字符，需要二个字节编码。 
    3. 大部分常用字（含中文），使用三个字节编码。
    4. 其他极少使用的Unicode辅助字符，使用四字节编码。

## 2.2 编码引出的问题

在IDEA中，使用`FileReader` 读取项目中的文本文件。由于IDEA的设置，都是默认的`UTF-8`编码，所以没有任何问题。但是，当读取Windows系统中创建的文本文件时，由于Windows系统的默认是GBK编码，就会出现乱码。

```java
public class ReaderDemo {
    public static void main(String[] args) throws IOException {
        FileReader fileReader = new FileReader("E:\\File_GBK.txt");
        int read;
        while ((read = fileReader.read()) != -1) {
            System.out.print((char)read);
        }
        fileReader.close();
    }
}
输出结果：
���
```

那么如何读取GBK编码的文件呢？ 

## 2.3 InputStreamReader类  

转换流`java.io.InputStreamReader`，是Reader的子类，是从字节流到字符流的桥梁。它读取字节，并使用指定的字符集将其解码为字符。它的字符集可以由名称指定，也可以接受平台的默认字符集。 

### 构造方法

* `InputStreamReader(InputStream in)`: 创建一个使用默认字符集的字符流。 
* `InputStreamReader(InputStream in, String charsetName)`: 创建一个指定字符集的字符流。

构造举例，代码如下： 

```java
InputStreamReader isr = new InputStreamReader(new FileInputStream("in.txt"));
InputStreamReader isr2 = new InputStreamReader(new FileInputStream("in.txt") , "GBK");
```

### 指定编码读取

```java
public class ReaderDemo2 {
    public static void main(String[] args) throws IOException {
      	// 定义文件路径,文件为gbk编码
        String FileName = "E:\\file_gbk.txt";
      	// 创建流对象,默认UTF8编码
        InputStreamReader isr = new InputStreamReader(new FileInputStream(FileName));
      	// 创建流对象,指定GBK编码
        InputStreamReader isr2 = new InputStreamReader(new FileInputStream(FileName) , "GBK");
		// 定义变量,保存字符
        int read;
      	// 使用默认编码字符流读取,乱码
        while ((read = isr.read()) != -1) {
            System.out.print((char)read); // ��Һ�
        }
        isr.close();
      
      	// 使用指定编码字符流读取,正常解析
        while ((read = isr2.read()) != -1) {
            System.out.print((char)read);// 大家好
        }
        isr2.close();
    }
}
```

## 2.4 OutputStreamWriter类

转换流`java.io.OutputStreamWriter` ，是Writer的子类，是从字符流到字节流的桥梁。使用指定的字符集将字符编码为字节。它的字符集可以由名称指定，也可以接受平台的默认字符集。 

### 构造方法

- `OutputStreamWriter(OutputStream in)`: 创建一个使用默认字符集的字符流。 
- `OutputStreamWriter(OutputStream in, String charsetName)`: 创建一个指定字符集的字符流。

构造举例，代码如下： 

```java
OutputStreamWriter isr = new OutputStreamWriter(new FileOutputStream("out.txt"));
OutputStreamWriter isr2 = new OutputStreamWriter(new FileOutputStream("out.txt") , "GBK");
```

### 指定编码写出

```java
public class OutputDemo {
    public static void main(String[] args) throws IOException {
      	// 定义文件路径
        String FileName = "E:\\out.txt";
      	// 创建流对象,默认UTF8编码
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream(FileName));
        // 写出数据
      	osw.write("你好"); // 保存为6个字节
        osw.close();
      	
		// 定义文件路径
		String FileName2 = "E:\\out2.txt";
     	// 创建流对象,指定GBK编码
        OutputStreamWriter osw2 = new OutputStreamWriter(new FileOutputStream(FileName2),"GBK");
        // 写出数据
      	osw2.write("你好");// 保存为4个字节
        osw2.close();
    }
}
```

### 转换流理解图解

**转换流是字节与字符间的桥梁！**![](/../img/2_zhuanhuan.jpg)

## 2.5 练习：转换文件编码

将GBK编码的文本文件，转换为UTF-8编码的文本文件。

### 案例分析

1. 指定GBK编码的转换流，读取文本文件。
2. 使用UTF-8编码的转换流，写出文本文件。

### 案例实现

```java
public class TransDemo {
   public static void main(String[] args) {      
    	// 1.定义文件路径
     	String srcFile = "file_gbk.txt";
        String destFile = "file_utf8.txt";
		// 2.创建流对象
    	// 2.1 转换输入流,指定GBK编码
        InputStreamReader isr = new InputStreamReader(new FileInputStream(srcFile) , "GBK");
    	// 2.2 转换输出流,默认utf8编码
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream(destFile));
		// 3.读写数据
    	// 3.1 定义数组
        char[] cbuf = new char[1024];
    	// 3.2 定义长度
        int len;
    	// 3.3 循环读取
        while ((len = isr.read(cbuf))!=-1) {
            // 循环写出
          	osw.write(cbuf,0,len);
        }
    	// 4.释放资源
        osw.close();
        isr.close();
  	}
}
```

# 3. 序列化

## 3.1 概述

Java 提供了一种对象**序列化**的机制。用一个字节序列可以表示一个对象，该字节序列包含该`对象的数据`、`对象的类型`和`对象中存储的属性`等信息。字节序列写出到文件之后，相当于文件中**持久保存**了一个对象的信息。 

反之，该字节序列还可以从文件中读取回来，重构对象，对它进行**反序列化**。`对象的数据`、`对象的类型`和`对象中存储的数据`信息，都可以用来在内存中创建对象。看图理解序列化： ![](/../img/3_xuliehua.jpg)

## 3.2 ObjectOutputStream类

`java.io.ObjectOutputStream ` 类，将Java对象的原始数据类型写出到文件,实现对象的持久存储。

### 构造方法

* `public ObjectOutputStream(OutputStream out) `： 创建一个指定OutputStream的ObjectOutputStream。

构造举例，代码如下：  

```java
FileOutputStream fileOut = new FileOutputStream("employee.txt");
ObjectOutputStream out = new ObjectOutputStream(fileOut);
```

### 序列化操作

1. 一个对象要想序列化，必须满足两个条件:

* 该类必须实现`java.io.Serializable ` 接口，`Serializable` 是一个标记接口，不实现此接口的类将不会使任何状态序列化或反序列化，会抛出`NotSerializableException` 。
* 该类的所有属性必须是可序列化的。如果有一个属性不需要可序列化的，则该属性必须注明是瞬态的，使用`transient` 关键字修饰。

```java
public class Employee implements java.io.Serializable {
    public String name;
    public String address;
    public transient int age; // transient瞬态修饰成员,不会被序列化
    public void addressCheck() {
      	System.out.println("Address  check : " + name + " -- " + address);
    }
}
```

2.写出对象方法

* `public final void writeObject (Object obj)` : 将指定的对象写出。

```java
public class SerializeDemo{
   	public static void main(String [] args)   {
    	Employee e = new Employee();
    	e.name = "zhangsan";
    	e.address = "beiqinglu";
    	e.age = 20; 
    	try {
      		// 创建序列化流对象
          ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("employee.txt"));
        	// 写出对象
        	out.writeObject(e);
        	// 释放资源
        	out.close();
        	fileOut.close();
        	System.out.println("Serialized data is saved"); // 姓名，地址被序列化，年龄没有被序列化。
        } catch(IOException i)   {
            i.printStackTrace();
        }
   	}
}
输出结果：
Serialized data is saved
```

## 3.3 ObjectInputStream类

ObjectInputStream反序列化流，将之前使用ObjectOutputStream序列化的原始数据恢复为对象。 

### 构造方法

* `public ObjectInputStream(InputStream in) `： 创建一个指定InputStream的ObjectInputStream。

### 反序列化操作1

如果能找到一个对象的class文件，我们可以进行反序列化操作，调用`ObjectInputStream`读取对象的方法：

- `public final Object readObject ()` : 读取一个对象。

```java
public class DeserializeDemo {
   public static void main(String [] args)   {
        Employee e = null;
        try {		
             // 创建反序列化流
             FileInputStream fileIn = new FileInputStream("employee.txt");
             ObjectInputStream in = new ObjectInputStream(fileIn);
             // 读取一个对象
             e = (Employee) in.readObject();
             // 释放资源
             in.close();
             fileIn.close();
        }catch(IOException i) {
             // 捕获其他异常
             i.printStackTrace();
             return;
        }catch(ClassNotFoundException c)  {
        	// 捕获类找不到异常
             System.out.println("Employee class not found");
             c.printStackTrace();
             return;
        }
        // 无异常,直接打印输出
        System.out.println("Name: " + e.name);	// zhangsan
        System.out.println("Address: " + e.address); // beiqinglu
        System.out.println("age: " + e.age); // 0
    }
}
```

**对于JVM可以反序列化对象，它必须是能够找到class文件的类。如果找不到该类的class文件，则抛出一个 `ClassNotFoundException` 异常。**  

### **反序列化操作2**

**另外，当JVM反序列化对象时，能找到class文件，但是class文件在序列化对象之后发生了修改，那么反序列化操作也会失败，抛出一个`InvalidClassException`异常。**发生这个异常的原因如下：

* 该类的序列版本号与从流中读取的类描述符的版本号不匹配 
* 该类包含未知数据类型 
* 该类没有可访问的无参数构造方法 

`Serializable` 接口给需要序列化的类，提供了一个序列版本号。`serialVersionUID` 该版本号的目的在于验证序列化的对象和对应类是否版本匹配。

```java
public class Employee implements java.io.Serializable {
     // 加入序列版本号
     private static final long serialVersionUID = 1L;
     public String name;
     public String address;
     // 添加新的属性 ,重新编译, 可以反序列化,该属性赋为默认值.
     public int eid; 

     public void addressCheck() {
         System.out.println("Address  check : " + name + " -- " + address);
     }
}
```



## 3.4 练习：序列化集合

1. 将存有多个自定义对象的集合序列化操作，保存到`list.txt`文件中。
2. 反序列化`list.txt` ，并遍历集合，打印对象信息。

### 案例分析

1. 把若干学生对象 ，保存到集合中。
2. 把集合序列化。
3. 反序列化读取时，只需要读取一次，转换为集合类型。
4. 遍历集合，可以打印所有的学生信息

### 案例实现

```java
public class SerTest {
	public static void main(String[] args) throws Exception {
		// 创建 学生对象
		Student student = new Student("老王", "laow");
		Student student2 = new Student("老张", "laoz");
		Student student3 = new Student("老李", "laol");

		ArrayList<Student> arrayList = new ArrayList<>();
		arrayList.add(student);
		arrayList.add(student2);
		arrayList.add(student3);
		// 序列化操作
		// serializ(arrayList);
		
		// 反序列化  
		ObjectInputStream ois  = new ObjectInputStream(new FileInputStream("list.txt"));
		// 读取对象,强转为ArrayList类型
		ArrayList<Student> list  = (ArrayList<Student>)ois.readObject();
		
      	for (int i = 0; i < list.size(); i++ ){
          	Student s = list.get(i);
        	System.out.println(s.getName()+"--"+ s.getPwd());
      	}
	}

	private static void serializ(ArrayList<Student> arrayList) throws Exception {
		// 创建 序列化流 
		ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("list.txt"));
		// 写出对象
		oos.writeObject(arrayList);
		// 释放资源
		oos.close();
	}
}
```


#  4. 打印流

## 4.1 概述

平时我们在控制台打印输出，是调用`print`方法和`println`方法完成的，这两个方法都来自于`java.io.PrintStream`类，该类能够方便地打印各种数据类型的值，是一种便捷的输出方式。

## 4.2 PrintStream类

### 构造方法

* `public PrintStream(String fileName)  `： 使用指定的文件名创建一个新的打印流。

构造举例，代码如下：  

```java
PrintStream ps = new PrintStream("ps.txt")；
```

### 改变打印流向

`System.out`就是`PrintStream`类型的，只不过它的流向是系统规定的，打印在控制台上。不过，既然是流对象，我们就可以玩一个"小把戏"，改变它的流向。

```java
public class PrintDemo {
    public static void main(String[] args) throws IOException {
		// 调用系统的打印流,控制台直接输出97
        System.out.println(97);
      
		// 创建打印流,指定文件的名称
        PrintStream ps = new PrintStream("ps.txt");
      	
      	// 设置系统的打印流流向,输出到ps.txt
        System.setOut(ps);
      	// 调用系统的打印流,ps.txt中输出97
        System.out.println(97);
    }
}
```

# 5. 压缩流和解压缩流

压缩流：

​	负责压缩文件或者文件夹

解压缩流：

​	负责把压缩包中的文件和文件夹解压出来

```java
/*
*   解压缩流
*
* */
public class ZipStreamDemo1 {
    public static void main(String[] args) throws IOException {

        //1.创建一个File表示要解压的压缩包
        File src = new File("D:\\aaa.zip");
        //2.创建一个File表示解压的目的地
        File dest = new File("D:\\");

        //调用方法
        unzip(src,dest);

    }

    //定义一个方法用来解压
    public static void unzip(File src,File dest) throws IOException {
        //解压的本质：把压缩包里面的每一个文件或者文件夹读取出来，按照层级拷贝到目的地当中
        //创建一个解压缩流用来读取压缩包中的数据
        ZipInputStream zip = new ZipInputStream(new FileInputStream(src));
        //要先获取到压缩包里面的每一个zipentry对象
        //表示当前在压缩包中获取到的文件或者文件夹
        ZipEntry entry;
        while((entry = zip.getNextEntry()) != null){
            System.out.println(entry);
            if(entry.isDirectory()){
                //文件夹：需要在目的地dest处创建一个同样的文件夹
                File file = new File(dest,entry.toString());
                file.mkdirs();
            }else{
                //文件：需要读取到压缩包中的文件，并把他存放到目的地dest文件夹中（按照层级目录进行存放）
                FileOutputStream fos = new FileOutputStream(new File(dest,entry.toString()));
                int b;
                while((b = zip.read()) != -1){
                    //写到目的地
                    fos.write(b);
                }
                fos.close();
                //表示在压缩包中的一个文件处理完毕了。
                zip.closeEntry();
            }
        }
        zip.close();
    }
}
```

```java
public class ZipStreamDemo2 {
    public static void main(String[] args) throws IOException {
        /*
         *   压缩流
         *      需求：
         *          把D:\\a.txt打包成一个压缩包
         * */
        //1.创建File对象表示要压缩的文件
        File src = new File("D:\\a.txt");
        //2.创建File对象表示压缩包的位置
        File dest = new File("D:\\");
        //3.调用方法用来压缩
        toZip(src,dest);
    }

    /*
    *   作用：压缩
    *   参数一：表示要压缩的文件
    *   参数二：表示压缩包的位置
    * */
    public static void toZip(File src,File dest) throws IOException {
        //1.创建压缩流关联压缩包
        ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(new File(dest,"a.zip")));
        //2.创建ZipEntry对象，表示压缩包里面的每一个文件和文件夹
        //参数：压缩包里面的路径
        ZipEntry entry = new ZipEntry("aaa\\bbb\\a.txt");
        //3.把ZipEntry对象放到压缩包当中
        zos.putNextEntry(entry);
        //4.把src文件中的数据写到压缩包当中
        FileInputStream fis = new FileInputStream(src);
        int b;
        while((b = fis.read()) != -1){
            zos.write(b);
        }
        zos.closeEntry();
        zos.close();
    }
}
```

```java
public class ZipStreamDemo3 {
    public static void main(String[] args) throws IOException {
        /*
         *   压缩流
         *      需求：
         *          把D:\\aaa文件夹压缩成一个压缩包
         * */
        //1.创建File对象表示要压缩的文件夹
        File src = new File("D:\\aaa");
        //2.创建File对象表示压缩包放在哪里（压缩包的父级路径）
        File destParent = src.getParentFile();//D:\\
        //3.创建File对象表示压缩包的路径
        File dest = new File(destParent,src.getName() + ".zip");
        //4.创建压缩流关联压缩包
        ZipOutputStream zos = new ZipOutputStream(new FileOutputStream(dest));
        //5.获取src里面的每一个文件，变成ZipEntry对象，放入到压缩包当中
        toZip(src,zos,src.getName());//aaa
        //6.释放资源
        zos.close();
    }

    /*
    *   作用：获取src里面的每一个文件，变成ZipEntry对象，放入到压缩包当中
    *   参数一：数据源
    *   参数二：压缩流
    *   参数三：压缩包内部的路径
    * */
    public static void toZip(File src,ZipOutputStream zos,String name) throws IOException {
        //1.进入src文件夹
        File[] files = src.listFiles();
        //2.遍历数组
        for (File file : files) {
            if(file.isFile()){
                //3.判断-文件，变成ZipEntry对象，放入到压缩包当中
                ZipEntry entry = new ZipEntry(name + "\\" + file.getName());//aaa\\no1\\a.txt
                zos.putNextEntry(entry);
                //读取文件中的数据，写到压缩包
                FileInputStream fis = new FileInputStream(file);
                int b;
                while((b = fis.read()) != -1){
                    zos.write(b);
                }
                fis.close();
                zos.closeEntry();
            }else{
                //4.判断-文件夹，递归
                toZip(file,zos,name + "\\" + file.getName());
                //     no1            aaa   \\   no1
            }
        }
    }
}
```

# 6. 工具包（Commons-io）

介绍：

​	Commons是apache开源基金组织提供的工具包，里面有很多帮助我们提高开发效率的API

比如：

​	StringUtils   字符串工具类

​	NumberUtils   数字工具类 

​	ArrayUtils   数组工具类  

​	RandomUtils   随机数工具类

​	DateUtils   日期工具类 

​	StopWatch   秒表工具类 

​	ClassUtils   反射工具类  

​	SystemUtils   系统工具类  

​	MapUtils   集合工具类

​	Beanutils   bean工具类

​	Commons-io io的工具类

​	等等.....

其中：Commons-io是apache开源基金组织提供的一组有关IO操作的开源工具包。

作用：提高IO流的开发效率。

使用方式：

1，新建lib文件夹

2，把第三方jar包粘贴到文件夹中

3，右键点击add as a library

代码示例：

```java
public class CommonsIODemo1 {
    public static void main(String[] args) throws IOException {
        /*
          FileUtils类
                static void copyFile(File srcFile, File destFile)                   复制文件
                static void copyDirectory(File srcDir, File destDir)                复制文件夹
                static void copyDirectoryToDirectory(File srcDir, File destDir)     复制文件夹
                static void deleteDirectory(File directory)                         删除文件夹
                static void cleanDirectory(File directory)                          清空文件夹
                static String readFileToString(File file, Charset encoding)         读取文件中的数据变成成字符串
                static void write(File file, CharSequence data, String encoding)    写出数据

            IOUtils类
                public static int copy(InputStream input, OutputStream output)      复制文件
                public static int copyLarge(Reader input, Writer output)            复制大文件
                public static String readLines(Reader input)                        读取数据
                public static void write(String data, OutputStream output)          写出数据
         */


        /* File src = new File("myio\\a.txt");
        File dest = new File("myio\\copy.txt");
        FileUtils.copyFile(src,dest);*/


        /*File src = new File("D:\\aaa");
        File dest = new File("D:\\bbb");
        FileUtils.copyDirectoryToDirectory(src,dest);*/

        /*File src = new File("D:\\bbb");
        FileUtils.cleanDirectory(src);*/



    }
}

```

# 7. 工具包（hutool）

介绍：

​	Commons是国人开发的开源工具包，里面有很多帮助我们提高开发效率的API

比如：

​	DateUtil  日期时间工具类 

​	TimeInterval  计时器工具类 

​	StrUtil  字符串工具类

​	HexUtil   16进制工具类

​	HashUtil   Hash算法类

​	ObjectUtil  对象工具类

​	ReflectUtil   反射工具类

​	TypeUtil  泛型类型工具类

​	PageUtil  分页工具类

​	NumberUtil  数字工具类

使用方式：

1，新建lib文件夹

2，把第三方jar包粘贴到文件夹中

3，右键点击add as a library

代码示例：

```java
public class Test1 {
    public static void main(String[] args) {
    /*
        FileUtil类:
                file：根据参数创建一个file对象
                touch：根据参数创建文件

                writeLines：把集合中的数据写出到文件中，覆盖模式。
                appendLines：把集合中的数据写出到文件中，续写模式。
                readLines：指定字符编码，把文件中的数据，读到集合中。
                readUtf8Lines：按照UTF-8的形式，把文件中的数据，读到集合中

                copy：拷贝文件或者文件夹
    */


       /* File file1 = FileUtil.file("D:\\", "aaa", "bbb", "a.txt");
        System.out.println(file1);//D:\aaa\bbb\a.txt

        File touch = FileUtil.touch(file1);
        System.out.println(touch);


        ArrayList<String> list = new ArrayList<>();
        list.add("aaa");
        list.add("aaa");
        list.add("aaa");

        File file2 = FileUtil.writeLines(list, "D:\\a.txt", "UTF-8");
        System.out.println(file2);*/

      /*  ArrayList<String> list = new ArrayList<>();
        list.add("aaa");
        list.add("aaa");
        list.add("aaa");
        File file3 = FileUtil.appendLines(list, "D:\\a.txt", "UTF-8");
        System.out.println(file3);*/
        List<String> list = FileUtil.readLines("D:\\a.txt", "UTF-8");
        System.out.println(list);
    }
}
```

# 综合练习

爬取数据，并读取处理，写入指定的文件中，生成目标的假数据

```java
package com.itheima.test_demo1;
//爬取数据

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class test1 {

    public static void main(String[] args) throws IOException {
        String FamilynameNet="https://hanyu.baidu.com/shici/detail?from=kg1&highlight=&pid=0b2f26d4c0ddb3ee693fdb1137ee1b0d&srcid=51369";
        String BoyNameNet="http://www.nejiaoyu.com/nanhaiqiming/8465.html";
        String GirlNameNet="http://www.nejiaoyu.com/nvhaiqiming/7744.html";

//        爬取数据
        String s = webCrawler(FamilynameNet);
        String s1 = webCrawler(BoyNameNet);
        String s2 = webCrawler(GirlNameNet);



//        通过正则表达式进行获取
          ArrayList<String> familyname=getData(s,"(.{4})((，|。))",1);
//          此处要求是中文且为两个字符，之后是以顿号或者句号结尾的。
          ArrayList<String> Boyname=getData(s1,"([\\u4e00-\\u9fa5·]{2})((、|。))",1);
          ArrayList<String> Girlname=getData(s2,"([\\u4e00-\\u9fa5·]{2})((、|。))",1);

          System.out.println(familyname);
          System.out.println(Boyname);
          System.out.println(Girlname );

//          数据的处理
        ArrayList<String> myfamilyname=new ArrayList<>();
        for (String s3 : familyname) {
            for (int i = 0; i < s3.length(); i++) {
                String s4= String.valueOf(s3.charAt(i));
                myfamilyname.add(s4);
            }
        }
//        检查数据的维度
        System.out.println(myfamilyname);
        System.out.println(myfamilyname.size());
        System.out.println(Boyname.size());
        System.out.println(Girlname.size());
        ArrayList<ArrayList> mylist=new ArrayList<>();
        mylist.add(Boyname);
        mylist.add(Girlname);

        ArrayList<ArrayList> infos = getInfos(myfamilyname, mylist, 100, 100);
        ArrayList<String> girl_info=infos.get(1);
        ArrayList<String> boy_info=infos.get(0);
        System.out.println(boy_info);
        System.out.println(girl_info);
        ArrayList<ArrayList> MyInfos=GetMyinfos(infos);
        ArrayList<String > Boy_info=MyInfos.get(1);
        ArrayList<String > Girl_info=MyInfos.get(0);
        System.out.println(Boy_info);
        System.out.println(Girl_info);
        BufferedWriter bw_b=new BufferedWriter(new FileWriter("C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src\\com\\itheima\\test3\\data\\Boy.txt"));
        BufferedWriter bw_g=new BufferedWriter(new FileWriter("C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src\\com\\itheima\\test3\\data\\girl.txt"));
        for (String s3 : Boy_info) {
            bw_b.write(s3);
            bw_b.newLine();
            bw_b.flush();
        }
        bw_b.close();
        for (String s4 : Girl_info) {
            bw_g.write(s4);
            bw_g.newLine();
            bw_g.flush();
        }
        bw_g.close();
    }

    private static ArrayList<ArrayList> GetMyinfos(ArrayList<ArrayList> infos) {
        ArrayList<String> my_list_name=new ArrayList<>();
        ArrayList<String> my_list_name0=new ArrayList<>();
        ArrayList<ArrayList> my_list_name1=new ArrayList<>();
        ArrayList<String> girl_info=infos.get(1);
        ArrayList<String> boy_info=infos.get(0);
        Random rdage=new Random();
        for (String s : girl_info) {
            my_list_name0.add(s+"-女-"+(rdage.nextInt(9)+18));
        }
        my_list_name1.add(my_list_name0);

        for (String s : boy_info) {
            my_list_name.add(s+"-男-"+(rdage.nextInt(9)+18));
        }
        my_list_name1.add(my_list_name);
        return my_list_name1;
    }

    //随机得到男生和女生的姓名
    public static ArrayList<ArrayList> getInfos(ArrayList<String> myfamilyname,ArrayList<ArrayList> mylist,int boy,int girl) {
        Random mrand = new Random();
        Random listrand = new Random();
        Random listrand0 = new Random();
        ArrayList<ArrayList> mydata=new ArrayList<>();

        HashSet<String> design_name_boy = new HashSet<>();
        HashSet<String> design_name_girl = new HashSet<>();
        while (design_name_boy.size() != boy) {
            ArrayList list = mylist.get(0);
            int nextInt1 = listrand.nextInt(list.size());
            int nextInt2 = listrand0.nextInt(myfamilyname.size());
            String peoplename = new String(myfamilyname.get(nextInt2) + list.get(nextInt1));
            System.out.println(peoplename);
            design_name_boy.add(peoplename);

        }
        while (design_name_girl.size() != girl) {
            ArrayList list = mylist.get(1);
            int nextInt1 = listrand.nextInt(list.size());
            int nextInt2 = listrand0.nextInt(myfamilyname.size());
            String peoplename = new String(myfamilyname.get(nextInt2) + list.get(nextInt1));
            System.out.println(peoplename);
            design_name_girl.add(peoplename);

        }
        List<String> collect = design_name_boy.stream().collect(Collectors.toList());
        List<String> collect1 = design_name_girl.stream().collect(Collectors.toList());
        mydata.add((ArrayList) collect);
        mydata.add((ArrayList) collect1);
        return mydata;
    }

//    对男生和女生的信息进行补充


    public  static String webCrawler(String net) throws IOException {
        StringBuilder SB=new StringBuilder();
        URL url=new URL(net);
        URLConnection conn= url.openConnection();
        InputStreamReader isr=new InputStreamReader(conn.getInputStream());
        int ch;
        while((ch=isr.read())!=-1){
            SB.append((char)ch);
        }
        isr.close();
        return SB.toString();
    }
    public static ArrayList<String> getData(String s,String st,int x){
        ArrayList<String> list=new ArrayList<>();
        Pattern compile = Pattern.compile(st);
        Matcher matcher = compile.matcher(s);
        while(matcher.find()){
            String group = matcher.group(x);
//            System.out.println(group);
            list.add(group);
        }
        return list;
    }
}

```

使用Hutool包生成假数据：

```java
package com.itheima.test_demo1;
//爬取数据

import cn.hutool.core.io.FileUtil;
import cn.hutool.core.io.file.FileWriter;
import cn.hutool.core.util.ReUtil;
import cn.hutool.http.HttpUtil;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class test2_hutool {

    public static void main(String[] args) throws IOException {
        String FamilynameNet="https://hanyu.baidu.com/shici/detail?from=kg1&highlight=&pid=0b2f26d4c0ddb3ee693fdb1137ee1b0d&srcid=51369";
        String BoyNameNet="http://www.nejiaoyu.com/nanhaiqiming/8465.html";
        String GirlNameNet="http://www.nejiaoyu.com/nvhaiqiming/7744.html";
        //请求列表页
        String listContent = HttpUtil.get(FamilynameNet);
        //请求列表
        // 使用正则获取所有标题
        List<String> Family_name = ReUtil.findAll("(.{4})((，|。))", listContent, 1);
        List<String> Boyname=ReUtil.findAll("([\\u4e00-\\u9fa5·]{2})((、|。))", HttpUtil.get(BoyNameNet), 1);
        List<String> Girlname=ReUtil.findAll("([\\u4e00-\\u9fa5·]{2})((、|。))", HttpUtil.get(GirlNameNet), 1);
//        利用set 集合去重
        Set<String> collect = Boyname.stream().collect(Collectors.toSet());
        Set<String> collect1 = Girlname.stream().collect(Collectors.toSet());
        List<String> collect2 = collect.stream().collect(Collectors.toList());
        List<String> list = collect1.stream().collect(Collectors.toList());
//        System.out.println(collect2);
//        System.out.println(list);
        ArrayList<ArrayList> mylist=new ArrayList<>();
        mylist.add((ArrayList) collect2);
        mylist.add((ArrayList) list);
        System.out.println(Family_name);
        ArrayList<String> myfamilyname=new ArrayList<>();
        for (String s3 : Family_name) {
            for (int i = 0; i < s3.length(); i++) {
                String s4= String.valueOf(s3.charAt(i));
                myfamilyname.add(s4);
            }
        }
        ArrayList<ArrayList> infos = getInfos((ArrayList<String>) myfamilyname , mylist, 100, 100);
        ArrayList<ArrayList> MyInfos=GetMyinfos(infos);
        ArrayList<String > Boy_info=MyInfos.get(1);
        ArrayList<String > Girl_info=MyInfos.get(0);
        System.out.println(Boy_info);
        System.out.println(Girl_info);
//        使用hutool包写出
        FileUtil.writeLines(Boy_info,"C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src\\com\\itheima\\test3\\data\\hutool_boy_1.txt","UTF-8");
        FileUtil.writeLines(Girl_info,"C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src\\com\\itheima\\test3\\data\\hutool_girl_1.txt","UTF-8");
    }

    private static ArrayList<ArrayList> GetMyinfos(ArrayList<ArrayList> infos) {
        ArrayList<String> my_list_name=new ArrayList<>();
        ArrayList<String> my_list_name0=new ArrayList<>();
        ArrayList<ArrayList> my_list_name1=new ArrayList<>();
        ArrayList<String> girl_info=infos.get(1);
        ArrayList<String> boy_info=infos.get(0);
        Random rdage=new Random();
        for (String s : girl_info) {
            my_list_name0.add(s+"-女-"+(rdage.nextInt(9)+18));
        }
        my_list_name1.add(my_list_name0);

        for (String s : boy_info) {
            my_list_name.add(s+"-男-"+(rdage.nextInt(9)+18));
        }
        my_list_name1.add(my_list_name);
        return my_list_name1;
    }

    //随机得到男生和女生的姓名
    public static ArrayList<ArrayList> getInfos(ArrayList<String> myfamilyname,ArrayList<ArrayList> mylist,int boy,int girl) {
        Random mrand = new Random();
        Random listrand = new Random();
        Random listrand0 = new Random();
        ArrayList<ArrayList> mydata=new ArrayList<>();

        HashSet<String> design_name_boy = new HashSet<>();
        HashSet<String> design_name_girl = new HashSet<>();
        while (design_name_boy.size() != boy) {
            ArrayList list = mylist.get(0);
            int nextInt1 = listrand.nextInt(list.size());
            int nextInt2 = listrand0.nextInt(myfamilyname.size());
            String peoplename = new String(myfamilyname.get(nextInt2) + list.get(nextInt1));

            design_name_boy.add(peoplename);

        }
        while (design_name_girl.size() != girl) {
            ArrayList list = mylist.get(1);
            int nextInt1 = listrand.nextInt(list.size());
            int nextInt2 = listrand0.nextInt(myfamilyname.size());
            String peoplename = new String(myfamilyname.get(nextInt2) + list.get(nextInt1));

            design_name_girl.add(peoplename);

        }
        List<String> collect = design_name_boy.stream().collect(Collectors.toList());
        List<String> collect1 = design_name_girl.stream().collect(Collectors.toList());
        mydata.add((ArrayList) collect);
        mydata.add((ArrayList) collect1);
        return mydata;
    }

}
```

##### 随机点名器（随机权重的方法）

```JAVA
package com.itheima.test_demo1;

import cn.hutool.core.io.FileUtil;

import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class test_dianming_3 {
    public static void main(String[] args) {
        ArrayList<String> strings_name = (ArrayList<String>) FileUtil.readLines("C:\\Users\\Administrator\\IdeaProjects\\mystudy\\src\\com\\itheima\\test3\\data\\hutool_boy_1.txt", "UTF-8");
        ArrayList<student> students_list=new ArrayList<>();
        for (String s : strings_name) {
            students_list.add(new student(s.split("-")[0],s.split("-")[1],Integer.parseInt(s.split("-")[2]),Double.parseDouble(s.split("-")[3])));
        }
        System.out.println(students_list);
        for (int i = 0; i < 16; i++) {
            ArrayList<student> students = randomWeight(students_list);
            System.out.println(students);
            System.out.println("---------------------------------------");
        }



    }

    public static ArrayList<student> randomWeight(ArrayList<student> students_list){
        double sum_wei=0;
        for (student student : students_list) {
            sum_wei+=student.getX();
        }
        System.out.println(sum_wei);
        double[] arr=new double[students_list.size()];
        int i=0;
        for (student student : students_list) {
            double v = student.getX() / sum_wei;
            arr[i]=v;
            i++;
        }
        System.out.println(Arrays.toString(arr));
        for (int i1 = 1; i1 < arr.length; i1++) {
            arr[i1]=arr[i1]+arr[i1-1];
        }
//        随机抽取
//        获取一个一个0.0-0.1之间的随机数
        double random = Math.random();
        System.out.println(random);
//        判断此时的random的所在的位置
        int index = Arrays.binarySearch(arr, random);
        int insert=-index-1;
//        插入点就是我们的最终的索引
//        修改当前的学生的权重
        double v = students_list.get(insert).getX() / 2;
        students_list.get(insert).setX(v);

        return students_list;
    }
    
}
```

# 多线程：

## 俩个概念

并发：在同一个时刻，有多个指令在单个的CPU上面交替的进行，多线程交替的进行

并行：在同一个时刻，有多个指令在多个CPU上同时执行，多线程同时进行。

## 多线程的实现方式

### 不需要获取结果

#### 继承Thred类的方式进行实现

```java
将类声明为 Thread 的子类。该子类应重写 Thread 类的 run 方法。接下来可以分配并启动该子类的实例。
```

```java
public class Threaddemo extends Thread{
//    多线程的启动方式
//    自己实现一个继承Thread并且重写这个润的方法
    
    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.println(getname()+"hello world");
        }
    }
}

```

TEST

```JAVA
public class test {

    public static void main(String[] args) {
//    多线程的启动方式
//    自己实现一个并重写run的方法，并创建对象启动线程
//
        Threaddemo my=new Threaddemo();
        Threaddemo my1=new Threaddemo();

        my.setName("线程一");
        my1.setName("线程二");

        my.start();

        my1.start();

    }
}

```

注意：start()方法的调用后并不是立即执行多线程代码，而是使得该线程变为可运行态（Runnable），什么时候运行是由操作系统决定的。
从程序运行的结果可以发现，多线程程序是乱序执行。因此，只有乱序执行的代码才有必要设计为多线程。
Thread.sleep()方法调用目的是不让当前线程独自霸占该进程所获取的CPU资源，以留出一定时间给其他线程执行的机会。
实际上所有的多线程代码执行顺序都是不确定的，每次执行的结果都是随机的。
但是start方法重复调用的话，会出现java.lang.IllegalThreadStateException异常。

#### 实现Runnable接口的方式实现

```java
package com.itheima.Threadstudy;

public class Threaddemo2 implements Runnable{
    @Override
    public void run() {
        for (int i = 0; i < 20; i++) {
            Thread t=Thread.currentThread();//获取到我们的当前的线程的对象
            System.out.println(t.getName()+"黄豆超甜");
        }
    }
}

```

test

```java
package com.itheima.Threadstudy;

public class test2 {

    public static void main(String[] args) {
//    多线程的启动方式
//    自己实现一个并重写run的方法
//    需要我们先创建实现接口的对象，并将其作为参数传入我们的Thread的对象中
//        使用创建Thread的对象去启动我们的线程

      Threaddemo2 p=new Threaddemo2();  //我们的任务对象
      Thread my=new Thread(p);
      Thread my2=new Thread(p);
      my.setName("线程1");
      my2.setName("线程2");
//      开启线程
      my.start();
      my2.start();

    }
}

```

Thread2类通过实现Runnable接口，使得该类有了多线程类的特征。run（）方法是多线程程序的一个约定。所有的多线程代码都在run方法里面。Thread类实际上也是实现了Runnable接口的类。
在启动的多线程的时候，需要先通过Thread类的构造方法Thread(Runnable target) 构造出对象，然后调用Thread对象的start()方法来运行多线程代码。
实际上所有的多线程代码都是通过运行Thread的start()方法来运行的。因此，不管是扩展Thread类还是实现Runnable接口来实现多线程，最终还是通过Thread的对象的API来控制线程的，熟悉Thread类的API是进行多线程编程的基础。

### 需要获取结果

#### 使用Callable接口和Future接口的方式进行

```java
package com.itheima.Threadstudy;

import java.util.concurrent.Callable;

public class Thread_demo3 implements Callable<Integer> {


    @Override

    public Integer call() throws Exception {
        int sum=0;
        for (int i = 0; i < 10; i++) sum = sum + i;
        return sum;
    }
}
```

```java

public class test3 {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
//        多线程的第三种是实现的方法
//可以获取到我们呢多线程的运行的结果
//        创建一个类的Callable的Callable的接口得类
//        重写这个类中的call的方法
//        创建一个实现callable的类的对象(表示多线程执行的对象
//        创建一个FutureTask的对象.作用管理多线程的运行的结果
//        创建Thread的对象表示线程
        Thread_demo3 mt=new Thread_demo3();
//        FutureTask的对象.作用管理多线程的运行的结果
        FutureTask<Integer> ft=new FutureTask<>(mt);

        Thread T1=new Thread(ft);
        T1.start();
//        获取多线程的运行的结果
        Integer integer = ft.get();
        System.out.println(integer);

    }
}

```

### 1.4实现多线程方式一：继承Thread类【应用】

- 方法介绍

  | 方法名       | 说明                                        |
  | ------------ | ------------------------------------------- |
  | void run()   | 在线程开启后，此方法将被调用执行            |
  | void start() | 使此线程开始执行，Java虚拟机会调用run方法() |

- 实现步骤

  - 定义一个类MyThread继承Thread类
  - 在MyThread类中重写run()方法
  - 创建MyThread类的对象
  - 启动线程

- 代码演示

  ```java
  public class MyThread extends Thread {
      @Override
      public void run() {
          for(int i=0; i<100; i++) {
              System.out.println(i);
          }
      }
  }
  public class MyThreadDemo {
      public static void main(String[] args) {
          MyThread my1 = new MyThread();
          MyThread my2 = new MyThread();
  
  //        my1.run();
  //        my2.run();
  
          //void start() 导致此线程开始执行; Java虚拟机调用此线程的run方法
          my1.start();
          my2.start();
      }
  }
  ```

- 两个小问题

  - 为什么要重写run()方法？

    因为run()是用来封装被线程执行的代码

  - run()方法和start()方法的区别？

    run()：封装线程执行的代码，直接调用，相当于普通方法的调用

    start()：启动线程；然后由JVM调用此线程的run()方法

### 1.5实现多线程方式二：实现Runnable接口【应用】

- Thread构造方法

  | 方法名                               | 说明                   |
  | ------------------------------------ | ---------------------- |
  | Thread(Runnable target)              | 分配一个新的Thread对象 |
  | Thread(Runnable target, String name) | 分配一个新的Thread对象 |

- 实现步骤

  - 定义一个类MyRunnable实现Runnable接口
  - 在MyRunnable类中重写run()方法
  - 创建MyRunnable类的对象
  - 创建Thread类的对象，把MyRunnable对象作为构造方法的参数
  - 启动线程

- 代码演示

  ```java
  public class MyRunnable implements Runnable {
      @Override
      public void run() {
          for(int i=0; i<100; i++) {
              System.out.println(Thread.currentThread().getName()+":"+i);
          }
      }
  }
  public class MyRunnableDemo {
      public static void main(String[] args) {
          //创建MyRunnable类的对象
          MyRunnable my = new MyRunnable();
  
          //创建Thread类的对象，把MyRunnable对象作为构造方法的参数
          //Thread(Runnable target)
  //        Thread t1 = new Thread(my);
  //        Thread t2 = new Thread(my);
          //Thread(Runnable target, String name)
          Thread t1 = new Thread(my,"坦克");
          Thread t2 = new Thread(my,"飞机");
  
          //启动线程
          t1.start();
          t2.start();
      }
  }
  ```

### 1.6实现多线程方式三: 实现Callable接口【应用】

+ 方法介绍

  | 方法名                           | 说明                                               |
  | -------------------------------- | -------------------------------------------------- |
  | V call()                         | 计算结果，如果无法计算结果，则抛出一个异常         |
  | FutureTask(Callable<V> callable) | 创建一个 FutureTask，一旦运行就执行给定的 Callable |
  | V get()                          | 如有必要，等待计算完成，然后获取其结果             |

+ 实现步骤

  + 定义一个类MyCallable实现Callable接口
  + 在MyCallable类中重写call()方法
  + 创建MyCallable类的对象
  + 创建Future的实现类FutureTask对象，把MyCallable对象作为构造方法的参数
  + 创建Thread类的对象，把FutureTask对象作为构造方法的参数
  + 启动线程
  + 再调用get方法，就可以获取线程结束之后的结果。

+ 代码演示

  ```java
  public class MyCallable implements Callable<String> {
      @Override
      public String call() throws Exception {
          for (int i = 0; i < 100; i++) {
              System.out.println("跟女孩表白" + i);
          }
          //返回值就表示线程运行完毕之后的结果
          return "答应";
      }
  }
  public class Demo {
      public static void main(String[] args) throws ExecutionException, InterruptedException {
          //线程开启之后需要执行里面的call方法
          MyCallable mc = new MyCallable();
  
          //Thread t1 = new Thread(mc);
  
          //可以获取线程执行完毕之后的结果.也可以作为参数传递给Thread对象
          FutureTask<String> ft = new FutureTask<>(mc);
  
          //创建线程对象
          Thread t1 = new Thread(ft);
  
          String s = ft.get();
          //开启线程
          t1.start();
  
          //String s = ft.get();
          System.out.println(s);
      }
  }
  ```

+ 三种实现方式的对比

  + 实现Runnable、Callable接口
    + 好处: 扩展性强，实现该接口的同时还可以继承其他的类
    + 缺点: 编程相对复杂，不能直接使用Thread类中的方法
  + 继承Thread类
    + 好处: 编程比较简单，可以直接使用Thread类中的方法
    + 缺点: 可以扩展性较差，不能再继承其他的类

### 1.7设置和获取线程名称【应用】

- 方法介绍

  | 方法名                     | 说明                               |
  | -------------------------- | ---------------------------------- |
  | void  setName(String name) | 将此线程的名称更改为等于参数name   |
  | String  getName()          | 返回此线程的名称                   |
  | Thread  currentThread()    | 返回对当前正在执行的线程对象的引用 |

- 代码演示

  ```java
  public class MyThread extends Thread {
      public MyThread() {}
      public MyThread(String name) {
          super(name);
      }
  
      @Override
      public void run() {
          for (int i = 0; i < 100; i++) {
              System.out.println(getName()+":"+i);
          }
      }
  }
  public class MyThreadDemo {
      public static void main(String[] args) {
          MyThread my1 = new MyThread();
          MyThread my2 = new MyThread();
  
          //void setName(String name)：将此线程的名称更改为等于参数 name
          my1.setName("高铁");
          my2.setName("飞机");
  
          //Thread(String name)
          MyThread my1 = new MyThread("高铁");
          MyThread my2 = new MyThread("飞机");
  
          my1.start();
          my2.start();
  
          //static Thread currentThread() 返回对当前正在执行的线程对象的引用
          System.out.println(Thread.currentThread().getName());
          //实质上现在我们获取到的是我们的main方法的线程
          
      }
  }
  ```

### 1.8线程休眠【应用】

+ 相关方法

  | 方法名                         | 说明                                             |
  | ------------------------------ | ------------------------------------------------ |
  | static void sleep(long millis) | 使当前正在执行的线程停留（暂停执行）指定的毫秒数 |

+ 代码演示

  ```java
  public class MyRunnable implements Runnable {
      @Override
      public void run() {
          for (int i = 0; i < 100; i++) {
              try {
                  Thread.sleep(100);
              } catch (InterruptedException e) {
                  e.printStackTrace();
              }
  
              System.out.println(Thread.currentThread().getName() + "---" + i);
          }
      }
  }
  public class Demo {
      public static void main(String[] args) throws InterruptedException {
          /*System.out.println("睡觉前");
          Thread.sleep(3000);
          System.out.println("睡醒了");*/
  
          MyRunnable mr = new MyRunnable();
  
          Thread t1 = new Thread(mr);
          Thread t2 = new Thread(mr);
  
          t1.start();
          t2.start();
      }
  }
  ```

### 1.9线程优先级【应用】

- 线程调度

  - 两种调度方式

    - 分时调度模型：所有线程轮流使用 CPU 的使用权，平均分配每个线程占用 CPU 的时间片
    - 抢占式调度模型：优先让优先级高的线程使用 CPU，如果线程的优先级相同，那么会随机选择一个，优先级高的线程获取的 CPU 时间片相对多一些

  - Java使用的是抢占式调度模型

  - 随机性

    假如计算机只有一个 CPU，那么 CPU 在某一个时刻只能执行一条指令，线程只有得到CPU时间片，也就是使用权，才可以执行指令。所以说多线程程序的执行是有随机性，因为谁抢到CPU的使用权是不一定的

    ![05_多线程示例图](/../img/05_多线程示例图.png)

- 优先级相关方法

  | 方法名                                  | 说明                                                         |
  | --------------------------------------- | ------------------------------------------------------------ |
  | final int getPriority()                 | 返回此线程的优先级                                           |
  | final void setPriority(int newPriority) | 更改此线程的优先级线程默认优先级是5；线程优先级的范围是：1-10 |

- 代码演示

  ```java
  public class MyCallable implements Callable<String> {
      @Override
      public String call() throws Exception {
          for (int i = 0; i < 100; i++) {
              System.out.println(Thread.currentThread().getName() + "---" + i);
          }
          return "线程执行完毕了";
      }
  }
  public class Demo {
      public static void main(String[] args) {
          //优先级: 1 - 10 默认值:5
          MyCallable mc = new MyCallable();
  
          FutureTask<String> ft = new FutureTask<>(mc);
  
          Thread t1 = new Thread(ft);
          t1.setName("飞机");
          t1.setPriority(10);
          //System.out.println(t1.getPriority());//5
          t1.start();
          MyCallable mc2 = new MyCallable();
          FutureTask<String> ft2 = new FutureTask<>(mc2);
          Thread t2 = new Thread(ft2);
          t2.setName("坦克");
          t2.setPriority(1);
          //System.out.println(t2.getPriority());//5
          t2.start();
      }
  }
  ```

### 1.10守护线程【应用】

- 相关方法

  | 方法名                     | 说明                                                         |
  | -------------------------- | ------------------------------------------------------------ |
  | void setDaemon(boolean on) | 将此线程标记为守护线程，当运行的线程都是守护线程时，Java虚拟机将退出 |

- 代码演示

  ```java
  public class MyThread1 extends Thread {
      @Override
      public void run() {
          for (int i = 0; i < 10; i++) {
              System.out.println(getName() + "---" + i);
          }
      }
  }
  public class MyThread2 extends Thread {
      @Override
      public void run() {
          for (int i = 0; i < 100; i++) {
              System.out.println(getName() + "---" + i);
          }
      }
  }
  public class Demo {
      public static void main(String[] args) {
          MyThread1 t1 = new MyThread1();
          MyThread2 t2 = new MyThread2();
  
          t1.setName("女神");
          t2.setName("备胎");
  
          //把第二个线程设置为守护线程
          //当当前的线程结束的时候，这个守护线程也会结束  
          
          //当普通线程执行完之后,那么守护线程也没有继续运行下去的必要了.
          t2.setDaemon(true);
  
          t1.start();
          t2.start();
      }
  }
  ```

<img src="/../assets/image-20230727114943567.png" alt="image-20230727114943567" style="zoom:80%;" />

**设置的马里奥的优先级高于黄豆豆的优先级，经过运行的时候，就会发现马里奥的进程提前完成。**

<img src="/../assets/image-20230727115659360.png" alt="image-20230727115659360" style="zoom:80%;" />

当别的线程结束的时候，我们的守护线程也会逐渐结束，而不是继续完成其应该完成的所有的安排

##   线程的生命周期

## ![image-20230727125244386](/../assets/image-20230727125244386.png) 

## 2.线程同步

### 2.1卖票【应用】

- 案例需求

  某电影院目前正在上映国产大片，共有100张票，而它有3个窗口卖票，请设计一个程序模拟该电影院卖票

- 实现步骤

  - 定义一个类SellTicket实现Runnable接口，里面定义一个成员变量：private int tickets = 100;

  - 在SellTicket类中重写run()方法实现卖票，代码步骤如下

  - 判断票数大于0，就卖票，并告知是哪个窗口卖的
  - 卖了票之后，总票数要减1
  - 票卖没了，线程停止
  - 定义一个测试类SellTicketDemo，里面有main方法，代码步骤如下
  - 创建SellTicket类的对象
  - 创建三个Thread类的对象，把SellTicket对象作为构造方法的参数，并给出对应的窗口名称
  - 启动线程

- 代码实现

  ```java
  public class SellTicket implements Runnable {
      private int tickets = 100;
      //在SellTicket类中重写run()方法实现卖票，代码步骤如下
      @Override
      public void run() {
          while (true) {
              if(ticket <= 0){
                      //卖完了
                      break;
                  }else{
                      try {
                          Thread.sleep(100);
                      } catch (InterruptedException e) {
                          e.printStackTrace();
                      }
                      ticket--;
                      System.out.println(Thread.currentThread().getName() + "在卖票,还剩下" + ticket + "张票");
                  }
          }
      }
  }
  public class SellTicketDemo {
      public static void main(String[] args) {
          //创建SellTicket类的对象
          SellTicket st = new SellTicket();
  
          //创建三个Thread类的对象，把SellTicket对象作为构造方法的参数，并给出对应的窗口名称
          Thread t1 = new Thread(st,"窗口1");
          Thread t2 = new Thread(st,"窗口2");
          Thread t3 = new Thread(st,"窗口3");
  
          //启动线程
          t1.start();
          t2.start();
          t3.start();
      }
  }
  ```


### 2.2卖票案例的问题【理解】

- 卖票出现了问题

  - **相同的票出现了多次**

  - **出现了负数的票**

- 问题产生原因

  线程执行的随机性导致的,可能在卖票过程中丢失cpu的执行权,导致出现问题


### 2.3同步代码块解决数据安全问题【应用】

- 安全问题出现的条件

  - 是多线程环境

  - 有共享数据

  - 有多条语句操作共享数据

- 如何解决多线程安全问题呢?

  - 基本思想：让程序没有安全问题的环境

- 怎么实现呢?

  - 把多条语句操作共享数据的代码给锁起来，让任意时刻只能有一个线程执行即可

  - Java提供了同步代码块的方式来解决

- 同步代码块格式：

  ```java
  synchronized(任意对象) { 
  	多条语句操作共享数据的代码 
  }
  ```

  synchronized(任意对象)：就相当于给代码加锁了，任意对象就可以看成是一把锁

- 同步的好处和弊端  

  - 好处：解决了多线程的数据安全问题

  - 弊端：当线程很多时，因为每个线程都会去判断同步上的锁，这是很耗费资源的，无形中会降低程序的运行效率

- 代码演示

  ```java
  public class SellTicket implements Runnable {
      private int tickets = 100;
      private Object obj = new Object();
  
      @Override
      public void run() {
          while (true) {
              synchronized (obj) { // 对可能有安全问题的代码加锁,多个线程必须使用同一把锁
                  //t1进来后，就会把这段代码给锁起来
                  if (tickets > 0) {
                      try {
                          Thread.sleep(100);
                          //t1休息100毫秒
                      } catch (InterruptedException e) {
                          e.printStackTrace();
                      }
                      //窗口1正在出售第100张票
                      System.out.println(Thread.currentThread().getName() + "正在出售第" + tickets + "张票");
                      tickets--; //tickets = 99;
                  }
              }
              //t1出来了，这段代码的锁就被释放了
          }
      }
  }
  
  public class SellTicketDemo {
      public static void main(String[] args) {
          SellTicket st = new SellTicket();
  
          Thread t1 = new Thread(st, "窗口1");
          Thread t2 = new Thread(st, "窗口2");
          Thread t3 = new Thread(st, "窗口3");
  
          t1.start();
          t2.start();
          t3.start();
      }
  }
  ```

### 2.4同步方法解决数据安全问题【应用】

- 同步方法的格式

  同步方法：就是把synchronized关键字加到方法上

  ```java
  修饰符 synchronized 返回值类型 方法名(方法参数) { 
  	方法体；
  }
  ```

  同步方法的锁对象是什么呢?

  ​	this

- 静态同步方法

  同步静态方法：就是把synchronized关键字加到静态方法上

  ```java
  修饰符 static synchronized 返回值类型 方法名(方法参数) { 
  	方法体；
  }
  ```

  同步静态方法的锁对象是什么呢?

  ​	类名.class

- 代码演示

  ```java
  public class MyRunnable implements Runnable {
      private static int ticketCount = 100;
  
      @Override
      public void run() {
          while(true){
              if("窗口一".equals(Thread.currentThread().getName())){
                  //同步方法
                  boolean result = synchronizedMthod();
                  if(result){
                      break;
                  }
              }
  
              if("窗口二".equals(Thread.currentThread().getName())){
                  //同步代码块
                  synchronized (MyRunnable.class){
                      if(ticketCount == 0){
                         break;
                      }else{
                          try {
                              Thread.sleep(10);
                          } catch (InterruptedException e) {
                              e.printStackTrace();
                          }
                          ticketCount--;
                          System.out.println(Thread.currentThread().getName() + "在卖票,还剩下" + ticketCount + "张票");
                      }
                  }
              }
  
          }
      }
  
      private static synchronized boolean synchronizedMthod() {
          if(ticketCount == 0){
              return true;
          }else{
              try {
                  Thread.sleep(10);
              } catch (InterruptedException e) {
                  e.printStackTrace();
              }
              ticketCount--;
              System.out.println(Thread.currentThread().getName() + "在卖票,还剩下" + ticketCount + "张票");
              return false;
          }
      }
  }
  ```

```java
  public class Demo {
  public static void main(String[] args) {
  MyRunnable mr = new MyRunnable();
   Thread t1 = new Thread(mr);
      Thread t2 = new Thread(mr);

      t1.setName("窗口一");
      t2.setName("窗口二");

      t1.start();
      t2.start();
  }
```



  ```java

### 2.5Lock锁【应用】

虽然我们可以理解同步代码块和同步方法的锁对象问题，但是我们并没有直接看到在哪里加上了锁，在哪里释放了锁，为了更清晰的表达如何加锁和释放锁，JDK5以后提供了一个新的锁对象Lock

Lock是接口不能直接实例化，这里采用它的实现类ReentrantLock来实例化

- ReentrantLock构造方法

  | 方法名             | 说明                   |
  | --------------- | -------------------- |
  | ReentrantLock() | 创建一个ReentrantLock的实例 |

- 加锁解锁方法

  | 方法名           | 说明   |
  | ------------- | ---- |
  | void lock()   | 获得锁  |
  | void unlock() | 释放锁  |

- 代码演示

  ```java
  public class Ticket implements Runnable {
      //票的数量
      private int ticket = 100;
      private Object obj = new Object();
      private ReentrantLock lock = new ReentrantLock();

      @Override
      public void run() {
          while (true) {
              //synchronized (obj){//多个线程必须使用同一把锁.
              try {
                  lock.lock();
                  if (ticket <= 0) {
                      //卖完了
                      break;
                  } else {
                      Thread.sleep(100);
                      ticket--;
                      System.out.println(Thread.currentThread().getName() + "在卖票,还剩下" + ticket + "张票");
                  }
              } catch (InterruptedException e) {
                  e.printStackTrace();
              } finally {
                  lock.unlock();
              }
              // }
          }
      }
  }

  public class Demo {
      public static void main(String[] args) {
          Ticket ticket = new Ticket();

          Thread t1 = new Thread(ticket);
          Thread t2 = new Thread(ticket);
          Thread t3 = new Thread(ticket);

          t1.setName("窗口一");
          t2.setName("窗口二");
          t3.setName("窗口三");

          t1.start();
          t2.start();
          t3.start();
      }
  }
  ```

### 2.6死锁【理解】

+ 概述

  线程死锁是指由于两个或者多个线程互相持有对方所需要的资源，导致这些线程处于等待状态，无法前往执行

+ 什么情况下会产生死锁

  1. 资源有限
  2. 同步嵌套

+ 代码演示

  ```java
  public class Demo {
      public static void main(String[] args) {
          Object objA = new Object();
          Object objB = new Object();
  
          new Thread(()->{
              while(true){
                  synchronized (objA){
                      //线程一
                      synchronized (objB){
                          System.out.println("小康同学正在走路");
                      }
                  }
              }
          }).start();
  
          new Thread(()->{
              while(true){
                  synchronized (objB){
                      //线程二
                      synchronized (objA){
                          System.out.println("小薇同学正在走路");
                      }
                  }
              }
          }).start();
      }
  }
  ```

## 3.生产者消费者

### 3.1生产者和消费者模式概述【应用】

- 概述

  生产者消费者模式是一个十分经典的多线程协作的模式，弄懂生产者消费者问题能够让我们对多线程编程的理解更加深刻。

  所谓生产者消费者问题，实际上主要是包含了两类线程：

  ​	一类是生产者线程用于生产数据

  ​	一类是消费者线程用于消费数据

  为了解耦生产者和消费者的关系，通常会采用共享的数据区域，就像是一个仓库

  生产者生产数据之后直接放置在共享数据区中，并不需要关心消费者的行为

  消费者只需要从共享数据区中去获取数据，并不需要关心生产者的行为

- Object类的等待和唤醒方法

  | 方法名           | 说明                                                         |
  | ---------------- | ------------------------------------------------------------ |
  | void wait()      | 导致当前线程等待，直到另一个线程调用该对象的 notify()方法或 notifyAll()方法 |
  | void notify()    | 唤醒正在等待对象监视器的单个线程                             |
  | void notifyAll() | 唤醒正在等待对象监视器的所有线程                             |

### 3.2生产者和消费者案例【应用】

- 案例需求

  + 桌子类(Desk)：定义表示包子数量的变量,定义锁对象变量,定义标记桌子上有无包子的变量

  + 生产者类(Cooker)：实现Runnable接口，重写run()方法，设置线程任务

    1.判断是否有包子,决定当前线程是否执行

    2.如果有包子,就进入等待状态,如果没有包子,继续执行,生产包子

    3.生产包子之后,更新桌子上包子状态,唤醒消费者消费包子

  + 消费者类(Foodie)：实现Runnable接口，重写run()方法，设置线程任务

    1.判断是否有包子,决定当前线程是否执行

    2.如果没有包子,就进入等待状态,如果有包子,就消费包子

    3.消费包子后,更新桌子上包子状态,唤醒生产者生产包子

  + 测试类(Demo)：里面有main方法，main方法中的代码步骤如下

    创建生产者线程和消费者线程对象

    分别开启两个线程

- 代码实现

  ```java
  public class Desk {
  
      //定义一个标记
      //true 就表示桌子上有汉堡包的,此时允许吃货执行
      //false 就表示桌子上没有汉堡包的,此时允许厨师执行
      public static boolean flag = false;
  
      //汉堡包的总数量
      public static int count = 10;
  
      //锁对象
      public static final Object lock = new Object();
  }
  
  public class Cooker extends Thread {
  //    生产者步骤：
  //            1，判断桌子上是否有汉堡包
  //    如果有就等待，如果没有才生产。
  //            2，把汉堡包放在桌子上。
  //            3，叫醒等待的消费者开吃。
      @Override
      public void run() {
          while(true){
              synchronized (Desk.lock){
                  if(Desk.count == 0){
                      break;
                  }else{
                      if(!Desk.flag){
                          //生产
                          System.out.println("厨师正在生产汉堡包");
                          Desk.flag = true;
                          Desk.lock.notifyAll();
                      }else{
                          try {
                              Desk.lock.wait();
                          } catch (InterruptedException e) {
                              e.printStackTrace();
                          }
                      }
                  }
              }
          }
      }
  }
  
  public class Foodie extends Thread {
      @Override
      public void run() {
  //        1，判断桌子上是否有汉堡包。
  //        2，如果没有就等待。
  //        3，如果有就开吃
  //        4，吃完之后，桌子上的汉堡包就没有了
  //                叫醒等待的生产者继续生产
  //        汉堡包的总数量减一
  
          //套路:
              //1. while(true)死循环
              //2. synchronized 锁,锁对象要唯一
              //3. 判断,共享数据是否结束. 结束
              //4. 判断,共享数据是否结束. 没有结束
          while(true){
              synchronized (Desk.lock){
                  if(Desk.count == 0){
                      break;
                  }else{
                      if(Desk.flag){
                          //有
                          System.out.println("吃货在吃汉堡包");
                          Desk.flag = false;
                          Desk.lock.notifyAll();
                          Desk.count--;
                      }else{
                          //没有就等待
                          //使用什么对象当做锁,那么就必须用这个对象去调用等待和唤醒的方法.
                          try {
                              Desk.lock.wait();
                          } catch (InterruptedException e) {
                              e.printStackTrace();
                          }
                      }
                  }
              }
          }
  
      }
  }
  
  public class Demo {
      public static void main(String[] args) {
          /*消费者步骤：
          1，判断桌子上是否有汉堡包。
          2，如果没有就等待。
          3，如果有就开吃
          4，吃完之后，桌子上的汉堡包就没有了
                  叫醒等待的生产者继续生产
          汉堡包的总数量减一*/
  
          /*生产者步骤：
          1，判断桌子上是否有汉堡包
          如果有就等待，如果没有才生产。
          2，把汉堡包放在桌子上。
          3，叫醒等待的消费者开吃。*/
  
          Foodie f = new Foodie();
          Cooker c = new Cooker();
  
          f.start();
          c.start();
  
      }
  }
  ```

### 3.3生产者和消费者案例优化【应用】

+ 需求

  + 将Desk类中的变量,采用面向对象的方式封装起来
  + 生产者和消费者类中构造方法接收Desk类对象,之后在run方法中进行使用
  + 创建生产者和消费者线程对象,构造方法中传入Desk类对象
  + 开启两个线程

+ 代码实现

  ```java
  public class Desk {
  
      //定义一个标记
      //true 就表示桌子上有汉堡包的,此时允许吃货执行
      //false 就表示桌子上没有汉堡包的,此时允许厨师执行
      //public static boolean flag = false;
      private boolean flag;
  
      //汉堡包的总数量
      //public static int count = 10;
      //以后我们在使用这种必须有默认值的变量
     // private int count = 10;
      private int count;
  
      //锁对象
      //public static final Object lock = new Object();
      private final Object lock = new Object();
  
      public Desk() {
          this(false,10); // 在空参内部调用带参,对成员变量进行赋值,之后就可以直接使用成员变量了
      }
  
      public Desk(boolean flag, int count) {
          this.flag = flag;
          this.count = count;
      }
  
      public boolean isFlag() {
          return flag;
      }
  
      public void setFlag(boolean flag) {
          this.flag = flag;
      }
  
      public int getCount() {
          return count;
      }
  
      public void setCount(int count) {
          this.count = count;
      }
  
      public Object getLock() {
          return lock;
      }
  
      @Override
      public String toString() {
          return "Desk{" +
                  "flag=" + flag +
                  ", count=" + count +
                  ", lock=" + lock +
                  '}';
      }
  }
  
  public class Cooker extends Thread {
  
      private Desk desk;
  
      public Cooker(Desk desk) {
          this.desk = desk;
      }
  //    生产者步骤：
  //            1，判断桌子上是否有汉堡包
  //    如果有就等待，如果没有才生产。
  //            2，把汉堡包放在桌子上。
  //            3，叫醒等待的消费者开吃。
  
      @Override
      public void run() {
          while(true){
              synchronized (desk.getLock()){
                  if(desk.getCount() == 0){
                      break;
                  }else{
                      //System.out.println("验证一下是否执行了");
                      if(!desk.isFlag()){
                          //生产
                          System.out.println("厨师正在生产汉堡包");
                          desk.setFlag(true);
                          desk.getLock().notifyAll();
                      }else{
                          try {
                              desk.getLock().wait();
                          } catch (InterruptedException e) {
                              e.printStackTrace();
                          }
                      }
                  }
              }
          }
      }
  }
  
  public class Foodie extends Thread {
      private Desk desk;
  
      public Foodie(Desk desk) {
          this.desk = desk;
      }
  
      @Override
      public void run() {
  //        1，判断桌子上是否有汉堡包。
  //        2，如果没有就等待。
  //        3，如果有就开吃
  //        4，吃完之后，桌子上的汉堡包就没有了
  //                叫醒等待的生产者继续生产
  //        汉堡包的总数量减一
  
          //套路:
              //1. while(true)死循环
              //2. synchronized 锁,锁对象要唯一
              //3. 判断,共享数据是否结束. 结束
              //4. 判断,共享数据是否结束. 没有结束
          while(true){
              synchronized (desk.getLock()){
                  if(desk.getCount() == 0){
                      break;
                  }else{
                      //System.out.println("验证一下是否执行了");
                      if(desk.isFlag()){
                          //有
                          System.out.println("吃货在吃汉堡包");
                          desk.setFlag(false);
                          desk.getLock().notifyAll();
                          desk.setCount(desk.getCount() - 1);
                      }else{
                          //没有就等待
                          //使用什么对象当做锁,那么就必须用这个对象去调用等待和唤醒的方法.
                          try {
                              desk.getLock().wait();
                          } catch (InterruptedException e) {
                              e.printStackTrace();
                          }
                      }
                  }
              }
          }
  
      }
  }
  
  public class Demo {
      public static void main(String[] args) {
          /*消费者步骤：
          1，判断桌子上是否有汉堡包。
          2，如果没有就等待。
          3，如果有就开吃
          4，吃完之后，桌子上的汉堡包就没有了
                  叫醒等待的生产者继续生产
          汉堡包的总数量减一*/
  
          /*生产者步骤：
          1，判断桌子上是否有汉堡包
          如果有就等待，如果没有才生产。
          2，把汉堡包放在桌子上。
          3，叫醒等待的消费者开吃。*/
  
          Desk desk = new Desk();
  
          Foodie f = new Foodie(desk);
          Cooker c = new Cooker(desk);
  
          f.start();
          c.start();
  
      }
  }
  ```

### 3.4阻塞队列基本使用【理解】

+ 阻塞队列继承结构

  ![06_阻塞队列继承结构](/../img/06_阻塞队列继承结构.png)


+ 常见BlockingQueue:

  ArrayBlockingQueue: 底层是数组,有界

  LinkedBlockingQueue: 底层是链表,无界.但不是真正的无界,最大为int的最大值

+ BlockingQueue的核心方法:

  put(anObject): 将参数放入队列,如果放不进去会阻塞

  take(): 取出第一个数据,取不到会阻塞

+ 代码示例

  ```java
  public class Demo02 {
      public static void main(String[] args) throws Exception {
          // 创建阻塞队列的对象,容量为 1
          ArrayBlockingQueue<String> arrayBlockingQueue = new ArrayBlockingQueue<>(1);
  
          // 存储元素
          arrayBlockingQueue.put("汉堡包");
  
          // 取元素
          System.out.println(arrayBlockingQueue.take());
          System.out.println(arrayBlockingQueue.take()); // 取不到会阻塞
  
          System.out.println("程序结束了");
      }
  }
  ```

### 3.5阻塞队列实现等待唤醒机制【理解】

+ 案例需求

  + 生产者类(Cooker)：实现Runnable接口，重写run()方法，设置线程任务

    1.构造方法中接收一个阻塞队列对象

    2.在run方法中循环向阻塞队列中添加包子

    3.打印添加结果

  + 消费者类(Foodie)：实现Runnable接口，重写run()方法，设置线程任务

    1.构造方法中接收一个阻塞队列对象

    2.在run方法中循环获取阻塞队列中的包子

    3.打印获取结果

  + 测试类(Demo)：里面有main方法，main方法中的代码步骤如下

    创建阻塞队列对象

    创建生产者线程和消费者线程对象,构造方法中传入阻塞队列对象

    分别开启两个线程

+ 代码实现

  ```java
  public class Cooker extends Thread {
  
      private ArrayBlockingQueue<String> bd;
  
      public Cooker(ArrayBlockingQueue<String> bd) {
          this.bd = bd;
      }
  //    生产者步骤：
  //            1，判断桌子上是否有汉堡包
  //    如果有就等待，如果没有才生产。
  //            2，把汉堡包放在桌子上。
  //            3，叫醒等待的消费者开吃。
  
      @Override
      public void run() {
          while (true) {
              try {
                  bd.put("汉堡包");
                  System.out.println("厨师放入一个汉堡包");
              } catch (InterruptedException e) {
                  e.printStackTrace();
              }
          }
      }
  }
  
  public class Foodie extends Thread {
      private ArrayBlockingQueue<String> bd;
  
      public Foodie(ArrayBlockingQueue<String> bd) {
          this.bd = bd;
      }
  
      @Override
      public void run() {
  //        1，判断桌子上是否有汉堡包。
  //        2，如果没有就等待。
  //        3，如果有就开吃
  //        4，吃完之后，桌子上的汉堡包就没有了
  //                叫醒等待的生产者继续生产
  //        汉堡包的总数量减一
  
          //套路:
          //1. while(true)死循环
          //2. synchronized 锁,锁对象要唯一
          //3. 判断,共享数据是否结束. 结束
          //4. 判断,共享数据是否结束. 没有结束
          while (true) {
              try {
                  String take = bd.take();
                  System.out.println("吃货将" + take + "拿出来吃了");
              } catch (InterruptedException e) {
                  e.printStackTrace();
              }
          }
  
      }
  }
  
  public class Demo {
      public static void main(String[] args) {
          ArrayBlockingQueue<String> bd = new ArrayBlockingQueue<>(1);
  
          Foodie f = new Foodie(bd);
          Cooker c = new Cooker(bd);
  
          f.start();
          c.start();
      }
  }
  ```

## 1. 线程池

### 1.1 线程状态介绍

当线程被创建并启动以后，它既不是一启动就进入了执行状态，也不是一直处于执行状态。线程对象在不同的时期有不同的状态。那么Java中的线程存在哪几种状态呢？Java中的线程

状态被定义在了java.lang.Thread.State枚举类中，State枚举类的源码如下：

```java
public class Thread {
    
    public enum State {
    
        /* 新建 */
        NEW , 

        /* 可运行状态 */
        RUNNABLE , 

        /* 阻塞状态 */
        BLOCKED , 

        /* 无限等待状态 */
        WAITING , 

        /* 计时等待 */
        TIMED_WAITING , 

        /* 终止 */
        TERMINATED;
    
	}
    
    // 获取当前线程的状态
    public State getState() {
        return jdk.internal.misc.VM.toThreadState(threadStatus);
    }
    
}
```

通过源码我们可以看到Java中的线程存在6种状态，每种线程状态的含义如下

| 线程状态      | 具体含义                                                     |
| ------------- | ------------------------------------------------------------ |
| NEW           | 一个尚未启动的线程的状态。也称之为初始状态、开始状态。线程刚被创建，但是并未启动。还没调用start方法。MyThread t = new MyThread()只有线程象，没有线程特征。 |
| RUNNABLE      | 当我们调用线程对象的start方法，那么此时线程对象进入了RUNNABLE状态。那么此时才是真正的在JVM进程中创建了一个线程，线程一经启动并不是立即得到执行，线程的运行与否要听令与CPU的调度，那么我们把这个中间状态称之为可执行状态(RUNNABLE)也就是说它具备执行的资格，但是并没有真正的执行起来而是在等待CPU的度。 |
| BLOCKED       | 当一个线程试图获取一个对象锁，而该对象锁被其他的线程持有，则该线程进入Blocked状态；当该线程持有锁时，该线程将变成Runnable状态。 |
| WAITING       | 一个正在等待的线程的状态。也称之为等待状态。造成线程等待的原因有两种，分别是调用Object.wait()、join()方法。处于等待状态的线程，正在等待其他线程去执行一个特定的操作。例如：因为wait()而等待的线程正在等待另一个线程去调用notify()或notifyAll()；一个因为join()而等待的线程正在等待另一个线程结束。 |
| TIMED_WAITING | 一个在限定时间内等待的线程的状态。也称之为限时等待状态。造成线程限时等待状态的原因有三种，分别是：Thread.sleep(long)，Object.wait(long)、join(long)。 |
| TERMINATED    | 一个完全运行完成的线程的状态。也称之为终止状态、结束状态     |

各个状态的转换，如下图所示：

![1591163781941](/../img/1591163781941.png)

### 1.2 线程池-基本原理

**概述 :** 

提到池，大家应该能想到的就是水池。水池就是一个容器，在该容器中存储了很多的水。那么什么是线程池呢？线程池也是可以看做成一个池子，在该池子中存储很多个线程。

线程池存在的意义：

系统创建一个线程的成本是比较高的，因为它涉及到与操作系统交互，当程序中需要创建大量生存期很短暂的线程时，频繁的创建和销毁线程对系统的资源消耗有可能大于业务处理是对系统资源的消耗，这样就有点"舍本逐末"了。针对这一种情况，为了提高性能，我们就可以采用线程池。线程池在启动的时，会创建大量空闲线程，当我们向线程池提交任务的时，线程池就会启动一个线程来执行该任务。等待任务执行完毕以后，线程并不会死亡，而是再次返回到线程池中称为空闲状态。等待下一次任务的执行。

**线程池的设计思路 :**

1. 准备一个任务容器
2. 一次性启动多个(2个)消费者线程
3. 刚开始任务容器是空的，所以线程都在wait
4. 直到一个外部线程向这个任务容器中扔了一个"任务"，就会有一个消费者线程被唤醒
5. 这个消费者线程取出"任务"，并且执行这个任务，执行完毕后，继续等待下一次任务的到来

### 1.3 线程池-Executors默认线程池

概述 : JDK对线程池也进行了相关的实现，在真实企业开发中我们也很少去自定义线程池，而是使用JDK中自带的线程池。

我们可以使用Executors中所提供的**静态**方法来创建线程池

​	static ExecutorService newCachedThreadPool()   创建一个默认的线程池
​	static newFixedThreadPool(int nThreads)	    创建一个指定最多线程数量的线程池

**代码实现 :** 

```java
package com.itheima.mythreadpool;


//static ExecutorService newCachedThreadPool()   创建一个默认的线程池
//static newFixedThreadPool(int nThreads)	    创建一个指定最多线程数量的线程池

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MyThreadPoolDemo {
    public static void main(String[] args) throws InterruptedException {

        //1,创建一个默认的线程池对象.池子中默认是空的.默认最多可以容纳int类型的最大值.
        ExecutorService executorService = Executors.newCachedThreadPool();
        //Executors --- 可以帮助我们创建线程池对象
        //ExecutorService --- 可以帮助我们控制线程池

        executorService.submit(()->{
            System.out.println(Thread.currentThread().getName() + "在执行了");
        });

        //Thread.sleep(2000);

        executorService.submit(()->{
            System.out.println(Thread.currentThread().getName() + "在执行了");
        });

        executorService.shutdown();
    }
}

```



### 1.4 线程池-Executors创建指定上限的线程池

**使用Executors中所提供的静态方法来创建线程池**

​	static ExecutorService newFixedThreadPool(int nThreads) : 创建一个指定最多线程数量的线程池

**代码实现 :** 

```java
package com.itheima.mythreadpool;

//static ExecutorService newFixedThreadPool(int nThreads)
//创建一个指定最多线程数量的线程池

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

public class MyThreadPoolDemo2 {
    public static void main(String[] args) {
        //参数不是初始值而是最大值
        ExecutorService executorService = Executors.newFixedThreadPool(10);

        ThreadPoolExecutor pool = (ThreadPoolExecutor) executorService;
        System.out.println(pool.getPoolSize());//0

        executorService.submit(()->{
            System.out.println(Thread.currentThread().getName() + "在执行了");
        });

        executorService.submit(()->{
            System.out.println(Thread.currentThread().getName() + "在执行了");
        });

        System.out.println(pool.getPoolSize());//2
//        executorService.shutdown();
    }
}

```



### 1.5 线程池-ThreadPoolExecutor

**创建线程池对象 :** 

ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(核心线程数量,最大线程数量,空闲线程最大存活时间,任务队列,创建线程工厂,任务的拒绝策略);

**代码实现 :** 

```java
package com.itheima.mythreadpool;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class MyThreadPoolDemo3 {
//    参数一：核心线程数量
//    参数二：最大线程数
//    参数三：空闲线程最大存活时间
//    参数四：时间单位
//    参数五：任务队列
//    参数六：创建线程工厂
//    参数七：任务的拒绝策略
    public static void main(String[] args) {
        ThreadPoolExecutor pool = new ThreadPoolExecutor(2,5,2,TimeUnit.SECONDS,new ArrayBlockingQueue<>(10), Executors.defaultThreadFactory(),new ThreadPoolExecutor.AbortPolicy());
        pool.submit(new MyRunnable());
        pool.submit(new MyRunnable());

        pool.shutdown();
    }
}
```

### 1.6 线程池-参数详解

![1591165506516](/../img/1591165506516.png)

```java
public ThreadPoolExecutor(int corePoolSize,
                              int maximumPoolSize,
                              long keepAliveTime,
                              TimeUnit unit,
                              BlockingQueue<Runnable> workQueue,
                              ThreadFactory threadFactory,
                              RejectedExecutionHandler handler)
    
corePoolSize：   核心线程的最大值，不能小于0
maximumPoolSize：最大线程数，不能小于等于0，maximumPoolSize >= corePoolSize
keepAliveTime：  空闲线程最大存活时间,不能小于0
unit：           时间单位
workQueue：      任务队列，不能为null
threadFactory：  创建线程工厂,不能为null      
handler：        任务的拒绝策略,不能为null  
```



### 1.7 线程池-非默认任务拒绝策略

RejectedExecutionHandler是jdk提供的一个任务拒绝策略接口，它下面存在4个子类。

```java
ThreadPoolExecutor.AbortPolicy: 		    丢弃任务并抛出RejectedExecutionException异常。是默认的策略。
ThreadPoolExecutor.DiscardPolicy： 		   丢弃任务，但是不抛出异常 这是不推荐的做法。
ThreadPoolExecutor.DiscardOldestPolicy：    抛弃队列中等待最久的任务 然后把当前任务加入队列中。
ThreadPoolExecutor.CallerRunsPolicy:        调用任务的run()方法绕过线程池直接执行。
```

注：明确线程池对多可执行的任务数 = 队列容量 + 最大线程数

**案例演示1**：演示ThreadPoolExecutor.AbortPolicy任务处理策略

```java
public class ThreadPoolExecutorDemo01 {

    public static void main(String[] args) {

        /**
         * 核心线程数量为1 ， 最大线程池数量为3, 任务容器的容量为1 ,空闲线程的最大存在时间为20s
         */
        ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(1 , 3 , 20 , TimeUnit.SECONDS ,
                new ArrayBlockingQueue<>(1) , Executors.defaultThreadFactory() , new ThreadPoolExecutor.AbortPolicy()) ;

        // 提交5个任务，而该线程池最多可以处理4个任务，当我们使用AbortPolicy这个任务处理策略的时候，就会抛出异常
        for(int x = 0 ; x < 5 ; x++) {
            threadPoolExecutor.submit(() -> {
                System.out.println(Thread.currentThread().getName() + "---->> 执行了任务");
            });
        }
    }
}
```

**控制台输出结果**

```java
pool-1-thread-1---->> 执行了任务
pool-1-thread-3---->> 执行了任务
pool-1-thread-2---->> 执行了任务
pool-1-thread-3---->> 执行了任务
```

控制台报错，仅仅执行了4个任务，有一个任务被丢弃了



**案例演示2**：演示ThreadPoolExecutor.DiscardPolicy任务处理策略

```java
public class ThreadPoolExecutorDemo02 {
    public static void main(String[] args) {
        /**
         * 核心线程数量为1 ， 最大线程池数量为3, 任务容器的容量为1 ,空闲线程的最大存在时间为20s
         */
        ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(1 , 3 , 20 , TimeUnit.SECONDS ,
                new ArrayBlockingQueue<>(1) , Executors.defaultThreadFactory() , new ThreadPoolExecutor.DiscardPolicy()) ;

        // 提交5个任务，而该线程池最多可以处理4个任务，当我们使用DiscardPolicy这个任务处理策略的时候，控制台不会报错
        for(int x = 0 ; x < 5 ; x++) {
            threadPoolExecutor.submit(() -> {
                System.out.println(Thread.currentThread().getName() + "---->> 执行了任务");
            });
        }
    }
}
```

**控制台输出结果**

```java
pool-1-thread-1---->> 执行了任务
pool-1-thread-1---->> 执行了任务
pool-1-thread-3---->> 执行了任务
pool-1-thread-2---->> 执行了任务
```

控制台没有报错，仅仅执行了4个任务，有一个任务被丢弃了



**案例演示3**：演示ThreadPoolExecutor.DiscardOldestPolicy任务处理策略

```java
public class ThreadPoolExecutorDemo02 {
    public static void main(String[] args) {
        /**
         * 核心线程数量为1 ， 最大线程池数量为3, 任务容器的容量为1 ,空闲线程的最大存在时间为20s
         */
        ThreadPoolExecutor threadPoolExecutor;
        threadPoolExecutor = new ThreadPoolExecutor(1 , 3 , 20 , TimeUnit.SECONDS ,
                new ArrayBlockingQueue<>(1) , Executors.defaultThreadFactory() , new ThreadPoolExecutor.DiscardOldestPolicy());
        // 提交5个任务
        for(int x = 0 ; x < 5 ; x++) {
            // 定义一个变量，来指定指定当前执行的任务;这个变量需要被final修饰
            final int y = x ;
            threadPoolExecutor.submit(() -> {
                System.out.println(Thread.currentThread().getName() + "---->> 执行了任务" + y);
            });     
        }
    }
}
```

**控制台输出结果**

```java
pool-1-thread-2---->> 执行了任务2
pool-1-thread-1---->> 执行了任务0
pool-1-thread-3---->> 执行了任务3
pool-1-thread-1---->> 执行了任务4
```

由于任务1在线程池中等待时间最长，因此任务1被丢弃。



**案例演示4**：演示ThreadPoolExecutor.CallerRunsPolicy任务处理策略

```java
public class ThreadPoolExecutorDemo04 {
    public static void main(String[] args) {

        /**
         * 核心线程数量为1 ， 最大线程池数量为3, 任务容器的容量为1 ,空闲线程的最大存在时间为20s
         */
        ThreadPoolExecutor threadPoolExecutor;
        threadPoolExecutor = new ThreadPoolExecutor(1 , 3 , 20 , TimeUnit.SECONDS ,
                new ArrayBlockingQueue<>(1) , Executors.defaultThreadFactory() , new ThreadPoolExecutor.CallerRunsPolicy());

        // 提交5个任务
        for(int x = 0 ; x < 5 ; x++) {
            threadPoolExecutor.submit(() -> {
                System.out.println(Thread.currentThread().getName() + "---->> 执行了任务");
            });
        }
    }
}
```

**控制台输出结果**

```java
pool-1-thread-1---->> 执行了任务
pool-1-thread-3---->> 执行了任务
pool-1-thread-2---->> 执行了任务
pool-1-thread-1---->> 执行了任务
main---->> 执行了任务
```

通过控制台的输出，我们可以看到次策略没有通过线程池中的线程执行任务，而是直接调用任务的run()方法绕过线程池直接执行。

## 2. 多线程综合练习

### 练习一：售票

需求：

​	一共有1000张电影票,可以在两个窗口领取,假设每次领取的时间为3000毫秒,

​	请用多线程模拟卖票过程并打印剩余电影票的数量

代码示例：

```java
public class MyThread extends Thread {

    //第一种方式实现多线程，测试类中MyThread会创建多次，所以需要加static
    static int ticket = 1000;

    @Override
    public void run() {
        //1.循环
        while (true) {
            //2.同步代码块
            synchronized (MyThread.class) {
                //3.判断共享数据（已经到末尾）
                if (ticket == 0) {
                    break;
                } else {
                    //4.判断共享数据（没有到末尾）
                    try {
                        Thread.sleep(3000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    ticket--;
                    System.out.println(getName() + "在卖票，还剩下" + ticket + "张票!!!");
                }
            }
        }
    }
}

public class Test {
    public static void main(String[] args) {
       /*
            一共有1000张电影票,可以在两个窗口领取,假设每次领取的时间为3000毫秒,
            要求:请用多线程模拟卖票过程并打印剩余电影票的数量
        */

        //创建线程对象
        MyThread t1 = new MyThread();
        MyThread t2 = new MyThread();

        //给线程设置名字
        t1.setName("窗口1");
        t2.setName("窗口2");

        //开启线程
        t1.start();
        t2.start();

    }
}

```



### 练习二：赠送礼物

需求：

​	有100份礼品,两人同时发送，当剩下的礼品小于10份的时候则不再送出。

​	利用多线程模拟该过程并将线程的名字和礼物的剩余数量打印出来.

```java
public class MyRunable implements Runnable {

    //第二种方式实现多线程，测试类中MyRunable只创建一次，所以不需要加static
    int count = 100;

    @Override
    public void run() {
        //1.循环
        while (true) {
            //2.同步代码块
            synchronized (MyThread.class) {
                //3.判断共享数据（已经到末尾）
                if (count < 10) {
                    System.out.println("礼物还剩下" + count + "不再赠送");
                    break;
                } else {
                    //4.判断共享数据（没有到末尾）
                    count--;
                    System.out.println(Thread.currentThread().getName() + "在赠送礼物，还剩下" + count + "个礼物!!!");
                }
            }
        }
    }
}


public class Test {
    public static void main(String[] args) {
        /*
            有100份礼品,两人同时发送，当剩下的礼品小于10份的时候则不再送出，
            利用多线程模拟该过程并将线程的名字和礼物的剩余数量打印出来.
        */

        //创建参数对象
        MyRunable mr = new MyRunable();

        //创建线程对象
        Thread t1 = new Thread(mr,"窗口1");
        Thread t2 = new Thread(mr,"窗口2");

        //启动线程
        t1.start();
        t2.start();
    }
}

```



### 练习三：打印数字

需求：

​	同时开启两个线程，共同获取1-100之间的所有数字。

​	将输出所有的奇数。

```java
public class MyRunable implements Runnable {

    //第二种方式实现多线程，测试类中MyRunable只创建一次，所以不需要加static
    int number = 1;

    @Override
    public void run() {
        //1.循环
        while (true) {
            //2.同步代码块
            synchronized (MyThread.class) {
                //3.判断共享数据（已经到末尾）
                if (number > 100) {
                    break;
                } else {
                    //4.判断共享数据（没有到末尾）
                    if(number % 2 == 1){
                        System.out.println(Thread.currentThread().getName() + "打印数字" + number);
                    }
                    number++;
                }
            }
        }
    }
}


public class Test {
    public static void main(String[] args) {
        /*
           同时开启两个线程，共同获取1-100之间的所有数字。
           要求：将输出所有的奇数。
        */


        //创建参数对象
        MyRunable mr = new MyRunable();

        //创建线程对象
        Thread t1 = new Thread(mr,"线程A");
        Thread t2 = new Thread(mr,"线程B");

        //启动线程
        t1.start();
        t2.start();
    }
}
```

### 练习四：抢红包

需求：

​	抢红包也用到了多线程。

​	假设：100块，分成了3个包，现在有5个人去抢。

​	其中，红包是共享数据。

​	5个人是5条线程。

​	打印结果如下：

​		  XXX抢到了XXX元

​		  XXX抢到了XXX元

 		 XXX抢到了XXX元
 	
 		XXX没抢到
 	
 		XXX没抢到

解决方案一：

```java
public class MyThread extends Thread{

    //共享数据
    //100块，分成了3个包
    static double money = 100;
    static int count = 3;

    //最小的中奖金额
    static final double MIN = 0.01;

    @Override
    public void run() {
        //同步代码块
        synchronized (MyThread.class){
            if(count == 0){
                //判断，共享数据是否到了末尾（已经到末尾）
                System.out.println(getName() + "没有抢到红包！");
            }else{
                //判断，共享数据是否到了末尾（没有到末尾）
                //定义一个变量，表示中奖的金额
                double prize = 0;
                if(count == 1){
                    //表示此时是最后一个红包
                    //就无需随机，剩余所有的钱都是中奖金额
                    prize = money;
                }else{
                    //表示第一次，第二次（随机）
                    Random r = new Random();
                    //100 元   3个包
                    //第一个红包：99.98
                    //100 - (3-1) * 0.01
                    double bounds = money - (count - 1) * MIN;
                    prize = r.nextDouble(bounds);
                    if(prize < MIN){
                        prize = MIN;
                    }
                }
                //从money当中，去掉当前中奖的金额
                money = money - prize;
                //红包的个数-1
                count--;
                //本次红包的信息进行打印
                System.out.println(getName() + "抢到了" + prize + "元");
            }
        }
    }
}
public class Test {
    public static void main(String[] args) {
        /*
            微信中的抢红包也用到了多线程。
            假设：100块，分成了3个包，现在有5个人去抢。
            其中，红包是共享数据。
            5个人是5条线程。
            打印结果如下：
            	XXX抢到了XXX元
            	XXX抢到了XXX元
            	XXX抢到了XXX元
            	XXX没抢到
            	XXX没抢到
        */

        //创建线程的对象
        MyThread t1 = new MyThread();
        MyThread t2 = new MyThread();
        MyThread t3 = new MyThread();
        MyThread t4 = new MyThread();
        MyThread t5 = new MyThread();

        //给线程设置名字
        t1.setName("小A");
        t2.setName("小QQ");
        t3.setName("小哈哈");
        t4.setName("小诗诗");
        t5.setName("小丹丹");

        //启动线程
        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();
    }
}
```

解决方案二：

```java
public class MyThread extends Thread{

    //总金额
    static BigDecimal money = BigDecimal.valueOf(100.0);
    //个数
    static int count = 3;
    //最小抽奖金额
    static final BigDecimal MIN = BigDecimal.valueOf(0.01);

    @Override
    public void run() {
        synchronized (MyThread.class){
            if(count == 0){
                System.out.println(getName() + "没有抢到红包！");
            }else{
                //中奖金额
                BigDecimal prize;
                if(count == 1){
                    prize = money;
                }else{
                    //获取抽奖范围
                    double bounds = money.subtract(BigDecimal.valueOf(count-1).multiply(MIN)).doubleValue();
                    Random r = new Random();
                    //抽奖金额
                    prize = BigDecimal.valueOf(r.nextDouble(bounds));
                }
                //设置抽中红包，小数点保留两位，四舍五入
                prize = prize.setScale(2,RoundingMode.HALF_UP);
                //在总金额中去掉对应的钱
                money = money.subtract(prize);
                //红包少了一个
                count--;
                //输出红包信息
                System.out.println(getName() + "抽中了" + prize + "元");
            }
        }
    }
}

public class Test {
    public static void main(String[] args) {
        /*
            微信中的抢红包也用到了多线程。
            假设：100块，分成了3个包，现在有5个人去抢。
            其中，红包是共享数据。
            5个人是5条线程。
            打印结果如下：
            	XXX抢到了XXX元
            	XXX抢到了XXX元
            	XXX抢到了XXX元
            	XXX没抢到
            	XXX没抢到
        */


        MyThread t1 = new MyThread();
        MyThread t2 = new MyThread();
        MyThread t3 = new MyThread();
        MyThread t4 = new MyThread();
        MyThread t5 = new MyThread();

        t1.setName("小A");
        t2.setName("小QQ");
        t3.setName("小哈哈");
        t4.setName("小诗诗");
        t5.setName("小丹丹");

        t1.start();
        t2.start();
        t3.start();
        t4.start();
        t5.start();
    }
}
```

### 练习五：抽奖箱

需求：

​	有一个抽奖池,该抽奖池中存放了奖励的金额,该抽奖池中的奖项为 {10,5,20,50,100,200,500,800,2,80,300,700}; 

创建两个抽奖箱(线程)设置线程名称分别为“抽奖箱1”，“抽奖箱2” 

随机从抽奖池中获取奖项元素并打印在控制台上,格式如下:

​               每次抽出一个奖项就打印一个(随机)

​		抽奖箱1 又产生了一个 10 元大奖

  		抽奖箱1 又产生了一个 100 元大奖
  	
  		抽奖箱1 又产生了一个 200 元大奖
  	
  		抽奖箱1 又产生了一个 800 元大奖  

​		抽奖箱2 又产生了一个 700 元大奖  

 		 .....

```java
public class MyThread extends Thread {

    ArrayList<Integer> list;

    public MyThread(ArrayList<Integer> list) {
        this.list = list;
    }

    @Override
    public void run() {
        //1.循环
        //2.同步代码块
        //3.判断
        //4.判断

        while (true) {
            synchronized (MyThread.class) {
                if (list.size() == 0) {
                    break;
                } else {
                    //继续抽奖
                    Collections.shuffle(list);
                    int prize = list.remove(0);
                    System.out.println(getName() + "又产生了一个" + prize + "元大奖");
                }
            }
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
}



public class Test {
    public static void main(String[] args) {
        /*
            有一个抽奖池,该抽奖池中存放了奖励的金额,该抽奖池中的奖项为 {10,5,20,50,100,200,500,800,2,80,300,700};
            创建两个抽奖箱(线程)设置线程名称分别为“抽奖箱1”，“抽奖箱2”
            随机从抽奖池中获取奖项元素并打印在控制台上,格式如下:
                             每次抽出一个奖项就打印一个(随机)
            	抽奖箱1 又产生了一个 10 元大奖
            	抽奖箱1 又产生了一个 100 元大奖
            	抽奖箱1 又产生了一个 200 元大奖
            	抽奖箱1 又产生了一个 800 元大奖
            	抽奖箱2 又产生了一个 700 元大奖
            	.....
        */

        //创建奖池
        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list,10,5,20,50,100,200,500,800,2,80,300,700);

        //创建线程
        MyThread t1 = new MyThread(list);
        MyThread t2 = new MyThread(list);

        //设置名字
        t1.setName("抽奖箱1");
        t2.setName("抽奖箱2");

        //启动线程
        t1.start();
        t2.start();
    }
}
```



### 练习六：多线程统计并求最大值

需求：

​	在上一题基础上继续完成如下需求：

​     每次抽的过程中，不打印，抽完时一次性打印(随机)

​     在此次抽奖过程中，抽奖箱1总共产生了6个奖项。

​              分别为：10,20,100,500,2,300最高奖项为300元，总计额为932元

​     在此次抽奖过程中，抽奖箱2总共产生了6个奖项。

​              分别为：5,50,200,800,80,700最高奖项为800元，总计额为1835元

解决方案一：

```java
public class MyThread extends Thread {

    ArrayList<Integer> list;

    public MyThread(ArrayList<Integer> list) {
        this.list = list;
    }

    //线程一
    static ArrayList<Integer> list1 = new ArrayList<>();
    //线程二
    static ArrayList<Integer> list2 = new ArrayList<>();

    @Override
    public void run() {
        while (true) {
            synchronized (MyThread.class) {
                if (list.size() == 0) {
                    if("抽奖箱1".equals(getName())){
                        System.out.println("抽奖箱1" + list1);
                    }else {
                        System.out.println("抽奖箱2" + list2);
                    }
                    break;
                } else {
                    //继续抽奖
                    Collections.shuffle(list);
                    int prize = list.remove(0);
                    if("抽奖箱1".equals(getName())){
                        list1.add(prize);
                    }else {
                        list2.add(prize);
                    }
                }
            }
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
}

public class Test {
    public static void main(String[] args) {
        /*
            有一个抽奖池,该抽奖池中存放了奖励的金额,该抽奖池中的奖项为 {10,5,20,50,100,200,500,800,2,80,300,700};
            创建两个抽奖箱(线程)设置线程名称分别为“抽奖箱1”，“抽奖箱2”
            随机从抽奖池中获取奖项元素并打印在控制台上,格式如下:
            每次抽的过程中，不打印，抽完时一次性打印(随机)    在此次抽奖过程中，抽奖箱1总共产生了6个奖项。
                分别为：10,20,100,500,2,300最高奖项为300元，总计额为932元
            在此次抽奖过程中，抽奖箱2总共产生了6个奖项。
                分别为：5,50,200,800,80,700最高奖项为800元，总计额为1835元
        */

        //创建奖池
        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list,10,5,20,50,100,200,500,800,2,80,300,700);

        //创建线程
        MyThread t1 = new MyThread(list);
        MyThread t2 = new MyThread(list);

        //设置名字
        t1.setName("抽奖箱1");
        t2.setName("抽奖箱2");

        //启动线程
        t1.start();
        t2.start();
    }
}

```

解决方案二：

```java
public class MyThread extends Thread {

    ArrayList<Integer> list;

    public MyThread(ArrayList<Integer> list) {
        this.list = list;
    }

    @Override
    public void run() {
        ArrayList<Integer> boxList = new ArrayList<>();//1 //2
        while (true) {
            synchronized (MyThread.class) {
                if (list.size() == 0) {
                    System.out.println(getName() + boxList);
                    break;
                } else {
                    //继续抽奖
                    Collections.shuffle(list);
                    int prize = list.remove(0);
                    boxList.add(prize);
                }
            }
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }
    }
}

public class Test {
    public static void main(String[] args) {
        /*
            有一个抽奖池,该抽奖池中存放了奖励的金额,该抽奖池中的奖项为 {10,5,20,50,100,200,500,800,2,80,300,700};
            创建两个抽奖箱(线程)设置线程名称分别为“抽奖箱1”，“抽奖箱2”
            随机从抽奖池中获取奖项元素并打印在控制台上,格式如下:
            每次抽的过程中，不打印，抽完时一次性打印(随机)    在此次抽奖过程中，抽奖箱1总共产生了6个奖项。
                分别为：10,20,100,500,2,300最高奖项为300元，总计额为932元
            在此次抽奖过程中，抽奖箱2总共产生了6个奖项。
                分别为：5,50,200,800,80,700最高奖项为800元，总计额为1835元
        */

        //创建奖池
        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list,10,5,20,50,100,200,500,800,2,80,300,700);

        //创建线程
        MyThread t1 = new MyThread(list);
        MyThread t2 = new MyThread(list);


        //设置名字
        t1.setName("抽奖箱1");
        t2.setName("抽奖箱2");


        //启动线程
        t1.start();
        t2.start();

    }
}
```



### 练习七：多线程之间的比较 

需求：

​	在上一题基础上继续完成如下需求：

​	在此次抽奖过程中，抽奖箱1总共产生了6个奖项，分别为：10,20,100,500,2,300

  	最高奖项为300元，总计额为932元

​	在此次抽奖过程中，抽奖箱2总共产生了6个奖项，分别为：5,50,200,800,80,700

  	最高奖项为800元，总计额为1835元

​	在此次抽奖过程中,抽奖箱2中产生了最大奖项,该奖项金额为800元

​	以上打印效果只是数据模拟,实际代码运行的效果会有差异

```java
public class MyCallable implements Callable<Integer> {

    ArrayList<Integer> list;

    public MyCallable(ArrayList<Integer> list) {
        this.list = list;
    }

    @Override
    public Integer call() throws Exception {
        ArrayList<Integer> boxList = new ArrayList<>();//1 //2
        while (true) {
            synchronized (MyCallable.class) {
                if (list.size() == 0) {
                    System.out.println(Thread.currentThread().getName() + boxList);
                    break;
                } else {
                    //继续抽奖
                    Collections.shuffle(list);
                    int prize = list.remove(0);
                    boxList.add(prize);
                }
            }
            Thread.sleep(10);
        }
        //把集合中的最大值返回
        if(boxList.size() == 0){
            return null;
        }else{
            return Collections.max(boxList);
        }
    }
}

package com.itheima.test7;

import java.util.ArrayList;
import java.util.Collections;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class Test {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        /*
            有一个抽奖池,该抽奖池中存放了奖励的金额,该抽奖池中的奖项为 {10,5,20,50,100,200,500,800,2,80,300,700};
            创建两个抽奖箱(线程)设置线程名称分别为    "抽奖箱1", "抽奖箱2"
            随机从抽奖池中获取奖项元素并打印在控制台上,格式如下:

            在此次抽奖过程中，抽奖箱1总共产生了6个奖项，分别为：10,20,100,500,2,300
        	    最高奖项为300元，总计额为932元

            在此次抽奖过程中，抽奖箱2总共产生了6个奖项，分别为：5,50,200,800,80,700
            	最高奖项为800元，总计额为1835元

            在此次抽奖过程中,抽奖箱2中产生了最大奖项,该奖项金额为800元
            核心逻辑：获取线程抽奖的最大值（看成是线程运行的结果）


            以上打印效果只是数据模拟,实际代码运行的效果会有差异
        */

        //创建奖池
        ArrayList<Integer> list = new ArrayList<>();
        Collections.addAll(list,10,5,20,50,100,200,500,800,2,80,300,700);

        //创建多线程要运行的参数对象
        MyCallable mc = new MyCallable(list);

        //创建多线程运行结果的管理者对象
        //线程一
        FutureTask<Integer> ft1 = new FutureTask<>(mc);
        //线程二
        FutureTask<Integer> ft2 = new FutureTask<>(mc);

        //创建线程对象
        Thread t1 = new Thread(ft1);
        Thread t2 = new Thread(ft2);

        //设置名字
        t1.setName("抽奖箱1");
        t2.setName("抽奖箱2");

        //开启线程
        t1.start();
        t2.start();


        Integer max1 = ft1.get();
        Integer max2 = ft2.get();

        System.out.println(max1);
        System.out.println(max2);

        //在此次抽奖过程中,抽奖箱2中产生了最大奖项,该奖项金额为800元
        if(max1 == null){
            System.out.println("在此次抽奖过程中,抽奖箱2中产生了最大奖项,该奖项金额为"+max2+"元");
        }else if(max2 == null){
            System.out.println("在此次抽奖过程中,抽奖箱1中产生了最大奖项,该奖项金额为"+max1+"元");
        }else if(max1 > max2){
            System.out.println("在此次抽奖过程中,抽奖箱1中产生了最大奖项,该奖项金额为"+max1+"元");
        }else if(max1 < max2){
            System.out.println("在此次抽奖过程中,抽奖箱2中产生了最大奖项,该奖项金额为"+max2+"元");
        }else{
            System.out.println("两者的最大奖项是一样的");
        }
    }
}
```







## 2. 原子性

### 2.1 volatile-问题

**代码分析 :** 

```java
package com.itheima.myvolatile;

public class Demo {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        t1.setName("小路同学");
        t1.start();

        MyThread2 t2 = new MyThread2();
        t2.setName("小皮同学");
        t2.start();
    }
}
```

```java
package com.itheima.myvolatile;

public class Money {
    public static int money = 100000;
}
```

```java
package com.itheima.myvolatile;

public class MyThread1 extends  Thread {
    @Override
    public void run() {
        while(Money.money == 100000){

        }

        System.out.println("结婚基金已经不是十万了");
    }
}

```

```java
package com.itheima.myvolatile;

public class MyThread2 extends Thread {
    @Override
    public void run() {
        try {
            Thread.sleep(10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Money.money = 90000;
    }
}

```

**程序问题 :**  女孩虽然知道结婚基金是十万，但是当基金的余额发生变化的时候，女孩无法知道最新的余额。



### 2.2 volatile解决

**以上案例出现的问题 :**

​	当A线程修改了共享数据时，B线程没有及时获取到最新的值，如果还在使用原先的值，就会出现问题 

​	1，堆内存是唯一的，每一个线程都有自己的线程栈。

​	2 ，每一个线程在使用堆里面变量的时候，都会先拷贝一份到变量的副本中。

​	3 ，在线程中，每一次使用是从变量的副本中获取的。

**Volatile关键字 :** 强制线程每次在使用的时候，都会看一下共享区域最新的值

**代码实现 :** **使用volatile关键字解决**

```java
package com.itheima.myvolatile;

public class Demo {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        t1.setName("小路同学");
        t1.start();

        MyThread2 t2 = new MyThread2();
        t2.setName("小皮同学");
        t2.start();
    }
}
```

```java
package com.itheima.myvolatile;

public class Money {
    public static volatile int money = 100000;
}
```

```java
package com.itheima.myvolatile;

public class MyThread1 extends  Thread {
    @Override
    public void run() {
        while(Money.money == 100000){

        }

        System.out.println("结婚基金已经不是十万了");
    }
}

```

```java
package com.itheima.myvolatile;

public class MyThread2 extends Thread {
    @Override
    public void run() {
        try {
            Thread.sleep(10);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Money.money = 90000;
    }
}

```



### 2.3 synchronized解决

**synchronized解决 :** 

​	1 ，线程获得锁

​	2 ，清空变量副本

​	3 ，拷贝共享变量最新的值到变量副本中

​	4 ，执行代码

​	5 ，将修改后变量副本中的值赋值给共享数据

​	6 ，释放锁

**代码实现 :** 

```java
package com.itheima.myvolatile2;

public class Demo {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        t1.setName("小路同学");
        t1.start();

        MyThread2 t2 = new MyThread2();
        t2.setName("小皮同学");
        t2.start();
    }
}
```

```java
package com.itheima.myvolatile2;

public class Money {
    public static Object lock = new Object();
    public static volatile int money = 100000;
}
```

```java
package com.itheima.myvolatile2;

public class MyThread1 extends  Thread {
    @Override
    public void run() {
        while(true){
            synchronized (Money.lock){
                if(Money.money != 100000){
                    System.out.println("结婚基金已经不是十万了");
                    break;
                }
            }
        }
    }
}
```

```java
package com.itheima.myvolatile2;

public class MyThread2 extends Thread {
    @Override
    public void run() {
        synchronized (Money.lock) {
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            Money.money = 90000;
        }
    }
}
```



### 2.4 原子性

**概述 :** 所谓的原子性是指在一次操作或者多次操作中，要么所有的操作全部都得到了执行并且不会受到任何因素的干扰而中断，要么所有的操作都不执行，多个操作是一个不可以分割的整体。

**代码实现 :** 

```java
package com.itheima.threadatom;

public class AtomDemo {
    public static void main(String[] args) {
        MyAtomThread atom = new MyAtomThread();

        for (int i = 0; i < 100; i++) {
            new Thread(atom).start();
        }
    }
}
class MyAtomThread implements Runnable {
    private volatile int count = 0; //送冰淇淋的数量

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            //1,从共享数据中读取数据到本线程栈中.
            //2,修改本线程栈中变量副本的值
            //3,会把本线程栈中变量副本的值赋值给共享数据.
            count++;
            System.out.println("已经送了" + count + "个冰淇淋");
        }
    }
}
```

**代码总结 :** count++ 不是一个原子性操作, 他在执行的过程中,有可能被其他线程打断



### 2.5 volatile关键字不能保证原子性

解决方案 : 我们可以给count++操作添加锁，那么count++操作就是临界区中的代码，临界区中的代码一次只能被一个线程去执行，所以count++就变成了原子操作。

```java
package com.itheima.threadatom2;

public class AtomDemo {
    public static void main(String[] args) {
        MyAtomThread atom = new MyAtomThread();

        for (int i = 0; i < 100; i++) {
            new Thread(atom).start();
        }
    }
}
class MyAtomThread implements Runnable {
    private volatile int count = 0; //送冰淇淋的数量
    private Object lock = new Object();

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            //1,从共享数据中读取数据到本线程栈中.
            //2,修改本线程栈中变量副本的值
            //3,会把本线程栈中变量副本的值赋值给共享数据.
            synchronized (lock) {
                count++;
                System.out.println("已经送了" + count + "个冰淇淋");
            }
        }
    }
}
```



### 2.6 原子性_AtomicInteger

概述：java从JDK1.5开始提供了java.util.concurrent.atomic包(简称Atomic包)，这个包中的原子操作类提供了一种用法简单，性能高效，线程安全地更新一个变量的方式。因为变

量的类型有很多种，所以在Atomic包里一共提供了13个类，属于4种类型的原子更新方式，分别是原子更新基本类型、原子更新数组、原子更新引用和原子更新属性(字段)。本次我们只讲解

使用原子的方式更新基本类型，使用原子的方式更新基本类型Atomic包提供了以下3个类：

AtomicBoolean： 原子更新布尔类型

AtomicInteger：   原子更新整型

AtomicLong：	原子更新长整型

以上3个类提供的方法几乎一模一样，所以本节仅以AtomicInteger为例进行讲解，AtomicInteger的常用方法如下：

```java
public AtomicInteger()：	   			    初始化一个默认值为0的原子型Integer
public AtomicInteger(int initialValue)：  初始化一个指定值的原子型Integer

int get():   			 				获取值
int getAndIncrement():      			 以原子方式将当前值加1，注意，这里返回的是自增前的值。
int incrementAndGet():     				 以原子方式将当前值加1，注意，这里返回的是自增后的值。
int addAndGet(int data):				 以原子方式将输入的数值与实例中的值（AtomicInteger里的value）相加，并返回结果。
int getAndSet(int value):   			 以原子方式设置为newValue的值，并返回旧值。
```

**代码实现 :**

```java
package com.itheima.threadatom3;

import java.util.concurrent.atomic.AtomicInteger;

public class MyAtomIntergerDemo1 {
//    public AtomicInteger()：	               初始化一个默认值为0的原子型Integer
//    public AtomicInteger(int initialValue)： 初始化一个指定值的原子型Integer
    public static void main(String[] args) {
        AtomicInteger ac = new AtomicInteger();
        System.out.println(ac);

        AtomicInteger ac2 = new AtomicInteger(10);
        System.out.println(ac2);
    }

}
```

```java
package com.itheima.threadatom3;

import java.lang.reflect.Field;
import java.util.concurrent.atomic.AtomicInteger;

public class MyAtomIntergerDemo2 {
//    int get():   		 		获取值
//    int getAndIncrement():     以原子方式将当前值加1，注意，这里返回的是自增前的值。
//    int incrementAndGet():     以原子方式将当前值加1，注意，这里返回的是自增后的值。
//    int addAndGet(int data):	 以原子方式将参数与对象中的值相加，并返回结果。
//    int getAndSet(int value):  以原子方式设置为newValue的值，并返回旧值。
    public static void main(String[] args) {
//        AtomicInteger ac1 = new AtomicInteger(10);
//        System.out.println(ac1.get());

//        AtomicInteger ac2 = new AtomicInteger(10);
//        int andIncrement = ac2.getAndIncrement();
//        System.out.println(andIncrement);
//        System.out.println(ac2.get());

//        AtomicInteger ac3 = new AtomicInteger(10);
//        int i = ac3.incrementAndGet();
//        System.out.println(i);//自增后的值
//        System.out.println(ac3.get());

//        AtomicInteger ac4 = new AtomicInteger(10);
//        int i = ac4.addAndGet(20);
//        System.out.println(i);
//        System.out.println(ac4.get());

        AtomicInteger ac5 = new AtomicInteger(100);
        int andSet = ac5.getAndSet(20);
        System.out.println(andSet);
        System.out.println(ac5.get());
    }
}
```



### 2.7 AtomicInteger-内存解析

**AtomicInteger原理 :** 自旋锁  + CAS 算法

**CAS算法：**

​	有3个操作数（内存值V， 旧的预期值A，要修改的值B）

​	当旧的预期值A == 内存值   此时修改成功，将V改为B                 

​	当旧的预期值A！=内存值   此时修改失败，不做任何操作                 

​	并重新获取现在的最新值（这个重新获取的动作就是自旋）

### 2.8 AtomicInteger-源码解析

**代码实现 :**

```java
package com.itheima.threadatom4;

public class AtomDemo {
    public static void main(String[] args) {
        MyAtomThread atom = new MyAtomThread();

        for (int i = 0; i < 100; i++) {
            new Thread(atom).start();
        }
    }
}
```

```java
package com.itheima.threadatom4;

import java.util.concurrent.atomic.AtomicInteger;

public class MyAtomThread implements Runnable {
    //private volatile int count = 0; //送冰淇淋的数量
    //private Object lock = new Object();
    AtomicInteger ac = new AtomicInteger(0);

    @Override
    public void run() {
        for (int i = 0; i < 100; i++) {
            //1,从共享数据中读取数据到本线程栈中.
            //2,修改本线程栈中变量副本的值
            //3,会把本线程栈中变量副本的值赋值给共享数据.
            //synchronized (lock) {
//                count++;
//                ac++;
            int count = ac.incrementAndGet();
            System.out.println("已经送了" + count + "个冰淇淋");
           // }
        }
    }
}

```

**源码解析 :** 

```java
//先自增，然后获取自增后的结果
public final int incrementAndGet() {
        //+ 1 自增后的结果
        //this 就表示当前的atomicInteger（值）
        //1    自增一次
        return U.getAndAddInt(this, VALUE, 1) + 1;
}

public final int getAndAddInt(Object o, long offset, int delta) {
        //v 旧值
        int v;
        //自旋的过程
        do {
            //不断的获取旧值
            v = getIntVolatile(o, offset);
            //如果这个方法的返回值为false，那么继续自旋
            //如果这个方法的返回值为true，那么自旋结束
            //o 表示的就是内存值
            //v 旧值
            //v + delta 修改后的值
        } while (!weakCompareAndSetInt(o, offset, v, v + delta));
            //作用：比较内存中的值，旧值是否相等，如果相等就把修改后的值写到内存中，返回true。表示修改成功。
            //                                 如果不相等，无法把修改后的值写到内存中，返回false。表示修改失败。
            //如果修改失败，那么继续自旋。
        return v;
}
```



### 2.9 悲观锁和乐观锁

**synchronized和CAS的区别 :** 

**相同点：**在多线程情况下，都可以保证共享数据的安全性。

**不同点：**synchronized总是从最坏的角度出发，认为每次获取数据的时候，别人都有可能修改。所以在每                       次操作共享数据之前，都会上锁。（悲观锁）

​	cas是从乐观的角度出发，假设每次获取数据别人都不会修改，所以不会上锁。只不过在修改共享数据的时候，会检查一下，别人有没有修改过这个数据。

​	如果别人修改过，那么我再次获取现在最新的值。            

​	 如果别人没有修改过，那么我现在直接修改共享数据的值.(乐观锁）



## 3. 并发工具类

### 3.1 并发工具类-Hashtable

​	**Hashtable出现的原因 :** 在集合类中HashMap是比较常用的集合对象，但是HashMap是线程不安全的(多线程环境下可能会存在问题)。为了保证数据的安全性我们可以使用Hashtable，但是Hashtable的效率低下。

**代码实现 :** 

```java
package com.itheima.mymap;

import java.util.HashMap;
import java.util.Hashtable;

public class MyHashtableDemo {
    public static void main(String[] args) throws InterruptedException {
        Hashtable<String, String> hm = new Hashtable<>();

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 25; i++) {
                hm.put(i + "", i + "");
            }
        });


        Thread t2 = new Thread(() -> {
            for (int i = 25; i < 51; i++) {
                hm.put(i + "", i + "");
            }
        });

        t1.start();
        t2.start();

        System.out.println("----------------------------");
        //为了t1和t2能把数据全部添加完毕
        Thread.sleep(1000);

        //0-0 1-1 ..... 50- 50

        for (int i = 0; i < 51; i++) {
            System.out.println(hm.get(i + ""));
        }//0 1 2 3 .... 50


    }
}
```



### 3.2 并发工具类-ConcurrentHashMap基本使用

​	**ConcurrentHashMap出现的原因 :** 在集合类中HashMap是比较常用的集合对象，但是HashMap是线程不安全的(多线程环境下可能会存在问题)。为了保证数据的安全性我们可以使用Hashtable，但是Hashtable的效率低下。

基于以上两个原因我们可以使用JDK1.5以后所提供的ConcurrentHashMap。

**体系结构 :** 

![1591168965857](/../img/1591168965857.png)

**总结 :** 

​	1 ，HashMap是线程不安全的。多线程环境下会有数据安全问题

​	2 ，Hashtable是线程安全的，但是会将整张表锁起来，效率低下

​	3，ConcurrentHashMap也是线程安全的，效率较高。     在JDK7和JDK8中，底层原理不一样。

**代码实现 :** 

```java
package com.itheima.mymap;

import java.util.Hashtable;
import java.util.concurrent.ConcurrentHashMap;

public class MyConcurrentHashMapDemo {
    public static void main(String[] args) throws InterruptedException {
        ConcurrentHashMap<String, String> hm = new ConcurrentHashMap<>(100);

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 25; i++) {
                hm.put(i + "", i + "");
            }
        });


        Thread t2 = new Thread(() -> {
            for (int i = 25; i < 51; i++) {
                hm.put(i + "", i + "");
            }
        });

        t1.start();
        t2.start();

        System.out.println("----------------------------");
        //为了t1和t2能把数据全部添加完毕
        Thread.sleep(1000);

        //0-0 1-1 ..... 50- 50

        for (int i = 0; i < 51; i++) {
            System.out.println(hm.get(i + ""));
        }//0 1 2 3 .... 50
    }
}
```



### 3.3 并发工具类-ConcurrentHashMap1.7原理

![1591169254280](/../img/1591169254280.png)

### 3.4 并发工具类-ConcurrentHashMap1.8原理

![1591169338256](/../img/1591169338256.png)

**总结 :** 

​	1，如果使用空参构造创建ConcurrentHashMap对象，则什么事情都不做。     在第一次添加元素的时候创建哈希表

​	2，计算当前元素应存入的索引。

​	3，如果该索引位置为null，则利用cas算法，将本结点添加到数组中。

​	4，如果该索引位置不为null，则利用volatile关键字获得当前位置最新的结点地址，挂在他下面，变成链表。		

​	5，当链表的长度大于等于8时，自动转换成红黑树6，以链表或者红黑树头结点为锁对象，配合悲观锁保证多线程操作集合时数据的安全性

### 3.5 并发工具类-CountDownLatch

**CountDownLatch类 :** 		

| 方法                             | 解释                             |
| -------------------------------- | -------------------------------- |
| public CountDownLatch(int count) | 参数传递线程数，表示等待线程数量 |
| public void await()              | 让线程等待                       |
| public void countDown()          | 当前线程执行完毕                 |

**使用场景：** 让某一条线程等待其他线程执行完毕之后再执行

**代码实现 :** 

```java
package com.itheima.mycountdownlatch;

import java.util.concurrent.CountDownLatch;

public class ChileThread1 extends Thread {

    private CountDownLatch countDownLatch;
    public ChileThread1(CountDownLatch countDownLatch) {
        this.countDownLatch = countDownLatch;
    }

    @Override
    public void run() {
        //1.吃饺子
        for (int i = 1; i <= 10; i++) {
            System.out.println(getName() + "在吃第" + i + "个饺子");
        }
        //2.吃完说一声
        //每一次countDown方法的时候，就让计数器-1
        countDownLatch.countDown();
    }
}

```

```java
package com.itheima.mycountdownlatch;

import java.util.concurrent.CountDownLatch;

public class ChileThread2 extends Thread {

    private CountDownLatch countDownLatch;
    public ChileThread2(CountDownLatch countDownLatch) {
        this.countDownLatch = countDownLatch;
    }
    @Override
    public void run() {
        //1.吃饺子
        for (int i = 1; i <= 15; i++) {
            System.out.println(getName() + "在吃第" + i + "个饺子");
        }
        //2.吃完说一声
        //每一次countDown方法的时候，就让计数器-1
        countDownLatch.countDown();
    }
}

```

```java
package com.itheima.mycountdownlatch;

import java.util.concurrent.CountDownLatch;

public class ChileThread3 extends Thread {

    private CountDownLatch countDownLatch;
    public ChileThread3(CountDownLatch countDownLatch) {
        this.countDownLatch = countDownLatch;
    }
    @Override
    public void run() {
        //1.吃饺子
        for (int i = 1; i <= 20; i++) {
            System.out.println(getName() + "在吃第" + i + "个饺子");
        }
        //2.吃完说一声
        //每一次countDown方法的时候，就让计数器-1
        countDownLatch.countDown();
    }
}

```

```java
package com.itheima.mycountdownlatch;

import java.util.concurrent.CountDownLatch;

public class MotherThread extends Thread {
    private CountDownLatch countDownLatch;
    public MotherThread(CountDownLatch countDownLatch) {
        this.countDownLatch = countDownLatch;
    }

    @Override
    public void run() {
        //1.等待
        try {
            //当计数器变成0的时候，会自动唤醒这里等待的线程。
            countDownLatch.await();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        //2.收拾碗筷
        System.out.println("妈妈在收拾碗筷");
    }
}

```

```java
package com.itheima.mycountdownlatch;

import java.util.concurrent.CountDownLatch;

public class MyCountDownLatchDemo {
    public static void main(String[] args) {
        //1.创建CountDownLatch的对象，需要传递给四个线程。
        //在底层就定义了一个计数器，此时计数器的值就是3
        CountDownLatch countDownLatch = new CountDownLatch(3);
        //2.创建四个线程对象并开启他们。
        MotherThread motherThread = new MotherThread(countDownLatch);
        motherThread.start();

        ChileThread1 t1 = new ChileThread1(countDownLatch);
        t1.setName("小明");

        ChileThread2 t2 = new ChileThread2(countDownLatch);
        t2.setName("小红");

        ChileThread3 t3 = new ChileThread3(countDownLatch);
        t3.setName("小刚");

        t1.start();
        t2.start();
        t3.start();
    }
}
```

**总结 :** 

​	1. CountDownLatch(int count)：参数写等待线程的数量。并定义了一个计数器。

​	2. await()：让线程等待，当计数器为0时，会唤醒等待的线程

​	3. countDown()： 线程执行完毕时调用，会将计数器-1。

### 3.6 并发工具类-Semaphore

**使用场景 :** 

​	可以控制访问特定资源的线程数量。

**实现步骤 :** 

​	1，需要有人管理这个通道

​	2，当有车进来了，发通行许可证

​	3，当车出去了，收回通行许可证

​	4，如果通行许可证发完了，那么其他车辆只能等着

**代码实现 :** 

```java
package com.itheima.mysemaphore;

import java.util.concurrent.Semaphore;

public class MyRunnable implements Runnable {
    //1.获得管理员对象，
    private Semaphore semaphore = new Semaphore(2);
    @Override
    public void run() {
        //2.获得通行证
        try {
            semaphore.acquire();
            //3.开始行驶
            System.out.println("获得了通行证开始行驶");
            Thread.sleep(2000);
            System.out.println("归还通行证");
            //4.归还通行证
            semaphore.release();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

```

```java
package com.itheima.mysemaphore;

public class MySemaphoreDemo {
    public static void main(String[] args) {
        MyRunnable mr = new MyRunnable();

        for (int i = 0; i < 100; i++) {
            new Thread(mr).start();
        }
    }
}
```

# 网络编程：



