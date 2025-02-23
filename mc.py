from ursina import *  # 导入Ursina引擎
from ursina.prefabs.first_person_controller import FirstPersonController  # 导入第一人称控制器

# 创建一个游戏应用
app = Ursina()

# 定义方块的类
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',  # 使用立方体模型
            origin_y=0.5,
            texture='white_cube',  # 使用白色纹理
            color=color.color(0, 0, random.uniform(0.9, 1.0)),  # 随机颜色
            highlight_color=color.lime,  # 高亮颜色
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':  # 左键点击放置方块
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':  # 右键点击删除方块
                destroy(self)

# 生成一个地面
for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x, 0, z))

# 添加第一人称控制器
player = FirstPersonController()

# 运行游戏
app.run()