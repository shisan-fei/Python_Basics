'''
面向过程和面向对象
面向过程：遇到问题后，分析解决问题之后一步步实现
        需要一步一步完成，一步一步执行
面向对象：分析问题中的抽象模型，创建模型，最后由模型对象完成功能
优缺点：
    面向过程：面向过程的核心就是过程，解决问题步骤
    优点：
        将负责的问题流程化，简单化
    缺点：
        扩展性差（更新，维护迭代）
    适用于完成一些简单的脚本任务
    面向对象：核心是对象，是一个特征和功能的综合体
    优点：
        可扩展性高
    缺点：
        编程复杂度高
'''

'''
面向对象中的名称：
类：
    类是对象的一个抽象
    对象是由类创建的实例
属性：
方法：
实例：
类是由对象总结而来，总结过程就是抽象
对象是由类具体实施出来的，这个过程就是实例化

苹果是一个对象，将苹果和香蕉等水果对象归类就是类。水果
'''

'''
总结：
    一个类可以实例化多个对象，每个对象在内存中是独立的
    当通过类实例化对象时，不会吧类中成员复制一份给对象，而是引用
    访问对象成员时，若对象自己没有成员，对象会去实例化他的类中去找
    对象成员的添加修改，只会影响当前对象自己，不会影响类和其他对象
    删除对象成员时，必须是该对象自己的成员
    对类的成员操作，会影响通过类创建的对象，包括已经创建的。
'''