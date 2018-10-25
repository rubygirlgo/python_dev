from django.db import models

# Create your models here.
#项目管理数据表
class project_list(models.Model):
    name = models.CharField("名称",max_length=100,blank=False) # 项目名称
    describe = models.TextField("描述") # 项目描述
    status = models.BooleanField("状态",default=True) # 状态
    update_time = models.DateTimeField('更新时间',auto_now=True) # 更新时间（ 自动获取当前时间）
    create_time = models.DateTimeField("创建时间",auto_now=True) # 创建时间（ 自动获取当前时间）

    def __str__(self):
        return self.name


# 模块管理
class module(models.Model):
    project_list = models.ForeignKey(project_list,on_delete=models.CASCADE) # 关联项目 id
    name = models.CharField("名称", max_length=100)  # 模块标题
    describe = models.TextField("描述",blank=True,null=True)  # 模块描述，text字段不需要写最大长度
    create_time = models.DateTimeField("创建时间",auto_now=True) # 创建时间（ 自动获取当前时间）
    def __str__(self):
        return self.name

